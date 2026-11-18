# Awesome Research Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/skills-154-blue?style=flat) [![Last Commit](https://img.shields.io/github/last-commit/neverbiasu/awesome-research-skills?style=flat)](https://github.com/neverbiasu/awesome-research-skills/commits/main)

[English](README.md) · [簡體中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

> 覆蓋學術研究各個階段的 Agent Skill，從文獻綜述到同行評審。

選題 → 文獻 → 研究設計 → 方法與理論 → 數據 → 訓練 → 示意圖 → 實驗 → 統計 → 定性 → 可解釋性 → 繪圖 → 寫作 → 同行評審

共 154 個 skill，逐個閱讀、逐個挑選。每一條都指向一個具體的 `SKILL.md` 目錄，而不是一個“裏面可能有點東西”的倉庫。收錄的是你自己動手做的那些步驟：查找已有工作、設計研究、把方法形式化、整理數據、跑實驗、統計分析、定性分析、作圖、寫作、同行評審。完整的自動科研流水線和 MLOps/部署工具不在收錄範圍內。

每一條都對照其倉庫讀過並覈對過（許可證、最近提交、運行所需的網絡/憑據/hook），不收模板批量生成或已無人維護的條目。其中 52 條還按一份書面規範逐步動手走過一遍。數據覈對至 2026-11-18；每條屬於 `static check` 還是 `audited: <結論>`，記錄在 `index.json` 中，定義見下文“這些條目是怎麼檢查的”。

條目名稱和鏈接與英文版一致；描述爲譯文，如有出入以[英文版](README.md)爲準。

## 目錄

- [方向探索與選題](#方向探索與選題)
- [文獻綜述](#文獻綜述)
- [研究設計與方案](#研究設計與方案)
- [方法形式化與理論](#方法形式化與理論)
- [數據與標註](#數據與標註)
- [模型訓練與微調](#模型訓練與微調)
- [示意圖與框圖](#示意圖與框圖)
- [實驗管理與可復現性](#實驗管理與可復現性)
- [統計分析](#統計分析)
- [定性與混合方法](#定性與混合方法)
- [可解釋性](#可解釋性)
- [論文級繪圖與可視化](#論文級繪圖與可視化)
- [寫作與投稿](#寫作與投稿)
- [同行評審與答辯](#同行評審與答辯)
- [這些條目是怎麼檢查的](#這些條目是怎麼檢查的)

## 方向探索與選題

*把模糊的興趣變成一個表述清楚、可以檢驗的研究問題。*

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - 引導從用戶提供的筆記和材料中生成可證僞、結構化的研究假設。

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - 在進入新問題領域或重新考慮項目方向時，運用結構化的構思框架找出研究方向。

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - 通過 5W1H 頭腦風暴、系統文獻綜述、多維度缺口分析和 SMART 研究問題表述，爲研究項目的啓動提供結構。

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - 把認知科學中的創造力技巧（組合創造、類比推理和約束操縱）用於生成研究方向。

- [Hypothesis Generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/hypothesis-generation) - 將觀察結果轉化爲可測試的研究計劃，通過撰寫競爭性解釋、區分性預測以及可直接用於預註冊的分析來實現，並附帶標準庫腳本，無需網絡或憑證。

- [Idea Generation](https://github.com/muye1112/skill/tree/HEAD/skills/idea-generation) - 生成多個候選研究想法，通過最多五輪自我批評進行精煉，並使用附帶腳本在 Semantic Scholar 上檢查新穎性，同時評估趣味性、可行性和新穎性。

- [Literature Weakness Scanner](https://github.com/flonat/flonat-research/tree/HEAD/skills/weakness-scanner) - 掃描文獻語料中反覆出現的薄弱論點、未支撐的假設和被反駁的發現以定位貢獻缺口，矛盾檢查步驟依賴可選的外部搜索 CLI。

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) `zh` - 分析文獻和早期想法，找出有依據的研究缺口和可檢驗的切入點，不強行聲稱新穎性。

- [Scientific Brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-brainstorming) - 將構思與證據評估及驗證分離，採用獨立生成、顯式假設、對抗性審查和決策日誌，並將所有輸出視爲提案而非發現。

## 文獻綜述

*查找、閱讀和綜合已有工作，並保證引用準確。*

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - 按關鍵詞、作者、日期範圍或學科類別檢索 bioRxiv 預印本元數據並獲取 PDF。

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - 監控 arXiv、OpenReview 和會議更新中與給定研究想法重疊的論文，給出可執行的放心/調研/跟進信號。

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - 通過 Chrome DevTools 瀏覽器自動化檢索中國知網（CNKI）並提取文獻元數據。

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - 圍繞一個引導問題，用論斷-來源臺賬和綜合矩陣構建發展理論的文獻綜述，並阻止逐篇羅列式總結和沒有依據的研究缺口聲明。

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) `zh` - 閱讀並分析來自 PDF、arXiv 或 Zotero 的學術論文，生成包含圖表、公式和概念鏈接的結構化筆記。

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) `zh` - 自動化每日論文推薦流程（抓取、評審、記筆記），用於跟進最新的 AI 研究。

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - 通過 Google 的 Gemini 研究智能體 API 執行多步驟的文獻與技術調研，生成帶引用的詳細報告。

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - 通過瀏覽器自動化檢索 Google Scholar，返回帶引用次數和全文鏈接的結構化結果。

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - 根據論文草稿生成排序後的候選文獻和相關工作小節摘要，在 Semantic Scholar、arXiv 和 OpenAlex 上用 LLM 辯論式排序，並沿引用圖擴展。

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - 用 MinerU 的免費 Agent API 或基於令牌的 Standard API 把學術 PDF 解析成乾淨的 Markdown，並提取表格和公式。

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - 只在 Nature Portfolio、AAAS Science 和 Cell Press 的期刊中按日期篩選檢索，爲稿件正文添加引用，並導出單個文獻管理器文件。

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - 把對一篇科學論文的深度閱讀整理成固定 16 節、以證據爲依據的研究卡片。

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - 在 Claude Code 中通過瀏覽器自動化查詢 Google NotebookLM 筆記本，獲得帶引用、以來源爲依據的回答。

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) `zh` - 通過六輪工作流把學術論文轉成詳細的 HTML 文章，包含代碼檢索、公式渲染和示意圖。

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - 爲技術研究開展專利現有技術檢索、知識產權格局梳理和可專利性評估。

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言學術skills/qinyan-citation) `zh` - 通過沁言學術 OpenAPI 檢索文獻，生成 GB/T 7714、IEEE、APA、MLA、Chicago、Harvard 和 Vancouver 格式的學術引用。

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - 按完整的 PRISMA 2020 清單（27 項）引導系統文獻綜述，產出期刊格式的 Word 稿件、帶標註的 PRISMA 流程圖和 APA 第 7 版參考文獻，明確不包含元分析和統計合併。

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - 沿引用圖向外擴展並獨立檢索草稿主題，找出草稿可能遺漏的相關工作，並按其對新穎性聲明的威脅程度爲每個候選評級。

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - 通過查詢 CrossRef、PubMed、arXiv、Semantic Scholar 和 ChemRxiv，根據 DOI、PMID、arXiv ID 或論文標題生成 BibTeX 條目。

## 研究設計與方案

*在收集任何數據之前決定測什麼、怎麼測：研究方案、倫理審查、預註冊、抽樣、測量工具設計。*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - 通過分階段的工作流爲醫療器械或藥物試驗起草研究方案，並提供僅調研模式，可在起草前檢索類似的已註冊試驗。

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - 規劃聯合分析調查實驗，涵蓋屬性結構、隨機化與正交性、功效計算和 AMCE/AMIE 估計。

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - 在收集數據前規劃研究，涵蓋隨機化、區組、析因與交叉設計，以及整羣或適應性設計。

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - 設計定性數據收集工具和方案：訪談提綱、焦點小組提綱、觀察方案、田野筆記模板和抽樣策略。

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - 撰寫、修改和評估定性研究的 IRB 與倫理方案，涵蓋 Common Rule 下豁免/快速/全委員會審查的判定、方案敘述和數據安全計劃。

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - 在分析開始前審查醫學研究的隊列邏輯、對照選擇和驗證策略，找出數據泄漏和效度風險。

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - 計算統計功效、所需樣本量和最小可檢測效應，支持含整羣的雙臂 RCT、多臂設計以及非標準設計的模擬功效分析，併產出可直接用於註冊的功效分析章節。

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - 按 OSF、AsPredicted 或 AEA RCT Registry 的格式起草結構化的預註冊文檔，涵蓋假設、抽樣計劃、分析計劃、排除標準和推斷準則，並用 MUST/SHOULD/MAY 標註明確程度。

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - 檢查計劃、實驗、數據集或論斷是否仍與已凍結的研究問題和方案一致；發現偏離時拒絕悄悄改寫作爲依據的文檔。

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - 依據已發表的社會科學方法論，起草和評審問卷的題目措辭、回答量表和問卷流程，以減少測量偏差。

## 方法形式化與理論

*把想法變成明確表述的方法：形式化論斷、檢查推導、撰寫和驗證證明。*

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - 對公式、估計量、恆等式或界至少獨立重新推導兩次，按數學等價性對結果聚類，並輸出記錄一致與離羣情況的驗證矩陣。

- [Formula Derivation](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/formula-derivation) - 把零散的公式和理論筆記整理成一條假設明確的連貫推導；筆記尚不足以支撐時，輸出說明原因的阻塞報告。

- [Lean 4 Theorem Proving](https://github.com/cameronfreer/lean4-skills/tree/HEAD/plugins/lean4/skills/lean4) - 在 Lean 4 和 mathlib 中形式化並證明數學命題，包括檢索 mathlib 已有引理、補全 `sorry`、檢查公理和尋找反例；輔助腳本以及會話和 Bash hook 由外層插件提供，不在該 skill 目錄內。

- [Numerical Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/numerical-check) - 在參數空間上隨機掃描，爲單調性、閾值、不等式或極限類命題尋找反例；未找到反例時只作爲證據而非證明來報告。

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - 根據給定的結論及其假設，起草並補全定理、引理和命題的嚴格數學證明。

- [Symbolic Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/symbolic-check) - 用 SymPy 證明或推翻自己寫的恆等式、導數、極限、比較靜態符號或閉式解，並要求爲每個符號明確聲明定義域假設。

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - 逐步檢查論文中的定理證明、代數推導和界，報告缺失的假設和缺少的歸納基礎；當論文從未說明某個符號的定義域時，把該步驟標爲未驗證而不是判爲錯誤。

## 數據與標註

*獲取、標註、整理和審計研究所用的數據。*

- [Dataset Codebook Generator](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/generate-codebook) - 將表格數據集的每個變量整理成 Markdown 和 JSON 格式的編碼手冊（codebook），列出含義未知的編碼值供字典查找，而非猜測其標籤。

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - 在 Hugging Face Hub、OpenML、GitHub 和論文交叉引用中檢索符合研究任務的數據集，返回排序並去重的列表。

- [Dataset Version Manifest](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/version-dataset) - 構建數據集的確定性內容哈希清單，並在後續副本中對照該清單進行驗證，報告發生漂移時的確切文件與列。

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - 在分析前對柵格、矢量、點和遙感數據集做質量檢查，涵蓋座標參考系、基準面、網格對齊、分辨率、無數據值、幾何有效性和空間連接基數。

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - 通過統一接口查詢基因組和生物醫學數據庫，獲取基因記錄、序列、比對、AlphaFold 結構、表達和疾病關聯，並固定工具版本以便查詢可重複。

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - 在模型訓練前分析數據集的偏差、分佈和公平性。

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - 解析並規範化分子結構，然後計算描述符、指紋、子結構匹配、化學反應以及二維或三維座標，用於化學信息學工作。

## 模型訓練與微調

*訓練和適配模型，從單 GPU 微調到分佈式訓練。*

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - 在 Hugging Face Jobs 上通過 TRL 或 Unsloth 微調語言模型和視覺語言模型，涵蓋 SFT、DPO、GRPO 和獎勵建模。

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - 在 Hugging Face Jobs 的雲端 GPU 上訓練和微調檢測、分類以及 SAM/SAM2 分割模型。

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - 把 PyTorch 訓練代碼組織成 LightningModule 並配置 Trainer，支持多 GPU/TPU 擴展、分佈式訓練（DDP、FSDP、DeepSpeed）和日誌集成（W&B、TensorBoard、MLflow）。

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - 用 Stable Baselines3 中可用於生產的 PPO、SAC、DQN、TD3、DDPG 和 A2C 實現，在 Gymnasium 環境上訓練強化學習智能體。

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - 用 NVIDIA TAO Toolkit 優化過的訓練與導出流程微調 Hugging Face 模型。

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - 爲長時間運行的機器學習訓練任務執行啓動前檢查清單，在啓動前發現配置、路徑和監控上的錯誤。

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - 爲一個高吞吐強化學習庫的環境、向量化、策略、訓練、評估和檢查點審查提供區分版本的指導。

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - 指導用 PyG 開發圖神經網絡，涵蓋節點/鏈接/圖分類、消息傳遞架構（GCN、GAT、GraphSAGE、GIN）、異構圖和鄰居採樣。

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - 用 sentence-transformers 庫訓練雙編碼器、交叉編碼器和 SPLADE 稀疏嵌入模型。

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - 通過 TRL 命令行界面微調 Transformer 語言模型，涵蓋 SFT、DPO、GRPO、KTO、RLOO 和獎勵建模。

## 示意圖與框圖

*架構圖、流程圖和概念圖，即論文裏畫出來的插圖，區別於由數據繪製的圖表。*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - 強制學術論文配圖走"獨立 TikZ 文件編譯成 PDF"的流程，禁止在論文源碼中內聯 TikZ，並要求每張圖在插入前都能編譯且經過目視檢查。

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - 以機制爲先規劃通路圖、信號圖和圖形摘要，再生成面向矢量或 300–600 DPI 印刷輸出的圖像模型提示詞。

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - 根據論文的研究類型和機制選擇合適的圖結構（流程、架構、對比矩陣、消融矩陣或分類樹），而不是機械套用固定模板。

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - 生成 .drawio XML 圖並通過 draw.io 桌面版命令行導出 PNG/SVG/PDF/JPG，涵蓋流程圖、架構圖、ER/UML 圖、網絡拓撲和 ML/DL 模型圖（Transformer、CNN、LSTM）。

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - 把示意圖、圖表或架構圖的參考圖像重建爲可編輯的 Draw.io 文件，優先保證與原圖的視覺一致，其次纔是可編輯性。

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - 根據自然語言描述生成 Mermaid 圖並校驗語法，支持流程圖、時序圖、類圖、ER 圖、甘特圖等共 23 種類型。

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - 從一個包含可複製圖標和可編輯模板的庫中查找、編輯並驗證 TikZ 圖，涵蓋神經網絡架構、編碼器-解碼器圖、訓練流程和系統框圖。

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - 根據論文的方法描述和圖注生成可發表質量的學術示意圖和流程圖，由多智能體流程（Retriever、Planner、Stylist、Visualizer、Critic）協作完成，面向 NeurIPS、ICML、ACL 等會議。

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - 指導製作圖形摘要、示意圖、工作流可視化和架構圖，同時涵蓋編程繪圖和設計工具兩種做法。

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - 用 AI 圖像模型繪製可發表質量的科學示意圖並迭代改進，僅當獨立的質量評審打分低於閾值時才重新生成，擅長神經網絡架構、系統圖、流程圖和生物通路。

## 實驗管理與可復現性

*運行實驗、記錄過程，並讓別人能復現結果。*

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - 調研某一研究方向的論文，提取常用的基準、數據集、指標和評測協議；也可從單篇論文中提取。

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - 把 bulk RNA-seq 讀段經質量控制、修剪、比對和定量處理成基因水平的計數矩陣，並在差異表達分析前檢查實驗設計和鏈特異性。

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - 爲 CCF 會議或期刊論文設計證據包，涵蓋數據集、基線、指標和消融實驗。

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - 爲 R 或生物信息學分析項目搭建 read/write/checkpoints 目錄結構，把不可變輸入、受版本控制的代碼和不入庫的輸出分開。

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - 審計機器學習流程中的訓練-測試污染、時間與空間泄漏、目標與代理變量泄漏、預處理泄漏和評測污染，並按嚴重程度對每項發現分級。

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) `zh` - 把機器學習實驗日誌總結爲結構化的中文輸出，區分證據與推測，並生成周報摘要。

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - 規範 Ansys、Abaqus、Nastran、OpenFOAM 和 COMSOL 中有限元與 CAE 分析結論的得出過程，強制進行理想化假設審查、基於 GCI 的網格無關性檢驗、驗證與確認，以及人工籤核關卡。

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - 在信任某個檢查點之前，按項目約定覈對一次 LibreYOLO 訓練的配置、數據集和指標。

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - 爲計算材料數據解析規範的 CMSO 和 ASMO 本體術語，在斷言某個關係之前檢查類層級以及屬性的定義域和值域。

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) `zh` - 把照片、語音或文字形式的實驗記錄規範化爲帶 YAML frontmatter 的 Markdown，寫入普通本地文件夾，可選接入 Obsidian 庫和飛書。

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - 把 arXiv 論文轉成帶引用錨點的 Python 實現，爲每個模塊標註它實現的論文章節；遇到含糊之處會標出而不是猜測。

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - 掃描 AI 編程智能體的緩存目錄，把其中的數值實驗結果提取成結構化格式。

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - 比較機器學習訓練運行時強制按相同 epoch 對齊，並把代理指標與下游目標分開。

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - 用"先取證再動手"的五步流程診斷失敗的機器學習實驗，涵蓋進程狀態、GPU、磁盤、日誌和檢查點。

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - 分七個階段從一個 arXiv 鏈接走到可度量的復現運行，用公開替代方案處理缺失的代碼、超參數和私有數據集。

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - 爲 artifact evaluation 投稿打包研究代碼和數據：README 與附錄、雙盲評審匿名化、ACM 徽章體系，以及 Zenodo 或 Software Heritage 的歸檔 DOI 指引，並對照會議當前規則檢查。

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - 按 AEA 數據與代碼可得性標準組裝可直接提交的可復現材料，包括 README、數據集清單、計算環境要求、圖表到腳本的對應表和保密數據存放計劃。

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - 講解在 Slurm 集羣上開展多任務實驗的方法：運行時長估算、任務與任務數組的劃分、提交順序，以及診斷沒有產出或悄悄用錯配置的運行。

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - 審計作者自己本地代碼產出的指標是否仍在給定容差內與論文中的表格和論斷一致，並把數值不符與復現失敗分開報告。

## 統計分析

*選擇並運行分析：迴歸、因果推斷、調查加權、元分析、貝葉斯建模。*

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - 爲實證經濟學研究選擇並壓力測試因果識別策略，涵蓋交錯雙重差分、弱工具變量穩健的工具變量法、斷點回歸、合成控制和 shift-share 設計。

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - 檢測實證研究內容中的統計錯誤和方法論謬誤，並按嚴重程度分級。

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - 在 Python 中分析複雜抽樣調查數據，處理分層、初級抽樣單元和權重，支持方差估計和調查加權 GLM，適用於 NHANES、CPS、DHS 等數據集。

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - 用 R 的 survey 包分析複雜抽樣調查數據，涵蓋設計對象、加權均值與總量、調查加權迴歸、子總體估計和重複權重（BRR、刀切法、自助法）。

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - 在 R 中估計高維固定效應模型，支持多維固定效應、工具變量估計、TWFE 與 Sun-Abraham 雙重差分，以及聚類或異方差穩健標準誤。

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - 選擇統計檢驗、檢查其前提假設、計算效應量，並按 APA 格式報告結果，涵蓋 t 檢驗、方差分析、迴歸和貝葉斯替代方法。

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - 爲診斷準確性、一致性、生存、傾向評分和調查加權分析生成可復現的 Python 或 R 代碼，並在讀取任何數據文件前檢查是否含受保護的健康信息。

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - 運行從 PROSPERO 方案註冊、偏倚風險評估到統計合併和符合 PRISMA 的報告的元分析流程。

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - 分析實驗結果文件，運行顯著性檢驗和模型比較，並起草帶配圖的 Results 部分。

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) `zh` - 運行從 PICO 到稿件骨架的網狀元分析：執行檢索、雙模型篩選、數據提取、偏倚風險評估、R 中的頻率學派與貝葉斯合併、GRADE 評級和 PRISMA-NMA 報告，含五個強制的人工決策關卡和審計日誌。

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - 用 PyMC 構建、擬合和驗證貝葉斯層次模型，涵蓋 MCMC 採樣、變分推斷和後驗預測檢驗。

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - 把 Stata 命令（reghdfe、xtreg、ivregress、margins、esttab、svy:）對應到 R 中的等價寫法，供在兩個生態之間遷移分析的研究者使用。

## 定性與混合方法

*訪談、田野調查和編碼文本：主題分析、紮根理論、民族誌、編碼者間信度。*

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - 覆蓋五種傳統的定性研究設計與分析：主題分析、紮根理論、解釋現象學分析、民族誌和案例研究，並給出可信度標準。

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - 以已編碼單元爲依據，搭建並索引反思、比較、整合和決策備忘錄，並把研究者的解釋與機器審計日誌分開保存。

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - 跟蹤多維度的理論飽和，生成隨研究階段變化的方法論隔離規則，並把規則變更和人爲覆蓋記入反思日誌。

- [Mixed Methods Instrument Design](https://github.com/Lambenthan/mixed-methods-instrument-design) `zh` - 設計調查問卷和訪談提綱，並通過經驗證的“研究問題至題項”映射矩陣實現兩者的對齊。

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - 對定性數據編碼並建立編碼本，支持演繹、歸納和混合編碼、編碼頻次、共現分析和編碼者間信度。

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - 開展紮根理論、反思性主題分析和內容分析，包含編碼本開發和編碼者間信度檢驗，並可導出爲 NVivo、ATLAS.ti、Dedoose 和 MAXQDA 格式。

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - 按 Braun 和 Clarke 的六階段框架，把訪談、焦點小組或開放式回答編碼成主題，涵蓋四項前置分析決策和一份 15 條的質量清單。

## 可解釋性

*打開訓練好的模型看它在計算什麼，並解釋單個預測。*

- [Interp CLI](https://github.com/azrabano23/interp) - 通過捆綁的 CLI 在 GPT-2 級別模型上運行 logit lens、直接 logit 歸因、激活補丁、歸納頭檢查、SAE 特徵查找和 steering，其測試固定了已發佈的電路結果。

- [Mechanism Skills](https://github.com/zjunlp/Mechanist/tree/HEAD/skills/mechanism-skills) - 根據每種方法使用的信號將機制問題路由到十一種方法族之一，然後在執行任何操作前要求閱讀該方法族及其子方法的文件，並按方法族說明成本、優勢和侷限性。

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - 檢查並操縱任意 PyTorch 模型的內部狀態，包括通過 NDIF 對本地 GPU 放不下的大模型遠程執行。

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - 通過聲明式、基於字典的干預框架，在 PyTorch 模型上做因果追蹤、激活修補和互換干預訓練。

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - 訓練並分析稀疏自編碼器，把多義的模型激活分解爲可解釋特徵，封裝了 SAELens 和 TransformerLens 庫。

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - 用基於博弈論的特徵歸因解釋和審計機器學習預測，涵蓋解釋器與掩碼器的選擇、歸因的計算與驗證、多輸出解釋以及局部/全局可視化。

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - 通過掛在每個模型激活上的 hook 點檢查注意力模式並運行激活修補實驗，逆向分析 Transformer 實現的算法。

## 論文級繪圖與可視化

*由結果繪製的圖表，達到期刊或會議要求的水準。*

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - 爲科研圖表生成可運行的 Matplotlib/Seaborn/mermaid 代碼，並附定量圖與概念圖的選擇指南。

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - 按固定的統一風格生成可直接發表的 Matplotlib 圖（柱狀圖、趨勢圖、散點圖、熱力圖和多面板佈局），並遵循 AI 會議和期刊投稿的印刷/矢量導出規範。

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - 校驗表格中的經緯度數據並渲染可復現的 SVG 研究地點圖，逐行應用公開、模糊化或受限的可見性策略並對座標取整。

- [mpltweak](https://github.com/shdbl/mpltweak/tree/HEAD/skills/mpltweak) - 通過拖拽（類似 PowerPoint 幻燈片風格）調整 matplotlib 子圖佈局，並在用戶確認後僅將具體數值寫回用戶的腳本。

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - 用 Python 或 R 爲高影響力期刊創建、修改和審查投稿級科研圖，支持多面板和符合期刊要求的導出。

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - 規劃並審查稿件的圖組織，強制每張圖只支撐一個論斷、爲各面板分配角色，並在撰寫圖注和結果正文前決定放正文還是補充材料。

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - 根據實驗數據和大綱爲學術論文生成可發表質量的圖表和概念圖，可選用視覺語言模型評審來迭代改進。

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - 在多個繪圖庫中落實 Edward Tufte 的數據可視化原則（數據墨水比、直接標註、範圍框座標軸），用於學術繪圖。

## 寫作與投稿

*起草稿件並使其達到可投稿狀態：結構、格式、適配投稿要求、投出前的自查。*

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - 把論文轉成幻燈片，並可選生成帶旁白的演示視頻，涵蓋講稿撰寫、幻燈片生成、語音合成旁白和視頻合成。

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - 爲 CCF 評級的會議和期刊規劃、起草、修改論文並適配投稿要求，同時保持用戶自己的想法範圍和證據不變。

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - 用作者確認過的本地內容製作可編輯的學術會議海報，並檢查物理尺寸、打印限制、無障礙、素材來源和導出就緒情況。

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - 按中文學術排版慣例（如三線表、獨立公式）創建和編輯 .docx 文件。

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - 把 50 多份寫作指南中的經濟學寫作建議整合爲可執行的規則，用於起草和修改經濟學論文。

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - 指導學術科研經費申請書的結構設計、與資助方的匹配度評估和預算設計。

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - 通過分析參考語料並逐節修改，使學術稿件適配目標期刊的寫作慣例。

- [JP Essay Scientific](https://github.com/lucasbabur/jp-essay/tree/HEAD/scientific) - 在 Claude Code 中研究、起草和修改帶引用的學術論文，在修改過程中保留來源鏈接的論斷，並生成文內引用和參考文獻列表。

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - 處理學術寫作中 LaTeX 文檔的創建、編譯、格式轉換和文檔分析。

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) `zh` - 協助研究生完成中文 LaTeX 學位論文，涵蓋編譯診斷、GB/T 7714 參考文獻格式、結構審查和盲審匿名化。

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - 在投稿或重投前做後期預檢，把論斷、圖、圖注、方法和補充材料與期刊要求交叉覈對。

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) `zh` - 修復學術論文 LaTeX 源碼中的浮動體位置問題：離首次引用太遠、寬度不匹配、扎堆和孤頁。

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) `zh` - 修復 LaTeX 溢出問題（overfull box、過長公式和 URL 溢出），先只做版式調整，版式無法解決時再升級爲委託改寫措辭。

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - 把原始研究材料轉成結構化大綱，包含繪圖計劃、文獻檢索計劃和章節計劃，用於學術論文寫作。

- [PhD Skills: Paper Check](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-check) - 在提交前對照代碼、結果和引用檢查論文，涵蓋數值、術語、公式與代碼一致性以及 BibTeX，併爲代碼開源發佈做準備。

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - 把已發表論文中確認的錯誤歸類爲更正（corrigendum）、勘誤（erratum）、關注聲明或撤稿，然後起草給合作者的通知、給編輯的請求和公開聲明。

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - 把已發表的論文轉成通俗摘要、圖形摘要構思和適配各平臺的社交媒體文案，並確保每個版本都不超出論文結果實際支持的範圍。

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - 指導修改 ML/CV/NLP 論文，包括段落級清晰度檢查、反向大綱、主題句梳理和論斷-證據對應審查。

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - 去除學術和研究文稿中常見的 AI 寫作痕跡，恢復更自然的文風。

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) `zh` - 圍繞一個研究主題撰寫綜述草稿，把多篇論文組織成以問題爲驅動、體現方法演進的敘述，而不是逐篇摘要。

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - 協助處理已有的 Typst 稿件，涵蓋編譯、投稿格式、語法、參考文獻和投稿就緒檢查。

## 同行評審與答辯

*投稿的另一面：評審別人的稿件，以及回應對自己稿件的評審意見。*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - 模擬由五位領域專家組成的國際期刊審稿小組，給出結構化的編輯決定和修改路線圖。

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - 從審稿人一側對論文做一輪誠信取證：建立定位到原文片段的證據臺賬，分派跨模型審計器檢查引用、實驗、一致性和基線對比造假，再計算確定性結論供人工審稿人蔘考。

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - 按 CCF 或目標會議的標準，從新穎性、可靠性、證據、寫作質量和格式合規幾個方面審閱稿件，模擬審稿人與領域主席小組。

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - 爲經濟學論文生成審稿人水準的報告，檢查識別策略、統計推斷、表格、公式和參考文獻，並輸出問題臺賬和按優先級排列的修改計劃。

- [Medical Manuscript Peer Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/peer-review) - 按期刊格式爲他人稿件起草結構化的審稿報告，通過腳本化門禁將建議與面向作者的評註隔離。

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - 通過分診、策略、起草和語氣修復幾種模式，把同行評審意見轉化爲以證據爲依據的答辯材料。

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - 面向學術稿件的結構化審閱與修改工作流，提供六種按投入程度分級的運行模式。

- [Rebuttal Skill](https://github.com/TobiasLee/Rebuttal-Skill) - 在覈查會議/期刊的生成式 AI 政策後，分類梳理審稿意見、按優先級規劃反駁實驗，並準備回覆材料，對缺失證據保留佔位符。

## 這些條目是怎麼檢查的

這是一份策展列表，不是認證。每一條都是有人讀過它的 `SKILL.md` 之後選入的。描述說明的是這個 skill 做什麼，並不代表它已在你的問題上端到端運行過。沒有任何條目聲稱做過可執行的端到端測試，因爲確實沒有做過。`SKILL.md` 不是英文的條目，名稱旁帶有語言標記。

**兩級檢查。** `static check`（102/154）表示已對照線上倉庫覈實路徑、許可證、提交日期和所需能力，並讀過 `SKILL.md`。`audited`（52/154）表示另外有人按書面審計規範，把 skill 自己的指令對着它附帶的文件逐步走了一遍，結論爲以下之一：`works`、`works with caveats`（能達到效果，但有一個需要事先知道的條件）、`unverifiable`（沒有憑據、付費權限或硬件就無法評估）。審計已經移除過一些讀起來不錯、但除了作者本人誰也用不了的條目。

**許可證、star 數、能力標記和每條的檢查狀態都在機器可讀的索引裏，不在本頁行內**：[`index.json`](index.json) 和 [`index.csv`](index.csv)，與本頁由同一份數據生成。如果你在意某個 skill 的許可證、是否需要網絡/憑據/hook，或它確切的審計結論，打開之前先在那裏查。簡單說：skill 自己 frontmatter 裏的 `license:` 與倉庫 LICENSE 不一致時，以前者爲準；`repo ★N` 是那個*倉庫*的 star 數，絕不是對該 skill 的評分。這些 skill 中有 92% 位於別人更大的倉庫裏，一個 2 萬 star 的大倉庫裏的 skill 可能只提交過一次、從沒人用過。

每一條背後的結構性檢查（內容是否充實、是否模板批量生成、倉庫是否覈實得上）與學科無關，這也是本列表所保證的。至於某個臨牀試驗、定性編碼或計量經濟學的 skill *在你的領域裏方法上是否正確*，策展人無法對這裏涉及的每個學科都做出判斷。請把各學科的條目當作有待評估的線索，而不是經過領域專家把關的結論。

## 參與貢獻

見 [CONTRIBUTING.md](CONTRIBUTING.md)。翻譯版 README 由英文版生成，請不要手工編輯。
