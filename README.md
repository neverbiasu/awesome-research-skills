# Awesome Research Skills [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> Agent Skills for people still doing their own research — not autoresearch pipelines.

> Sections follow the research lifecycle (ideation → literature → study design → data → method → analysis → visualization → writing), not alphabetical order. Not scoped to one discipline: alongside the ML/CV tooling there are entries for study protocols, qualitative coding, survey statistics, and systematic reviews.

> Honest disclosure: for 95% of entries below, the star count is the *parent repo's* stars, not a measure of this specific skill's own popularity — most Agent Skills right now live as a subfolder in someone's larger repo, not as their own independently-starred project. That's a fact about how young this ecosystem is; the raw data behind every entry is in `data/skills.json` if you want to check which ones.

> Curation method: each entry is chosen by reading its SKILL.md and checking it against the live repo (stars, license, last commit on that exact path) — not by running it end-to-end. Descriptions state what the skill claims to do; verify it yourself before depending on it for real work.

> On domain expertise: the structural checks behind every entry (is it substantive, is it template-farmed, does the repo verify) are discipline-independent, and they are what this list actually guarantees. Whether a clinical-trial, qualitative-coding, or econometrics skill is *methodologically correct for your field* is a judgment its curator cannot make for every discipline represented here — treat domain entries as leads to evaluate, not as vetted by a subject expert.

## Contents

- [Direction Scanning & Ideation](#direction-scanning--ideation)
- [Literature Review](#literature-review)
- [Study Design & Protocol](#study-design--protocol)
- [Data & Annotation](#data--annotation)
- [Model Training & Fine-Tuning](#model-training--fine-tuning)
- [Generative Image/Video Editing & Eval](#generative-imagevideo-editing--eval)
- [Diagrams & Schematics](#diagrams--schematics)
- [Experiment Management & Reproducibility](#experiment-management--reproducibility)
- [Statistical Analysis](#statistical-analysis)
- [Qualitative & Mixed Methods](#qualitative--mixed-methods)
- [Interpretability](#interpretability)
- [Deployment & Inference Optimization](#deployment--inference-optimization)
- [Paper-Grade Plotting & Visualization](#paper-grade-plotting--visualization)
- [Writing & Submission](#writing--submission)

## Direction Scanning & Ideation

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) - Analyzes literature and early ideas to identify grounded research gaps and testable entry points without forcing novelty claims. `skill` `MIT` · ⭐325 · updated 2026-04-05.

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - Guides generation of falsifiable, structured research hypotheses from user-provided notes and content. `skill` `unverified` · ⭐46 · updated 2026-05-15.

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - Structures research project initiation through 5W1H brainstorming, systematic literature review, multi-dimensional gap analysis, and SMART research-question formulation. `skill` `MIT` · ⭐4983 · updated 2026-05-13.

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - Applies structured ideation frameworks to surface research directions when entering a new problem space or reconsidering a project's direction. `skill` `MIT` · ⭐11572 · updated 2026-02-19.

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - Applies cognitive-science creativity techniques — combinatorial creativity, analogical reasoning, and constraint manipulation — to generating research directions. `skill` `MIT` · ⭐11572 · updated 2026-02-19.

## Literature Review

- [arXiv Skills](https://github.com/ultimatile/arxiv-skills/tree/HEAD/skills/arxiv-lookup) - Converts an arXiv paper (LaTeX-source-first, PDF fallback) into implementation-ready Markdown with preserved math, and looks up papers by DOI/title via the arXiv API. `suite` `net` `MIT` · ⭐39 · updated 2026-04-09.

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - Generates a BibTeX entry from a DOI, PMID, arXiv ID, or paper title by querying CrossRef, PubMed, arXiv, Semantic Scholar, and ChemRxiv. `skill` `net` `LGPL-3.0` · ⭐17 · updated 2026-02-15.

- [Semantic Scholar Skill](https://github.com/agents365-ai/semanticscholar-skill/tree/HEAD/skills/semanticscholar-skill) - Wraps the Semantic Scholar Graph API for paper search, citation-graph traversal, and author lookup across 200M+ papers, rate-limited for multi-agent use. `skill` `net` `MIT` · ⭐60 · updated 2026-05-10.

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - Adds citations to manuscript text by searching only Nature Portfolio, AAAS Science, and Cell Press titles, filtered by date, and exports a single reference-manager file. `skill` `net` `Apache-2.0` · ⭐33299 · updated 2026-08-03.

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - Structures a deep reading of one scientific paper into a fixed 16-section, evidence-grounded research card. `skill` `Apache-2.0` · ⭐33299 · updated 2026-08-03.

- [Nature Literature Pipeline](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-literature-pipeline) - Searches multiple literature sources, scores candidates across six dimensions, delivers digests, and archives results with deduplication. `skill` `net` `Apache-2.0` · ⭐33300 · updated 2026-08-03.

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - Queries Google NotebookLM notebooks from Claude Code for citation-backed, source-grounded answers via browser automation. `skill` `net` `MIT` · ⭐7566 · updated 2025-11-21.

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - Monitors arXiv, OpenReview, and conference feeds for papers overlapping with a given research idea, producing actionable relax/research/follow-up signals. `skill` `net` `MIT` · ⭐1453 · updated 2026-06-09.

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - Searches and extracts metadata from CNKI, China's primary academic database, via Chrome DevTools browser automation. `suite` `net` `unverified` · ⭐810 · updated 2026-02-28.

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) - Reads and analyzes academic papers from PDF, arXiv, or Zotero, generating structured notes with figures, formulas, and concept links. `skill` `Apache-2.0` · ⭐1106 · updated 2026-07-10.

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) - Automates a daily paper-recommendation pipeline — fetch, review, and note-taking — for keeping up with recent AI research. `skill` `net` `Apache-2.0` · ⭐1106 · updated 2026-07-10.

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) - Converts an academic paper into a detailed HTML article via a six-round workflow with code search, formula rendering, and diagrams. `skill` `net` `unverified` · ⭐968 · updated 2026-05-21.

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) - Generates formatted academic citations in GB/T 7714, IEEE, APA, MLA, Chicago, Harvard, and Vancouver styles by searching literature through the Qinyan Academic OpenAPI. `skill` `net` `MIT` · ⭐759 · updated 2026-03-13.

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - Searches Google Scholar via browser automation, returning structured results with citation counts and full-text links. `suite` `net` `MIT` · ⭐470 · updated 2026-03-04.

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - Conducts patent prior-art searches, IP landscape mapping, and patentability assessment for technology research. `skill` `net` `unverified` · ⭐449 · updated 2026-06-22.

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - Executes multi-step literature and technical research using the Google Gemini Deep Research Agent to produce a detailed cited report. `skill` `net` `Apache-2.0` · ⭐364 · updated 2026-02-19.

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - Parses academic PDFs into clean Markdown with table and formula extraction, using MinerU's free Agent API or token-based Standard API. `skill` `net` `MIT` · ⭐91 · updated 2026-06-02.

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - Generates ranked paper candidates and related-work section summaries from a paper draft, using LLM-driven debate ranking over Semantic Scholar, arXiv, and OpenAlex with citation-graph expansion. `skill` `net` `Apache-2.0` · ⭐46 · updated 2026-05-07.

- [Academic Writing: Verify Claims](https://github.com/alessandrocaforio/academic-writing/tree/HEAD/.claude/skills/verify-claims) - Verifies thesis claims against a literature corpus stored in ChromaDB using RAG queries, extracting claims from LaTeX chapters and assessing evidentiary support for each. `skill` `MIT` · ⭐17 · updated 2026-02-17.

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - Guides a systematic literature review through the full 27-item PRISMA 2020 checklist, producing a journal-format Word manuscript, an annotated PRISMA flow diagram, and APA 7th referencing, explicitly excluding meta-analysis and statistical pooling. `skill` `unverified` · ⭐90 · updated 2026-03-28.

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - Searches bioRxiv preprint metadata and retrieves PDFs by keyword, author, date range, or subject category. `skill` `net` `unverified` · ⭐1044 · updated 2026-02-27.

## Study Design & Protocol

- [TW Research Ethics Reviewer](https://github.com/fw1201/tw-research-skills/tree/HEAD/tw-research-ethics-reviewer) - Provides structured self-assessment for research ethics compliance and IRB preparation. `skill` `unverified` · ⭐8 · updated 2026-05-08.

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - Generates clinical trial protocols for medical devices or drugs through a waypoint-based workflow, with a research-only mode for surveying similar registered trials before drafting. `skill` `unverified` · ⭐371 · updated 2026-06-15.

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - Drafts a structured preregistration document in OSF, AsPredicted, or AEA RCT Registry style, covering hypotheses, sampling plan, analysis plan, exclusions, and inference criteria, annotated with MUST/SHOULD/MAY clarity flags. `skill` `MIT` · ⭐1441 · updated 2026-06-09.

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - Computes statistical power, required sample size, and minimum detectable effect for two-arm RCTs with clustering, multi-arm designs, or simulation-based power for non-standard designs, producing a registry-ready power section. `skill` `MIT` · ⭐1441 · updated 2026-06-09.

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - Writes, revises, and evaluates IRB and ethics protocols for qualitative research, covering Common Rule exempt/expedited/full-board determination, protocol narrative, and data security planning. `skill` `unverified` · ⭐20 · updated 2026-07-27.

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - Designs qualitative data-collection instruments and protocols — interview guides, focus group guides, observation protocols, field note templates, and sampling strategies. `skill` `unverified` · ⭐20 · updated 2026-07-27.

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - Drafts and critiques survey question wording, response scales, and instrument flow against published social-science methodology to reduce measurement bias. `skill` `unverified` · ⭐39 · updated 2026-07-02.

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - Plans conjoint survey experiments, covering attribute architecture, randomization and orthogonality, power calculation, and AMCE/AMIE estimation. `skill` `unverified` · ⭐39 · updated 2026-07-02.

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - Reviews cohort logic, comparator choice, and validation strategy for medical studies to surface leakage and validity risks before analysis begins. `skill` `MIT` · ⭐246 · updated 2026-07-25.

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - Plans studies before data collection, covering randomization, blocking, factorial and crossover layouts, and cluster or adaptive designs. `skill` `MIT` · ⭐33151 · updated 2026-07-28.

## Data & Annotation

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - Analyzes dataset bias, distribution, and fairness before model training. `skill` `MIT` · ⭐357 · updated 2026-03-12.

- [FiftyOne Dataset Curation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-curation) - Inspects CV dataset schema, quality, class distributions, and embeddings, then creates curated subsets and train/val/test splits using FiftyOne. `skill` `Apache-2.0` · ⭐37 · updated 2026-05-18.

- [FiftyOne Dataset Import](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-import) - Imports and auto-detects dataset formats — images, video, point clouds, labels — into FiftyOne for CV research. `skill` `Apache-2.0` · ⭐37 · updated 2026-05-18.

- [FiftyOne Dataset Export](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-dataset-export) - Exports FiftyOne datasets to standard annotation formats — COCO, YOLO, VOC, CVAT, CSV — for downstream model training and sharing. `skill` `Apache-2.0` · ⭐37 · updated 2026-05-14.

- [Label Studio Setup](https://github.com/majiayu000/claude-skill-registry/tree/HEAD/skills/data/label-studio-setup) - Covers Label Studio installation, project setup, data import/export, labeling interface customization, quality control, and ML backend integration for image, text, audio, and video annotation. `skill` `MIT` · ⭐534 · updated 2026-04-20.

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - Searches HuggingFace Hub, OpenML, GitHub, and paper cross-references for datasets matching a stated research task, returning a ranked and deduplicated list. `skill` `net` `unverified` · ⭐1044 · updated 2026-02-26.

## Model Training & Fine-Tuning

- [HuggingFace Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - Trains and fine-tunes detection, classification, and SAM/SAM2 segmentation models on Hugging Face Jobs cloud GPUs. `skill` `net` `Apache-2.0` · ⭐10895 · updated 2026-03-23.

- [HuggingFace LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - Fine-tunes language and vision-language models via TRL or Unsloth on Hugging Face Jobs, covering SFT, DPO, GRPO, and reward modeling. `skill` `net` `Apache-2.0` · ⭐10895 · updated 2026-07-06.

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - Fine-tunes transformer language models via the TRL command-line interface, covering SFT, DPO, GRPO, KTO, RLOO, and reward modeling. `skill` `net` `Apache-2.0` · ⭐10895 · updated 2026-08-03.

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - Trains bi-encoder, cross-encoder, and SPLADE sparse embedding models with the sentence-transformers library. `skill` `net` `Apache-2.0` · ⭐10895 · updated 2026-05-07.

- [NVIDIA TAO Finetune HuggingFace Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - Fine-tunes a Hugging Face model using the NVIDIA TAO Toolkit's optimized training and export path. `skill` `net` `Apache-2.0` · ⭐2789 · updated 2026-06-22.

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - Runs a pre-flight checklist for long-running ML training jobs to catch misconfigured configs, paths, and monitoring before launch. `skill` `MIT` · ⭐357 · updated 2026-04-30.

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - Trains reinforcement learning agents with Stable Baselines3's production-ready PPO, SAC, DQN, TD3, DDPG, and A2C implementations on Gymnasium environments. `skill` `MIT` · ⭐32623 · updated 2026-07-26.

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - Organizes PyTorch training code into LightningModules with configured Trainers for multi-GPU/TPU scaling, distributed training (DDP, FSDP, DeepSpeed), and logging integrations (W&B, TensorBoard, MLflow). `skill` `MIT` · ⭐32623 · updated 2026-07-28.

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - Guides graph neural network development with PyTorch Geometric, covering node/link/graph classification, message-passing architectures (GCN, GAT, GraphSAGE, GIN), heterogeneous graphs, and neighbor sampling. `skill` `MIT` · ⭐32623 · updated 2026-07-26.

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - Provides version-aware guidance for PufferLib reinforcement-learning environments, vectorization, policies, training, evaluation, and checkpoint review. `skill` `MIT` · ⭐32623 · updated 2026-07-26.

## Generative Image/Video Editing & Eval

- [HuggingFace LoRA Space Builder](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-lora-space-builder) - Builds and publishes a Gradio demo Space for a given LoRA on FLUX, SDXL, Qwen-Image, LTX-Video, or Wan. `skill` `net` `Apache-2.0` · ⭐10895 · updated 2026-07-16.

- [GPT-Image2 Skill](https://github.com/wuyoscar/GPT-Image2-Skill/tree/HEAD/skills/gpt-image) - Generates and edits images via the GPT Image 2 API from natural-language prompts, with gallery-based reference-image matching. `skill` `net` `MIT` · ⭐4149 · updated 2026-05-23.

- [Video Toolkit: LTX-2](https://github.com/digitalsamba/claude-code-video-toolkit/tree/HEAD/.claude/skills/ltx2) - Generates short video clips from text or images using the LTX-2.3 model on Modal cloud GPU. `skill` `net` `MIT` · ⭐1894 · updated 2026-04-21.

- [K-Dense: Generate Image](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/generate-image) - Generates or edits images through the OpenRouter Image API across multiple backends (Gemini, FLUX, Seedream, Recraft, GPT-Image) for figures, concept art, and visual assets. `skill` `net` `MIT` · ⭐32623 · updated 2026-07-31.

- [Analyze Generative Diffusion Model](https://github.com/pjt222/agent-almanac/tree/HEAD/skills/analyze-generative-diffusion-model) - Evaluates pre-trained diffusion models through FID, IS, and CLIP score metrics, noise-schedule inspection, cross-attention map extraction, and latent-space probing. `skill` `MIT` · ⭐28 · updated 2026-06-05.

## Diagrams & Schematics

- [TW Research Viz](https://github.com/fw1201/tw-research-skills/tree/HEAD/tw-research-viz) - Generates academic research visualizations — conceptual frameworks, literature maps, PRISMA flows, SEM path models, statistical charts — for papers, theses, and grant proposals. `skill` `net` `unverified` · ⭐8 · updated 2026-04-26.

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - Enforces a standalone-TikZ-to-PDF pipeline for academic paper figures, forbidding inline TikZ in paper source and requiring every figure to compile and be visually verified before insertion. `skill` `MIT` · ⭐291 · updated 2026-03-19.

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - Guides creation of graphical abstracts, schematic diagrams, workflow visualizations, and architecture diagrams, covering both programmatic and design-tool approaches. `skill` `MIT` · ⭐269 · updated 2026-03-15.

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - Reconstructs reference images of diagrams, figures, or architecture visuals into editable Draw.io files, prioritizing visual fidelity to the source over pure editability. `skill` `unverified` · ⭐5006 · updated 2026-07-16.

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - Generates and syntax-verifies Mermaid diagrams — flowcharts, sequence diagrams, class diagrams, ER diagrams, Gantt charts, and 18 other types — from a natural-language description. `skill` `MIT` · ⭐14235 · updated 2026-07-13.

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - Generates .drawio XML diagrams and exports to PNG/SVG/PDF/JPG via the native draw.io desktop CLI, covering flowcharts, architecture diagrams, ER/UML diagrams, network topology, and ML/DL model figures (Transformer, CNN, LSTM). `skill` `MIT` · ⭐7147 · updated 2026-07-25.

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - Classifies a paper's research type and mechanism to select an appropriate diagram structure — pipeline, architecture, comparison matrix, ablation matrix, or taxonomy tree — rather than mechanically applying one fixed template. `skill` `MIT` · ⭐176 · updated 2026-06-15.

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - Finds, edits, and verifies TikZ figures from a library of copyable icons and editable templates for neural network architectures, encoder-decoder diagrams, training pipelines, and system block diagrams. `skill` `unverified` · ⭐239 · updated 2026-07-04.

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - Generates publication-quality academic diagrams and pipeline figures from a paper's methodology text and figure caption, orchestrating a multi-agent pipeline (Retriever, Planner, Stylist, Visualizer, Critic) targeting venues like NeurIPS, ICML, and ACL. `skill` `net` `Apache-2.0` · ⭐6885 · updated 2026-06-22.

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - Creates publication-quality scientific diagrams using an AI image model with smart iterative refinement, re-generating only when a separate quality-review pass scores below threshold, specialized in neural network architectures, system diagrams, flowcharts, and biological pathways. `skill` `net` `MIT` · ⭐32623 · updated 2026-07-31.

## Experiment Management & Reproducibility

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - Verifies a LibreYOLO training run's config, dataset, and metrics against project conventions before a checkpoint is trusted. `skill` `unverified` · ⭐555 · updated 2026-07-05.

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - Turns an arXiv paper into a citation-anchored Python implementation, tagging each module to the paper section it implements and flagging rather than guessing at ambiguities. `skill` `MIT` · ⭐1468 · updated 2026-04-03.

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - Surveys papers in a research direction to extract the benchmarks, datasets, metrics, and evaluation protocols in common use, or extracts them from a single given paper. `skill` `MIT` · ⭐36 · updated 2026-04-24.

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) - Standardizes lab experiment logging from raw input (photos, voice, text) into YAML-frontmattered notes in an Obsidian vault. `skill` `net` `Apache-2.0` · ⭐33303 · updated 2026-08-03.

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - Designs an evidence package for a CCF-venue paper, covering datasets, baselines, metrics, and ablations. `skill` `MIT` · ⭐1453 · updated 2026-07-08.

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - Scans AI coding-agent cache directories and extracts numeric experiment results into a structured format. `skill` `unverified` · ⭐627 · updated 2026-04-17.

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - Diagnoses a failing ML experiment with a five-step evidence-before-action protocol covering process state, GPU, disk, logs, and checkpoints. `skill` `MIT` · ⭐357 · updated 2026-04-30.

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - Enforces same-epoch alignment when comparing ML training runs and separates proxy metrics from downstream targets. `skill` `MIT` · ⭐357 · updated 2026-04-30.

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - Walks through seven stages from an arXiv URL to a measurable replication run, handling missing code, hyperparameters, and private datasets via public-substitute strategies. `skill` `MIT` · ⭐357 · updated 2026-04-30.

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - Prepares research code for public release alongside a paper submission, covering repository cleanup, dependency auditing, and a reproducibility checklist. `skill` `MIT` · ⭐357 · updated 2026-03-12.

- [Nature Paper Skills: Results Analysis](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/research/results-analysis) - Runs a systematic pipeline for analyzing ML experimental results, running statistical tests, and generating paper-ready figures and text. `skill` `MIT` · ⭐410 · updated 2026-04-29.

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) - Summarizes ML experiment logs into structured Chinese output with evidence/speculation separated and a weekly-update abstract. `skill` `MIT` · ⭐325 · updated 2026-04-05.

- [FiftyOne Model Evaluation](https://github.com/voxel51/fiftyone-skills/tree/HEAD/skills/fiftyone-model-evaluation) - Evaluates CV model predictions against ground truth using standard protocols like COCO and Open Images. `skill` `Apache-2.0` · ⭐37 · updated 2026-05-14.

- [TW Research Data Management](https://github.com/fw1201/tw-research-skills/tree/HEAD/tw-research-data-management) - Guides data management planning, privacy compliance, anonymization, and file organization, with legal references to Taiwan PDPA and GDPR. `skill` `unverified` · ⭐8 · updated 2026-05-08.

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - Assembles a submission-ready replication package to the AEA Data and Code Availability Standard, including a replication README, dataset manifest, computational-requirements capture, a table/figure-to-script map, and a confidential-data deposit plan. `skill` `MIT` · ⭐1441 · updated 2026-06-09.

## Statistical Analysis

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - Detects statistical errors and methodological fallacies in empirical research content, with structured severity levels. `skill` `unverified` · ⭐46 · updated 2026-05-15.

- [DiD / Event Study](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/did-event-study) - Runs staggered difference-in-differences and event-study analysis by driving the canonical R and Stata packages, enforcing a doubly-robust default, a mandatory diagnostic and sensitivity suite, and uniform-band inference rather than reimplementing any estimator. `skill` `MIT` · ⭐1441 · updated 2026-06-09.

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - Analyzes complex survey data in R with the survey package, covering design objects, weighted means and totals, survey-weighted regression, domain estimation, and replicate weights (BRR, jackknife, bootstrap). `skill` `LGPL-3.0` · ⭐226 · updated 2026-07-15.

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - Estimates high-dimensional fixed-effects models in R with multi-way fixed effects, IV estimation, TWFE and Sun-Abraham difference-in-differences, and clustered or heteroskedasticity-robust standard errors. `skill` `LGPL-3.0` · ⭐226 · updated 2026-07-24.

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - Maps Stata commands (reghdfe, xtreg, ivregress, margins, esttab, svy:) to their R equivalents for researchers moving an analysis between the two ecosystems. `skill` `LGPL-3.0` · ⭐226 · updated 2026-07-24.

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - Analyzes experiment result files, runs significance tests and model comparisons, and drafts a Results section with accompanying figures. `skill` `unverified` · ⭐1044 · updated 2026-02-26.

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - Runs the meta-analysis pipeline from PROSPERO protocol registration and risk-of-bias assessment through statistical synthesis and PRISMA-compliant reporting. `skill` `MIT` · ⭐246 · updated 2026-08-10.

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - Generates reproducible Python or R code for diagnostic accuracy, agreement, survival, propensity-score, and survey-weighted analyses, with a protected-health-information check before reading any data file. `skill` `MIT` · ⭐246 · updated 2026-07-23.

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - Selects statistical tests, checks their assumptions, computes effect sizes, and reports results in APA format across t-tests, ANOVA, regression, and Bayesian alternatives. `skill` `MIT` · ⭐33151 · updated 2026-07-26.

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - Builds, fits, and validates Bayesian hierarchical models with PyMC, covering MCMC sampling, variational inference, and posterior predictive checks. `skill` `MIT` · ⭐33151 · updated 2026-07-28.

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - Analyzes complex-sample survey data in Python with strata, PSU, and weight handling, variance estimation, and survey-weighted GLM for datasets such as NHANES, CPS, and DHS. `skill` `LGPL-3.0` · ⭐227 · updated 2026-07-15.

## Qualitative & Mixed Methods

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - Conducts thematic analysis of interviews, focus groups, or open-ended responses following Braun and Clarke's six-phase framework, covering the four upfront analytic decisions and a 15-point quality checklist. `skill` `MIT` · ⭐12 · updated 2026-05-11.

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - Codes qualitative data and builds codebooks with deductive, inductive, and hybrid coding, code frequencies, co-occurrence analysis, and intercoder reliability. `skill` `unverified` · ⭐20 · updated 2026-07-27.

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - Runs grounded theory, reflexive thematic analysis, and content analysis with codebook development and inter-coder reliability checks, exporting to NVivo, ATLAS.ti, Dedoose, and MAXQDA formats. `skill` `net` `unverified` · ⭐123 · updated 2026-07-14.

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - Covers qualitative design and analysis across five traditions — thematic analysis, grounded theory, interpretative phenomenological analysis, ethnography, and case study — with trustworthiness criteria. `skill` `net` `MIT` · ⭐58 · updated 2026-07-02.

## Interpretability

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - Trains and analyzes sparse autoencoders to decompose polysemantic model activations into interpretable features, wrapping the SAELens and TransformerLens libraries. `skill` `MIT` · ⭐225368 · updated 2026-07-24.

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - Explains and audits machine-learning predictions with SHAP, covering explainer/masker selection, feature-attribution computation and validation, multi-output explanations, and local/global visualizations. `skill` `MIT` · ⭐32623 · updated 2026-07-23.

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - Inspects and manipulates the internals of any PyTorch model with nnsight, including remote execution against models too large for local GPUs via NDIF. `skill` `net` `MIT` · ⭐11572 · updated 2025-12-17.

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - Performs causal tracing, activation patching, and interchange intervention training on PyTorch models through pyvene's declarative, dict-based intervention framework. `skill` `MIT` · ⭐11572 · updated 2025-12-17.

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - Reverse-engineers transformer algorithms by inspecting attention patterns and running activation-patching experiments through TransformerLens HookPoints. `skill` `MIT` · ⭐11572 · updated 2025-12-17.

## Deployment & Inference Optimization

- [NVIDIA TAO Run Inference Service](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-run-inference-service) - Stands up and runs a NVIDIA TAO-trained model as a live inference service. `skill` `net` `Apache-2.0` · ⭐2789 · updated 2026-06-22.

- [NVIDIA Inference Builder](https://github.com/NVIDIA-AI-IOT/inference_builder/tree/HEAD/skills/inference-builder) - Generates deployable GPU-accelerated vision and video inference pipelines from a YAML config, targeting DeepStream, Triton, vLLM, or TensorRT-LLM backends. `skill` `Apache-2.0` · ⭐72 · updated 2026-05-07.

- [vLLM Ascend](https://github.com/ascend-ai-coding/awesome-ascend-skills/tree/HEAD/skills/inference/vllm-ascend) - Serves LLM inference on Huawei Ascend NPUs via the vLLM Ascend plugin, covering batch inference, API serving, and quantization. `suite` `net` `unverified` · ⭐154 · updated 2026-05-18.

- [Video Toolkit: RunPod Deployment](https://github.com/digitalsamba/claude-code-video-toolkit/tree/HEAD/.claude/skills/runpod) - Deploys five video/image processing models (Qwen-edit, Real-ESRGAN, ProPainter, SadTalker, Qwen3-TTS) as RunPod serverless endpoints with pay-per-second billing. `skill` `net` `MIT` · ⭐1894 · updated 2026-03-22.

- [K-Dense: Optimize for GPU](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/optimize-for-gpu) - Converts CPU-bound Python (NumPy, pandas, scikit-learn, NetworkX, GeoPandas, Faiss workloads) to NVIDIA GPU acceleration via CuPy, Numba CUDA, cuDF, cuML, cuGraph, and related RAPIDS libraries. `skill` `MIT` · ⭐32623 · updated 2026-07-26.

- [GGUF Quantization](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/10-optimization/gguf) - Converts and quantizes models to GGUF format for llama.cpp inference at 2-8 bit precision, covering Hugging Face conversion, imatrix-based quantization, and OpenAI-compatible server deployment. `skill` `MIT` · ⭐11393 · updated 2025-11-25.

- [Modal](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/modal) - Deploys and serves AI/ML models on Modal's serverless cloud platform, covering on-demand GPU workloads, web endpoint serving, batch job scheduling, and scaling Python code to cloud containers. `skill` `net` `MIT` · ⭐32623 · updated 2026-07-26.

## Paper-Grade Plotting & Visualization

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - Produces publication-ready matplotlib figures — bar, trend, scatter, heatmap, and multi-panel layouts — in a fixed house style with print/vector export conventions for AI conference and journal submissions. `skill` `unverified` · ⭐2970 · updated 2026-06-24.

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - Creates, revises, and audits submission-grade scientific figures for high-impact venues in Python or R, with multi-panel support and journal-ready export. `skill` `Apache-2.0` · ⭐33299 · updated 2026-08-03.

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - Generates publication-quality figures and conceptual diagrams for academic papers from experimental data and an outline, with optional VLM-based critique refinement. `skill` `net` `unverified` · ⭐627 · updated 2026-04-10.

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - Plans and audits manuscript figure organization, enforcing one claim per figure, assigning panel roles, and deciding main-versus-supplement placement before legends or results text are written. `skill` `MIT` · ⭐410 · updated 2026-07-12.

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - Generates runnable matplotlib/seaborn/mermaid code for research figures with a decision guide between quantitative and conceptual diagrams. `skill` `unverified` · ⭐46 · updated 2026-05-15.

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - Enforces Edward Tufte's data-visualization principles — data-ink ratio, direct labeling, range-frame axes — across multiple charting libraries for academic plotting. `skill` `MIT` · ⭐195 · updated 2026-02-19.

## Writing & Submission

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - Simulates a five-person international journal peer-review panel with field-specific reviewer personas, producing structured editorial decisions and revision roadmaps. `skill` `hooks` `unverified` · ⭐40865 · updated 2026-08-01.

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - Guides revision of ML/CV/NLP papers with paragraph-level clarity checks, reverse outlining, topic-sentence mapping, and claim-evidence alignment audits. `skill` `MIT` · ⭐5795 · updated 2026-06-20.

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - Plans, drafts, revises, and venue-adapts research paper text for CCF-ranked venues while preserving the user's own idea scope and evidence. `skill` `MIT` · ⭐1453 · updated 2026-07-08.

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - Reviews a manuscript against CCF/target-venue criteria across novelty, soundness, evidence, writing quality, and format compliance, simulating a reviewer/AC panel. `skill` `MIT` · ⭐1453 · updated 2026-07-08.

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - Structured review and revision workflow for academic manuscripts with six operating modes scaled to effort level. `skill` `unverified` · ⭐614 · updated 2026-06-16.

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - Converts peer reviews into evidence-based rebuttal packages through triage, strategy, drafting, and tone-repair modes. `skill` `unverified` · ⭐614 · updated 2026-06-16.

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - Converts raw research materials into a structured outline with a plotting plan, literature-search plan, and section plan for academic paper writing. `skill` `unverified` · ⭐627 · updated 2026-06-02.

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - Handles LaTeX document creation, compilation, format conversion, and document analysis for academic writing. `skill` `unverified` · ⭐681 · updated 2026-08-03.

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - Adapts an academic manuscript to a target journal's writing conventions by analyzing a reference corpus and revising the manuscript section by section. `skill` `MIT` · ⭐738 · updated 2026-05-15.

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - Verifies paper claims against code and data through numerical-accuracy, terminology-consistency, and formula-code alignment checks. `skill` `MIT` · ⭐357 · updated 2026-03-12.

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - Runs a late-stage manuscript preflight audit that cross-checks claims, figures, legends, methods, and supplement against venue expectations before submission or resubmission. `skill` `MIT` · ⭐410 · updated 2026-05-08.

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) - Writes a survey draft around a research topic by organizing multiple papers into problem-driven, method-evolution narratives rather than paper-by-paper summaries. `skill` `MIT` · ⭐325 · updated 2026-04-05.

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - Assists with existing Typst manuscripts covering compilation, venue formatting, grammar, bibliography, and submission readiness. `skill` `unverified` · ⭐404 · updated 2026-07-27.

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) - Assists graduate students with Chinese LaTeX thesis projects, covering compilation diagnosis, GB/T 7714 bibliography formatting, structure review, and blind-review anonymization. `skill` `unverified` · ⭐404 · updated 2026-07-27.

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - Guides grant proposal architecture, funder fit evaluation, and budget design for academic research funding. `skill` `unverified` · ⭐449 · updated 2026-06-22.

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - Synthesizes economics-writing guidance from 50+ style guides into executable rules for drafting and revising economics papers. `skill` `MIT` · ⭐510 · updated 2026-07-15.

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - Creates and edits .docx files with Chinese academic formatting conventions such as three-line tables and block formulas. `skill` `MIT` · ⭐348 · updated 2026-06-30.

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - Removes common AI-writing patterns from academic and research prose to restore a more natural voice. `skill` `MIT` · ⭐337 · updated 2026-03-18.

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) - Fixes LaTeX overflow defects — overfull hboxes, long formulas, URL overflows — in academic paper source files through minimal, non-semantic edits. `skill` `MIT` · ⭐332 · updated 2026-05-08.

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) - Fixes LaTeX float placement defects — distance from first reference, width mismatch, clustering, page orphaning — in academic paper source code. `skill` `MIT` · ⭐332 · updated 2026-05-08.

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - Orchestrates a reviewer-side integrity forensics sweep of a research paper — building a span-anchored evidence ledger, fanning out cross-model auditors for citation, experiment, consistency, and baseline-comparison fabrication, then computing a deterministic verdict for a human reviewer. `suite` `net` `MIT` · ⭐None · updated 2026-07-14.

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - Turns a paper into a slide deck and optionally a narrated demo video, covering script drafting, slide generation, text-to-speech narration, and video assembly. `skill` `net` `unverified` · ⭐1044 · updated 2026-03-04.

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - Drafts and completes rigorous mathematical proofs of theorems, lemmas, and propositions from a stated result and its assumptions. `skill` `MIT` · ⭐14483 · updated 2026-07-13.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — this list is data-driven, don't edit README.md by hand.
