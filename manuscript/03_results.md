# 3. RESULTS

> **STATUS:** This Results section is a complete, journal-ready *scaffold*. All numeric estimates, study counts, and domain percentages are **placeholders** marked `[TO BE FILLED]`. No pooled diagnostic accuracy parameters have been invented. After dual-reviewer screening, extraction, QUADAS-2 assessment, and execution of `analysis/dta_meta_analysis.R`, replace every `[TO BE FILLED]` token, complete the tables, and insert the generated figures.
>
> **Integration sources:** `data/extraction_template.md` (study-level 2×2 and characteristics) → `analysis/dta_meta_analysis.R` (`output/tables/*.csv`, `output/figures/*.pdf`) → this file.
>
> This section maps to **PRISMA-DTA items 17–23**.

---

## 3.1 Study Selection

The electronic search was executed on **[SEARCH DATE: DD Month 2026]** and updated on **[UPDATE DATE, or “not applicable”]**. Database-specific hit counts are summarized in Table 1.

**Table 1. Records retrieved by information source**

| Source | Platform / interface | Records identified (n) |
|--------|----------------------|------------------------|
| PubMed/MEDLINE | PubMed | `[n]` |
| Embase | Embase.com / Ovid | `[n]` |
| Web of Science Core Collection | Clarivate Advanced Search | `[n]` |
| Scopus | Elsevier | `[n]` |
| ScienceDirect | Elsevier `tak()` | `[n]` |
| Cochrane Library (CDSR + CENTRAL) | Cochrane | `[n]` |
| Google Scholar (first 200, relevance) | scholar.google.com | `[n]` |
| ClinicalTrials.gov / WHO ICTRP | Trial registries | `[n]` |
| ProQuest Dissertations & Theses | ProQuest | `[n]` |
| medRxiv / bioRxiv | Preprint servers | `[n]` |
| Citation tracking (backward / forward) | — | `[n]` |
| Manufacturer IFUs / WHO IRIS | Grey literature | `[n]` |
| **Total before deduplication** | | **`[N_total]`** |
| Duplicates removed | | `[n_dup]` |
| **Unique records screened** | | **`[N_unique]`** |

### 3.1.1 PRISMA 2020 Flow (Figure 1)

**Identification**
- Records identified from databases and registers: `[N_total]`
- Duplicate records removed: `[n_dup]`
- Records marked as ineligible by automation tools: `[n]` (if used; otherwise 0)
- Records removed for other reasons: `[n]`

**Screening**
- Unique records screened at title/abstract: `[N_unique]`
- Records excluded at title/abstract: `[n_ta_excl]`
- Reports sought for retrieval: `[n_sought]`
- Reports not retrieved: `[n_not_retrieved]`

**Eligibility**
- Full-text reports assessed for eligibility: `[n_ft]`
- Full-text reports excluded, with reasons: `[n_ft_excl]`
  - Wrong population (not acute dengue / fever >7 days only / asymptomatic screening): `[n]`
  - Wrong index test (visual ICT only; NS1 not disaggregable; non-FIA fluorescence methods): `[n]`
  - 2×2 table not extractable and not reconstructable: `[n]`
  - Wrong target condition or no clinical validation cohort: `[n]`
  - Duplicate overlapping dataset: `[n]`
  - Other (specify): `[n]`

**Inclusion**
- Studies included in the qualitative synthesis: **`[k_qual]`**
- Studies included in the quantitative meta-analysis (FIA vs. reference): **`[k_fia]`**
- Studies contributing paired FIA–ELISA head-to-head data: **`[k_h2h]`**

Inter-rater agreement was **κ = [x.xx]** at title/abstract screening and **κ = [x.xx]** at full-text screening (**[interpretation: substantial / almost perfect]**). Disagreements were resolved by discussion in `[n]` instances and by third-reviewer adjudication in `[n]` instances. Corresponding authors were contacted for `[n]` studies; `[n]` provided additional 2×2 data.

**Figure 1.** PRISMA 2020 flow diagram of study identification, screening, eligibility, and inclusion. *[Insert figure generated from the counts above; template: PRISMA 2020 flow diagram, http://www.prisma-statement.org]*

---

## 3.2 Study Characteristics and Demographics

### 3.2.1 Overview of the Evidence Base

`[k_qual]` studies published between **[year_min]** and **[year_max]** met eligibility criteria and contributed data on **[N_patients]** unique participants (**[n_dengue+]** dengue-positive and **[n_dengue−]** dengue-negative by the study reference standard; overall dengue prevalence **[xx.x%]**). `[k_fia]` studies provided extractable 2×2 tables for FIA versus a reference standard and entered the primary bivariate model. `[k_h2h]` studies evaluated FIA and ELISA on the same specimens.

Study designs comprised `[n]` prospective cross-sectional or cohort evaluations, `[n]` retrospective diagnostic accuracy studies, and `[n]` `[other: nested surveillance / case-control — specify]`. Settings were predominantly `[hospital inpatient / mixed inpatient–outpatient / emergency / sentinel surveillance]`. `[n]` studies were multicenter.

**Table 2. Characteristics of included studies**

| Study ID | Country / region | Design & setting | N | Fever days (mean/median, range) | Primary / secondary (n) | Serotypes reported | FIA brand (reader) | ELISA brand (if tested) | Reference standard | Specimen |
|----------|------------------|------------------|---|--------------------------------|-------------------------|--------------------|--------------------|-------------------------|--------------------|----------|
| `[Author, Year]` | `[Country]` | `[Prospective / Retrospective]; [Inpt / Outpt / Mixed]` | `[n]` | `[e.g., 3 (1–7)]` | `[P: n / S: n / NR]` | `[DENV-1–4 or NR]` | `[STANDARD F / QUANTI CARD / other]` | `[Platelia / Panbio / STANDARD E / NR]` | `[RT-PCR / ELISA / Composite]` | `[Serum / Plasma / WB]` |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| **Total** | **`[k]` countries** | | **`[N]`** | | | | | | | |

*NR = not reported; WB = whole blood. Full extraction fields are in Supplementary Table S3.*

### 3.2.2 Geographical Distribution

Included studies originated from **`[k_countries]`** countries across **`[k_regions]`** WHO regions (Figure 2):

| WHO / analytic region | Studies (k) | Participants (n) | Predominant serotype(s) if reported |
|-----------------------|-------------|------------------|-------------------------------------|
| South Asia | `[k]` | `[n]` | `[DENV-x]` |
| Southeast Asia | `[k]` | `[n]` | `[DENV-x]` |
| Western Pacific | `[k]` | `[n]` | `[DENV-x]` |
| Latin America / Caribbean | `[k]` | `[n]` | `[DENV-x]` |
| Africa | `[k]` | `[n]` | `[DENV-x]` |
| Eastern Mediterranean | `[k]` | `[n]` | `[DENV-x]` |
| Other / multi-region | `[k]` | `[n]` | `[DENV-x]` |

**Figure 2.** Geographic distribution of included studies (bubble size proportional to sample size). *[Insert map after extraction.]*

### 3.2.3 Population Demographics

- **Age:** `[n]` studies enrolled mixed ages; `[n]` were pediatric-only (≤18 years); `[n]` were adult-only. Across studies reporting a central estimate, median/mean age ranged from **`[x]`** to **`[y]`** years.
- **Sex:** Where reported, the proportion male ranged from **`[x%]`** to **`[y%]`** (median **`[z%]`**).
- **Fever duration:** `[n]` studies restricted enrollment to days 0–3; `[n]` to days 0–7 with a reported mean/median ≤7 days; `[n]` provided day-stratified 2×2 tables. Median fever day at sampling ranged from **`[x]`** to **`[y]`**.
- **Clinical spectrum (WHO 2009):** `[n]` studies enrolled unselected suspected dengue; `[n]` were restricted to hospitalized or severe dengue; `[n]` reported dengue with warning signs separately.
- **Infection status:** `[n]` studies classified primary vs. secondary infection (method: IgM/IgG ratio `[n]`; paired sera `[n]`; HI assay `[n]`). Among classified cases, **`[n_prim]`** were primary and **`[n_sec]`** secondary.
- **Serotypes:** `[n]` studies reported serotype-specific 2×2 data. Combined counts: DENV-1 `[n]`, DENV-2 `[n]`, DENV-3 `[n]`, DENV-4 `[n]`, untyped `[n]`.
- **Specimen:** serum `[k]`, plasma `[k]`, whole blood `[k]`, more than one type `[k]`. Fresh specimens `[k]`; stored/frozen `[k]`; not reported `[k]`.

### 3.2.4 Index Tests, Comparators, and Reference Standards

**FIA platforms.** STANDARD F Dengue NS1 Ag FIA (SD Biosensor) was used in `[k]` studies (`[reader model, e.g., F200]`); NS1 Ag QUANTI CARD in `[k]`; other FIA platforms in `[k]` (`[list]`). Manufacturer-recommended COI cutoffs were used in `[k]` studies; post-hoc or modified thresholds in `[k]`; cutoff not stated in `[k]`. Reported turnaround time ranged from **`[x]`** to **`[y]`** minutes.

**ELISA (comparator or reference).** Platelia Dengue NS1 Ag (Bio-Rad) `[k]`; Panbio Dengue Early ELISA `[k]`; STANDARD E NS1 ELISA `[k]`; other/in-house `[k]`.

**Reference standard hierarchy (as classified in Methods §2.2):**

| Tier | Definition | Studies (k) | Participants (n) |
|------|------------|-------------|------------------|
| 1 | RT-PCR | `[k]` | `[n]` |
| 2 | Virus isolation ± RT-PCR | `[k]` | `[n]` |
| 3 | Composite (RT-PCR + seroconversion ± NS1 ELISA) | `[k]` | `[n]` |
| 4 | NS1 ELISA alone | `[k]` | `[n]` |

Same-specimen testing of index and reference was confirmed in `[k]` studies; interval ≤24 hours in `[k]`; interval not reported in `[k]`.

### 3.2.5 Individual-Study 2×2 Data (FIA vs. Reference)

**Table 3. Contingency tables and crude accuracy of FIA for dengue NS1**

| Study ID | TP | FP | FN | TN | N | Se (%) | Sp (%) | Zero-cell* |
|----------|----|----|----|----|---|--------|--------|------------|
| `[Author, Year]` | | | | | | | | Y/N |
| | | | | | | | | |
| | | | | | | | | |
| **Pooled (bivariate)** | — | — | — | — | **`[N]`** | **See §3.4** | **See §3.4** | — |

*Continuity correction of 0.5 applied in the model if any cell = 0. Crude Se/Sp are Wilson (or study-reported) estimates; they are **not** the bivariate pooled estimates.

ELISA-specific 2×2 tables (independent reference) are in Supplementary Table S4. FIA–ELISA agreement tables for paired specimens are in Supplementary Table S5.

**Candidate studies identified during protocol development** (Pohekar & Bhalchandra 2023; Ghogre 2021; Chaiyo et al. 2022) will be included **only if they pass formal dual-reviewer eligibility screening**. They are not listed as included studies in this draft.

---

## 3.3 Risk of Bias Assessment (QUADAS-2)

Two reviewers independently applied the tailored QUADAS-2 tool (`analysis/quadas2_protocol.md`). Inter-rater agreement for overall RoB was **κ = [x.xx]**. Domain-level judgments are shown in Figure 3 (traffic light) and Figure 4 (weighted summary bars), and tabulated in Supplementary Table S6.

### 3.3.1 Domain-Level Synthesis

**Table 4. QUADAS-2 summary (n = `[k]` studies)**

| Domain | Low n (%) | High n (%) | Unclear n (%) | Applicability: Low / High / Unclear n |
|--------|-----------|------------|---------------|----------------------------------------|
| D1 Patient selection | `[n] ([%])` | `[n] ([%])` | `[n] ([%])` | `[n]` / `[n]` / `[n]` |
| D2 Index test (FIA) | `[n] ([%])` | `[n] ([%])` | `[n] ([%])` | `[n]` / `[n]` / `[n]` |
| D3 Reference standard | `[n] ([%])` | `[n] ([%])` | `[n] ([%])` | `[n]` / `[n]` / `[n]` |
| D4 Flow and timing | `[n] ([%])` | `[n] ([%])` | `[n] ([%])` | N/A |
| **Overall RoB** | `[n] ([%])` | `[n] ([%])` | `[n] ([%])` | — |

**Patient selection (Domain 1).** `[Narrative: proportion consecutive/random vs. convenience or two-gate designs; fever-duration reporting (signalling question 1.4); spectrum concerns — exclusively severe dengue or healthy controls].` High applicability concern was assigned when `[describe, e.g., blood-donor controls or exclusively hospitalized severe dengue]`.

**Index test (Domain 2).** `[Narrative: blinding or automated COI readout; pre-specified manufacturer cutoff vs. post-hoc ROC optimization; IFU adherence; handling of indeterminate COI values].`

**Reference standard (Domain 3).** `[Narrative: RT-PCR vs. ELISA-only (imperfect reference → Unclear); incorporation bias when the same ELISA kit served as both comparator and sole reference (signalling question 3.3); diagnostic-window mismatch for RT-PCR].`

**Flow and timing (Domain 4).** `[Narrative: same-specimen testing; differential verification (RT-PCR only in FIA-positive patients); exclusions of indeterminates >5%; presence of STARD-style flow diagrams].`

**Figure 3.** QUADAS-2 traffic-light plot (study × domain). *Source: `output/figures/quadas2_traffic_light.pdf`.*

**Figure 4.** QUADAS-2 weighted bar chart of Low / High / Unclear judgments by domain. *Source: `output/figures/quadas2_summary.pdf`.*

Overall, **`[n]`** studies were judged Low RoB, **`[n]`** High RoB in ≥2 domains (excluded in sensitivity analysis §3.6.2), and **`[n]`** Unclear overall.

---

## 3.4 Diagnostic Test Accuracy Synthesis

### 3.4.1 Primary Analysis: FIA versus Reference Standard

The primary bivariate random-effects model (Reitsma) included **`[k_fia]`** studies and **`[N]`** participants. Variance components were estimated by REML. `[n]` studies required a 0.5 continuity correction for zero cells.

**Table 5. Pooled diagnostic accuracy of FIA for dengue NS1 antigen (bivariate GLMM)**

| Measure | Pooled estimate | 95% CI | Source |
|---------|-----------------|--------|--------|
| Sensitivity | **`[xx.x%]`** | `[ll.l]–[uu.u]%` | logit-Se back-transformed |
| Specificity | **`[xx.x%]`** | `[ll.l]–[uu.u]%` | 1 − logit-FPR back-transformed |
| False-positive rate | **`[x.xx]`** | `[ll]–[uu]` | logit-FPR |
| Positive likelihood ratio (PLR) | **`[x.xx]`** | `[ll.ll]–[uu.uu]` | parametric bootstrap, 10,000 draws |
| Negative likelihood ratio (NLR) | **`[0.xxx]`** | `[ll.ll]–[uu.uu]` | parametric bootstrap |
| Diagnostic odds ratio (DOR) | **`[xxx]`** | `[ll]–[uu]` | parametric bootstrap |
| HSROC AUC | **`[0.xxx]`** | `[ll.ll]–[uu.uu]` if estimated | HSROC parameterization |

*Interpretation aid (to be completed after estimates are available): a PLR >10 and NLR <0.1 generally indicate large shifts in post-test probability; DOR >25 is often considered strong discriminatory performance. Do not insert clinical claims until CIs are known.*

**Between-study heterogeneity (FIA primary model)**

| Parameter | Estimate | Notes |
|-----------|----------|-------|
| Cochran’s Q (logit-Se) | `[Q]`, df = `[k−1]`, *p* = `[p]` | α = 0.10 |
| I² (logit-Se) | **`[xx.x%]`** | `[might not be important / moderate / substantial / considerable]` |
| τ² (logit-Se) | `[x.xxxx]` | bivariate Σ[1,1] |
| Cochran’s Q (logit-Sp) | `[Q]`, df = `[k−1]`, *p* = `[p]` | |
| I² (logit-Sp) | **`[xx.x%]`** | |
| τ² (logit-FPR) | `[x.xxxx]` | bivariate Σ[2,2] |
| Correlation ρ (logit-Se, logit-FPR) | **`[−0.xx]`** | threshold-effect interpretation: `[yes if ρ < −0.3 / no / weak]` |

**Figure 5.** Coupled forest plots of FIA sensitivity and specificity. *Source: `output/figures/coupled_forest_fia.pdf` (and `forest_plot_fia.pdf`).*

**Figure 6.** HSROC curve for FIA (summary operating point, 95% confidence region, 95% prediction region, individual studies). *Source: `output/figures/sroc_fia.pdf`.*

**HSROC parameters (Rutter–Gatsonis parameterization, equivalent to Reitsma in the absence of covariates):** Λ (accuracy) = `[x.xx]`; Θ (threshold) = `[x.xx]`; β (symmetry) = `[x.xx]`. `[If β ≈ 0, the SROC is symmetric; if |β| is large, note asymmetry.]`

### 3.4.2 ELISA versus Independent Reference (Where Available)

Among studies that tested ELISA against an independent reference (RT-PCR or composite), **`[k_elisa]`** studies (**`[N]`** participants) entered a separate bivariate model.

**Table 6. Pooled diagnostic accuracy of ELISA for dengue NS1 (independent reference)**

| Measure | Pooled estimate | 95% CI |
|---------|-----------------|--------|
| Sensitivity | **`[xx.x%]`** | `[ll.l]–[uu.u]%` |
| Specificity | **`[xx.x%]`** | `[ll.l]–[uu.u]%` |
| PLR | **`[x.xx]`** | `[ll]–[uu]` |
| NLR | **`[0.xxx]`** | `[ll]–[uu]` |
| DOR | **`[xxx]`** | `[ll]–[uu]` |
| HSROC AUC | **`[0.xxx]`** | `[ll]–[uu]` |

If fewer than four such studies were available, ELISA accuracy is reported as a narrative range (individual-study Se **`[min]–[max]%`**, Sp **`[min]–[max]%`**) rather than a bivariate pooled estimate. `[Delete unused option.]*`

### 3.4.3 Head-to-Head Comparison: FIA versus ELISA (Paired Specimens)

**`[k_h2h]`** studies tested both assays on the same specimens. For a fair comparison, FIA was re-fitted on this overlapping subset.

**Table 7. Head-to-head bivariate estimates (identical study set)**

| Test | k | N | Sensitivity (95% CI) | Specificity (95% CI) | PLR (95% CI) | NLR (95% CI) |
|------|---|---|----------------------|----------------------|--------------|--------------|
| FIA (subset) | `[k]` | `[N]` | `[xx.x%] ([ll]–[uu])` | `[xx.x%] ([ll]–[uu])` | `[x.xx]` | `[0.xxx]` |
| ELISA | `[k]` | `[N]` | `[xx.x%] ([ll]–[uu])` | `[xx.x%] ([ll]–[uu])` | `[x.xx]` | `[0.xxx]` |
| **Difference (FIA − ELISA)** | — | — | **`[Δ Se, pp]`** | **`[Δ Sp, pp]`** | — | — |

Paired agreement (when FIA-vs-ELISA 2×2 tables were reported): overall agreement **`[xx.x%]`**; Cohen’s κ **`[0.xx]`** (95% CI `[ll]–[uu]`); McNemar *p* = `[p]`.

**Figure 7.** Comparative HSROC overlay: FIA (blue) vs. ELISA (red), paired-study subset. *Source: `output/figures/sroc_fia_vs_elisa.pdf`.*

**Narrative interpretation placeholder:** `[State whether CIs overlap; whether FIA was numerically similar, inferior, or superior on Se and/or Sp; do not claim non-inferiority unless a pre-specified margin was tested.]`

---

## 3.5 Subgroup and Meta-Regression Analyses

Subgroup bivariate models were fitted when **≥4 studies** were available per stratum (Methods §2.9.2). Strata below this threshold are described narratively only.

### 3.5.1 Early Acute (Days 0–3) versus Late Acute (Days 4–7)

**Table 8. FIA accuracy by timing of specimen collection**

| Stratum | k | N | Se (95% CI) | Sp (95% CI) | PLR | NLR | DOR |
|---------|---|---|-------------|-------------|-----|-----|-----|
| Early acute (days 0–3) | `[k]` | `[n]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Late acute (days 4–7) | `[k]` | `[n]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Mixed / unstratified (not in contrast) | `[k]` | `[n]` | — | — | — | — | — |

**Narrative:** `[Expected direction from protocol: higher Se in days 0–3. Report whether this was observed and whether Sp was stable.]` Likelihood-ratio test for fever-category covariate (meta-regression): χ² = `[x.xx]`, df = `[d]`, *p* = `[p]`.

### 3.5.2 Primary versus Secondary Infection

**Table 9. FIA accuracy by infection status**

| Stratum | k | N | Se (95% CI) | Sp (95% CI) | PLR | NLR | DOR |
|---------|---|---|-------------|-------------|-----|-----|-----|
| Primary infection | `[k]` | `[n]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Secondary infection | `[k]` | `[n]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Narrative:** `[Expected direction: lower Se in secondary infection due to anti-NS1 immune complexes (Duong et al., 2011). Report Δ Se in percentage points.]` LR test: χ² = `[x.xx]`, df = `[d]`, *p* = `[p]`.

### 3.5.3 Additional Pre-Specified Subgroups

**Table 10. Other subgroup bivariate models (FIA)**

| Covariate | Stratum | k | Se (95% CI) | Sp (95% CI) | Model fitted? |
|-----------|---------|---|-------------|-------------|---------------|
| DENV serotype | DENV-1 | `[k]` | `[ ]` | `[ ]` | Y / N (<4 studies) |
| | DENV-2 | `[k]` | `[ ]` | `[ ]` | Y / N |
| | DENV-3 | `[k]` | `[ ]` | `[ ]` | Y / N |
| | DENV-4 | `[k]` | `[ ]` | `[ ]` | Y / N |
| Reference standard | RT-PCR | `[k]` | `[ ]` | `[ ]` | Y / N |
| | ELISA | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Composite | `[k]` | `[ ]` | `[ ]` | Y / N |
| FIA platform | STANDARD F | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Other FIA | `[k]` | `[ ]` | `[ ]` | Y / N |
| Region | South Asia | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Southeast Asia | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Latin America | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Other | `[k]` | `[ ]` | `[ ]` | Y / N |
| Age | Pediatric ≤18 y | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Adult >18 y | `[k]` | `[ ]` | `[ ]` | Y / N |
| Design | Prospective | `[k]` | `[ ]` | `[ ]` | Y / N |
| | Retrospective | `[k]` | `[ ]` | `[ ]` | Y / N |

### 3.5.4 Univariable Bivariate Meta-Regression

**Table 11. Meta-regression (covariate vs. intercept-only; ML likelihood-ratio tests)**

| Covariate | Levels | LR χ² | df | *p* | Direction of effect on Se / Sp (if *p* < 0.05) |
|-----------|--------|-------|----|-----|-----------------------------------------------|
| Reference standard type | `[n levels]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| FIA brand | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Fever-duration category | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Infection type | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Specimen type | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Study design | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Prevalence (≤50% vs. >50%) | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Geographic region | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Overall QUADAS-2 RoB (Low vs. High/Unclear) | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

Covariates were entered one at a time. Multivariable bivariate meta-regression was `[not undertaken because k was insufficient / undertaken for {list} — specify]`.

---

## 3.6 Publication Bias and Sensitivity Analyses

### 3.6.1 Deeks’ Funnel Plot Asymmetry Test

Deeks’ regression of ln(DOR) on \(1/\sqrt{\text{ESS}}\) for the primary FIA dataset (**k = `[k_fia]`**):

| Statistic | Value |
|-----------|--------|
| Slope | `[x.xxx]` |
| Slope SE | `[x.xxx]` |
| *t* | `[x.xx]` |
| *p* (two-sided) | **`[0.xxx]`** |
| Interpretation (*p* < 0.10) | **[Evidence of small-study effects / No evidence of publication bias]** |

**Figure 8.** Deeks’ funnel plot (1/√ESS vs. ln[DOR]) with fitted regression line. *Source: `output/figures/deeks_funnel.pdf`.*

Visual inspection `[did / did not]` suggest asymmetry driven by `[smaller studies with higher DOR / no pattern]`. `[If k < 10, state that Deeks’ test has limited power and interpret with caution.]`

### 3.6.2 Sensitivity Analyses

**Table 12. Robustness of the FIA pooled operating point**

| Analysis | k | Sensitivity (95% CI) | Specificity (95% CI) | Δ Se vs. primary (pp) | Δ Sp vs. primary (pp) |
|----------|---|----------------------|----------------------|------------------------|------------------------|
| Primary (all eligible; REML; CC = 0.5) | `[k]` | `[ ]` | `[ ]` | — | — |
| Exclude High RoB in ≥2 domains | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| RT-PCR / virus isolation reference only | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Peer-reviewed full texts only (drop preprints/abstracts) | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Continuity correction = 0.1 | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Continuity correction = 1.0 | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| ML instead of REML | `[k]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Leave-one-out influence analysis.** Sequential omission of each study yielded sensitivity ranging from **`[min]`** to **`[max]`** and specificity from **`[min]`** to **`[max]`** (primary: Se `[xx.x%]`, Sp `[xx.x%]`). The most influential study was **`[Author, Year]`** (omission changed Se by `[x.x]` pp and/or Sp by `[x.x]` pp). Full LOO results: `output/tables/leave_one_out_results.csv`.

**Figure 9 (optional).** Leave-one-out plot of pooled Se and Sp. *[Generate from LOO table if desired.]*

**Narrative stability statement:** `[The pooled operating point was / was not materially changed by restriction to low-RoB studies, molecular reference standards, or alternative continuity corrections. Specify any analysis that moved Se or Sp outside the primary 95% CI.]`

### 3.6.3 Certainty of Evidence (GRADE for DTA) — Optional

If GRADE for test accuracy is applied (Methods §2.10.3):

**Table 13. GRADE Summary of Findings (FIA for dengue NS1)**

| Outcome | Study design (k, N) | RoB | Inconsistency | Indirectness | Imprecision | Publication bias | Certainty | Pooled estimate (95% CI) |
|---------|---------------------|-----|---------------|--------------|-------------|------------------|-----------|--------------------------|
| Sensitivity | `[k, N]` | `[serious / not]` | `[serious / not]` | `[serious / not]` | `[serious / not]` | `[undetected / suspected]` | **[⊕⊕⊕⊕ / ⊕⊕⊕○ / ⊕⊕○○ / ⊕○○○]** | `[xx.x% (ll–uu)]` |
| Specificity | `[k, N]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | **[ ]** | `[xx.x% (ll–uu)]` |

---

## 3.7 Summary of Principal Findings (Results Only)

*This paragraph is a factual recap for the start of the Discussion; keep interpretation for Section 4.*

In `[k]` studies (`[N]` participants) from `[regions]`, FIA for dengue NS1 showed pooled sensitivity **`[xx.x%]`** (95% CI `[ll]–[uu]`) and specificity **`[xx.x%]`** (95% CI `[ll]–[uu]`), with PLR **`[x.xx]`**, NLR **`[0.xxx]`**, DOR **`[xxx]`**, and HSROC AUC **`[0.xx]`**. In `[k]` paired studies, FIA `[was similar to / differed from]` ELISA by `[Δ Se]` pp and `[Δ Sp]` pp. Heterogeneity was `[I²-Se / I²-Sp interpretation]`. Accuracy `[was / was not]` lower in secondary infection and `[was / was not]` higher in the first 3 days of fever. Deeks’ test `[did / did not]` indicate small-study effects (*p* = `[p]`). Sensitivity analyses `[supported / qualified]` the primary operating point.

---

## FIGURE AND TABLE MANIFEST (for production)

| Item | File / location | Status |
|------|-----------------|--------|
| Figure 1 PRISMA 2020 flow | Draw from Table 1 counts | Pending search |
| Figure 2 Geographic map | Optional | Pending extraction |
| Figure 3 QUADAS-2 traffic light | `output/figures/quadas2_traffic_light.pdf` | Pending RoB |
| Figure 4 QUADAS-2 summary bars | `output/figures/quadas2_summary.pdf` | Pending RoB |
| Figure 5 Coupled forest plots | `output/figures/coupled_forest_fia.pdf` | Pending R script |
| Figure 6 HSROC (FIA) | `output/figures/sroc_fia.pdf` | Pending R script |
| Figure 7 Comparative HSROC | `output/figures/sroc_fia_vs_elisa.pdf` | Pending ≥4 paired studies |
| Figure 8 Deeks’ funnel | `output/figures/deeks_funnel.pdf` | Pending R script |
| Table 3 2×2 data | Extraction summary table | Pending extraction |
| Table 5 pooled estimates | `output/tables/pooled_estimates_with_ci.csv` | Pending R script |
| Table 12 sensitivity | LOO + restriction runs | Pending R script |

---

## DATA-INTEGRATION CHECKLIST

- [ ] Execute searches; complete Table 1 and Figure 1
- [ ] Dual screen; record κ and exclusion taxonomy
- [ ] Complete Tables 2–3 from `data/extraction_template.md`
- [ ] Complete QUADAS-2 spreadsheet; generate Figures 3–4
- [ ] Replace placeholder 2×2 data in `analysis/dta_meta_analysis.R`
- [ ] Run script; paste Table 5–7 and 8–12 from CSV output
- [ ] Insert Figures 5–8
- [ ] Write §3.7 recap using **only** filled estimates
- [ ] Confirm no leftover `[TO BE FILLED]` tokens before journal submission

---

*Manuscript version: 1.0 — Results scaffold*
*Prepared: August 2026*
*No pooled diagnostic accuracy estimates were fabricated.*
