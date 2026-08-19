#!/usr/bin/env python3
"""Deduplicate bibliographic records for the 19 August 2026 search.

Matching order (first hit wins):
1. DOI (normalized)
2. PMID
3. Normalized title + year

Bibliographic order: PubMed, then Embase, then Web of Science, then ScienceDirect.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path("/Users/subasah/Desktop/Ritu-meta-analysis")
SEARCH_DATE = "2026-08-19"

STOP = re.compile(r"[^a-z0-9]+")


def norm_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = d.strip().rstrip(".")
    return d or None


def norm_title(title: str | None) -> str | None:
    if not title:
        return None
    t = title.lower()
    t = re.sub(r"<[^>]+>", " ", t)
    t = STOP.sub(" ", t).strip()
    t = re.sub(r"\s+", " ", t)
    return t or None


def year_of(val) -> str | None:
    if val is None:
        return None
    m = re.search(r"(19|20)\d{2}", str(val))
    return m.group(0) if m else None


def load_pubmed() -> list[dict]:
    path = ROOT / "data" / "raw" / "pubmed" / f"pubmed_esummary_{SEARCH_DATE}.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        out.append(
            {
                "source": "pubmed",
                "pmid": str(r.get("pmid") or "").strip() or None,
                "doi": norm_doi(r.get("doi")),
                "title": (r.get("title") or "").strip(),
                "year": year_of(r.get("pubdate")),
                "journal": r.get("source"),
                "authors": r.get("authors") or [],
                "pui": None,
                "ut": None,
            }
        )
    return out


def load_embase() -> list[dict]:
    path = ROOT / "data" / "raw" / "embase" / f"embase_records_{SEARCH_DATE}.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        pmid = str(r.get("pmid") or "").strip() or None
        out.append(
            {
                "source": "embase",
                "pmid": pmid,
                "doi": norm_doi(r.get("doi")),
                "title": (r.get("title") or "").strip(),
                "year": year_of(r.get("year")),
                "journal": r.get("journal"),
                "authors": r.get("authors") or [],
                "pui": r.get("pui"),
                "ut": None,
            }
        )
    return out


def load_wos() -> list[dict]:
    path = ROOT / "data" / "raw" / "wos" / f"wos_records_{SEARCH_DATE}.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        out.append(
            {
                "source": "web_of_science",
                "pmid": str(r.get("pmid") or "").strip() or None,
                "doi": norm_doi(r.get("doi")),
                "title": (r.get("title") or "").strip(),
                "year": year_of(r.get("year")),
                "journal": r.get("journal"),
                "authors": r.get("authors") or [],
                "pui": None,
                "ut": r.get("ut"),
                "pii": None,
            }
        )
    return out


def load_sciencedirect() -> list[dict]:
    path = ROOT / "data" / "raw" / "sciencedirect" / f"sciencedirect_records_{SEARCH_DATE}.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        out.append(
            {
                "source": "sciencedirect",
                "pmid": None,
                "doi": norm_doi(r.get("doi")),
                "title": (r.get("title") or "").strip(),
                "year": year_of(r.get("year")),
                "journal": r.get("journal"),
                "authors": r.get("authors") or [],
                "pui": None,
                "ut": None,
                "pii": r.get("pii"),
            }
        )
    return out


def load_cochrane() -> list[dict]:
    path = ROOT / "data" / "raw" / "cochrane" / f"cochrane_records_{SEARCH_DATE}.json"
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for r in raw:
        out.append(
            {
                "source": "cochrane_central",
                "pmid": None,
                "doi": norm_doi(r.get("doi")),
                "title": (r.get("title") or "").strip(),
                "year": year_of(r.get("year")),
                "journal": r.get("journal"),
                "authors": r.get("authors") or [],
                "pui": None,
                "ut": None,
                "pii": None,
                "cn": r.get("cn"),
            }
        )
    return out


def load_grey() -> list[dict]:
    out = []
    ct = ROOT / "data" / "raw" / "grey" / f"clinicaltrials_{SEARCH_DATE}.json"
    if ct.exists():
        for r in json.loads(ct.read_text(encoding="utf-8")):
            out.append(
                {
                    "source": "clinicaltrials_gov",
                    "pmid": None,
                    "doi": None,
                    "title": (r.get("title") or "").strip(),
                    "year": None,
                    "journal": None,
                    "authors": [],
                    "pui": None,
                    "ut": None,
                    "nct": r.get("nct"),
                }
            )
    epmc = ROOT / "data" / "raw" / "grey" / f"europepmc_preprints_{SEARCH_DATE}.json"
    if epmc.exists():
        for r in json.loads(epmc.read_text(encoding="utf-8")):
            doi = r.get("doi") or r.get("DOI")
            pmid = r.get("pmid")
            out.append(
                {
                    "source": "europepmc_preprints",
                    "pmid": str(pmid).strip() if pmid else None,
                    "doi": norm_doi(doi),
                    "title": (r.get("title") or "").strip(),
                    "year": year_of(r.get("pubYear") or r.get("firstPublicationDate")),
                    "journal": r.get("journalTitle"),
                    "authors": [],
                    "pui": None,
                    "ut": None,
                    "pmcid": r.get("pmcid"),
                }
            )
    return out


def dedup(records: list[dict]) -> tuple[list[dict], dict]:
    by_doi: dict[str, int] = {}
    by_pmid: dict[str, int] = {}
    by_ty: dict[tuple[str, str | None], int] = {}
    unique: list[dict] = []
    removed = []
    source_dup = {}

    def keep(rec: dict, reason: str | None = None, match_idx: int | None = None):
        rec = dict(rec)
        rec["duplicate_of"] = None
        rec["match_reason"] = None
        rec["sources"] = [rec["source"]]
        unique.append(rec)
        idx = len(unique) - 1
        if rec.get("doi"):
            by_doi[rec["doi"]] = idx
        if rec.get("pmid"):
            by_pmid[rec["pmid"]] = idx
        nt = norm_title(rec.get("title"))
        if nt:
            by_ty[(nt, rec.get("year"))] = idx
        return idx

    for rec in records:
        src = rec["source"]
        doi = rec.get("doi")
        pmid = rec.get("pmid")
        nt = norm_title(rec.get("title"))
        hit = None
        reason = None
        if doi and doi in by_doi:
            hit, reason = by_doi[doi], "doi"
        elif pmid and pmid in by_pmid:
            hit, reason = by_pmid[pmid], "pmid"
        elif nt and (nt, rec.get("year")) in by_ty:
            hit, reason = by_ty[(nt, rec.get("year"))], "title_year"
        elif nt:
            title_hits = [idx for (t, _y), idx in by_ty.items() if t == nt]
            if title_hits:
                hit, reason = title_hits[0], "title"
        if hit is None:
            keep(rec)
            continue
        unique[hit]["sources"] = sorted(set(unique[hit]["sources"] + [src]))
        if doi and not unique[hit].get("doi"):
            unique[hit]["doi"] = doi
            by_doi[doi] = hit
        if pmid and not unique[hit].get("pmid"):
            unique[hit]["pmid"] = pmid
            by_pmid[pmid] = hit
        if rec.get("pui") and not unique[hit].get("pui"):
            unique[hit]["pui"] = rec.get("pui")
        if rec.get("ut") and not unique[hit].get("ut"):
            unique[hit]["ut"] = rec.get("ut")
        if rec.get("pii") and not unique[hit].get("pii"):
            unique[hit]["pii"] = rec.get("pii")
        removed.append({"from": src, "reason": reason, "title": rec.get("title"), "doi": doi, "pmid": pmid})
        source_dup[src] = source_dup.get(src, 0) + 1

    stats = {
        "input_n": len(records),
        "unique_n": len(unique),
        "duplicates_removed": len(removed),
        "duplicates_by_source": source_dup,
        "by_reason": {},
    }
    for r in removed:
        stats["by_reason"][r["reason"]] = stats["by_reason"].get(r["reason"], 0) + 1
    return unique, stats


def write_unique_csv(path: Path, rows: list[dict]) -> None:
    fields = ["sources", "pmid", "doi", "pui", "ut", "pii", "title", "year", "journal"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(
                {
                    "sources": "|".join(r.get("sources") or [r["source"]]),
                    "pmid": r.get("pmid") or "",
                    "doi": r.get("doi") or "",
                    "pui": r.get("pui") or "",
                    "ut": r.get("ut") or "",
                    "pii": r.get("pii") or "",
                    "title": r.get("title") or "",
                    "year": r.get("year") or "",
                    "journal": r.get("journal") or "",
                }
            )


def main() -> None:
    pubmed = load_pubmed()
    embase = load_embase()
    wos = load_wos()
    sd = load_sciencedirect()
    cochrane = load_cochrane()
    grey = load_grey()
    bib_pm_em = pubmed + embase
    unique_pm_em, stats_pm_em = dedup(bib_pm_em)
    bib_wos = pubmed + embase + wos
    unique_wos, stats_wos = dedup(bib_wos)
    bib = pubmed + embase + wos + sd
    unique_bib, stats_bib = dedup(bib)
    unique_all, stats_all = dedup(bib + grey + cochrane)

    out_dir = ROOT / "data" / "deduped"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"unique_pubmed_embase_{SEARCH_DATE}.json").write_text(
        json.dumps(unique_pm_em, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_unique_csv(out_dir / f"unique_pubmed_embase_{SEARCH_DATE}.csv", unique_pm_em)
    (out_dir / f"unique_pubmed_embase_wos_{SEARCH_DATE}.json").write_text(
        json.dumps(unique_wos, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_unique_csv(out_dir / f"unique_pubmed_embase_wos_{SEARCH_DATE}.csv", unique_wos)
    (out_dir / f"unique_pubmed_embase_wos_sd_{SEARCH_DATE}.json").write_text(
        json.dumps(unique_bib, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_unique_csv(out_dir / f"unique_pubmed_embase_wos_sd_{SEARCH_DATE}.csv", unique_bib)

    report = {
        "search_date": SEARCH_DATE,
        "identified": {
            "pubmed": len(pubmed),
            "embase": len(embase),
            "web_of_science": len(wos),
            "web_of_science_records_in_file": len(wos),
            "sciencedirect": len(sd),
            "cochrane_central": len(cochrane),
            "clinicaltrials_gov": sum(1 for x in grey if x["source"] == "clinicaltrials_gov"),
            "europepmc_preprints": sum(1 for x in grey if x["source"] == "europepmc_preprints"),
        },
        "bibliographic_pubmed_embase": stats_pm_em,
        "bibliographic_pubmed_embase_wos": stats_wos,
        "bibliographic_pubmed_embase_wos_sd": stats_bib,
        "bibliographic_plus_grey": stats_all,
        "note": (
            "Duplicates were removed among retrieved PubMed, Embase, Web of Science, and ScienceDirect records. "
            "Cochrane CENTRAL (10 trials; 0 CDSR reviews) is a supplementary harvest. "
            "unique_screened for PRISMA is not closed: Google Scholar remains a supplementary harvest and is not merged."
        ),
    }
    (ROOT / "data" / "logs" / f"dedup_{SEARCH_DATE}.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
