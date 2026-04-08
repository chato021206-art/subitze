# SUBITZE プロジェクト

数の瞬間認識（Subitizing）をテーマにしたブラウザゲーム。
HTML/CSS/JS + Python（ステージ生成スクリプト）で構成。

## サブエージェント運用ルール

このプロジェクトでは `/plan` → `/generate` → `/evaluate` の3つのサブエージェントをパイプラインとして運用する。

### ワークフロー

```
/plan → spec.md（仕様書）
  ↓ ユーザー承認必須
/generate N → 実装 + sprint_N_report.md
  ↓
/evaluate N → sprint_N_evaluation.md
  ↓
  PASS → /generate N+1
  CONDITIONAL PASS → 修正 → /evaluate N 再実行
  FAIL → /generate N 再実行
```

### ファイル規約

| ファイル | 生成者 | 説明 |
|---------|--------|------|
| `spec.md` | Planner | プロダクト仕様書。唯一の信頼できる仕様ソース |
| `sprint_N_report.md` | Generator | スプリントN の自己評価レポート |
| `sprint_N_evaluation.md` | Evaluator | スプリントN の評価レポート |

- これらのファイルはプロジェクトルート直下に置く
- 各エージェントは自分の担当ファイルのみ書き込む。他エージェントのファイルは読み取り専用
- `spec.md` の変更は `/plan` 経由のみ。手動編集はユーザーのみ許可

### エージェント間の境界

**Planner（`/plan`）**
- 入力: ユーザーのアイデア（1〜4行）
- 出力: `spec.md`
- 禁止: 技術スタック・DB設計・API設計・ライブラリ選定などの実装詳細を書くこと
- 「何を作るか」だけに集中。「どう作るか」は Generator に委ねる

**Generator（`/generate`）**
- 入力: `spec.md` + スプリント番号
- 出力: 実装コード + `sprint_N_report.md`
- 必須: 前スプリントの `sprint_N_evaluation.md` が存在する場合、指摘事項を反映してから着手
- 禁止: 仕様にない機能の追加、複数スプリントの同時実装

**Evaluator（`/evaluate`）**
- 入力: `spec.md` + `sprint_N_report.md` + 実装コード
- 出力: `sprint_N_evaluation.md`
- 原則: Generator の自己評価を鵜呑みにしない。コードを独立に検証する
- 判定基準: PASS / CONDITIONAL PASS / FAIL

### 実装ルール

- 既存コードのスタイルに合わせる（インデント、命名規則、ファイル構成）
- 1スプリント = 1機能単位。小さく作って確実に動かす
- Playwright MCP が利用可能な場合、Evaluator はブラウザで実際の動作確認を行う
- コミットはスプリント単位で行う。コミットメッセージに `Sprint N:` プレフィックスを付ける

### 中断・再開

- パイプラインはどの段階でも中断・再開できる
- 再開時は `spec.md` と最新の `sprint_*_report.md` / `sprint_*_evaluation.md` を読めば状態を復元できる
- 途中でスプリント計画を変更したい場合は `/plan` で `spec.md` を更新する

### やってはいけないこと

- Planner が実装詳細を指定する（誤った技術判断が伝播する）
- Generator が Evaluator の指摘を無視して次スプリントに進む
- Evaluator がコードを直接修正する（修正は Generator の責務）
- ユーザーの承認なしに `spec.md` を変更する
- 1スプリントで多機能を詰め込む
