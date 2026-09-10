# Awesome Research Skills [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) [![Skills](https://img.shields.io/badge/skills-146-blue?style=flat-square)](index.json) [![Last Commit](https://img.shields.io/github/last-commit/neverbiasu/awesome-research-skills?style=flat-square)](https://github.com/neverbiasu/awesome-research-skills/commits/main)

> 146 Agent Skills for researchers, read and chosen one at a time — every entry is one exact `SKILL.md` directory, not a repo that might contain something useful.

`146 skills` · `individually curated` · `37 hands-on audited` · `one exact SKILL.md path per entry`

For the steps you do yourself: finding prior work, designing the study, formalizing the method, curating data, running and auditing experiments, statistics, qualitative analysis, figures, writing, and peer review. Skills that automate the whole research loop are out of scope, as are MLOps and deployment tooling.

Entries are curated by reading the skill and checking it against its repository, not template-farmed or abandoned or moved elsewhere. Each one carries its own license, its subdirectory's last commit, and flags for what it needs to run — network, credentials, hooks. 37 have also been walked through by hand against the files they ship; what that does and does not guarantee is set out at the end of this page.

All entries checked against GitHub as of 2026-09-06. Each entry below is marked either `static check` (path, license, commit date, and capability flags verified) or `audited: <verdict>` (additionally walked through by hand against a written spec) — full definitions in [How these entries are checked](#how-these-entries-are-checked).

## Contents

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

## Direction Scanning & Ideation

*Turning a vague interest into a formulated, testable research question.*

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - Guides generation of falsifiable, structured research hypotheses from user-provided notes and content.

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - Applies structured ideation frameworks to surface research directions when entering a new problem space or reconsidering a project's direction.

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - Structures research project initiation through 5W1H brainstorming, systematic literature review, multi-dimensional gap analysis, and SMART research-question formulation.

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - Applies cognitive-science creativity techniques — combinatorial creativity, analogical reasoning, and constraint manipulation — to generating research directions.

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) - Analyzes literature and early ideas to identify grounded research gaps and testable entry points without forcing novelty claims.

## Literature Review

*Finding, reading, and synthesising prior work, and keeping citations honest.*

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - Searches bioRxiv preprint metadata and retrieves PDFs by keyword, author, date range, or subject category.

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - Monitors arXiv, OpenReview, and conference feeds for papers overlapping with a given research idea, producing actionable relax/research/follow-up signals.

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - Searches and extracts metadata from CNKI, China's primary academic database, via Chrome DevTools browser automation. `zh`

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - Builds a theory-developing literature review around a guiding question using a claim-source ledger and synthesis matrix, and blocks article-by-article summary and unsupported gap claims.

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) - Reads and analyzes academic papers from PDF, arXiv, or Zotero, generating structured notes with figures, formulas, and concept links.

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) - Automates a daily paper-recommendation pipeline — fetch, review, and note-taking — for keeping up with recent AI research.

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - Executes multi-step literature and technical research using the Google Gemini Deep Research Agent to produce a detailed cited report.

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - Searches Google Scholar via browser automation, returning structured results with citation counts and full-text links.

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - Generates ranked paper candidates and related-work section summaries from a paper draft, using LLM-driven debate ranking over Semantic Scholar, arXiv, and OpenAlex with citation-graph expansion.

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - Parses academic PDFs into clean Markdown with table and formula extraction, using MinerU's free Agent API or token-based Standard API.

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - Adds citations to manuscript text by searching only Nature Portfolio, AAAS Science, and Cell Press titles, filtered by date, and exports a single reference-manager file.

- [Nature Literature Pipeline](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-literature-pipeline) - Searches multiple literature sources, scores candidates across six dimensions, delivers digests, and archives results with deduplication.

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - Structures a deep reading of one scientific paper into a fixed 16-section, evidence-grounded research card.

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - Queries Google NotebookLM notebooks from Claude Code for citation-backed, source-grounded answers via browser automation.

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) - Converts an academic paper into a detailed HTML article via a six-round workflow with code search, formula rendering, and diagrams.

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - Conducts patent prior-art searches, IP landscape mapping, and patentability assessment for technology research.

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) - Generates formatted academic citations in GB/T 7714, IEEE, APA, MLA, Chicago, Harvard, and Vancouver styles by searching literature through the Qinyan Academic OpenAPI. `zh`

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - Guides a systematic literature review through the full 27-item PRISMA 2020 checklist, producing a journal-format Word manuscript, an annotated PRISMA flow diagram, and APA 7th referencing, explicitly excluding meta-analysis and statistical pooling.

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - Finds related work a draft may have missed by expanding outward through the citation graph and searching the draft's topic independently, grading each candidate by how much it threatens the novelty claim.

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - Generates a BibTeX entry from a DOI, PMID, arXiv ID, or paper title by querying CrossRef, PubMed, arXiv, Semantic Scholar, and ChemRxiv.

## Study Design & Protocol

*Deciding what to measure and how, before any data is collected — protocols, ethics review, preregistration, sampling, instrument design.*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - Generates clinical trial protocols for medical devices or drugs through a waypoint-based workflow, with a research-only mode for surveying similar registered trials before drafting.

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - Plans conjoint survey experiments, covering attribute architecture, randomization and orthogonality, power calculation, and AMCE/AMIE estimation.

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - Plans studies before data collection, covering randomization, blocking, factorial and crossover layouts, and cluster or adaptive designs.

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - Designs qualitative data-collection instruments and protocols — interview guides, focus group guides, observation protocols, field note templates, and sampling strategies.

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - Writes, revises, and evaluates IRB and ethics protocols for qualitative research, covering Common Rule exempt/expedited/full-board determination, protocol narrative, and data security planning.

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - Reviews cohort logic, comparator choice, and validation strategy for medical studies to surface leakage and validity risks before analysis begins.

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - Computes statistical power, required sample size, and minimum detectable effect for two-arm RCTs with clustering, multi-arm designs, or simulation-based power for non-standard designs, producing a registry-ready power section.

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - Drafts a structured preregistration document in OSF, AsPredicted, or AEA RCT Registry style, covering hypotheses, sampling plan, analysis plan, exclusions, and inference criteria, annotated with MUST/SHOULD/MAY clarity flags.

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - Checks whether a plan, experiment, dataset, or claim still aligns with the frozen research question and protocol, and refuses to silently rewrite the governing artifact when drift is found.

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - Drafts and critiques survey question wording, response scales, and instrument flow against published social-science methodology to reduce measurement bias.

## Method Formalization & Theory

*Turning an idea into a stated method: formalizing claims, checking derivations, and writing and verifying proofs.*

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - Re-derives a formula, estimator, identity, or bound at least twice independently, clusters the results by mathematical equivalence, and emits a verification matrix recording agreement and outliers.

- [Formalize Problem](https://github.com/MerLeanProver/MerLean/tree/HEAD/.claude/skills/formalizeproblem) - Translates an informal mathematical problem into faithful, type-checking Lean 4 statements left at `sorry`, surfacing inequivalent readings and degenerate cases before any proof is attempted.

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - Drafts and completes rigorous mathematical proofs of theorems, lemmas, and propositions from a stated result and its assumptions.

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - Checks a paper's theorem proofs, algebraic derivations, and bounds step by step, reporting missing hypotheses and absent base cases, and flagging a step as unverified rather than refuted when the paper never states a symbol's domain.

## Data & Annotation

*Sourcing, labelling, curating, and auditing the data a study runs on.*

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - Searches Hugging Face Hub, OpenML, GitHub, and paper cross-references for datasets matching a stated research task, returning a ranked and deduplicated list.

- [FiftyOne Dataset Curation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-curation) - Inspects CV dataset schema, quality, class distributions, and embeddings, then creates curated subsets and train/val/test splits using FiftyOne.

- [FiftyOne Dataset Export](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-export) - Exports FiftyOne datasets to standard annotation formats — COCO, YOLO, VOC, CVAT, CSV — for downstream model training and sharing.

- [FiftyOne Dataset Import](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-import) - Imports and auto-detects dataset formats — images, video, point clouds, labels — into FiftyOne for CV research.

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - Quality-checks raster, vector, point, and remote-sensing datasets for CRS, datum, grid alignment, resolution, nodata, geometry validity, and spatial-join cardinality before analysis.

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - Queries genomic and biomedical databases for gene records, sequences, alignments, AlphaFold structures, expression, and disease associations through one interface, pinning the tool version so a lookup can be repeated.

- [Label Studio Setup](https://github.com/majiayu000/claude-skill-registry/tree/HEAD/skills/data/label-studio-setup) - Covers Label Studio installation, project setup, data import/export, labeling interface customization, quality control, and ML backend integration for image, text, audio, and video annotation.

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - Analyzes dataset bias, distribution, and fairness before model training.

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - Parses and sanitizes molecular structures, then computes descriptors, fingerprints, substructure matches, reactions, and 2D or 3D coordinates for cheminformatics work.

## Model Training & Fine-Tuning

*Training and adapting models, from single-GPU fine-tuning to distributed runs.*

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - Fine-tunes language and vision-language models via TRL or Unsloth on Hugging Face Jobs, covering SFT, DPO, GRPO, and reward modeling.

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - Trains and fine-tunes detection, classification, and SAM/SAM2 segmentation models on Hugging Face Jobs cloud GPUs.

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - Organizes PyTorch training code into LightningModules with configured Trainers for multi-GPU/TPU scaling, distributed training (DDP, FSDP, DeepSpeed), and logging integrations (W&B, TensorBoard, MLflow).

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - Trains reinforcement learning agents with Stable Baselines3's production-ready PPO, SAC, DQN, TD3, DDPG, and A2C implementations on Gymnasium environments.

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - Fine-tunes a Hugging Face model using the NVIDIA TAO Toolkit's optimized training and export path.

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - Runs a pre-flight checklist for long-running ML training jobs to catch misconfigured configs, paths, and monitoring before launch.

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - Provides version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, training, evaluation, and checkpoint review.

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - Guides graph neural network development with PyTorch Geometric, covering node/link/graph classification, message-passing architectures (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, and neighbor sampling.

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - Trains bi-encoder, cross-encoder, and SPLADE sparse embedding models with the sentence-transformers library.

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - Fine-tunes transformer language models via the TRL command-line interface, covering SFT, DPO, GRPO, KTO, RLOO, and reward modeling.

## Diagrams & Schematics

*Architecture, pipeline, and concept figures — the drawn illustrations in a paper, as opposed to charts plotted from data.*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - Enforces a standalone-TikZ-to-PDF pipeline for academic paper figures, forbidding inline TikZ in paper source and requiring every figure to compile and be visually verified before insertion.

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - Plans biomedical mechanism figures, pathway maps, and graphical abstracts mechanism-first, then builds image-model prompts targeting vector or 300-600 DPI print output.

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - Classifies a paper's research type and mechanism to select an appropriate diagram structure — pipeline, architecture, comparison matrix, ablation matrix, or taxonomy tree — rather than mechanically applying one fixed template.

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - Generates .drawio XML diagrams and exports to PNG/SVG/PDF/JPG via the native draw.io desktop CLI, covering flowcharts, architecture diagrams, ER/UML diagrams, network topology, and ML/DL model figures (Transformer, CNN, LSTM).

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - Reconstructs reference images of diagrams, figures, or architecture visuals into editable Draw.io files, prioritizing visual fidelity to the source over pure editability.

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - Generates and syntax-verifies Mermaid diagrams — flowcharts, sequence diagrams, class diagrams, ER diagrams, Gantt charts, and 18 other types — from a natural-language description.

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - Finds, edits, and verifies TikZ figures from a library of copyable icons and editable templates for neural network architectures, encoder-decoder diagrams, training pipelines, and system block diagrams.

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - Generates publication-quality academic diagrams and pipeline figures from a paper's methodology text and figure caption, orchestrating a multi-agent pipeline (Retriever, Planner, Stylist, Visualizer, Critic) targeting venues like NeurIPS, ICML, and ACL.

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - Guides creation of graphical abstracts, schematic diagrams, workflow visualizations, and architecture diagrams, covering both programmatic and design-tool approaches.

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - Creates publication-quality scientific diagrams using an AI image model with smart iterative refinement, re-generating only when a separate quality-review pass scores below threshold, specialized in neural network architectures, system diagrams, flowcharts, and biological pathways.

## Experiment Management & Reproducibility

*Running experiments, tracking what happened, and making the result reproducible by someone else.*

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - Surveys papers in a research direction to extract the benchmarks, datasets, metrics, and evaluation protocols in common use, or extracts them from a single given paper.

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - Takes bulk RNA-seq reads through quality control, trimming, alignment, and quantification to a gene-level count matrix, gating on experimental design and strandedness before differential expression.

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - Designs an evidence package for a CCF-venue paper, covering datasets, baselines, metrics, and ablations.

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - Scaffolds an R or bioinformatics analysis project on a read/write/checkpoints layout that keeps immutable inputs, tracked code, and untracked outputs separate.

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - Audits an ML pipeline for train-test contamination, temporal and spatial leakage, target and proxy leakage, preprocessing leakage, and evaluation contamination, classifying each finding by severity.

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) - Summarizes ML experiment logs into structured Chinese output with evidence/speculation separated and a weekly-update abstract. `zh`

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - Governs finite-element and CAE analysis claims across Ansys, Abaqus, Nastran, OpenFOAM, and COMSOL, enforcing idealization review, mesh-independence via GCI, verification and validation, and human sign-off gates.

- [FiftyOne Model Evaluation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-model-evaluation) - Evaluates CV model predictions against ground truth using standard protocols like COCO and Open Images.

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - Verifies a LibreYOLO training run's config, dataset, and metrics against project conventions before a checkpoint is trusted.

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - Resolves canonical CMSO and ASMO ontology terms for computational materials data, checking class hierarchies and property domain and range before a relationship is asserted.

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) - Standardizes lab experiment logging from photos, voice, or text into YAML-frontmattered Markdown written to a plain local folder, with optional Obsidian vault and Feishu integrations.

- [Nature Paper Skills: Results Analysis](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/research/results-analysis) - Runs a systematic pipeline for analyzing ML experimental results, running statistical tests, and generating paper-ready figures and text.

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - Turns an arXiv paper into a citation-anchored Python implementation, tagging each module to the paper section it implements and flagging rather than guessing at ambiguities.

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - Scans AI coding-agent cache directories and extracts numeric experiment results into a structured format.

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - Enforces same-epoch alignment when comparing ML training runs and separates proxy metrics from downstream targets.

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - Diagnoses a failing ML experiment with a five-step evidence-before-action protocol covering process state, GPU, disk, logs, and checkpoints.

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - Walks through seven stages from an arXiv URL to a measurable replication run, handling missing code, hyperparameters, and private datasets via public-substitute strategies.

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - Prepares research code for public release alongside a paper submission, covering repository cleanup, dependency auditing, and a reproducibility checklist.

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - Packages research code and data for artifact-evaluation submission — README and appendix, anonymization for double-blind review, ACM badge taxonomy, and archival-DOI guidance for Zenodo or Software Heritage — checked against live venue rules.

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - Assembles a submission-ready replication package to the AEA Data and Code Availability Standard, including a replication README, dataset manifest, computational-requirements capture, a table/figure-to-script map, and a confidential-data deposit plan.

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - Covers the methodology of multi-job experiment campaigns on Slurm clusters — walltime sizing, job and array shaping, submission order, and diagnosing runs that produced nothing or silently used the wrong configuration.

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - Audits whether metrics produced by an author's own local code still match the tables and claims reported in their paper, within stated tolerances, and reports mismatches separately from reproduction failures.

## Statistical Analysis

*Choosing and running the analysis: regression, causal inference, survey weighting, meta-analysis, Bayesian modelling.*

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - Selects and stress-tests a causal identification strategy for empirical economics, covering staggered difference-in-differences, weak-IV-robust instrumental variables, regression discontinuity, synthetic control, and shift-share designs.

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - Detects statistical errors and methodological fallacies in empirical research content, with structured severity levels.

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - Analyzes complex-sample survey data in Python with strata, PSU, and weight handling, variance estimation, and survey-weighted GLM for datasets such as NHANES, CPS, and DHS.

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - Analyzes complex survey data in R with the survey package, covering design objects, weighted means and totals, survey-weighted regression, domain estimation, and replicate weights (BRR, jackknife, bootstrap).

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - Estimates high-dimensional fixed-effects models in R with multi-way fixed effects, IV estimation, TWFE and Sun-Abraham difference-in-differences, and clustered or heteroskedasticity-robust standard errors.

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - Selects statistical tests, checks their assumptions, computes effect sizes, and reports results in APA format across t-tests, ANOVA, regression, and Bayesian alternatives.

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - Generates reproducible Python or R code for diagnostic accuracy, agreement, survival, propensity-score, and survey-weighted analyses, with a protected-health-information check before reading any data file.

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - Runs the meta-analysis pipeline from PROSPERO protocol registration and risk-of-bias assessment through statistical synthesis and PRISMA-compliant reporting.

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - Analyzes experiment result files, runs significance tests and model comparisons, and drafts a Results section with accompanying figures.

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) - Runs a network meta-analysis from PICO to manuscript skeleton — search execution, dual-model screening, extraction, risk-of-bias, frequentist and Bayesian synthesis in R, GRADE rating, and PRISMA-NMA reporting — with five mandatory human decision gates and an audit log. `zh`

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - Builds, fits, and validates Bayesian hierarchical models with PyMC, covering MCMC sampling, variational inference, and posterior predictive checks.

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - Maps Stata commands (reghdfe, xtreg, ivregress, margins, esttab, svy:) to their R equivalents for researchers moving an analysis between the two ecosystems.

## Qualitative & Mixed Methods

*Interviews, fieldwork, and coded text — thematic analysis, grounded theory, ethnography, intercoder reliability.*

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - Covers qualitative design and analysis across five traditions — thematic analysis, grounded theory, interpretative phenomenological analysis, ethnography, and case study — with trustworthiness criteria.

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - Scaffolds and indexes reflexive, comparative, integrative, and decision memos grounded in coded units, keeping the researcher's interpretation separate from the machine audit log.

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - Tracks multi-dimensional theoretical saturation, generates phase-sensitive methodological isolation rules, and logs rule changes and overrides to a reflexivity journal.

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - Codes qualitative data and builds codebooks with deductive, inductive, and hybrid coding, code frequencies, co-occurrence analysis, and intercoder reliability.

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - Runs grounded theory, reflexive thematic analysis, and content analysis with codebook development and inter-coder reliability checks, exporting to NVivo, ATLAS.ti, Dedoose, and MAXQDA formats.

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - Conducts thematic analysis of interviews, focus groups, or open-ended responses following Braun and Clarke's six-phase framework, covering the four upfront analytic decisions and a 15-point quality checklist.

## Interpretability

*Opening up a trained model to see what it computes, and explaining individual predictions.*

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - Inspects and manipulates the internals of any PyTorch model with nnsight, including remote execution against models too large for local GPUs via NDIF.

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - Performs causal tracing, activation patching, and interchange intervention training on PyTorch models through pyvene's declarative, dict-based intervention framework.

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - Trains and analyzes sparse autoencoders to decompose polysemantic model activations into interpretable features, wrapping the SAELens and TransformerLens libraries.

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - Explains and audits machine-learning predictions with SHAP, covering explainer/masker selection, feature-attribution computation and validation, multi-output explanations, and local/global visualizations.

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - Reverse-engineers transformer algorithms by inspecting attention patterns and running activation-patching experiments through TransformerLens HookPoints.

## Paper-Grade Plotting & Visualization

*Charts plotted from results, to the standard a journal or conference expects.*

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - Generates runnable matplotlib/seaborn/mermaid code for research figures with a decision guide between quantitative and conceptual diagrams.

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - Produces publication-ready matplotlib figures — bar, trend, scatter, heatmap, and multi-panel layouts — in a fixed house style with print/vector export conventions for AI conference and journal submissions.

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - Validates tabular longitude and latitude data and renders reproducible SVG site maps, applying a per-row public, generalized, or restricted visibility policy with coordinate rounding.

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - Creates, revises, and audits submission-grade scientific figures for high-impact venues in Python or R, with multi-panel support and journal-ready export.

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - Plans and audits manuscript figure organization, enforcing one claim per figure, assigning panel roles, and deciding main-versus-supplement placement before legends or results text are written.

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - Generates publication-quality figures and conceptual diagrams for academic papers from experimental data and an outline, with optional VLM-based critique refinement.

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - Enforces Edward Tufte's data-visualization principles — data-ink ratio, direct labeling, range-frame axes — across multiple charting libraries for academic plotting.

## Writing & Submission

*Drafting the manuscript and getting it submission-ready — structure, formatting, venue adaptation, self-checks before it goes out.*

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - Turns a paper into a slide deck and optionally a narrated demo video, covering script drafting, slide generation, text-to-speech narration, and video assembly.

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - Plans, drafts, revises, and venue-adapts research paper text for CCF-ranked venues while preserving the user's own idea scope and evidence.

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - Builds an editable conference poster from author-approved local content, checking physical dimensions, printer constraints, accessibility, asset provenance, and export readiness.

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - Creates and edits .docx files with Chinese academic formatting conventions such as three-line tables and block formulas. `zh`

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - Synthesizes economics-writing guidance from 50+ style guides into executable rules for drafting and revising economics papers.

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - Guides grant proposal architecture, funder fit evaluation, and budget design for academic research funding.

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - Adapts an academic manuscript to a target journal's writing conventions by analyzing a reference corpus and revising the manuscript section by section.

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - Handles LaTeX document creation, compilation, format conversion, and document analysis for academic writing.

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) - Assists graduate students with Chinese LaTeX thesis projects, covering compilation diagnosis, GB/T 7714 bibliography formatting, structure review, and blind-review anonymization. `zh`

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - Runs a late-stage manuscript preflight audit that cross-checks claims, figures, legends, methods, and supplement against venue expectations before submission or resubmission.

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) - Fixes LaTeX float placement defects — distance from first reference, width mismatch, clustering, page orphaning — in academic paper source code.

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) - Fixes LaTeX overflow defects — overfull boxes, long formulas, and URL overflows — starting from layout-only edits and escalating to delegated rewording when layout alone cannot fit it.

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - Converts raw research materials into a structured outline with a plotting plan, literature-search plan, and section plan for academic paper writing.

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - Verifies paper claims against code and data through numerical-accuracy, terminology-consistency, and formula-code alignment checks.

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - Classifies a confirmed error in an already-published paper as a corrigendum, erratum, expression of concern, or retraction, then drafts the co-author notification, editor request, and public notice.

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - Converts a published paper into a plain-language summary, graphical-abstract concept, and platform-tailored social copy, holding every version to what the paper's findings actually support.

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - Guides revision of ML/CV/NLP papers with paragraph-level clarity checks, reverse outlining, topic-sentence mapping, and claim-evidence alignment audits.

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - Removes common AI-writing patterns from academic and research prose to restore a more natural voice.

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) - Writes a survey draft around a research topic by organizing multiple papers into problem-driven, method-evolution narratives rather than paper-by-paper summaries.

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - Assists with existing Typst manuscripts covering compilation, venue formatting, grammar, bibliography, and submission readiness.

## Peer Review & Rebuttal

*The other side of submission: refereeing someone else's manuscript, and answering the reviews of your own.*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - Simulates a five-person international journal peer-review panel with field-specific reviewer personas, producing structured editorial decisions and revision roadmaps.

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - Orchestrates a reviewer-side integrity forensics sweep of a research paper — building a span-anchored evidence ledger, fanning out cross-model auditors for citation, experiment, consistency, and baseline-comparison fabrication, then computing a deterministic verdict for a human reviewer.

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - Reviews a manuscript against CCF/target-venue criteria across novelty, soundness, evidence, writing quality, and format compliance, simulating a reviewer/AC panel.

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - Produces a referee-grade report on an economics paper, checking identification strategy, inference, tables, equations, and references, and outputs a findings ledger with a prioritized revision plan.

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - Converts peer reviews into evidence-based rebuttal packages through triage, strategy, drafting, and tone-repair modes.

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - Structured review and revision workflow for academic manuscripts with six operating modes scaled to effort level.

## How these entries are checked

This is a curated list, not a certification. Each entry is chosen by a person reading its `SKILL.md`. A description states what the skill does; it is not a report of it having been run end to end on your problem. No entry claims an executable end-to-end test, because none has been run. Entries whose `SKILL.md` is not in English carry a language tag next to the name.

**Two levels of checking.** `static check` (109 of 146) means the path, license, commit date, and required capabilities were verified against the live repo and the `SKILL.md` was read. `audited` (37 of 146) means someone additionally walked the skill's own instructions against the files it ships, against a written audit spec, and got one of: `works`, `works with caveats` (delivers the outcome but with a condition worth knowing up front), or `unverifiable` (couldn't be assessed without credentials, paid access, or hardware). Auditing has removed entries that read well but could not work for anyone but their author.

**License, stars, capability flags, and per-entry check status live in the machine-readable index, not inline here** — [`index.json`](index.json) and [`index.csv`](index.csv), generated from the same source as this page. Look a skill up there before you open it if you care about its license, whether it needs network/credentials/hooks, or its exact audit verdict. In short: a `license:` in the skill's own frontmatter wins over the repo LICENSE where they disagree; `repo ★N` is that *repo's* stars, never the skill's own rating — 94% of these skills live inside someone's larger repo, so a skill in a 20,000-star monorepo may have been committed once and never used.

The structural checks behind every entry — is it substantive, is it template-farmed, does the repo verify — are discipline-independent, and they are what this list guarantees. Whether a clinical-trial, qualitative-coding, or econometrics skill is *methodologically correct for your field* is a judgment its curator cannot make across every discipline represented here. Treat domain entries as leads to evaluate, not as vetted by a subject expert.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — this list is data-driven, don't edit README.md by hand.
