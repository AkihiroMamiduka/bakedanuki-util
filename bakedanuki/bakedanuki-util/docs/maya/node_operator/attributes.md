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

すべての `PlugOperator` が持つ主な操作は次の通りです。

- `connect()`
- `connect_from()`
- `connect_next_index()`
- `disconnect()`
- `disconnect_from()`
- `src_plug()` / `src_name()` / `src_plug_name()`
- `dst_plugs()` / `dst_names()` / `dst_plug_names()`
- `keyframe`
- `add_attr()`
- `cmds_add_attr()`

値操作はplug型が対応するものだけを提供します。

- `get()`
- `set()`
- `set_direct()`

例えばscalar numericは`get()` / `set()`、typed matrixは`get()` /
`set_direct()`を持ち、message、generic、mixed compoundなど値操作へ
対応しない型にはこれらのmethodがありません。利用できない操作を
例外送出用methodとして残さないため、IDE補完にも表示されません。

`value` / `value_direct` propertyは提供しません。値操作は型注釈と
反映方法が明確な上記methodを使用します。

`set()` は `ModifierManager.dg_mod` 経由で編集します。

`set_direct()` は `MPlug` へ即時反映します。undo には参加しません。

### 値操作methodの実装規則

新しい`PlugOperator`型を追加するときは、その型で実行できる値操作だけを
具象class、または全派生classが同じ操作へ対応する共通基底classに実装します。

現在の代表的な対応関係は次の通りです。

| plug family | `get()` | `set()` | `set_direct()` |
| --- | --- | --- | --- |
| scalar numeric / enum / unit | yes | yes | 原則no |
| custom scalar compound | yes | yes | yes |
| matrix / floatMatrix attribute | yes | yes | no |
| string data | yes | yes | yes |
| numeric / array / matrix data | yes | no | yes |
| addr | yes | no | yes |
| message / generic / lightData / mixed compound | no | no | no |
| mesh / lattice / nurbs data | no | no | no |

未対応操作を、`NotImplementedError`や`UnsupportedOperationError`を送出するだけの
methodとして定義しません。`PlugOperator`や`DataTypePlugOperator`などの共通基底にも
値操作methodを置きません。これにより、実行できない操作がIDE補完へ現れることを
防ぎます。

公開する`get()` / `set()` / `set_direct()`には、対象となるMaya型、Python側の
値型、単位、ModifierManager経由か即時反映かをdocstringへ記載します。対応関係を
変更した場合はruntimeのcapability testとPyright contractも同時に更新します。

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
src.output.connect(dst.input)
dst.input.connect_from("src.output")
dst.input.connect_from(["src", "output"])
dst.input.disconnect_from("src.output")
dst.multiInput.connect_next_index(src.output)
```

`connect()` / `disconnect()` は接続元から接続先を指定します。
`connect_from()` / `disconnect_from()` は接続先から接続元を指定します。

## connection query

接続元は単一の `PlugOperator`、接続先は複数の `PlugOperator` として取得します。

```python
source = dst.input.src_plug()
source_node_name = dst.input.src_name()
source_plug_name = dst.input.src_plug_name()

destinations = src.output.dst_plugs()
destination_node_names = src.output.dst_names()
destination_plug_names = src.output.dst_plug_names()
```

接続元がない場合、`src_plug()` / `src_name()` / `src_plug_name()` は `None` を返します。
接続先がない場合、destination 系メソッドは空 tuple を返します。

`src_name()` / `dst_names()` は `NodeOperator.name`、
`src_plug_name()` / `dst_plug_names()` は `PlugOperator.plug_name` を返します。
同じノードの複数 plug が接続先の場合、`dst_names()` はノード名を重複させ、
3 つの destination 系メソッドで要素数と順序を揃えます。

接続照会は `MPlug.connectedTo()` と同じく、対象 plug 自身への直接接続だけを返します。
multi / compound の親 plug から element や child の接続は集約しません。

接続ノードの `NodeOperator` class で結果を絞り込めます。

```python
joint_source = dst.input.src_plug(
    filter_type=nodes.types.Joint,
)

exact_joint_destinations = src.output.dst_plugs(
    filter_type=nodes.types.Joint,
    include_subclasses=False,
)
```

`include_subclasses=True` が初期値です。
`False` の場合は、解決された `NodeOperator` の class が `filter_type` と完全一致する接続だけを返します。
接続があっても filter に一致しない場合は、source 系は `None`、destination 系は空 tuple を返します。
`filter_type` なしで `include_subclasses=False` を指定すると `ValueError` を送出します。

### connection query の設計境界

`filter_type` が判定するのは、直接接続されているノードです。
`unitConversion` などの中間ノードを通過して上流・下流を探索する機能ではありません。
将来 pass-through traversal を追加する場合も、直接接続を返す初期動作は維持し、
別の option または API として明示します。

接続先の `MPlug` は `ExistingNode` を経由して `PlugOperator` へ解決します。
このとき、照会元と同じ `ModifierManager` を引き継ぎ、既存ノードを変更しないよう
`auto_add_attr=False` で包みます。結果は接続先を改めて解決した wrapper であり、
別経路ですでに取得した `PlugOperator` との Python object identity は保証しません。
同じ plug かどうかは `is` ではなく `MPlug` を表す `plug` で比較します。

destination 系メソッドの順序は `MPlug.connectedTo()` の結果に従い、独自の sort は行いません。
同一の scene 状態では `dst_plugs()` / `dst_names()` / `dst_plug_names()` の要素を
同じ順序で対応させますが、この順序を接続作成順などの意味として扱わないでください。
再現可能な順序が必要な処理では、呼び出し側で `plug_name` などを key に sort します。

現在の `PlugOperator` への解決は、`ExistingNode` で型を解決でき、対象 attribute が
その `NodeOperator` / `AttributeField` に定義されていることを前提とします。
生成後に追加された未知の plug-in node type や runtime extra attribute など、
この前提を満たさない接続は `AttributeError` になる場合があります。
これは「接続なし」を表す `None` / 空 tuple とは別の状態です。
name 系メソッドも対応する plug query の結果から名前を取得するため、同じ解決境界を持ちます。
また、接続状態は scene 編集で変化するため、connection query の結果は cache しません。

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

### typed dataのdefault値

`MFnTypedAttribute`でdefault値に対応する型は、Python値をdata objectへ変換し、
その`MObject`を`MFnTypedAttribute.create()`のdefault引数へ渡します。attributeを
ノードへ追加してから`set_direct()`する方法は使いません。作成時に渡すことで、
現在値だけでなくattribute definitionのdefault値としてMayaへ保持されます。

`DataTypePlugOperator._add_attr_base()`は`default_object_factory`を受け取り、
現在はstring dataが`MFnStringData`による変換を提供します。`None`はdefault未指定を
表し、空文字列などのfalseyな値も有効なdefault値として扱います。

新しいtyped data型で`default_value`を公開する場合は、対応する`MFn*Data.create()`で
Python値から`MObject`を作るfactoryを実装し、`_add_attr_base()`へ渡します。
factoryを用意できない型では`default_value`を公開しません。

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

固定長かつ同種の scalar child で構成される compound の `get()` は、
attribute type に対応する immutable な専用値型を返します。

```python
import bd_util as bdu

result = node.offset.get()

isinstance(result, bdu.Double3)
result.x
result.y
result.z

x, y, z = result
result[0]
result.as_tuple()
```

専用値型は `bd_util.maya.value.scalar_compound` 以下に、attribute type の
継承関係が分かる package 構造で配置します。各専用値型は `bd_util` の
トップレベルからも公開します。

`bd_util` パッケージ内部で専用値型や関連 module を参照する場合は、
`from bd_util.maya...` のような package top 起点の import ではなく、
import 元の module を基準にした相対 import を使用します。
これは内部実装の規約であり、利用者向けコードでは従来どおり
`import bd_util as bdu` から公開 API を利用します。

主な対応は次の通りです。

- `double2/3/4` -> `Double2` / `Double3` / `Double4`
- `float2/3` -> `Float2` / `Float3`
- `long2/3` -> `Long2` / `Long3`
- `short2/3` -> `Short2` / `Short3`
- `double_linear2/3` -> `DoubleLinear2` / `DoubleLinear3`
- `float_linear2/3` -> `FloatLinear2` / `FloatLinear3`
- `double_angle2/3` -> `DoubleAngle2` / `DoubleAngle3`
- `float_angle2/3` -> `FloatAngle2` / `FloatAngle3`
- `quat` -> `Quat`

専用値型は `Sequence` として index access、slice、iteration、unpack、
`tuple()` / `list()` への変換に対応します。値は変更できず、hashable です。

初期実装では四則演算を持ちません。

```python
bdu.Double2(1.0, 2.0) + bdu.Double2(3.0, 4.0)
# TypeError
```

`set()` と `set_direct()` は、展開引数と sequence の両方を受け取ります。
専用値型も sequence としてそのまま渡せます。

```python
node.offset.set(1.0, 2.0, 3.0)
node.offset.set([1.0, 2.0, 3.0])
node.offset.set((1.0, 2.0, 3.0))
node.offset.set(bdu.Double3(1.0, 2.0, 3.0))

node.offset.set_direct(1.0, 2.0, 3.0)
```

専用値型同士の比較では、値に加えて型も一致する必要があります。
通常の list / tuple と比較したい場合は `tuple(result)`、`list(result)`、
またはテスト用途の `pytest.approx()` などを使用します。

mixed compound の `get()` は専用値型の対象外です。

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
