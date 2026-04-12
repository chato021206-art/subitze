# 評価レポート: retry サポート維持バグ修正 + spec ドロップ率調整

**判定:** 条件付き合格（CONDITIONAL PASS）
**評価日:** 2026-04-13
**評価対象:** 作業ツリーの未コミット変更（`stage.html` +6/-3, `docs/spec.md` +1/-1）

## スコア

| 基準 | スコア | 閾値 | 判定 |
|------|--------|------|------|
| 機能完全性 | 5/5 | 4 | PASS |
| 動作安定性 | 5/5 | 4 | PASS |
| UI/UX品質 | 4/5 | 3 | PASS |
| エラーハンドリング | 4/5 | 3 | PASS |
| 回帰なし | 5/5 | 5 | PASS |
| 仕様/コード整合性 | 3/5 | 4 | **FAIL** |

## 変更の要約

### 1. `stage.html`: `startStage(d, idx, keepSupport)` 追加
- `retryStage(fromFail)` が `_supportMode/_supportLeft/_supportUsed` を予約してから `startStage` を呼ぶが、従来の `startStage` 冒頭で無条件に 3 変数をリセットしていたため、**ミス後リトライの「やさしさサポート」が一度も発動していなかった**。
- 修正: `startStage` に `keepSupport` 引数を追加し、`true` のときはリセットをスキップ。`retryStage` は `fromFail === true` を渡すように変更。

### 2. `docs/spec.md`: 通常ステージのドロップ率 20% → 15%

## 機能テスト（コードトレース）

### 受け入れ確認
- **ミス後の「もう一回」ボタンでサポートが発動するか**
  - `fail-overlay` の retry: `retryStage(true)` → `_supportMode=true, _supportLeft=2, _supportUsed=true` → `startStage(curDiff, curIdx, true)` → `if(!keepSupport)` ブロック skip → サポート状態維持 ✅
- **クリア後の「もう一回」では発動しないか**
  - `result-overlay` の retry (stage.html:1837): `retryStage()` → `fromFail=undefined` → `fromFail===true` は `false` → `keepSupport=false` → リセット ✅
- **マップからの新規ステージ開始時にサポートが残存しないか**
  - stage.html:3832 の唯一の外部呼び出しは `startStage(d, idx)` (2引数) → `keepSupport=undefined` → リセット ✅
- **2 回目以降のミス後リトライ**
  - `_supportUsed=true` のためサポートは再発動しないが、`keepSupport=true` で現在状態（残数 0 等）が維持される。仕様「1ステージ1回限り」に整合 ✅

### 回帰チェック
- `startStage` 呼び出し箇所は `grep` で 3 か所のみ：宣言(3964) / マップノード(3832) / retryStage(6074)。マップノード経由は 2 引数のため挙動不変 ✅
- `taMode/survivalMode/drillMode/brainMode` の早期 return は `startStage` を経由しないので影響なし ✅
- `_supportUsed` の他参照は宣言(6049)・初期化(3969)・retryStage(6064) のみ。スコープ違反なし ✅

## 不合格項目

### [Major] spec.md と CARD_DROP_RATES の不整合
- `docs/spec.md:47` を「通常ステージ クリア 15%」に変更したが、`stage.html:2130` の実装は依然 `{ common: 0.20, uncommon: 0.20, rare: 0.20 }` のまま。
- **そもそも以前の spec（20% / 12% / 8%）と実装も乖離していた**（実装は全レアリティ一律 0.20）。今回の編集は spec 側だけを変えたため、ズレがさらに広がった。
- 期待される動作: 仕様と実装が一致するか、片方をもう一方に合わせる。
- 再現手順: `grep -n "CARD_DROP_RATES" stage.html` → 0.20 が並んでいるのを確認。

## バグ一覧

| # | 重要度 | 内容 | 再現手順 |
|---|--------|------|----------|
| 1 | Major | spec の通常ドロップ率(15%) と実装(0.20) が不一致。Mid-Boss/Final Boss も実装は一律 0.20 で spec の 12%/8% を満たさない | `stage.html:2130` を確認 |

## Generator への指示

1. **ドロップ率の整合を取る**: `CARD_DROP_RATES` を `{ common: 0.15, uncommon: 0.12, rare: 0.08 }` に修正するのが spec.md との最短整合。意図的に「全レアリティ 20%」運用にしているのであれば、spec.md 側を実装に合わせて書き戻すこと。どちらを採用するかユーザー判断を仰いでよい。
2. **コミット前の確認**: `rollCardDrop` が参照する `card.rarity` の値域（`common/uncommon/rare`）が `CARD_CATALOG` 構築側で正しく設定されているかも併せて検証してから値を変えること。

## 改善提案
- `startStage` の `keepSupport` 引数は名前が局所的すぎる。今後 retry 時にだけ維持したい状態が増えると引数が肥大化するので、将来的には `_pendingSupport` のような外部フラグで管理する方が拡張しやすい（今回の修正範囲としては許容）。
