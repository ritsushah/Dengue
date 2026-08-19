# ScienceDirect

**Search date:** 19 August 2026  
**Interface:** ScienceDirect Advanced Search via University of Toledo OpenAthens (`sciencedirect.com/search`)  
**Field:** Title, abstract or author-specified keywords (`tak`)

**Vendor limit:** ScienceDirect allows a maximum of 8 Boolean connectors per field. The full protocol `tak()` string was rejected (`Entry is too long`). The executed query keeps the five protocol blocks with reduced synonyms:

```
(dengue OR DENV) AND NS1 AND (FIA OR ELISA OR "fluorescence immunoassay" OR Platelia) AND (sensitivity OR specificity)
```

**Hits:**
- 88 before article-type filter
- **75** after protocol filter: Research articles (73) + Review articles (2)

**Results URL:**  
https://www.sciencedirect.com/search?tak=%28dengue+OR+DENV%29+AND+NS1+AND+%28FIA+OR+ELISA+OR+%22fluorescence+immunoassay%22+OR+Platelia%29+AND+%28sensitivity+OR+specificity%29&articleTypes=FLA%2CREV&show=100

Files: `sciencedirect_records_2026-08-19.ris`, `.csv`; parsed JSON in `data/raw/sciencedirect/`.
