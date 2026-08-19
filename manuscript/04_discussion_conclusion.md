# 4. DISCUSSION, LIMITATIONS, AND CONCLUSION

> **STATUS:** Interpretive prose is written against the *a priori* hypotheses (Introduction §1.6) and the published dengue NS1 literature. **Pooled estimates from this review remain placeholders** (`[Se]`, `[Sp]`, `[k]`, etc.). After Results §3.4–3.7 are populated from `analysis/dta_meta_analysis.R`, replace every bracketed token and delete any sentence whose direction of effect is contradicted by the data. Do not submit with unresolved placeholders.
>
> This section maps to **PRISMA-DTA items 24–26**.

---

## 4.1 Principal Findings

This systematic review and meta-analysis is, to our knowledge, the first DTA synthesis to isolate **fluorescence immunoassay (FIA)** as a distinct technology for dengue NS1 antigen detection, rather than pooling it with visually read immunochromatographic tests (ICTs). Across **`[k]`** studies and **`[N]`** participants, FIA showed pooled sensitivity **`[xx.x%]`** (95% CI `[ll]–[uu]`) and specificity **`[xx.x%]`** (95% CI `[ll]–[uu]`), with PLR **`[x.xx]`**, NLR **`[0.xxx]`**, DOR **`[xxx]`**, and HSROC AUC **`[0.xx]`**. In the paired subset (`[k_h2h]` studies, same specimens), FIA differed from ELISA by **`[Δ Se]`** percentage points in sensitivity and **`[Δ Sp]`** percentage points in specificity.

These estimates should be read against three comparators already established in the literature.

**FIA versus visual ICT.** Prior meta-analyses of visually read NS1 ICTs report pooled sensitivity in the range of approximately 71% with specificity near 95% (Haider et al.: NS1-only ICT sensitivity 70.97%, specificity 94.73%, DOR 43.95) [1], and combination NS1/IgM/IgG ICTs approaching 91% sensitivity and 96% specificity, albeit with I² > 90% [2]. Individual FIA evaluations have suggested that reader-based fluorescence detection can exceed visual ICT on the same specimens (e.g., Ghogre: FIA 96.5%/96.4% vs. ICT 65.5%/83.9% against ELISA; Chaiyo et al.: FIA NS1 79.1%/92.3% vs. ICT 76.6%/92.3% against a combinatorial RT-PCR–ELISA standard) [3,4]. **`[If our pooled FIA Se exceeds ~71% with overlapping or higher Sp, state that FIA appears to close part of the ICT–ELISA gap. If not, state that FIA remains in the ICT performance envelope.]`**

**FIA versus ELISA.** NS1 ELISA remains the laboratory workhorse. Da Silva et al. pooled Platelia sensitivity at 74% (95% CI 63–82%) and Panbio at 66% (95% CI 61–71%), both with specificity 99% [5]. Guzmán et al. found Platelia more sensitive than Pan-E (66% vs. 52%) with 100% specificity in non-dengue febrile patients [6]. Pillay et al., using a Bayesian model that does not assume a perfect gold standard, estimated NS1 ELISA sensitivity at 90% (95% CrI 68–98%) and specificity 93% (71–99%) during days 0–4, approaching RT-PCR [7]. Pal et al. (WHO/TDR evaluation) reported NS1 ELISA sensitivity 60–75% against RT-PCR, with a clear drop in secondary infection [8]. **`[Compare our paired FIA vs ELISA ΔSe/ΔSp and CI overlap. If CIs overlap, conclude diagnostic interchangeability has not been excluded; if ELISA Se is higher and CIs separate, conclude FIA is a rapid adjunct rather than a laboratory replacement.]`**

**Likelihood ratios and clinical utility.** A PLR of **`[x.xx]`** `[if >10: produces a large increase in post-test probability of acute dengue when FIA is positive; if 5–10: moderate; if 2–5: small]` [9]. An NLR of **`[0.xxx]`** `[if <0.1: a negative FIA substantially lowers probability; if 0.1–0.2: moderate reduction; if >0.2: a negative result does not reliably exclude dengue, particularly in secondary infection and after day 3]` [9]. In high-prevalence outbreak settings, even a moderately high PLR can yield a high positive predictive value; the same NLR will miss more cases when prior probability is high. This asymmetry is the operational argument for using FIA as a **rule-in** test during the febrile window, with a negative result triggering ELISA, RT-PCR, or paired serology rather than discharge from a dengue pathway [10,11].

**Heterogeneity and a priori hypotheses.** Between-study I² was **`[xx%]`** for sensitivity and **`[xx%]`** for specificity. Subgroup models `[supported / did not support]` lower sensitivity in secondary infection and `[supported / did not support]` higher sensitivity on days 0–3, consistent with NS1 kinetics and anti-NS1 immune-complex formation [12–14]. **`[State serotype and platform findings if k ≥ 4 per stratum; otherwise note that those hypotheses remain untested in this evidence base.]`** Deeks’ test `[did / did not]` suggest small-study effects (*p* = `[p]`) [15].

Taken together, the principal finding is that FIA occupies a **middle stratum** of the dengue NS1 diagnostic landscape: faster and more portable than ELISA, more objective than visual ICT, and **`[comparable to / modestly inferior to / not yet distinguishable from]`** ELISA on paired specimens — at the cost of a reader device, cartridge supply chain, and residual sensitivity loss in secondary and late-acute infection.

---

## 4.2 Clinical and Operational Implications

### 4.2.1 Why turnaround time is a clinical, not merely logistical, variable

WHO 2009 dengue guidance ties risk stratification (warning signs, plasma leakage, shock) to the period around defervescence, typically days 3–7 of illness [11]. NS1 is most detectable from day 0 through approximately day 9, peaking in the first four days, and often before IgM appears [13,16]. ELISA batching plus transport from primary or rural sites commonly yields 24–48 hours to an actionable result [17,18]. That delay can span the transition from undifferentiated fever to the critical phase. FIA results in 5–15 minutes on whole blood, serum, or plasma [4,19,20] therefore change *when* a diagnosis can inform fluid management, admission, and isolation — not only *whether* the assay is analytically accurate.

### 4.2.2 Emergency departments and hospital triage

In endemic EDs and fever clinics, the differential includes malaria, leptospirosis, typhoid, chikungunya, and Zika [10,21]. A same-encounter NS1 result supports:

- **Rule-in pathway.** A positive FIA with PLR **`[x.xx]`** can justify dengue-protocol monitoring (hematocrit, platelets, warning-sign review) without waiting for ELISA. Pohekar and Bhalchandra reported an inverse relationship between FIA cutoff index (COI) and platelet count, raising the possibility that COI is not only a dichotomous diagnostic threshold but a crude severity correlate; this remains hypothesis-generating until confirmed [20].
- **Rule-out caution.** Because NS1 sensitivity falls in secondary infection and after day 3–4 [8,12–14], a negative FIA in a patient with warning signs or known prior dengue **must not** stop the dengue work-up. Sequential testing (FIA → IgM/IgG or RT-PCR) is the appropriate algorithm, analogous to combined NS1/IgM strategies that raise sensitivity in ICT meta-analyses [1,2].
- **Operator effects.** Visual ICT line-reading is a documented source of disagreement [8]. Automated FIA COI readout reduces that subjectivity — an advantage in shift-based ED staffing — provided the manufacturer cutoff is used without post-hoc adjustment (QUADAS-2 Domain 2) [22].

### 4.2.3 Low-resource and outbreak settings

ELISA remains preferable in equipped central laboratories: higher analytical standardization, batch efficiency during large runs, and (in several evaluations) higher or equivalent sensitivity [5–8,18]. It is poorly matched to:

- Primary health centers without plate readers, washers, or 2–8 °C storage for ELISA reagents
- Surge conditions in which batch queues exceed clinical time-to-decision
- Sites where specimen transport adds 6–24 hours [17]

FIA still requires electricity (or a charged analyzer), a functioning reader, and a cartridge cold- or ambient-chain per the IFU. It is therefore **near-POC**, not a zero-infrastructure test. Relative to ELISA it is more deployable; relative to visual ICT it is less so. National programs should treat FIA as a **tier**: visual ICT or FIA at the periphery; ELISA and RT-PCR at the reference laboratory; composite algorithms for severe or discordant cases [11,16,23].

### 4.2.4 Proposed placement in a diagnostic algorithm (pending our estimates)

Until Results are filled, the evidence-based placement is:

1. **Days 0–3, suspected dengue, any setting with a reader:** FIA NS1 as first-line. Positive → manage as laboratory-supported dengue; confirm with ELISA/RT-PCR as capacity allows (especially for surveillance and serotyping).
2. **Days 4–7 or suspected secondary infection:** FIA NS1 **plus** IgM (and IgG if secondary status is needed). Negative dual testing → RT-PCR or paired serology; do not exclude dengue on NS1 alone [1,7,13].
3. **Severe dengue, ICU, or medicolegal/surveillance confirmation:** RT-PCR and/or NS1 ELISA remain the reference, because FIA has not been shown to replace molecular diagnosis or serotype identification [7,16].
4. **Negative FIA, high clinical probability:** never used as a stop test.

`[After data: add a one-sentence statement of whether our pooled NLR supports or forbids standalone rule-out.]`

---

## 4.3 Strengths of This Meta-Analysis

Several features distinguish this review from prior dengue RDT syntheses.

**Technology-specific question.** Mata et al. and Haider et al. necessarily pooled visually read ICTs (and, in some cases, mixed antigen–antibody cartridges) [1,2]. FIA differs in signal generation (fluorescence vs. colloidal gold), interpretation (instrument COI vs. subjective lines), and operational footprint (reader vs. cassette-only). Mixing the two classes attenuates or inflates summary points and misleads procurement. Isolating FIA is the central contribution.

**PRISMA-DTA and PRISMA 2020 reporting.** Protocol registration before extraction, PIRD eligibility, PRISMA-S search documentation, dual independent screening and extraction with κ, and a pre-specified exclusion taxonomy address reproducibility standards for DTA reviews [24–26].

**QUADAS-2 tailored to NS1 kinetics.** Signalling questions were adapted for fever duration ≤7 days, IFU adherence, indeterminate COI handling, incorporation bias (ELISA as both comparator and sole reference), and reference-standard diagnostic window [22,27]. These are the biases most likely to distort dengue NS1 accuracy and are often under-specified in generic QUADAS-2 applications.

**Statistically appropriate pooling.** Univariate pooling of sensitivity and specificity separately, or DOR-only models, ignore the Se–Sp trade-off. We used the bivariate random-effects GLMM of Reitsma et al., equivalent (without covariates) to the HSROC model of Rutter and Gatsonis [28–30], with REML, bootstrap CIs for PLR/NLR/DOR, Deeks’ test rather than Egger’s test [15], and pre-specified subgroup and meta-regression analyses. The analysis code is archived (`analysis/dta_meta_analysis.R`) to allow exact replication once 2×2 data are locked.

**Head-to-head design.** Restricting the FIA–ELISA contrast to overlapping specimens avoids confounding by case-mix — a common threat when ELISA accuracy is taken from one literature and FIA from another.

**Clinical covariates specified a priori.** Primary vs. secondary infection, fever day, serotype, reference-standard tier, and platform were not post-hoc explorations; they follow NS1 biology [12–14].

---

## 4.4 Methodological and Clinical Limitations

### 4.4.1 Imperfect and heterogeneous reference standards

RT-PCR, virus isolation, composite algorithms, and NS1 ELISA are not interchangeable gold standards. ELISA-only reference (Tier 4) introduces **incorporation bias** when FIA is judged against the same analyte detected by a related immunoassay, typically inflating agreement [22]. Conversely, RT-PCR after the viremic window produces false-negative “truth,” misclassifying true dengue as non-dengue and **lowering apparent FIA sensitivity** [7,13]. Composite references reduce but do not eliminate differential verification (e.g., PCR only in FIA-positive patients). Our subgroup and sensitivity analyses by reference tier mitigate, but cannot fully correct, this spectrum of misclassification. Latent-class or Bayesian imperfect-gold-standard models [7] were not the primary analysis and would require a larger, more homogeneous evidence base.

### 4.4.2 Timing of sample collection

Even within the ≤7-day window, NS1 concentration is not constant [13,14]. Studies that report only a mixed mean fever day cannot be cleanly assigned to early vs. late strata, reducing power for the days 0–3 vs. 4–7 contrast. Residual mixing biases pooled sensitivity toward the average of two different biological states. We excluded convalescent-only cohorts, but we could not recover day-specific 2×2 tables when authors did not publish them.

### 4.4.3 Serotype effects and flavivirus cross-reactivity

NS1 secretion and assay capture antibodies vary by serotype; DENV-1 primary infection often yields higher detectable NS1 than DENV-2 [14], and DENV-4 has been associated with lower NS1 ELISA sensitivity in some evaluations [5,6]. Few FIA studies are powered for serotype-specific 2×2 tables; **`[if k < 4 per serotype, state that Hypothesis 3 remains unresolved]`**.

NS1 assays can cross-react with other flaviviruses, notably Zika virus, and less often yellow fever or Japanese encephalitis, depending on antibody clone and geography [8,16]. Endemic co-circulation (Americas: DENV/ZIKV; Asia: DENV/JEV) may inflate false-positive rates in a way that is invisible if “non-dengue” controls are healthy blood donors rather than patients with other acute flavivirus infections. Spectrum bias from healthy controls would **overestimate specificity** (QUADAS-2 applicability, Domain 1).

### 4.4.4 Primary versus secondary infection misclassification

IgM/IgG ratios, HI titers, and unpaired IgG are imperfect classifiers of immune status. Mislabeling secondary as primary (or the reverse) attenuates true Se differences and may explain residual heterogeneity even when a subgroup contrast is “non-significant.”

### 4.4.5 Threshold, platform, and industry involvement

FIA positivity is a COI cut-point. Manufacturer defaults were required for low Domain-2 RoB, but lot-to-lot and reader-model differences (e.g., STANDARD F200 vs. other analyzers) were rarely reported. Industry-supported evaluations may preferentially publish favorable lots. We recorded funding and conflicts; we could not exclude sponsorship bias.

### 4.4.6 Statistical and evidence-base constraints

- Expected **k** for FIA-specific studies is smaller than for ICT reviews (Mata: 57 studies; Haider: 15) [1,2]. Bivariate models with few studies yield imprecise τ² and wide prediction regions; a 95% prediction region that is much larger than the confidence region means the next study may not replicate the summary point.
- Continuity correction (0.5) for zero cells is conventional but arbitrary; we examined 0.1 and 1.0 in sensitivity analysis.
- Univariable meta-regression only: multivariable bivariate models are underpowered when k is modest.
- English-language dominance in indexed dengue diagnostics may miss regional FIA evaluations in local journals despite the absence of language limits.
- Preprints and abstracts, if included, are down-weighted in sensitivity analysis but can still affect the primary model.
- **`[If Deeks p < 0.10:]`** Small-study effects may reflect true heterogeneity (outbreak vs. endemic mix) rather than unpublished negative studies; we cannot distinguish these.

### 4.4.7 What this review does not estimate

We did not meta-analyze cost-effectiveness, COI–severity correlation, or combined FIA NS1+IgM/IgG cartridges unless NS1 could be isolated. We did not evaluate FIA for blood-donor screening or for pre-vaccination serostatus (IgG), where the target condition differs [16]. Generalizability to neonates, highly immunocompromised hosts, and non-endemic returning travelers is limited if those groups were sparse in included cohorts.

---

## 4.5 Future Research Directions and Policy Recommendations

### 4.5.1 Research

1. **Prospective, paired, STARD-compliant studies** of FIA and ELISA on the same acute specimens, with RT-PCR (and serotype) as an independent reference, consecutive enrollment, and day-of-illness recorded to the day — not as a mean only [31].
2. **Secondary-infection strata** with a pre-specified immune-status definition (paired sera preferred) large enough for precise Se differences.
3. **Flavivirus challenge panels** (ZIKV, YFV, JEV, WNV) from the same region as the intended use, to bound FIA specificity in co-endemic areas [8,16].
4. **Reader-agnostic and lot-to-lot reproducibility** studies, including borderline COI values, reported as indeterminates rather than dropped.
5. **Impact studies**, not only accuracy: time-to-decision, admission rates, antibiotic use, and severe-dengue progression when FIA is added to usual care.
6. **Head-to-head FIA vs. visual ICT vs. ELISA vs. RT-PCR** in a single protocol, to complete the four-tier comparison this review can only approximate from the literature.
7. As dengue **vaccines** scale, diagnostic algorithms must separate infection from vaccine-induced serology; NS1 antigen (FIA or ELISA) may retain a larger role than IgM/IgG for acute diagnosis in vaccinated populations [16]. This should be an explicit stratum in future DTA studies.

### 4.5.2 Policy and implementation

- **Do not treat “rapid dengue test” as one product class.** Procurement specifications should separate visual ICT, FIA, ELISA, and NAAT, with independent performance data for NS1-only results.
- **Place FIA in near-POC triage** (ED, outbreak camps, district hospitals) where a 15-minute objective NS1 result changes monitoring, contingent on our pooled NLR **not** being used as a standalone rule-out.
- **Retain ELISA and RT-PCR** at reference laboratories for confirmation, serotyping, quality assurance of peripheral FIA, and discrepant results [7,11,23].
- **External quality assessment** should include FIA readers, not only ELISA plates, if FIA is scaled nationally.
- **WHO/national case definitions** for laboratory-confirmed dengue should state whether FIA NS1 is an accepted confirmatory assay or a screening assay requiring ELISA/NAAT confirmation; this review’s paired estimates are the empirical input to that decision **`[once filled]`**.

---

## 4.6 Conclusion

Early NS1 detection during the first week of fever is central to dengue care, yet ELISA’s accuracy is offset by infrastructure and delay, and visual ICT’s speed is offset by modest and operator-dependent sensitivity [1,2,5–8,17]. FIA was developed to occupy the gap between those poles.

This PRISMA-DTA review, using tailored QUADAS-2 and a bivariate Reitsma/HSROC model, found that FIA for dengue NS1 has pooled sensitivity **`[xx.x%]`** (95% CI `[ll]–[uu]`) and specificity **`[xx.x%]`** (95% CI `[ll]–[uu]`), with DOR **`[xxx]`** and AUC **`[0.xx]`**. Against ELISA on paired specimens, FIA was **`[comparable / slightly less sensitive / other — fill from Table 7]`**. Performance **`[was / was not]`** worse in secondary infection and **`[was / was not]`** better in the first three days of illness, in line with NS1 biology [12–14].

**Actionable insights:**

1. **Use FIA as a rapid, objective NS1 test for rule-in** in triage, emergency, and outbreak settings when a reader can be maintained — particularly in the early febrile window.
2. **Do not use a negative FIA to exclude dengue** in secondary infection, late acute presentation, or severe disease; reflex to IgM/IgG, ELISA, and/or RT-PCR.
3. **Do not equate FIA with visual ICT or with ELISA** in guidelines or tenders; they are different tests with different error profiles.
4. **Keep ELISA/RT-PCR as the laboratory reference** for confirmation, surveillance, and serotype-dependent public health action.
5. **Commission paired, day-stratified, serotype-aware studies** with independent molecular reference standards before making FIA the sole confirmatory test in national algorithms.

Until those studies accumulate, FIA is best understood as a **clinically useful near-point-of-care NS1 assay** that can shorten time-to-diagnosis toward ELISA-like objectivity without fully replacing laboratory confirmation.

---

## REFERENCES (Discussion)

1. Haider M, Yousaf S, Zaib A, Sarfraz A, Sarfraz Z, Cherrez-Ojeda I. Diagnostic accuracy of various immunochromatographic tests for NS1 antigen and IgM antibodies detection in acute dengue virus infection. *Int J Environ Res Public Health*. 2022;19(14):8756. doi:10.3390/ijerph19148756. PMID: 35886607.
2. Mata VE, Andrade CAF, Passos SRL, Hökerberg YHM, Fukuoka LVB, Silva SA. Rapid immunochromatographic tests for the diagnosis of dengue: a systematic review and meta-analysis. *Cad Saúde Pública*. 2020;36(6):e00225618. doi:10.1590/0102-311X00225618. PMID: 32520084. PROSPERO: CRD42014009885.
3. Ghogre S. Utility of fluorescence immunoassay in early diagnosis of dengue. *Int J Curr Res Rev*. 2021;14(1):116. doi:10.31782/ijcrr.2021.14116.
4. Chaiyo S, Wichit S, Chaiwattanarungruengpaisan S, et al. A performance comparison between fluorescent immunoassay and immunochromatography for rapid dengue detection in clinical specimens. *Sci Rep*. 2022;12:17476. doi:10.1038/s41598-022-21581-x. PMID: 36261530.
5. Da Silva NS, Undurraga EA, da Silva Telleria AR, et al. A meta-analysis of the diagnostic accuracy of two commercial NS1 antigen ELISA tests for early dengue virus detection. *PLoS One*. 2014;9(4):e94655. doi:10.1371/journal.pone.0094655. PMID: 24722258.
6. Guzman MG, Jaenisch T, Gaczkowski R, et al. Multi-country evaluation of the sensitivity and specificity of two commercially-available NS1 ELISA assays for dengue diagnosis. *PLoS Negl Trop Dis*. 2010;4(8):e811. doi:10.1371/journal.pntd.0000811. PMID: 20844768.
7. Pillay K, et al. Evaluating the performance of common reference laboratory tests for acute dengue diagnosis: a systematic review and meta-analysis of RT-PCR, NS1 ELISA, and IgM ELISA. *Lancet Microbe*. 2025;6(5):101088. doi:10.1016/j.lanmic.2025.101088. PROSPERO: CRD42022341552.
8. Hunsperger EA, Yoksan S, Buchy P, et al. Evaluation of commercially available diagnostic tests for the detection of dengue virus NS1 antigen and anti-dengue virus IgM antibody. *PLoS Negl Trop Dis*. 2014;8(10):e3171. doi:10.1371/journal.pntd.0003171. PMID: 25330157.
9. Jaeschke R, Guyatt GH, Sackett DL. Users' guides to the medical literature. III. How to use an article about a diagnostic test. B. What are the results and will they help me in caring for my patients? *JAMA*. 1994;271(9):703-707. doi:10.1001/jama.1994.03510330081039. PMID: 8309035.
10. Wilder-Smith A, Ooi EE, Horstick O, Wills B. Dengue. *Lancet*. 2019;393(10169):350-363. doi:10.1016/S0140-6736(18)32560-1. PMID: 30696575.
11. World Health Organization. *Dengue: Guidelines for Diagnosis, Treatment, Prevention and Control*. New Edition. Geneva: WHO; 2009.
12. Duong V, Ly S, Lorn Try P, et al. Clinical and virological factors influencing the performance of a NS1 antigen-capture assay and potential use as a marker of dengue disease severity. *PLoS Negl Trop Dis*. 2011;5(7):e1199. doi:10.1371/journal.pntd.0001199. PMID: 21750741.
13. Muller DA, Depelsenaire ACI, Young PR. Clinical and laboratory diagnosis of dengue virus infection. *J Infect Dis*. 2017;215(suppl_2):S13-S17. doi:10.1093/infdis/jiw649. PMID: 28403441.
14. Ainsworth HR, et al. Kinetics of NS1 and anti-NS1 IgG following dengue infection reveals likely early formation of immune complexes in secondary infected patients. *Sci Rep*. 2025;15:9874. doi:10.1038/s41598-025-91099-5.
15. Deeks JJ, Macaskill P, Irwig L. The performance of tests of publication bias and other sample size effects in systematic reviews of diagnostic test accuracy was assessed. *J Clin Epidemiol*. 2005;58(9):882-893. doi:10.1016/j.jclinepi.2005.01.016. PMID: 16085191.
16. Frazer JL, Norton R. Dengue: a review of laboratory diagnostics in the vaccine age. *J Med Microbiol*. 2024;73(5):001833. doi:10.1099/jmm.0.001833. PMID: 38717483.
17. Sharma A, et al. Assessing the readiness of rapid diagnostic tests for integration into the national dengue control strategy of India. *Discov Public Health*. 2026;23:46. doi:10.1186/s12982-026-02269-3.
18. Peeling RW, Artsob H, Pelegrino JL, et al. Evaluation of diagnostic tests: dengue. *Nat Rev Microbiol*. 2010;8(12 Suppl):S30-S38. doi:10.1038/nrmicro2459. PMID: 21548185.
19. SD Biosensor Inc. STANDARD F Dengue NS1 Ag FIA [package insert]. Suwon, South Korea: SD Biosensor; 2023.
20. Pohekar JA, Bhalchandra MH. Prospective study to compare results of FIA (fluorescent immunoassay) test with gold standard ELISA test in Dengue NS1 patients admitted in a tertiary care hospital. *Indian J Med Microbiol*. 2023;46:100376. doi:10.1016/j.ijmmb.2023.100376.
21. Simmons CP, Farrar JJ, Nguyen VV, Wills B. Dengue. *N Engl J Med*. 2012;366(15):1423-1432. doi:10.1056/NEJMra1110265. PMID: 22494122.
22. Whiting PF, Rutjes AW, Westwood ME, et al. QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies. *Ann Intern Med*. 2011;155(8):529-536. doi:10.7326/0003-4819-155-8-201110180-00009. PMID: 22007046.
23. World Health Organization. Dengue: global situation, surveillance and progress — 2024 update. *Wkly Epidemiol Rec*. 2024;99(50/52):665-678.
24. McInnes MDF, Moher D, Thombs BD, et al. Preferred reporting items for a systematic review and meta-analysis of diagnostic test accuracy studies: the PRISMA-DTA statement. *JAMA*. 2018;319(4):388-396. doi:10.1001/jama.2017.19163. PMID: 29362800.
25. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71. doi:10.1136/bmj.n71. PMID: 33782057.
26. Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to the PRISMA Statement for reporting literature searches in systematic reviews. *Syst Rev*. 2021;10(1):39. doi:10.1186/s13643-020-01542-z. PMID: 33499930.
27. Bossuyt PM, Reitsma JB, Bruns DE, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. *BMJ*. 2015;351:h5527. doi:10.1136/bmj.h5527. PMID: 26511519.
28. Reitsma JB, Glas AS, Rutjes AW, Scholten RJ, Bossuyt PM, Zwinderman AH. Bivariate analysis of sensitivity and specificity produces informative summary measures in diagnostic reviews. *J Clin Epidemiol*. 2005;58(10):982-990. doi:10.1016/j.jclinepi.2005.02.022. PMID: 16168343.
29. Rutter CM, Gatsonis CA. A hierarchical regression approach to meta-analysis of diagnostic test accuracy evaluations. *Stat Med*. 2001;20(19):2865-2884. doi:10.1002/sim.942. PMID: 11568945.
30. Harbord RM, Deeks JJ, Egger M, Whiting P, Sterne JA. A unification of models for meta-analysis of diagnostic accuracy studies. *Biostatistics*. 2007;8(2):239-251. doi:10.1093/biostatistics/kxl004. PMID: 16698768.
31. Cohen JF, Korevaar DA, Altman DG, et al. STARD 2015 guidelines for reporting diagnostic accuracy studies: explanation and elaboration. *BMJ Open*. 2016;6(11):e012799. doi:10.1136/bmjopen-2016-012799. PMID: 28137831.

---

*Manuscript version: 1.0 — Discussion, Limitations, and Conclusion*
*Prepared: August 2026*
*Pooled estimates from this review were not fabricated. Citation of Haider 2022, Mata 2020, and Frazer & Norton 2024 replaces earlier “Defined Health” placeholders used in the Introduction.*
