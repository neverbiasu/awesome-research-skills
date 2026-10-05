# Awesome Research Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/skills-142-blue?style=flat) [![Last Commit](https://img.shields.io/github/last-commit/neverbiasu/awesome-research-skills?style=flat)](https://github.com/neverbiasu/awesome-research-skills/commits/main)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · 한국어

> 연구자를 위한 Agent Skill 142개를 하나씩 읽고 골랐습니다. 모든 항목은 '쓸 만한 것이 들어 있을지도 모르는 저장소'가 아니라, 특정한 `SKILL.md` 디렉터리 하나를 가리킵니다.

연구자가 직접 수행하는 단계를 대상으로 합니다. 선행 연구 찾기, 연구 설계, 방법의 형식화, 데이터 정리, 실험 수행, 통계 분석, 질적 분석, 그림 작성, 글쓰기, 동료 심사를 다룹니다. 연구 전체를 자동으로 돌리는 파이프라인과 MLOps·배포 도구는 범위에 포함하지 않습니다.

모든 항목은 해당 저장소와 대조하여 읽고, 라이선스, 마지막 커밋, 실행에 필요한 것(네트워크, 자격 증명, 훅)을 확인했습니다. 템플릿으로 찍어낸 항목이나 방치된 항목은 싣지 않습니다. 그중 46개는 문서화된 명세에 따라 사람이 직접 절차를 따라가며 점검했습니다. 데이터는 2026-10-05 기준으로 GitHub와 대조했습니다. 각 항목이 `static check`인지 `audited: <판정>`인지는 `index.json`에 기록되어 있으며, 정의는 아래 '항목을 확인하는 방법'에 있습니다.

항목 이름과 링크는 영문판과 같습니다. 설명은 번역이며, 내용이 다를 경우 [영문판](README.md)을 기준으로 합니다.

## 목차

- [연구 방향 탐색과 아이디어 구상](#연구-방향-탐색과-아이디어-구상)
- [문헌 검토](#문헌-검토)
- [연구 설계와 프로토콜](#연구-설계와-프로토콜)
- [방법의 형식화와 이론](#방법의-형식화와-이론)
- [데이터와 어노테이션](#데이터와-어노테이션)
- [모델 학습과 미세조정](#모델-학습과-미세조정)
- [다이어그램과 도식](#다이어그램과-도식)
- [실험 관리와 재현성](#실험-관리와-재현성)
- [통계 분석](#통계-분석)
- [질적 연구와 혼합 방법](#질적-연구와-혼합-방법)
- [해석 가능성](#해석-가능성)
- [논문 수준의 플로팅과 시각화](#논문-수준의-플로팅과-시각화)
- [글쓰기와 투고](#글쓰기와-투고)
- [동료 심사와 반박](#동료-심사와-반박)
- [항목을 확인하는 방법](#항목을-확인하는-방법)

## 연구 방향 탐색과 아이디어 구상

*막연한 관심을 정식화된, 검증 가능한 연구 질문으로 바꿉니다.*

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - 사용자가 제공한 메모와 자료로부터 반증 가능하고 구조화된 연구 가설을 만들도록 안내합니다.

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - 새로운 문제 영역에 들어서거나 프로젝트 방향을 다시 생각할 때, 구조화된 발상 틀을 적용하여 연구 방향을 찾아냅니다.

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - 5W1H 브레인스토밍, 체계적 문헌 검토, 다차원 공백 분석, SMART 연구 질문 정식화를 통해 연구 프로젝트의 시작 단계를 구조화합니다.

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - 조합적 창의성, 유추적 추론, 제약 조작 같은 인지과학의 창의성 기법을 연구 방향을 떠올리는 데 적용합니다.

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) `zh` - 문헌과 초기 아이디어를 분석하여 근거 있는 연구 공백과 검증 가능한 진입점을 찾습니다. 참신성 주장을 억지로 만들지 않습니다.

## 문헌 검토

*선행 연구를 찾고, 읽고, 종합하며, 인용을 정확하게 유지합니다.*

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - 키워드, 저자, 기간, 주제 분류로 bioRxiv 프리프린트 메타데이터를 검색하고 PDF를 가져옵니다.

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - arXiv, OpenReview, 학회 피드를 모니터링하여 주어진 연구 아이디어와 겹치는 논문을 찾고, '안심·조사 필요·후속 확인'의 실행 가능한 신호를 제공합니다.

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - Chrome DevTools 브라우저 자동화를 통해 중국의 대표 학술 데이터베이스인 CNKI를 검색하고 메타데이터를 추출합니다.

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - 주장-출처 대장과 종합 매트릭스를 사용해, 길잡이 질문을 중심으로 이론을 발전시키는 문헌 검토를 구성합니다. 논문별 요약 나열과 근거 없는 연구 공백 주장은 허용하지 않습니다.

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) `zh` - PDF, arXiv, Zotero의 학술 논문을 읽고 분석하여 그림, 수식, 개념 링크가 포함된 구조화된 노트를 생성합니다.

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) `zh` - 최신 AI 연구를 따라가기 위해 수집, 평가, 노트 작성으로 이루어진 일일 논문 추천 파이프라인을 자동화합니다.

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - Google의 Gemini 리서치 에이전트 API를 통해 여러 단계의 문헌 및 기술 조사를 수행하고, 인용이 달린 상세 보고서를 작성합니다.

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - 브라우저 자동화로 Google Scholar를 검색하여, 인용 수와 전문 링크가 포함된 구조화된 결과를 반환합니다.

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - 논문 초안으로부터 순위가 매겨진 후보 논문과 관련 연구 섹션 요약을 생성합니다. Semantic Scholar, arXiv, OpenAlex를 대상으로 LLM 토론 방식의 순위 매기기를 수행하고, 인용 그래프를 따라 범위를 넓힙니다.

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - MinerU의 무료 Agent API 또는 토큰 기반 Standard API를 사용해 학술 PDF를 표와 수식 추출을 포함한 깔끔한 Markdown으로 변환합니다.

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - Nature Portfolio, AAAS Science, Cell Press의 학술지만을 날짜로 걸러 검색하여 원고 본문에 인용을 추가하고, 참고문헌 관리 도구용 파일 하나를 내보냅니다.

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - 과학 논문 한 편의 정독 내용을 근거에 기반한 16개 섹션 고정 형식의 연구 카드로 정리합니다.

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - Claude Code에서 브라우저 자동화로 Google NotebookLM 노트북에 질의하여, 인용이 달리고 출처에 근거한 답변을 얻습니다.

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) `zh` - 코드 검색, 수식 렌더링, 다이어그램을 포함한 6라운드 워크플로로 학술 논문을 상세한 HTML 글로 변환합니다.

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - 기술 연구를 위해 특허 선행기술 조사, 지식재산 동향 파악, 특허 가능성 평가를 수행합니다.

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) `zh` - Qinyan Academic OpenAPI로 문헌을 검색하여 GB/T 7714, IEEE, APA, MLA, Chicago, Harvard, Vancouver 형식의 학술 인용을 생성합니다.

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - PRISMA 2020 체크리스트의 27개 항목 전체에 따라 체계적 문헌 검토를 안내하고, 학술지 형식의 Word 원고, 주석이 달린 PRISMA 흐름도, APA 7판 참고문헌을 만듭니다. 메타분석과 통계적 통합은 명시적으로 제외합니다.

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - 인용 그래프를 따라 바깥으로 확장하고 초안의 주제를 독립적으로 검색하여, 초안이 놓쳤을 수 있는 관련 연구를 찾습니다. 각 후보를 참신성 주장을 얼마나 위협하는지에 따라 등급을 매깁니다.

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - CrossRef, PubMed, arXiv, Semantic Scholar, ChemRxiv에 질의하여 DOI, PMID, arXiv ID, 논문 제목으로부터 BibTeX 항목을 생성합니다.

## 연구 설계와 프로토콜

*자료를 수집하기 전에 무엇을 어떻게 측정할지 정합니다. 프로토콜, 윤리 심의, 사전등록, 표집, 측정 도구 설계가 대상입니다.*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - 의료기기 또는 의약품 임상시험의 연구 프로토콜을 단계별 워크플로로 작성합니다. 작성 전에 유사한 등록 시험을 조사하는 조사 전용 모드도 있습니다.

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - 컨조인트 설문 실험을 계획합니다. 속성 구조, 무작위화와 직교성, 검정력 계산, AMCE/AMIE 추정을 다룹니다.

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - 자료 수집 전에 연구를 계획합니다. 무작위화, 블록화, 요인 설계와 교차 설계, 군집 설계나 적응적 설계를 다룹니다.

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - 질적 자료 수집 도구와 절차를 설계합니다. 면담 가이드, 포커스 그룹 가이드, 관찰 프로토콜, 현장 노트 템플릿, 표집 전략이 대상입니다.

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - 질적 연구의 IRB 및 윤리 심의 프로토콜을 작성, 수정, 평가합니다. Common Rule에 따른 면제·신속·정규 심의 판정, 프로토콜 서술, 데이터 보안 계획을 다룹니다.

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - 의학 연구의 코호트 논리, 비교 대상 선택, 검증 전략을 검토하여, 분석을 시작하기 전에 누수와 타당도 위험을 찾아냅니다.

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - 통계적 검정력, 필요한 표본 크기, 최소 검출 가능 효과를 계산합니다. 군집이 있는 2군 RCT, 다군 설계, 비표준 설계의 시뮬레이션 기반 검정력을 지원하며, 등록에 바로 쓸 수 있는 검정력 섹션을 만듭니다.

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - OSF, AsPredicted, AEA RCT Registry 형식으로 구조화된 사전등록 문서를 작성합니다. 가설, 표집 계획, 분석 계획, 제외 기준, 추론 기준을 다루며, MUST/SHOULD/MAY 명확성 표시를 붙입니다.

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - 계획, 실험, 데이터셋, 주장이 확정된 연구 질문과 프로토콜에 여전히 부합하는지 확인합니다. 어긋남을 발견해도 기준이 되는 문서를 몰래 고쳐 쓰지 않습니다.

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - 출판된 사회과학 방법론에 비추어 설문 문항의 표현, 응답 척도, 설문 흐름을 작성하고 비평합니다. 측정 편향을 줄이는 것이 목적입니다.

## 방법의 형식화와 이론

*아이디어를 명시적인 방법으로 바꿉니다. 주장의 형식화, 유도 과정 점검, 증명의 작성과 검증이 대상입니다.*

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - 수식, 추정량, 항등식, 경계를 최소 두 번 독립적으로 다시 유도하고, 수학적 동치성에 따라 결과를 묶은 뒤, 일치와 이상치를 기록한 검증 매트릭스를 출력합니다.

- [Formula Derivation](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/formula-derivation) - 흩어진 수식과 이론 메모를 가정이 명시된 하나의 일관된 유도 과정으로 정리합니다. 메모만으로 유도를 뒷받침할 수 없으면 그 이유를 설명하는 차단 보고서를 냅니다.

- [Lean 4 Theorem Proving](https://github.com/cameronfreer/lean4-skills/tree/HEAD/plugins/lean4/skills/lean4) - Lean 4와 mathlib에서 수학 명제를 형식화하고 증명합니다. mathlib의 기존 보조정리 검색, `sorry` 채우기, 공리 확인, 반례 탐색을 수행합니다. 보조 스크립트와 세션 및 Bash 훅은 스킬 디렉터리가 아니라 바깥의 플러그인이 제공합니다.

- [Numerical Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/numerical-check) - 단조성, 임계값, 부등식, 극한에 관한 주장에 대해 매개변수 공간을 무작위로 탐색하여 반례를 찾습니다. 반례가 나오지 않아도 증명이 아니라 증거로 보고합니다.

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - 주어진 결과와 그 가정으로부터 정리, 보조정리, 명제의 엄밀한 수학적 증명을 작성하고 완성합니다.

- [Symbolic Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/symbolic-check) - 직접 작성한 항등식, 도함수, 극한, 비교정학 부호, 닫힌 형태의 해를 SymPy로 증명하거나 반증합니다. 모든 기호에 대해 정의역 가정을 명시하도록 요구합니다.

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - 논문의 정리 증명, 대수적 유도, 경계를 단계별로 확인하고, 빠진 가정과 누락된 기저 사례를 보고합니다. 논문이 기호의 정의역을 밝히지 않은 경우에는 해당 단계를 틀렸다고 판정하지 않고 미검증으로 표시합니다.

## 데이터와 어노테이션

*연구에 쓰이는 데이터를 확보하고, 레이블을 붙이고, 정리하고, 점검합니다.*

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - Hugging Face Hub, OpenML, GitHub, 논문 상호 참조에서 주어진 연구 과제에 맞는 데이터셋을 검색하여, 순위를 매기고 중복을 제거한 목록을 반환합니다.

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - 분석 전에 래스터, 벡터, 포인트, 원격탐사 데이터셋의 품질을 점검합니다. 좌표계, 측지 기준, 격자 정렬, 해상도, nodata, 도형 유효성, 공간 조인의 대응 수를 확인합니다.

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - 하나의 인터페이스로 유전체 및 생의학 데이터베이스를 조회하여 유전자 레코드, 서열, 정렬, AlphaFold 구조, 발현, 질병 연관성을 가져옵니다. 조회를 재현할 수 있도록 도구 버전을 고정합니다.

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - 모델 학습 전에 데이터셋의 편향, 분포, 공정성을 분석합니다.

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - 분자 구조를 파싱하고 정규화한 뒤, 기술자, 지문, 부분구조 매칭, 반응, 2D 또는 3D 좌표를 계산합니다. 화학정보학 작업을 위한 것입니다.

## 모델 학습과 미세조정

*단일 GPU 미세조정부터 분산 학습까지, 모델의 학습과 적응을 다룹니다.*

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - Hugging Face Jobs에서 TRL 또는 Unsloth로 언어 모델과 시각-언어 모델을 미세조정합니다. SFT, DPO, GRPO, 보상 모델링을 지원합니다.

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - Hugging Face Jobs의 클라우드 GPU에서 탐지, 분류, SAM/SAM2 분할 모델을 학습하고 미세조정합니다.

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - PyTorch 학습 코드를 LightningModule로 정리하고 Trainer를 설정합니다. 다중 GPU/TPU 확장, 분산 학습(DDP, FSDP, DeepSpeed), 로깅 연동(W&B, TensorBoard, MLflow)을 지원합니다.

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - Stable Baselines3의 실사용 가능한 PPO, SAC, DQN, TD3, DDPG, A2C 구현으로 Gymnasium 환경에서 강화학습 에이전트를 학습시킵니다.

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - NVIDIA TAO Toolkit의 최적화된 학습 및 내보내기 경로를 사용해 Hugging Face 모델을 미세조정합니다.

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - 오래 걸리는 머신러닝 학습 작업을 위한 사전 점검 목록을 수행하여, 설정, 경로, 모니터링의 오류를 실행 전에 찾아냅니다.

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - 고처리량 강화학습 라이브러리의 환경, 벡터화, 정책, 학습, 평가, 체크포인트 점검에 대해 버전을 고려한 지침을 제공합니다.

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - PyG로 그래프 신경망을 개발하는 과정을 안내합니다. 노드·링크·그래프 분류, 메시지 전달 아키텍처(GCN, GAT, GraphSAGE, GIN), 이종 그래프, 이웃 샘플링을 다룹니다.

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - sentence-transformers 라이브러리로 바이인코더, 크로스인코더, SPLADE 희소 임베딩 모델을 학습시킵니다.

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - TRL 명령줄 인터페이스로 Transformer 언어 모델을 미세조정합니다. SFT, DPO, GRPO, KTO, RLOO, 보상 모델링을 지원합니다.

## 다이어그램과 도식

*아키텍처, 파이프라인, 개념 그림 등 논문에 넣는 그려진 삽화입니다. 데이터로 그리는 차트와는 구분합니다.*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - 학술 논문 그림에 대해 독립된 TikZ 파일을 PDF로 만드는 절차를 강제합니다. 논문 소스에 TikZ를 직접 넣는 것을 금지하고, 모든 그림이 삽입 전에 컴파일되고 눈으로 확인되도록 요구합니다.

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - 경로 지도, 신호전달 다이어그램, 그래픽 초록을 메커니즘 우선으로 설계한 뒤, 벡터 또는 300~600 DPI 인쇄 출력을 겨냥한 이미지 모델용 프롬프트를 만듭니다.

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - 논문의 연구 유형과 메커니즘을 분류하여, 고정된 템플릿을 기계적으로 적용하는 대신 파이프라인, 아키텍처, 비교 매트릭스, 절제 매트릭스, 분류 트리 중 알맞은 그림 구조를 선택합니다.

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - .drawio XML 다이어그램을 생성하고 draw.io 데스크톱 CLI로 PNG/SVG/PDF/JPG로 내보냅니다. 순서도, 아키텍처 다이어그램, ER/UML 다이어그램, 네트워크 토폴로지, ML/DL 모델 그림(Transformer, CNN, LSTM)을 지원합니다.

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - 다이어그램, 그림, 아키텍처 시각 자료의 참조 이미지를 편집 가능한 Draw.io 파일로 재구성합니다. 편집 편의성보다 원본과의 시각적 일치를 우선합니다.

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - 자연어 설명으로부터 Mermaid 다이어그램을 생성하고 문법을 검증합니다. 순서도, 시퀀스 다이어그램, 클래스 다이어그램, ER 다이어그램, 간트 차트 등 총 23가지 유형을 지원합니다.

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - 복사해 쓸 수 있는 아이콘과 편집 가능한 템플릿 라이브러리에서 TikZ 그림을 찾고, 편집하고, 검증합니다. 신경망 아키텍처, 인코더-디코더 다이어그램, 학습 파이프라인, 시스템 블록 다이어그램이 대상입니다.

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - 논문의 방법론 설명과 그림 캡션으로부터 게재 품질의 학술 도식과 파이프라인 그림을 생성합니다. 다중 에이전트 파이프라인(Retriever, Planner, Stylist, Visualizer, Critic)이 협력하며, NeurIPS, ICML, ACL 같은 학회를 겨냥합니다.

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - 그래픽 초록, 도식, 워크플로 시각화, 아키텍처 다이어그램 제작을 안내합니다. 프로그래밍 방식과 디자인 도구 방식을 모두 다룹니다.

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - AI 이미지 모델로 게재 품질의 과학 도식을 만들고 반복적으로 개선합니다. 별도의 품질 검토 점수가 임계값보다 낮을 때만 다시 생성합니다. 신경망 아키텍처, 시스템 다이어그램, 순서도, 생물학적 경로에 특화되어 있습니다.

## 실험 관리와 재현성

*실험을 수행하고, 무슨 일이 있었는지 기록하며, 다른 사람이 결과를 재현할 수 있게 합니다.*

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - 특정 연구 방향의 논문을 조사하여 널리 쓰이는 벤치마크, 데이터셋, 지표, 평가 프로토콜을 추출합니다. 논문 한 편에서 추출하는 것도 가능합니다.

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - 벌크 RNA-seq 리드를 품질 관리, 트리밍, 정렬, 정량을 거쳐 유전자 수준의 카운트 행렬로 만듭니다. 차등 발현 분석 전에 실험 설계와 가닥 방향성을 확인합니다.

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - CCF 등급 학회·학술지 논문을 위한 근거 자료 묶음을 설계합니다. 데이터셋, 베이스라인, 지표, 절제 실험을 다룹니다.

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - R 또는 생물정보학 분석 프로젝트를 read/write/checkpoints 구조로 구성하여, 변경 불가능한 입력, 버전 관리되는 코드, 관리 대상이 아닌 출력을 분리합니다.

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - 머신러닝 파이프라인을 감사하여 학습-테스트 오염, 시간적·공간적 누수, 목표 변수 및 대리 변수 누수, 전처리 누수, 평가 오염을 찾아내고, 각 발견 사항을 심각도로 분류합니다.

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) `zh` - 머신러닝 실험 로그를 증거와 추측을 구분한 구조화된 중국어 출력으로 요약하고, 주간 보고용 초록도 작성합니다.

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - Ansys, Abaqus, Nastran, OpenFOAM, COMSOL에서의 유한요소 및 CAE 해석 주장을 관리합니다. 이상화 검토, GCI를 통한 격자 독립성 확인, 검증 및 타당성 확인, 사람의 승인 관문을 의무화합니다.

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - 체크포인트를 신뢰하기 전에 LibreYOLO 학습 실행의 설정, 데이터셋, 지표를 프로젝트 규약에 비추어 확인합니다.

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - 계산 재료 데이터를 위한 CMSO와 ASMO의 표준 온톨로지 용어를 찾아 줍니다. 관계를 주장하기 전에 클래스 계층과 속성의 정의역·치역을 확인합니다.

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) `zh` - 사진, 음성, 텍스트로 된 실험 기록을 YAML 프런트매터가 있는 Markdown으로 표준화하여 일반 로컬 폴더에 저장합니다. Obsidian 보관소와 Feishu 연동은 선택 사항입니다.

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - arXiv 논문을 인용 위치가 연결된 Python 구현으로 바꿉니다. 각 모듈에 그것이 구현하는 논문 섹션을 표시하고, 모호한 부분은 추측하지 않고 따로 표시합니다.

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - AI 코딩 에이전트의 캐시 디렉터리를 훑어 수치 실험 결과를 구조화된 형식으로 추출합니다.

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - 머신러닝 학습 실행을 비교할 때 같은 에폭 기준으로 맞추도록 강제하고, 대리 지표와 다운스트림 목표를 구분합니다.

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - '행동보다 증거 먼저'를 원칙으로 하는 5단계 절차로 실패한 머신러닝 실험을 진단합니다. 프로세스 상태, GPU, 디스크, 로그, 체크포인트를 확인합니다.

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - arXiv URL에서 측정 가능한 재현 실행까지 일곱 단계로 진행합니다. 코드, 하이퍼파라미터, 비공개 데이터셋이 없을 때는 공개된 대체 수단으로 대응합니다.

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - 논문 투고에 맞춰 연구 코드를 공개할 준비를 합니다. 저장소 정리, 의존성 점검, 재현성 체크리스트를 다룹니다.

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - artifact evaluation 제출을 위해 연구 코드와 데이터를 묶습니다. README와 부록, 이중 맹검 심사를 위한 익명화, ACM 배지 체계, Zenodo 또는 Software Heritage의 보관용 DOI 안내를 다루며, 학회의 현행 규정에 비추어 확인합니다.

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - AEA 데이터 및 코드 공개 기준에 맞춰 바로 제출할 수 있는 재현 자료를 구성합니다. README, 데이터셋 목록, 계산 환경 요건, 표·그림과 스크립트의 대응표, 기밀 데이터 기탁 계획을 포함합니다.

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - Slurm 클러스터에서 여러 작업으로 이루어진 실험을 진행하는 방법을 다룹니다. 실행 시간 산정, 작업과 작업 배열 구성, 제출 순서, 아무 결과도 내지 못했거나 모르는 사이에 잘못된 설정을 쓴 실행의 진단이 대상입니다.

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - 저자 자신의 로컬 코드가 내놓는 지표가 논문에 보고된 표와 주장과 정해진 허용 오차 안에서 여전히 일치하는지 점검합니다. 수치 불일치와 재현 실패는 따로 보고합니다.

## 통계 분석

*분석을 선택하고 수행합니다. 회귀, 인과 추론, 조사 가중치, 메타분석, 베이지안 모델링이 대상입니다.*

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - 실증 경제학의 인과 식별 전략을 선택하고 강건성을 점검합니다. 시차가 있는 이중차분, 약한 도구변수에 강건한 도구변수법, 회귀불연속, 통제집단합성법, shift-share 설계를 다룹니다.

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - 실증 연구 내용에서 통계적 오류와 방법론적 오류를 찾아내고, 심각도를 단계별로 구분해 제시합니다.

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - Python에서 복합표본 조사 자료를 분석합니다. 층, 1차 추출 단위, 가중치 처리, 분산 추정, 조사 가중 GLM을 지원하며, NHANES, CPS, DHS 같은 데이터셋에 쓸 수 있습니다.

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - R의 survey 패키지로 복합표본 조사 자료를 분석합니다. 설계 객체, 가중 평균과 총계, 조사 가중 회귀, 부분모집단 추정, 반복 가중치(BRR, 잭나이프, 부트스트랩)를 다룹니다.

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - R에서 고차원 고정효과 모형을 추정합니다. 다원 고정효과, 도구변수 추정, TWFE와 Sun-Abraham 이중차분, 군집 또는 이분산에 강건한 표준오차를 지원합니다.

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - 통계 검정을 선택하고, 그 가정을 점검하며, 효과 크기를 계산하고, 결과를 APA 형식으로 보고합니다. t 검정, 분산분석, 회귀, 베이지안 대안을 지원합니다.

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - 진단 정확도, 일치도, 생존, 성향 점수, 조사 가중 분석을 위한 재현 가능한 Python 또는 R 코드를 생성합니다. 데이터 파일을 읽기 전에 보호 대상 건강 정보가 들어 있는지 확인합니다.

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - PROSPERO 프로토콜 등록과 비뚤림 위험 평가부터 통계적 통합, PRISMA를 따르는 보고까지 메타분석 파이프라인을 수행합니다.

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - 실험 결과 파일을 분석하고, 유의성 검정과 모델 비교를 수행하며, 그림이 포함된 Results 섹션 초안을 작성합니다.

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) `zh` - PICO부터 원고 골격까지 네트워크 메타분석을 수행합니다. 검색 실행, 두 모델을 이용한 선별, 자료 추출, 비뚤림 위험 평가, R에서의 빈도주의 및 베이지안 통합, GRADE 평가, PRISMA-NMA 보고를 포함하며, 사람이 반드시 결정해야 하는 관문 다섯 개와 감사 로그가 있습니다.

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - PyMC로 베이지안 계층 모형을 구축, 적합, 검증합니다. MCMC 샘플링, 변분 추론, 사후 예측 점검을 다룹니다.

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - Stata 명령어(reghdfe, xtreg, ivregress, margins, esttab, svy:)를 R의 대응 표현으로 연결해 줍니다. 두 환경 사이에서 분석을 옮기는 연구자를 위한 것입니다.

## 질적 연구와 혼합 방법

*면담, 현장 연구, 코딩된 텍스트를 다룹니다. 주제 분석, 근거이론, 문화기술지, 코더 간 신뢰도가 대상입니다.*

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - 주제 분석, 근거이론, 해석현상학적 분석, 문화기술지, 사례 연구의 다섯 가지 전통에 걸친 질적 연구 설계와 분석을 다루며, 신뢰성 기준도 함께 제시합니다.

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - 코딩된 단위에 근거하여 성찰, 비교, 통합, 의사결정 메모를 구성하고 색인화합니다. 연구자의 해석은 기계 감사 로그와 분리하여 보관합니다.

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - 다차원 이론적 포화를 추적하고, 연구 단계에 따라 달라지는 방법론적 분리 규칙을 생성하며, 규칙 변경과 예외 적용을 성찰 일지에 기록합니다.

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - 질적 자료를 코딩하고 코드북을 만듭니다. 연역적·귀납적·혼합 코딩, 코드 빈도, 동시출현 분석, 코더 간 신뢰도를 지원합니다.

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - 근거이론, 성찰적 주제 분석, 내용 분석을 코드북 개발과 코더 간 신뢰도 점검과 함께 수행합니다. NVivo, ATLAS.ti, Dedoose, MAXQDA 형식으로 내보낼 수 있습니다.

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - Braun과 Clarke의 6단계 틀에 따라 면담, 포커스 그룹, 개방형 응답을 주제로 코딩합니다. 사전에 내려야 하는 네 가지 분석 결정과 15개 항목의 품질 체크리스트를 다룹니다.

## 해석 가능성

*학습된 모델을 열어 무엇을 계산하는지 살펴보고, 개별 예측을 설명합니다.*

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - 임의의 PyTorch 모델의 내부를 들여다보고 조작합니다. 로컬 GPU에 올리기에는 너무 큰 모델에 대해 NDIF를 통한 원격 실행도 가능합니다.

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - 선언적이고 딕셔너리 기반인 개입 프레임워크를 통해 PyTorch 모델에서 인과 추적, 활성화 패칭, 교환 개입 학습을 수행합니다.

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - 희소 오토인코더를 학습하고 분석하여, 다의적인 모델 활성화를 해석 가능한 특징으로 분해합니다. SAELens와 TransformerLens 라이브러리를 감싸고 있습니다.

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - 게임 이론 기반의 특징 기여도로 머신러닝 예측을 설명하고 감사합니다. explainer와 masker 선택, 기여도 계산과 검증, 다중 출력 설명, 국소·전역 시각화를 다룹니다.

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - 모델의 모든 활성화에 걸린 훅 지점을 통해 어텐션 패턴을 살펴보고 활성화 패칭 실험을 수행하여, Transformer가 구현한 알고리즘을 역공학합니다.

## 논문 수준의 플로팅과 시각화

*결과로부터 그리는 차트를 학술지나 학회가 요구하는 수준으로 만듭니다.*

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - 연구용 그림을 위한 실행 가능한 Matplotlib/Seaborn/mermaid 코드를 생성하고, 정량적 그림과 개념도 중 무엇을 쓸지 고르는 가이드를 함께 제공합니다.

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - 막대, 추세, 산점도, 히트맵, 다중 패널 레이아웃 등 바로 게재할 수 있는 Matplotlib 그림을 고정된 통일 스타일로 만듭니다. AI 학회와 학술지 투고를 위한 인쇄·벡터 내보내기 관행을 따릅니다.

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - 표 형식의 경도·위도 데이터를 검증하고 재현 가능한 SVG 연구 지점 지도를 그립니다. 행마다 공개, 일반화, 제한 중 하나의 공개 정책을 적용하고 좌표를 반올림합니다.

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - Python 또는 R로 영향력 높은 학술지를 위한 투고 수준의 과학 그림을 만들고, 수정하고, 점검합니다. 다중 패널과 학술지 요건에 맞는 내보내기를 지원합니다.

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - 원고의 그림 구성을 계획하고 점검합니다. 그림 하나에 주장 하나라는 원칙을 지키게 하고, 각 패널에 역할을 배정하며, 그림 설명이나 결과 본문을 쓰기 전에 본문과 보충 자료 중 어디에 둘지 결정합니다.

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - 실험 데이터와 개요로부터 학술 논문용 게재 품질의 그림과 개념도를 생성합니다. 시각-언어 모델의 비평을 이용한 개선은 선택 사항입니다.

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - 데이터-잉크 비율, 직접 레이블, 범위 프레임 축 등 Edward Tufte의 데이터 시각화 원칙을 여러 차트 라이브러리에 걸쳐 학술용 그림에 적용합니다.

## 글쓰기와 투고

*원고를 작성하고 투고할 수 있는 상태로 만듭니다. 구조, 서식, 투고처에 맞춘 조정, 제출 전 자체 점검이 대상입니다.*

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - 논문을 슬라이드로 바꾸고, 필요하면 내레이션이 들어간 데모 영상도 만듭니다. 대본 작성, 슬라이드 생성, 음성 합성 내레이션, 영상 조립을 다룹니다.

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - CCF 등급 학회·학술지를 대상으로 논문 본문을 계획, 작성, 수정하고 투고처에 맞게 조정합니다. 사용자 자신의 아이디어 범위와 근거는 그대로 유지합니다.

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - 저자가 승인한 로컬 콘텐츠로 편집 가능한 학회 포스터를 만듭니다. 실제 크기, 인쇄 제약, 접근성, 자료 출처, 내보내기 준비 상태를 확인합니다.

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - 삼선표와 독립 수식 등 중국어 학술 문서의 서식 관행에 맞춰 .docx 파일을 만들고 편집합니다.

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - 50개 이상의 스타일 가이드에 담긴 경제학 글쓰기 지침을 실행 가능한 규칙으로 정리하여, 경제학 논문의 작성과 수정에 쓸 수 있게 합니다.

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - 학술 연구비 신청서의 구조 설계, 지원 기관과의 적합성 평가, 예산 설계를 안내합니다.

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - 참조 말뭉치를 분석하고 원고를 섹션별로 수정하여, 학술 원고를 투고 대상 학술지의 글쓰기 관행에 맞춥니다.

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - 학술 글쓰기를 위한 LaTeX 문서의 작성, 컴파일, 형식 변환, 문서 분석을 처리합니다.

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) `zh` - 중국어 LaTeX 학위논문을 쓰는 대학원생을 돕습니다. 컴파일 진단, GB/T 7714 참고문헌 서식, 구조 검토, 블라인드 심사를 위한 익명화를 다룹니다.

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - 투고 또는 재투고 전에 원고의 최종 단계 사전 점검을 수행합니다. 주장, 그림, 그림 설명, 방법, 보충 자료를 투고처의 요건과 교차 확인합니다.

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) `zh` - 학술 논문 LaTeX 소스의 플로트 배치 문제를 고칩니다. 첫 참조 위치와의 거리, 너비 불일치, 몰림, 고립된 페이지가 대상입니다.

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) `zh` - LaTeX 넘침 문제(overfull box, 긴 수식, URL 넘침)를 고칩니다. 레이아웃만 바꾸는 편집부터 시작하고, 그것만으로 해결되지 않으면 문구 수정을 위임하는 단계로 넘어갑니다.

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - 가공되지 않은 연구 자료를 그림 계획, 문헌 검색 계획, 섹션 계획이 포함된 구조화된 개요로 변환합니다. 학술 논문 작성을 위한 것입니다.

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - 수치 정확성, 용어 일관성, 수식-코드 대응 점검을 통해 논문의 주장을 코드와 데이터에 비추어 검증합니다.

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - 이미 출판된 논문에서 확인된 오류를 저자 정정(corrigendum), 출판사 정정(erratum), 우려 표명, 철회 중 하나로 분류한 뒤, 공저자 통지문, 편집자 요청서, 공개 공지문 초안을 작성합니다.

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - 출판된 논문을 쉬운 말로 쓴 요약, 그래픽 초록 구상, 플랫폼별로 맞춘 소셜 미디어 문구로 바꿉니다. 어느 버전도 논문의 결과가 실제로 뒷받침하는 범위를 넘지 않도록 합니다.

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - ML/CV/NLP 논문의 수정을 안내합니다. 문단 수준의 명확성 점검, 역개요 작성, 주제문 정리, 주장-근거 대응 점검을 수행합니다.

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - 학술 및 연구 글에서 흔한 AI 글쓰기 패턴을 제거하여 더 자연스러운 문체로 되돌립니다.

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) `zh` - 연구 주제에 대한 서베이 초안을 작성합니다. 여러 논문을 논문별 요약이 아니라 문제 중심으로 방법의 발전을 따라가는 서술로 구성합니다.

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - 기존 Typst 원고에 대해 컴파일, 투고처 서식, 문법, 참고문헌, 투고 준비 상태 점검을 돕습니다.

## 동료 심사와 반박

*투고의 다른 한쪽입니다. 다른 사람의 원고를 심사하는 일과, 자신의 원고에 대한 심사 의견에 답하는 일을 다룹니다.*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - 분야별 심사자 페르소나 5명으로 구성된 국제 학술지 동료 심사 패널을 모의하여, 구조화된 편집 결정과 수정 로드맵을 제공합니다.

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - 심사자 입장에서 논문의 연구 진실성을 점검합니다. 원문 구간에 연결된 증거 대장을 만들고, 여러 모델의 감사기로 인용, 실험, 일관성, 베이스라인 비교의 조작 여부를 살핀 뒤, 사람 심사자를 위한 결정론적 판정을 계산합니다.

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - CCF 또는 투고 대상 학회의 기준에 따라 참신성, 타당성, 근거, 글의 품질, 형식 준수 측면에서 원고를 심사하며, 심사자와 영역 의장 패널을 모의합니다.

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - 경제학 논문에 대해 심사자 수준의 보고서를 작성합니다. 식별 전략, 통계적 추론, 표, 수식, 참고문헌을 점검하고, 지적 사항 대장과 우선순위가 매겨진 수정 계획을 출력합니다.

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - 분류, 전략, 초안 작성, 어조 수정 모드를 통해 동료 심사 의견을 근거에 기반한 반박 자료 묶음으로 변환합니다.

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - 학술 원고를 위한 구조화된 검토 및 수정 워크플로입니다. 투입 노력 수준에 맞춘 여섯 가지 작동 모드가 있습니다.

## 항목을 확인하는 방법

이것은 선별한 목록이지 인증이 아닙니다. 각 항목은 사람이 `SKILL.md`를 읽고 골랐습니다. 설명은 그 스킬이 무엇을 하는지를 말할 뿐, 여러분의 문제에 대해 처음부터 끝까지 실행해 본 결과를 보고하는 것이 아닙니다. 실행 가능한 엔드투엔드 테스트를 했다고 주장하는 항목은 하나도 없습니다. 실제로 하지 않았기 때문입니다. `SKILL.md`가 영어가 아닌 항목에는 이름 옆에 언어 태그를 붙였습니다.

**확인은 두 단계입니다.** `static check`(142개 중 96개)는 경로, 라이선스, 커밋 날짜, 필요한 권한과 환경을 실제 저장소에서 확인하고 `SKILL.md`를 읽었다는 뜻입니다. `audited`(142개 중 46개)는 여기에 더해, 문서화된 감사 명세에 따라 스킬 자체의 지시를 함께 제공되는 파일과 대조하며 단계별로 따라가 본 뒤 다음 중 하나의 판정을 받았다는 뜻입니다. `works`, `works with caveats`(목적은 달성하지만 미리 알아야 할 조건이 있음), `unverifiable`(자격 증명, 유료 접근 권한, 하드웨어 없이는 평가할 수 없음). 감사를 통해, 읽기에는 좋아 보이지만 작성자 본인 말고는 아무도 쓸 수 없는 항목을 삭제해 왔습니다.

**라이선스, 스타 수, 권한 및 환경 표시, 항목별 확인 상태는 이 페이지의 각 줄이 아니라 기계가 읽을 수 있는 색인에 있습니다.** [`index.json`](index.json)과 [`index.csv`](index.csv)이며, 이 페이지와 같은 데이터에서 생성됩니다. 스킬의 라이선스, 네트워크·자격 증명·훅이 필요한지 여부, 정확한 감사 판정이 중요하다면 열어 보기 전에 거기서 찾아보세요. 요약하면, 스킬 자체의 프런트매터에 있는 `license:`와 저장소의 LICENSE가 다를 때는 전자를 따릅니다. `repo ★N`은 그 *저장소*의 스타 수이며, 스킬 자체에 대한 평가가 결코 아닙니다. 이 스킬들의 94%는 다른 사람의 더 큰 저장소 안에 있으므로, 스타 2만 개짜리 모노레포에 있는 스킬이라도 한 번 커밋된 뒤 아무도 쓰지 않았을 수 있습니다.

모든 항목에 적용하는 구조적 확인(내용이 충실한지, 템플릿으로 찍어낸 것이 아닌지, 저장소가 확인되는지)은 분야와 무관하며, 이 목록이 보장하는 것은 바로 그 부분입니다. 임상시험, 질적 코딩, 계량경제학 스킬이 *여러분의 분야에서 방법론적으로 올바른지*는 여기에 포함된 모든 분야에 대해 큐레이터가 판단할 수 있는 일이 아닙니다. 각 분야의 항목은 전문가의 검증을 거친 것이 아니라, 직접 평가해 볼 단서로 다루어 주세요.

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 이 목록은 데이터에서 생성되므로 README를 직접 편집하지 마세요.
