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
  - `Transform` ノード定義です。
- `python/bd_util/maya/node/operator/attr/_core.py`
  - `AttributeField` / `AttrOperator` / `PlugOperator` の中核です。
- `python/bd_util/maya/node/operator/attr/extra/add_attr.py`
  - extra attribute 作成用の `AddAttr` API です。
- `python/bd_util/maya/node/operator/attr/lookup.py`
  - Maya 上の既存アトリビュートから対応する `AttrOperator` を推定します。
- `python/bd_util/maya/node/modifier/_core.py`
  - `ModifierManager` です。
- `python/bd_util/maya/node/nodes.py`
  - `Nodes` です。ノード作成と既存ノード変換で同じ `ModifierManager` を共有する統合入口です。
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
    OpenMaya["maya.api.OpenMaya"]

    Nodes --> NodeCreator
    Nodes --> ExistingAccessor
    Nodes --> ModifierManager
    ExistingAccessor --> ExistingNode
    NodeCreator --> NodeOperator
    NodeCreator --> ModifierManager
    ExistingNode --> NodeOperator
    ExistingNode --> ModifierManager
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

内部の `NodeCreator` は DG ノード名と transform 系 DAG ノード名を lazy import し、`NodeOperator.create()` を呼びます。
生成メソッド名は `multiplyDivide` のような Maya nodeType 名に合わせています。
`create()` には `plus_minus_average` のような snake_case と、`multiplyDivide` のような Maya nodeType 名のどちらでも渡せます。
IDE 補完用に `.pyi` を用意し、主要な生成メソッドの戻り型が各 `NodeOperator` クラスとして見えるようにしています。

`transform` / `joint` は `nodes.create` から作成できます。
shape 系ノードは transform 親の扱いが絡むため、現時点では作成 API には出していません。
ただし `nodes.existing` 用の class 解決対象には含めています。

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
