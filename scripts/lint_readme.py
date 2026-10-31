#!/usr/bin/env python3
"""PR check for README.md entry lines. Needs nothing but README.md."""
import re
import sys

import render

_, rows = render.read_readme()  # exits on a line that is not '- [Name](url) - Description.'
errors, seen, last = [], set(), {}
for r in rows:
    tag = r["name"]
    url = r["url"].lower()
    if url in seen:
        errors.append(f"{tag}: duplicate link")
    seen.add(url)
    if not re.fullmatch(r"https://github\.com/[^/]+/[^/]+(/tree/HEAD/.+)?", r["url"]):
        errors.append(f"{tag}: link must be the repo or /tree/HEAD/<skill directory>")
    if not (r["desc"][0].isupper() and r["desc"].endswith(".")):
        errors.append(f"{tag}: description must start uppercase and end with a period")
    if r["name"].casefold() < last.get(r["category"], ""):
        errors.append(f"{tag}: not in alphabetical order in its section")
    last[r["category"]] = r["name"].casefold()
for e in errors:
    print(f"::error file=README.md::{e}")
print(f"{len(rows)} entries, {len(errors)} problems")
sys.exit(1 if errors else 0)
