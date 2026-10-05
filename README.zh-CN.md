# Awesome Research Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/skills-142-blue?style=flat) [![Last Commit](https://img.shields.io/github/last-commit/neverbiasu/awesome-research-skills?style=flat)](https://github.com/neverbiasu/awesome-research-skills/commits/main)

[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md)

> 面向研究者的 142 个 Agent Skill，逐个阅读、逐个挑选。每一条都指向一个具体的 `SKILL.md` 目录，而不是一个“里面可能有点东西”的仓库。

收录的是你自己动手做的那些步骤：查找已有工作、设计研究、把方法形式化、整理数据、跑实验、统计分析、定性分析、作图、写作、同行评审。完整的自动科研流水线和 MLOps/部署工具不在收录范围内。

每一条都对照其仓库读过并核对过（许可证、最近提交、运行所需的网络/凭据/hook），不收模板批量生成或已无人维护的条目。其中 46 条还按一份书面规范逐步动手走过一遍。数据核对至 2026-10-05；每条属于 `static check` 还是 `audited: <结论>`，记录在 `index.json` 中，定义见下文“这些条目是怎么检查的”。

条目名称和链接与英文版一致；描述为译文，如有出入以[英文版](README.md)为准。

## 目录

- [方向探索与选题](#方向探索与选题)
- [文献综述](#文献综述)
- [研究设计与方案](#研究设计与方案)
- [方法形式化与理论](#方法形式化与理论)
- [数据与标注](#数据与标注)
- [模型训练与微调](#模型训练与微调)
- [示意图与框图](#示意图与框图)
- [实验管理与可复现性](#实验管理与可复现性)
- [统计分析](#统计分析)
- [定性与混合方法](#定性与混合方法)
- [可解释性](#可解释性)
- [论文级绘图与可视化](#论文级绘图与可视化)
- [写作与投稿](#写作与投稿)
- [同行评审与答辩](#同行评审与答辩)
- [这些条目是怎么检查的](#这些条目是怎么检查的)

## 方向探索与选题

*把模糊的兴趣变成一个表述清楚、可以检验的研究问题。*

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - 引导从用户提供的笔记和材料中生成可证伪、结构化的研究假设。

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - 在进入新问题领域或重新考虑项目方向时，运用结构化的构思框架找出研究方向。

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - 通过 5W1H 头脑风暴、系统文献综述、多维度缺口分析和 SMART 研究问题表述，为研究项目的启动提供结构。

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - 把认知科学中的创造力技巧（组合创造、类比推理和约束操纵）用于生成研究方向。

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) `zh` - 分析文献和早期想法，找出有依据的研究缺口和可检验的切入点，不强行声称新颖性。

## 文献综述

*查找、阅读和综合已有工作，并保证引用准确。*

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - 按关键词、作者、日期范围或学科类别检索 bioRxiv 预印本元数据并获取 PDF。

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - 监控 arXiv、OpenReview 和会议更新中与给定研究想法重叠的论文，给出可执行的放心/调研/跟进信号。

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - 通过 Chrome DevTools 浏览器自动化检索中国知网（CNKI）并提取文献元数据。

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - 围绕一个引导问题，用论断-来源台账和综合矩阵构建发展理论的文献综述，并阻止逐篇罗列式总结和没有依据的研究缺口声明。

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) `zh` - 阅读并分析来自 PDF、arXiv 或 Zotero 的学术论文，生成包含图表、公式和概念链接的结构化笔记。

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) `zh` - 自动化每日论文推荐流程（抓取、评审、记笔记），用于跟进最新的 AI 研究。

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - 通过 Google 的 Gemini 研究智能体 API 执行多步骤的文献与技术调研，生成带引用的详细报告。

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - 通过浏览器自动化检索 Google Scholar，返回带引用次数和全文链接的结构化结果。

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - 根据论文草稿生成排序后的候选文献和相关工作小节摘要，在 Semantic Scholar、arXiv 和 OpenAlex 上用 LLM 辩论式排序，并沿引用图扩展。

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - 用 MinerU 的免费 Agent API 或基于令牌的 Standard API 把学术 PDF 解析成干净的 Markdown，并提取表格和公式。

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - 只在 Nature Portfolio、AAAS Science 和 Cell Press 的期刊中按日期筛选检索，为稿件正文添加引用，并导出单个文献管理器文件。

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - 把对一篇科学论文的深度阅读整理成固定 16 节、以证据为依据的研究卡片。

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - 在 Claude Code 中通过浏览器自动化查询 Google NotebookLM 笔记本，获得带引用、以来源为依据的回答。

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) `zh` - 通过六轮工作流把学术论文转成详细的 HTML 文章，包含代码检索、公式渲染和示意图。

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - 为技术研究开展专利现有技术检索、知识产权格局梳理和可专利性评估。

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) `zh` - 通过沁言学术 OpenAPI 检索文献，生成 GB/T 7714、IEEE、APA、MLA、Chicago、Harvard 和 Vancouver 格式的学术引用。

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - 按完整的 PRISMA 2020 清单（27 项）引导系统文献综述，产出期刊格式的 Word 稿件、带标注的 PRISMA 流程图和 APA 第 7 版参考文献，明确不包含元分析和统计合并。

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - 沿引用图向外扩展并独立检索草稿主题，找出草稿可能遗漏的相关工作，并按其对新颖性声明的威胁程度为每个候选评级。

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - 通过查询 CrossRef、PubMed、arXiv、Semantic Scholar 和 ChemRxiv，根据 DOI、PMID、arXiv ID 或论文标题生成 BibTeX 条目。

## 研究设计与方案

*在收集任何数据之前决定测什么、怎么测：研究方案、伦理审查、预注册、抽样、测量工具设计。*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - 通过分阶段的工作流为医疗器械或药物试验起草研究方案，并提供仅调研模式，可在起草前检索类似的已注册试验。

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - 规划联合分析调查实验，涵盖属性结构、随机化与正交性、功效计算和 AMCE/AMIE 估计。

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - 在收集数据前规划研究，涵盖随机化、区组、析因与交叉设计，以及整群或适应性设计。

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - 设计定性数据收集工具和方案：访谈提纲、焦点小组提纲、观察方案、田野笔记模板和抽样策略。

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - 撰写、修改和评估定性研究的 IRB 与伦理方案，涵盖 Common Rule 下豁免/快速/全委员会审查的判定、方案叙述和数据安全计划。

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - 在分析开始前审查医学研究的队列逻辑、对照选择和验证策略，找出数据泄漏和效度风险。

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - 计算统计功效、所需样本量和最小可检测效应，支持含整群的双臂 RCT、多臂设计以及非标准设计的模拟功效分析，并产出可直接用于注册的功效分析章节。

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - 按 OSF、AsPredicted 或 AEA RCT Registry 的格式起草结构化的预注册文档，涵盖假设、抽样计划、分析计划、排除标准和推断准则，并用 MUST/SHOULD/MAY 标注明确程度。

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - 检查计划、实验、数据集或论断是否仍与已冻结的研究问题和方案一致；发现偏离时拒绝悄悄改写作为依据的文档。

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - 依据已发表的社会科学方法论，起草和评审问卷的题目措辞、回答量表和问卷流程，以减少测量偏差。

## 方法形式化与理论

*把想法变成明确表述的方法：形式化论断、检查推导、撰写和验证证明。*

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - 对公式、估计量、恒等式或界至少独立重新推导两次，按数学等价性对结果聚类，并输出记录一致与离群情况的验证矩阵。

- [Formula Derivation](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/formula-derivation) - 把零散的公式和理论笔记整理成一条假设明确的连贯推导；笔记尚不足以支撑时，输出说明原因的阻塞报告。

- [Lean 4 Theorem Proving](https://github.com/cameronfreer/lean4-skills/tree/HEAD/plugins/lean4/skills/lean4) - 在 Lean 4 和 mathlib 中形式化并证明数学命题，包括检索 mathlib 已有引理、补全 `sorry`、检查公理和寻找反例；辅助脚本以及会话和 Bash hook 由外层插件提供，不在该 skill 目录内。

- [Numerical Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/numerical-check) - 在参数空间上随机扫描，为单调性、阈值、不等式或极限类命题寻找反例；未找到反例时只作为证据而非证明来报告。

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - 根据给定的结论及其假设，起草并补全定理、引理和命题的严格数学证明。

- [Symbolic Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/symbolic-check) - 用 SymPy 证明或推翻自己写的恒等式、导数、极限、比较静态符号或闭式解，并要求为每个符号明确声明定义域假设。

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - 逐步检查论文中的定理证明、代数推导和界，报告缺失的假设和缺少的归纳基础；当论文从未说明某个符号的定义域时，把该步骤标为未验证而不是判为错误。

## 数据与标注

*获取、标注、整理和审计研究所用的数据。*

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - 在 Hugging Face Hub、OpenML、GitHub 和论文交叉引用中检索符合研究任务的数据集，返回排序并去重的列表。

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - 在分析前对栅格、矢量、点和遥感数据集做质量检查，涵盖坐标参考系、基准面、网格对齐、分辨率、无数据值、几何有效性和空间连接基数。

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - 通过统一接口查询基因组和生物医学数据库，获取基因记录、序列、比对、AlphaFold 结构、表达和疾病关联，并固定工具版本以便查询可重复。

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - 在模型训练前分析数据集的偏差、分布和公平性。

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - 解析并规范化分子结构，然后计算描述符、指纹、子结构匹配、化学反应以及二维或三维坐标，用于化学信息学工作。

## 模型训练与微调

*训练和适配模型，从单 GPU 微调到分布式训练。*

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - 在 Hugging Face Jobs 上通过 TRL 或 Unsloth 微调语言模型和视觉语言模型，涵盖 SFT、DPO、GRPO 和奖励建模。

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - 在 Hugging Face Jobs 的云端 GPU 上训练和微调检测、分类以及 SAM/SAM2 分割模型。

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - 把 PyTorch 训练代码组织成 LightningModule 并配置 Trainer，支持多 GPU/TPU 扩展、分布式训练（DDP、FSDP、DeepSpeed）和日志集成（W&B、TensorBoard、MLflow）。

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - 用 Stable Baselines3 中可用于生产的 PPO、SAC、DQN、TD3、DDPG 和 A2C 实现，在 Gymnasium 环境上训练强化学习智能体。

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - 用 NVIDIA TAO Toolkit 优化过的训练与导出流程微调 Hugging Face 模型。

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - 为长时间运行的机器学习训练任务执行启动前检查清单，在启动前发现配置、路径和监控上的错误。

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - 为一个高吞吐强化学习库的环境、向量化、策略、训练、评估和检查点审查提供区分版本的指导。

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - 指导用 PyG 开发图神经网络，涵盖节点/链接/图分类、消息传递架构（GCN、GAT、GraphSAGE、GIN）、异构图和邻居采样。

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - 用 sentence-transformers 库训练双编码器、交叉编码器和 SPLADE 稀疏嵌入模型。

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - 通过 TRL 命令行界面微调 Transformer 语言模型，涵盖 SFT、DPO、GRPO、KTO、RLOO 和奖励建模。

## 示意图与框图

*架构图、流程图和概念图，即论文里画出来的插图，区别于由数据绘制的图表。*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - 强制学术论文配图走"独立 TikZ 文件编译成 PDF"的流程，禁止在论文源码中内联 TikZ，并要求每张图在插入前都能编译且经过目视检查。

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - 以机制为先规划通路图、信号图和图形摘要，再生成面向矢量或 300–600 DPI 印刷输出的图像模型提示词。

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - 根据论文的研究类型和机制选择合适的图结构（流程、架构、对比矩阵、消融矩阵或分类树），而不是机械套用固定模板。

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - 生成 .drawio XML 图并通过 draw.io 桌面版命令行导出 PNG/SVG/PDF/JPG，涵盖流程图、架构图、ER/UML 图、网络拓扑和 ML/DL 模型图（Transformer、CNN、LSTM）。

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - 把示意图、图表或架构图的参考图像重建为可编辑的 Draw.io 文件，优先保证与原图的视觉一致，其次才是可编辑性。

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - 根据自然语言描述生成 Mermaid 图并校验语法，支持流程图、时序图、类图、ER 图、甘特图等共 23 种类型。

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - 从一个包含可复制图标和可编辑模板的库中查找、编辑并验证 TikZ 图，涵盖神经网络架构、编码器-解码器图、训练流程和系统框图。

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - 根据论文的方法描述和图注生成可发表质量的学术示意图和流程图，由多智能体流程（Retriever、Planner、Stylist、Visualizer、Critic）协作完成，面向 NeurIPS、ICML、ACL 等会议。

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - 指导制作图形摘要、示意图、工作流可视化和架构图，同时涵盖编程绘图和设计工具两种做法。

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - 用 AI 图像模型绘制可发表质量的科学示意图并迭代改进，仅当独立的质量评审打分低于阈值时才重新生成，擅长神经网络架构、系统图、流程图和生物通路。

## 实验管理与可复现性

*运行实验、记录过程，并让别人能复现结果。*

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - 调研某一研究方向的论文，提取常用的基准、数据集、指标和评测协议；也可从单篇论文中提取。

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - 把 bulk RNA-seq 读段经质量控制、修剪、比对和定量处理成基因水平的计数矩阵，并在差异表达分析前检查实验设计和链特异性。

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - 为 CCF 会议或期刊论文设计证据包，涵盖数据集、基线、指标和消融实验。

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - 为 R 或生物信息学分析项目搭建 read/write/checkpoints 目录结构，把不可变输入、受版本控制的代码和不入库的输出分开。

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - 审计机器学习流程中的训练-测试污染、时间与空间泄漏、目标与代理变量泄漏、预处理泄漏和评测污染，并按严重程度对每项发现分级。

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) `zh` - 把机器学习实验日志总结为结构化的中文输出，区分证据与推测，并生成周报摘要。

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - 规范 Ansys、Abaqus、Nastran、OpenFOAM 和 COMSOL 中有限元与 CAE 分析结论的得出过程，强制进行理想化假设审查、基于 GCI 的网格无关性检验、验证与确认，以及人工签核关卡。

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - 在信任某个检查点之前，按项目约定核对一次 LibreYOLO 训练的配置、数据集和指标。

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - 为计算材料数据解析规范的 CMSO 和 ASMO 本体术语，在断言某个关系之前检查类层级以及属性的定义域和值域。

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) `zh` - 把照片、语音或文字形式的实验记录规范化为带 YAML frontmatter 的 Markdown，写入普通本地文件夹，可选接入 Obsidian 库和飞书。

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - 把 arXiv 论文转成带引用锚点的 Python 实现，为每个模块标注它实现的论文章节；遇到含糊之处会标出而不是猜测。

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - 扫描 AI 编程智能体的缓存目录，把其中的数值实验结果提取成结构化格式。

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - 比较机器学习训练运行时强制按相同 epoch 对齐，并把代理指标与下游目标分开。

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - 用"先取证再动手"的五步流程诊断失败的机器学习实验，涵盖进程状态、GPU、磁盘、日志和检查点。

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - 分七个阶段从一个 arXiv 链接走到可度量的复现运行，用公开替代方案处理缺失的代码、超参数和私有数据集。

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - 为随论文投稿公开研究代码做准备，涵盖仓库清理、依赖审计和可复现性清单。

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - 为 artifact evaluation 投稿打包研究代码和数据：README 与附录、双盲评审匿名化、ACM 徽章体系，以及 Zenodo 或 Software Heritage 的归档 DOI 指引，并对照会议当前规则检查。

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - 按 AEA 数据与代码可得性标准组装可直接提交的可复现材料，包括 README、数据集清单、计算环境要求、图表到脚本的对应表和保密数据存放计划。

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - 讲解在 Slurm 集群上开展多任务实验的方法：运行时长估算、任务与任务数组的划分、提交顺序，以及诊断没有产出或悄悄用错配置的运行。

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - 审计作者自己本地代码产出的指标是否仍在给定容差内与论文中的表格和论断一致，并把数值不符与复现失败分开报告。

## 统计分析

*选择并运行分析：回归、因果推断、调查加权、元分析、贝叶斯建模。*

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - 为实证经济学研究选择并压力测试因果识别策略，涵盖交错双重差分、弱工具变量稳健的工具变量法、断点回归、合成控制和 shift-share 设计。

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - 检测实证研究内容中的统计错误和方法论谬误，并按严重程度分级。

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - 在 Python 中分析复杂抽样调查数据，处理分层、初级抽样单元和权重，支持方差估计和调查加权 GLM，适用于 NHANES、CPS、DHS 等数据集。

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - 用 R 的 survey 包分析复杂抽样调查数据，涵盖设计对象、加权均值与总量、调查加权回归、子总体估计和重复权重（BRR、刀切法、自助法）。

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - 在 R 中估计高维固定效应模型，支持多维固定效应、工具变量估计、TWFE 与 Sun-Abraham 双重差分，以及聚类或异方差稳健标准误。

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - 选择统计检验、检查其前提假设、计算效应量，并按 APA 格式报告结果，涵盖 t 检验、方差分析、回归和贝叶斯替代方法。

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - 为诊断准确性、一致性、生存、倾向评分和调查加权分析生成可复现的 Python 或 R 代码，并在读取任何数据文件前检查是否含受保护的健康信息。

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - 运行从 PROSPERO 方案注册、偏倚风险评估到统计合并和符合 PRISMA 的报告的元分析流程。

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - 分析实验结果文件，运行显著性检验和模型比较，并起草带配图的 Results 部分。

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) `zh` - 运行从 PICO 到稿件骨架的网状元分析：执行检索、双模型筛选、数据提取、偏倚风险评估、R 中的频率学派与贝叶斯合并、GRADE 评级和 PRISMA-NMA 报告，含五个强制的人工决策关卡和审计日志。

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - 用 PyMC 构建、拟合和验证贝叶斯层次模型，涵盖 MCMC 采样、变分推断和后验预测检验。

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - 把 Stata 命令（reghdfe、xtreg、ivregress、margins、esttab、svy:）对应到 R 中的等价写法，供在两个生态之间迁移分析的研究者使用。

## 定性与混合方法

*访谈、田野调查和编码文本：主题分析、扎根理论、民族志、编码者间信度。*

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - 覆盖五种传统的定性研究设计与分析：主题分析、扎根理论、解释现象学分析、民族志和案例研究，并给出可信度标准。

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - 以已编码单元为依据，搭建并索引反思、比较、整合和决策备忘录，并把研究者的解释与机器审计日志分开保存。

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - 跟踪多维度的理论饱和，生成随研究阶段变化的方法论隔离规则，并把规则变更和人为覆盖记入反思日志。

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - 对定性数据编码并建立编码本，支持演绎、归纳和混合编码、编码频次、共现分析和编码者间信度。

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - 开展扎根理论、反思性主题分析和内容分析，包含编码本开发和编码者间信度检验，并可导出为 NVivo、ATLAS.ti、Dedoose 和 MAXQDA 格式。

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - 按 Braun 和 Clarke 的六阶段框架，把访谈、焦点小组或开放式回答编码成主题，涵盖四项前置分析决策和一份 15 条的质量清单。

## 可解释性

*打开训练好的模型看它在计算什么，并解释单个预测。*

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - 检查并操纵任意 PyTorch 模型的内部状态，包括通过 NDIF 对本地 GPU 放不下的大模型远程执行。

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - 通过声明式、基于字典的干预框架，在 PyTorch 模型上做因果追踪、激活修补和互换干预训练。

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - 训练并分析稀疏自编码器，把多义的模型激活分解为可解释特征，封装了 SAELens 和 TransformerLens 库。

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - 用基于博弈论的特征归因解释和审计机器学习预测，涵盖解释器与掩码器的选择、归因的计算与验证、多输出解释以及局部/全局可视化。

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - 通过挂在每个模型激活上的 hook 点检查注意力模式并运行激活修补实验，逆向分析 Transformer 实现的算法。

## 论文级绘图与可视化

*由结果绘制的图表，达到期刊或会议要求的水准。*

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - 为科研图表生成可运行的 Matplotlib/Seaborn/mermaid 代码，并附定量图与概念图的选择指南。

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - 按固定的统一风格生成可直接发表的 Matplotlib 图（柱状图、趋势图、散点图、热力图和多面板布局），并遵循 AI 会议和期刊投稿的印刷/矢量导出规范。

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - 校验表格中的经纬度数据并渲染可复现的 SVG 研究地点图，逐行应用公开、模糊化或受限的可见性策略并对坐标取整。

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - 用 Python 或 R 为高影响力期刊创建、修改和审查投稿级科研图，支持多面板和符合期刊要求的导出。

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - 规划并审查稿件的图组织，强制每张图只支撑一个论断、为各面板分配角色，并在撰写图注和结果正文前决定放正文还是补充材料。

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - 根据实验数据和大纲为学术论文生成可发表质量的图表和概念图，可选用视觉语言模型评审来迭代改进。

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - 在多个绘图库中落实 Edward Tufte 的数据可视化原则（数据墨水比、直接标注、范围框坐标轴），用于学术绘图。

## 写作与投稿

*起草稿件并使其达到可投稿状态：结构、格式、适配投稿要求、投出前的自查。*

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - 把论文转成幻灯片，并可选生成带旁白的演示视频，涵盖讲稿撰写、幻灯片生成、语音合成旁白和视频合成。

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - 为 CCF 评级的会议和期刊规划、起草、修改论文并适配投稿要求，同时保持用户自己的想法范围和证据不变。

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - 用作者确认过的本地内容制作可编辑的学术会议海报，并检查物理尺寸、打印限制、无障碍、素材来源和导出就绪情况。

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - 按中文学术排版惯例（如三线表、独立公式）创建和编辑 .docx 文件。

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - 把 50 多份写作指南中的经济学写作建议整合为可执行的规则，用于起草和修改经济学论文。

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - 指导学术科研经费申请书的结构设计、与资助方的匹配度评估和预算设计。

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - 通过分析参考语料并逐节修改，使学术稿件适配目标期刊的写作惯例。

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - 处理学术写作中 LaTeX 文档的创建、编译、格式转换和文档分析。

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) `zh` - 协助研究生完成中文 LaTeX 学位论文，涵盖编译诊断、GB/T 7714 参考文献格式、结构审查和盲审匿名化。

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - 在投稿或重投前做后期预检，把论断、图、图注、方法和补充材料与期刊要求交叉核对。

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) `zh` - 修复学术论文 LaTeX 源码中的浮动体位置问题：离首次引用太远、宽度不匹配、扎堆和孤页。

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) `zh` - 修复 LaTeX 溢出问题（overfull box、过长公式和 URL 溢出），先只做版式调整，版式无法解决时再升级为委托改写措辞。

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - 把原始研究材料转成结构化大纲，包含绘图计划、文献检索计划和章节计划，用于学术论文写作。

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - 通过数值准确性、术语一致性和公式-代码对应检查，对照代码和数据核实论文中的论断。

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - 把已发表论文中确认的错误归类为更正（corrigendum）、勘误（erratum）、关注声明或撤稿，然后起草给合作者的通知、给编辑的请求和公开声明。

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - 把已发表的论文转成通俗摘要、图形摘要构思和适配各平台的社交媒体文案，并确保每个版本都不超出论文结果实际支持的范围。

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - 指导修改 ML/CV/NLP 论文，包括段落级清晰度检查、反向大纲、主题句梳理和论断-证据对应审查。

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - 去除学术和研究文稿中常见的 AI 写作痕迹，恢复更自然的文风。

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) `zh` - 围绕一个研究主题撰写综述草稿，把多篇论文组织成以问题为驱动、体现方法演进的叙述，而不是逐篇摘要。

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - 协助处理已有的 Typst 稿件，涵盖编译、投稿格式、语法、参考文献和投稿就绪检查。

## 同行评审与答辩

*投稿的另一面：评审别人的稿件，以及回应对自己稿件的评审意见。*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - 模拟由五位领域专家组成的国际期刊审稿小组，给出结构化的编辑决定和修改路线图。

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - 从审稿人一侧对论文做一轮诚信取证：建立定位到原文片段的证据台账，分派跨模型审计器检查引用、实验、一致性和基线对比造假，再计算确定性结论供人工审稿人参考。

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - 按 CCF 或目标会议的标准，从新颖性、可靠性、证据、写作质量和格式合规几个方面审阅稿件，模拟审稿人与领域主席小组。

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - 为经济学论文生成审稿人水准的报告，检查识别策略、统计推断、表格、公式和参考文献，并输出问题台账和按优先级排列的修改计划。

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - 通过分诊、策略、起草和语气修复几种模式，把同行评审意见转化为以证据为依据的答辩材料。

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - 面向学术稿件的结构化审阅与修改工作流，提供六种按投入程度分级的运行模式。

## 这些条目是怎么检查的

这是一份策展列表，不是认证。每一条都是有人读过它的 `SKILL.md` 之后选入的。描述说明的是这个 skill 做什么，并不代表它已在你的问题上端到端运行过。没有任何条目声称做过可执行的端到端测试，因为确实没有做过。`SKILL.md` 不是英文的条目，名称旁带有语言标记。

**两级检查。** `static check`（96/142）表示已对照线上仓库核实路径、许可证、提交日期和所需能力，并读过 `SKILL.md`。`audited`（46/142）表示另外有人按书面审计规范，把 skill 自己的指令对着它附带的文件逐步走了一遍，结论为以下之一：`works`、`works with caveats`（能达到效果，但有一个需要事先知道的条件）、`unverifiable`（没有凭据、付费权限或硬件就无法评估）。审计已经移除过一些读起来不错、但除了作者本人谁也用不了的条目。

**许可证、star 数、能力标记和每条的检查状态都在机器可读的索引里，不在本页行内**：[`index.json`](index.json) 和 [`index.csv`](index.csv)，与本页由同一份数据生成。如果你在意某个 skill 的许可证、是否需要网络/凭据/hook，或它确切的审计结论，打开之前先在那里查。简单说：skill 自己 frontmatter 里的 `license:` 与仓库 LICENSE 不一致时，以前者为准；`repo ★N` 是那个*仓库*的 star 数，绝不是对该 skill 的评分。这些 skill 中有 94% 位于别人更大的仓库里，一个 2 万 star 的大仓库里的 skill 可能只提交过一次、从没人用过。

每一条背后的结构性检查（内容是否充实、是否模板批量生成、仓库是否核实得上）与学科无关，这也是本列表所保证的。至于某个临床试验、定性编码或计量经济学的 skill *在你的领域里方法上是否正确*，策展人无法对这里涉及的每个学科都做出判断。请把各学科的条目当作有待评估的线索，而不是经过领域专家把关的结论。

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。本列表由数据生成，请不要手工编辑任何 README。
