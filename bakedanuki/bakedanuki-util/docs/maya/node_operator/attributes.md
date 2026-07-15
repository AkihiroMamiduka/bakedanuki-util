# Attributes

このページは `NodeOperator` の attribute / plug 周辺仕様をまとめます。

## 3 つの役割

### AttributeField

`AttributeField` は descriptor です。

ノードクラス定義に置かれ、アクセス元に応じて `AttrOperator` または `PlugOperator` を生成します。

```python
class MyNode(NodeOperator):
    myValue = AddAttr.at.double(default_value=1.0)
```

### AttrOperator

`AttrOperator` はアトリビュート定義側の情報を持ちます。

主な情報は次の通りです。

- `node_cls`
- `long_name`
- `short_name`
- `attr_path`
- `parent_attr_path`
- `multi`
- `extra`
- `default_value`
- `min_value` / `max_value`
- `soft_min_value` / `soft_max_value`
- `child_index`

### PlugOperator

`PlugOperator` は Maya scene 上の plug 操作を担当します。

主な操作は次の通りです。

- `get()`
- `set()`
- `set_direct()`
- `connect()`
- `connect_next_index()`
- `disconnect()`
- `keyframe`
- `add_attr()`
- `cmds_add_attr()`

`set()` は基本的に `ModifierManager.dg_mod` 経由で編集します。

`set_direct()` は `MPlug` へ即時反映します。undo には参加しません。

## plug access

```python
node.attr
node.attr.child
node.multiAttr[0]
node.multiAttr[next]
node.multiAttr[0].child
```

`next` は Python builtin の `next` sentinel を利用します。

```python
src.output.connect_next_index(dst.multiInput)
src.output > dst.input
src.output >> dst.multiInput
```

`connect()` を明示的に呼ぶ方が、演算子経由より意図と速度の両面で分かりやすい場面があります。

## extra attribute

extra attribute は `AddAttr` から定義します。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr

class MyNode(NodeOperator):
    weight = AddAttr.at.double(default_value=1.0)
    offset = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])
    rotation = AddAttr.at.double_angle3(default_value=[0.0, 0.0, 0.0])
    orient = AddAttr.at.quat()
```

Python class 上の field 名は、通常そのまま Python 側の access 名と Maya attribute の `longName` になります。

```python
class MyNode(NodeOperator):
    weight = AddAttr.at.float(default_value=1.0)

node.weight
# Maya attribute: weight
```

Maya 側の名前だけを Python 側の access 名と変えたい場合は、`long_name` / `short_name` を指定します。

```python
class MyNode(NodeOperator):
    weight = AddAttr.at.float(
        default_value=1.0,
        long_name="blendWeight",
        short_name="bw",
    )

node.weight
# Maya attribute: blendWeight / bw
```

`AddAttr.at.*(...)` の factory は、主に次の共通 option を受け取ります。

- `long_name`
- `short_name`
- `multi`
- `readable`
- `writable`
- `category`

numeric / unit 系では `default_value`、`min_value` / `max_value`、`soft_min_value` / `soft_max_value` も指定できます。

これらの option は OpenMaya 経由の `add_attr()` と `cmds.addAttr()` 経由の `cmds_add_attr()` の両方で、実際の Maya attribute へ反映されます。

`multi=True` の場合は array attribute として作成され、通常の multi plug と同じように `node.attr[index]` / `node.attr[next]` でアクセスします。

`NodeOperator` 初期化時、`extra=True` の field は対象ノードに存在しなければ自動で追加されます。

`cmds_add_attr()` が必要な型は `cmds` 経由、それ以外は OpenMaya 経由の `add_attr()` を使います。

### extra enum attribute

追加アトリビュートの enum は、`PlugOperator` と `field` だけで定義します。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr


class SpaceModePlugOperator(AddAttr.define.at.enum.plug_operator):
    __slots__ = ()

    LOCAL = 0
    WORLD = 1

    NAME_MAP = {
        LOCAL: "Local",
        WORLD: "World",
    }


class SpaceModeField(
    AddAttr.define.at.enum.field[SpaceModePlugOperator]
):
    __slots__ = ()


class MyNode(NodeOperator):
    spaceMode = SpaceModeField()
```

この形では追加アトリビュート用の `AttrOperator` を明示的に定義する必要はありません。

`node.spaceMode` は `SpaceModePlugOperator` として補完されます。

```python
node.spaceMode.LOCAL
node.spaceMode.name_by_index(node.spaceMode.WORLD)
node.spaceMode.index_by_name("Local")
```

Maya に作成される enum label は `SpaceModePlugOperator.NAME_MAP` から作られます。

`NAME_MAP` は Maya 上の表示名と enum index の対応です。

追加 enum では `PlugOperator` 側に定義します。

`AddAttr.define.at.enum` は追加アトリビュート用の enum 定義として、`field` と `plug_operator` のみを公開します。

`AddAttr.define.at.enum.field[...]` の型引数は IDE 補完に使われるため、省略せずに記述します。

### extra compound attribute

追加アトリビュートの compound も、基本方針は enum と同じです。

`PlugOperator` と `field` だけを定義し、追加アトリビュート用の `AttrOperator` は明示的に定義しません。

```python
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr


class SpaceOptionDetailPlugOperator(
    AddAttr.define.at.compound.plug_operator
):
    __slots__ = ()

    visible = AddAttr.at.bool(default_value=True)
    blend = AddAttr.at.float(default_value=0.5, min_value=0.0, max_value=1.0)


class SpaceOptionDetailField(
    AddAttr.define.at.compound.field[SpaceOptionDetailPlugOperator]
):
    __slots__ = ()


class SpaceOptionPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    enabled = AddAttr.at.bool(default_value=False)
    weight = AddAttr.at.float(default_value=1.0, min_value=0.0)
    detail = SpaceOptionDetailField()
    offset = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])
    aim = AddAttr.at.double_angle3(default_value=[0.0, 0.0, 0.0])


class SpaceOptionField(
    AddAttr.define.at.compound.field[SpaceOptionPlugOperator]
):
    __slots__ = ()


class MyNode(NodeOperator):
    spaceOption = SpaceOptionField()
```

`node.spaceOption` は `SpaceOptionPlugOperator` として補完されます。

そのため、子アトリビュートも plug から直接辿れます。

```python
node.spaceOption.enabled
node.spaceOption.weight
node.spaceOption.detail.visible
node.spaceOption.detail.blend
node.spaceOption.offset.x
node.spaceOption.aim.z
```

compound child でも、通常は Python class 上の field 名が Python 側の access 名と Maya child attribute の `longName` になります。

```python
class SpaceOptionPlugOperator(AddAttr.define.at.compound.plug_operator):
    __slots__ = ()

    cmp1Float = AddAttr.at.float(default_value=1.0)
    cmp1Double3 = AddAttr.at.double3(default_value=[0.0, 0.0, 0.0])


node.spaceOption.cmp1Float
node.spaceOption.cmp1Double3.x
```

child の Maya 名だけを変えたい場合も `long_name` / `short_name` を使えますが、その場合も Python 側の access 名は field 名のままです。

Maya attribute の作成は `CompoundPlugOperator.add_attr()` が OpenMaya 経由で行います。

compound child の中にさらに compound child を定義できます。

その場合も、各階層の field は `AddAttr.define.at.compound.field[...]` で定義し、型引数にはその階層の `PlugOperator` を渡します。

custom scalar compound も child として定義できます。

現行で対象になる主な型は `double2` / `double3` / `double4` / `quat` / `float2` / `float3` / `long2` / `long3` / `short2` / `short3` / `double_linear2` / `double_linear3` / `double_angle2` / `double_angle3` / `float_linear2` / `float_linear3` / `float_angle2` / `float_angle3` です。

`double_angle3` は Maya 上では親 `double3`、子 `doubleAngle` として作成されます。

現時点では OpenMaya で compound child として作成できる型を対象とし、未対応の child 型は `UnsupportedOperationError` にします。

`AddAttr.define.at.compound` は追加アトリビュート用の compound 定義として、`field` と `plug_operator` のみを公開します。

`AddAttr.define.at.compound.field[...]` の型引数は IDE 補完に使われるため、省略せずに記述します。

## custom scalar compound

compound 系の custom 実装は `define/custom/at/scalar_compound` 配下にあります。

現行で主に扱う型は次の通りです。

- numeric compound
  - `double2`
  - `double3`
  - `double4`
  - `float2`
  - `float3`
  - `long2`
  - `long3`
  - `short2`
  - `short3`
- unit compound
  - `double_linear2`
  - `double_linear3`
  - `double_angle2`
  - `double_angle3`
  - `float_linear2`
  - `float_linear3`
  - `float_angle2`
  - `float_angle3`
- semantic alias
  - `quat`

`quat` は低レベル型としては `double4` 相当で、意味付き alias として扱います。

default は未指定時に `[0.0, 0.0, 0.0, 1.0]` です。

## compound get / set

compound の `get()` は child 値の list を返します。

```python
node.offset.get()
# [1.0, 2.0, 3.0]
```

`set()` と `set_direct()` は、展開引数と sequence の両方を受け取ります。

```python
node.offset.set(1.0, 2.0, 3.0)
node.offset.set([1.0, 2.0, 3.0])
node.offset.set((1.0, 2.0, 3.0))

node.offset.set_direct(1.0, 2.0, 3.0)
```

要素数が child 数と一致しない場合は `TypeError` です。

この validation は child を一部だけ変更してしまう事故を避けるため、実際の set 前に行います。

## limit 設定

custom scalar compound は child attribute に対して次の public method を持ちます。

```python
node.offset.set_min([-1.0, -2.0, -3.0])
node.offset.set_max(10.0)
node.offset.set_soft_min(0.0)
node.offset.set_soft_max([1.0, 2.0, 3.0])
```

値は scalar または child 数と同じ長さの sequence を受け取ります。

- scalar
  - 全 child に同じ値を設定します。
- sequence
  - child ごとに個別値を設定します。

unit 系では、内部で Maya API に渡す形式へ変換してから設定します。

## child names

通常の child 名は suffix から生成されます。

```text
longNameX / shortNamex
longNameY / shortNamey
longNameZ / shortNamez
longNameW / shortNamew
```

既存 Maya attribute に合わせたい場合は `CHILD_ATTR_NAMES` で明示します。

`Transform.translate` / `Transform.rotate` / `Transform.scale` はこの方式で Maya 標準名に合わせます。

```text
translate / t
translateX / tx
translateY / ty
translateZ / tz
```

## lookup

`lookup_attr_cls(node, attr)` は Maya 上の既存 attribute から対応する `AttrOperator` class を返します。

floating point compound は parent の `attributeType` と child の `attributeType` を見て解決します。

child 型が混在している場合、現状は unsupported として `TypeError` を出します。

`double4` かつ long name に `quat` が含まれる場合は `Quat4AttrOperator` に解決します。

## 注意点

- `addr` は Maya 側に存在しますが、基本的に使用しない attribute のため `AddAttr` 公開や自動 add_attr 対応の対象外です。
- `set_direct()` は undo 対応外です。
- `NodeOperator.__getitem__()` の文字列パス解析は現状 active ではありません。
- `lookup.py` は新しい型を追加したら追従が必要です。
