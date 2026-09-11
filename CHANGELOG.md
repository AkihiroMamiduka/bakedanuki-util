# Changelog

このプロジェクトの注目すべき変更は、このファイルに記録します。

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を参考にし、
バージョン番号は [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

### Added

- `get_curve_data()`に範囲指定を追加し、`get_key_data()`と共通の境界補完を実装。
  既定の`include_boundaries=True`では、元カーブを変更せずに境界キーと調整後の接線を取得する。
  連続接線をfixed化し、step / stepnext、weighted、単位を保持して区間を切り出す。
  constant / linearの範囲外補完に対応。cycle系の範囲外補完は明示的に拒否する。
- `KeyframeManager.get_weighted()` / `set_weighted()`を追加。単純な直接接続カーブの
  weightedを照会・変更し、接線の変換はMaya標準処理に委譲する。変更は予約実行とUndo / Redoに対応。
- `KeyData` / `AnimCurveData`と、`KeyframeManager`の`get_key_data()` /
  `set_key_data()` / `get_curve_data()` / `set_curve_data()`を追加。
  単純な直接接続のTA/TL/TUカーブについて、接線・lock・breakdown・weighted・infinityを
  JSON経由でも保存・復元できる。degree / cmと保存時の時間単位を保持し、
  遅延実行・Undo / Redo・途中失敗時rollbackに対応する。
- scalar plugに`sample_values(*, frames)`を追加。constraint・layer・計算ノードを含む
  指定時刻の評価済み値を、`set_keys()`へ渡せる`(frame, value)`のlistで取得する。
  公開単位と入力順を維持し、現在時刻・Undo履歴・保留中modifierを変更しない。
- `KeyframeManager.get_keys(start_frame=None, end_frame=None)`を追加。上流の
  time-inputカーブに実在するキーを、範囲の両端を含む`(frame, value)`のlistで返す。
  予約中の操作は実行せず、値の単位は取得したカーブ型から換算する。
- `KeyframeManager.set_keys(keys, ...)`を追加。`keys`は`(frame, value)`の列。
  単位・tangent・予約実行とUndo / Redoは`set_key()`と共通で、全入力を捕捉・検証してから入力順に
  設定する。単純なカーブではバッチ内の取得と変更キャッシュを共有し、新規作成や
  複雑な接続ではMaya標準のキー設定を使用する。
- `Quat`をimmutableなraw Quaternion値のまま拡張。identity / sequence /
  `MQuaternion` constructor、Euler / axis-angle / 2-vector / matrixからの作成、
  Quaternion積、変換、逆元、共役、正規化、shortest-path slerp、状態と等価性の
  照会に対応。Euler変換の`rotate_order`は回転順序名とMayaの0〜5のindexを受け取る。
- `Double2` / `Double3` / `Double4`、`Float2` / `Float3`に、同じ具体型同士の
  加減算、scalarによる乗除算、符号反転を追加。
- `Transform` / `Joint`に、指定したDAGノードへDAG原点のworld位置を合わせる
  `match_position()`を追加。合わせる軸と、world / local / objectの基準空間を
  指定できる。
- `Transform` / `Joint`に、world姿勢を`rotate` / `rotateAxis` / `jointOrient`の
  いずれか1属性だけで合わせる属性別マッチAPIを追加。非対象の回転属性と
  translate / pivotは変更せず、rotate pivotに対する位置補償は行わない。

### Changed

- `get_key_data(start_frame, end_frame)`は、既定で境界を補完する破壊的変更。
  既存キーと元の接線情報だけを取得する場合は`include_boundaries=False`を指定する。
  範囲無指定の取得と`get_keys()`の仕様は維持する。
- `KeyData`を直接編集可能に変更。設定予約時とJSON出力時に再検証し、独立コピーを保持する。
  `set_key_data()`の`weighted`引数を廃止し、既存カーブの設定を維持、新規はnonweightedとする。
  接線XYをweighted相当の共通表現へ統一し、保存schemaを2へ更新。
  `AnimCurveData.from_dict()`はschema 2のみを受け付け、旧形式の変換処理は提供しない。
- `KeyframeManager.set_keys()`の入力を、別々の`values` / `frames`から
  `(frame, value)`のpair列へ変更する破壊的変更。旧引数は提供しない。
  `set_keys(zip(frames, values, strict=True), ...)`で移行でき、単位・共通tangent・
  予約実行・Undo / Redoの仕様は維持する。
- `KeyframeManager.set()`を`set_key()`へ、`insert()`を`insert_key()`へ改名する
  破壊的変更。旧名のaliasは提供せず、`plug.keyframe.set_key()` /
  `plug.keyframe.insert_key()`へ移行する。引数、`None`戻り値、予約実行、
  Undo / Redoの仕様は維持する。
- `Quat`を`Double4`の派生型から、`Scalar4[float]`を直接共有する独立した具体型へ変更。
  double4 plugの物理表現は共有しつつ、numeric値型のcomponent-wise演算が
  Quaternionへ波及しない型階層へ整理。
- `PlugOperator` の接続照会を `MPlug.connectedTo()` ベースへ変更。
  接続先を具体的な `PlugOperator` として返し、`nodes.types` によるnode type filterと
  subclassの包含指定に対応。ノード名・plug名は専用メソッドで取得する。
- `MatrixPlugOperator.get()` と `DataMatrixPlugOperator.get()` の戻り値を
  `TransformMatrix` に統一。未設定のtyped matrix plugはidentity matrixや`None`へ
  補完せず、値を取得できない場合は`ValueError`を送出する。
- matrix plugの値設定が`TransformMatrix` / `MMatrix` /
  `MTransformationMatrix`を受け取れるように変更。
- `TransformMatrix`と`MMatrix`の左右両方向の乗算に対応し、結果を
  `TransformMatrix`として返すように変更。
- `TransformMatrix`の分解値をtupleからcompound専用値型へ変更。
  `translate`は`DoubleLinear3`、`rotate` / `get_rotate()`は`DoubleAngle3`、
  `scale` / `shear`は`Double3`、`quat`は`Quat`を返す。
- `TransformMatrix.get_rotate()`の引数名を`order`から`rotate_order`へ変更し、
  回転順序名に加えてMayaの`rotateOrder` indexを受け取るように変更。

### Removed

- matrix plugの`transform_matrix`プロパティを削除。`get()`が返す
  `TransformMatrix`を使用する。

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
- v1.0.0 未満の互換性方針を明文化。破壊的変更は原則として minor release で行い、
  patch release では意図的に行わず、一度公開した `MTypeId` は変更・再利用しない方針を追加。

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
