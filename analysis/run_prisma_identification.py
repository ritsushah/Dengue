#!/usr/bin/env python3
"""PRISMA-DTA identification searches executed 19 August 2026.

PubMed uses the same MEDLINE index as pubmed.ncbi.nlm.nih.gov (E-utilities,
no API key; polite-pool 3 req/s). OpenAlex and Crossref use public APIs.
Institutional vendor sites (Embase, WoS, ScienceDirect) are searched in the
browser and are not called here.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path("/Users/subasah/Desktop/Ritu-meta-analysis")
RAW = ROOT / "data" / "raw"
LOGS = ROOT / "data" / "logs"
IMP = ROOT / "data" / "imports"
SEARCH_DATE = "2026-08-19"
UA = "RituDengueNS1DTA/1.0 (systematic-review; mailto:not-provided)"

PUBMED_TERM = """
("Dengue"[MeSH Terms] OR "Dengue Virus"[MeSH Terms] OR "Severe Dengue"[MeSH Terms]
OR dengue[tiab] OR DENV[tiab] OR "dengue fever"[tiab] OR "dengue virus"[tiab]
OR "dengue hemorrhagic fever"[tiab] OR "dengue haemorrhagic fever"[tiab]
OR "dengue shock syndrome"[tiab] OR "break-bone fever"[tiab] OR "breakbone fever"[tiab]
OR DENV-1[tiab] OR DENV-2[tiab] OR DENV-3[tiab] OR DENV-4[tiab])
AND
("Viral Nonstructural Proteins"[MeSH Terms] OR "NS1"[tiab] OR "NS-1"[tiab]
OR "NS1 antigen"[tiab] OR "NS1 Ag"[tiab] OR "nonstructural protein 1"[tiab]
OR "non-structural protein 1"[tiab] OR "nonstructural glycoprotein 1"[tiab]
OR "non-structural glycoprotein 1"[tiab] OR "nonstructural protein-1"[tiab]
OR "NS1 antigenemia"[tiab] OR "NS1 antigenaemia"[tiab])
AND
(
("Fluorescence Immunoassay"[tiab] OR "fluorescent immunoassay"[tiab] OR "FIA"[tiab]
OR "fluorescence-based immunoassay"[tiab] OR "time-resolved fluorescence immunoassay"[tiab]
OR "TRFIA"[tiab] OR "TR-FIA"[tiab] OR "immunofluorescence assay"[tiab]
OR "fluorescent lateral flow"[tiab] OR "fluorescence lateral flow"[tiab]
OR "europium fluorescence"[tiab] OR "quantum dot immunoassay"[tiab]
OR "STANDARD F"[tiab] OR "SD Biosensor"[tiab] OR "F200 analyzer"[tiab]
OR "STANDARD F200"[tiab] OR "fluorescent rapid diagnostic"[tiab]
OR "fluorescence rapid test"[tiab] OR "QUANTI CARD"[tiab] OR "Fluoroimmunoassay"[MeSH Terms])
OR
("Enzyme-Linked Immunosorbent Assay"[MeSH Terms] OR "ELISA"[tiab]
OR "enzyme linked immunosorbent assay"[tiab] OR "enzyme-linked immunosorbent assay"[tiab]
OR "enzyme immunoassay"[tiab] OR "EIA"[tiab] OR "Platelia"[tiab] OR "Panbio"[tiab]
OR "microwell ELISA"[tiab] OR "sandwich ELISA"[tiab] OR "capture ELISA"[tiab]
OR "NS1 ELISA"[tiab] OR "Panbio Dengue Early ELISA"[tiab]
OR "Platelia Dengue NS1 Ag"[tiab] OR "InBios DENV Detect"[tiab] OR "STANDARD E"[tiab])
)
AND
("Sensitivity and Specificity"[MeSH Terms] OR "Predictive Value of Tests"[MeSH Terms]
OR "ROC Curve"[MeSH Terms] OR "Diagnostic Tests, Routine"[MeSH Terms]
OR "Reference Standards"[MeSH Terms]
OR sensitivity[tiab] OR specificity[tiab] OR "diagnostic accuracy"[tiab]
OR "diagnostic performance"[tiab] OR "diagnostic test"[tiab]
OR "predictive value"[tiab] OR "positive predictive value"[tiab]
OR "negative predictive value"[tiab] OR "likelihood ratio"[tiab]
OR "likelihood ratios"[tiab] OR "receiver operating characteristic"[tiab]
OR "ROC curve"[tiab] OR "area under the curve"[tiab] OR "AUC"[tiab]
OR "diagnostic odds ratio"[tiab] OR "true positive"[tiab] OR "false positive"[tiab]
OR "true negative"[tiab] OR "false negative"[tiab]
OR "accuracy"[tiab] OR "agreement"[tiab] OR "kappa"[tiab]
OR "concordance"[tiab] OR "comparative study"[tiab] OR "evaluation"[tiab]
OR "performance"[tiab] OR "validation"[tiab])
""".strip()

OPENALEX_SEARCH = (
    '(dengue OR DENV) AND (NS1 OR "nonstructural protein 1" OR "non-structural protein 1") '
    "AND (FIA OR \"fluorescence immunoassay\" OR \"fluorescent immunoassay\" OR TRFIA "
    'OR ELISA OR "enzyme-linked" OR Platelia OR Panbio) '
    'AND (sensitivity OR specificity OR "diagnostic accuracy" OR "diagnostic performance")'
)

CROSSREF_QUERY = (
    "dengue NS1 (fluorescence immunoassay OR FIA OR ELISA) "
    "(sensitivity OR specificity OR diagnostic accuracy)"
)


def http_json(url: str, data: bytes | None = None, delay: float = 0.4) -> dict | list:
    time.sleep(delay)
    req = urllib.request.Request(
        url,
        data=data,
        headers={"User-Agent": UA, "Accept": "application/json"},
        method="POST" if data else "GET",
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        raw = resp.read().decode("utf-8")
    return json.loads(raw)


def http_text(url: str, data: bytes | None = None, delay: float = 0.4) -> str:
    time.sleep(delay)
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8")


def pubmed_search() -> dict:
    params = urllib.parse.urlencode(
        {
            "db": "pubmed",
            "term": PUBMED_TERM,
            "retmax": "10000",
            "retmode": "json",
            "sort": "pub+date",
        }
    ).encode()
    payload = http_json(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        data=params,
        delay=0.4,
    )
    result = payload["esearchresult"]
    count = int(result["count"])
    ids = result.get("idlist", [])
    # if truncated, use history
    if count > len(ids):
        params2 = urllib.parse.urlencode(
            {
                "db": "pubmed",
                "term": PUBMED_TERM,
                "retmax": str(min(count, 10000)),
                "retmode": "json",
                "usehistory": "y",
            }
        ).encode()
        payload = http_json(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            data=params2,
        )
        result = payload["esearchresult"]
        ids = result.get("idlist", [])
        count = int(result["count"])
        webenv = result.get("webenv")
        query_key = result.get("querykey")
    else:
        webenv = result.get("webenv")
        query_key = result.get("querykey")

    summaries = []
    for i in range(0, len(ids), 200):
        chunk = ids[i : i + 200]
        q = urllib.parse.urlencode(
            {"db": "pubmed", "id": ",".join(chunk), "retmode": "json"}
        )
        data = http_json(
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?{q}"
        )
        uids = data["result"]["uids"]
        for uid in uids:
            rec = data["result"][uid]
            summaries.append(
                {
                    "pmid": uid,
                    "title": rec.get("title"),
                    "source": rec.get("source"),
                    "pubdate": rec.get("pubdate"),
                    "authors": [
                        a.get("name") for a in rec.get("authors", []) if a.get("name")
                    ][:12],
                    "doi": next(
                        (
                            x.get("value")
                            for x in rec.get("articleids", [])
                            if x.get("idtype") == "doi"
                        ),
                        None,
                    ),
                }
            )

    (IMP / "pubmed").mkdir(parents=True, exist_ok=True)
    (RAW / "pubmed").mkdir(parents=True, exist_ok=True)
    pmid_path = IMP / "pubmed" / f"pubmed_pmids_{SEARCH_DATE}.txt"
    json_path = RAW / "pubmed" / f"pubmed_esummary_{SEARCH_DATE}.json"
    pmid_path.write_text("\n".join(ids) + ("\n" if ids else ""), encoding="utf-8")
    json_path.write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    website_url = "https://pubmed.ncbi.nlm.nih.gov/?term=" + urllib.parse.quote(
        PUBMED_TERM
    )
    return {
        "source": "PubMed/MEDLINE",
        "interface": "pubmed.ncbi.nlm.nih.gov (same index via E-utilities; no API key)",
        "date": SEARCH_DATE,
        "count": count,
        "retrieved": len(summaries),
        "pmid_file": str(pmid_path.relative_to(ROOT)),
        "summary_file": str(json_path.relative_to(ROOT)),
        "website_url": website_url,
        "query": PUBMED_TERM,
    }


def openalex_search() -> dict:
    works = []
    cursor = "*"
    url_base = "https://api.openalex.org/works"
    while cursor:
        q = urllib.parse.urlencode(
            {
                "search": OPENALEX_SEARCH,
                "per_page": "200",
                "cursor": cursor,
                "mailto": "openalex@example.com",
            }
        )
        data = http_json(f"{url_base}?{q}", delay=0.2)
        works.extend(data.get("results", []))
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor or len(works) >= 2000:
            break
    slim = []
    for w in works:
        loc = w.get("primary_location") or {}
        src = loc.get("source") or {}
        slim.append(
            {
                "id": w.get("id"),
                "doi": w.get("doi"),
                "title": w.get("display_name"),
                "year": w.get("publication_year"),
                "cited_by": w.get("cited_by_count"),
                "venue": src.get("display_name"),
                "oa": (w.get("open_access") or {}).get("oa_status"),
            }
        )
    meta_count = None
    # first page meta
    q0 = urllib.parse.urlencode(
        {"search": OPENALEX_SEARCH, "per_page": "1", "mailto": "openalex@example.com"}
    )
    meta = http_json(f"{url_base}?{q0}", delay=0.2)
    meta_count = (meta.get("meta") or {}).get("count")
    out = RAW / "openalex" / f"openalex_works_{SEARCH_DATE}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(slim, indent=2), encoding="utf-8")
    (IMP / "openalex").mkdir(parents=True, exist_ok=True)
    (IMP / "openalex" / f"openalex_ids_{SEARCH_DATE}.txt").write_text(
        "\n".join(x["id"] for x in slim if x.get("id")) + "\n", encoding="utf-8"
    )
    return {
        "source": "OpenAlex",
        "date": SEARCH_DATE,
        "count": meta_count,
        "retrieved": len(slim),
        "file": str(out.relative_to(ROOT)),
        "query": OPENALEX_SEARCH,
    }


def crossref_search() -> dict:
    items = []
    cursor = "*"
    while True:
        q = urllib.parse.urlencode(
            {
                "query": CROSSREF_QUERY,
                "rows": "1000",
                "cursor": cursor,
                "mailto": "crossref@example.com",
            }
        )
        data = http_json(f"https://api.crossref.org/works?{q}", delay=0.3)
        msg = data.get("message") or {}
        batch = msg.get("items") or []
        items.extend(batch)
        cursor = msg.get("next-cursor")
        if not batch or not cursor or len(items) >= 2000:
            break
    slim = []
    for it in items:
        slim.append(
            {
                "doi": it.get("DOI"),
                "title": " ".join(it.get("title") or []),
                "container": " ".join(it.get("container-title") or []),
                "issued": ((it.get("issued") or {}).get("date-parts") or [[None]])[0],
                "type": it.get("type"),
            }
        )
    out = RAW / "crossref" / f"crossref_works_{SEARCH_DATE}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(slim, indent=2), encoding="utf-8")
    total = (data.get("message") or {}).get("total-results")
    return {
        "source": "Crossref",
        "date": SEARCH_DATE,
        "count": total,
        "retrieved": len(slim),
        "file": str(out.relative_to(ROOT)),
        "query": CROSSREF_QUERY,
    }


def clinicaltrials_search() -> dict:
    q = urllib.parse.urlencode(
        {
            "query.cond": "dengue",
            "query.term": "NS1 AND (FIA OR fluorescence OR ELISA OR immunoassay)",
            "pageSize": "100",
            "countTotal": "true",
        }
    )
    data = http_json(f"https://clinicaltrials.gov/api/v2/studies?{q}", delay=0.2)
    studies = []
    for s in data.get("studies", []):
        proto = (s.get("protocolSection") or {})
        ident = proto.get("identificationModule") or {}
        studies.append(
            {
                "nct": ident.get("nctId"),
                "title": ident.get("officialTitle") or ident.get("briefTitle"),
            }
        )
    out = RAW / "grey" / f"clinicaltrials_{SEARCH_DATE}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(studies, indent=2), encoding="utf-8")
    return {
        "source": "ClinicalTrials.gov",
        "date": SEARCH_DATE,
        "count": data.get("totalCount"),
        "retrieved": len(studies),
        "file": str(out.relative_to(ROOT)),
    }


def europepmc_preprints() -> dict:
    query = (
        '(dengue OR DENV) AND (NS1) AND (FIA OR "fluorescence immunoassay" '
        'OR ELISA) AND (sensitiv* OR specific* OR "diagnostic accuracy") '
        "AND (SRC:PPR)"
    )
    q = urllib.parse.urlencode(
        {"query": query, "format": "json", "pageSize": "1000", "resultType": "lite"}
    )
    data = http_json(
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{q}", delay=0.3
    )
    hits = (data.get("resultList") or {}).get("result") or []
    out = RAW / "grey" / f"europepmc_preprints_{SEARCH_DATE}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(hits, indent=2), encoding="utf-8")
    return {
        "source": "Europe PMC preprints (medRxiv/bioRxiv subset)",
        "date": SEARCH_DATE,
        "count": int(data.get("hitCount") or 0),
        "retrieved": len(hits),
        "file": str(out.relative_to(ROOT)),
        "query": query,
    }


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, fn in [
        ("pubmed", pubmed_search),
        ("openalex", openalex_search),
        ("crossref", crossref_search),
        ("clinicaltrials", clinicaltrials_search),
        ("europepmc_preprints", europepmc_preprints),
    ]:
        print(f"Running {name}...", flush=True)
        try:
            results[name] = fn()
            print(json.dumps({k: results[name][k] for k in results[name] if k != "query"}, indent=2), flush=True)
        except Exception as e:
            results[name] = {"source": name, "error": str(e)}
            print(f"ERROR {name}: {e}", flush=True)
    log = LOGS / f"search_run_{SEARCH_DATE}.json"
    log.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote {log}", flush=True)


if __name__ == "__main__":
    main()
