# Awesome Research Skills [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> 146 Agent Skills for researchers, read and chosen one at a time — every entry is one exact `SKILL.md` directory, not a repo that might contain something useful.

`146 skills` · `individually curated` · `37 hands-on audited` · `one exact SKILL.md path per entry`

For the steps you do yourself: finding prior work, designing the study, formalizing the method, curating data, running and auditing experiments, statistics, qualitative analysis, figures, writing, and peer review. Skills that automate the whole research loop are out of scope, as are MLOps and deployment tooling.

Entries are curated by reading the skill and checking it against its repository, not template-farmed or abandoned or moved elsewhere. Each one carries its own license, its subdirectory's last commit, and flags for what it needs to run — network, credentials, hooks. 37 have also been walked through by hand against the files they ship; what that does and does not guarantee is set out at the end of this page.

## Contents

- [Start here](#start-here)
- [Direction Scanning & Ideation](#direction-scanning--ideation)
- [Literature Review](#literature-review)
- [Study Design & Protocol](#study-design--protocol)
- [Method Formalization & Theory](#method-formalization--theory)
- [Data & Annotation](#data--annotation)
- [Model Training & Fine-Tuning](#model-training--fine-tuning)
- [Diagrams & Schematics](#diagrams--schematics)
- [Experiment Management & Reproducibility](#experiment-management--reproducibility)
- [Statistical Analysis](#statistical-analysis)
- [Qualitative & Mixed Methods](#qualitative--mixed-methods)
- [Interpretability](#interpretability)
- [Paper-Grade Plotting & Visualization](#paper-grade-plotting--visualization)
- [Writing & Submission](#writing--submission)
- [Peer Review & Rebuttal](#peer-review--rebuttal)
- [How these entries are checked](#how-these-entries-are-checked)

## Start here

One default and up to two alternatives per task, chosen by fit rather than by stars. Find the name in the catalog below for the link and the checked metadata.

**Find what has already been published**

|Skill                         |Best for                                                                     |In → out                                                              |
|------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
|**Nature Literature Pipeline**|A broad sweep across sources when you do not yet know the shape of the field |A topic or question → Scored, deduplicated candidate papers           |
|Surveying Literature          |A draft that may be missing prior art, graded by threat to your novelty claim|A paper draft with a bibliography → Missed-work list with novelty risk|
|SLR PRISMA                    |A formal systematic review that must satisfy PRISMA                          |A protocol and search strategy → PRISMA-compliant screening record    |

**Turn an interest into a research question**

|Skill                  |Best for                                                         |In → out                                                          |
|-----------------------|-----------------------------------------------------------------|------------------------------------------------------------------|
|**Research Gap Finder**|Grounding a direction in gaps the literature actually leaves open|Literature notes and early ideas → Gaps with testable entry points|
|Archora: Hypothesis    |Forcing a vague idea into a falsifiable statement                |Notes and context → Structured hypotheses                         |

**Design the study before collecting data**

|Skill                  |Best for                                               |In → out                                                   |
|-----------------------|-------------------------------------------------------|-----------------------------------------------------------|
|**Experimental Design**|General randomization, blocking, and factorial planning|Research question and constraints → A design specification |
|Power Analysis         |Deciding sample size and minimum detectable effect     |Effect size assumptions → Power curves and required n      |
|Preregister            |Locking the plan publicly before outcome data exists   |A finished design → OSF, AsPredicted, or AEA registry draft|

**Formalize the method or check the math**

|Skill                |Best for                                                     |In → out                                                                      |
|---------------------|-------------------------------------------------------------|------------------------------------------------------------------------------|
|**Derivation Verify**|A formula, estimator, or bound that later work will depend on|One atomic derived claim → Independent re-derivations and a convergence matrix|
|Verifying Proofs     |Auditing a proof or appendix you already wrote               |Theorem and proof text → Localized gaps, one per step                         |
|Formalize Problem    |Restating a claim in Lean 4 before proving anything          |An informal statement → Type-checking Lean statement at `sorry`               |

**Curate and audit the dataset**

|Skill                           |Best for                                                             |In → out                                                       |
|--------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------|
|**PhD Skills: Dataset Curation**|Checking bias, distribution, and fairness before training            |A dataset → Bias and distribution report                       |
|FiftyOne Dataset Curation       |Vision datasets, with schema, embeddings, and curated views          |An image or video dataset → FiftyOne views and quality findings|
|Geospatial Data QC              |Spatial data, where CRS and datum mismatches silently corrupt results|Raster, vector, or point data → Quantified integrity defects   |

**Run an ML experiment**

|Skill                      |Best for                                                       |In → out                                                           |
|---------------------------|---------------------------------------------------------------|-------------------------------------------------------------------|
|**PhD Skills: Launch**     |Getting a run started and tracked on your own machine or server|A training script and config → A launched, logged run              |
|Running Cluster Experiments|A multi-job campaign on a shared Slurm cluster                 |An experiment matrix and allocation → Sized, staged job submissions|
|Data Leakage Audit         |Before you trust any number the run produced                   |Pipeline and split definitions → Leakage findings by severity      |

**Reproduce someone else's paper**

|Skill                    |Best for                                                 |In → out                                                   |
|-------------------------|---------------------------------------------------------|-----------------------------------------------------------|
|**PhD Skills: Reproduce**|Working from an arXiv URL to a measurable replication run|A paper and its code, if any → A staged replication attempt|
|Paper2Code               |A paper with no usable released implementation           |The paper → Citation-anchored implementation               |

**Do the statistics**

|Skill                            |Best for                                                             |In → out                                                             |
|---------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
|**Guided Statistical Analysis**  |Choosing a test, checking its assumptions, and reporting effect sizes|A dataset and a question → Test choice, assumptions, effect sizes    |
|AER Identification               |Observational causal work — DiD, IV, RDD, synthetic control          |A design and data structure → Identification strategy and diagnostics|
|Meta-Analysis & Systematic Review|Pooling published evidence                                           |A protocol and extracted effects → Meta-analytic synthesis           |

**Analyze interviews or open-ended text**

|Skill                      |Best for                                                         |In → out                                                      |
|---------------------------|-----------------------------------------------------------------|--------------------------------------------------------------|
|**Thematic Analysis**      |Braun and Clarke reflexive thematic analysis, done by the book   |Transcripts → Themes with a quality checklist                 |
|Scholar Qualitative Toolkit|When the work must land in NVivo, ATLAS.ti, or MAXQDA            |Transcripts and a codebook → Coded data and reliability report|
|Analytic Memo Writing      |Keeping your developing interpretation as evidence-grounded memos|Coded units and reflections → An indexed memo bank            |

**Make the figures**

|Skill                              |Best for                                                           |In → out                                          |
|-----------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
|**Figures4Papers**                 |Charts plotted from results                                        |Result data → Publication-ready matplotlib figures|
|CCF-Figure                         |A concept or architecture diagram matched to your paper's mechanism|Method description → A diagram structure and draft|
|Nature Paper Skills: Figure Planner|Deciding what belongs in which figure before drawing anything      |Claims and results → One-claim-per-figure plan    |

**Write and revise the manuscript**

|Skill                            |Best for                                                |In → out                                          |
|---------------------------------|--------------------------------------------------------|--------------------------------------------------|
|**Research Paper Writing Skills**|Paragraph-level revision of an ML, CV, or NLP draft     |A draft → Clarity and structure edits             |
|Journal Adapt Writing Skill      |Retargeting a finished manuscript at a different venue  |Draft and target journal → Convention-adapted text|
|PaperFit: Overflow Repair        |LaTeX that overflows the template days before a deadline|A LaTeX project → Fixed overfull boxes            |

**Check your own claims before submitting**

|Skill                                |Best for                                               |In → out                                                   |
|-------------------------------------|-------------------------------------------------------|-----------------------------------------------------------|
|**PhD Skills: Paper Verification**   |Confirming the paper's numbers match the code and data |Paper, code, results → Numerical and terminology mismatches|
|Nature Paper Skills: Submission Audit|A late preflight across claims, figures, and references|A near-final manuscript → Preflight defect list            |

**Review a paper, or answer your reviewers**

|Skill                             |Best for                                                    |In → out                                         |
|----------------------------------|------------------------------------------------------------|-------------------------------------------------|
|**Academic Paper Reviewer**       |Refereeing a manuscript across several reviewer perspectives|A manuscript → A structured review               |
|Paper Lifecycle: Rebuttal Response|Turning reviews into an evidence-based response             |Reviews and your paper → Triaged rebuttal package|

## Direction Scanning & Ideation

*Turning a vague interest into a formulated, testable research question.*

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) - Analyzes literature and early ideas to identify grounded research gaps and testable entry points without forcing novelty claims. `skill` · MIT · repo ★347 · updated 2026-04-05 · checked 2026-09-06 · static check.

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - Guides generation of falsifiable, structured research hypotheses from user-provided notes and content. `skill` · MIT · repo ★47 · updated 2026-05-15 · checked 2026-09-06 · static check.

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - Structures research project initiation through 5W1H brainstorming, systematic literature review, multi-dimensional gap analysis, and SMART research-question formulation. `skill` `external` · MIT · repo ★5341 · updated 2026-05-13 · checked 2026-09-06 · static check.

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - Applies structured ideation frameworks to surface research directions when entering a new problem space or reconsidering a project's direction. `skill` · MIT · repo ★12358 · updated 2026-02-19 · checked 2026-09-06 · static check.

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - Applies cognitive-science creativity techniques — combinatorial creativity, analogical reasoning, and constraint manipulation — to generating research directions. `skill` · MIT · repo ★12358 · updated 2026-02-19 · checked 2026-09-06 · static check.

## Literature Review

*Finding, reading, and synthesising prior work, and keeping citations honest.*

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - Generates a BibTeX entry from a DOI, PMID, arXiv ID, or paper title by querying CrossRef, PubMed, arXiv, Semantic Scholar, and ChemRxiv. `skill` `net` · LGPL-3.0 · repo ★17 · updated 2026-02-15 · checked 2026-09-06 · static check.

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - Adds citations to manuscript text by searching only Nature Portfolio, AAAS Science, and Cell Press titles, filtered by date, and exports a single reference-manager file. `skill` · Apache-2.0 · repo ★39542 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - Structures a deep reading of one scientific paper into a fixed 16-section, evidence-grounded research card. `skill` · Apache-2.0 · repo ★39542 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [Nature Literature Pipeline](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-literature-pipeline) - Searches multiple literature sources, scores candidates across six dimensions, delivers digests, and archives results with deduplication. `skill` · MIT⚠(repo says Apache-2.0) · repo ★39542 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - Queries Google NotebookLM notebooks from Claude Code for citation-backed, source-grounded answers via browser automation. `skill` · MIT · repo ★7754 · updated 2025-11-21 · checked 2026-09-06 · static check.

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - Monitors arXiv, OpenReview, and conference feeds for papers overlapping with a given research idea, producing actionable relax/research/follow-up signals. `skill` · MIT · repo ★2200 · updated 2026-09-05 · checked 2026-09-06 · static check.

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - Searches and extracts metadata from CNKI, China's primary academic database, via Chrome DevTools browser automation. `suite` `external` `zh` · unverified · repo ★904 · updated 2026-02-28 · checked 2026-09-06 · static check.

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) - Reads and analyzes academic papers from PDF, arXiv, or Zotero, generating structured notes with figures, formulas, and concept links. `skill` · Apache-2.0 · repo ★1203 · updated 2026-07-10 · checked 2026-09-06 · static check.

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) - Automates a daily paper-recommendation pipeline — fetch, review, and note-taking — for keeping up with recent AI research. `skill` · Apache-2.0 · repo ★1203 · updated 2026-07-10 · checked 2026-09-06 · static check.

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) - Converts an academic paper into a detailed HTML article via a six-round workflow with code search, formula rendering, and diagrams. `skill` · unverified · repo ★1139 · updated 2026-05-21 · checked 2026-09-06 · static check.

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) - Generates formatted academic citations in GB/T 7714, IEEE, APA, MLA, Chicago, Harvard, and Vancouver styles by searching literature through the Qinyan Academic OpenAPI. `skill` `creds` `zh` · MIT · repo ★872 · updated 2026-03-13 · checked 2026-09-06 · static check.

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - Searches Google Scholar via browser automation, returning structured results with citation counts and full-text links. `suite` `external` · MIT · repo ★501 · updated 2026-03-04 · checked 2026-09-06 · static check.

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - Conducts patent prior-art searches, IP landscape mapping, and patentability assessment for technology research. `skill` · MIT · repo ★715 · updated 2026-06-22 · checked 2026-09-06 · static check.

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - Executes multi-step literature and technical research using the Google Gemini Deep Research Agent to produce a detailed cited report. `skill` `creds` · Apache-2.0 · repo ★417 · updated 2026-02-19 · checked 2026-09-06 · static check.

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - Parses academic PDFs into clean Markdown with table and formula extraction, using MinerU's free Agent API or token-based Standard API. `skill` `creds` · MIT · repo ★112 · updated 2026-06-02 · checked 2026-09-06 · static check.

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - Generates ranked paper candidates and related-work section summaries from a paper draft, using LLM-driven debate ranking over Semantic Scholar, arXiv, and OpenAlex with citation-graph expansion. `skill` `creds` `net` · Apache-2.0 · repo ★51 · updated 2026-05-07 · checked 2026-09-06 · static check.

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - Guides a systematic literature review through the full 27-item PRISMA 2020 checklist, producing a journal-format Word manuscript, an annotated PRISMA flow diagram, and APA 7th referencing, explicitly excluding meta-analysis and statistical pooling. `skill` `external` · unverified · repo ★93 · updated 2026-03-28 · checked 2026-09-06 · static check.

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - Searches bioRxiv preprint metadata and retrieves PDFs by keyword, author, date range, or subject category. `skill` · unverified · repo ★1058 · updated 2026-02-27 · checked 2026-09-06 · static check.

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - Builds a theory-developing literature review around a guiding question using a claim-source ledger and synthesis matrix, and blocks article-by-article summary and unsupported gap claims. `skill` · MIT · repo ★0 · updated 2026-08-09 · checked 2026-09-06 · audited.

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - Finds related work a draft may have missed by expanding outward through the citation graph and searching the draft's topic independently, grading each candidate by how much it threatens the novelty claim. `skill` `creds` · MIT · repo ★4 · updated 2026-09-05 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

## Study Design & Protocol

*Deciding what to measure and how, before any data is collected — protocols, ethics review, preregistration, sampling, instrument design.*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - Generates clinical trial protocols for medical devices or drugs through a waypoint-based workflow, with a research-only mode for surveying similar registered trials before drafting. `skill` `external` · unverified · repo ★408 · updated 2026-06-15 · checked 2026-09-06 · static check.

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - Drafts a structured preregistration document in OSF, AsPredicted, or AEA RCT Registry style, covering hypotheses, sampling plan, analysis plan, exclusions, and inference criteria, annotated with MUST/SHOULD/MAY clarity flags. `skill` · MIT · repo ★1564 · updated 2026-08-21 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - Computes statistical power, required sample size, and minimum detectable effect for two-arm RCTs with clustering, multi-arm designs, or simulation-based power for non-standard designs, producing a registry-ready power section. `skill` · MIT · repo ★1564 · updated 2026-08-23 · checked 2026-09-06 · static check.

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - Writes, revises, and evaluates IRB and ethics protocols for qualitative research, covering Common Rule exempt/expedited/full-board determination, protocol narrative, and data security planning. `skill` · unverified · repo ★24 · updated 2026-07-27 · checked 2026-09-06 · static check.

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - Designs qualitative data-collection instruments and protocols — interview guides, focus group guides, observation protocols, field note templates, and sampling strategies. `skill` · unverified · repo ★24 · updated 2026-07-27 · checked 2026-09-06 · static check.

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - Drafts and critiques survey question wording, response scales, and instrument flow against published social-science methodology to reduce measurement bias. `skill` · unverified · repo ★54 · updated 2026-09-05 · checked 2026-09-06 · static check.

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - Plans conjoint survey experiments, covering attribute architecture, randomization and orthogonality, power calculation, and AMCE/AMIE estimation. `skill` · unverified · repo ★54 · updated 2026-09-05 · checked 2026-09-06 · static check.

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - Reviews cohort logic, comparator choice, and validation strategy for medical studies to surface leakage and validity risks before analysis begins. `skill` · MIT · repo ★284 · updated 2026-07-25 · checked 2026-09-06 · static check.

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - Plans studies before data collection, covering randomization, blocking, factorial and crossover layouts, and cluster or adaptive designs. `skill` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - Checks whether a plan, experiment, dataset, or claim still aligns with the frozen research question and protocol, and refuses to silently rewrite the governing artifact when drift is found. `skill` · MIT · repo ★2 · updated 2026-08-12 · checked 2026-09-06 · audited.

## Method Formalization & Theory

*Turning an idea into a stated method: formalizing claims, checking derivations, and writing and verifying proofs.*

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - Drafts and completes rigorous mathematical proofs of theorems, lemmas, and propositions from a stated result and its assumptions. `skill` · MIT · repo ★15779 · updated 2026-07-13 · checked 2026-09-06 · static check.

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - Checks a paper's theorem proofs, algebraic derivations, and bounds step by step, reporting missing hypotheses and absent base cases, and flagging a step as unverified rather than refuted when the paper never states a symbol's domain. `skill` · MIT · repo ★4 · updated 2026-08-17 · checked 2026-09-06 · audited.

- [Formalize Problem](https://github.com/MerLeanProver/MerLean/tree/HEAD/.claude/skills/formalizeproblem) - Translates an informal mathematical problem into faithful, type-checking Lean 4 statements left at `sorry`, surfacing inequivalent readings and degenerate cases before any proof is attempted. `skill` · Apache-2.0 · repo ★8 · updated 2026-08-19 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - Re-derives a formula, estimator, identity, or bound at least twice independently, clusters the results by mathematical equivalence, and emits a verification matrix recording agreement and outliers. `skill` · unverified · repo ★16 · updated 2026-09-05 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

## Data & Annotation

*Sourcing, labelling, curating, and auditing the data a study runs on.*

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - Analyzes dataset bias, distribution, and fairness before model training. `skill` · MIT · repo ★385 · updated 2026-03-12 · checked 2026-09-06 · static check.

- [FiftyOne Dataset Curation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-curation) - Inspects CV dataset schema, quality, class distributions, and embeddings, then creates curated subsets and train/val/test splits using FiftyOne. `skill` · Apache-2.0 · repo ★39 · updated 2026-05-18 · checked 2026-09-06 · static check.

- [FiftyOne Dataset Import](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-import) - Imports and auto-detects dataset formats — images, video, point clouds, labels — into FiftyOne for CV research. `skill` `net` · Apache-2.0 · repo ★39 · updated 2026-05-18 · checked 2026-09-06 · static check.

- [FiftyOne Dataset Export](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-export) - Exports FiftyOne datasets to standard annotation formats — COCO, YOLO, VOC, CVAT, CSV — for downstream model training and sharing. `skill` `net` · Apache-2.0 · repo ★39 · updated 2026-05-14 · checked 2026-09-06 · static check.

- [Label Studio Setup](https://github.com/majiayu000/claude-skill-registry/tree/HEAD/skills/data/label-studio-setup) - Covers Label Studio installation, project setup, data import/export, labeling interface customization, quality control, and ML backend integration for image, text, audio, and video annotation. `skill` `creds` `external` · MIT · repo ★593 · updated 2026-04-20 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - Searches Hugging Face Hub, OpenML, GitHub, and paper cross-references for datasets matching a stated research task, returning a ranked and deduplicated list. `skill` · unverified · repo ★1058 · updated 2026-02-26 · checked 2026-09-06 · static check.

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - Quality-checks raster, vector, point, and remote-sensing datasets for CRS, datum, grid alignment, resolution, nodata, geometry validity, and spatial-join cardinality before analysis. `skill` · MIT · repo ★2 · updated 2026-08-12 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - Queries genomic and biomedical databases for gene records, sequences, alignments, AlphaFold structures, expression, and disease associations through one interface, pinning the tool version so a lookup can be repeated. `skill` · BSD-2-Clause⚠(repo says MIT) · repo ★43177 · updated 2026-09-02 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - Parses and sanitizes molecular structures, then computes descriptors, fingerprints, substructure matches, reactions, and 2D or 3D coordinates for cheminformatics work. `skill` · BSD-3-Clause⚠(repo says MIT) · repo ★43177 · updated 2026-09-02 · checked 2026-09-06 · audited.

## Model Training & Fine-Tuning

*Training and adapting models, from single-GPU fine-tuning to distributed runs.*

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - Trains and fine-tunes detection, classification, and SAM/SAM2 segmentation models on Hugging Face Jobs cloud GPUs. `skill` `creds` `net` · Apache-2.0 · repo ★11023 · updated 2026-03-23 · checked 2026-09-06 · static check.

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - Fine-tunes language and vision-language models via TRL or Unsloth on Hugging Face Jobs, covering SFT, DPO, GRPO, and reward modeling. `skill` `creds` `external` `net` · Apache-2.0 · repo ★11023 · updated 2026-07-06 · checked 2026-09-06 · static check.

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - Fine-tunes transformer language models via the TRL command-line interface, covering SFT, DPO, GRPO, KTO, RLOO, and reward modeling. `skill` `net` · Apache-2.0 · repo ★11023 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - Trains bi-encoder, cross-encoder, and SPLADE sparse embedding models with the sentence-transformers library. `skill` `creds` `net` · Apache-2.0 · repo ★11023 · updated 2026-08-18 · checked 2026-09-06 · static check.

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - Fine-tunes a Hugging Face model using the NVIDIA TAO Toolkit's optimized training and export path. `skill` `creds` `external` `net` · Apache-2.0 · repo ★3213 · updated 2026-09-01 · checked 2026-09-06 · static check.

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - Runs a pre-flight checklist for long-running ML training jobs to catch misconfigured configs, paths, and monitoring before launch. `skill` `creds` `external` · MIT · repo ★385 · updated 2026-04-30 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - Trains reinforcement learning agents with Stable Baselines3's production-ready PPO, SAC, DQN, TD3, DDPG, and A2C implementations on Gymnasium environments. `skill` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - Organizes PyTorch training code into LightningModules with configured Trainers for multi-GPU/TPU scaling, distributed training (DDP, FSDP, DeepSpeed), and logging integrations (W&B, TensorBoard, MLflow). `skill` · Apache-2.0⚠(repo says MIT) · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - Guides graph neural network development with PyTorch Geometric, covering node/link/graph classification, message-passing architectures (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, and neighbor sampling. `skill` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - Provides version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, training, evaluation, and checkpoint review. `skill` `creds` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · audited.

## Diagrams & Schematics

*Architecture, pipeline, and concept figures — the drawn illustrations in a paper, as opposed to charts plotted from data.*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - Enforces a standalone-TikZ-to-PDF pipeline for academic paper figures, forbidding inline TikZ in paper source and requiring every figure to compile and be visually verified before insertion. `skill` · MIT · repo ★292 · updated 2026-03-19 · checked 2026-09-06 · static check.

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - Guides creation of graphical abstracts, schematic diagrams, workflow visualizations, and architecture diagrams, covering both programmatic and design-tool approaches. `skill` · MIT · repo ★288 · updated 2026-03-15 · checked 2026-09-06 · static check.

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - Reconstructs reference images of diagrams, figures, or architecture visuals into editable Draw.io files, prioritizing visual fidelity to the source over pure editability. `skill` · unverified · repo ★6608 · updated 2026-07-16 · checked 2026-09-06 · static check.

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - Generates and syntax-verifies Mermaid diagrams — flowcharts, sequence diagrams, class diagrams, ER diagrams, Gantt charts, and 18 other types — from a natural-language description. `skill` `external` · MIT · repo ★15778 · updated 2026-07-13 · checked 2026-09-06 · static check.

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - Generates .drawio XML diagrams and exports to PNG/SVG/PDF/JPG via the native draw.io desktop CLI, covering flowcharts, architecture diagrams, ER/UML diagrams, network topology, and ML/DL model figures (Transformer, CNN, LSTM). `skill` · MIT · repo ★9074 · updated 2026-09-03 · checked 2026-09-06 · static check.

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - Classifies a paper's research type and mechanism to select an appropriate diagram structure — pipeline, architecture, comparison matrix, ablation matrix, or taxonomy tree — rather than mechanically applying one fixed template. `skill` · MIT · repo ★206 · updated 2026-06-15 · checked 2026-09-06 · static check.

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - Finds, edits, and verifies TikZ figures from a library of copyable icons and editable templates for neural network architectures, encoder-decoder diagrams, training pipelines, and system block diagrams. `skill` · unverified · repo ★246 · updated 2026-07-04 · checked 2026-09-06 · static check.

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - Generates publication-quality academic diagrams and pipeline figures from a paper's methodology text and figure caption, orchestrating a multi-agent pipeline (Retriever, Planner, Stylist, Visualizer, Critic) targeting venues like NeurIPS, ICML, and ACL. `skill` `creds` · MIT-0⚠(repo says Apache-2.0) · repo ★7041 · updated 2026-06-22 · checked 2026-09-06 · static check.

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - Creates publication-quality scientific diagrams using an AI image model with smart iterative refinement, re-generating only when a separate quality-review pass scores below threshold, specialized in neural network architectures, system diagrams, flowcharts, and biological pathways. `skill` `creds` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - Plans biomedical mechanism figures, pathway maps, and graphical abstracts mechanism-first, then builds image-model prompts targeting vector or 300-600 DPI print output. `skill` · unverified · repo ★21 · updated 2026-05-06 · checked 2026-09-06 · audited.

## Experiment Management & Reproducibility

*Running experiments, tracking what happened, and making the result reproducible by someone else.*

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - Verifies a LibreYOLO training run's config, dataset, and metrics against project conventions before a checkpoint is trusted. `skill` `creds` · unverified · repo ★634 · updated 2026-08-08 · checked 2026-09-06 · static check.

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - Turns an arXiv paper into a citation-anchored Python implementation, tagging each module to the paper section it implements and flagging rather than guessing at ambiguities. `skill` · MIT · repo ★1518 · updated 2026-04-03 · checked 2026-09-06 · static check.

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - Surveys papers in a research direction to extract the benchmarks, datasets, metrics, and evaluation protocols in common use, or extracts them from a single given paper. `skill` · MIT · repo ★37 · updated 2026-04-24 · checked 2026-09-06 · static check.

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) - Standardizes lab experiment logging from photos, voice, or text into YAML-frontmattered Markdown written to a plain local folder, with optional Obsidian vault and Feishu integrations. `skill` · MIT⚠(repo says Apache-2.0) · repo ★39542 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - Designs an evidence package for a CCF-venue paper, covering datasets, baselines, metrics, and ablations. `skill` · MIT · repo ★2200 · updated 2026-09-05 · checked 2026-09-06 · static check.

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - Scans AI coding-agent cache directories and extracts numeric experiment results into a structured format. `skill` · unverified · repo ★650 · updated 2026-04-17 · checked 2026-09-06 · static check.

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - Diagnoses a failing ML experiment with a five-step evidence-before-action protocol covering process state, GPU, disk, logs, and checkpoints. `skill` · MIT · repo ★385 · updated 2026-04-30 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - Enforces same-epoch alignment when comparing ML training runs and separates proxy metrics from downstream targets. `skill` `creds` · MIT · repo ★385 · updated 2026-04-30 · checked 2026-09-06 · static check.

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - Walks through seven stages from an arXiv URL to a measurable replication run, handling missing code, hyperparameters, and private datasets via public-substitute strategies. `skill` · MIT · repo ★385 · updated 2026-04-30 · checked 2026-09-06 · static check.

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - Prepares research code for public release alongside a paper submission, covering repository cleanup, dependency auditing, and a reproducibility checklist. `skill` · MIT · repo ★385 · updated 2026-03-12 · checked 2026-09-06 · audited.

- [Nature Paper Skills: Results Analysis](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/research/results-analysis) - Runs a systematic pipeline for analyzing ML experimental results, running statistical tests, and generating paper-ready figures and text. `skill` · MIT · repo ★483 · updated 2026-04-29 · checked 2026-09-06 · static check.

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) - Summarizes ML experiment logs into structured Chinese output with evidence/speculation separated and a weekly-update abstract. `skill` `zh` · MIT · repo ★347 · updated 2026-04-05 · checked 2026-09-06 · static check.

- [FiftyOne Model Evaluation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-model-evaluation) - Evaluates CV model predictions against ground truth using standard protocols like COCO and Open Images. `skill` · Apache-2.0 · repo ★39 · updated 2026-05-14 · checked 2026-09-06 · static check.

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - Assembles a submission-ready replication package to the AEA Data and Code Availability Standard, including a replication README, dataset manifest, computational-requirements capture, a table/figure-to-script map, and a confidential-data deposit plan. `skill` · MIT · repo ★1564 · updated 2026-08-21 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - Governs finite-element and CAE analysis claims across Ansys, Abaqus, Nastran, OpenFOAM, and COMSOL, enforcing idealization review, mesh-independence via GCI, verification and validation, and human sign-off gates. `skill` · Apache-2.0 · repo ★4 · updated 2026-06-29 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - Scaffolds an R or bioinformatics analysis project on a read/write/checkpoints layout that keeps immutable inputs, tracked code, and untracked outputs separate. `skill` · unverified · repo ★8 · updated 2026-09-02 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - Covers the methodology of multi-job experiment campaigns on Slurm clusters — walltime sizing, job and array shaping, submission order, and diagnosing runs that produced nothing or silently used the wrong configuration. `skill` `external` · MIT · repo ★4 · updated 2026-08-12 · checked 2026-09-06 · audited. ⓘ hands-on audit: unverifiable.

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - Audits an ML pipeline for train-test contamination, temporal and spatial leakage, target and proxy leakage, preprocessing leakage, and evaluation contamination, classifying each finding by severity. `skill` · MIT · repo ★2 · updated 2026-08-12 · checked 2026-09-06 · audited.

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - Takes bulk RNA-seq reads through quality control, trimming, alignment, and quantification to a gene-level count matrix, gating on experimental design and strandedness before differential expression. `skill` · MIT · repo ★43177 · updated 2026-09-02 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - Resolves canonical CMSO and ASMO ontology terms for computational materials data, checking class hierarchies and property domain and range before a relationship is asserted. `skill` · Apache-2.0 · repo ★66 · updated 2026-06-25 · checked 2026-09-06 · audited.

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - Packages research code and data for artifact-evaluation submission — README and appendix, anonymization for double-blind review, ACM badge taxonomy, and archival-DOI guidance for Zenodo or Software Heritage — checked against live venue rules. `skill` · Apache-2.0 · repo ★41 · updated 2026-06-21 · checked 2026-09-06 · audited.

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - Audits whether metrics produced by an author's own local code still match the tables and claims reported in their paper, within stated tolerances, and reports mismatches separately from reproduction failures. `skill` · Apache-2.0 · repo ★41 · updated 2026-06-21 · checked 2026-09-06 · audited.

## Statistical Analysis

*Choosing and running the analysis: regression, causal inference, survey weighting, meta-analysis, Bayesian modelling.*

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - Detects statistical errors and methodological fallacies in empirical research content, with structured severity levels. `skill` · MIT · repo ★47 · updated 2026-05-15 · checked 2026-09-06 · static check.

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - Analyzes complex survey data in R with the survey package, covering design objects, weighted means and totals, survey-weighted regression, domain estimation, and replicate weights (BRR, jackknife, bootstrap). `skill` · LGPL-3.0 · repo ★235 · updated 2026-07-15 · checked 2026-09-06 · static check.

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - Estimates high-dimensional fixed-effects models in R with multi-way fixed effects, IV estimation, TWFE and Sun-Abraham difference-in-differences, and clustered or heteroskedasticity-robust standard errors. `skill` · LGPL-3.0 · repo ★235 · updated 2026-08-03 · checked 2026-09-06 · static check.

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - Maps Stata commands (reghdfe, xtreg, ivregress, margins, esttab, svy:) to their R equivalents for researchers moving an analysis between the two ecosystems. `skill` · LGPL-3.0 · repo ★235 · updated 2026-07-24 · checked 2026-09-06 · static check.

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - Analyzes experiment result files, runs significance tests and model comparisons, and drafts a Results section with accompanying figures. `skill` · unverified · repo ★1058 · updated 2026-02-26 · checked 2026-09-06 · static check.

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - Runs the meta-analysis pipeline from PROSPERO protocol registration and risk-of-bias assessment through statistical synthesis and PRISMA-compliant reporting. `skill` · MIT · repo ★284 · updated 2026-08-19 · checked 2026-09-06 · static check.

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - Generates reproducible Python or R code for diagnostic accuracy, agreement, survival, propensity-score, and survey-weighted analyses, with a protected-health-information check before reading any data file. `skill` `creds` · MIT · repo ★284 · updated 2026-09-06 · checked 2026-09-06 · static check.

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - Selects statistical tests, checks their assumptions, computes effect sizes, and reports results in APA format across t-tests, ANOVA, regression, and Bayesian alternatives. `skill` · MIT · repo ★43176 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - Builds, fits, and validates Bayesian hierarchical models with PyMC, covering MCMC sampling, variational inference, and posterior predictive checks. `skill` · Apache-2.0⚠(repo says MIT) · repo ★43176 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - Analyzes complex-sample survey data in Python with strata, PSU, and weight handling, variance estimation, and survey-weighted GLM for datasets such as NHANES, CPS, and DHS. `skill` · LGPL-3.0 · repo ★235 · updated 2026-07-15 · checked 2026-09-06 · static check.

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) - Runs a network meta-analysis from PICO to manuscript skeleton — search execution, dual-model screening, extraction, risk-of-bias, frequentist and Bayesian synthesis in R, GRADE rating, and PRISMA-NMA reporting — with five mandatory human decision gates and an audit log. `skill` `creds` `external` `zh` · MIT · repo ★3 · updated 2026-08-06 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - Selects and stress-tests a causal identification strategy for empirical economics, covering staggered difference-in-differences, weak-IV-robust instrumental variables, regression discontinuity, synthetic control, and shift-share designs. `skill` `external` · MIT · repo ★48 · updated 2026-07-08 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

## Qualitative & Mixed Methods

*Interviews, fieldwork, and coded text — thematic analysis, grounded theory, ethnography, intercoder reliability.*

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - Conducts thematic analysis of interviews, focus groups, or open-ended responses following Braun and Clarke's six-phase framework, covering the four upfront analytic decisions and a 15-point quality checklist. `skill` `external` · MIT · repo ★15 · updated 2026-05-11 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - Codes qualitative data and builds codebooks with deductive, inductive, and hybrid coding, code frequencies, co-occurrence analysis, and intercoder reliability. `skill` · unverified · repo ★24 · updated 2026-08-28 · checked 2026-09-06 · static check.

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - Runs grounded theory, reflexive thematic analysis, and content analysis with codebook development and inter-coder reliability checks, exporting to NVivo, ATLAS.ti, Dedoose, and MAXQDA formats. `skill` `creds` `hooks` · unverified · repo ★140 · updated 2026-08-25 · checked 2026-09-06 · static check.

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - Covers qualitative design and analysis across five traditions — thematic analysis, grounded theory, interpretative phenomenological analysis, ethnography, and case study — with trustworthiness criteria. `skill` · MIT · repo ★64 · updated 2026-07-02 · checked 2026-09-06 · static check.

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - Scaffolds and indexes reflexive, comparative, integrative, and decision memos grounded in coded units, keeping the researcher's interpretation separate from the machine audit log. `skill` · MIT · repo ★1 · updated 2026-07-31 · checked 2026-09-06 · audited.

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - Tracks multi-dimensional theoretical saturation, generates phase-sensitive methodological isolation rules, and logs rule changes and overrides to a reflexivity journal. `skill` · unverified · repo ★17 · updated 2026-02-01 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

## Interpretability

*Opening up a trained model to see what it computes, and explaining individual predictions.*

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - Trains and analyzes sparse autoencoders to decompose polysemantic model activations into interpretable features, wrapping the SAELens and TransformerLens libraries. `skill` · MIT · repo ★242281 · updated 2026-08-08 · checked 2026-09-06 · static check.

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - Explains and audits machine-learning predictions with SHAP, covering explainer/masker selection, feature-attribution computation and validation, multi-output explanations, and local/global visualizations. `skill` · MIT · repo ★43175 · updated 2026-09-02 · checked 2026-09-06 · static check.

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - Inspects and manipulates the internals of any PyTorch model with nnsight, including remote execution against models too large for local GPUs via NDIF. `skill` `creds` · MIT · repo ★12358 · updated 2025-12-17 · checked 2026-09-06 · static check.

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - Performs causal tracing, activation patching, and interchange intervention training on PyTorch models through pyvene's declarative, dict-based intervention framework. `skill` · MIT · repo ★12358 · updated 2025-12-17 · checked 2026-09-06 · static check.

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - Reverse-engineers transformer algorithms by inspecting attention patterns and running activation-patching experiments through TransformerLens HookPoints. `skill` `creds` · MIT · repo ★12358 · updated 2025-12-17 · checked 2026-09-06 · static check.

## Paper-Grade Plotting & Visualization

*Charts plotted from results, to the standard a journal or conference expects.*

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - Produces publication-ready matplotlib figures — bar, trend, scatter, heatmap, and multi-panel layouts — in a fixed house style with print/vector export conventions for AI conference and journal submissions. `skill` · unverified · repo ★4724 · updated 2026-06-24 · checked 2026-09-06 · static check.

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - Creates, revises, and audits submission-grade scientific figures for high-impact venues in Python or R, with multi-panel support and journal-ready export. `skill` · Apache-2.0 · repo ★39542 · updated 2026-09-06 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - Generates publication-quality figures and conceptual diagrams for academic papers from experimental data and an outline, with optional VLM-based critique refinement. `skill` · unverified · repo ★650 · updated 2026-04-10 · checked 2026-09-06 · static check.

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - Plans and audits manuscript figure organization, enforcing one claim per figure, assigning panel roles, and deciding main-versus-supplement placement before legends or results text are written. `skill` · MIT · repo ★483 · updated 2026-09-04 · checked 2026-09-06 · static check.

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - Generates runnable matplotlib/seaborn/mermaid code for research figures with a decision guide between quantitative and conceptual diagrams. `skill` · MIT · repo ★47 · updated 2026-05-15 · checked 2026-09-06 · static check.

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - Enforces Edward Tufte's data-visualization principles — data-ink ratio, direct labeling, range-frame axes — across multiple charting libraries for academic plotting. `skill` · MIT · repo ★212 · updated 2026-02-19 · checked 2026-09-06 · static check.

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - Validates tabular longitude and latitude data and renders reproducible SVG site maps, applying a per-row public, generalized, or restricted visibility policy with coordinate rounding. `skill` · MIT · repo ★0 · updated 2026-08-12 · checked 2026-09-06 · audited.

## Writing & Submission

*Drafting the manuscript and getting it submission-ready — structure, formatting, venue adaptation, self-checks before it goes out.*

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - Guides revision of ML/CV/NLP papers with paragraph-level clarity checks, reverse outlining, topic-sentence mapping, and claim-evidence alignment audits. `skill` · MIT · repo ★6583 · updated 2026-06-20 · checked 2026-09-06 · static check.

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - Plans, drafts, revises, and venue-adapts research paper text for CCF-ranked venues while preserving the user's own idea scope and evidence. `skill` · MIT · repo ★2200 · updated 2026-09-06 · checked 2026-09-06 · static check.

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - Converts raw research materials into a structured outline with a plotting plan, literature-search plan, and section plan for academic paper writing. `skill` · unverified · repo ★650 · updated 2026-06-02 · checked 2026-09-06 · static check.

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - Handles LaTeX document creation, compilation, format conversion, and document analysis for academic writing. `skill` · unverified · repo ★741 · updated 2026-09-06 · checked 2026-09-06 · static check.

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - Adapts an academic manuscript to a target journal's writing conventions by analyzing a reference corpus and revising the manuscript section by section. `skill` · MIT · repo ★770 · updated 2026-05-15 · checked 2026-09-06 · static check.

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - Verifies paper claims against code and data through numerical-accuracy, terminology-consistency, and formula-code alignment checks. `skill` · MIT · repo ★385 · updated 2026-03-12 · checked 2026-09-06 · static check.

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - Runs a late-stage manuscript preflight audit that cross-checks claims, figures, legends, methods, and supplement against venue expectations before submission or resubmission. `skill` · MIT · repo ★483 · updated 2026-05-08 · checked 2026-09-06 · static check.

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) - Writes a survey draft around a research topic by organizing multiple papers into problem-driven, method-evolution narratives rather than paper-by-paper summaries. `skill` · MIT · repo ★347 · updated 2026-04-05 · checked 2026-09-06 · static check.

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - Assists with existing Typst manuscripts covering compilation, venue formatting, grammar, bibliography, and submission readiness. `skill` · unverified · repo ★444 · updated 2026-08-29 · checked 2026-09-06 · static check.

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) - Assists graduate students with Chinese LaTeX thesis projects, covering compilation diagnosis, GB/T 7714 bibliography formatting, structure review, and blind-review anonymization. `skill` `zh` · unverified · repo ★444 · updated 2026-09-05 · checked 2026-09-06 · static check.

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - Guides grant proposal architecture, funder fit evaluation, and budget design for academic research funding. `skill` · MIT · repo ★715 · updated 2026-06-22 · checked 2026-09-06 · static check.

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - Synthesizes economics-writing guidance from 50+ style guides into executable rules for drafting and revising economics papers. `skill` · MIT · repo ★585 · updated 2026-07-15 · checked 2026-09-06 · static check.

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - Creates and edits .docx files with Chinese academic formatting conventions such as three-line tables and block formulas. `skill` `zh` · MIT · repo ★401 · updated 2026-06-30 · checked 2026-09-06 · static check.

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - Removes common AI-writing patterns from academic and research prose to restore a more natural voice. `skill` · MIT · repo ★381 · updated 2026-03-18 · checked 2026-09-06 · static check.

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) - Fixes LaTeX overflow defects — overfull boxes, long formulas, and URL overflows — starting from layout-only edits and escalating to delegated rewording when layout alone cannot fit it. `skill` · MIT · repo ★333 · updated 2026-05-08 · checked 2026-09-06 · audited.

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) - Fixes LaTeX float placement defects — distance from first reference, width mismatch, clustering, page orphaning — in academic paper source code. `skill` · MIT · repo ★333 · updated 2026-05-08 · checked 2026-09-06 · static check.

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - Turns a paper into a slide deck and optionally a narrated demo video, covering script drafting, slide generation, text-to-speech narration, and video assembly. `skill` `creds` · unverified · repo ★1058 · updated 2026-03-04 · checked 2026-09-06 · static check.

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - Builds an editable conference poster from author-approved local content, checking physical dimensions, printer constraints, accessibility, asset provenance, and export readiness. `skill` · MIT · repo ★43177 · updated 2026-09-02 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - Converts a published paper into a plain-language summary, graphical-abstract concept, and platform-tailored social copy, holding every version to what the paper's findings actually support. `skill` · Apache-2.0 · repo ★1 · updated 2026-07-16 · checked 2026-09-06 · audited.

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - Classifies a confirmed error in an already-published paper as a corrigendum, erratum, expression of concern, or retraction, then drafts the co-author notification, editor request, and public notice. `skill` · Apache-2.0 · repo ★1 · updated 2026-07-16 · checked 2026-09-06 · audited.

## Peer Review & Rebuttal

*The other side of submission: refereeing someone else's manuscript, and answering the reviews of your own.*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - Simulates a five-person international journal peer-review panel with field-specific reviewer personas, producing structured editorial decisions and revision roadmaps. `skill` `hooks` · unverified · repo ★46506 · updated 2026-08-20 · checked 2026-09-06 · static check.

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - Reviews a manuscript against CCF/target-venue criteria across novelty, soundness, evidence, writing quality, and format compliance, simulating a reviewer/AC panel. `skill` · MIT · repo ★2200 · updated 2026-09-06 · checked 2026-09-06 · static check.

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - Structured review and revision workflow for academic manuscripts with six operating modes scaled to effort level. `skill` · unverified · repo ★666 · updated 2026-06-16 · checked 2026-09-06 · static check.

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - Converts peer reviews into evidence-based rebuttal packages through triage, strategy, drafting, and tone-repair modes. `skill` · unverified · repo ★666 · updated 2026-06-16 · checked 2026-09-06 · static check.

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - Orchestrates a reviewer-side integrity forensics sweep of a research paper — building a span-anchored evidence ledger, fanning out cross-model auditors for citation, experiment, consistency, and baseline-comparison fabrication, then computing a deterministic verdict for a human reviewer. `suite` `external` `net` · MIT · repo ★149 · updated 2026-08-10 · checked 2026-09-06 · static check.

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - Produces a referee-grade report on an economics paper, checking identification strategy, inference, tables, equations, and references, and outputs a findings ledger with a prioritized revision plan. `skill` · unverified · repo ★19 · updated 2026-07-15 · checked 2026-09-06 · audited. ⓘ hands-on audit: works with caveats.

## How these entries are checked

This is a curated list, not a certification. Each entry is chosen by a person reading its `SKILL.md`, and the metadata beside it is refreshed by script against GitHub. That script and its source file are not published, so what you see can be spot-checked entry by entry — every row links to the directory it describes — but not re-run wholesale. Treat it as a maintained record, not as an independently reproducible audit. Batches are also audited hands-on — walking a skill's own instructions against the files it ships — which has removed entries that read well but could not work for anyone but their author. A description states what the skill does; it is not a report of it having been run end to end on your problem.

**Badge legend.** `skill`/`suite`/`plugin` is what the entry is. A language tag marks a non-English `SKILL.md`. `updated` is the last commit **to that subdirectory**, not to its repo, and `checked` is when this list last verified the entry against GitHub.

**Capability flags.** `net`, `creds`, `hooks`, `external`, `bypass` mean the skill talks to the network, needs a key or account, installs agent hooks, shells out to another tool, or asks for permission checks to be skipped. They are found by matching the shipped files and then reading the line that matched, so only capabilities the file presents as *required* appear here; optional, merely mentioned, and explicitly discouraged matches are kept in the machine-readable index with the rule, file, and line behind each one.

**Licenses are resolved for the skill, not the repo.** A `license:` in the skill's own frontmatter wins over the repo LICENSE; where the two disagree the entry shows ⚠ and the repo's answer beside it.

**About `repo ★N`.** GitHub has no per-directory star metric, and 94% of these skills live inside someone's larger repo. The number is that repo's stars — an adoption signal for the project it lives in, and never a rating of the skill itself. A skill in a 20,000-star monorepo may have been committed once and never used.

**Two levels of checking.** *static check* means the path, license, commit date, and capability flags were verified against the live repo and the `SKILL.md` was read. *audited* means someone additionally walked the skill's own instructions against the files it ships, against a written audit spec; where that audit found a condition worth knowing, it is stated inline on the entry. No entry claims an executable end-to-end test, because none has been run.

The structural checks behind every entry — is it substantive, is it template-farmed, does the repo verify — are discipline-independent, and they are what this list guarantees. Whether a clinical-trial, qualitative-coding, or econometrics skill is *methodologically correct for your field* is a judgment its curator cannot make across every discipline represented here. Treat domain entries as leads to evaluate, not as vetted by a subject expert.

Entries not in English carry a language tag. The same data is published as [`index.json`](index.json) and [`index.csv`](index.csv), generated from the same source as this page.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — this list is data-driven, don't edit README.md by hand.
