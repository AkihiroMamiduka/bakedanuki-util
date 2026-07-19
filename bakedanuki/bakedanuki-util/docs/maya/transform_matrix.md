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

translate = tm.translate  # (x, y, z)
rotate = tm.rotate        # XYZ order / degree
scale = tm.scale          # (x, y, z)
shear = tm.shear          # (xy, xz, yz)
quat = tm.quat            # (x, y, z, w)
```

すべての戻り値は `float` の tuple です。`rotate` は既存の angle plug API と同じく degree を返します。

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

## 行列積

`TransformMatrix` 同士を `*` で乗算すると、新しい `TransformMatrix` を返します。計算は TRS の各値ではなく、保持している `MMatrix` 同士で行います。

```python
src_wm = bdu.TransformMatrix(f"{src}.worldMatrix[0]")
dst_pim = bdu.TransformMatrix(f"{dst}.parentInverseMatrix[0]")

local_tm = src_wm * dst_pim
local_translate = local_tm.translate
```

この例の結果は、src のワールド行列を dst の親空間へ変換した行列です。

## 逆行列

`inverse()` は逆行列を保持する新しい `TransformMatrix` を返します。

```python
inverse_tm = tm.inverse()
```

## 分解時の注意

行列から取得する translate / rotate / scale / shear は、行列に対する等価な分解結果です。元の transform ノードが持つ `rotatePivot`、`rotateAxis`、`jointOrient` などの個別属性を復元するものではありません。

また、行列自体は元ノードの `rotateOrder` を保持しません。`rotate` は XYZ として分解し、別の回転順序が必要な場合は `get_rotate()` を使用します。負スケールや shear を含む行列では、等価な分解が複数存在する場合があります。
