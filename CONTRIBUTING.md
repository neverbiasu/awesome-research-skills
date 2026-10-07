# Contribution Guidelines

## Suggesting an entry

Open an issue or PR with:

- Link to the `SKILL.md` (repo + path)
- One objective sentence describing what it does — not marketing copy, doesn't restate the entry's own name
- Why it belongs here: aimed at people doing their own research, not a full autoresearch/autonomous-pipeline product

`README.md` is maintained by hand and is the source of truth for what is listed, so a PR that edits it directly is fine: add one line, `- [Name](link to the skill directory) - Description.`, in the section where it belongs, keeping the section alphabetical. Leave `README.zh-CN.md`, `README.ja.md`, `README.ko.md`, `index.json` and `index.csv` alone — those are generated from `README.md`.

## What belongs on this list

- Only awesome is awesome — this is a curation, not a collection. If it can't be personally recommended, it doesn't belong.
- Must be a `SKILL.md`-format Agent Skill (or a small suite of them), aimed at people doing their own research — not a full autoresearch/autonomous-pipeline product.
- No unmaintained, archived, or doc-less repos.
- No duplicates — check the current README first.

## Style

- Follows the [sindresorhus/awesome](https://github.com/sindresorhus/awesome/blob/main/awesome.md) conventions this list is built on: consistent formatting, no hard-wrapping, no CI badges, no "Inspired by Awesome" links.
- Category order follows the research lifecycle (ideation → literature → data → training → execution/analysis → visualization → writing), not alphabetical order. New categories go in lifecycle order, not appended at the end.
- Category names avoid domain branding (no "CV"/"ML" in titles) — this list isn't scoped to any one research domain.

## License

This list (`README.md` and all curation text) is released under [CC0](LICENSE) — public domain. Linked skills retain whatever license their own repo declares.
