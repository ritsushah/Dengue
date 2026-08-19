# Customized QUADAS-2 Risk of Bias Assessment Protocol

**Review:** Diagnostic Accuracy of Fluorescence Immunoassay (FIA) versus Enzyme-Linked Immunosorbent Assay (ELISA) for Dengue Virus NS1 Antigen Detection: A Systematic Review and Meta-Analysis

**Tool:** QUADAS-2 (Quality Assessment of Diagnostic Accuracy Studies 2)
**Reference:** Whiting PF, Rutjes AW, Westwood ME, et al. *Ann Intern Med*. 2011;155(8):529–536. doi:10.7326/0003-4819-155-8-201110180-00009

---

## 1. Overview

QUADAS-2 assesses risk of bias (RoB) and applicability concerns in diagnostic accuracy studies across four domains:

1. **Patient Selection**
2. **Index Test**
3. **Reference Standard**
4. **Flow and Timing**

Each domain is evaluated for **risk of bias** (Low / High / Unclear). The first three domains are additionally evaluated for **applicability concerns** (Low / High / Unclear). Domain 4 (Flow and Timing) has no applicability assessment.

The signalling questions below have been **tailored specifically for dengue NS1 diagnostic accuracy studies** evaluating FIA against ELISA and/or RT-PCR reference standards, with particular attention to:
- Timing of blood draw relative to symptom onset (critical for NS1 kinetics)
- Reference standard independence (incorporation bias when ELISA serves as both comparator and reference)
- Threshold pre-specification (COI cutoff variability across FIA platforms)
- Differential verification and partial verification bias

---

## 2. Domain-Specific Signalling Questions, Decision Rules, and Rationale

---

### DOMAIN 1: PATIENT SELECTION

**Objective:** Assess whether patients were enrolled in a way that avoids spectrum bias, selection bias, and inappropriate case-control designs.

#### Signalling Questions

| # | Signalling Question | Answer Options |
|---|---------------------|----------------|
| 1.1 | **Was a consecutive or random sample of patients enrolled?** | Yes / No / Unclear |
| 1.2 | **Was a case-control design avoided?** | Yes / No / Unclear |
| 1.3 | **Did the study avoid inappropriate exclusions?** | Yes / No / Unclear |
| 1.4 | **Were patients enrolled with a clinically appropriate fever duration (≤7 days)?** *(Review-specific)* | Yes / No / Unclear |

#### Decision Rules

| Question | "Yes" Criteria | "No" Criteria | "Unclear" Criteria |
|----------|----------------|---------------|---------------------|
| 1.1 | Consecutive enrollment or random sampling is explicitly stated in the methods. | Convenience sampling, selected specimens, or enriched sample with disproportionate disease prevalence. | Enrollment strategy is not described or cannot be determined. |
| 1.2 | Cross-sectional, prospective cohort, or retrospective cohort design where all patients undergo both index test and reference standard. | Separate sampling of known dengue-positive cases and known dengue-negative controls (two-gate design). | Study design is ambiguous or not clearly described. |
| 1.3 | All clinically suspected dengue patients were eligible regardless of disease severity (DF, DF+WS, severe dengue), age, or infection status (primary/secondary). | Systematic exclusion of patients with warning signs, severe dengue, secondary infections, pediatric cases, or specific serotypes without clinical justification. | Exclusion criteria are not reported or are vague. |
| 1.4 | Specimens were collected during the acute febrile phase (≤7 days post-symptom onset), either as stated inclusion criterion or documented median/mean fever duration ≤7 days. | Specimens collected exclusively from convalescent patients (>7 days) or mixed acute/convalescent with no subgroup separation. | Timing of specimen collection relative to symptom onset is not reported. |

#### Risk of Bias Judgment

| Judgment | Criteria |
|----------|----------|
| **Low** | All signalling questions answered "Yes." |
| **High** | Any signalling question answered "No." Specifically: case-control design, convenience sampling of pre-selected positive/negative panels, or systematic exclusion of clinically relevant subpopulations. |
| **Unclear** | Insufficient information to determine the answer to one or more signalling questions, AND the available information does not suggest high risk. |

#### Applicability Concern

| Concern | Criteria |
|---------|----------|
| **Low** | Study enrolled patients presenting with suspected acute dengue in an endemic or epidemic setting, representative of the clinical scenario where FIA would be deployed. Mixed or unselected population with respect to severity, age, and infection status. |
| **High** | Study population differs substantially from the target clinical scenario: exclusively hospitalized severe dengue patients (spectrum bias toward severe end), exclusively healthy blood donors as controls (inflated specificity), exclusively pediatric or neonatal population when the review targets all ages, or exclusively seroprevalence/surveillance specimens without clinical suspicion. |
| **Unclear** | Insufficient description of the clinical setting, referral pathway, or patient demographics to assess representativeness. |

#### Rationale for Review-Specific Adaptations

> **Question 1.4** is added because NS1 antigen kinetics are time-dependent: NS1 is detectable from day 0 through approximately day 9 post-symptom onset, with peak levels during days 0–5 (Muller et al., 2017, *J Infect Dis*, 215:S13–S17). Studies collecting specimens beyond the acute window may systematically underestimate sensitivity due to declining NS1 levels, introducing time-dependent spectrum bias. This question ensures that the temporal eligibility window is explicitly assessed.

---

### DOMAIN 2: INDEX TEST (Fluorescence Immunoassay — FIA)

**Objective:** Assess whether the FIA was conducted and interpreted in a way that avoids bias from knowledge of the reference standard result or post-hoc threshold optimization.

#### Signalling Questions

| # | Signalling Question | Answer Options |
|---|---------------------|----------------|
| 2.1 | **Were the FIA results interpreted without knowledge of the reference standard results?** | Yes / No / Unclear |
| 2.2 | **If a threshold (Cutoff Index, COI) was used, was it pre-specified?** | Yes / No / Unclear |
| 2.3 | **Was the FIA performed according to the manufacturer's instructions for use (IFU)?** *(Review-specific)* | Yes / No / Unclear |
| 2.4 | **Were indeterminate, invalid, or borderline FIA results reported and handled appropriately?** *(Review-specific)* | Yes / No / Unclear |

#### Decision Rules

| Question | "Yes" Criteria | "No" Criteria | "Unclear" Criteria |
|----------|----------------|---------------|---------------------|
| 2.1 | Blinding of FIA interpretation to reference standard results is explicitly stated, or tests were performed simultaneously on the same day by independent operators with no cross-communication of results. Automated reader-based FIA interpretation (no subjective visual reading) also qualifies as "Yes" since the COI is determined by the instrument without operator discretion. | FIA results were interpreted after reference standard results were known, or a single operator performed both tests sequentially and was aware of the reference result before reading the FIA. | Blinding is not mentioned, and the workflow does not make it implicit. |
| 2.2 | The manufacturer's recommended COI cutoff was used without modification, or the cutoff was pre-specified in the study protocol before data analysis. | The COI threshold was optimized post-hoc using ROC analysis on the study data to maximize sensitivity/specificity (data-driven threshold selection). | The threshold used is not clearly stated, or it is unclear whether it was pre-specified or data-driven. |
| 2.3 | The study states that testing was performed per the manufacturer's IFU, including correct specimen volume, incubation time, reading window, and storage conditions. | The study explicitly deviates from the IFU (e.g., modified incubation time, diluted specimen, non-recommended specimen type) without providing a rationale or validation. | IFU adherence is not mentioned. |
| 2.4 | Indeterminate, invalid, or borderline results are reported with their counts and management (re-tested, excluded, classified as positive or negative). Proportion of indeterminate results is <5% of total. | Indeterminate results are not mentioned despite being expected in clinical testing, or a substantial proportion (≥5%) were excluded without sensitivity analysis. | Not addressed in the study. |

#### Risk of Bias Judgment

| Judgment | Criteria |
|----------|----------|
| **Low** | Questions 2.1 and 2.2 answered "Yes." Questions 2.3 and 2.4 do not raise concerns. |
| **High** | FIA was interpreted with knowledge of the reference standard result (2.1 = No), OR the threshold was optimized post-hoc (2.2 = No), OR a substantial proportion of indeterminate results were excluded without accounting for them. |
| **Unclear** | Blinding and threshold pre-specification cannot be determined. |

#### Applicability Concern

| Concern | Criteria |
|---------|----------|
| **Low** | The FIA test evaluated is a commercially available platform (e.g., STANDARD F Dengue NS1 Ag FIA, SD Biosensor) using the manufacturer's recommended COI cutoff, tested on clinically relevant specimen types (whole blood, serum, or plasma). |
| **High** | The FIA is a prototype, laboratory-developed, or experimental platform not commercially available; or a non-standard specimen type (saliva, urine) was used; or the COI threshold differs substantially from the manufacturer's recommendation. |
| **Unclear** | The FIA platform or COI threshold is not clearly described. |

#### Rationale for Review-Specific Adaptations

> **Question 2.3** is added because FIA performance is sensitive to pre-analytical variables (specimen type, hemolysis, storage temperature) and incubation time. Deviations from the IFU may introduce systematic bias not attributable to the assay's inherent diagnostic accuracy.
>
> **Question 2.4** is added because FIA readers can produce borderline COI values near the cutoff, which are clinically important. Their exclusion constitutes a form of partial verification bias that may inflate apparent sensitivity and specificity.

---

### DOMAIN 3: REFERENCE STANDARD

**Objective:** Assess whether the reference standard correctly classifies the target condition (acute dengue infection) and whether it was interpreted independently of the index test.

#### Signalling Questions

| # | Signalling Question | Answer Options |
|---|---------------------|----------------|
| 3.1 | **Is the reference standard likely to correctly classify the target condition?** | Yes / No / Unclear |
| 3.2 | **Were the reference standard results interpreted without knowledge of the FIA results?** | Yes / No / Unclear |
| 3.3 | **If ELISA served as the reference standard, was incorporation bias avoided?** *(Review-specific)* | Yes / No / Unclear / N/A |
| 3.4 | **Was the reference standard applied during the appropriate diagnostic window?** *(Review-specific)* | Yes / No / Unclear |

#### Decision Rules

| Question | "Yes" Criteria | "No" Criteria | "Unclear" Criteria |
|----------|----------------|---------------|---------------------|
| 3.1 | RT-PCR for DENV RNA, virus isolation, or a composite reference standard combining RT-PCR with IgM/IgG seroconversion on paired sera. These are accepted gold/reference standards for acute dengue diagnosis. | A single serological test (IgM-only or IgG-only ELISA) used as the sole reference standard, which cannot distinguish acute from past infection and has poor sensitivity in the early acute phase. | NS1 ELISA alone as the reference standard — this is an imperfect reference standard for acute DENV infection (may miss NS1-negative viremic cases). |
| 3.2 | Blinding of reference standard interpretation to FIA results is explicitly stated, or the reference standard is an automated molecular test (RT-PCR) with objective readout not influenced by knowledge of FIA results. | Reference standard results were determined after FIA results were known and may have been influenced. | Blinding is not mentioned. |
| 3.3 | The ELISA serving as the reference standard is immunologically independent from the FIA index test (e.g., different antibody clones, different epitope targets), OR the reference standard is RT-PCR (not ELISA). Answer "N/A" if ELISA is used only as a comparator test and RT-PCR serves as the reference standard. | The same ELISA (identical kit) is used as both the comparator AND the reference standard, creating circular validation (incorporation bias). | The relationship between the ELISA comparator and the reference standard is not clearly delineated. |
| 3.4 | The reference standard was applied to specimens collected during the acute phase (≤7 days), when both NS1 antigen and DENV RNA are expected to be present. For RT-PCR, the specimen was collected within the viremic window (days 0–7). For IgM seroconversion, paired sera (acute + convalescent at ≥7 days interval) were used. | The reference standard was applied to a specimen collected outside its optimal diagnostic window (e.g., RT-PCR on a day 10+ specimen, when viremia may have cleared). | The timing of specimen collection relative to the reference standard's diagnostic window is not reported. |

#### Risk of Bias Judgment

| Judgment | Criteria |
|----------|----------|
| **Low** | RT-PCR or virus isolation used as reference standard (3.1 = Yes), blinding confirmed (3.2 = Yes), no incorporation bias (3.3 = Yes or N/A), appropriate diagnostic window (3.4 = Yes). |
| **High** | Reference standard is unlikely to correctly classify acute dengue (3.1 = No), OR FIA results influenced reference standard interpretation (3.2 = No), OR clear incorporation bias exists (3.3 = No). |
| **Unclear** | NS1 ELISA used as sole reference standard (imperfect reference — 3.1 = Unclear), OR blinding status unknown, OR diagnostic window unclear. |

#### Applicability Concern

| Concern | Criteria |
|---------|----------|
| **Low** | The reference standard defines the target condition (acute DENV infection confirmed by virological evidence) as intended by this review. |
| **High** | The reference standard defines a different target condition (e.g., "any past or present dengue infection" based on IgG positivity alone, or "dengue-like illness" based on clinical criteria without laboratory confirmation). |
| **Unclear** | The exact definition of a positive reference standard result is ambiguous. |

#### Rationale for Review-Specific Adaptations

> **Question 3.3** addresses a critical concern in dengue NS1 diagnostic studies: when NS1 ELISA is used simultaneously as the comparator test and as the sole reference standard, any concordance between FIA and ELISA is tautological (incorporation bias). This inflates apparent sensitivity and specificity of FIA because the "truth" is defined by the very test it is being compared against. Studies must use an independent reference (RT-PCR, virus isolation, or composite) to avoid this circularity.
>
> **Question 3.4** is added because dengue diagnostic tests have serotype- and phase-dependent kinetics. Applying RT-PCR to a specimen collected after day 7 (when viremia is clearing) may produce false-negative reference results, misclassifying true dengue cases as non-dengue and spuriously lowering the index test's apparent sensitivity.

---

### DOMAIN 4: FLOW AND TIMING

**Objective:** Assess whether all patients were accounted for in the analysis and whether the flow of patients through the study introduced bias.

#### Signalling Questions

| # | Signalling Question | Answer Options |
|---|---------------------|----------------|
| 4.1 | **Was there an appropriate interval between the index test and reference standard?** | Yes / No / Unclear |
| 4.2 | **Did all patients receive the same reference standard?** | Yes / No / Unclear |
| 4.3 | **Were all patients included in the analysis?** | Yes / No / Unclear |
| 4.4 | **Was the flow of patients clearly described with a participant flow diagram or equivalent?** *(Review-specific)* | Yes / No / Unclear |

#### Decision Rules

| Question | "Yes" Criteria | "No" Criteria | "Unclear" Criteria |
|----------|----------------|---------------|---------------------|
| 4.1 | FIA and reference standard were performed on the **same specimen** (aliquots from the same blood draw), OR on specimens collected within **24 hours** of each other. Given the rapid kinetics of NS1 antigenemia, same-specimen testing is strongly preferred. | Index test and reference standard were performed on specimens collected >24 hours apart, during which NS1 levels may have changed substantially (especially across the day 5–7 transition when NS1 declines and IgM rises). | The time interval between specimen collections for FIA and reference standard is not reported. |
| 4.2 | All participants received the **same reference standard** (e.g., all were tested with RT-PCR, or all received the same composite algorithm). No differential verification. | **Differential verification** occurred: some patients received RT-PCR (more accurate) while others received only ELISA or clinical criteria (less accurate), and the choice of reference standard was influenced by index test results or clinical status. This is a common source of bias in dengue diagnostic studies where RT-PCR may only be performed on FIA-positive patients. | The reference standard verification scheme is not clearly described. |
| 4.3 | All enrolled patients are accounted for in the final 2×2 table. If patients were excluded (indeterminate results, missing specimens, loss to follow-up), the number is reported and is <5% of total, with reasons provided. | >5% of enrolled patients are excluded from the final analysis without adequate justification, OR a substantial number of patients with indeterminate/borderline results are excluded, potentially biasing accuracy estimates. | The number of excluded patients is not reported, or the denominator in the 2×2 table does not match the reported enrollment. |
| 4.4 | A patient flow diagram (STARD-style) or clear narrative description of patient flow from enrollment through testing to final analysis is provided, showing the number screened, tested, excluded, and analyzed. | Patient flow is not described, and the reader cannot reconstruct the pathway from enrollment to analysis. | Partial flow information is available but incomplete. |

#### Risk of Bias Judgment

| Judgment | Criteria |
|----------|----------|
| **Low** | All signalling questions answered "Yes." Same-specimen testing, uniform reference standard, complete data, transparent flow. |
| **High** | Index test and reference standard were performed >24 hours apart (4.1 = No), OR differential verification occurred (4.2 = No), OR >5% of patients excluded without justification (4.3 = No). |
| **Unclear** | Insufficient information to determine the answer to key signalling questions, but no overt red flags. |

#### Applicability Concern

Domain 4 does not have an applicability assessment per the standard QUADAS-2 framework.

#### Rationale for Review-Specific Adaptations

> **Question 4.4** is added for operational quality assurance. In dengue diagnostic studies, patients may be lost to follow-up (especially in outpatient settings during epidemics), specimens may be insufficient for all tests, or indeterminate FIA results may not be re-tested. A clear flow diagram is essential for assessing whether the analyzed cohort represents the enrolled cohort, which directly affects the external validity of diagnostic accuracy estimates.

---

## 3. Summary of Review-Specific Signalling Questions (Beyond Standard QUADAS-2)

| Domain | Added Question | Rationale |
|--------|---------------|-----------|
| 1 (Patient Selection) | 1.4: Clinically appropriate fever duration ≤7 days | NS1 antigen kinetics: peak days 0–5, declining by day 7–9. Time-dependent spectrum bias. |
| 2 (Index Test) | 2.3: IFU adherence | FIA sensitivity depends on pre-analytical variables and procedural compliance. |
| 2 (Index Test) | 2.4: Indeterminate result handling | Borderline COI values are clinically relevant; their exclusion inflates accuracy. |
| 3 (Reference Standard) | 3.3: Incorporation bias (ELISA as both comparator and reference) | Circular validation when same ELISA serves dual roles. |
| 3 (Reference Standard) | 3.4: Reference standard applied in appropriate diagnostic window | RT-PCR sensitivity declines after viremic window; misclassification biases index test accuracy. |
| 4 (Flow and Timing) | 4.4: Patient flow transparency | Essential for reconstructing enrollment-to-analysis pathway in epidemic settings. |

---

## 4. Assessment Process

### 4.1 Assessors
- Two reviewers will independently assess each included study.
- A calibration exercise will be performed on 3 studies before full assessment.
- Discrepancies will be resolved by discussion; unresolved disagreements adjudicated by a third reviewer.

### 4.2 Data Recording
- Judgments will be recorded in a standardized spreadsheet (one row per study, columns for each signalling question answer and domain-level judgments).
- Supporting text evidence from each study will be recorded alongside judgments for audit trail.

### 4.3 Visualization

Results will be presented using the `robvis` R package (McGuinness & Higgins, 2021, *Res Synth Methods*, 12:55–61):

**Traffic Light Plot** — study-level domain judgments:

```r
rob_traffic_light(quadas_data, tool = "QUADAS-2",
                  colour = "cochrane", psize = 14)
```

**Summary Bar Plot** — weighted proportion of Low/High/Unclear judgments per domain:

```r
rob_summary(quadas_data, tool = "QUADAS-2",
            overall = TRUE, weighted = TRUE,
            colour = "cochrane")
```

### 4.4 Expected Data Frame Structure for `robvis`

For QUADAS-2, `robvis` expects the following column structure:

| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 |
|----------|----------|----------|----------|----------|----------|----------|
| Study | D1 (Patient Selection) | D2 (Index Test) | D3 (Reference Standard) | D4 (Flow and Timing) | Overall | Weight |

Values for domains: `"Low"`, `"High"`, or `"Unclear"`.

---

## 5. Integration with Meta-Analysis

### 5.1 Sensitivity Analysis by Risk of Bias

The primary meta-analysis will be re-run after excluding studies judged as **High** risk of bias in ≥2 domains to assess the robustness of pooled sensitivity and specificity estimates.

### 5.2 Meta-Regression by Risk of Bias

Overall QUADAS-2 risk of bias (dichotomized as Low vs. High/Unclear) will be included as a covariate in bivariate meta-regression:

```r
reitsma(data, formula = cbind(tsens, tfpr) ~ rob_overall)
```

### 5.3 Reporting

- The QUADAS-2 assessment for each included study will be presented in a summary table in the main manuscript.
- Traffic light and summary bar plots will be presented as figures.
- Detailed signalling question responses with supporting evidence will be provided as supplementary material.

---

## 6. References

1. Whiting PF, Rutjes AW, Westwood ME, et al. QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies. *Ann Intern Med*. 2011;155(8):529-536. doi:10.7326/0003-4819-155-8-201110180-00009
2. Muller DA, Depelsenaire ACI, Young PR. Clinical and laboratory diagnosis of dengue virus infection. *J Infect Dis*. 2017;215(suppl_2):S13-S17. doi:10.1093/infdis/jiw649
3. McGuinness LA, Higgins JPT. Risk-of-bias VISualization (robvis): an R package and Shiny web app for visualizing risk-of-bias assessments. *Res Synth Methods*. 2021;12(1):55-61. doi:10.1002/jrsm.1411
4. Bossuyt PM, Reitsma JB, Bruns DE, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. *BMJ*. 2015;351:h5527. doi:10.1136/bmj.h5527
5. Defined Health et al. Preferred reporting items for systematic review and meta-analysis of diagnostic test accuracy studies (PRISMA-DTA): explanation, elaboration, and checklist. *BMJ*. 2020;370:m2632. doi:10.1136/bmj.m2632

---

*Document version: 1.0*
*Prepared: August 2026*
