# GRAVITY モード仕様書

## 概要
ブロックの「地面」が画面中央にあり、中央の軸から上下両方向にブロックが生えるモード。従来の下積み上げと異なり、視線が上下に分散するため瞬間認識の難易度が自然に上がる。EASY〜ULTIMATEまで全難易度で成立する第3モード。

## コア機能一覧

| # | 機能名 | 説明 | 優先度 |
|---|--------|------|--------|
| 1 | GRAVITYステージ生成 | 各難易度のGRAVITY版ステージデータを生成 | Must |
| 2 | 上下分裂ブロック描画 | 各列のブロックを上半分・下半分に分割して中央から生やす | Must |
| 3 | パネル4追加 | スワイプUIの第4パネルにGRAVITY難易度タブ+ステージマップ | Must |
| 4 | 解放条件 | 各難易度のPlus全10面クリアでGRAVITY解放 | Must |
| 5 | 難易度カラー | GRAVITY用の色定義（既存と区別できる色調） | Must |
| 6 | 進捗保存 | GRAVITY進捗をlocalStorageに保存 | Must |
| 7 | カードドロップ対応 | GRAVITYステージでもカードがドロップする | Should |

## スプリント計画

### Sprint 1: ステージ生成 + ブロック描画
**ゴール:** GRAVITYモードでブロックが上下に生えるレンダリングを実装
**機能:**
- [ ] makeGravityStages()関数: Plus同様に基本ステージから派生。bag値は+版と同等、gravity:trueフラグ付き
- [ ] STAGES['EASY▲']〜['ULTIMATE▲']の5難易度分を生成（命名: 難易度名+▲記号）
- [ ] renderBlocks()にgravityレイアウト分岐: 各列のブロック数hを上半分(ceil(h/2))と下半分(floor(h/2))にランダム分割。上はflex-direction:column（天井から下へ）、下はflex-direction:column-reverse（床から上へ）。中央に2pxの軸線を表示
- [ ] DC色定義: 既存色のネオン/反転バージョン
**受け入れ基準:**
- GRAVITYステージでブロックが中央から上下に分かれて表示されること
- ブロック合計数が正しいこと（上+下=元の列高さ）
- 全難易度でレイアウトが崩れないこと

### Sprint 2: UI統合（パネル・タブ・解放）
**ゴール:** GRAVITYモードにUIからアクセスできるようにする
**機能:**
- [ ] Panel 3のHTML追加: gravity-tabs + gravity-scroll + gravity-stage-list
- [ ] pi-dot-3の追加、パネルナビゲーション更新
- [ ] gravityUnlocked()関数: 該当難易度のPlus全10面クリアで解放
- [ ] switchTab()のGRAVITY対応
- [ ] renderMap()のGRAVITY対応（gravity-stage-listに描画）
- [ ] 進捗保存: prog['EASY▲']等をlocalStorageに含める
- [ ] カードシステム: GRAVITY難易度のカードカタログ追加（ENEMIESは通常版を共有、hue-rotate+invertで視覚区別）
**受け入れ基準:**
- スワイプでPanel 3にアクセスできること
- Plus全クリア後にGRAVITYタブが解放されること
- ステージ進行・クリア・星評価が正常に動作すること

## UI/UX 要件

### ブロック描画
```
従来（下積み上げ）:        GRAVITY（中央分裂）:
                           ■
  ■                        ■ ■
  ■ ■                      ■ ■ ■
  ■ ■ ■                  ──────── 軸線
  ■ ■ ■                    ■ ■ ■
─────────                   ■ ■
  地面                        ■
```

### パネル構成
- Panel 0: メニュー（既存）
- Panel 1: 通常ステージ（既存）
- Panel 2: +ステージ（既存）
- Panel 3: ▲ステージ（新規）

### 難易度命名
▲記号を使用: EASY▲, NORMAL▲, HARD▲, EXTREME▲, ULTIMATE▲

### 難易度カラー（ネオン系で区別）
- EASY▲: #00E676（ネオングリーン）
- NORMAL▲: #00B0FF（ネオンブルー）
- HARD▲: #FF6D00（ネオンオレンジ）
- EXTREME▲: #FF1744（ネオンレッド）
- ULTIMATE▲: #D500F9（ネオンパープル）

## 非機能要件
- low-endデバイスでもGRAVITYレイアウトがスムーズに描画されること
- 既存モード（通常/+）の動作に影響しないこと

## 制約事項
- GRAVITY版の11面（true_final）はスコープ外（通常版・+版と同様に後から追加可能）
- GRAVITY専用の背景SVGはスコープ外（+版と同じ背景を流用）
- GRAVITY専用のカードアートはスコープ外（hue-rotate+invertで自動色変え）
