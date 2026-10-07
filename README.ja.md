# Awesome Research Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Skills](https://img.shields.io/badge/skills-142-blue?style=flat) [![Last Commit](https://img.shields.io/github/last-commit/neverbiasu/awesome-research-skills?style=flat)](https://github.com/neverbiasu/awesome-research-skills/commits/main)

[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [한국어](README.ko.md)

> 文献レビューから査読まで、学術研究の各段階を支援する Agent Skill です。

アイデア出し → 文献 → 研究デザイン → 手法と理論 → データ → 学習 → 図解 → 実験 → 統計 → 質的研究 → 解釈可能性 → 作図 → 執筆 → 査読

142 件のスキルを、1つずつ読んで選びました。どの項目も、「何か役に立つものが入っているかもしれないリポジトリ」ではなく、特定の `SKILL.md` ディレクトリ1つを指しています。対象は、研究者が自分の手で行う作業です。先行研究の調査、研究デザイン、手法の定式化、データの整備、実験の実行、統計分析、質的分析、図の作成、執筆、査読を扱います。研究全体を自動で回すパイプラインや、MLOps・デプロイ用のツールは対象外です。

すべての項目は、リポジトリと照らして内容を読み、ライセンス、最終コミット、実行に必要なもの（ネットワーク、認証情報、フック）を確認しています。テンプレートで量産されたものや放置されたものは載せていません。そのうち 46 件は、文書化した仕様に沿って手作業で手順をたどって確認しています。データは 2026-10-05 時点で GitHub と照合済みです。各項目が `static check` か `audited: <判定>` かは `index.json` に記録しており、定義は下の「各項目の確認方法」にあります。

項目名とリンクは英語版と同じです。説明文は翻訳で、内容に違いがある場合は[英語版](README.md)が正となります。

## 目次

- [研究の方向性探索とアイデア出し](#研究の方向性探索とアイデア出し)
- [文献レビュー](#文献レビュー)
- [研究デザインとプロトコル](#研究デザインとプロトコル)
- [手法の定式化と理論](#手法の定式化と理論)
- [データとアノテーション](#データとアノテーション)
- [モデルの学習とファインチューニング](#モデルの学習とファインチューニング)
- [図解と模式図](#図解と模式図)
- [実験管理と再現性](#実験管理と再現性)
- [統計分析](#統計分析)
- [質的研究と混合研究法](#質的研究と混合研究法)
- [解釈可能性](#解釈可能性)
- [論文品質の作図と可視化](#論文品質の作図と可視化)
- [執筆と投稿](#執筆と投稿)
- [査読と反論](#査読と反論)
- [各項目の確認方法](#各項目の確認方法)

## 研究の方向性探索とアイデア出し

*漠然とした関心を、定式化された検証可能な研究課題にします。*

- [Archora: Hypothesis](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/hypothesis) - ユーザーが提供したメモや資料から、反証可能で構造化された研究仮説の作成を導きます。

- [Brainstorming Research Ideas](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/brainstorming-research-ideas) - 新しい問題領域に入るときや、プロジェクトの方向性を見直すときに、構造化された発想の枠組みを使って研究の方向性を見つけ出します。

- [Claude Scholar: Research Ideation](https://github.com/Galaxy-Dawn/claude-scholar/tree/HEAD/skills/research-ideation) - 5W1H のブレインストーミング、体系的な文献レビュー、多面的なギャップ分析、SMART な研究課題の定式化によって、研究プロジェクトの立ち上げを構造化します。

- [Creative Thinking for Research](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/21-research-ideation/creative-thinking-for-research) - 組み合わせによる創造、類推的推論、制約の操作といった認知科学の創造性の技法を、研究の方向性の発想に応用します。

- [Research Gap Finder](https://github.com/chtc66/academic-skills/tree/HEAD/research-gap-finder) `zh` - 文献と初期のアイデアを分析し、根拠のある研究ギャップと検証可能な着手点を特定します。新規性の主張を無理に作ることはしません。

## 文献レビュー

*先行研究を探し、読み、統合し、引用を正確に保ちます。*

- [bioRxiv Database Search](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/biorxiv-database) - キーワード、著者、期間、分野カテゴリで bioRxiv のプレプリントのメタデータを検索し、PDF を取得します。

- [CCF Literature Monitor](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-literature-monitor) - arXiv、OpenReview、会議のフィードを監視し、指定した研究アイデアと重なる論文を見つけて、「問題なし・要調査・要フォロー」の行動指針を示します。

- [CNKI Skills](https://github.com/cookjohn/cnki-skills/tree/HEAD/skills/cnki-search) - Chrome DevTools によるブラウザ自動操作で、中国の主要な学術データベース CNKI を検索し、メタデータを抽出します。

- [Critical Integrative Review](https://github.com/ozzyzhou99/critical-integrative-review-skill/tree/HEAD/write-critical-literature-review) - 主張と出典の台帳および統合マトリクスを使い、導きとなる問いを軸に理論を発展させる文献レビューを構築します。論文ごとの要約の羅列や根拠のないギャップの主張は認めません。

- [Daily Paper Reader](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/paper-reader) `zh` - PDF、arXiv、Zotero の学術論文を読んで分析し、図、数式、概念リンクを含む構造化ノートを生成します。

- [Daily Papers](https://github.com/huangkiki/dailypaper-skills/tree/HEAD/skills/daily-papers) `zh` - 最新の AI 研究を追うために、取得、評価、ノート作成からなる毎日の論文推薦パイプラインを自動化します。

- [Gemini Deep Research](https://github.com/sanjay3290/ai-skills/tree/HEAD/skills/deep-research) - Google の Gemini リサーチエージェント API を通じて複数段階の文献・技術調査を実行し、引用付きの詳細なレポートを作成します。

- [Google Scholar Skills](https://github.com/cookjohn/gs-skills/tree/HEAD/skills/gs-search) - ブラウザ自動操作で Google Scholar を検索し、被引用数と全文リンクを含む構造化された結果を返します。

- [LitLLM](https://github.com/litllm/litllm/tree/HEAD/skill) - 論文の草稿から、順位付けした候補論文と関連研究セクションの要約を生成します。Semantic Scholar、arXiv、OpenAlex を対象に LLM によるディベート形式のランキングを行い、引用グラフをたどって範囲を広げます。

- [MinerU Skill](https://github.com/nebutra/mineru-skill/tree/HEAD/skills/mineru) - MinerU の無料の Agent API またはトークン制の Standard API を使い、学術 PDF を表と数式の抽出を含めてきれいな Markdown に変換します。

- [Nature Citation](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-citation) - Nature Portfolio、AAAS Science、Cell Press の雑誌だけを日付で絞り込んで検索し、原稿の本文に引用を追加して、文献管理ソフト用のファイルを1つ書き出します。

- [Nature Paper Card](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-paper-card) - 1本の科学論文の精読を、エビデンスに基づく16セクション固定の研究カードにまとめます。

- [NotebookLM Skill](https://github.com/pleaseprompto/notebooklm-skill) - Claude Code からブラウザ自動操作で Google NotebookLM のノートブックに問い合わせ、引用付きで出典に基づいた回答を得ます。

- [Paper Analyzer](https://github.com/zsyggg/paper-craft-skills/tree/HEAD/skills/paper-analyzer) `zh` - コード検索、数式のレンダリング、図を含む6ラウンドのワークフローで、学術論文を詳細な HTML 記事に変換します。

- [Patent Research](https://github.com/borghei/Claude-Skills/tree/HEAD/research/patent) - 技術研究のために、特許の先行技術調査、知的財産の動向の整理、特許性の評価を行います。

- [Qinyan Citation](https://github.com/LeonChaoX/qinyan-academic-skills/tree/HEAD/skills/沁言学术skills/qinyan-citation) `zh` - Qinyan Academic OpenAPI で文献を検索し、GB/T 7714、IEEE、APA、MLA、Chicago、Harvard、Vancouver の各形式で整形した学術引用を生成します。

- [SLR PRISMA](https://github.com/keemanxp/slr-prisma) - PRISMA 2020 チェックリストの全27項目に沿って系統的文献レビューを導き、ジャーナル形式の Word 原稿、注釈付きの PRISMA フロー図、APA 第7版の参考文献を作成します。メタ分析と統計的統合は明示的に対象外です。

- [Surveying Literature](https://github.com/chgagne/claude-skills-research/tree/HEAD/surveying-literature) - 引用グラフを外側にたどり、草稿のトピックを独立に検索することで、草稿が見落としている可能性のある関連研究を見つけます。各候補を、新規性の主張をどの程度脅かすかで評価します。

- [Wenxian](https://github.com/njzjz/wenxian/tree/HEAD/skill) - CrossRef、PubMed、arXiv、Semantic Scholar、ChemRxiv に問い合わせ、DOI、PMID、arXiv ID、論文タイトルから BibTeX エントリを生成します。

## 研究デザインとプロトコル

*データを集める前に、何をどう測るかを決めます。プロトコル、倫理審査、事前登録、サンプリング、測定用具の設計が対象です。*

- [Clinical Trial Protocol](https://github.com/anthropics/healthcare/tree/HEAD/plugins/healthcare/skills/clinical-trial-protocol) - 医療機器または医薬品の治験プロトコルを段階的なワークフローで起草します。起草前に類似の登録済み試験を調べる調査専用モードもあります。

- [Conjoint Experiment Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/conjoint-design) - コンジョイント調査実験を計画します。属性の構成、無作為化と直交性、検出力の計算、AMCE/AMIE の推定を扱います。

- [Experimental Design](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/experimental-design) - データ収集の前に研究を計画します。無作為化、ブロック化、要因計画とクロスオーバー計画、クラスターデザインや適応的デザインを扱います。

- [Fieldwork Methods](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/fieldwork-methods) - 質的データ収集の道具と手順を設計します。インタビューガイド、フォーカスグループガイド、観察プロトコル、フィールドノートのテンプレート、サンプリング戦略が対象です。

- [IRB Protocol](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/irb-protocol) - 質的研究の IRB・倫理審査プロトコルを作成、改訂、評価します。Common Rule における免除・迅速・本審査の判定、プロトコル本文、データセキュリティ計画を扱います。

- [Medical Study Design Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/design-study) - 医学研究のコホートの論理、比較対照の選択、検証戦略をレビューし、分析を始める前にリークと妥当性のリスクを洗い出します。

- [Power Analysis](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/power-analysis) - 検出力、必要なサンプルサイズ、最小検出可能効果を計算します。クラスターを含む2群 RCT、多群デザイン、標準的でないデザインのシミュレーションによる検出力に対応し、登録にそのまま使える検出力のセクションを作成します。

- [Preregister](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/preregister) - OSF、AsPredicted、AEA RCT Registry の形式で、構造化された事前登録文書を起草します。仮説、標本抽出計画、分析計画、除外基準、推論の基準を扱い、MUST/SHOULD/MAY の明確さのフラグを付けます。

- [Research Question Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/research-question-audit) - 計画、実験、データセット、主張が、確定済みの研究課題とプロトコルに沿っているかを確認します。ずれが見つかっても、基準となる文書を黙って書き換えることはしません。

- [Survey Instrument Designer](https://github.com/scdenney/open-science-skills/tree/HEAD/plugin/skills/survey-design) - 公刊された社会科学の方法論に照らして、調査票の質問文、回答尺度、質問の流れを起草し、批評します。測定バイアスを減らすことが目的です。

## 手法の定式化と理論

*アイデアを明示的な手法にします。主張の定式化、導出の確認、証明の作成と検証が対象です。*

- [Derivation Verify](https://github.com/fkguo/nullius/tree/HEAD/skills/derivation-verify) - 数式、推定量、恒等式、上下界を少なくとも2回独立に導出し直し、数学的同値性で結果をまとめ、一致と外れ値を記録した検証マトリクスを出力します。

- [Formula Derivation](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/formula-derivation) - 散在する数式や理論メモを、仮定を明示した一貫した導出にまとめます。メモだけでは導出を支えられない場合は、その理由を説明するブロッカーレポートを出します。

- [Lean 4 Theorem Proving](https://github.com/cameronfreer/lean4-skills/tree/HEAD/plugins/lean4/skills/lean4) - Lean 4 と mathlib で数学的な命題を形式化して証明します。mathlib の既存の補題の検索、`sorry` の補完、公理の確認、反例の探索を行います。補助スクリプトと、セッションおよび Bash のフックは、スキルのディレクトリではなく外側のプラグインが提供します。

- [Numerical Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/numerical-check) - 単調性、閾値、不等式、極限に関する主張について、パラメータ空間をランダムに探索して反例を探します。反例が見つからなくても、証明ではなく証拠として報告します。

- [Proof Writer](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/proof-writer) - 与えられた結果とその仮定から、定理、補題、命題の厳密な数学的証明を起草し、完成させます。

- [Symbolic Check](https://github.com/flonat/flonat-research/tree/HEAD/skills/symbolic-check) - 自分で書いた恒等式、導関数、極限、比較静学の符号、閉形式解を SymPy で証明または反証します。すべての記号について定義域の仮定を明示することを求めます。

- [Verifying Proofs](https://github.com/chgagne/claude-skills-research/tree/HEAD/verifying-proofs) - 論文の定理の証明、代数的な導出、上下界を一歩ずつ確認し、欠けている仮定や基底ケースの欠落を報告します。論文が記号の定義域を述べていない場合は、その手順を誤りとはせず、未検証として示します。

## データとアノテーション

*研究に使うデータの入手、ラベル付け、整備、監査を扱います。*

- [Dataset Discovery](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/dataset-discovery) - Hugging Face Hub、OpenML、GitHub、論文の相互参照から、指定した研究タスクに合うデータセットを検索し、順位付けして重複を除いた一覧を返します。

- [Geospatial Data QC](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/geospatial-data-qc) - 分析の前に、ラスター、ベクター、ポイント、リモートセンシングのデータセットを品質チェックします。座標参照系、測地系、グリッドの整合、解像度、nodata、ジオメトリの妥当性、空間結合の多重度を確認します。

- [gget](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/gget) - 単一のインターフェースでゲノム・生物医学データベースを検索し、遺伝子レコード、配列、アラインメント、AlphaFold 構造、発現、疾患との関連を取得します。検索を再現できるよう、ツールのバージョンを固定します。

- [PhD Skills: Dataset Curation](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/dataset-curation) - モデルを学習させる前に、データセットのバイアス、分布、公平性を分析します。

- [RDKit Cheminformatics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/rdkit) - 分子構造を解析して正規化し、記述子、フィンガープリント、部分構造マッチ、反応、2D または 3D 座標を計算します。ケモインフォマティクス向けです。

## モデルの学習とファインチューニング

*単一 GPU でのファインチューニングから分散学習まで、モデルの学習と適応を扱います。*

- [Hugging Face LLM Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-llm-trainer) - Hugging Face Jobs 上で TRL または Unsloth を使い、言語モデルと視覚言語モデルをファインチューニングします。SFT、DPO、GRPO、報酬モデリングに対応します。

- [Hugging Face Vision Trainer](https://github.com/huggingface/skills/tree/HEAD/skills/huggingface-vision-trainer) - Hugging Face Jobs のクラウド GPU で、検出、分類、SAM/SAM2 セグメンテーションのモデルを学習・ファインチューニングします。

- [K-Dense: PyTorch Lightning](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pytorch-lightning) - PyTorch の学習コードを LightningModule に整理し、Trainer を設定します。複数 GPU/TPU へのスケーリング、分散学習（DDP、FSDP、DeepSpeed）、ロギング連携（W&B、TensorBoard、MLflow）に対応します。

- [K-Dense: Stable Baselines3](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/stable-baselines3) - Stable Baselines3 の実運用可能な PPO、SAC、DQN、TD3、DDPG、A2C 実装を使い、Gymnasium 環境で強化学習エージェントを学習させます。

- [NVIDIA TAO Finetune Hugging Face Model](https://github.com/NVIDIA/skills/tree/HEAD/skills/tao-finetune-huggingface-model) - NVIDIA TAO Toolkit の最適化された学習・エクスポートの経路を使い、Hugging Face のモデルをファインチューニングします。

- [PhD Skills: Launch](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/launch) - 長時間かかる機械学習の学習ジョブについて、起動前のチェックリストを実行し、設定、パス、監視の誤りを起動前に見つけます。

- [PufferLib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pufferlib) - 高スループットな強化学習ライブラリの環境、ベクトル化、方策、学習、評価、チェックポイントの確認について、バージョンを踏まえた指針を提供します。

- [PyTorch Geometric](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/torch-geometric) - PyG でのグラフニューラルネットワーク開発を導きます。ノード・リンク・グラフ分類、メッセージパッシング型アーキテクチャ（GCN、GAT、GraphSAGE、GIN）、異種グラフ、近傍サンプリングを扱います。

- [Train Sentence Transformers](https://github.com/huggingface/skills/tree/HEAD/skills/train-sentence-transformers) - sentence-transformers ライブラリで、バイエンコーダ、クロスエンコーダ、SPLADE のスパース埋め込みモデルを学習させます。

- [TRL Training](https://github.com/huggingface/skills/tree/HEAD/skills/trl-training) - TRL のコマンドラインインターフェースで Transformer 言語モデルをファインチューニングします。SFT、DPO、GRPO、KTO、RLOO、報酬モデリングに対応します。

## 図解と模式図

*アーキテクチャ図、パイプライン図、概念図など、論文に載せる描いた図です。データから描くグラフとは区別します。*

- [Academic Figure Drawing (TikZ)](https://github.com/nanoAgentTeam/research-claw/tree/HEAD/config/.skills/figure-drawing) - 学術論文の図について、独立した TikZ ファイルから PDF を作る手順を徹底します。論文のソースへの TikZ の直接記述を禁じ、すべての図について、挿入前にコンパイルが通り、目視で確認されていることを求めます。

- [Biomedical Mechanism Figures](https://github.com/yiyanli123/biorender-mechanism-figures-skill/tree/HEAD/biorender-mechanism-figures) - パスウェイ図、シグナル伝達図、グラフィカルアブストラクトをメカニズム優先で設計し、ベクター形式または 300〜600 DPI の印刷出力を想定した画像モデル用プロンプトを作成します。

- [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) - 論文の研究タイプとメカニズムを分類し、固定テンプレートを機械的に当てはめるのではなく、パイプライン、アーキテクチャ、比較マトリクス、アブレーションマトリクス、分類ツリーの中から適切な図の構造を選びます。

- [Draw.io Diagrams](https://github.com/Agents365-ai/drawio-skill/tree/HEAD/skills/drawio-skill) - .drawio XML の図を生成し、draw.io デスクトップ版の CLI で PNG/SVG/PDF/JPG に書き出します。フローチャート、アーキテクチャ図、ER/UML 図、ネットワーク構成図、ML/DL モデル図（Transformer、CNN、LSTM）に対応します。

- [Draw.io Reconstruction](https://github.com/HKUSTDial/Supervisor-Skills/tree/HEAD/skills/drawio-reconstruction) - 図、グラフ、アーキテクチャ図の参照画像を、編集可能な Draw.io ファイルとして再構成します。編集のしやすさよりも元画像への視覚的な忠実さを優先します。

- [Mermaid Diagram Generator](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/HEAD/skills/mermaid-diagram) - 自然言語の説明から Mermaid 図を生成し、構文を検証します。フローチャート、シーケンス図、クラス図、ER 図、ガントチャートなど計23種類に対応します。

- [OpenTikZ](https://github.com/opentikz/opentikz/tree/HEAD/skills/using-opentikz) - コピーして使えるアイコンと編集可能なテンプレートのライブラリから、TikZ の図を探して編集し、検証します。ニューラルネットワークのアーキテクチャ、エンコーダ・デコーダ図、学習パイプライン、システムブロック図が対象です。

- [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/HEAD/skill) - 論文の手法の説明と図のキャプションから、掲載品質の学術的な模式図やパイプライン図を生成します。マルチエージェントのパイプライン（Retriever、Planner、Stylist、Visualizer、Critic）が連携し、NeurIPS、ICML、ACL などの会議を想定しています。

- [Scientific Illustration Guide](https://github.com/wentorai/research-plugins/tree/HEAD/skills/tools/diagram/scientific-illustration-guide) - グラフィカルアブストラクト、模式図、ワークフローの可視化、アーキテクチャ図の作成を導きます。プログラムによる作図とデザインツールによる作図の両方を扱います。

- [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/scientific-schematics) - AI 画像モデルで掲載品質の科学的な模式図を作成し、反復的に改善します。別途行う品質レビューの点数が閾値を下回った場合にのみ再生成します。ニューラルネットワークのアーキテクチャ、システム図、フローチャート、生物学的パスウェイを得意とします。

## 実験管理と再現性

*実験を実行し、何が起きたかを記録し、他の人が結果を再現できるようにします。*

- [Benchmark Research Skill](https://github.com/eternalwavee/benchmark-research-skill) - ある研究分野の論文を調査し、よく使われるベンチマーク、データセット、指標、評価プロトコルを抽出します。単一の論文からの抽出にも対応します。

- [Bulk RNA-seq Pipeline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/bulk-rnaseq) - バルク RNA-seq のリードを、品質管理、トリミング、アラインメント、定量を経て遺伝子レベルのカウント行列にします。発現変動解析の前に、実験デザインとストランド情報を確認します。

- [CCF Experiment Designer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-experiment-designer) - CCF ランクの会議・論文誌向け論文のエビデンス一式を設計します。データセット、ベースライン、指標、アブレーションを扱います。

- [Creating Analysis Projects](https://github.com/wolf5996/agentic-skills/tree/HEAD/creating-analysis-projects) - R またはバイオインフォマティクスの解析プロジェクトを read/write/checkpoints 構成で立ち上げ、変更不可の入力、バージョン管理するコード、管理対象外の出力を分離します。

- [Data Leakage Audit](https://github.com/isshikiayane/research-workflow-skills/tree/HEAD/data-leakage-audit) - 機械学習パイプラインを監査し、学習・テスト間の汚染、時間的・空間的リーク、目的変数や代理変数のリーク、前処理リーク、評価の汚染を調べ、各指摘を重大度で分類します。

- [Experiment Log Summarizer](https://github.com/chtc66/academic-skills/tree/HEAD/experiment-log-summarizer) `zh` - 機械学習の実験ログを、証拠と推測を分けた構造化された中国語の出力に要約し、週次報告用の要旨も作成します。

- [FEM/CAE Governance](https://github.com/test1card/femis-skill) - Ansys、Abaqus、Nastran、OpenFOAM、COMSOL における有限要素解析・CAE 解析の主張を統制します。理想化のレビュー、GCI によるメッシュ非依存性の確認、検証と妥当性確認、人による承認ゲートを必須にします。

- [LibreYOLO Verify Training](https://github.com/LibreYOLO/libreyolo/tree/HEAD/skills/libreyolo-verify-training) - チェックポイントを信頼する前に、LibreYOLO の学習実行の設定、データセット、指標をプロジェクトの規約に照らして確認します。

- [Materials Ontology Explorer](https://github.com/HeshamFS/materials-simulation-skills/tree/HEAD/skills/ontology/ontology-explorer) - 計算材料データのために CMSO と ASMO の正規のオントロジー用語を特定します。関係を主張する前に、クラス階層とプロパティの定義域・値域を確認します。

- [Nature Experiment Log](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-experiment-log) `zh` - 写真、音声、テキストによる実験記録を、YAML フロントマター付きの Markdown に標準化して、通常のローカルフォルダに書き込みます。Obsidian の保管庫や Feishu との連携は任意です。

- [Paper2Code](https://github.com/PrathamLearnsToCode/paper2code/tree/HEAD/skills/paper2code) - arXiv の論文を、引用箇所に紐づいた Python 実装に変換します。各モジュールに、それが実装する論文のセクションを付記し、曖昧な点は推測せずに明示します。

- [PaperOrchestra: Agent Research Aggregator](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/agent-research-aggregator) - AI コーディングエージェントのキャッシュディレクトリを走査し、数値の実験結果を構造化された形式で抽出します。

- [PhD Skills: Compare](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/compare) - 機械学習の学習実行を比較するときに同じエポックでの対応づけを徹底し、代理指標と下流の目標を分けて扱います。

- [PhD Skills: Debug](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/debug) - 「行動の前に証拠」を原則とする5段階の手順で、失敗した機械学習の実験を診断します。プロセスの状態、GPU、ディスク、ログ、チェックポイントを確認します。

- [PhD Skills: Reproduce](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/reproduce) - arXiv の URL から測定可能な再現実行まで、7つの段階で進めます。コード、ハイパーパラメータ、非公開データセットが欠けている場合は、公開されている代替手段で対処します。

- [PhD Skills: Research Publishing](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/research-publishing) - 論文の投稿に合わせて研究コードを公開する準備をします。リポジトリの整理、依存関係の監査、再現性チェックリストを扱います。

- [Prepare Artifacts](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/prepare-artifacts) - artifact evaluation への提出に向けて、研究のコードとデータをまとめます。README と付録、ダブルブラインド査読のための匿名化、ACM バッジの体系、Zenodo や Software Heritage でのアーカイブ用 DOI の指針を扱い、会議の最新の規則と照らして確認します。

- [Replication Package](https://github.com/pedrohcgs/claude-code-my-workflow/tree/HEAD/.claude/skills/replication-package) - AEA のデータ・コード公開基準に沿って、そのまま提出できる再現用の資料一式をまとめます。README、データセットの一覧、計算環境の要件、表・図とスクリプトの対応表、機密データの寄託計画を含みます。

- [Running Cluster Experiments](https://github.com/chgagne/claude-skills-research/tree/HEAD/running-cluster-experiments) - Slurm クラスター上で多数のジョブからなる実験を進める方法を扱います。実行時間の見積もり、ジョブとジョブ配列の組み方、投入の順序、何も出力しなかった実行や気づかないうちに誤った設定を使った実行の診断が対象です。

- [Verify Results](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/HEAD/skills/verify-results) - 著者自身のローカルのコードが出力する指標が、論文に記載された表や主張と、指定した許容誤差の範囲で今も一致しているかを監査します。数値の不一致と再現の失敗は分けて報告します。

## 統計分析

*分析を選んで実行します。回帰、因果推論、調査ウェイト、メタ分析、ベイズモデリングが対象です。*

- [AER Identification](https://github.com/brycewang-stanford/AER-Skills/tree/HEAD/skills/aer-identification) - 実証経済学の因果識別戦略を選び、頑健性を検証します。対象は時期のずれた差の差分析、弱操作変数に頑健な操作変数法、回帰不連続、合成コントロール、シフトシェア設計です。

- [Archora: Stats](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/stats) - 実証研究の内容に含まれる統計的な誤りや方法論上の誤謬を検出し、重大度を段階分けして示します。

- [Complex Survey Analysis (Python)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/svy) - Python で複雑な標本調査データを分析します。層、一次抽出単位、ウェイトの処理、分散推定、調査加重 GLM に対応し、NHANES、CPS、DHS などのデータセットで使えます。

- [Complex Survey Analysis (R)](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/survey-r) - R の survey パッケージで複雑な標本調査データを分析します。デザインオブジェクト、加重平均と総計、調査加重回帰、部分母集団推定、反復ウェイト（BRR、ジャックナイフ、ブートストラップ）を扱います。

- [Fixest](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/fixest) - R で高次元固定効果モデルを推定します。多元固定効果、操作変数推定、TWFE と Sun-Abraham の差の差分析、クラスター頑健または不均一分散頑健な標準誤差に対応します。

- [Guided Statistical Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/statistical-analysis) - 統計的検定を選び、その前提を確認し、効果量を計算して、結果を APA 形式で報告します。t 検定、分散分析、回帰、ベイズ的な代替手法に対応します。

- [Medical Statistical Analysis](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/analyze-stats) - 診断精度、一致度、生存、傾向スコア、調査加重の分析のために、再現可能な Python または R のコードを生成します。データファイルを読む前に、保護対象の健康情報が含まれていないか確認します。

- [Meta-Analysis & Systematic Review](https://github.com/Aperivue/medsci-skills/tree/HEAD/skills/meta-analysis) - PROSPERO へのプロトコル登録とバイアスリスク評価から、統計的統合、PRISMA に準拠した報告までのメタ分析パイプラインを実行します。

- [ML Experiment Results Analysis](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/inno-experiment-analysis) - 実験結果のファイルを分析し、有意性検定とモデル比較を実行して、図を添えた Results セクションを起草します。

- [Network Meta-Analysis Pipeline](https://github.com/xinglongMedical/nma-research-skill) `zh` - PICO から原稿の骨子までのネットワークメタ分析を実行します。検索の実行、2つのモデルによるスクリーニング、データ抽出、バイアスリスク評価、R での頻度論的・ベイズ的統合、GRADE 評価、PRISMA-NMA 報告を含み、人による必須の判断ゲートが5つと監査ログがあります。

- [PyMC Bayesian Modeling](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pymc) - PyMC でベイズ階層モデルを構築、推定、検証します。MCMC サンプリング、変分推論、事後予測チェックを扱います。

- [Stata-to-R Translation](https://github.com/DAAF-Contribution-Community/daaf/tree/HEAD/.claude/skills/stata-r-translation) - Stata のコマンド（reghdfe、xtreg、ivregress、margins、esttab、svy:）を R の対応する書き方に対応づけます。2つの環境の間で分析を移行する研究者向けです。

## 質的研究と混合研究法

*インタビュー、フィールドワーク、コーディングしたテキストを扱います。主題分析、グラウンデッド・セオリー、エスノグラフィー、コーダー間信頼性が対象です。*

- [AlterLab Qualitative Methods](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills/tree/HEAD/skills/research-tools/alterlab-qualitative-methods) - 主題分析、グラウンデッド・セオリー、解釈的現象学的分析、エスノグラフィー、事例研究の5つの伝統にわたる質的研究の設計と分析を扱い、信用性の基準も示します。

- [Analytic Memo Writing](https://github.com/smirik/psy-qm-skills/tree/HEAD/skills/memo-write) - コーディング済みの単位に基づいて、省察、比較、統合、意思決定のメモを組み立てて索引化します。研究者の解釈は機械の監査ログと分けて保持します。

- [Methodological Rules & Saturation](https://github.com/linxule/interpretive-orchestration/tree/HEAD/plugin/skills/methodological-rules) - 多面的な理論的飽和を追跡し、研究段階に応じた方法論上の分離ルールを生成して、ルールの変更と上書きを省察ジャーナルに記録します。

- [Qualitative Analysis](https://github.com/MattArtzAnthro/AI-Anthropology-Toolkit/tree/HEAD/skills/qualitative-analysis) - 質的データをコーディングしてコードブックを作成します。演繹的・帰納的・混合コーディング、コード頻度、共起分析、コーダー間信頼性に対応します。

- [Scholar Qualitative Toolkit](https://github.com/joshzyj/open-scholar-skill/tree/HEAD/.claude/skills/scholar-qual) - グラウンデッド・セオリー、省察的主題分析、内容分析を、コードブックの作成とコーダー間信頼性の確認とともに実行します。NVivo、ATLAS.ti、Dedoose、MAXQDA の形式に書き出せます。

- [Thematic Analysis](https://github.com/keemanxp/thematic-analysis-skill/tree/HEAD/thematic-analysis) - Braun と Clarke の6段階の枠組みに従い、インタビュー、フォーカスグループ、自由記述の回答をテーマにコーディングします。事前に行う4つの分析上の決定と、15項目の品質チェックリストを扱います。

## 解釈可能性

*学習済みモデルの中を見て何を計算しているかを調べ、個々の予測を説明します。*

- [nnsight](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/nnsight) - 任意の PyTorch モデルの内部を調べて操作します。ローカルの GPU には大きすぎるモデルに対して、NDIF 経由でリモート実行することもできます。

- [pyvene](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/pyvene) - 宣言的な辞書ベースの介入フレームワークを通じて、PyTorch モデルに対する因果トレース、アクティベーションパッチング、交換介入学習を行います。

- [SAELens: Sparse Autoencoders for Mechanistic Interpretability](https://github.com/NousResearch/hermes-agent/tree/HEAD/optional-skills/mlops/saelens) - スパースオートエンコーダを学習・分析し、多義的なモデルの活性を解釈可能な特徴に分解します。SAELens と TransformerLens のライブラリをラップしています。

- [SHAP](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/shap) - ゲーム理論に基づく特徴量の寄与度で機械学習の予測を説明し、監査します。explainer と masker の選択、寄与度の計算と検証、多出力の説明、局所・大域の可視化を扱います。

- [TransformerLens](https://github.com/Orchestra-Research/AI-Research-SKILLs/tree/HEAD/04-mechanistic-interpretability/transformer-lens) - モデルのすべての活性に設けたフックポイントを通じて、アテンションのパターンを調べ、アクティベーションパッチングの実験を行い、Transformer が実装するアルゴリズムをリバースエンジニアリングします。

## 論文品質の作図と可視化

*結果から描くグラフを、ジャーナルや会議が求める水準で作成します。*

- [Archora: Figure](https://github.com/richard-kim-79/archora-skills/tree/HEAD/skills/figure) - 研究用の図のために実行可能な Matplotlib/Seaborn/mermaid コードを生成し、定量的な図と概念図の選び方のガイドも付けます。

- [Figures4Papers](https://github.com/ChenLiu-1996/figures4papers/tree/HEAD/scientific-figure-making) - 棒グラフ、推移図、散布図、ヒートマップ、複数パネルのレイアウトなど、そのまま掲載できる Matplotlib の図を固定の統一スタイルで作成します。AI 系の会議・論文誌への投稿に向けた印刷・ベクター出力の慣行に従います。

- [Map Research Sites](https://github.com/Revonia-gh/evidence-first-research-skills/tree/HEAD/.agents/skills/map-research-sites) - 表形式の経度・緯度データを検証し、再現可能な SVG の調査地点地図を描画します。行ごとに公開、概略化、制限のいずれかの公開方針を適用し、座標を丸めます。

- [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/HEAD/skills/nature-figure) - Python または R で、インパクトの高い雑誌向けの投稿品質の科学的な図を作成、修正、監査します。複数パネルと、ジャーナルの要件に合った書き出しに対応します。

- [Nature Paper Skills: Figure Planner](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/figure-planner) - 原稿の図の構成を計画し、監査します。1つの図に1つの主張という原則を徹底し、各パネルに役割を割り当て、図の説明文や結果の本文を書く前に本文か補足資料かを決めます。

- [PaperOrchestra: Plotting Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/plotting-agent) - 実験データとアウトラインから、学術論文用の掲載品質の図と概念図を生成します。視覚言語モデルによる批評を使った改善は任意です。

- [Tufte Data Viz](https://github.com/caylent/tufte-data-viz) - データインク比、直接ラベル、レンジフレームの軸といった Edward Tufte のデータ可視化の原則を、複数の作図ライブラリにわたって学術的な作図に適用します。

## 執筆と投稿

*原稿を起草し、投稿できる状態にします。構成、書式、投稿先への適合、提出前のセルフチェックが対象です。*

- [Academic Presentations & Demo Video](https://github.com/OpenLAIR/dr-claw/tree/HEAD/skills/making-academic-presentations) - 論文をスライドに変換し、必要に応じてナレーション付きのデモ動画も作成します。台本の作成、スライド生成、音声合成によるナレーション、動画の組み立てを扱います。

- [CCF Paper Writer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-writer) - CCF ランクの会議・論文誌向けに論文の本文を計画、起草、改訂し、投稿先に合わせて調整します。ユーザー自身のアイデアの範囲とエビデンスは変えません。

- [Conference Poster Builder](https://github.com/K-Dense-AI/scientific-agent-skills/tree/HEAD/skills/pptx-posters) - 著者が承認したローカルの内容から、編集可能な学会ポスターを作成します。実寸、印刷上の制約、アクセシビリティ、素材の出所、書き出しの準備状況を確認します。

- [DOCX Skill for Chinese Papers](https://github.com/gostyan/docx-skill-4-cn-paper/tree/HEAD/docx-editor-cn) - 三線表や独立数式など、中国語の学術文書の書式慣行に沿って .docx ファイルを作成、編集します。

- [Econ Writing Skill](https://github.com/hanlulong/econ-writing-skill/tree/HEAD/skills/econ-write) - 50以上のスタイルガイドにある経済学の文章作法を実行可能なルールにまとめ、経済学論文の起草と改訂に使えるようにします。

- [Grant Proposal Skill](https://github.com/borghei/Claude-Skills/tree/HEAD/research/grants) - 学術研究の助成金申請書について、構成の設計、助成機関との適合性の評価、予算設計を導きます。

- [Journal Adapt Writing Skill](https://github.com/wantongc/journal-adapt-writing-skill/tree/HEAD/skill) - 参照コーパスを分析し、原稿をセクションごとに改訂することで、学術原稿を投稿先ジャーナルの文章の慣行に合わせます。

- [LaTeX Document Skill](https://github.com/ndpvt-web/latex-document-skill) - 学術的な執筆のための LaTeX 文書の作成、コンパイル、形式変換、文書分析を扱います。

- [LaTeX Thesis (Chinese)](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/latex-thesis-zh) `zh` - 中国語の LaTeX 学位論文に取り組む大学院生を支援します。コンパイルの診断、GB/T 7714 の参考文献書式、構成のレビュー、ブラインド審査向けの匿名化を扱います。

- [Nature Paper Skills: Submission Audit](https://github.com/boom5426/nature-paper-skills/tree/HEAD/skills/core/submission-audit) - 投稿または再投稿の前に、原稿の最終段階の事前点検を行います。主張、図、図の説明文、方法、補足資料を、投稿先の要件と突き合わせて確認します。

- [PaperFit: Float Optimizer](https://github.com/openraiser/paperfit/tree/HEAD/skills/float-optimizer) `zh` - 学術論文の LaTeX ソースにおけるフロートの配置の問題を修正します。最初の参照箇所からの距離、幅の不一致、集中、孤立したページが対象です。

- [PaperFit: Overflow Repair](https://github.com/openraiser/paperfit/tree/HEAD/skills/overflow-repair) `zh` - LaTeX のはみ出しの問題（overfull box、長い数式、URL のはみ出し）を修正します。まずレイアウトだけの編集から始め、それで収まらない場合は文言の書き換えを委任する段階に進みます。

- [PaperOrchestra: Outline Agent](https://github.com/Ar9av/PaperOrchestra/tree/HEAD/skills/outline-agent) - 生の研究資料を、作図計画、文献検索計画、セクション計画を含む構造化されたアウトラインに変換します。学術論文の執筆向けです。

- [PhD Skills: Paper Verification](https://github.com/fcakyon/phd-skills/tree/HEAD/plugin/skills/paper-verification) - 数値の正確さ、用語の一貫性、数式とコードの対応の確認を通じて、論文の主張をコードとデータに照らして検証します。

- [Post-Publication Corrector](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/post-publication-corrector/skills/post-publication-corrector) - 出版済みの論文で確認された誤りを、著者訂正（corrigendum）、出版社訂正（erratum）、懸念表明、撤回のいずれかに分類し、共著者への通知、編集者への依頼、公開する告知を起草します。

- [Research Disseminator](https://github.com/yaotingsun/academic-publishing-skills/tree/HEAD/plugins/research-disseminator/skills/research-disseminator) - 出版済みの論文を、平易な言葉の要約、グラフィカルアブストラクトの構想、各プラットフォームに合わせた SNS 用の文面に変換します。どの版も、論文の結果が実際に裏づける範囲を超えないようにします。

- [Research Paper Writing Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/HEAD/research-paper-writing) - ML/CV/NLP 論文の改訂を導きます。段落単位の明確さの確認、リバースアウトライン、トピックセンテンスの整理、主張とエビデンスの対応の監査を行います。

- [Skill Deslop](https://github.com/stephenturner/skill-deslop) - 学術・研究の文章から、AI が書いた文章によくあるパターンを取り除き、より自然な文体に戻します。

- [Survey Writer](https://github.com/chtc66/academic-skills/tree/HEAD/survey-writer) `zh` - 研究トピックについてサーベイ論文の草稿を書きます。複数の論文を、論文ごとの要約ではなく、問題を軸に手法の発展をたどる流れに整理します。

- [Typst Paper](https://github.com/bahayonghang/academic-writing-skills/tree/HEAD/academic-writing-skills/typst-paper) - 既存の Typst 原稿について、コンパイル、投稿先の書式、文法、参考文献、投稿準備の確認を支援します。

## 査読と反論

*投稿のもう一方の側面です。他者の原稿の査読と、自分の原稿への査読コメントへの回答を扱います。*

- [Academic Paper Reviewer](https://github.com/Imbad0202/academic-research-skills/tree/HEAD/academic-paper-reviewer) - 分野別の査読者ペルソナ5名による国際ジャーナルの査読パネルを模擬し、構造化された編集判定と改訂ロードマップを出力します。

- [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch/tree/HEAD/workflows/anti-autoresearch) - 査読者の立場から論文の研究公正性を検証します。原文の該当箇所に紐づく証拠台帳を作り、複数モデルの監査器で引用、実験、一貫性、ベースライン比較の捏造を調べ、人間の査読者向けに決定的な判定を算出します。

- [CCF Paper Reviewer](https://github.com/mikubaka88/CCFA-Skills/tree/HEAD/ccf-paper-reviewer) - CCF または投稿先の基準に沿って、新規性、妥当性、エビデンス、文章の質、書式の遵守の観点から原稿を査読し、査読者とエリアチェアのパネルを模擬します。

- [Econ Paper Review](https://github.com/hanlulong/econ-paper-review-skill/tree/HEAD/econ-review) - 経済学論文に対して査読者水準のレポートを作成します。識別戦略、統計的推論、表、数式、参考文献を確認し、指摘事項の台帳と優先順位付きの改訂計画を出力します。

- [Paper Lifecycle: Rebuttal Response](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/rebuttal-response) - トリアージ、戦略、起草、トーン修正の各モードを通じて、査読コメントをエビデンスに基づく反論資料一式に変換します。

- [Paper Lifecycle: Review & Revision](https://github.com/M1n-n9/paper-lifecycle/tree/HEAD/review-revision) - 学術原稿のための構造化されたレビューと改訂のワークフローです。作業量に応じた6つの動作モードがあります。

## 各項目の確認方法

これはキュレーションしたリストであり、認証ではありません。各項目は、人が `SKILL.md` を読んだうえで選んでいます。説明文はそのスキルが何をするかを述べたもので、あなたの課題に対して最初から最後まで実行した結果の報告ではありません。実行可能なエンドツーエンドのテストを行ったと主張する項目は1つもありません。実際に行っていないからです。`SKILL.md` が英語以外で書かれている項目には、名前の横に言語タグを付けています。

**確認は2段階です。** `static check`（142 件中 96 件）は、パス、ライセンス、コミット日、必要な権限や環境を実際のリポジトリで確認し、`SKILL.md` を読んだことを意味します。`audited`（142 件中 46 件）は、それに加えて、文書化した監査仕様に沿ってスキル自身の指示を同梱ファイルと照らしながら手順どおりにたどり、次のいずれかの判定を得たことを意味します。`works`、`works with caveats`（目的は果たせるが、事前に知っておくべき条件がある）、`unverifiable`（認証情報、有料アクセス、ハードウェアがないと評価できない）。監査の結果、読むかぎりは良さそうでも作者本人以外には動かせない項目を削除してきました。

**ライセンス、スター数、権限や環境のフラグ、項目ごとの確認状況は、このページの各行ではなく、機械可読のインデックスにあります。** [`index.json`](index.json) と [`index.csv`](index.csv) で、このページと同じデータから生成しています。スキルのライセンス、ネットワーク・認証情報・フックが必要かどうか、正確な監査判定が気になる場合は、開く前にそこで調べてください。要点だけ述べると、スキル自身のフロントマターにある `license:` とリポジトリの LICENSE が食い違う場合は前者を優先します。`repo ★N` はその*リポジトリ*のスター数であり、スキル自体の評価ではありません。これらのスキルの 94% は他者のより大きなリポジトリの中にあるため、スター2万のモノレポにあるスキルでも、一度コミットされたきり誰にも使われていないことがあります。

すべての項目に対して行っている構造面の確認（中身があるか、テンプレートの量産品でないか、リポジトリを確認できるか）は分野によらず、このリストが保証するのはその部分です。臨床試験、質的コーディング、計量経済学などのスキルが*あなたの分野で方法論的に正しいか*は、ここに含まれるすべての分野についてキュレーターが判断できることではありません。各分野の項目は、専門家の審査を経たものではなく、自分で評価するための手がかりとして扱ってください。

## コントリビュート

[CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。このリストはデータから生成しているため、README を手で編集しないでください。
