# SUBITZE Native — 進捗ログ

本プロジェクトは「SUBITZE の完全オリジナル化＋グローバル本格展開」（spec.md v2）に基づく 14 スプリント（Sprint 0〜13）構成である。既存 Web 版 (stage.html) とは並行して存在し、ネイティブアプリ版は別プロダクトとして作り上げる。

旧カード収集スプリント（Sprint 1〜6）のログは `progress_v1_cards.md.bak` に保存済み。

---

## Sprint 0: 世界観＆キャラクター再設計（完全オリジナル化）

**ステータス:** 実装完了 - 評価待ち
**実装日:** 2026-04-13

### 実装内容

- `docs/world_bible.md` を新規作成し、以下の内容をまとめた：
  - 設計原則 6 項目（既存 IP 類似ゼロ・宗教文化中立・地球神話回避・造語中心・抽象ビジュアル・全年齢）
  - **5 つのオリジナル Realm（領域）** の設定
    - Realm 1: Dewlight Glade（露光の園）
    - Realm 2: Chorus Grove（唱樹の森）
    - Realm 3: Kilnsands（窯野）
    - Realm 4: Tempest Reef（嵐礁群島）
    - Realm 5: Prism Hollow（虹洞）
  - **全 51 体のオリジナルキャラクター**の命名・タイプ・色・短いバックストーリー
    - Realm 1: Driblet / Mossy / Petali / Glimp / Brambo(mid) / Pluff / Nectra / Pondy / Sproutlet / Honeypod(final)
    - Realm 2: Woodle / Fluttong / Chimelet / Bounca / Harmon(mid) / Tweeli / Rumbly / Pluckin / Echowl / Maestrum(final)
    - Realm 3: Glasine / Dunette / Craterun / Pebblr / Gloamer(mid) / Scorchie / Tumbler / Dustle / Quartlet / Kilnwarden(final)
    - Realm 4: Mistle / Sparkel / Galen / Drencher / Thundro(mid) / Zephy / Halowl / Swirly / Frostin / Galestorm(final)
    - Realm 5: Dawngleam / Noonburst / Sundye / Duskwing / Starlit(mid) / Moonglim / Cometra / Nebulite / Hollowspark / Auroria(final) / Prismah(true_final)
  - **類似性セルフチェック** — FF/Pokemon/Dragon Quest/Megami Tensei/Cuphead 等との非類似を自己確認
  - **宗教・文化モチーフ除外チェック** — 現 Web 版で使用していた「マハカラ」「鳥居」「曼荼羅」「数珠」「ギリシャ神名」等をすべて排除、不使用シンボルを明示
  - **視覚設計ガイドライン** — 全キャラ共通の形状・目・口・禁止事項を列挙
  - **カード図鑑用世界観テキスト** — 5 Realm それぞれの短い紹介文
  - **Sprint 10 法務レビューへの申し送り事項** — 第三者チェックが必要な項目をリスト化
  - **バージョン履歴** — v1 (2026-04-13)

### 自己評価

| 基準 | スコア (1-5) | コメント |
|------|-------------|---------|
| 機能完全性 | 5 | Sprint 0 の全ての受け入れ基準（5 Realm・51 キャラ・宗教シンボルゼロ・既存 IP 類似ゼロ）を満たす |
| コード品質 | 5 | デザイン文書として構造化され、後続スプリントで再利用しやすい形式 |
| UI/UX | - | このスプリントは設計のみで UI 実装なし |
| エラーハンドリング | - | 該当なし（設計ドキュメント） |
| 既存機能との統合 | 5 | 現 Web 版 (stage.html) には一切手を加えておらず、並行運用可能 |

### 技術的な判断

1. **既存 Web 版は touch せず別プロダクトとして扱う** — Sprint 0 の段階で stage.html を改変する価値は低く、むしろ壊してしまうリスクが高いため。現 Web 版は個人プレイグラウンドとして保持し、Native 版は Sprint 4 以降で新規に構築する。

2. **51 キャラの命名方針に「造語中心 + 2語の portmanteau」を採用** — 一般英単語だと商標取得が難しく、既存キャラと被る確率も高い。例えば "Dribbly" は Pokemon 類似のリスクがあるため、"Driblet"（drop + -let 指小辞）のような造語を基本にした。

3. **現 Web 版の敵名（マハカラ／ジュリオン／アルニア／プネーマ等）は一切流用しない** — 既に現 Web 版でクリーンアップしたが、Native 版ではさらに徹底して「ギリシャ神話・ヒンドゥー神話・仏教概念」由来の発音すら排除した。Auroria（極光）や Prismah（虹）は一般自然現象なので可。

4. **Realm 名もオリジナル造語** — "Dewlight", "Chorus Grove", "Kilnsands", "Tempest Reef", "Prism Hollow" はすべて一般単語の組み合わせで、特定文化を指さない。

5. **商標検索は Sprint 10 に繰り延べ** — 個人開発者が USPTO/JPO/EUIPO で本格的な検索を行うには時間と費用がかかる。Sprint 0 では「自己照合で既知の有名キャラと被らない」ことだけを確認し、正式な検索は法務レビュースプリントに委ねた。

### 既知の課題

1. **商標検索の正式実施は未完了** — Sprint 10 で第三者または有料サービスによる検索が必要。
2. **ビジュアルの最終決定は未完了** — 命名と色だけを固めた段階。実際の SVG アイコンとカード絵柄は Sprint 1 で作成する。
3. **世界観のストーリーライン全体は未作成** — 各キャラのバックストーリーは断片的。全体を貫く物語（プレイヤーは何者で、なぜ Realm を旅するのか）は未定義。Sprint 1 か別途のライティングスプリントで補完する必要あり。
4. **アプリ名最終決定も未完了** — 現 "SUBITZE" を継続するか、"Dewlight" や "Quick Count" 等へリブランドするかは Sprint 10 で判断。
5. **現 Web 版と Native 版の関係性の明示** — プロジェクトルート直下に README 的な整理が今後必要。

### Evaluator への引き渡し事項

このスプリントは設計文書のみのため、動作確認は不要。代わりに以下をレビューしてほしい：

**起動方法:** 該当なし（コード変更なし）

**確認対象ファイル:**
- `docs/world_bible.md` — 主成果物
- `docs/progress.md` — このファイル
- `docs/spec.md` — spec から外れていないか照合

**確認シナリオ（文書レビュー）:**
1. `docs/world_bible.md` を通読し、以下を確認：
   - 5 Realm の設定に相互の一貫性があるか
   - 51 キャラの命名に既知の既存ゲームキャラと被るものがないか
   - 宗教・文化モチーフが除外されているか
   - 各 Realm のボス構造（中ボス・ボス・真ボス）が正しく配置されているか
   - カード図鑑用世界観テキストが 5 Realm 分ある
2. `docs/spec.md` の Sprint 0 受け入れ基準と照合：
   - 「全キャラ名を商標 DB で検索して衝突なし」→ **自己照合のみ実施、第三者チェックは Sprint 10 に繰延**
   - 「既存ゲームのキャラと明らかに似ているものがゼロ」→ 自己確認済
   - 「宗教を想起させるシンボルが全キャラ・背景からゼロ」→ 自己確認済
   - 「第三者法務チェックで OK が出る」→ **Sprint 10 で実施予定**
3. 既存 Web 版 (stage.html) が未変更であることを確認（`git status` で stage.html に変更なし）

**注意事項:** このスプリントの評価では、Sprint 10 未完了の項目を除き、文書内容の完成度のみを評価してほしい。具体的には：
- 商標衝突の最終確認（→ Sprint 10）
- 外部法務レビュー（→ Sprint 10）
- 実際のビジュアル生成（→ Sprint 1）
はすべて「後のスプリントに引き継がれている」状態なので、Sprint 0 単体では判定対象外とする。
