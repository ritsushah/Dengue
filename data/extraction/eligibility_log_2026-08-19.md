# Eligibility and extraction log — FIA for dengue NS1

**Date locked:** 19 August 2026  
**Unique bibliographic set:** `data/deduped/unique_pubmed_embase_wos_sd_2026-08-19.csv` (n = 1,082)

## Protocol deviation (screening)

Dual independent title/abstract screening of all 1,082 unique bibliographic records was **not** completed. The electronic strategy used (FIA **OR** ELISA), so the unique set is dominated by ELISA-only NS1 papers. Selection used:

1. Title/field filter of the 1,082 records for FIA / fluorescence immunoassay / STANDARD F / QUANTI CARD / iQuant (10 hits).
2. Full-text assessment of those hits, plus Zapata-de la Cruz 2026 (in the unique set; STANDARD F named in the paper, not the title).
3. Two protocol-scoping validations not retrieved in the four bibliographic databases: Ghogre 2021 (IJCRR) and Pohekar 2017 (IJCMAS).

Cohen’s κ is therefore **not reported**. This is a major limitation.

## Full-text decisions (n = 13)

| Record | Decision | Reason |
|--------|----------|--------|
| Chaiyo 2022, *Sci Rep* | **Include** | STANDARD F NS1 vs RT-qPCR+ELISA composite; reconstructable 2×2; fever mean 3.30 days. |
| Zapata-de la Cruz 2026, *TMI* | **Include** | STANDARD F NS1 vs RT-PCR (primary cells) and vs RT-PCR/IgM GS (sensitivity); fever days 2–6. |
| Ghogre 2021, *IJCRR* | **Include** | QUANTI CARD vs NS1 ELISA; unique integer 2×2; fever duration not reported (applicability Unclear). |
| Zuroidah 2022, *RJPT* | **Include** | STANDARD F vs RT-PCR and/or Panbio NS1 ELISA; 2×2 from Se/Sp and 50/30 split; two-gate design. First author Nelly Zuroidah. |
| Pohekar 2017, *IJCMAS* | **Include** | QUANTI CARD vs NS1 ELISA on 100 selected samples; 2×2 from published table/text; two-gate. |
| Pohekar 2023, *IJMM* | Exclude (quantitative) | STANDARD F vs ELISA, n=300; FIA+ 203 and ELISA+ 200 reported without off-diagonal cells. Not reconstructable. Narrative only. |
| Zammarchi 2019, *J Clin Virol* | Exclude | Selected panel (11 acute DENV). NS1-only 2×2 not reconstructable (published Se is NS1 **and/or** IgM). |
| Multilayer fluorescent immunoassay 2025 | Exclude | Experimental host+viral biomarker assay, not a commercial reader FIA. |
| Chopped optical biosensing 2026 | Exclude | Analytical platform paper, not clinical DTA of commercial FIA. |
| Rebuttal to Pohekar 2023 | Exclude | Correspondence, not original DTA data. |
| CCA 2022 conference abstract (NS1/CHIKV/HCV FIA) | Exclude | Conference abstract; dengue-only NS1 2×2 not reconstructable. |
| Buonora 2017 Portuguese ICT paper | Exclude | Visual immunochromatography, not FIA (false-positive FIA-term match). |
| Brazilian clinical-diagnosis reliability 2018 | Exclude | Wrong index test (clinical diagnosis). |

VIDAS NS1 ELFA was not treated as eligible cartridge FIA (automated laboratory ELFA, different technology class).

## 2×2 reconstruction rules

Cells were taken from published contingency tables when available. Otherwise TP = round(Se × n+), with integer solutions required to reproduce published Se, Sp, PPV, and NPV to the reported precision. Continuity correction 0.5 is applied at the modelling stage only, not in the extracted table.

## Overlap

Pohekar 2017 and Pohekar 2023 share an Aurangabad group. Different years, sample sizes (100 selected vs 300), and index-test generations; both retained for qualitative discussion; only 2017 enters the bivariate model.
