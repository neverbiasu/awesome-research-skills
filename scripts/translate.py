"""Machine-translate entry descriptions that are missing or stale in data/i18n/<lang>.tsv.

  python3 scripts/translate.py                  # translate what i18n.py would fall back on
  python3 scripts/translate.py --approve zh ID… # human checked these rows (no IDs = all of zh)

Needs TRANSLATE_API_KEY, TRANSLATE_BASE_URL (OpenAI-compatible, e.g. .../v1) and TRANSLATE_MODEL. Every row it writes is
listed in data/i18n/review.json as pending human review until --approve removes it."""
import json
import os
import sys
import urllib.request

LANGS = {"zh": "Simplified Chinese", "ja": "Japanese", "ko": "Korean"}
D = "data/i18n"
REVIEW = f"{D}/review.json"


def read_tsv(lang):
    p = f"{D}/{lang}.tsv"
    if not os.path.exists(p):
        return {}
    return dict(l.rstrip("\n").split("\t", 1) for l in open(p, encoding="utf-8") if "\t" in l)


def write_tsv(lang, rows):
    with open(f"{D}/{lang}.tsv", "w", encoding="utf-8") as f:
        f.writelines(f"{i}\t{t}\n" for i, t in sorted(rows.items()))


def dump(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


def ask(lang, items, examples):
    key, base, model = (os.environ.get(f"TRANSLATE_{v}") for v in ("API_KEY", "BASE_URL", "MODEL"))
    if not (key and base and model):
        sys.exit("Set TRANSLATE_API_KEY, TRANSLATE_BASE_URL and TRANSLATE_MODEL; refusing to write translations.")
    ex = "\n".join(f"EN: {e}\n{lang.upper()}: {t}" for e, t in examples)
    prompt = (
        f"Translate each English description of an AI agent research skill into {LANGS[lang]}.\n"
        "Keep code spans, file names, product/library names and terms like SKILL.md, MCP, LaTeX, GPU as-is. "
        "One sentence each, objective tone, matching these existing rows:\n\n"
        f"{ex}\n\nReturn only a JSON object mapping each id to its translation.\n\n"
        + json.dumps(items, ensure_ascii=False, indent=1))
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(f"{base.rstrip('/')}/chat/completions", body, {  # any OpenAI-compatible endpoint
        "authorization": f"Bearer {key}", "content-type": "application/json"})
    text = json.load(urllib.request.urlopen(req, timeout=300))["choices"][0]["message"]["content"]
    out = json.loads(text[text.index("{"):text.rindex("}") + 1])
    missing = set(items) - set(out)
    if missing:
        sys.exit(f"{lang}: model returned no translation for {sorted(missing)}; nothing written.")
    return {i: " ".join(out[i].split()) for i in items}  # tsv rows must stay single-line


def main():
    review = json.load(open(REVIEW)) if os.path.exists(REVIEW) else {}
    if sys.argv[1:2] == ["--approve"]:
        lang, ids = sys.argv[2], set(sys.argv[3:])
        review[lang] = sorted(i for i in review.get(lang, []) if ids and i not in ids)
        dump(REVIEW, {k: v for k, v in review.items() if v})
        return
    cur = {e["id"]: e["description"] for e in json.load(open("index.json"))["entries"]}
    src = json.load(open(f"{D}/src.json"))
    tsv = {l: read_tsv(l) for l in LANGS}
    # src.json is shared by all languages, so a stale source means retranslating every language
    stale = {i for i in cur if src.get(i) != cur[i] or any(i not in tsv[l] for l in LANGS)}
    if not stale:
        print("translate: nothing to do")
        return
    items = {i: cur[i] for i in sorted(stale)}
    todo = {}
    for lang in LANGS:
        examples = [(src[i], tsv[lang][i]) for i in sorted(tsv[lang]) if i in src and i not in stale][:8]
        # A brand-new id that already has a row was translated by the PR author: keep it.
        todo[lang] = {i: t for i, t in items.items() if i in src or i not in tsv[lang]}
        if todo[lang]:
            tsv[lang].update(ask(lang, todo[lang], examples))
    for lang in LANGS:  # write only after every language succeeded
        write_tsv(lang, tsv[lang])
        review[lang] = sorted(set(review.get(lang, [])) | set(todo[lang]))
    src.update(items)
    dump(f"{D}/src.json", src)
    dump(REVIEW, review)
    print(f"translate: {len(stale)} entries x {len(LANGS)} languages, marked pending in {REVIEW}")


if __name__ == "__main__":
    main()
