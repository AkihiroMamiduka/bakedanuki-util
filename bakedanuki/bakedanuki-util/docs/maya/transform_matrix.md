# TransformMatrix

`TransformMatrix` は、Maya の 4x4 transform 行列を合成・分解するための読み取り専用ラッパーです。

生成時点の行列値を保持するスナップショットとして動作します。元の plug や `MTransformationMatrix` を後から変更しても、既に作成した `TransformMatrix` の値は変わりません。

## 作成

公開APIから利用できます。

```python
from maya import cmds
from maya.api import OpenMaya as om
import bd_util as bdu

transform = cmds.createNode("transform", name="test")

from_name = bdu.TransformMatrix(f"{transform}.worldMatrix[0]")

selection = om.MSelectionList()
selection.add(f"{transform}.worldMatrix[0]")
from_plug = bdu.TransformMatrix(selection.getPlug(0))

from_matrix = bdu.TransformMatrix(om.MMatrix())
from_transformation = bdu.TransformMatrix(om.MTransformationMatrix())
```

コンストラクタは次の値を受け取ります。

- `TransformMatrix`
- `node.attr` 形式の matrix plug 名
- `MPlug`
- `MMatrix`
- `MTransformationMatrix`

matrix ではない plug を渡した場合は `TypeError` を送出します。

## 値の取得

```python
tm = bdu.TransformMatrix(f"{transform}.worldMatrix[0]")

translate = tm.translate  # DoubleLinear3(x, y, z)
rotate = tm.rotate        # DoubleAngle3(x, y, z) / XYZ order / degree
scale = tm.scale          # Double3(x, y, z)
shear = tm.shear          # Double3(xy, xz, yz)
quat = tm.quat            # Quat(x, y, z, w)
```

分解値は、対応するplugの `get()` と同じ値型を返します。

- `translate`: `DoubleLinear3`
- `rotate` / `get_rotate()`: `DoubleAngle3`
- `scale` / `shear`: `Double3`
- `quat`: `Quat`

これらは読み取り専用のsequence値で、`.x` / `.y` / `.z` / `.w` による成分取得、indexアクセス、アンパックに対応します。従来と同じtupleが必要な場合は `.as_tuple()` を使用します。

```python
x = tm.translate.x
x, y, z = tm.rotate
scale_tuple = tm.scale.as_tuple()
```

`translate` は既存のlinear plug APIと同じくcentimeter、`rotate` はangle plug APIと同じくdegreeです。

XYZ 以外の Euler 回転が必要な場合は `get_rotate()` で回転順序を指定します。

```python
rotate_zyx = tm.get_rotate(order="zyx")
```

対応する値は `xyz` / `yzx` / `zxy` / `xzy` / `yxz` / `zyx` です。大文字と小文字は区別しません。

生の OpenMaya 値が必要な場合は、コピーを取得できます。

```python
matrix = tm.matrix
transformation_matrix = tm.transformation_matrix
```

## Matrix plug からの取得

`MatrixPlugOperator.get()` と `DataMatrixPlugOperator.get()` は、現在の plug 値を `TransformMatrix` のスナップショットとして取得します。

```python
import bd_util as bdu

nodes = bdu.Nodes()
node = nodes.existing.transform("test")
world_matrix = node.worldMatrix[0]

tm = world_matrix.get()
matrix = tm.matrix
transformation_matrix = tm.transformation_matrix
translate = world_matrix.translate
rotate = world_matrix.rotate
rotate_zyx = world_matrix.get_rotate(order="zyx")
scale = world_matrix.scale
shear = world_matrix.shear
quat = world_matrix.quat
```

`DataMatrixPlugOperator` の各成分プロパティも、アクセス時点の plug 値から新しいスナップショットを作ります。複数成分を同じ評価時点の値として扱う場合は、`get()` を一度実行してから各成分へアクセスします。

```python
tm = node.worldMatrix[0].get()
translate = tm.translate
rotate = tm.rotate
scale = tm.scale
```

`MatrixPlugOperator.get()` と `DataMatrixPlugOperator.get()` は、どちらも常に `TransformMatrix` を返します。未設定のtyped matrix plugはmatrix data自体を持たないため、`get()`、plugの `transformation_matrix`、および各成分へアクセスすると `ValueError` を送出します。未設定状態にidentity matrixを補完することはありません。

## Matrix plug への設定

`MatrixPlugOperator.set()` と `DataMatrixPlugOperator.set_direct()` は、`TransformMatrix` / `MMatrix` / `MTransformationMatrix` を受け取ります。

```python
mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

src_node = nodes.existing.transform("src")
mult_matrix = nodes.create.multMatrix(name="mult_matrix")

src_world = src_node.worldMatrix[0].get()
mult_matrix.matrixIn[0].set(src_world)
mod.do_it_dg()
```

typed matrix plugの `set_direct()` は即時反映され、`ModifierManager` の undo / redo履歴には入りません。

## 行列積

`TransformMatrix` は `TransformMatrix` または `MMatrix` と `*` で乗算でき、新しい `TransformMatrix` を返します。`MMatrix * TransformMatrix` の順序にも対応します。計算は TRS の各値ではなく、保持している `MMatrix` で行います。

```python
src_wm = bdu.TransformMatrix(f"{src}.worldMatrix[0]")
dst_pim = bdu.TransformMatrix(f"{dst}.parentInverseMatrix[0]")

local_tm = src_wm * dst_pim
local_translate = local_tm.translate

maya_matrix = om.MMatrix()
right_result = local_tm * maya_matrix
left_result = maya_matrix * local_tm
```

この例の結果は、src のワールド行列を dst の親空間へ変換した行列です。

## DAG 間の行列変換

DAG の `get_relative_matrix()` は、self の行列を指定した dst 自身の空間で表します。

```python
relative_tm = src_dag.get_relative_matrix(dst_dag)
```

内部では、各DAGパスの `instanceNumber()` に対応する配列要素を使って次の計算を行います。

```python
src_world = src_dag.worldMatrix[src_index].get()
dst_world_inverse = dst_dag.worldInverseMatrix[dst_index].get()
relative_tm = src_world * dst_world_inverse
```

`get_local_matrix()` は、self の `worldMatrix` を再現するための dst 用local行列を返します。

```python
local_tm = src_dag.get_local_matrix(dst_dag)
```

計算は次のとおりです。

```python
src_world = src_dag.worldMatrix[src_index].get()
dst_parent_inverse = dst_dag.parentInverseMatrix[dst_index].get()
local_tm = src_world * dst_parent_inverse
```

Mayaの `parentMatrix` には dst の `offsetParentMatrix` が既に合成されています。その逆行列である `parentInverseMatrix` を使うため、`get_local_matrix()` の結果にも `offsetParentMatrix` の補正が含まれます。

`ModifierManager` に積んだノード作成や値設定は、行列を取得する前に `do_it_dag()` / `do_it_dg()` で実行してください。

## 逆行列

`inverse()` は逆行列を保持する新しい `TransformMatrix` を返します。

```python
inverse_tm = tm.inverse()
```

## 分解時の注意

行列から取得する translate / rotate / scale / shear は、行列に対する等価な分解結果です。元の transform ノードが持つ `rotatePivot`、`rotateAxis`、`jointOrient` などの個別属性を復元するものではありません。

また、行列自体は元ノードの `rotateOrder` を保持しません。`rotate` は XYZ として分解し、別の回転順序が必要な場合は `get_rotate()` を使用します。負スケールや shear を含む行列では、等価な分解が複数存在する場合があります。
