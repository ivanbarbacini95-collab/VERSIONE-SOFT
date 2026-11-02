#!/usr/bin/env python3
"""Install the global INJ Node Tech Soft visual layer without changing app logic."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
CSS_SOURCE = ROOT / ".soft" / "tech-soft.css"
CSS_OUTPUT = ROOT / "tech-soft.css"
CSS_TAG = '<link rel="stylesheet" href="./tech-soft.css?v=20261102-tech-soft-1" data-inj-tech-soft="true">'
updated = []
shutil.copyfile(CSS_SOURCE, CSS_OUTPUT)

for html_file in sorted(ROOT.glob("*.html")):
    old = html_file.read_text(encoding="utf-8")
    if not re.search(r"</head\s*>", old, flags=re.I):
        continue
    fresh = re.sub(
        r"(<html\b)(?![^>]*\bdata-inj-soft=)",
        r'\1 data-inj-soft="true"',
        old,
        count=1,
        flags=re.I,
    )
    fresh = re.sub(
        r'\s*<link[^>]+data-inj-tech-soft="true"[^>]*>',
        "",
        fresh,
        flags=re.I,
    )
    fresh = re.sub(r"</head\s*>", "\n" + CSS_TAG + "\n</head>", fresh, count=1, flags=re.I)
    if fresh != old:
        html_file.write_text(fresh, encoding="utf-8")
        updated.append(html_file.name)

print("Tech Soft stylesheet:", CSS_OUTPUT.name)
print("Tech Soft applied to", len(updated), "HTML entry points")
for path in updated:
    print(" •", path)

if "index.html" not in updated:
    raise SystemExit("ERROR: index.html not themed")
if not (ROOT / "app.js").is_file() or not (ROOT / "treasury.js").is_file():
    raise SystemExit("ERROR: official application bundle missing")
