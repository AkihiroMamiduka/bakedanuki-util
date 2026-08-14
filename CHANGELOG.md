# Changelog

このプロジェクトの注目すべき変更は、このファイルに記録します。

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を参考にし、
バージョン番号は [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

## [0.2.0] - 2026-08-14

v0.1.0 以降の NodeOperator 基盤の改善に加え、Windows版 Maya 2025 / 2026 /
2027 向けのネイティブ C++ plug-in `bdUtilNodes.mll` を初めて同梱するリリースです。

### Added

- Windows版 Maya 2025 / 2026 / 2027 向けのネイティブ C++ plug-in
  `bdUtilNodes.mll` を追加。
  `double`、`double3`、`doubleLinear`、`doubleLinear3`、`doubleAngle` の算術・
  補間・範囲・条件・平均系ノードを追加。
- Quaternion / Euler の値、積、基底変換、Bend / Twist の分解・合成・制限を扱う
  ネイティブノードを追加。
- position、orientation、Bend / Twist の RBF weight / falloff weight と、
  RBF weight から TRS pose を合成する pose blend ノードを追加。
- ネイティブ plug-in の線形代数実装に Eigen 5.0.1 を追加し、配布物へ第三者
  ライセンスと notice を同梱。
- `Double2` / `Double3` / `Double4`、`Float2` / `Float3`、`Long2` / `Long3`、
  `Short2` / `Short3`、unit compound、`Quat` の snapshot value 型を公開 API に追加。
- `PlugOperator` に、接続先から接続元を指定する `connect_from()` と
  `disconnect_from()` を追加。接続元には `PlugOperator`、`"node.attr"`、
  `["node", "attr"]`、`("node", "attr")` を指定可能。
- Pyright による `nodes.create` / `nodes.existing`、plug、value 型の型・補完
  contract を追加。
- Maya versionごとのAPI versionをplug-in metadataへ登録し、Python package versionとの
  整合性を各Maya実行環境で検証するテストを追加。
- Autodeskから取得した固有Node ID block `0x00142680` - `0x0014277F` を、
  配布する全ネイティブノードへ割り当て。

### Changed

- scalar / compound attribute の型階層と値変換を整理し、公開 API の型注釈と
  IDE 補完を改善。
- NodeOperator のノード作成、plug 解決、値取得の処理を高速化。
- node class generator と生成 stub を、現在の型階層およびネイティブノードへ対応。

### Fixed

- `FltMatrix` と `longLongInt` attribute の値取得・設定が動作しない問題を修正。
- compound attribute の一部で不定な default value を生成する問題を修正。
- Maya command へ文字列ではなく `MPlug` を渡していた箇所を修正。

### Removed

- `PlugOperator` の接続・切断用演算子オーバーロード `__gt__()`、`__lt__()`、
  `__or__()`、`__ror__()` を削除。接続には `connect()` / `connect_from()`、
  切断には `disconnect()` / `disconnect_from()` を使用する。

## [0.1.0] - 2026-07-24

`bakedanuki-util` の最初の公開リリースです。
v1.0.0 未満の開発中 API のため、今後のリリースで破壊的変更が入る可能性があります。

### Added

- Windows / Maya 2025 以降を対象とした Maya Module 形式の配布構成を追加。
  `installer.py`、Maya 2025 / 2026 / 2027 用ランチャー、既存ランチャーへの組み込みに対応。
- ノードの作成と既存ノードのラップを統合する `Nodes` API を追加。
  `nodes.create` / `nodes.existing` から具体的な `NodeOperator` 型へアクセス可能。
- Maya の DG / DAG ノードを Python クラスとして扱う `NodeOperator` と、
  `AttributeField` / `AttrOperator` / `PlugOperator` による attribute・plug 操作を追加。
- plug の値取得・設定、接続・切断、multi attribute の空き index 取得、
  extra attribute の追加、キーフレームの作成・照会・削除・tangent 操作に対応。
- `MDGModifier` / `MDagModifier` の操作、実行履歴、undo / redo を管理する
  `ModifierManager` を追加。
- matrix の合成・乗算・逆行列・TRS 分解を扱う `TransformMatrix` と、
  matrix plug からの translate・rotate・scale・shear・quaternion 取得を追加。
- DAG の親子操作、循環する親子関係の防止、world transform を維持した親変更、
  DAG 間の relative matrix・local matrix 取得に対応。
- Maya node type から生成クラスと手書き可能な公開 wrapper を作成する
  NodeOperator generator と、`nodes.create` / `nodes.existing` の補完 stub 生成を追加。
- Maya 実行環境で公開 API、NodeOperator、attribute・plug、matrix、generator を検証する
  pytest スイートと開発ドキュメントを追加。

[Unreleased]: https://github.com/AkihiroMamiduka/bakedanuki-util/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/AkihiroMamiduka/bakedanuki-util/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/AkihiroMamiduka/bakedanuki-util/releases/tag/v0.1.0
