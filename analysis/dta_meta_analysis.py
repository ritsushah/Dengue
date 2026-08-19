#!/usr/bin/env python3
"""
Bivariate random-effects (Reitsma 2005) DTA meta-analysis for FIA dengue NS1.

R/mada is the protocol engine; R is not installed in this environment.
This script implements the same intercept-only Reitsma model:
  y_i = (logit Se_i, logit FPR_i) ~ N(mu, C_i + Psi)
with REML for Psi and GLS for mu. Continuity correction 0.5 is applied to
studies with a zero cell (Cochrane DTA default).

Do not substitute placeholder 2x2 data. Input is the locked extraction CSV.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import norm, t as student_t

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data/extraction/included_2x2_2026-08-19.csv"
FIG_DIR = ROOT / "output/figures"
TAB_DIR = ROOT / "output/tables"
MS_FIG = ROOT / "manuscript/figures"
for d in (FIG_DIR, TAB_DIR, MS_FIG):
    d.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(42)


def logit(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return np.log(p / (1 - p))


def expit(x):
    x = np.clip(x, -20, 20)
    return 1 / (1 + np.exp(-x))


def wilson(x, n, z=1.96):
    if n == 0:
        return (np.nan, np.nan, np.nan)
    p = x / n
    den = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / den
    half = z * math.sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / den
    return p, max(0, centre - half), min(1, centre + half)


def apply_cc(tp, fp, fn, tn, cc=0.5, control="zeros"):
    cells = np.array([tp, fp, fn, tn], dtype=float)
    if control == "all" or (control == "zeros" and np.any(cells == 0)):
        cells = cells + cc
    return cells


def study_yi_ci(row, cc=0.5, control="zeros"):
    tp, fp, fn, tn = apply_cc(row.TP, row.FP, row.FN, row.TN, cc, control)
    se = tp / (tp + fn)
    fpr = fp / (fp + tn)
    y = np.array([logit(se), logit(fpr)])
    c11 = 1 / tp + 1 / fn
    c22 = 1 / fp + 1 / tn
    C = np.diag([c11, c22])
    return y, C, se, 1 - fpr


def unpack_psi(par):
    log_t1, log_t2, zrho = par
    t1 = math.exp(log_t1)
    t2 = math.exp(log_t2)
    rho = math.tanh(zrho)
    Psi = np.array([[t1**2, rho * t1 * t2], [rho * t1 * t2, t2**2]])
    return Psi, t1, t2, rho


def gls_mu(ys, Cs, Psi):
    Wsum = np.zeros((2, 2))
    Wy = np.zeros(2)
    for y, C in zip(ys, Cs):
        V = C + Psi
        W = np.linalg.inv(V)
        Wsum += W
        Wy += W @ y
    mu = np.linalg.solve(Wsum, Wy)
    vcov = np.linalg.inv(Wsum)
    return mu, vcov, Wsum


def reml_nll(par, ys, Cs):
    Psi, _, _, _ = unpack_psi(par)
    # keep Psi PD
    if np.min(np.linalg.eigvalsh(Psi)) < 1e-10:
        return 1e6
    try:
        mu, _, Wsum = gls_mu(ys, Cs, Psi)
    except np.linalg.LinAlgError:
        return 1e6
    ll = 0.0
    sign, logdet_w = np.linalg.slogdet(Wsum)
    if sign <= 0:
        return 1e6
    ll -= 0.5 * logdet_w
    for y, C in zip(ys, Cs):
        V = C + Psi
        sign, logdet = np.linalg.slogdet(V)
        if sign <= 0:
            return 1e6
        resid = y - mu
        ll -= 0.5 * logdet
        ll -= 0.5 * float(resid @ np.linalg.solve(V, resid))
    return -ll


def fit_reitsma(df, cc=0.5, control="zeros"):
    ys, Cs = [], []
    for row in df.itertuples():
        y, C, _, _ = study_yi_ci(row, cc, control)
        ys.append(y)
        Cs.append(C)
    # univariate DL start
    def dl_tau(idx):
        yi = np.array([y[idx] for y in ys])
        vi = np.array([C[idx, idx] for C in Cs])
        w = 1 / vi
        ybar = np.sum(w * yi) / np.sum(w)
        Q = np.sum(w * (yi - ybar) ** 2)
        den = np.sum(w) - np.sum(w**2) / np.sum(w)
        tau2 = max(1e-6, (Q - (len(yi) - 1)) / den) if den > 0 else 1e-6
        return math.sqrt(tau2)

    x0 = np.array([math.log(dl_tau(0)), math.log(dl_tau(1)), 0.0])
    res = minimize(
        reml_nll,
        x0,
        args=(ys, Cs),
        method="L-BFGS-B",
        bounds=[(-8, 3), (-8, 3), (-4, 4)],
    )
    if not res.success:
        res = minimize(reml_nll, x0, args=(ys, Cs), method="Nelder-Mead")
    Psi, t1, t2, rho = unpack_psi(res.x)
    mu, vcov, _ = gls_mu(ys, Cs, Psi)
    return {
        "success": bool(res.success),
        "nll": float(res.fun),
        "mu": mu,
        "vcov": vcov,
        "Psi": Psi,
        "tau_se": t1,
        "tau_fpr": t2,
        "rho": rho,
        "ys": ys,
        "Cs": Cs,
        "k": len(df),
    }


def derived_from_mu(mu):
    se = float(expit(mu[0]))
    fpr = float(expit(mu[1]))
    sp = 1 - fpr
    plr = se / fpr if fpr > 0 else math.inf
    nlr = (1 - se) / sp if sp > 0 else math.inf
    dor = (se / (1 - se)) / (fpr / (1 - fpr)) if 0 < se < 1 and 0 < fpr < 1 else math.inf
    return se, sp, fpr, plr, nlr, dor


def logit_wald_ci(mu, vcov):
    se = expit(mu[0])
    sp = 1 - expit(mu[1])
    se_lo, se_hi = expit(mu[0] + np.array([-1.96, 1.96]) * math.sqrt(vcov[0, 0]))
    fpr_lo, fpr_hi = expit(mu[1] + np.array([-1.96, 1.96]) * math.sqrt(vcov[1, 1]))
    # spec = 1-fpr, so bounds reverse
    sp_lo, sp_hi = 1 - fpr_hi, 1 - fpr_lo
    return {
        "sens": (float(se), float(se_lo), float(se_hi)),
        "spec": (float(sp), float(sp_lo), float(sp_hi)),
    }


def bootstrap_derived(mu, vcov, n=10000):
    draws = RNG.multivariate_normal(mu, vcov, size=n)
    se = expit(draws[:, 0])
    fpr = expit(draws[:, 1])
    sp = 1 - fpr
    plr = se / np.clip(fpr, 1e-12, 1)
    nlr = (1 - se) / np.clip(sp, 1e-12, 1)
    dor = (se / np.clip(1 - se, 1e-12, 1)) / (fpr / np.clip(1 - fpr, 1e-12, 1))
    out = {}
    for name, arr in [
        ("Sensitivity", se),
        ("Specificity", sp),
        ("PLR", plr),
        ("NLR", nlr),
        ("DOR", dor),
    ]:
        out[name] = {
            "estimate": float(np.median(arr)) if name in {"PLR", "NLR", "DOR"} else float(arr.mean()),
            "ci_lower": float(np.quantile(arr, 0.025)),
            "ci_upper": float(np.quantile(arr, 0.975)),
        }
    # point estimates from mu, CIs from bootstrap
    se_p, sp_p, _, plr_p, nlr_p, dor_p = derived_from_mu(mu)
    out["Sensitivity"]["estimate"] = se_p
    out["Specificity"]["estimate"] = sp_p
    out["PLR"]["estimate"] = plr_p
    out["NLR"]["estimate"] = nlr_p
    out["DOR"]["estimate"] = dor_p
    return out


def sroc_curve(mu, Psi, n=400):
    """Regression of logit Se on logit FPR using between-study Psi (Reitsma SROC)."""
    t1 = math.sqrt(Psi[0, 0])
    t2 = math.sqrt(Psi[1, 1])
    rho = Psi[0, 1] / (t1 * t2) if t1 * t2 > 0 else 0
    fpr = np.linspace(0.001, 0.999, n)
    logit_fpr = logit(fpr)
    slope = rho * t1 / t2 if t2 > 0 else 0
    logit_se = mu[0] + slope * (logit_fpr - mu[1])
    return fpr, expit(logit_se)


def auc_from_sroc(mu, Psi):
    fpr, se = sroc_curve(mu, Psi, n=2000)
    # integrate Se with respect to FPR; AUC = int Se d(FPR) is not ROC AUC
    # ROC AUC = int Se d(1-Sp) = int Se d FPR
    return float(np.trapezoid(se, fpr))


def univariate_het(df, measure="sens", cc=0.5):
    yi, vi = [], []
    for row in df.itertuples():
        tp, fp, fn, tn = apply_cc(row.TP, row.FP, row.FN, row.TN, cc, "zeros")
        if measure == "sens":
            p = tp / (tp + fn)
            v = 1 / tp + 1 / fn
        else:
            p = tn / (tn + fp)
            v = 1 / tn + 1 / fp
        yi.append(logit(p))
        vi.append(v)
    yi = np.array(yi)
    vi = np.array(vi)
    w = 1 / vi
    ybar = np.sum(w * yi) / np.sum(w)
    Q = float(np.sum(w * (yi - ybar) ** 2))
    k = len(yi)
    dfq = k - 1
    pval = float(1 - __import__("scipy.stats").stats.chi2.cdf(Q, dfq)) if dfq > 0 else 1.0
    i2 = max(0.0, (Q - dfq) / Q) * 100 if Q > 0 else 0.0
    den = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0.0, (Q - dfq) / den) if den > 0 else 0.0
    return {"Q": Q, "df": dfq, "p": pval, "I2": i2, "tau2": tau2}


def deeks_test(df):
    log_dor, inv_sqrt_ess = [], []
    for row in df.itertuples():
        tp, fp, fn, tn = row.TP + 0.5, row.FP + 0.5, row.FN + 0.5, row.TN + 0.5
        dor = (tp * tn) / (fp * fn)
        n_pos = row.TP + row.FN
        n_neg = row.FP + row.TN
        ess = 4 * n_pos * n_neg / (n_pos + n_neg)
        log_dor.append(math.log(dor))
        inv_sqrt_ess.append(1 / math.sqrt(ess))
    x = np.array(inv_sqrt_ess)
    y = np.array(log_dor)
    X = np.column_stack([np.ones(len(x)), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n = len(x)
    s2 = np.sum(resid**2) / (n - 2)
    cov = s2 * np.linalg.inv(X.T @ X)
    se_slope = math.sqrt(cov[1, 1])
    tstat = beta[1] / se_slope
    p = float(2 * student_t.sf(abs(tstat), df=n - 2))
    return {
        "slope": float(beta[1]),
        "intercept": float(beta[0]),
        "se": se_slope,
        "t": float(tstat),
        "p": p,
        "x": x.tolist(),
        "y": y.tolist(),
        "study": df["study_label"].tolist(),
    }


def style_axes(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)


def plot_forest(df, pooled, path):
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.6), sharey=True)
    labels = df["study_label"].tolist()[::-1]
    y = np.arange(len(df))
    for ax, measure, color in zip(axes, ["sens", "spec"], ["#1f4e79", "#9c2a2a"]):
        xs, lo, hi = [], [], []
        for row in list(df.itertuples())[::-1]:
            if measure == "sens":
                p, a, b = wilson(row.TP, row.TP + row.FN)
            else:
                p, a, b = wilson(row.TN, row.TN + row.FP)
            xs.append(p)
            lo.append(a)
            hi.append(b)
        ax.hlines(y, lo, hi, color=color, lw=1.6)
        ax.plot(xs, y, "o", color=color, ms=6, zorder=3)
        est, clo, chi = pooled[measure]
        ax.axvline(est, color="black", ls="--", lw=0.9, zorder=1)
        ax.fill_betweenx([-0.7, len(df) - 0.3], clo, chi, color=color, alpha=0.12, zorder=0)
        ax.set_xlim(0.35, 1.02)
        ax.set_xlabel("Sensitivity" if measure == "sens" else "Specificity")
        ax.set_yticks(y)
        ax.set_yticklabels(labels)
        ax.set_ylim(-0.8, len(df) - 0.2)
        style_axes(ax)
    axes[0].set_title("Sensitivity", loc="left", fontsize=11)
    axes[1].set_title("Specificity", loc="left", fontsize=11)
    fig.suptitle("FIA for dengue NS1 antigen versus study reference standard", fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_sroc(df, fit, path):
    fig, ax = plt.subplots(figsize=(6.2, 6.2))
    fpr_c, se_c = sroc_curve(fit["mu"], fit["Psi"])
    ax.plot(fpr_c, se_c, color="black", lw=1.8, label="SROC")
    # 95% confidence ellipse on (FPR, Se) from mu vcov via logit transform sampling
    draws = RNG.multivariate_normal(fit["mu"], fit["vcov"], size=4000)
    pts = np.column_stack([expit(draws[:, 1]), expit(draws[:, 0])])
    # convex hull-ish percentile contour: kernel-free ellipse in logit space
    from matplotlib.patches import Ellipse
    # delta-method ellipse in probability space is imperfect; draw logit-space ellipse mapped
    # Use 95% chi2 ellipse on mu then transform a grid
    cov = fit["vcov"]
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    theta = np.linspace(0, 2 * math.pi, 200)
    chi = math.sqrt(5.991)  # 95% df=2
    circle = np.column_stack([np.cos(theta), np.sin(theta)])
    ell = (chi * np.sqrt(vals)) * circle
    ell = ell @ vecs.T + fit["mu"]
    ax.plot(expit(ell[:, 1]), expit(ell[:, 0]), color="#1f4e79", lw=1.1, label="95% confidence region")
    se, sp, fpr, *_ = derived_from_mu(fit["mu"])
    ax.plot(fpr, se, marker="D", color="black", ms=9, label="Summary point", zorder=4)
    for row in df.itertuples():
        npos = row.TP + row.FN
        nneg = row.TN + row.FP
        ax.scatter(
            row.FP / nneg,
            row.TP / npos,
            s=18 + 0.08 * row.N,
            facecolors="white",
            edgecolors="#444",
            lw=1.1,
            zorder=3,
        )
        ax.annotate(
            f"{row.first_author} {row.year}",
            (row.FP / nneg, row.TP / npos),
            textcoords="offset points",
            xytext=(5, 4),
            fontsize=7,
            color="#333",
        )
    ax.set_xlim(0, 0.25)
    ax.set_ylim(0.55, 1.01)
    ax.set_xlabel("False-positive rate (1 − specificity)")
    ax.set_ylabel("Sensitivity")
    ax.set_title("HSROC / bivariate SROC — FIA for dengue NS1")
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_deeks(deeks, path):
    fig, ax = plt.subplots(figsize=(6.0, 5.4))
    x = np.array(deeks["x"])
    y = np.array(deeks["y"])
    ax.scatter(x, y, s=42, c="#1f4e79", zorder=3)
    for xi, yi, lab in zip(x, y, deeks["study"]):
        ax.annotate(lab, (xi, yi), textcoords="offset points", xytext=(5, 3), fontsize=7)
    xx = np.linspace(x.min() * 0.9, x.max() * 1.1, 50)
    ax.plot(xx, deeks["intercept"] + deeks["slope"] * xx, color="#9c2a2a", lw=1.4)
    ax.set_xlabel(r"$1 / \sqrt{\mathrm{ESS}}$")
    ax.set_ylabel("ln(DOR)")
    ax.set_title(f"Deeks' funnel plot  (slope p = {deeks['p']:.3f})")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_quadas(judgments, path_tl, path_sum):
    studies = [j["study"] for j in judgments]
    domains = ["D1 Patient selection", "D2 Index test", "D3 Reference standard", "D4 Flow & timing", "Overall"]
    keys = ["D1", "D2", "D3", "D4", "Overall"]
    colors = {"Low": "#3b7d4f", "Unclear": "#e1b12c", "High": "#c0392b"}
    fig, ax = plt.subplots(figsize=(8.8, 3.4 + 0.28 * len(studies)))
    for i, j in enumerate(judgments):
        for k, key in enumerate(keys):
            ax.scatter(k, len(studies) - 1 - i, s=220, c=colors[j[key]], zorder=3)
    ax.set_xticks(range(5))
    ax.set_xticklabels(domains, rotation=18, ha="right")
    ax.set_yticks(range(len(studies)))
    ax.set_yticklabels(list(reversed(studies)))
    ax.set_xlim(-0.6, 4.6)
    ax.set_ylim(-0.6, len(studies) - 0.4)
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    handles = [mpatches.Patch(color=c, label=l) for l, c in colors.items()]
    ax.legend(handles=handles, frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3)
    ax.set_title("QUADAS-2 risk of bias", pad=22)
    fig.tight_layout()
    fig.savefig(path_tl, dpi=300, bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    y = np.arange(len(keys))[::-1]
    lows, highs, uns = [], [], []
    for key in keys:
        vals = [j[key] for j in judgments]
        lows.append(100 * vals.count("Low") / len(vals))
        highs.append(100 * vals.count("High") / len(vals))
        uns.append(100 * vals.count("Unclear") / len(vals))
    ax.barh(y, lows, color=colors["Low"], label="Low")
    ax.barh(y, uns, left=lows, color=colors["Unclear"], label="Unclear")
    ax.barh(y, highs, left=np.array(lows) + np.array(uns), color=colors["High"], label="High")
    ax.set_yticks(y)
    ax.set_yticklabels(domains)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Percentage of studies")
    ax.legend(frameon=False, loc="lower right")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(path_sum, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_prisma(path):
    fig, ax = plt.subplots(figsize=(10.5, 8.4))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    def box(x, y, w, h, text, fc="#f4f4f4"):
        rec = mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.3,rounding_size=0.8",
            linewidth=0.8, edgecolor="#222", facecolor=fc,
        )
        ax.add_patch(rec)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7.4, wrap=True)

    box(6, 86, 40, 10, "Records identified from databases\nPubMed 423 · Embase 959 · WoS 432 · ScienceDirect 75\nTotal = 1,889", "#e8f1fa")
    box(54, 86, 40, 10, "Additional records\nCochrane CENTRAL 10 · Scholar 100\nClinicalTrials.gov 22 · Europe PMC preprints 66\nScoping (Ghogre 2021; Pohekar 2017)", "#e8f1fa")
    box(6, 70, 40, 9, "Duplicates removed from bibliographic set\nn = 807", "#fdecea")
    box(6, 54, 40, 10, "Unique bibliographic records\nn = 1,082\n(Scopus not searched)", "#e8f1fa")
    box(54, 54, 40, 10, "FIA-term title/field filter\nn = 10 flagged\n+ Zapata 2026 (unique set, FIA in full text)\n+ 2 scoping papers not in the 1,082", "#fff6e0")
    box(6, 36, 40, 10, "Not dual-screened (ELISA-dominant unique set)\nn = 1,072\nProtocol deviation: no dual independent\nscreening of the full unique set", "#fdecea")
    box(54, 36, 40, 10, "Full texts assessed for eligibility\nn = 13", "#e8f1fa")
    box(6, 16, 40, 14, "Full-text exclusions n = 8\n· Experimental/analytical platform 2\n· Correspondence 1\n· Wrong index test 2\n· No reconstructable NS1 2×2  2\n· Conference abstract without cells 1", "#fdecea")
    box(54, 16, 40, 14, "Included in qualitative synthesis n = 6\n(5 quantitative + Pohekar 2023 narrative)\n\nIncluded in bivariate meta-analysis\nn = 5 studies (794 specimens)", "#e7f6ea")
    ax.annotate("", xy=(26, 79), xytext=(26, 86), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(26, 64), xytext=(26, 70), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(26, 46), xytext=(26, 54), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(54, 59), xytext=(46, 59), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(74, 46), xytext=(74, 54), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(54, 41), xytext=(46, 41), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(26, 30), xytext=(26, 36), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.annotate("", xy=(74, 30), xytext=(74, 36), arrowprops=dict(arrowstyle="->", color="#222"))
    ax.set_title("Figure 1. PRISMA 2020 flow diagram (search date 19 August 2026)", fontsize=11, pad=8)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def fmt_pct(x):
    return f"{100 * x:.1f}%"


def main():
    df = pd.read_csv(CSV)
    df["study_label"] = df["first_author"] + " " + df["year"].astype(str)
    df["N_check"] = df["TP"] + df["FP"] + df["FN"] + df["TN"]
    assert list(df["N_check"]) == list(df["N"])

    # individual estimates (no CC)
    rows = []
    for r in df.itertuples():
        se, slo, shi = wilson(r.TP, r.TP + r.FN)
        sp, plo, phi = wilson(r.TN, r.TN + r.FP)
        ppv = r.TP / (r.TP + r.FP) if (r.TP + r.FP) else np.nan
        npv = r.TN / (r.TN + r.FN) if (r.TN + r.FN) else np.nan
        plr = se / (1 - sp) if sp < 1 else np.inf
        nlr = (1 - se) / sp if sp > 0 else np.inf
        dor = (r.TP * r.TN) / (r.FP * r.FN) if r.FP * r.FN else np.inf
        rows.append(
            {
                "study": r.study_label,
                "N": int(r.N),
                "TP": int(r.TP),
                "FP": int(r.FP),
                "FN": int(r.FN),
                "TN": int(r.TN),
                "sens": se,
                "sens_lo": slo,
                "sens_hi": shi,
                "spec": sp,
                "spec_lo": plo,
                "spec_hi": phi,
                "ppv": ppv,
                "npv": npv,
                "plr": plr,
                "nlr": nlr,
                "dor": dor,
            }
        )
    ind = pd.DataFrame(rows)

    fit = fit_reitsma(df)
    wald = logit_wald_ci(fit["mu"], fit["vcov"])
    boot = bootstrap_derived(fit["mu"], fit["vcov"])
    auc = auc_from_sroc(fit["mu"], fit["Psi"])
    # AUC CI: bootstrap mu
    draws = RNG.multivariate_normal(fit["mu"], fit["vcov"], size=3000)
    auc_draws = [auc_from_sroc(m, fit["Psi"]) for m in draws]
    het_se = univariate_het(df, "sens")
    het_sp = univariate_het(df, "spec")
    deeks = deeks_test(df)

    # leave-one-out
    loo = []
    for i, lab in enumerate(df["study_label"]):
        sub = df.drop(df.index[i]).reset_index(drop=True)
        f = fit_reitsma(sub)
        se, sp, *_ = derived_from_mu(f["mu"])
        loo.append({"excluded": lab, "sens": se, "spec": sp, "auc": auc_from_sroc(f["mu"], f["Psi"])})

    # continuity / method sensitivity
    sens_tbl = []
    for name, kwargs in [
        ("Primary (zeros-only CC 0.5)", {"cc": 0.5, "control": "zeros"}),
        ("CC 0.5 applied to all cells", {"cc": 0.5, "control": "all"}),
        ("CC 0.1 (zeros-only)", {"cc": 0.1, "control": "zeros"}),
        ("CC 1.0 (zeros-only)", {"cc": 1.0, "control": "zeros"}),
    ]:
        f = fit_reitsma(df, **kwargs)
        se, sp, *_ = derived_from_mu(f["mu"])
        sens_tbl.append({"analysis": name, "k": f["k"], "sens": se, "spec": sp})

    # exploratory subsets
    subsets = {
        "STANDARD F only": df[df.fia_brand == "STANDARD F"],
        "QUANTI CARD only": df[df.fia_brand == "QUANTI CARD"],
        "Independent/composite reference (not ELISA-only)": df[df.ref_tier != "Tier 4"],
        "Documented fever ≤7 days": df[df.first_author.isin(["Chaiyo", "Zapata-de la Cruz"])],
        "Exclude High overall RoB": df[df.first_author.isin(["Zapata-de la Cruz", "Ghogre"])],
    }
    subset_out = []
    for name, sub in subsets.items():
        sub = sub.reset_index(drop=True)
        if len(sub) < 3:
            se_list = []
            for r in sub.itertuples():
                se_list.append(
                    {
                        "study": f"{r.first_author} {r.year}",
                        "sens": r.TP / (r.TP + r.FN),
                        "spec": r.TN / (r.TN + r.FP),
                    }
                )
            subset_out.append({"analysis": name, "k": len(sub), "pooled": None, "individual": se_list})
            continue
        f = fit_reitsma(sub)
        se, sp, *_ = derived_from_mu(f["mu"])
        w = logit_wald_ci(f["mu"], f["vcov"])
        subset_out.append(
            {
                "analysis": name,
                "k": len(sub),
                "pooled": {
                    "sens": se,
                    "sens_lo": w["sens"][1],
                    "sens_hi": w["sens"][2],
                    "spec": sp,
                    "spec_lo": w["spec"][1],
                    "spec_hi": w["spec"][2],
                },
            }
        )

    quadas = [
        {"study": "Chaiyo 2022", "D1": "High", "D2": "Unclear", "D3": "Low", "D4": "Low", "Overall": "High"},
        {"study": "Zapata-de la Cruz 2026", "D1": "Low", "D2": "Unclear", "D3": "Low", "D4": "Low", "Overall": "Unclear"},
        {"study": "Ghogre 2021", "D1": "Unclear", "D2": "Unclear", "D3": "Unclear", "D4": "Low", "Overall": "Unclear"},
        {"study": "Zuroidah 2022", "D1": "High", "D2": "Unclear", "D3": "High", "D4": "Low", "Overall": "High"},
        {"study": "Pohekar 2017", "D1": "High", "D2": "Unclear", "D3": "Unclear", "D4": "High", "Overall": "High"},
    ]

    se, sp, fpr, plr, nlr, dor = derived_from_mu(fit["mu"])
    results = {
        "k": int(fit["k"]),
        "N": int(df.N.sum()),
        "dengue_positive": int((df.TP + df.FN).sum()),
        "dengue_negative": int((df.FP + df.TN).sum()),
        "pooled": {
            "sensitivity": {"est": se, "lo": wald["sens"][1], "hi": wald["sens"][2]},
            "specificity": {"est": sp, "lo": wald["spec"][1], "hi": wald["spec"][2]},
            "plr": boot["PLR"],
            "nlr": boot["NLR"],
            "dor": boot["DOR"],
            "auc": {"est": auc, "lo": float(np.quantile(auc_draws, 0.025)), "hi": float(np.quantile(auc_draws, 0.975))},
        },
        "bootstrap": boot,
        "wald": wald,
        "het_sens": het_se,
        "het_spec": het_sp,
        "rho": fit["rho"],
        "tau_logit_se": fit["tau_se"],
        "tau_logit_fpr": fit["tau_fpr"],
        "Psi": fit["Psi"].tolist(),
        "mu": fit["mu"].tolist(),
        "vcov": fit["vcov"].tolist(),
        "deeks": {k: deeks[k] for k in ("slope", "se", "t", "p")},
        "loo": loo,
        "sensitivity_analyses": sens_tbl,
        "subsets": subset_out,
        "engine": "Python Reitsma REML (R/mada unavailable in this runtime)",
        "correction": "0.5 added to all four cells of studies with a zero cell",
    }

    ind.to_csv(TAB_DIR / "individual_study_estimates.csv", index=False)
    pd.DataFrame(loo).to_csv(TAB_DIR / "leave_one_out_results.csv", index=False)
    with open(TAB_DIR / "pooled_estimates.json", "w") as f:
        json.dump(results, f, indent=2)

    pooled_tuple = {
        "sens": (se, wald["sens"][1], wald["sens"][2]),
        "spec": (sp, wald["spec"][1], wald["spec"][2]),
    }
    plot_forest(df, pooled_tuple, FIG_DIR / "coupled_forest_fia.png")
    plot_sroc(df, fit, FIG_DIR / "sroc_fia.png")
    plot_deeks(deeks, FIG_DIR / "deeks_funnel.png")
    plot_quadas(quadas, FIG_DIR / "quadas2_traffic_light.png", FIG_DIR / "quadas2_summary.png")
    plot_prisma(FIG_DIR / "prisma_flow.png")
    for name in [
        "coupled_forest_fia.png",
        "sroc_fia.png",
        "deeks_funnel.png",
        "quadas2_traffic_light.png",
        "quadas2_summary.png",
        "prisma_flow.png",
    ]:
        src = FIG_DIR / name
        dst = MS_FIG / name
        dst.write_bytes(src.read_bytes())

    print("====== FIA dengue NS1 bivariate meta-analysis ======")
    print(f"k={fit['k']}  N={results['N']}  DENV+={results['dengue_positive']}  DENV-={results['dengue_negative']}")
    print(f"Pooled Se {fmt_pct(se)} ({fmt_pct(wald['sens'][1])}–{fmt_pct(wald['sens'][2])})")
    print(f"Pooled Sp {fmt_pct(sp)} ({fmt_pct(wald['spec'][1])}–{fmt_pct(wald['spec'][2])})")
    print(f"PLR {plr:.2f} ({boot['PLR']['ci_lower']:.2f}–{boot['PLR']['ci_upper']:.2f})")
    print(f"NLR {nlr:.3f} ({boot['NLR']['ci_lower']:.3f}–{boot['NLR']['ci_upper']:.3f})")
    print(f"DOR {dor:.1f} ({boot['DOR']['ci_lower']:.1f}–{boot['DOR']['ci_upper']:.1f})")
    print(f"SROC AUC {auc:.3f} ({np.quantile(auc_draws,0.025):.3f}–{np.quantile(auc_draws,0.975):.3f})")
    print(f"I2 Se {het_se['I2']:.1f}%  I2 Sp {het_sp['I2']:.1f}%  rho {fit['rho']:.3f}")
    print(f"Deeks p={deeks['p']:.4f}")
    print("Leave-one-out:")
    for row in loo:
        print(f"  drop {row['excluded']}: Se {fmt_pct(row['sens'])}  Sp {fmt_pct(row['spec'])}")
    print("Wrote output/tables and output/figures; copied figures to manuscript/figures")


if __name__ == "__main__":
    main()
