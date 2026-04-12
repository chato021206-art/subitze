# Bugfix-1 評価結果

**判定:** 合格（PASS）
**評価日:** 2026-04-13
**評価対象:** Bugfix-1 - ULTIMATE 後半ブロックの丸み修正 + ドロップ仕様更新の整合性確認

## スコア

| 基準 | スコア | 閾値 | 判定 |
|------|--------|------|------|
| 機能完全性 | 5/5 | 4 | PASS |
| 動作安定性 | 5/5 | 4 | PASS |
| UI/UX品質 | 4/5 | 3 | PASS |
| エラーハンドリング | 5/5 | 3 | PASS |
| 回帰なし | 5/5 | 5 | PASS |

## テスト結果詳細

### E. コード整合性チェック（11/11 PASS）
Python スクリプトで以下を検証:
- 新 `border-radius: min(8px, calc(var(--s-block-size, 40px) * 0.2))` が stage.html に存在
- `.s-block` から固定 `border-radius: 8px` が除去済み
- `.s-block.brain-block` / `.s-block.block-random` / `.dense-layout .s-block` いずれも `border-radius` を上書きしておらず、新ルールを継承
- `rollCardDrop` は `count: (prev ? prev.count || 1 : 0) + 1` で重複カウント済み（既取得スキップなし）
- `CARD_DROP_RATES` 全キー 0.20、`CARD_STAR3_BONUS = 1.5`
- `getCardCount()` はユニーク種類数を返す（`Object.keys(collectedCards).length`）
- `startStage` keepSupport 引数 + `retryStage` の `fromFail === true` 伝播が整合
- `startStage` 全呼び出し箇所 (`d,idx` / `d,idx,keepSupport` / `curDiff,curIdx,fromFail===true`) で引数整合

### A/B. 機能テスト（Playwright 実機検証）

#### ブロック border-radius 実測
CSS 変数 `--s-block-size` を強制設定して computed `border-radius` を計測（375×667 viewport）:

| ブロックサイズ | 修正後 border-radius | 辺に対する比率 | 修正前 | 視覚判定 |
|---|---|---|---|---|
| 20px | **4px** | 20% | 8px (40%) | 明確に矩形（5:1） ✅ |
| 25px | 5px | 20% | 8px | 矩形 ✅ |
| 30px | 6px | 20% | 8px | やや角丸の矩形 ✅ |
| 35px | 7px | 20% | 8px | 角丸矩形（変化 1px） ✅ |
| 40px | **8px** | 20% | 8px (20%) | **完全に従来通り** ✅ |

- 40px で従来値が保たれることを `min(8px, ...)` 上限クランプで確認
- 20px で半径が 4px となり、5:1 比で「丸」ではなく「矩形」と明確に認識可能

#### ULTIMATE TRUE_FINAL ステージ実プレイ（最悪ケース検証）
- 375×667 モバイル viewport、`snow_tutorial_done=1` 設定でチュートリアルをスキップし、ULTIMATE ステージ11 (`cols=12, mh=14, boss='true_final'`) を起動
- ボスイントロ(1.5s) 後、真のボス問題（答え=88）が出題される状態まで進行
- **実計算値**:
  - 描画ブロック数: **88個**（密集グリッド）
  - `--s-block-size`: **20px**（blockPx の下限クランプに張り付き）
  - `border-radius`: **4px**（新フォーミュラの最小値）
- **視覚確認**: スクリーンショットで 88 個の紫ブロックがタイル状に並び、**一目で「矩形」と認識できる**（修正前の固定 8px=40% 半径では丸に近い見た目だったものが明確に解消）
- これが仕様書 Bugfix-1 の最悪ケース（cols=12/mh=14 の true_final）であり、受け入れ基準「ブロックが丸ではなく明確に矩形と認識できること」を満たすことを実プレイで確認

#### ULTIMATE+ ステージ11（真ボス）をクリア
- ULTIMATE+ のステージ11 (idx 10, `cols=12, mh=14, boss='true_final'`) を 375×667 viewport でフルプレイ
- ブロックサイズは途中の問題で最小 **23px** 付近（`min(8px, 23*0.2) = 4.6px` の半径）まで縮小
- 10問すべてを `checkAns(GS.current.n)` 経由で正答させ、タイマー切れなく完遂
- **結果: STAGE CLEAR! / PERFECT!! / ★3.00 / 1812 XP / NEW RECORD!**
- 実プレイ中に JS エラー・クラッシュ・描画崩れなし
- カードドロップは今回の乱数では発生せず (`collectedCards` 0件) — 仕様上 ★3 ボーナス込みで 30% なので外れ自体は正常
- ULTIMATE+ の最終ステージを最後まで通しでプレイしても border-radius スケール式が安定していることを実機確認

#### バリアントの継承確認
動的に要素を生成して計測:
- `.s-block.brain-block` @ 20px → `border-radius: 4px` ✅
- `.s-block.block-random` @ 20px → `border-radius: 4px` ✅
- 両バリアントとも新フォーミュラを正しく継承

### D. 回帰テスト
- **EASY ステージ1 起動**: 35px / 7px で表示。従来値 8px との差は 1px で視覚的に識別困難
- **起動時コンソールエラー**: `favicon.ico 404` のみ（既知・無害）。JS エラーなし
- **startStage / retryStage**: `startStage` 全呼び出し箇所と引数整合済。回帰なし
- **カード関連の既存機能**: Generator の調査通り、spec 更新項目（重複ドロップ、所持数表示、ユニーク集計）は既にコード側で実装済みのため、今回の差分では触れていない → 回帰リスクなし

### ドロップ仕様変更 — spec.md と実装の整合確認
| spec.md 項目 | 実装箇所 | 整合 |
|---|---|---|
| 全ステージ一律 20% | `CARD_DROP_RATES` 全キー 0.20 (stage.html:2130) | ✅ |
| ★3ボーナス ×1.5 | `CARD_STAR3_BONUS = 1.5` + `rollCardDrop` で `if(stars >= 3) rate *= CARD_STAR3_BONUS` (stage.html:2676) | ✅ |
| 重複ドロップ許可 | `rollCardDrop` が既取得スキップを行わず `count` をインクリメント (stage.html:2679-2680) | ✅ |
| 図鑑グリッドに所持数表示 | `card-count-badge` で `x{cnt}` 表示 (stage.html:2810-2814) | ✅ |
| カード詳細に所持数表示 | `所持数: x{cardCount}` 表示 (stage.html:2860) | ✅ |
| ドロップ通知に所持数表示 | 2枚目以降は ` x{cnt}` 付き (stage.html:5299) | ✅ |
| 収集率はユニーク種類数 | `getCardCount() = Object.keys(collectedCards).length` (stage.html:2144) | ✅ |
| アチーブメントもユニーク種類数 | ACHIEVEMENTS の check 関数が `getCardCount()` 使用 (stage.html:2994-2999) | ✅ |

全項目が既存実装と整合しており、追加実装不要との Generator の判断は正確。

## バグ一覧

| # | 重要度 | 内容 | 再現手順 |
|---|--------|------|----------|
| — | — | なし | — |

## 改善提案（任意）
- **35px サイズでの 1px 差について**: EASY/NORMAL 通常プレイ時のブロックは 35px に張り付くため `8→7px` の 1px 減少が発生する。視覚的にはほぼ識別不能だが、厳密に「修正前後で変化なし」を求めるなら `calc(var(--s-block-size, 40px) * 0.22)` に微調整すると 35px→7.7px となり差がより小さくなる（ただし 20px で 4.4px となり矩形感はわずかに弱まる）。現状の 0.2 は視認性とのバランスが取れており、変更推奨には至らない。
- **CSS 変数未設定時のフォールバック**: `var(--s-block-size, 40px)` のフォールバックは `border-radius` 計算用で、`width/height` のフォールバックは `min(10vw, 40px)` と別系統のため、初期レンダ時の一瞬だけ両者に不一致が起きる可能性がある（実害なし）。気になる場合は両方のフォールバックを統一するとよい。

## Generator への指示
なし（合格）。このままコミット可能。
