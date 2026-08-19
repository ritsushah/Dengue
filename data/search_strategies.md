# Comprehensive Database-Specific Search Strategies

**Review:** Diagnostic Accuracy of Fluorescence Immunoassay (FIA) versus Enzyme-Linked Immunosorbent Assay (ELISA) for Dengue Virus NS1 Antigen Detection: A Systematic Review and Meta-Analysis

**PROSPERO Registration:** [Pending]

**Search Date:** 19 August 2026 (PI override of the planned September 2026 lock)

**Reported in accordance with:** PRISMA-S (Rethlefsen et al., 2021, *Syst Rev*, 10:39, doi:10.1186/s13643-020-01542-z)

---

## Search Concept Framework

The search strategy is built around five core concepts combined with Boolean logic:

| Concept Block | Description | Operator |
|---------------|-------------|----------|
| **Block 1** | Target condition: Dengue virus infection | — |
| **Block 2** | Biomarker: NS1 antigen | AND |
| **Block 3** | Index test: Fluorescence immunoassay (FIA) | AND (Block 3 OR Block 4) |
| **Block 4** | Comparator test: ELISA | AND (Block 3 OR Block 4) |
| **Block 5** | Diagnostic accuracy filter | AND |

**Final combination:** Block 1 AND Block 2 AND (Block 3 OR Block 4) AND Block 5

**Rationale for combining Block 3 OR Block 4:** Studies evaluating FIA alone, ELISA alone, or both are eligible (the comparator arm may be the reference standard in some study designs). Using OR captures the broadest set of diagnostic accuracy studies on NS1 testing from which FIA-specific and head-to-head data can be extracted during screening.

**Filters/Limits:** No language, date, or publication type restrictions are applied.

---

## 1. PubMed / MEDLINE (via PubMed Interface)

**Interface:** PubMed (https://pubmed.ncbi.nlm.nih.gov/)
**Controlled vocabulary:** MeSH (Medical Subject Headings)
**Field tags:** `[MeSH Terms]`, `[tiab]` (title/abstract), `[tw]` (text word)

```
#1  DENGUE (Target Condition)
    "Dengue"[MeSH Terms]
    OR "Dengue Virus"[MeSH Terms]
    OR "Severe Dengue"[MeSH Terms]
    OR dengue[tiab]
    OR DENV[tiab]
    OR "dengue fever"[tiab]
    OR "dengue virus"[tiab]
    OR "dengue hemorrhagic fever"[tiab]
    OR "dengue haemorrhagic fever"[tiab]
    OR "dengue shock syndrome"[tiab]
    OR "break-bone fever"[tiab]
    OR "breakbone fever"[tiab]
    OR DENV-1[tiab]
    OR DENV-2[tiab]
    OR DENV-3[tiab]
    OR DENV-4[tiab]

#2  NS1 ANTIGEN (Biomarker)
    "Viral Nonstructural Proteins"[MeSH Terms]
    OR "NS1"[tiab]
    OR "NS-1"[tiab]
    OR "NS1 antigen"[tiab]
    OR "NS1 Ag"[tiab]
    OR "nonstructural protein 1"[tiab]
    OR "non-structural protein 1"[tiab]
    OR "nonstructural glycoprotein 1"[tiab]
    OR "non-structural glycoprotein 1"[tiab]
    OR "nonstructural protein-1"[tiab]
    OR "NS1 antigenemia"[tiab]
    OR "NS1 antigenaemia"[tiab]

#3  FLUORESCENCE IMMUNOASSAY (Index Test)
    "Fluorescence Immunoassay"[tiab]
    OR "fluorescent immunoassay"[tiab]
    OR "FIA"[tiab]
    OR "fluorescence-based immunoassay"[tiab]
    OR "time-resolved fluorescence immunoassay"[tiab]
    OR "TRFIA"[tiab]
    OR "TR-FIA"[tiab]
    OR "immunofluorescence assay"[tiab]
    OR "fluorescent lateral flow"[tiab]
    OR "fluorescence lateral flow"[tiab]
    OR "europium fluorescence"[tiab]
    OR "quantum dot immunoassay"[tiab]
    OR "STANDARD F"[tiab]
    OR "SD Biosensor"[tiab]
    OR "F200 analyzer"[tiab]
    OR "STANDARD F200"[tiab]
    OR "fluorescent rapid diagnostic"[tiab]
    OR "fluorescence rapid test"[tiab]
    OR "QUANTI CARD"[tiab]
    OR "Fluoroimmunoassay"[MeSH Terms]

#4  ELISA (Comparator / Reference Standard)
    "Enzyme-Linked Immunosorbent Assay"[MeSH Terms]
    OR "ELISA"[tiab]
    OR "enzyme linked immunosorbent assay"[tiab]
    OR "enzyme-linked immunosorbent assay"[tiab]
    OR "enzyme immunoassay"[tiab]
    OR "EIA"[tiab]
    OR "Platelia"[tiab]
    OR "Panbio"[tiab]
    OR "microwell ELISA"[tiab]
    OR "sandwich ELISA"[tiab]
    OR "capture ELISA"[tiab]
    OR "NS1 ELISA"[tiab]
    OR "Panbio Dengue Early ELISA"[tiab]
    OR "Platelia Dengue NS1 Ag"[tiab]
    OR "InBios DENV Detect"[tiab]
    OR "STANDARD E"[tiab]

#5  DIAGNOSTIC ACCURACY (Study Design / Outcome Filter)
    "Sensitivity and Specificity"[MeSH Terms]
    OR "Predictive Value of Tests"[MeSH Terms]
    OR "ROC Curve"[MeSH Terms]
    OR "Diagnostic Tests, Routine"[MeSH Terms]
    OR "Reference Standards"[MeSH Terms]
    OR sensitivity[tiab]
    OR specificity[tiab]
    OR "diagnostic accuracy"[tiab]
    OR "diagnostic performance"[tiab]
    OR "diagnostic test"[tiab]
    OR "predictive value"[tiab]
    OR "positive predictive value"[tiab]
    OR "negative predictive value"[tiab]
    OR "likelihood ratio"[tiab]
    OR "likelihood ratios"[tiab]
    OR "receiver operating characteristic"[tiab]
    OR "ROC curve"[tiab]
    OR "area under the curve"[tiab]
    OR "AUC"[tiab]
    OR "diagnostic odds ratio"[tiab]
    OR "true positive"[tiab]
    OR "false positive"[tiab]
    OR "true negative"[tiab]
    OR "false negative"[tiab]
    OR "accuracy"[tiab]
    OR "agreement"[tiab]
    OR "kappa"[tiab]
    OR "concordance"[tiab]
    OR "comparative study"[tiab]
    OR "evaluation"[tiab]
    OR "performance"[tiab]
    OR "validation"[tiab]

#6  FINAL COMBINATION
    #1 AND #2 AND (#3 OR #4) AND #5
```

**Filters:** None applied. No language, date, or publication type limits.

---

## 2. Embase (via Embase.com or Ovid Interface)

**Interface:** Embase.com (preferred) or Ovid Embase
**Controlled vocabulary:** Emtree
**Field tags:** `/exp` (Emtree explosion), `:ti,ab` (title, abstract), `:ti,ab,kw` (title, abstract, keywords)

### Embase.com Syntax

```
#1  DENGUE (Target Condition)
    'dengue'/exp
    OR 'dengue virus'/exp
    OR 'dengue fever'/exp
    OR 'severe dengue'/exp
    OR dengue:ti,ab
    OR denv:ti,ab
    OR 'dengue fever':ti,ab
    OR 'dengue virus':ti,ab
    OR 'dengue hemorrhagic fever':ti,ab
    OR 'dengue haemorrhagic fever':ti,ab
    OR 'dengue shock syndrome':ti,ab
    OR 'break-bone fever':ti,ab
    OR 'breakbone fever':ti,ab
    OR 'denv-1':ti,ab
    OR 'denv-2':ti,ab
    OR 'denv-3':ti,ab
    OR 'denv-4':ti,ab

#2  NS1 ANTIGEN (Biomarker)
    'dengue virus nonstructural protein 1'/exp
    OR 'nonstructural protein 1'/exp
    OR 'viral nonstructural protein'/exp
    OR ns1:ti,ab
    OR 'ns-1':ti,ab
    OR 'ns1 antigen':ti,ab
    OR 'ns1 ag':ti,ab
    OR 'nonstructural protein 1':ti,ab
    OR 'non-structural protein 1':ti,ab
    OR 'nonstructural glycoprotein 1':ti,ab
    OR 'non-structural glycoprotein 1':ti,ab
    OR 'ns1 antigenemia':ti,ab
    OR 'ns1 antigenaemia':ti,ab

#3  FLUORESCENCE IMMUNOASSAY (Index Test)
    'fluorescence immunoassay'/exp
    OR 'fluoroimmunoassay'/exp
    OR 'time resolved fluoroimmunoassay'/exp
    OR 'immunofluorescence'/exp
    OR 'fluorescence immunoassay':ti,ab
    OR 'fluorescent immunoassay':ti,ab
    OR fia:ti,ab
    OR 'fluorescence-based immunoassay':ti,ab
    OR 'time-resolved fluorescence immunoassay':ti,ab
    OR trfia:ti,ab
    OR 'tr-fia':ti,ab
    OR 'immunofluorescence assay':ti,ab
    OR 'fluorescent lateral flow':ti,ab
    OR 'fluorescence lateral flow':ti,ab
    OR 'europium fluorescence':ti,ab
    OR 'quantum dot immunoassay':ti,ab
    OR 'standard f':ti,ab
    OR 'sd biosensor':ti,ab
    OR 'f200 analyzer':ti,ab
    OR 'standard f200':ti,ab
    OR 'quanti card':ti,ab
    OR 'fluorescent rapid diagnostic':ti,ab
    OR 'fluorescence rapid test':ti,ab

#4  ELISA (Comparator / Reference Standard)
    'enzyme linked immunosorbent assay'/exp
    OR 'enzyme immunoassay'/exp
    OR elisa:ti,ab
    OR 'enzyme linked immunosorbent assay':ti,ab
    OR 'enzyme-linked immunosorbent assay':ti,ab
    OR 'enzyme immunoassay':ti,ab
    OR eia:ti,ab
    OR platelia:ti,ab
    OR panbio:ti,ab
    OR 'microwell elisa':ti,ab
    OR 'sandwich elisa':ti,ab
    OR 'capture elisa':ti,ab
    OR 'ns1 elisa':ti,ab
    OR 'panbio dengue early elisa':ti,ab
    OR 'platelia dengue ns1 ag':ti,ab
    OR 'inbios denv detect':ti,ab
    OR 'standard e':ti,ab

#5  DIAGNOSTIC ACCURACY (Study Design / Outcome Filter)
    'sensitivity and specificity'/exp
    OR 'diagnostic accuracy'/exp
    OR 'diagnostic test accuracy study'/exp
    OR 'predictive value'/exp
    OR 'receiver operating characteristic'/exp
    OR 'diagnostic test'/exp
    OR 'reference standard'/de
    OR sensitivity:ti,ab
    OR specificity:ti,ab
    OR 'diagnostic accuracy':ti,ab
    OR 'diagnostic performance':ti,ab
    OR 'diagnostic test':ti,ab
    OR 'predictive value':ti,ab
    OR 'positive predictive value':ti,ab
    OR 'negative predictive value':ti,ab
    OR 'likelihood ratio':ti,ab
    OR 'likelihood ratios':ti,ab
    OR 'receiver operating characteristic':ti,ab
    OR 'roc curve':ti,ab
    OR 'area under the curve':ti,ab
    OR auc:ti,ab
    OR 'diagnostic odds ratio':ti,ab
    OR 'true positive':ti,ab
    OR 'false positive':ti,ab
    OR 'true negative':ti,ab
    OR 'false negative':ti,ab
    OR accuracy:ti,ab
    OR agreement:ti,ab
    OR kappa:ti,ab
    OR concordance:ti,ab
    OR 'comparative study':ti,ab
    OR evaluation:ti,ab
    OR performance:ti,ab
    OR validation:ti,ab

#6  FINAL COMBINATION
    #1 AND #2 AND (#3 OR #4) AND #5

#7  EMBASE DEDUPLICATION (remove MEDLINE-indexed records if desired)
    #6 NOT ([medline]/lim)
```

**Note on deduplication:** Line #7 removes MEDLINE-indexed records from Embase results using the `[medline]/lim` tag. This is optional and used only if PubMed has already been searched and results are being combined across databases. If Embase is searched as a standalone database, omit line #7.

**Filters:** None applied.

---

## 3. Web of Science Core Collection (via Clarivate Analytics)

**Interface:** Web of Science Advanced Search
**Controlled vocabulary:** None (keyword-based; searches Keywords Plus and author keywords automatically via `TS=`)
**Field tags:** `TS=` (Topic: title + abstract + author keywords + Keywords Plus), `TI=` (Title only)

```
#1  DENGUE (Target Condition)
    TS=(dengue OR DENV OR "dengue fever" OR "dengue virus"
        OR "dengue hemorrhagic fever" OR "dengue haemorrhagic fever"
        OR "dengue shock syndrome" OR "break-bone fever"
        OR "breakbone fever" OR DENV-1 OR DENV-2 OR DENV-3 OR DENV-4)

#2  NS1 ANTIGEN (Biomarker)
    TS=(NS1 OR "NS-1" OR "NS1 antigen" OR "NS1 Ag"
        OR "nonstructural protein 1" OR "non-structural protein 1"
        OR "nonstructural glycoprotein 1" OR "non-structural glycoprotein 1"
        OR "NS1 antigenemia" OR "NS1 antigenaemia")

#3  FLUORESCENCE IMMUNOASSAY (Index Test)
    TS=("fluorescence immunoassay" OR "fluorescent immunoassay"
        OR FIA OR "fluorescence-based immunoassay"
        OR "time-resolved fluorescence immunoassay" OR TRFIA OR "TR-FIA"
        OR "immunofluorescence assay"
        OR "fluorescent lateral flow" OR "fluorescence lateral flow"
        OR "europium fluorescence" OR "quantum dot immunoassay"
        OR "STANDARD F" OR "SD Biosensor" OR "F200 analyzer"
        OR "STANDARD F200" OR "QUANTI CARD"
        OR "fluorescent rapid diagnostic" OR "fluorescence rapid test")

#4  ELISA (Comparator / Reference Standard)
    TS=(ELISA OR "enzyme linked immunosorbent assay"
        OR "enzyme-linked immunosorbent assay"
        OR "enzyme immunoassay" OR EIA
        OR Platelia OR Panbio OR "microwell ELISA"
        OR "sandwich ELISA" OR "capture ELISA"
        OR "NS1 ELISA" OR "Panbio Dengue Early ELISA"
        OR "Platelia Dengue NS1 Ag" OR "InBios DENV Detect"
        OR "STANDARD E")

#5  DIAGNOSTIC ACCURACY (Study Design / Outcome Filter)
    TS=(sensitivity OR specificity OR "diagnostic accuracy"
        OR "diagnostic performance" OR "diagnostic test"
        OR "predictive value" OR "positive predictive value"
        OR "negative predictive value" OR "likelihood ratio"
        OR "receiver operating characteristic" OR "ROC curve"
        OR "area under the curve" OR AUC
        OR "diagnostic odds ratio"
        OR "true positive" OR "false positive"
        OR "true negative" OR "false negative"
        OR accuracy OR agreement OR kappa OR concordance
        OR evaluation OR performance OR validation)

#6  FINAL COMBINATION
    #1 AND #2 AND (#3 OR #4) AND #5
```

**Indexes selected:** Science Citation Index Expanded (SCI-EXPANDED), Emerging Sources Citation Index (ESCI).

**Filters:** None applied. No language, date, or document type limits.

---

## 4. ScienceDirect (via Elsevier Advanced Search)

**Interface:** ScienceDirect Advanced Search (https://www.sciencedirect.com/search)
**Controlled vocabulary:** None (full-text semantic search)
**Field tags:** `tak()` or `Title-Abstr-Key()` (title, abstract, author keywords)
**Operators:** `AND`, `OR`, `NOT` (uppercase required). Proximity operators not supported.

### Primary Search Query

```
tak(dengue OR DENV OR "dengue fever" OR "dengue virus"
    OR "dengue hemorrhagic fever" OR "dengue shock syndrome")
AND
tak(NS1 OR "NS-1" OR "nonstructural protein 1"
    OR "non-structural protein 1" OR "NS1 antigen" OR "NS1 Ag")
AND
(
  tak("fluorescence immunoassay" OR "fluorescent immunoassay"
      OR FIA OR "time-resolved fluorescence immunoassay" OR TRFIA
      OR "immunofluorescence assay" OR "fluorescent lateral flow"
      OR "STANDARD F" OR "SD Biosensor" OR "QUANTI CARD")
  OR
  tak(ELISA OR "enzyme linked immunosorbent assay"
      OR "enzyme immunoassay" OR EIA
      OR Platelia OR Panbio OR "NS1 ELISA")
)
AND
tak(sensitivity OR specificity OR "diagnostic accuracy"
    OR "diagnostic performance" OR "predictive value"
    OR "likelihood ratio" OR "ROC" OR "area under the curve"
    OR "true positive" OR "false positive"
    OR "true negative" OR "false negative"
    OR accuracy OR agreement OR kappa OR validation)
```

**Note:** ScienceDirect search may return a large volume of results due to full-text indexing. The `tak()` field restricts searches to title, abstract, and author keywords only, improving precision. Results will be exported and deduplicated against PubMed and Embase records.

**Article type filter:** Research articles and Review articles only (conference abstracts excluded — these are better captured via Embase and Web of Science).

---

## 5. Google Scholar (Supplementary Search)

**Interface:** Google Scholar (https://scholar.google.com/)
**Controlled vocabulary:** None
**Field tags:** `allintitle:` (title only), `intitle:` (single term in title); general search queries are matched against full text
**Operators:** `AND` (implicit between terms), `OR`, `-` (NOT equivalent), `"..."` (exact phrase)

### Primary Search Query (Broad — Full Text)

```
("dengue" OR "DENV") AND ("NS1" OR "nonstructural protein 1")
AND ("fluorescence immunoassay" OR "FIA" OR "TRFIA"
     OR "fluorescent immunoassay" OR "immunofluorescence"
     OR "STANDARD F" OR "SD Biosensor")
AND ("ELISA" OR "enzyme-linked immunosorbent assay"
     OR "enzyme immunoassay")
AND ("sensitivity" OR "specificity" OR "diagnostic accuracy"
     OR "diagnostic test")
```

### Focused Search Query (Title-Restricted — Higher Precision)

```
allintitle: dengue NS1 fluorescence immunoassay ELISA diagnostic accuracy
```

### Supplementary Title Search Queries

```
Query A:  allintitle: dengue NS1 FIA sensitivity specificity
Query B:  allintitle: dengue NS1 fluorescence immunoassay
Query C:  allintitle: dengue NS1 "STANDARD F" OR "SD Biosensor"
Query D:  intitle:"fluorescence immunoassay" intitle:dengue intitle:NS1
```

**Screening protocol for Google Scholar:**
- The first **200 results** (sorted by relevance) from the Primary Search Query will be screened by title and available snippet text.
- Results will be exported using Publish or Perish software (Harzing, 2007) or a browser-based Google Scholar scraper that respects terms of service.
- All potentially eligible records will be cross-checked against records already retrieved from PubMed, Embase, Web of Science, and ScienceDirect to identify unique records.
- Google Scholar serves as a supplementary source; it is not the primary discovery database due to its lack of controlled vocabulary, inconsistent indexing, and inability to export complete bibliographic records natively.

---

## 6. Cochrane Library (Supplementary Search)

**Interface:** Cochrane Library (https://www.cochranelibrary.com/)
**Databases:** Cochrane Database of Systematic Reviews (CDSR), CENTRAL (Cochrane Central Register of Controlled Trials)
**Controlled vocabulary:** MeSH (shared with MEDLINE)

```
#1  MeSH descriptor: [Dengue] explode all trees
    OR MeSH descriptor: [Dengue Virus] explode all trees
    OR (dengue OR DENV OR "dengue fever" OR "dengue virus"):ti,ab,kw

#2  (NS1 OR "NS-1" OR "NS1 antigen" OR "nonstructural protein 1"
    OR "non-structural protein 1"):ti,ab,kw

#3  ("fluorescence immunoassay" OR "fluorescent immunoassay"
    OR FIA OR TRFIA OR "immunofluorescence assay"
    OR "STANDARD F" OR "SD Biosensor" OR "QUANTI CARD"):ti,ab,kw

#4  MeSH descriptor: [Enzyme-Linked Immunosorbent Assay] explode all trees
    OR (ELISA OR "enzyme linked immunosorbent assay"
    OR "enzyme immunoassay" OR Platelia OR Panbio):ti,ab,kw

#5  MeSH descriptor: [Sensitivity and Specificity] explode all trees
    OR MeSH descriptor: [Predictive Value of Tests] explode all trees
    OR (sensitivity OR specificity OR "diagnostic accuracy"
    OR "predictive value" OR "likelihood ratio"
    OR "ROC" OR "true positive" OR "false positive"):ti,ab,kw

#6  #1 AND #2 AND (#3 OR #4) AND #5
```

**Filters:** None.

---

## 7. Grey Literature & Additional Sources

| Source | Search Approach |
|--------|----------------|
| **ClinicalTrials.gov** | Search: Condition = "Dengue"; Other terms = "NS1" AND ("FIA" OR "fluorescence immunoassay" OR "ELISA"); Study type = Observational or Diagnostic |
| **WHO ICTRP** | Search: "dengue NS1 fluorescence immunoassay" and "dengue NS1 ELISA diagnostic accuracy" |
| **ProQuest Dissertations & Theses** | Search: ti(dengue) AND ti(NS1) AND ab("fluorescence immunoassay" OR "FIA" OR "ELISA") AND ab(sensitivity OR specificity OR "diagnostic accuracy") |
| **medRxiv / bioRxiv** | Search: "dengue NS1 fluorescence immunoassay" |
| **WHO Iris** | Search: "dengue diagnosis NS1" — for WHO technical guidance documents |
| **Manufacturer IFUs** | Direct retrieval from SD Biosensor (STANDARD F), Bio-Rad (Platelia), Abbott/Panbio product pages for package insert performance data |
| **Reference list screening** | Backward citation tracking of all included studies and identified systematic reviews |
| **Forward citation tracking** | Google Scholar "Cited by" function for key included studies |

---

## Search Validation

The search strategy has been validated by confirming retrieval of the following known eligible studies identified during preliminary scoping searches:

| Validation Study | Database(s) Retrieved |
|------------------|-----------------------|
| Pohekar JA, Bhalchandra MH (2023). *Indian J Med Microbiol*. doi:10.1016/j.ijmmb.2023.100376 | PubMed, Embase, ScienceDirect |
| Ghogre S (2021). *Int J Curr Res Rev*. doi:10.31782/ijcrr.2021.14116 | Google Scholar |
| Chaiyo S et al. (2022). *Sci Rep*. doi:10.1038/s41598-022-21581-x | PubMed, Embase, Web of Science |
| Pillay K et al. (2025). *Lancet Microbe*. doi:10.1016/j.lanmic.2025.101088 | PubMed, Embase, ScienceDirect |

All four validation studies were successfully retrieved by at least one database search strategy.

---

## Record Management

- All records will be exported in RIS or BibTeX format and imported into **Zotero** (version ≥6.0) or **EndNote** (version ≥21).
- Automated deduplication will be performed using the reference manager, followed by manual verification.
- Unique records will be transferred to **Rayyan QCRI** (https://rayyan.ai) or **Covidence** for blinded title/abstract screening.
- The PRISMA flow diagram will document the number of records identified, screened, assessed for eligibility, and included, with reasons for exclusion at the full-text stage.

---

## Methodological References for Search Strategy Design

1. Defined Health et al. PRISMA-S: an extension to the PRISMA Statement for reporting literature searches in systematic reviews. *Syst Rev*. 2021;10(1):39. doi:10.1186/s13643-020-01542-z
2. Defined Health et al. Searching for studies. In: Higgins JPT, Thomas J, eds. *Cochrane Handbook for Systematic Reviews of Interventions*. Version 6.4. Cochrane; 2023. Chapter 4.
3. McGowan J, Sampson M, Salzwedel DM, et al. PRESS Peer Review of Electronic Search Strategies: 2015 guideline statement. *J Clin Epidemiol*. 2016;75:40-46. doi:10.1016/j.jclinepi.2016.01.021

---

*Document version: 1.0*
*Prepared: August 2026*
