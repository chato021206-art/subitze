# Android低スペ端末パフォーマンス完全修正

## 概要
Android低スペ端末でのブロック描画カクつきを完全に解消する。監査で発見された8つの未対策箇所をすべて修正。

## 発見された問題と修正計画

### Sprint 1: CSS未対策箇所の一括修正

**修正項目:**
1. `.enemy-char`の`drop-shadow`がlow-endで無効化されていない
2. `enemyIdle`/`enemyIdleBoss`の連続アニメーションがlow-endで動き続ける
3. `.enemy-damage`のkeyframe内`brightness()`フィルタがlow-endで除去されていない
4. `.r-rating-bar-inner`のCSSトランジションがlow-endで即時表示されていない
5. マップ上の`.node-crown`や`.node-enemy-preview`のアニメーション/フィルタ
6. `.enemy-char.plus-enemy`のフィルタが依然4重

**受け入れ基準:**
- low-endデバイスで上記すべてのフィルタ/アニメーションが無効化されていること
- iPhoneや高スペAndroidでは今まで通り動作すること
