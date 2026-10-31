#!/usr/bin/env python3
"""README.md is hand-maintained and is the source of truth for what is listed: section, name, link,
language tag, description. This script writes it only under --fix-numbers, and then only the typed counts. It reads README.md, syncs data/skills.json
to it (README wins), checks the numbers quoted in the README prose against what it counts, and
generates everything derived: index.json, index.csv and the translated READMEs.

Inverted 2026-10-07. Before that README.md was generated from data/skills.json."""
import datetime
import json
import os
import re
import sys

import i18n


def gh_anchor(title):
    """Match GitHub's actual heading-to-anchor slug: strip non [\\w\\- ], lowercase, spaces->hyphens.
    Does NOT collapse consecutive hyphens — GitHub doesn't either."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")

# Ordered to follow the actual research lifecycle (lit review -> data -> method/training ->
# execution/analysis -> visualization -> writing), not alphabetically or by "importance".
# No domain marker on any category — a category is not a boundary on what can go in it.
# Each category carries a one-line note saying what it is for and who would reach for it —
# a visitor from outside ML should be able to tell at a glance whether a section concerns them.
CATEGORIES = [
    ("ideation", "Direction Scanning & Ideation",
     "Turning a vague interest into a formulated, testable research question."),
    ("lit_review", "Literature Review",
     "Finding, reading, and synthesising prior work, and keeping citations honest."),
    ("study_design", "Study Design & Protocol",
     "Deciding what to measure and how, before any data is collected — protocols, ethics review, preregistration, sampling, instrument design."),
    ("method_theory", "Method Formalization & Theory",
     "Turning an idea into a stated method: formalizing claims, checking derivations, and writing and verifying proofs."),
    ("cv_data_annotation", "Data & Annotation",
     "Sourcing, labelling, curating, and auditing the data a study runs on."),
    ("model_training_finetuning", "Model Training & Fine-Tuning",
     "Training and adapting models, from single-GPU fine-tuning to distributed runs."),
    ("diagrams_schematics", "Diagrams & Schematics",
     "Architecture, pipeline, and concept figures — the drawn illustrations in a paper, as opposed to charts plotted from data."),
    ("experiment_repro", "Experiment Management & Reproducibility",
     "Running experiments, tracking what happened, and making the result reproducible by someone else."),
    ("statistical_analysis", "Statistical Analysis",
     "Choosing and running the analysis: regression, causal inference, survey weighting, meta-analysis, Bayesian modelling."),
    ("qualitative_methods", "Qualitative & Mixed Methods",
     "Interviews, fieldwork, and coded text — thematic analysis, grounded theory, ethnography, intercoder reliability."),
    ("interpretability", "Interpretability",
     "Opening up a trained model to see what it computes, and explaining individual predictions."),
    ("ml_plotting", "Paper-Grade Plotting & Visualization",
     "Charts plotted from results, to the standard a journal or conference expects."),
    ("writing_submission", "Writing & Submission",
     "Drafting the manuscript and getting it submission-ready — structure, formatting, venue adaptation, self-checks before it goes out."),
    ("peer_review_rebuttal", "Peer Review & Rebuttal",
     "The other side of submission: refereeing someone else's manuscript, and answering the reviews of your own."),
    ("end_to_end", "Full-Pipeline Suites",
     "Suites spanning several lifecycle stages at once."),
]


ENTRY = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>https://github\.com/[^)]+)\)(?: `(?P<lang>[a-z-]+)`)? - (?P<desc>.+)$")


def url_of(e):
    return f"https://github.com/{e['repo']}/tree/HEAD/{e['path']}" if e.get("path") else f"https://github.com/{e['repo']}"


def read_readme(path="README.md"):
    """Parse the hand-written README into (title_line, [entry dicts in page order])."""
    title_to_key = {title: key for key, title, _ in CATEGORIES}
    lines = open(path, encoding="utf-8").read().split("\n")
    rows, cat = [], None
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            cat = title_to_key.get(line[3:].strip())  # None for Contents / How these... / Contributing
            continue
        if line.startswith("- [") and cat:
            m = ENTRY.match(line)
            if not m:
                raise SystemExit(f"README.md:{n}: entry line does not match '- [Name](url) - Description.'")
            rows.append({"category": cat, **m.groupdict()})
    return lines[0], rows


def sync(skills, rows):
    """Make data/skills.json agree with README.md. README wins on name, description, category,
    language tag, and on which entries exist. Verification and audit data stay with the entry."""
    by_url = {url_of(e): e for e in skills}
    ids = {e["id"] for e in skills}
    out, added, changed = [], [], []
    for r in rows:
        e = by_url.pop(r["url"], None)
        if e is None:
            m = re.match(r"https://github\.com/([^/]+/[^/]+)(?:/tree/HEAD/(.+))?$", r["url"])
            if not m:
                raise SystemExit(f"README.md: cannot read repo/path from {r['url']}")
            base = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
            i, k = base, 2
            while i in ids:
                i, k = f"{base}-{k}", k + 1
            ids.add(i)
            e = {"id": i, "name": r["name"], "repo": m.group(1), "path": m.group(2) or "", "description": r["desc"],
                 "category": r["category"], "form": "skill", "disclosure": [], "added": datetime.date.today().isoformat(),
                 "verification": {}, "audit": {"level": "static", "date": datetime.date.today().isoformat()}}
            added.append(i)
        for field, val in (("name", r["name"]), ("description", r["desc"]), ("category", r["category"])):
            if e.get(field) != val:
                changed.append(f"{e['id']}.{field}")
                e[field] = val
        if r["lang"]:
            e["lang"] = r["lang"]
        else:
            e.pop("lang", None)
        out.append(e)
    removed = list(by_url.values())
    return out, added, changed, removed


NUMBER_CHECKS = [(r"badge/skills-(\d+)-", "n"), (r"(?m)^(\d+) skills, read", "n"), (r"(\d+) have also been walked", "a"),
                 (r"`static check` \((\d+) of \d+\)", "s"), (r"`static check` \(\d+ of (\d+)\)", "n"),
                 (r"`audited` \((\d+) of \d+\)", "a"), (r"`audited` \(\d+ of (\d+)\)", "n"),
                 (r"(\d+)% of these skills", "m")]


def check_numbers(readme, stats):
    """The README quotes a few counts in prose. They are typed by hand, so check them."""
    return [f"README.md says {m.group(1)} where the count is {stats[k]} (pattern: {rx})"
            for rx, k in NUMBER_CHECKS for m in [re.search(rx, readme)] if m and int(m.group(1)) != stats[k]]


def fix_numbers(readme, stats):
    """Rewrite only the typed counts. Entry lines and descriptions stay hand-written."""
    for rx, k in NUMBER_CHECKS:
        m = re.search(rx, readme)
        if m:
            readme = readme[:m.start(1)] + str(stats[k]) + readme[m.end(1):]
    return readme


def from_index():
    """Rebuild entries from the published index.json, for CI: data/skills.json stays private."""
    entries = []
    for r in json.load(open("index.json"))["entries"]:
        e = {k: r[k] for k in ("id", "name", "category", "repo", "path", "description", "form")}
        if r.get("lang") != "en":
            e["lang"] = r["lang"]
        e["disclosure"] = [x for x in r["required_capabilities"].split("|") if x]
        e["verification"] = {k: r[k] for k in ("license", "license_scope", "repo_license", "license_conflict", "capabilities",
                                               "repo_stars", "stars_scope", "path_last_commit", "stale", "checked_at")
                             if r.get(k) is not None}
        e["audit"] = {"level": r.get("audit_level"), "verdict": r.get("audit_verdict")}
        entries.append(e)
    return entries


def write_exports(skills):
    """Machine-readable copies of the catalog, generated with the README from the same source.
    A directory nobody can query is a directory nobody integrates."""
    import csv
    rows = []
    for e in skills:
        v = e.get("verification", {})
        rows.append({
            "id": e["id"], "name": e["name"], "category": e["category"],
            "repo": e["repo"], "path": e["path"],
            "url": f"https://github.com/{e['repo']}/tree/HEAD/{e['path']}" if e.get("path") else f"https://github.com/{e['repo']}",
            "description": e["description"], "form": e.get("form", "skill"),
            "lang": e.get("lang", "en"),
            "required_capabilities": "|".join(e.get("disclosure", [])),
            "license": v.get("license"), "license_scope": v.get("license_scope"),
            "repo_license": v.get("repo_license"), "license_conflict": v.get("license_conflict"),
            "capabilities": [dict(c) for c in v.get("capabilities", [])],
            "repo_stars": v.get("repo_stars"),
            "stars_scope": v.get("stars_scope"),
            "path_last_commit": v.get("path_last_commit"), "stale": v.get("stale"),
            "checked_at": v.get("checked_at"),
            "audit_level": e.get("audit", {}).get("level"),
            "audit_verdict": e.get("audit", {}).get("verdict"),
        })
    with open("index.json", "w") as f:
        json.dump({"count": len(rows), "generated_from": "data/skills.json", "entries": rows}, f, indent=1)
    with open("index.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    private = os.path.exists("data/skills.json")
    if private:
        with open("data/skills.json") as f:
            skills = json.load(f)
    else:
        skills = from_index()
    title_line, rows = read_readme()
    skills, added, changed, removed = sync(skills, rows)
    if removed and private:
        with open(f"data/audits/removed-from-readme-{datetime.date.today().isoformat()}.json", "a") as f:
            json.dump(removed, f, indent=1, ensure_ascii=False)
    if private:
        with open("data/skills.json", "w") as f:
            f.write(json.dumps(skills, indent=2, ensure_ascii=False) + "\n")
    for label, items in (("added from README", added), ("updated from README", changed), ("removed (not in README)", [e["id"] for e in removed])):
        if items:
            print(f"sync: {label}: {', '.join(items)}")
    if added and private:
        print("sync: new entries need `python3 scripts/verify.py --write`")

    by_cat = {}
    for e in skills:
        by_cat.setdefault(e["category"], []).append(e)
    audited_n = sum(1 for e in skills if e.get("audit", {}).get("level") == "hands_on")
    # Every subpath entry is monorepo-scoped (validate.py), so this also holds before verify.py has run.
    monorepo_pct = round(100 * sum(1 for e in skills if e.get("path")) / len(skills))
    checked_dates = [e.get("verification", {}).get("checked_at") for e in skills if e.get("verification", {}).get("checked_at")]
    stats = {"n": len(skills), "a": audited_n, "s": len(skills) - audited_n,
             "d": max(checked_dates) if checked_dates else "unverified", "m": monorepo_pct}

    write_exports(skills)
    missing = i18n.render_all(skills, by_cat, CATEGORIES, title_line + "\n", url_of, stats)
    for lang, n in missing.items():
        if n:
            print(f"i18n: {n} entries in {lang} fall back to English (untranslated or source changed)")
    print(f"Read README.md: {len(skills)} entries across {len(by_cat)} categories.")
    readme = open("README.md", encoding="utf-8").read()
    if "--fix-numbers" in sys.argv:
        readme = fix_numbers(readme, stats)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)
    problems = check_numbers(readme, stats)
    for p in problems:
        print("NUMBER MISMATCH:", p)
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
