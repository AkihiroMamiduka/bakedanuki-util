# NodeOperator

このドキュメントは、`bd_util.maya.node.operator` 周辺の現行仕様を共有するためのメモです。

対象は Maya 2025 / Python 3.11.4 以降です。まだ 1.0.0 前の開発中 API として扱い、利便性と OpenMaya に近い速度の両立を優先します。

## 目的

`NodeOperator` は Maya ノード操作を Python から扱いやすくするためのラッパーです。

主な狙いは次の通りです。

- `maya.api.OpenMaya` を直接使うより記述量を減らす。
- `maya.cmds` / PyMEL より型とアクセス経路を明確にする。
- ノード、アトリビュート、プラグ、modifier の責務を分ける。
- 速度面では生の OpenMaya にできるだけ近づける。
- 将来 MPxCommand で undo / redo を組み込めるようにする。

## 主要ファイル

- `python/bd_util/maya/node/operator/node/_core.py`
  - `NodeOperator` の基底クラスです。
- `python/bd_util/maya/node/operator/node/dg/_core.py`
  - DG ノード共通の基底クラスです。
- `python/bd_util/maya/node/operator/node/dag/_core.py`
  - DAG ノード共通の基底クラスです。
- `python/bd_util/maya/node/operator/node/dag/transform/_core.py`
  - 手書きの公開 `Transform` クラスと、Transform 固有の操作 API です。
- `python/bd_util/maya/node/operator/node/dg/_generated`
  - DG NodeOperator の自動生成 class を置く package です。
- `python/bd_util/maya/node/operator/node/dag/_generated`
  - DAG NodeOperator の自動生成 class を置く package です。
- `python/bd_util/maya/node/operator/node/dag/transform/_generated`
  - Generator が出力する `GeneratedTransform` と Transform 派生 NodeOperator の生成 class です。
- `python/bd_util/maya/node/operator/node/dag/shape/_generated`
  - Shape NodeOperator の自動生成 class を置く package です。
- `python/bd_util/maya/node/operator/node/dg/<node_type>.py`
  - 生成 class を継承する手書き可能な公開 wrapper です。Transform / Shape 派生 node も同じ分離方針です。
- `python/bd_util/maya/node/operator/attr/_core.py`
  - `AttributeField` / `AttrOperator` / `PlugOperator` の中核です。
- `python/bd_util/maya/node/operator/attr/extra/add_attr.py`
  - extra attribute 作成用の `AddAttr` API です。
- `python/bd_util/maya/node/operator/attr/lookup.py`
  - Maya 上の既存アトリビュートから対応する `AttrOperator` を推定します。
- `python/bd_util/maya/node/modifier/_core.py`
  - `ModifierManager` です。
- `python/bd_util/maya/node/nodes.py`
  - `Nodes` です。ノード作成、既存ノード変換、NodeOperator class参照の統合入口です。
- `python/bd_util/maya/node/node_types.py`
  - `nodes.types` を構成する、NodeOperator classの遅延参照accessorです。
- `python/bd_util/maya/node/creator/_core.py`
  - `nodes.create` を構成する内部実装の `NodeCreator` です。
- `python/bd_util/maya/node/existing_node.py`
  - `nodes.existing` を構成する内部実装の `ExistingNode` です。

## 基本構成

```mermaid
flowchart TD
    NodeOperator["NodeOperator"]
    DG["DG"]
    DAG["DAG"]
    Transform["Transform"]
    AttributeField["AttributeField"]
    AttrOperator["AttrOperator"]
    PlugOperator["PlugOperator"]
    ModifierManager["ModifierManager"]
    Nodes["Nodes"]
    NodeCreator["NodeCreator"]
    ExistingAccessor["nodes.existing"]
    ExistingNode["ExistingNode"]
    NodeTypes["nodes.types"]
    OpenMaya["maya.api.OpenMaya"]

    Nodes --> NodeCreator
    Nodes --> ExistingAccessor
    Nodes --> NodeTypes
    Nodes --> ModifierManager
    ExistingAccessor --> ExistingNode
    NodeCreator --> NodeOperator
    NodeCreator --> ModifierManager
    ExistingNode --> NodeOperator
    ExistingNode --> ModifierManager
    NodeTypes --> NodeOperator
    NodeOperator --> DG
    NodeOperator --> DAG
    DAG --> Transform
    NodeOperator --> AttributeField
    AttributeField --> AttrOperator
    AttributeField --> PlugOperator
    PlugOperator --> ModifierManager
    NodeOperator --> ModifierManager
    ModifierManager --> OpenMaya
```

## アクセスモデル

`AttributeField` は descriptor として動作します。

同じフィールドでも、アクセス元によって返すものが変わります。

- `SomeNode.someAttr`
  - クラスアクセスです。
  - `AttrOperator` を返します。
- `node.someAttr`
  - ノードインスタンスからのアクセスです。
  - `PlugOperator` を返します。
- `node.compound.child`
  - compound plug から子 plug へのアクセスです。
  - 子の `PlugOperator` を返します。

`short_name` alias は同じ plug instance を返す方針です。

```python
node.output3D is node.o3
node.output3D.output3Dx is node.output3Dx
node.input3D[0] is node.input3D[0]
```

## NodeOperator の生成

`Nodes` は、ノード作成と既存ノード変換を一つの `ModifierManager` から扱う推奨入口です。

```python
from maya import cmds
import bd_util as bdu

cmds.createNode("transform", name="existing_node")

modifier_manager = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=modifier_manager)

created = nodes.create.transform(name="new_node")
existing = nodes.existing.transform("existing_node")

modifier_manager.do_it_dag()
```

`nodes.create` は、共有 `ModifierManager` を使うノード作成アクセサです。
`nodes.existing` は、同じ `ModifierManager` を使う既存ノードアクセサです。
したがって、各呼び出しで `modifier_manager=` を繰り返す必要はありません。

```python
assert created.modifier_manager is modifier_manager
assert existing.modifier_manager is modifier_manager
```

既存ノードの nodeType を自動判定する場合は、`nodes.existing` 自体を呼び出します。

```python
existing = nodes.existing("existing_node")
```

生成済みの `NodeOperator` classを参照する場合は、`nodes.types` を使います。
属性名はMaya node type名ではなく、Python classと同じPascalCaseです。

```python
transform_type = nodes.types.Transform
locator_type = nodes.types.Locator
shape_type = nodes.types.Shape

assert issubclass(locator_type, shape_type)
```

`NodeOperator` / `DAG` / `Shape` / `BaseGeometryVarGroup` のような基底classと、
`nodes.existing` が具体型へ解決できる生成済みclassを参照できます。作成可否とは
独立しているため、`IkHandle` / `UnknownDag` / `SphereLocator` も対象です。
実classは属性へ最初にアクセスしたときだけimportされ、結果はaccessor内でcacheされます。

動的なMaya node type名から解決する場合は `resolve()` を使います。

```python
node_type = nodes.types.resolve("locator")
```

`resolve()` は正確なMaya node type名を受け取り、静的な戻り値型は
`type[NodeOperator]`です。具体型のIDE補完が必要なコードでは
`nodes.types.Locator` の形式を使います。

`NodeCreator` / `ExistingNode` は `Nodes` の内部実装として維持しますが、`bd_util` の公開APIには含めません。
ノード作成と既存ノード変換は、どちらも `Nodes` から利用します。

ノード作成は `ModifierManager` を受け取ります。

```python
from bd_util.maya.node.modifier import ModifierManager
from bd_util.maya.node.operator.node.dg.plus_minus_average import PlusMinusAverage

modifier_manager = ModifierManager()

node = PlusMinusAverage.create(modifier_manager, name="test_pma")
modifier_manager.do_it_dg()
```

複数のノード型を扱う場合は、個別の `NodeOperator` クラスを毎回 import せず、`nodes.create` から作成できます。

```python
import bd_util as bdu

modifier_manager = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=modifier_manager)

pma = nodes.create.plusMinusAverage(name="plus_minus_ave")
mult_div = nodes.create.multiplyDivide(name="mult_div")

modifier_manager.do_it_dg()
```

内部の `NodeCreator` は DG ノード名、transform 系 DAG ノード名、作成確認済みの
shape ノード名を lazy import し、`NodeOperator.create()` を呼びます。
生成メソッド名は `multiplyDivide` のような Maya nodeType 名に合わせています。
`create()` には `plus_minus_average` のような snake_case と、`multiplyDivide` のような Maya nodeType 名のどちらでも渡せます。
IDE 補完用に `.pyi` を用意し、主要な生成メソッドの戻り型が各 `NodeOperator` クラスとして見えるようにしています。

Maya 2025で作成確認済みのconcrete transform系52種は、`nodes.create`から
未接続・未初期化のrawノードとして作成できます。作成時の親は`parent=`で指定でき、
親子を同じ`MDagModifier`に積めます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

parent = nodes.create.transform(name="parent")
constraint = nodes.create.aimConstraint(
    name="raw_aim_constraint",
    parent=parent,
)

mod.do_it_dag()
```

constraintのtarget接続、IKのjoint / solver設定、fieldのdynamics接続など、
Mayaの専用commandが行う用途別初期化はraw作成に含めません。作成不能な抽象native基底
`baseGeometryVarGroup`と、transform直系ではない`unknownDag`は`nodes.create`へ
公開しません。

shape 系ノードは、親 `Transform` を必須として作成します。親を省略して Maya に
Transform を自動生成させる経路は公開しません。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

transform = nodes.create.transform(name="mesh")
mesh = nodes.create.mesh(
    name="meshShape",
    parent=transform,
)

mod.do_it_dag()
```

transform と shape を一度に用意する場合は、`nodes.create.with_transform` を使います。
戻り値は `(Transform, concrete Shape)` の順で、両方が同じ `ModifierManager` に
積まれます。`name` は transform 名を表し、`shape_name` を省略すると
`{name}Shape` が使われます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

transform, mesh = nodes.create.with_transform.mesh(name="mesh")

mod.do_it_dag()
```

明示的な shape 名や、作成する transform の親も指定できます。

```python
group = nodes.create.transform(name="group")
transform, camera = nodes.create.with_transform.camera(
    name="camera",
    shape_name="renderCameraShape",
    parent=group,
)

mod.do_it_dag()
```

`nodes.create.mesh(parent=transform)` は親必須の raw shape 作成として維持します。
一括作成は `nodes.create.with_transform.mesh()` という別入口にすることで、
既存 API と transform 自動生成の意図を区別しています。

### raw shape 作成と一括作成を分ける理由

2つの入口は、作成するノード数だけでなく、引数と戻り値の意味も異なります。

| API | 作成対象 | `name` | `parent` | 戻り値 |
| --- | --- | --- | --- | --- |
| `nodes.create.locator(parent=transform)` | Shapeのみ | Shape名 | Shapeの親Transform。必須 | `Locator` |
| `nodes.create.with_transform.locator()` | Transform + Shape | Transform名 | 新規Transformの親。任意 | `tuple[Transform, Locator]` |

`nodes.create.locator()` の `parent` を省略可能にし、その有無で処理を切り替える
overload も技術的には実装できます。ただし、その設計では次の問題が生じます。

- `parent` の指定漏れがエラーにならず、意図しない Transform 作成へ変わる。
- 同じメソッドの戻り値が `Locator` または `tuple[Transform, Locator]` になる。
- `parent: Transform | None` を渡すと戻り値も union になり、利用側で型の絞り込みが必要になる。
- `name` と `parent` の意味が、同じメソッド内で条件によって変わる。
- scene に1ノードを作る操作と2ノードを作る操作を、呼び出しから判別しにくい。

戻り値を常に Shape のみにすれば union は避けられますが、自動作成した Transform を
直接受け取れません。また、Transform の作成が呼び出し側から見えにくくなります。

そのため、raw API は親の指定漏れを検出し、常に具体 Shape 型を返す入口として固定します。
一括作成 API は Transform の生成を明示し、常に
`tuple[Transform, concrete Shape]` を返す別入口として固定します。

現在 `nodes.create` から作成できる shape は、動作確認済みの次の80種類です。

- `aiAreaLight`
- `aiCurveCollector`
- `aiLightBlocker`
- `aiLightPortal`
- `aiMeshLight`
- `aiPhotometricLight`
- `aiSkyDomeLight`
- `aiStandIn`
- `aiVolume`
- `ambientLight`
- `angleDimension`
- `annotationShape`
- `arcLengthDimension`
- `areaLight`
- `baseLattice`
- `bezierCurve`
- `camera`
- `clusterFlexorShape`
- `clusterHandle`
- `deformBend`
- `deformFlare`
- `deformSine`
- `deformSquash`
- `deformTwist`
- `deformWave`
- `directedDisc`
- `directionalLight`
- `distanceDimShape`
- `dropoffLocator`
- `dynamicConstraint`
- `dynHolder`
- `environmentFog`
- `flexorShape`
- `fluidShape`
- `fluidTexture2D`
- `fluidTexture3D`
- `follicle`
- `geoConnectable`
- `greasePlane`
- `greasePlaneRenderShape`
- `hairConstraint`
- `hairSystem`
- `heightField`
- `hikFloorContactMarker`
- `imagePlane`
- `implicitBox`
- `implicitCone`
- `implicitSphere`
- `lattice`
- `lineModifier`
- `locator`
- `mesh`
- `motionTrailShape`
- `nCloth`
- `nParticle`
- `nRigid`
- `nurbsCurve`
- `nurbsSurface`
- `orientationMarker`
- `paramDimension`
- `particle`
- `pfxHair`
- `pfxToon`
- `pointLight`
- `positionMarker`
- `renderBox`
- `renderCone`
- `renderRect`
- `renderSphere`
- `rigidBody`
- `sketchPlane`
- `snapshotShape`
- `softModHandle`
- `spotLight`
- `spring`
- `stereoRigCamera`
- `stroke`
- `subdiv`
- `ufeProxyCameraShape`
- `volumeLight`

Maya 標準 light shape 6種は、指定した親 Transform と名前での作成、および
同じ `ModifierManager` に積んだ一括 undo / redo を Maya 2025 上で確認済みです。
MtoA ロード時は、各 light に生成されている Arnold attribute も戻り値型から利用できます。

Arnold 固有 light shape 5種は MtoA のロードを前提とし、指定した親 Transform と
名前での作成、および一括 undo / redo を Maya 2025 + MtoA 上で確認済みです。

残る Arnold 固有 shape 4種も、MtoA ロード下で raw shape としての作成と
undo / redo を確認済みです。`aiStandIn.dso` や `aiVolume.filename` の値設定、
geometry・shader 接続など、用途別の初期化はこの API では自動実行しません。

Maya 標準 geometry shape の `baseLattice` / `bezierCurve` / `lattice` / `subdiv`
も、raw shape としての作成と undo / redo を確認済みです。geometry データや
lattice 分割数などの内容初期化は自動実行しません。

Maya 標準 primitive shape の `implicitBox` / `implicitCone` / `implicitSphere` /
`renderBox` / `renderCone` / `renderRect` / `renderSphere` も、raw shape としての
作成と undo / redo を確認済みです。size や radius などの値設定は自動実行しません。

Maya 標準の計測・注釈 shape `angleDimension` / `annotationShape` /
`arcLengthDimension` / `distanceDimShape` / `paramDimension` も、raw shape としての
作成と undo / redo を確認済みです。計測点、表示テキスト、NURBS geometry との接続
など、用途別の初期化は自動実行しません。

Maya 標準の補助 locator・marker・handle shape `clusterHandle` / `directedDisc` /
`dropoffLocator` / `hikFloorContactMarker` / `motionTrailShape` /
`orientationMarker` / `positionMarker` / `softModHandle` も、raw shape としての作成と
undo / redo を確認済みです。deformer、motion path、HIK などとの接続や用途別の
初期化は自動実行しません。生成済みの `SphereLocator` class は Maya 2025 の
標準状態で node type を作成できないため、`nodes.create` へは公開していません。

Maya 標準の非線形 deformer 表示 shape `deformBend` / `deformFlare` /
`deformSine` / `deformSquash` / `deformTwist` / `deformWave` も、raw shape としての
作成と undo / redo を確認済みです。対応する deformer node との接続や
`deformerData` の初期化は自動実行しません。

Maya 標準の deformation connection helper shape `clusterFlexorShape` /
`flexorShape` / `geoConnectable` も、raw shape としての作成と undo / redo を
確認済みです。driver、flexor、surface geometry などとの接続は自動実行しません。

Maya 標準のシーン表示・カメラ補助 shape `imagePlane` / `sketchPlane` /
`snapshotShape` / `stereoRigCamera` も、raw shape としての作成と undo / redo を
確認済みです。画像ファイル、描画内容、snapshot frame、stereo camera 接続などの
用途別初期化は自動実行しません。

Maya 標準の UFE proxy camera shape `ufeProxyCameraShape` も、標準起動状態での
raw shape 作成と undo / redo を確認済みです。UFE scene item や camera との関連付けなど、
用途別初期化は自動実行しません。

Maya 標準のレンダリング・環境表現補助 shape `environmentFog` / `fluidTexture2D` /
`fluidTexture3D` / `heightField` も、raw shape としての作成と undo / redo を
確認済みです。camera、fluid data、texture、displacement などとの接続や
用途別初期化は自動実行しません。

Maya 標準の描画・Paint Effects 補助 shape `greasePlane` /
`greasePlaneRenderShape` / `lineModifier` / `pfxHair` / `pfxToon` / `stroke` も、
raw shape としての作成と undo / redo を確認済みです。image、brush、hair / toon
input、render geometry、line modifier などの接続や用途別初期化は自動実行しません。

Maya 標準の hair・dynamics 補助 shape `dynamicConstraint` / `dynHolder` / `follicle` /
`hairConstraint` / `hairSystem` / `spring` も、raw shape としての作成と undo / redo を
確認済みです。simulation設定、constraint component、hair curve、surface、solver
などとの接続や用途別初期化は自動実行しません。

Maya 標準の simulation body shape `fluidShape` / `nCloth` / `nParticle` / `nRigid` /
`particle` / `rigidBody` も、raw shape としての作成と undo / redo を確認済みです。
geometry・particle data、initial state、nucleus・rigid solver などとの接続や用途別初期化は
自動実行しません。

Maya 2025 + MtoA の concrete shape 81種は class 生成済みで、
`nodes.existing.<nodeType>()` から具体的な戻り値型として利用できます。
このうち80種は作成確認済みで、`nodes.create` へ公開しています。残る
`SphereLocator` は Maya 2025 の標準状態で node type が登録されていないため、
非公開のまま維持します。
`polyCube` のように Transform、Shape、history node をまとめて作る操作は、raw shape
作成とは別の高レベル API として扱います。

## DAG の親子操作

`DAG.parent` は直接の親を返し、ワールド直下では `None` を返します。
`DAG.parents` は直接の親を tuple で返し、ワールドは含めません。
`DAG.children()` はTransformとShapeを区別せず、すべての直接の子をMayaの
child index順で返します。自分自身、world、孫は含めません。
`filter_type=`へDAG系`NodeOperator` classを渡すと、`isinstance()`で一致する子だけを
同じ順序で返します。省略時または`None`では、従来どおりすべての直接の子を返します。
`include_subclasses=False`を併用すると、派生classを除き、指定classと完全一致する子だけを
返します。
`include_shapes=False`を指定すると、Transformや`UnknownDag`などを残したまま、
すべてのShape系nodeを結果から除外します。
`DAG.ancestors()` は保持中のpathを基準に、直接の親からroot方向へ返します。
自分自身とworldは含めません。`filter_type=`を指定した場合もrootまで辿り、
一致した祖先だけを同じ順序で返します。
`until=`へDAGを指定すると、その境界までを探索し、境界が保持中pathになければ`None`を
返します。
`DAG.descendants()` は各階層のchild index順を維持したdepth-first pre-orderで、
すべての子孫を返します。自分自身とworldは含めません。
`filter_type=`を指定した場合も探索範囲は変えず、一致した子孫だけを結果へ含めます。
`DAG.descendant_chain(child_index=0)`は、各階層で同じchild indexの子だけを選び、
そのindexの子が存在しなくなるまで返します。`until=`を指定すると、その固定chain上の
境界までを返し、境界が見つからなければ`None`を返します。自分自身とworldは含めません。

```python
parent = child.parent
parents = child.parents
children = parent.children()
non_shape_children = parent.children(include_shapes=False)
transform_children = parent.children(filter_type=nodes.types.Transform)
exact_transform_children = parent.children(
    filter_type=nodes.types.Transform,
    include_subclasses=False,
)
shape_children = parent.children(filter_type=nodes.types.Shape)
locator_children = parent.children(filter_type=nodes.types.Locator)
ancestors = child.ancestors()
ancestors_to_root = child.ancestors(until=root)
transform_ancestors = child.ancestors(filter_type=nodes.types.Transform)
exact_transform_ancestors = child.ancestors(
    filter_type=nodes.types.Transform,
    include_subclasses=False,
)
descendants = parent.descendants()
non_shape_descendants = parent.descendants(include_shapes=False)
transform_descendants = parent.descendants(
    filter_type=nodes.types.Transform,
)
exact_transform_descendants = parent.descendants(
    filter_type=nodes.types.Transform,
    include_subclasses=False,
)
shape_descendants = parent.descendants(filter_type=nodes.types.Shape)
mesh_descendants = parent.descendants(filter_type=nodes.types.Mesh)
first_child_chain = parent.descendant_chain()
second_child_chain = parent.descendant_chain(child_index=1)
chain_to_target = parent.descendant_chain(until=target)
is_instanced = child.is_instanced
```

`children()` / `ancestors()` / `descendants()` / `descendant_chain()` の各要素は
scene上のnode typeに
対応する具体的な`DAG`系
`NodeOperator`で、元のnodeと同じ`ModifierManager`を共有します。結果はcacheせず、
呼び出すたびに現在のsceneから取得します。同じ`ModifierManager`に積まれていても、
未実行の`MDagModifier`による作成・親変更は`do_it_dag()`まで含めません。

`children(filter_type=...)` / `ancestors(filter_type=...)` /
`descendants(filter_type=...)` は継承関係を考慮します。
例えば`Transform`には`Joint`などの派生classも含まれ、`Shape`にはconcrete shapeが
含まれます。`include_subclasses=False`を指定すると`type(node) is filter_type`で判定し、
`Transform`だけを対象として`Joint`などを除外できます。`Shape`や`DAG`のような基底classを
完全一致で指定した結果に該当nodeがなければ、空tupleを返します。戻り値型は
`nodes.types.Locator`を渡した場合に`tuple[Locator, ...]`となるよう、
`type[T]`とoverloadで公開します。DG系class、NodeOperator instance、複数classの
tupleは受け取らず、`TypeError`にします。`include_subclasses`はboolだけを受け取り、
`filter_type`なしで`False`を指定した場合は`ValueError`にします。

`include_shapes`はboolだけを受け取り、初期値は`True`です。`False`では
Maya APIの`MFn.kShape`に一致するnodeを結果から除外します。Shapeだけへの限定は
`filter_type=nodes.types.Shape`で表現します。`filter_type`と併用した場合はAND条件とし、
例えば`filter_type=nodes.types.Shape, include_shapes=False`は空tupleを返します。
このoptionはShapeを通常の直接childとして列挙する`children()` / `descendants()`だけに
提供し、`ancestors()`には追加しません。

`descendants()`のfilterは結果だけに適用します。例えば`Mesh`を指定した場合、途中の
`Transform`は結果へ含めませんが、そのsubtreeは探索し、末端の`Mesh`を返します。
列挙順、instanced subtreeのpathごとの再訪、実行済みscene状態を都度読む契約は、
filterを指定しない場合と同じです。

`ancestors()`のfilterも結果だけに適用します。途中の祖先が条件に一致しなくても、
そこで探索を止めず、保持中pathのrootまで確認します。instanced nodeでは従来どおり
保持中の1つのpathだけを基準にします。

`ancestors(until=boundary)`は直接親から境界までをinclusiveに探索します。境界は
Python instanceや名前ではなく`MObject` identityで比較するため、別の`Nodes`や
`ModifierManager`から取得した同じscene nodeも指定できます。境界が保持中pathに
存在しなければ、途中までの結果ではなく`None`を返します。自分自身は祖先ではないため、
`until=self`も`None`です。

`until`による境界検出と`filter_type`による結果filterは独立しています。境界がfilterに
一致しなくても発見済みとして探索を終了し、その境界だけを結果から除外します。
この場合、境界が見つかってfilter結果が0件なら空tuple、境界自体が見つからなければ
`None`です。`until`省略時または`None`では従来どおりtupleを返し、DAG指定時は
`tuple[T, ...] | None`となるoverloadを公開します。

`descendant_chain()`は`descendants()`とは異なる探索規則を持つ独立メソッドです。
例えば`child_index=1`なら、rootでも次の階層でもindex 1だけを選びます。ある階層に
index 1が存在しなければ、index 0などへfallbackせず、そこで終了します。Transformと
Shapeを区別せずに選択し、選ばれたShapeも結果へ含めます。`child_index`は0以上のintだけを
受け取り、boolなどの非intは`TypeError`、負数は`ValueError`にします。

`descendant_chain(until=boundary)`は、選択された固定child indexのchain上だけを探索し、
境界までをinclusiveに返します。境界が別indexの兄弟や別subtreeに存在しても、その方向へは
探索せず`None`を返します。境界比較は`ancestors(until=...)`と同じく`MObject` identityを
使うため、別の`Nodes`や`ModifierManager`から取得した同じscene nodeも指定できます。
自分自身はchainに含めないため、`until=self`は`None`です。未実行の`MDagModifier`変更も
共通のtraversal契約どおり`do_it_dag()`まで探索へ反映しません。`until`省略時または
`None`では従来どおり`tuple[DAG, ...]`、DAG指定時は`tuple[DAG, ...] | None`を返します。

親変更は `set_parent()` で現在の `MDagModifier` に積みます。
初期値では local transform を維持するため、親の transform に応じて world transform が変わります。

```python
child.set_parent(parent)
mod.do_it_dag()
```

`Transform.set_parent()` では、親変更時の world transform を維持できます。
自身または自身の子孫を親にする循環操作は、同じ `ModifierManager` に積まれた
未実行の作成・親変更も含め、modifierへ積む前に拒否します。

```python
child.set_parent(
    parent,
    preserve_world_transform=True,
)
mod.do_it_dag()
```

ワールド直下への親変更は Transform 専用です。

```python
child.set_parent_to_world()
mod.do_it_dag()
```

world transform を維持する場合は、次のように指定します。

```python
child.set_parent_to_world(preserve_world_transform=True)
mod.do_it_dag()
```

インスタンス DAG は階層パスが複数あるため、`parent`、`set_parent()`、`set_parent_to_world()` は `RuntimeError` にします。
すべての直接の親を調べる場合は `parents` を使用します。
`children()` はMObject中心で直接の子を取得するため、instanced childも取得できます。
返されたnodeの保持pathは従来どおり`MDagPath.getAPathTo()`が選んだ1つです。
`ancestors()` はinstanced nodeでも例外にせず、同じく`getAPathTo()`で保持した
1つのpathを基準に祖先を列挙します。すべての直接親が必要な場合は`parents`を使います。
`descendants()` はMayaのdepth-first traversalと同様に、instanced subtreeへ
複数のDAG pathから到達する場合はpathごとに再訪します。そのため、同じ`MObject`を
包むnodeが結果に複数回現れることがあります。

`full_path` は保持中の `MDagPath` からアクセスごとに取得します。
親変更や rename の確定、および undo / redo 後も現在のフルパスを返します。

## Transform / Joint の回転集約

`Transform` は、現在評価されている `rotateAxis` と `rotate` の回転を一方へ
集約できます。集約後もlocal matrixは維持され、集約先以外の回転値は
`(0.0, 0.0, 0.0)`になります。

```python
transform.rotation_to_rotate()
# または
transform.rotation_to_rotate_axis()
mod.do_it_dg()
```

`Joint` では `rotateAxis`、`rotate`、`jointOrient` の3つをすべて合成します。
継承する2メソッドに加えて、`jointOrient`への集約も利用できます。

```python
joint.rotation_to_rotate()
joint.rotation_to_rotate_axis()
joint.rotation_to_joint_orient()
mod.do_it_dg()
```

## 姿勢を維持した回転値の設定

`Transform`では、現在の姿勢を維持したまま`rotateAxis`または`rotate`へ
任意の回転値を設定できます。メソッド名の`with`より後ろにある属性が、
設定による回転差分を吸収します。

```python
transform.set_rotate_axis_with_rotate((10.0, 20.0, 30.0))
transform.set_rotate_with_rotate_axis(40.0, 50.0, 60.0)
mod.do_it_dg()
```

`Joint`では継承する上記2メソッドに加えて、`jointOrient`と`rotate`の間でも
同じ操作を利用できます。

```python
joint.set_joint_orient_with_rotate((10.0, 20.0, 30.0))
joint.set_rotate_with_joint_orient(40.0, 50.0, 60.0)
mod.do_it_dg()
```

設定対象には指定値がそのまま入り、補償先だけが姿勢維持に必要な値へ変わります。
`Joint`で`rotateAxis`と`rotate`の間を補償する場合は`jointOrient`を変更せず、
`jointOrient`と`rotate`の間を補償する場合は`rotateAxis`を変更しません。
変更しない第三の回転属性は、lockや入力接続があっても検証対象に含めません。

補償値は同じ回転を表すEuler解のうち、補償先の現在値に近い解を選びます。
これにより、姿勢維持に不要な`360`度単位の変化を抑えます。
入力はdegree単位で、3要素sequenceまたは3つの数値として指定できます。

回転はEuler値の成分加算ではなく、Mayaの回転積と同じ順序でquaternionとして
合成・補償します。`rotate`の計算結果は現在の`rotateOrder`でEuler値へ変換し、
`rotateAxis`と`jointOrient`の計算結果は固定XYZ順で変換します。

値設定は現在の`MDGModifier`へ積まれ、各メソッドは自身を返します。
同じmodifierへ積んだ未実行の値設定は回転計算から読み取れないため、先行する
値設定がある場合は、操作前に`mod.do_it_dg()`で確定してください。

各操作で変更する回転plugまたはその子plugがlockされている場合や、animation curveを
含む入力接続を持つ場合は、変更を積む前に`RuntimeError`を送出します。接続解除、
keyframe削除、lock解除は自動実行しません。操作時点のlocal matrixは維持されますが、
回転属性の役割が変わるため、その後のrotate操作やIKに対する意味まで維持する操作では
ありません。

### 回転積と補償式（開発者向け）

実装では、`rotateAxis`、`rotate`、`jointOrient`から得たquaternionをそれぞれ
`A`、`R`、`J`と表し、回転部分を次の積として扱います。

- Transform: `Q = A * R`
- Joint: `Q = A * R * J`

`A`と`J`は固定XYZ順、`R`は現在の`rotateOrder`でEuler値とquaternionを
相互変換します。指定値を`A_target`、`R_target`、`J_target`としたとき、
各メソッドの補償値は次の式で求めます。

| メソッド | 補償式 | 変更しない属性 |
| --- | --- | --- |
| `set_rotate_axis_with_rotate(A_target)` | `R_new = inverse(A_target) * A * R` | Jointの`jointOrient` |
| `set_rotate_with_rotate_axis(R_target)` | `A_new = A * R * inverse(R_target)` | Jointの`jointOrient` |
| `set_joint_orient_with_rotate(J_target)` | `R_new = R * J * inverse(J_target)` | `rotateAxis` |
| `set_rotate_with_joint_orient(R_target)` | `J_new = inverse(R_target) * R * J` | `rotateAxis` |

`rotation_to_*()`も同じ回転積を使用し、集約先以外を単位回転にしたうえで
集約先のEuler値へ変換します。積順またはEuler変換順を変更する場合は、全6種類の
`rotateOrder`についてlocal matrix維持とundo / redoを検証してください。

## DAG の行列変換

`DAG` は、2つのDAGノード間で行列を変換する共通メソッドを持ちます。

```python
relative_tm = src_dag.get_relative_matrix(dst_dag)
local_tm = src_dag.get_local_matrix(dst_dag)
```

- `get_relative_matrix(dst_dag)`
  - src の行列を dst 自身の空間で表した `TransformMatrix` を返します。
  - `src.worldMatrix * dst.worldInverseMatrix` に相当します。
- `get_local_matrix(dst_dag)`
  - src の `worldMatrix` を再現するdst用local行列を返します。
  - `src.worldMatrix * dst.parentInverseMatrix` に相当します。
  - `parentInverseMatrix` を通じて、dst の `offsetParentMatrix` も補正されます。

どちらも各 `MDagPath.instanceNumber()` に対応する matrix plug を使います。戻り値の分解方法とmatrix plugからの直接取得については、[TransformMatrix](../transform_matrix.md) を参照してください。

シーン上に既に存在するノードは `nodes.existing` で対応する `NodeOperator` に変換できます。

```python
from maya import cmds

import bd_util as bdu

cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

nodes = bdu.Nodes()
node = nodes.existing("test_plus_minus_ave")
node.input1D[0].set(10.0)
nodes.modifier_manager.do_it_dg()
```

`nodes.existing` は既存ノードを包むだけなので、初期値では extra attribute を自動追加しません。
必要な場合は `nodes.existing("nodeName", auto_add_attr=True)` のように指定します。

内部の `ExistingNode` は生成済みの DG / DAG / transform / shape class から node type を解決します。
そのため、既存の mesh shape や camera shape も対応する `NodeOperator` として包めます。

nodeType を呼び出し側で明示したい場合は、`nodes.existing` の型別メソッドを使用できます。

```python
import bd_util as bdu

modifier_manager = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=modifier_manager)
node = nodes.existing.decomposeMatrix("test_decompose_matrix")
```

型別メソッドは実行時に対象 class を lazy import し、`existing_node.pyi` では通常の nodeType に対して具体的な戻り値型を公開します。
`nodes.existing` についても `nodes.pyi` で同じ具体的な戻り値型を公開します。
この例の `node` は IDE 上でも `DecomposeMatrix` として扱われます。
Maya 上の実際の nodeType が指定したメソッドと異なる場合は `TypeError` を送出します。
自動判定する `nodes.existing("nodeName")` と型を明示する `nodes.existing.decomposeMatrix("nodeName")` は、同じ既存ノード変換処理を共有します。

transform 派生 node は、既存 node の具体型対応と作成 API を分けて段階公開します。
`ikHandle` / `ikEffector` は `nodes.existing.ikHandle()` /
`nodes.existing.ikEffector()` から具体型として利用できますが、作成には専用の
初期化手順が必要なため `nodes.create` には公開しません。
constraint 系14種も `nodes.existing.aimConstraint()` /
`nodes.existing.parentConstraint()` などから具体型として利用できます。
これらも専用 command や接続を伴うため `nodes.create` には公開しません。
field / emitter 系11種も `nodes.existing.airField()` /
`nodes.existing.fluidEmitter()` などから具体型として利用できます。
これらも dynamics 用の初期化や接続を伴うため `nodes.create` には公開しません。
dynamics / deformer 周辺の5種も `nodes.existing.nucleus()` /
`nodes.existing.primitiveFalloff()` などから具体型として利用できます。
これらも専用の作成手順や接続を伴うため `nodes.create` には公開しません。
HIK 系5種も `nodes.existing.hikFKJoint()` /
`nodes.existing.hikHandle()` などから具体型として利用できます。
`HikFKJoint` は `Joint`、`HikHandle` は `IkHandle` の継承関係も維持します。
scene / utility 系6種も `nodes.existing.dagContainer()` /
`nodes.existing.lookAt()` などから具体型として利用できます。
`LookAt` はnative継承に合わせて `AimConstraint` の派生型として扱います。
VarGroup 系5種も `nodes.existing.curveVarGroup()` /
`nodes.existing.meshVarGroup()` などから具体型として利用できます。
5種共通の抽象native基底は `BaseGeometryVarGroup` として型階層に保持します。
特殊transformの `ufeProxyTransform` / `unknownTransform` も
`nodes.existing` から具体型として利用できます。`UfeProxyTransform` では、
各instanceへ追加される `ufePath` も静的なfieldとして公開します。

transformでもshapeでもない汎用DAGの `unknownDag` も、
`nodes.existing.unknownDag()` から `UnknownDag` として利用できます。Mayaは
`unknownDag` の作成時に親Transformも自動作成するため、戻り値と命名の契約が明確な
`nodes.create` には公開しません。

`NodeOperator` は内部で `m_obj` と lazy な `MFnDependencyNode` を持ちます。

`fn_node` は初回アクセス時に作られ、以降はキャッシュされます。

## キャッシュ方針

速度改善のため、次のものをキャッシュしています。

- `NodeOperator.fn_node`
- `NodeOperator._plug_cache`
- `PlugOperator.plug`
- indexed plug access の `plug[index]`
- `connect_next_index()` 用の next index

alias や child plug は同じ logical plug を指す場合、同じ `PlugOperator` instance を返すことを重視します。

## 文字列アクセス

現状の `NodeOperator.__getitem__()` は `getattr(self, key)` 相当です。

過去には `"attrName[0].subAttr"` のような文字列パス解析を想定していた形跡がありますが、現時点では active な仕様ではありません。

## 関連ドキュメント

- [attributes.md](attributes.md)
- [core.md](core.md)
- [generator.md](generator.md)
- [modifier_manager.md](modifier_manager.md)
- [testing.md](testing.md)
- [roadmap.md](roadmap.md)
