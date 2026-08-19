#!/usr/bin/env python3
"""Render the combined manuscript Markdown to a journal-style PDF via HTML + Chrome."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "FIA_vs_ELISA_Dengue_NS1_MetaAnalysis.md"
HTML_PATH = ROOT / "_manuscript_preview.html"
PDF_PATH = ROOT / "FIA_vs_ELISA_Dengue_NS1_MetaAnalysis.pdf"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

CSS = """
@page {
  size: A4;
  margin: 22mm 18mm 24mm 18mm;
}
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Times New Roman", Times, Georgia, serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #111;
  max-width: 180mm;
  margin: 0 auto;
}
h1 {
  font-size: 16pt;
  line-height: 1.25;
  margin: 0 0 12pt 0;
  text-align: center;
}
h2 {
  font-size: 13pt;
  margin: 18pt 0 8pt 0;
  border-bottom: 0.6pt solid #333;
  padding-bottom: 2pt;
  page-break-after: avoid;
}
h3 {
  font-size: 11.5pt;
  font-style: italic;
  margin: 14pt 0 6pt 0;
  page-break-after: avoid;
}
p { margin: 0 0 8pt 0; text-align: justify; hyphens: auto; }
strong { font-weight: 700; }
em { font-style: italic; }
ul, ol { margin: 0 0 10pt 18pt; }
li { margin-bottom: 3pt; }
hr {
  border: 0;
  border-top: 0.4pt solid #999;
  margin: 14pt 0;
}
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 8.5pt;
  line-height: 1.3;
  margin: 8pt 0 12pt 0;
  page-break-inside: auto;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th, td {
  border: 0.5pt solid #444;
  padding: 3.5pt 5pt;
  vertical-align: top;
  text-align: left;
}
th { background: #f0f0f0; font-weight: 700; }
pre, code {
  font-family: "Courier New", Courier, monospace;
  font-size: 8.5pt;
}
pre {
  white-space: pre-wrap;
  word-break: break-word;
  background: #f7f7f7;
  border: 0.4pt solid #ccc;
  padding: 8pt;
  margin: 8pt 0 12pt 0;
}
blockquote {
  margin: 8pt 0 12pt 12pt;
  padding-left: 8pt;
  border-left: 2pt solid #888;
  color: #333;
}
"""


def strip_yaml(text: str) -> str:
    if text.startswith("---"):
        match = re.match(r"^---\n.*?\n---\n+", text, flags=re.S)
        if match:
            return text[match.end() :]
    return text


def md_to_html(md_text: str) -> str:
    body = markdown.markdown(
        strip_yaml(md_text),
        extensions=["tables", "fenced_code", "sane_lists", "smarty"],
        output_format="html5",
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>FIA vs ELISA for dengue NS1 antigen detection</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    if not CHROME.exists():
        raise SystemExit("Google Chrome not found; cannot print PDF.")
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def main() -> int:
    md_text = MD_PATH.read_text(encoding="utf-8")
    HTML_PATH.write_text(md_to_html(md_text), encoding="utf-8")
    html_to_pdf(HTML_PATH, PDF_PATH)
    HTML_PATH.unlink(missing_ok=True)
    size_kb = PDF_PATH.stat().st_size / 1024
    print(f"Wrote {PDF_PATH.name} ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
