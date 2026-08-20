# Roadmap

このページは `NodeOperator` 周辺の設計メモと今後の作業候補です。

1.0.0 までは開発中 API として扱います。将来の設計と使いやすさを優先し、互換性維持
よりも改善を選んで、必要な破壊的変更を積極的に行います。安定した API 互換性の提供は
1.0.0 以降を対象とします。破壊的変更は原則として `0.x.0` の minor release で行い、
`0.x.y` の patch release では意図的に行いません。変更内容と移行手順はルートの
`CHANGELOG.md` に記録します。

## 現在固まっている方針

- Maya 専用パッケージとして割り切る。
- Maya 2025 / Python 3.11.4 以降を対象にする。
- `ModifierManager` を経由して `MDGModifier` / `MDagModifier` を扱う。
- `AttributeField` は entry point / descriptor に専念する。
- `AttrOperator` は定義情報を持つ。
- `PlugOperator` は scene 上の plug 操作を担当する。
- alias は同じ logical plug なら同じ instance を返す。
- `set_direct()` は便利用途として残すが undo 対象外と明記する。
- custom compound は低レベル型と意味付き alias を分ける。
- `Quat` は `Double4` の意味付き alias として扱う。

## 完了済みの大きな流れ

- pytest 導入。
- `plus_minus_average` / `wt_add_matrix` の代表的な挙動を pytest 化。
- `ModifierManager` 追加。
- NodeOperator / PlugOperator の modifier 参照を manager 経由へ移行。
- Pyright による node 作成、descriptor、compound / multi、戻り値型の
  contract test を追加。
- plug cache / indexed plug cache / child direct index などの速度改善。
- custom scalar compound の階層整理。
- `double2` / `double3` / `double4` / `float2` / `float3` などを custom compound 側へ移行。
- `long2` / `long3` / `short2` / `short3` を custom compound 側へ移行。
- unit compound の `double_angle2/3`、`double_linear2/3`、`float_angle2/3`、`float_linear2/3` を追加。
- compound `get()` / `set()` / `set_direct()` を整備。
- compound child limit の public method 化。
- `lookup.py` の double4 / quat 解決対応。
- 18 種類の compound 専用値型を追加し、scalar compound の
  `get()` / `value` / `value_direct` の戻り値へ接続。
- DAG の `full_path` / `is_instanced` / `parent` / `parents` と、親変更時の
  instancing 制約を追加。
- 親 Transform 必須の raw shape 作成 API を追加。
- `camera` / `locator` / `mesh` / `nurbsCurve` / `nurbsSurface` を最初の
  作成確認済み shape として公開。
- 抽象 `shape` の共通 attribute を静的 query から生成し、concrete shape の
  重複生成から除外。
- concrete shape も node instance を作らない静的 query へ統一し、Maya 2025 +
  MtoA の shape 81 種で attribute 取得、TODO なしのコード生成、構文確認、
  別 mayapy process 間の snapshot 比較を完了。
- concrete shape 81種の generated class / public wrapper / node_attr を正式生成し、
  `nodes.existing` の具体的な補完 stub へ反映。

## 決定済みのロードマップ

次の順序で、DAG 階層と shape 作成 API を整備します。

### 1. DAG path と instancing の方針（初期対応完了）

子孫・先祖 traversal の実装前に、`MDagPath` と instanced DAG node の
扱いを決めます。

現在の `NodeOperator` は `MObject` を中心に扱うため、同じ node が複数の
DAG path を持つ場合に、どの path の階層を返すかが曖昧になります。

初期版では `MDagPath.getAPathTo()` で path を保持し、複数 path が存在する
node の単一 `parent` 取得や親変更は `RuntimeError` にします。すべての直接親は
`parents` から取得できます。将来 path を明示的に選択する API が必要になった場合は、
`ExistingNode` の入力と保持方法を拡張します。

### 2. DAG 階層 traversal

DAG path / instancing の方針確定後、次の階層取得 API を追加します。

- 直接の子。
- 直接親から root 方向へ辿る先祖。
- depth-first で辿る子孫。

戻り値は同じ `ModifierManager` を共有する `DAG` 系の `NodeOperator` とし、
world を含めるか、shape を含めるか、列挙順、未実行の `MDagModifier` の
変更を含めるかを仕様として固定します。

### 3. 親 Transform 必須の shape 作成（段階公開中）

最初の shape 作成 API は、親 `Transform` を必須として公開します。

```python
mesh = nodes.create.mesh(
    name="meshShape",
    parent=transform,
)
```

親を指定せず `MDagModifier.createNode()` で shape type を作成すると、
Maya が transform を自動生成し、返される `MObject` も transform になる
場合があります。そのため、既存の DG / transform 作成 API と同じ形で
shape package 全体を無条件に公開しません。

作成可能なことを確認できた shape type から限定して公開します。第一サンプルとして
`camera` / `locator` / `mesh` / `nurbsCurve` / `nurbsSurface` の戻り値型、
undo / redo、命名、親との `ModifierManager` 共有を検証済みです。

第二段階として、Maya 標準 light shape の `ambientLight` / `areaLight` /
`directionalLight` / `pointLight` / `spotLight` / `volumeLight` も同じ条件で検証し、
`nodes.create` へ公開済みです。MtoA ロード時は、生成済みの Arnold attribute も
利用できます。

第三段階として、MtoA をロードした Maya 上で Arnold 固有 light shape の
`aiAreaLight` / `aiLightPortal` / `aiMeshLight` / `aiPhotometricLight` /
`aiSkyDomeLight` を検証し、`nodes.create` へ公開済みです。

第四段階として、残る Arnold 固有 shape の `aiCurveCollector` /
`aiLightBlocker` / `aiStandIn` / `aiVolume` も raw shape としての作成、命名、
親子関係、undo / redo を検証し、`nodes.create` へ公開済みです。ファイル指定や
geometry・shader 接続などの用途別初期化は、高レベル API の候補として分離します。

第五段階として、Maya 標準 geometry shape の `baseLattice` / `bezierCurve` /
`lattice` / `subdiv` を個別のシーンで検証し、`nodes.create` へ公開済みです。
geometry データや lattice 分割数などの内容初期化は raw shape 作成と分離します。

第六段階として、Maya 標準 primitive shape の `implicitBox` / `implicitCone` /
`implicitSphere` / `renderBox` / `renderCone` / `renderRect` / `renderSphere` を
個別のシーンで検証し、`nodes.create` へ公開済みです。size や radius などの
値設定は raw shape 作成と分離します。

第七段階として、Maya 標準の計測・注釈 shape `angleDimension` /
`annotationShape` / `arcLengthDimension` / `distanceDimShape` / `paramDimension` を
個別のシーンで検証し、`nodes.create` へ公開済みです。計測点、表示テキスト、
NURBS geometry との接続などの用途別初期化は raw shape 作成と分離します。

第八段階として、Maya 標準の補助 locator・marker・handle shape `clusterHandle` /
`directedDisc` / `dropoffLocator` / `hikFloorContactMarker` / `motionTrailShape` /
`orientationMarker` / `positionMarker` / `softModHandle` を個別のシーンで検証し、
`nodes.create` へ公開済みです。deformer、motion path、HIK などとの接続や
用途別初期化は raw shape 作成と分離します。`SphereLocator` は Maya 2025 の
標準状態で `invalid node type` となるため、未公開のまま維持します。

第九段階として、Maya 標準の非線形 deformer 表示 shape `deformBend` /
`deformFlare` / `deformSine` / `deformSquash` / `deformTwist` / `deformWave` を
個別のシーンで検証し、`nodes.create` へ公開済みです。対応する deformer node
との接続や `deformerData` の初期化は raw shape 作成と分離します。

第十段階として、Maya 標準の deformation connection helper shape
`clusterFlexorShape` / `flexorShape` / `geoConnectable` を個別のシーンで検証し、
`nodes.create` へ公開済みです。driver、flexor、surface geometry などとの接続は
raw shape 作成と分離します。

第十一段階として、Maya 標準のシーン表示・カメラ補助 shape `imagePlane` /
`sketchPlane` / `snapshotShape` / `stereoRigCamera` を個別のシーンで検証し、
`nodes.create` へ公開済みです。画像ファイル、描画内容、snapshot frame、
stereo camera 接続などの用途別初期化は raw shape 作成と分離します。

第十二段階として、Maya 標準のレンダリング・環境表現補助 shape `environmentFog` /
`fluidTexture2D` / `fluidTexture3D` / `heightField` を個別のシーンで検証し、
`nodes.create` へ公開済みです。camera、fluid data、texture、displacement などとの
接続や用途別初期化は raw shape 作成と分離します。

第十三段階として、Maya 標準の描画・Paint Effects 補助 shape `greasePlane` /
`greasePlaneRenderShape` / `lineModifier` / `pfxHair` / `pfxToon` / `stroke` を
個別のシーンで検証し、`nodes.create` へ公開済みです。image、brush、hair / toon
input、render geometry、line modifier などの接続や用途別初期化は raw shape 作成と
分離します。

全 shape class の生成後も、`nodes.create` には作成検証済み type だけを
明示的に opt-in します。未検証 class は `nodes.existing` からの利用に限定します。
Arnold 固有 shape 9種はすべて作成確認済みです。その他の shape は、用途と
作成前提ごとに分けて検証します。

### 4. transform と shape の一括作成

親 Transform 必須の API が安定した後、transform と shape を同じ
`ModifierManager` に積んで一括作成する便利 API を検討します。

shape 名と transform 名、戻り値を shape 単体にするか両方返すか、
既存の `nodes.create.<nodeType>()` とどう区別するかを明示します。

`polyCube` のように history node も生成する primitive 作成は、raw shape
作成とは別の高レベル API として扱います。

## 将来の拡張候補

### compound 専用値型の演算

compound 専用値型の利用例が集まり、演算の意味を固定できてから追加します。

通常の numeric compound では、同じ型同士の加算・減算、scalar との
乗算・除算を最初の候補とします。要素積、内積、行列との演算、
quaternion multiplication などは同じ演算子へ一律に割り当てません。

## 近い作業候補

### 1. docs の継続更新

仕様変更後は `bakedanuki/bakedanuki-util/docs/maya/node_operator` を更新します。

特に API の使用例、未対応仕様、設計判断の理由はここに残すと後続作業が安定します。

### 2. lookup.py の追従

新しい attribute type や custom compound を追加したら `lookup_attr_cls()` の解決対象に追加します。

混在型や未対応型は fallback せず、明示的に unsupported として扱う方針です。

### 3. pytest の移植

既存 `_test` のうち、仕様固定できるものを順次 pytest へ移します。

優先候補:

- extra attribute
- custom compound
- keyframe
- transform の built-in compound alias
- connect / disconnect / next index

ベンチマークは `_test` に残します。

### 4. MPxCommand 連携

`ModifierManager` を MPxCommand の undo / redo に組み込む設計を固めます。

目標は command ごとの実装を次の形に近づけることです。

```python
def undoIt(self):
    self.modifier_manager.undo_it()

def redoIt(self):
    self.modifier_manager.redo_it()
```

### 5. set_direct の扱い

`set_direct()` は高速で便利ですが、undo には参加しません。

今後も明確に「即時編集用」として扱い、undo が必要な処理では `set()` と `ModifierManager` を使います。

### 6. 文字化けコメントの整理

一部ソース内に文字化けしたコメントや docstring が残っています。

実装に影響しない箇所でも、今後の保守性のために UTF-8 の日本語コメントへ修復する価値があります。

### 7. 1.0.0 前の API 整理

正式リリース前に次を整理します。

- 公開 API と内部 API の境界。
- deprecated なしで削除してよい旧実装。
- `AddAttr` へ公開する型。
- docs と README の導線。
- MayaModule への導入方法。

## watch points

- `NodeOperator.__getitem__()` の文字列パス解析は未確定です。
- `set_direct()` は undo 非対応です。
- `lookup.py` は型追加時に更新漏れが起きやすいです。
- unit 系の戻り値や入力単位は、実装と docs を常に揃える必要があります。
- 速度改善は、利便性を壊さない範囲で行います。
