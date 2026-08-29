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
- 全`PlugOperator`のlock / unlock APIと、scalar / scalar compoundだけに現れる
  Channel Box 3状態のAPIを追加。undo対応のqueued methodと、即時反映するdirect methodを
  分離し、compound child展開、multi element制約、runtime / Pyrightのcapability contractを
  Maya 2025上で検証。
- compound child limit の public method 化。
- `lookup.py` の double4 / quat 解決対応。
- 18 種類の compound 専用値型を追加し、scalar compound の
  `get()` の戻り値へ接続。
- `MatrixPlugOperator.get()` / `DataMatrixPlugOperator.get()`を
  `TransformMatrix`へ統一し、matrix plugの値設定、`MMatrix`との乗算、
  typed matrixの未設定時エラーを同じ契約へ整理。
- `TransformMatrix`とmatrix plugの値設定に、row-majorのflat 16要素 / 4行4列の
  numeric sequence入力を追加。厳密な形状検証、snapshot、runtime / Pyright contractを
  Maya 2025上で検証。
- `TransformMatrix`に、translate / Euler rotate / quaternion / scale / shearを
  keyword-onlyで受け取るcomponent合成を追加。全componentの任意指定、matrix sourceとの
  排他、全Euler回転順序とquaternionの`composeMatrix`等価性をMaya 2025上で検証。
- `TransformMatrix`の分解値をplugの`get()`と同じcompound専用値型へ統一。
  translateはcentimeterの`DoubleLinear3`、Euler回転はdegreeの
  `DoubleAngle3`、scale / shearは`Double3`、quaternionは`Quat`を返す。
- DAG の `full_path` / `is_instanced` / `parent` / `parents` と、親変更時の
  instancing 制約を追加。
- DAG traversal の `children()` / `ancestors()` / `descendants()` を追加。
  具体型解決、`ModifierManager`共有、実行済みscene状態、instancing時の列挙規則を
  Maya 2025上で検証。
- DAG traversalへShape filter、class-based type filter、完全一致option、
  固定child indexの`descendant_chain()`、`until`による境界指定を追加。
  `nodes.types`から具体classを参照できる型・補完contractも整備。
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
- Maya 2025 で作成可能な concrete shape 80種を、親 Transform 必須の
  `nodes.create.<nodeType>()` へ公開。
- 80種すべてについて `nodes.create.with_transform.<nodeType>()` を追加し、
  Transform と具体 Shape の一括作成、命名、undo / redo、戻り値型の補完を整備。
- transform 派生 NodeOperator の生成と作成 API を分離し、`nodes.create` は
  allowlist による段階公開へ変更。
- Maya 2025で作成可能なconcrete transform系52種すべてを、未接続・未初期化の
  rawノードとして`nodes.create.<nodeType>()`へ公開。親指定、具体型、命名、
  undo / redoと補完stubを検証。
- transform 派生 node の最初の既存 node 用サンプルとして、`ikHandle` /
  `ikEffector` の具体型と `nodes.existing` 補完を追加。
- transform 派生 node の第二グループとして、constraint 系14種の具体型と
  `nodes.existing` 補完を追加。専用command相当の接続はraw作成と分離。
- transform 派生 node の第三グループとして、field / emitter 系11種の具体型と
  `nodes.existing` 補完を追加。dynamics用の初期化・接続はraw作成と分離。
- transform 派生 node の第四グループとして、dynamics / deformer 周辺5種の
  具体型と `nodes.existing` 補完を追加。専用の作成手順・接続はraw作成と分離。
- transform 派生 node の第五グループとして、HIK 系5種の具体型と
  `nodes.existing` 補完を追加。`hikFKJoint` / `hikHandle` はnative継承に合わせて
  `Joint` / `IkHandle` を基底とし、専用作成手順はraw作成と分離。
- transform 派生 node の第六グループとして、scene / utility 系6種の具体型と
  `nodes.existing` 補完を追加。`lookAt` はnative継承に合わせて `AimConstraint` を
  基底とする。
- transform 派生 node の第七グループとして、VarGroup 系5種の具体型と
  `nodes.existing` 補完を追加。作成不能な抽象native基底 `baseGeometryVarGroup` も
  `BaseGeometryVarGroup` として型階層に保持し、抽象基底だけは`nodes.create`に非公開。
- transform 派生 node の第八グループとして、特殊transform
  `ufeProxyTransform` / `unknownTransform` の具体型と `nodes.existing` 補完を追加。
  `ufePath` はruntime-defined attributeとして補い、両方をraw作成へ公開。
- transformでもshapeでもない最後の汎用DAG `unknownDag` を、`DAG` 直系の
  `UnknownDag` として追加。Mayaが親Transformを自動作成するplaceholder nodeのため、
  `nodes.existing` のみに公開。
- `Transform` / `Joint`に、指定したDAGへDAG原点のworld位置を合わせる
  `match_position()`と、world姿勢を`rotate` / `rotateAxis` / `jointOrient`の
  いずれか1属性だけで合わせる属性別マッチAPIを追加。部分軸のworld / local /
  object基準、offsetParentMatrix、全rotateOrder、undo / redoをMaya 2025上で検証。
  子補償optionも設定APIと共通化し、目標値の計算後は対応する`set_*()`へ委譲。
  world姿勢のみ／位置を含む補償とJoint子の補償属性を個別に選択可能。
- `Transform` / `Joint`に、`translate` / `rotateAxis` / `rotate` / `jointOrient`の
  設定・丸めを行うnode-level APIを追加。丸めは共通の値設定経路を使用。子補償は
  既定で無効とし、world姿勢、world位置、Joint子の`rotate` / `jointOrient`補償を
  個別に選択可能。全rotateOrder、undo / redo、lock・入力接続・instanced DAGの拒否を
  Maya 2025上で検証。
- 上記の属性値設定APIへ`space="local"` / `"world"`を追加。既定のlocal属性値設定を
  維持し、world指定ではDAG原点または最終world姿勢を、対象の1属性だけで実現する
  local値へ変換。match APIとworld→local変換を共有し、offsetParentMatrix、全rotateOrder、
  非一様scale / shear、負scale、子補償、instanced DAGと非可逆な実効親行列の拒否を検証。

## 完了済み: DAG / shape API roadmap

以下の順序で、DAG階層とshape作成APIを整備しました。

### 1. DAG path と instancing の方針（初期対応完了）

子孫・先祖 traversal の実装前に、`MDagPath` と instanced DAG node の
扱いを決めました。

現在の `NodeOperator` は `MObject` を中心に扱うため、同じ node が複数の
DAG path を持つ場合に、どの path の階層を返すかが曖昧になります。

初期版では `MDagPath.getAPathTo()` で path を保持し、複数 path が存在する
node の単一 `parent` 取得や親変更は `RuntimeError` にします。すべての直接親は
`parents` から取得できます。将来 path を明示的に選択する API が必要になった場合は、
`ExistingNode` の入力と保持方法を拡張します。

### 2. DAG 階層 traversal（初期対応完了）

DAG path / instancing の方針確定後、次の階層取得APIを追加しました。

traversal 中に transform 派生 node を具体型へ解決できない問題を避けるため、
先に transform 派生 NodeOperator の coverage を段階的に整備します。Maya 2025で
登録された transform 派生134種のうち、manipulator等82種を既存規則で除外し、
残る52種はinstanceを作らない静的query、コード生成、構文確認に成功しています。
最初の代表型 `ikHandle` / `ikEffector` に続き、constraint 系14種を追加しました。
さらにfield / emitter系11種、dynamics / deformer周辺5種、HIK系5種、
scene / utility系6種、VarGroup系5種、特殊transform 2種を追加し、
`transform` / `joint` を含む52種すべてを具体型へ解決できます。
さらにtransformでもshapeでもない `unknownDag` も具体型へ解決できます。
DAG具体型の事前整備を完了してからtraversalを実装しました。

- 直接の子。
- 直接親から root 方向へ辿る先祖。
- depth-first で辿る子孫。

第一段階として`children()`を追加しました。TransformとShapeを区別せず、
Mayaのchild index順で直接の子だけを返します。自分自身、world、孫は含めません。
戻り値は同じ`ModifierManager`を共有する具体的な`DAG`系`NodeOperator`です。
結果はcacheせず、未実行の`MDagModifier`の変更は含めません。instanced childは
MObject中心で取得し、保持pathは`MDagPath.getAPathTo()`が選ぶ現行方針を維持します。

第二段階として`ancestors()`を追加しました。保持中の`MDagPath.getAPathTo()`の
1つのpathを基準に、直接の親からroot方向へ列挙します。自分自身とworldは含めず、
`children()`と同じく具体型、`ModifierManager`共有、都度取得、実行済みscene状態の
契約を維持します。

第三段階として`descendants()`を追加しました。各階層のchild index順を維持した
depth-first pre-orderで、すべての子孫を列挙します。自分自身とworldは含めません。
instanced subtreeはMaya標準traversalと同様にDAG pathごとに再訪するため、同じ
`MObject`が複数回現れる場合があります。

これで`children()` / `ancestors()` / `descendants()`の初期DAG traversalは完了です。
Shape / type filterなどの利便APIも、後述のDAG traversal拡張として実装しました。
pathを明示的に選択するAPIは、必要な利用例が揃った段階で検討します。

### 3. 親 Transform 必須の shape 作成（段階公開完了）

最初の shape 作成 API は、親 `Transform` を必須として公開しました。

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

第十四段階として、Maya 標準の hair・dynamics 補助 shape `dynamicConstraint` /
`dynHolder` / `follicle` / `hairConstraint` / `hairSystem` / `spring` を個別のシーンで
検証し、`nodes.create` へ公開済みです。simulation設定、constraint component、
hair curve、surface、solverなどとの接続や用途別初期化は raw shape 作成と分離します。

第十五段階として、Maya 標準の simulation body shape `fluidShape` / `nCloth` /
`nParticle` / `nRigid` / `particle` / `rigidBody` を個別のシーンで検証し、
`nodes.create` へ公開済みです。geometry・particle data、initial state、nucleus・
rigid solver などとの接続や用途別初期化は raw shape 作成と分離します。

第十六段階として、Maya 標準の `ufeProxyCameraShape` を標準起動状態で検証し、
`nodes.create` へ公開済みです。UFE scene item や camera との関連付けなどの用途別初期化は
raw shape 作成と分離します。残る `SphereLocator` は node type 自体が登録されておらず、
`MDagModifier.createNode()` が `invalid node type` となるため非公開のまま維持します。

全 shape class の生成後も、`nodes.create` には作成検証済み type だけを
明示的に opt-in します。生成済み concrete shape 81種のうち、Maya 2025 で
作成可能な80種を公開済みです。

### 4. transform と shape の一括作成（対応完了）

親 Transform 必須の raw shape 作成とは別に、次の一括作成 API を公開済みです。

```python
transform, mesh = nodes.create.with_transform.mesh(name="mesh")
mod.do_it_dag()
```

`name` は transform 名、`shape_name` は shape 名です。`shape_name` の省略時は
`name` に `Shape` を加えた名前を使います。戻り値は `(Transform, concrete Shape)`
とし、両方を同じ `ModifierManager` に積みます。作成する transform の親は
`parent` で指定できます。

検証済み80種すべてについて具体 shape 型の補完を提供し、raw 作成は引き続き
`nodes.create.<nodeType>(parent=transform)` として区別します。

同じ `nodes.create.<nodeType>()` の `parent` の有無で切り替える方式は採用しません。
その方式では、指定漏れによる意図しない Transform 作成、条件による戻り値型の変化、
`name` と `parent` の意味の変化が生じるためです。raw API は常に Shape のみ、
`with_transform` API は常に Transform と Shape の両方を作成する契約に固定します。

`polyCube` のように history node も生成する primitive 作成は、raw shape
作成とは別の高レベル API として扱います。

ここまでを shape 系 NodeOperator と shape 作成 API の一区切りとします。
その後、DAG path / instancing方針と初期DAG traversalまで実装し、当初予定した
DAG / shape API roadmapは完了しました。

## 完了済み: DAG traversal 拡張

初期traversalの契約を維持したまま、次の利便APIを実装しました。ここに記載する
引数名、戻り値型、探索規則は、Maya 2025の実挙動、IDE補完、Pyright contractを
確認して確定した現行仕様です。

共通方針です。

- filterは返す結果だけに適用し、対象外nodeの子孫も探索する。filterを理由に
  subtreeをpruneしない。
- 結果はcacheせず、実行済みscene状態を都度取得する。
- 自分自身とworldは含めない。
- 結果はscene上のnode typeに対応する具体的な`DAG`系`NodeOperator`とし、
  元nodeと同じ`ModifierManager`を共有する。
- instancingは現在のMObject中心と`MDagPath.getAPathTo()`の方針を維持する。

### 1. Shape filter

`children()` / `descendants()`へ`include_shapes: bool = True`を追加しました。
`False`ではMaya APIの`MFn.kShape`に一致するnodeを結果から除外します。Shapeだけへの
限定はclass-based type filterへ`Shape`を渡すことで表現し、`only` / `exclude` / `all`の
三状態を単一optionへ詰め込みません。type filterと併用した場合はAND条件です。

Shape filterも返す結果だけに適用し、`descendants()`の探索範囲は変更しません。
戻り値型は`filter_type`の有無に従う従来のPyright contractを維持します。

Maya 2025ではShapeを親にnodeを作成すると、通常childではなく
`shape->|child`形式のunderworld pathになります。`MFnDagNode(shape).childCount()`には
列挙されず、pathには現行`ExistingNode`未対応の暗黙`dagNode`も含まれるため、
underworld traversalは今回の対象外とします。Shapeが祖先になるのはこの対象外pathの
場合であるため、`ancestors()`には`include_shapes`を追加しません。

### 2. Type filter

Maya node type名の文字列ではなく、`Transform` / `Joint` / `Shape` / `Mesh`のような
`DAG`系Python classを受け取ります。`isinstance()`に基づくfilterなら
継承関係を利用でき、`type[T]`と組み合わせて戻り値を`tuple[T, ...]`として表現できます。

filter実装の事前整備として、生成済みNodeOperator classを
`nodes.types.Transform` / `nodes.types.Locator` のように参照できるAPIを追加しました。
PascalCase属性は具体的な`type[T]`をstubで公開し、実classはアクセス時に遅延importします。
`NodeOperator` / `DAG` / `Shape` / `BaseGeometryVarGroup` の基底classも参照できます。
動的なMaya node type名には `nodes.types.resolve("locator")` を使用します。

第一段階として、`children(filter_type=...)`へ単一のDAG系Python classを渡せるように
しました。filterは`isinstance()`に基づくため、`Transform`を指定すると`Joint`などの
派生型も含まれます。引数省略時と`None`は従来どおり`tuple[DAG, ...]`、
`type[T]`指定時は`tuple[T, ...]`としてPyright contractを固定しています。

第二段階として、同じclass filterを`descendants(filter_type=...)`へ拡張しました。
filterは結果だけに適用し、対象外nodeのsubtreeをpruneしません。depth-first pre-order、
instanced subtreeのpathごとの再訪、具体型と`ModifierManager`共有、実行済みscene状態を
都度取得する契約を維持します。

第三段階として、`children()` / `descendants()`へ`include_subclasses: bool = True`を
追加しました。初期値では従来どおり`isinstance()`で派生型を含め、`False`では
`type(node) is filter_type`による完全一致に切り替えます。探索範囲と列挙順は変えず、
`filter_type`なしの`False`は意味を持たないため拒否します。

第四段階として、`ancestors()`へ同じ型filterと完全一致optionを拡張しました。
保持中pathを直接親からrootまで辿る規則は維持し、filterは結果だけに適用します。
これで`children()` / `ancestors()` / `descendants()`のclass-based type filterは
同じ引数とPyright contractで利用できます。

filter対象外nodeも探索経路としては残します。例えば`Mesh`だけを要求した場合も、
途中の`Transform`で探索を止めません。Maya node type文字列は、実際の用途が必要に
なった段階で別optionとして検討します。

### 3. child indexを固定した末端までのchain

`descendant_chain(child_index: int = 0)`を追加しました。全子孫を列挙する
`descendants()`へmodeを追加せず、探索規則が異なる独立メソッドとしています。
各階層で同じchild indexだけを選び、そのindexの子が存在しない時点で終了します。
別indexへのfallbackは行わず、自分自身とworldは含めません。

結果はscene上のnode typeに対応する具体的な`DAG`系`NodeOperator`で、元nodeと同じ
`ModifierManager`を共有します。結果はcacheせず、未実行の`MDagModifier`変更は
`do_it_dag()`まで含めません。`child_index`は0以上のintとし、boolなどの非intと負数を
区別して拒否します。

### 4. 指定したDAGまでの範囲

第一段階として、`ancestors(until=...)`を追加しました。直接親から境界nodeまでを
inclusiveに探索し、指定したDAGが保持中path上に存在しない場合は`None`を返します。
自分自身は探索対象に含めないため、`until=self`も`None`です。

比較はPython instanceやnode名ではなく`MObject` identityを使い、別の`Nodes`や
`ModifierManager`から取得した同じscene nodeも境界として利用できます。instanced nodeは
保持中の1つのpathだけを対象とし、別pathに境界が存在しても`None`とします。未実行の
`MDagModifier`変更は`do_it_dag()`まで認識しません。

境界検出はtype filterから独立させます。境界がfilterに一致しない場合もそこで探索を
終了しますが、その境界は結果へ含めません。境界発見後の結果が0件なら空tuple、境界が
見つからなければ`None`です。引数省略時と`None`は従来の`tuple[T, ...]`、DAG指定時は
`tuple[T, ...] | None`になるoverloadをPyright contractで固定しました。

第二段階として、`descendant_chain(until=...)`へ同じ境界契約を拡張しました。各階層で
指定したchild indexだけを選ぶ既存規則を維持し、その固定chain上で境界を発見した場合だけ
境界までをinclusiveに返します。境界が別indexの兄弟や別subtreeにある場合、別方向へは
探索せず`None`を返します。

比較は`MObject` identityを使うため、別の`Nodes`や`ModifierManager`から取得した同じscene
nodeも指定できます。自分自身はchainの対象外なので`until=self`は`None`です。未実行の
`MDagModifier`変更は`do_it_dag()`まで含めず、引数省略時と`None`は従来の
`tuple[DAG, ...]`、DAG指定時は`tuple[DAG, ...] | None`となるPyright contractを固定しました。

これで当初予定したDAG traversal拡張のShape filter、class-based type filter、完全一致option、
固定child index chain、祖先・chainの境界指定は完了です。

## 将来の拡張候補

### Transform / Joint マッチの拡張境界

現行の位置・姿勢マッチは、非instanced DAGの評価済みscene状態を対象とする
初期仕様まで完了しています。今後機能を広げる場合も、既存メソッドの意味を
暗黙に変えず、次の境界を維持します。

- instanced DAG対応は、src / dstのDAG pathを利用者が明示できるAPIとセットで
  検討する。`MObject`から自動選択したpathへ黙ってマッチしない。
- 姿勢マッチ時のDAG原点補償は、現行メソッドへ暗黙に追加しない。必要になった場合は
  `translate`または`rotatePivotTranslate`のどちらで吸収するか、lock・入力接続、
  undo / redoの単位を含めた明示的なopt-in APIとして設計する。
- 姿勢の部分軸マッチを追加する場合は、Euler成分の単純な置換として扱わない。
  基準空間、回転積、特異点付近の解、残す姿勢成分を先に定義してから別機能として
  追加する。
- 未実行modifierを暗黙評価する仕組みは追加しない。複数のマッチ結果が依存する場合は、
  現行どおり操作間で`do_it_dg()`または`do_it_dag()`を実行する。

### compound 専用値型の演算

compound 専用値型の利用例が集まり、演算の意味を固定できてから追加します。

通常の numeric compound では、同じ型同士の加算・減算、scalar との
乗算・除算を最初の候補とします。要素積、内積、行列との演算、
quaternion multiplication などは同じ演算子へ一律に割り当てません。

`TransformMatrix`の分解値にもcompound専用値型を使用するため、今後は
translate / scale / shear / Euler回転 / quaternionの用途が同じ値型APIへ
集まります。ただし、単位付き値、要素値、Euler回転、quaternionでは妥当な演算が
異なります。共通基底へ一律に演算を追加せず、具体的な利用例と戻り値型を
型ごとに確定してから実装します。

### matrix plugの成分アクセス

matrix plugの主な値取得経路は、型やsnapshotの境界が明確な`get()`に統一します。

```python
tm = matrix_plug.get()
translate = tm.translate
```

現在、`DataMatrixPlugOperator`は`translate` / `rotate` / `get_rotate()` /
`scale` / `shear` / `quat`の委譲APIも持ちますが、`MatrixPlugOperator`は
`get()`だけを提供します。将来この差を整理する場合は、利用例を確認したうえで、
`MatrixPlugOperator`にも委譲APIを追加するか、両方を`get()`中心へ集約するかを
破壊的変更が可能なminor releaseで判断します。

委譲APIを維持・拡張する場合も、戻り値型、単位、未設定時の`ValueError`、
アクセスごとに新しいsnapshotを取得する評価規則は`TransformMatrix`と揃えます。

### connected plug の汎用解決

現在のconnection queryは、`ExistingNode`で型を解決でき、対象attributeが
`NodeOperator` / `AttributeField`に定義されているplugを`PlugOperator`として返します。
この範囲に含まれない未知のplug-in node typeやruntime extra attributeにも対応する場合は、
OpenMayaの`MObject` / `MPlug`から汎用wrapperへ解決する内部経路を追加する候補があります。

ただし、未知のattributeから専用の具象`PlugOperator`を常に復元できるとは限りません。
汎用fallbackを設ける場合は、次を先に決めます。

- 「接続なし」と「接続はあるがwrapperへ未対応」を区別し、未対応を黙って`None`や空tupleにしない。
- `cmds`へ戻さずOpenMayaで解決し、照会元の`ModifierManager`を共有する。
- 既存nodeを変更しない`auto_add_attr=False`の原則を維持する。
- scalar / compound / multi / message / typed attributeと未知のplug-in nodeをtest対象にする。
- public APIの戻り値型とIDE補完を、汎用fallbackの責務に合わせて更新する。

中間nodeを透過するconnection traversalはこの汎用解決とは別の機能です。
追加する場合も、`MPlug.connectedTo()`相当の直接接続を返す既定仕様は変更しません。

## DAG traversal 拡張後の作業候補

### 1. docs の継続更新

仕様変更後は `bakedanuki/bakedanuki-util/docs/maya/node_operator` を更新します。

特に API の使用例、未対応仕様、設計判断の理由はここに残すと後続作業が安定します。

### 2. lookup.py の追従

新しい attribute type や custom compound を追加したら `lookup_attr_cls()` の解決対象に追加します。

混在型や未対応型は fallback せず、明示的に unsupported として扱う方針です。

### 3. legacy test の整理

当初の優先候補だったextra attribute、custom compound、keyframe、transformの
built-in compound alias、connect / disconnect / next indexはpytest化済みです。

残る`bd_util/_test`は、現行pytestと重複する古い手動test、調査用script、benchmarkを
区別して整理します。仕様を追加で固定できるものだけpytestへ移し、benchmarkは
`_test`に残します。

### 4. MPxCommand 連携

`ModifierManager` を MPxCommand の undo / redo に組み込む設計を固めます。

目標は command ごとの実装を次の形に近づけることです。

```python
def undoIt(self):
    self.modifier_manager.undo_it()

def redoIt(self):
    self.modifier_manager.redo_it()
```

DAG traversal拡張の次に着手する大きな共有基盤の候補です。現在の`MPxCommandBase`が
直接保持する単一`MDagModifier`を、DG / DAG双方の履歴を扱う`ModifierManager`へ
移行する設計を固めます。

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
- matrix plugの主な取得経路は`get() -> TransformMatrix`とし、成分委譲APIを
  拡張するときも値型、単位、エラー、snapshotの契約を揃える必要があります。
- 速度改善は、利便性を壊さない範囲で行います。
