# Node Generator

このページは `src/bd_util/_dev/maya/node/operator/node/generate.py` の現行仕様をまとめます。
Generator は Maya の node type と attribute query 結果から、`NodeOperator` 用の Python class を生成する開発用ツールです。

## 目的

主な目的は、Maya 標準 DG ノードを `NodeOperator` として扱える形へ機械的に変換することです。

- Maya の node type から `DG` 継承 class を生成する。
- compound attribute が必要な場合は `attr.define.node_attr` 側に専用 Field / AttrOperator / PlugOperator を生成する。
- 生成後の差分を git で確認し、手書き実装との差分や未対応型を炙り出す。
- 生成できない attribute は TODO コメントとして残し、後続対応しやすくする。

## 入力

入力は `AttrInfo` の list です。
通常は `bd_util.maya.attr.query.get_attribute_infos(node_type)` から取得します。

`AttrInfo` では、主に次の情報を参照します。

- `long_name`
- `short_name`
- `attribute_type`
- `data_type`
- `enum_name`
- `multi`
- `number_of_children`
- `parent`
- `path_name`
- `enforcing_unique_name`

`path_name` が存在する場合、Generator は生成コード上の canonical な Maya attribute path として `path_name` を優先します。
これは `hierarchyTestNode4` のように、通常の `longName` だけでは実際の attribute path を正しく扱いにくいケースへの対応です。

## 出力

`generate_node_class_file(node_type, src_dir)` は、`src_dir` 以下に次のファイルを生成します。

```text
bd_util/maya/node/operator/node/dg/<node_type_snake>.py
bd_util/maya/node/operator/attr/define/node_attr/<node_type_snake>.py
```

`node_attr` 側のファイルは、compound attribute 用の専用 class が必要な場合に出力されます。
単純な scalar / typed / enum attribute だけで構成できる場合は、node class 側だけで完結します。

## 命名規則

node type は次のように変換します。

```text
plusMinusAverage -> PlusMinusAverage
plusMinusAverage -> plus_minus_average.py
```

attribute 名は Python identifier として安全になるように変換されます。

- Python keyword は末尾に `_` を付ける。
  - `from` -> `from_`
- 数字始まりは英単語 prefix に変換する。
  - `3d` -> `threed`
  - `11w` -> `one1w`
- 使用できない記号は `_` に変換する。
- `NodeOperator` の既存 API と衝突する field 名は `_` を追加して回避する。
  - `name` -> `name_`
  - `create` -> `create_`

Maya 側の本来の `long_name` / `short_name` と Python field 名が異なる場合は、Field constructor に `long_name=` / `short_name=` を明示します。

```python
name_ = DataStringField(long_name="name", short_name="nm")
nm = name_
```

## short_name alias

`short_name` alias は、次の条件を満たす場合だけ生成します。

- `short_name` が存在する。
- `short_name != long_name`。
- `short_name` に `.` を含まない。
- `short_name` が数字始まりではない。
- `long_name` / `short_name` に `deprecated` を含まない。

このため、Maya の内部的な dotted short name や数字始まり alias は Python descriptor としては出力しません。

## attribute type 解決

`attribute_type` は `_AT_TYPE_MAP` で Field class へ解決します。

例:

- `double` -> `DoubleField`
- `float3` -> `Float3Field`
- `message` -> `MessageField`
- `matrix` -> `MatrixField`

`data_type` は `_DT_TYPE_MAP` で Field class へ解決します。

例:

- `matrix` -> `DataMatrixField`
- `string` -> `DataStringField`
- `vectorArray` -> `DataVectorArrayField`

`attribute_type == "typed"` の場合に加えて、Maya の query 結果で `attribute_type is None` だが `data_type` が取得できる場合も `_DT_TYPE_MAP` を使います。
これにより、`timeEditorClip` の `rootObjLocalXform` や `jiggle` の `cachedInputPositionList` のような attribute を TODO ではなく typed data field として生成できます。

`cmds.attributeQuery(..., attributeType=True)` が `None` を返す場合でも、`MFnNumericAttribute` / `MFnUnitAttribute` / `MFnMatrixAttribute` などから型を復元できる場合があります。
`bd_util.maya.attr.query` はこの OpenMaya fallback を使い、multi compound の内部 leaf のような attribute も `FloatField` / `DoubleField` / `DoubleLinearField` などとして解決します。

解決できない attribute は TODO コメントとして残します。
全 DG 生成では、NodeOperator の通常利用対象から外れる特殊ノードを skip するため、生成 snapshot 側に TODO が残らない状態を目指します。

## skipped node type

一部の DG node type は、生成対象から意図的に除外します。

現状の skip 対象は次の通りです。

- `nodeGraphEditorInfo`
  - Node Editor の UI 状態保存寄りの内部ノードです。
  - standalone mayapy では一部 attribute の型情報を十分に取得できません。
  - 通常の NodeOperator 操作対象としての実用性が低いため、全量生成から除外します。

調査目的で明示的に生成したい場合は `include_skipped=True` を指定します。

```python
generate_node_class_file(
    node_type="nodeGraphEditorInfo",
    src_dir=path,
    include_skipped=True,
)
```

## enum 生成

enum attribute は専用の `EnumPlugOperator` / `EnumAttrOperator` / `EnumField` を node class 内に生成します。

```python
class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_OPERATION = 0
    SUM = 1
    SUBTRACT = 2
    AVERAGE = 3
```

Maya の enum label に explicit value が含まれる場合は、それを反映します。

```text
Waiting-Normal=8
```

同じ label が複数存在し、Python member 名が重複する場合は、値 suffix を付けて衝突を避けます。

```python
RGBA = 0
RGBA_2 = 2

NAME_MAP = {
    RGBA: "RGBA",
    RGBA_2: "RGBA",
}
```

## compound 生成

compound parent と child の情報から、専用の compound class を生成します。

生成対象になる主な compound は次の通りです。

- `compound`
- `lightData`
- numeric scalar compound
  - `double2`
  - `double3`
  - `double4`
  - `float2`
  - `float3`
  - `long2`
  - `long3`
  - `short2`
  - `short3`
- quat-like compound

child の型が混在する場合や、対応する base class が存在しない場合は TODO 扱いにします。
混在型を旧実装へ fallback する方針ではありません。

## quat-like compound

次の条件を満たす attribute は quat-like compound として扱います。

- parent の `attribute_type` が `compound` または `double4`。
- parent の long/path name に `quat` を含む。
- child 数が 4。
- child の `attribute_type` がすべて `double`。

この場合は `QuatCompoundBaseField` 系を継承する生成 class にします。
低レベル型としては double4 相当ですが、将来的な quat 用メソッド追加を見越して quat 専用 base を挟む方針です。

## child alias

non-multi compound parent では、親経由だけでなく node 直下から child へアクセスできる alias も生成します。

```python
output3D = Output3DField()
o3 = output3D

output3Dx = output3D.output3Dx
o3x = output3Dx
```

この alias は同じ logical plug を指す場合、同じ `PlugOperator` instance を返すことを期待します。

## unsupported attribute

Generator は未対応 attribute を削除しません。
解決できない場合は、node class 内に TODO コメントを残します。

```python
# TODO: attrName (attributeType=None, dataType=None) は未対応のため手動で追加してください
```

ただし `attributeType` に `<` / `>` を含む query 結果は、生成対象から除外します。
これは Maya 側の特殊な表示や未整理の型情報が混ざり、Python class として安全に生成しづらいためです。

また、`nodeGraphEditorInfo` のように node type 自体が NodeOperator の通常対象外と判断できる場合は、attribute TODO を残すのではなく全量生成から node type ごと skip します。

## 実行例

Maya Script Editor または mayapy 上で実行します。

```python
from bd_util._dev.maya.node.operator.node.generate import generate_node_class_file

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\src"

node_types = [
    "plusMinusAverage",
    "wtAddMatrix",
    "composeMatrix",
]

for node_type in node_types:
    generate_node_class_file(
        node_type=node_type,
        src_dir=path,
    )
```

`mayapy` で単体実行する場合は、必要に応じて `maya.standalone.initialize(name="python")` を先に呼びます。

```python
import maya.standalone
maya.standalone.initialize(name="python")
```

## 検証

Generator まわりの pytest は次にあります。

```text
tests/dev/maya/node/operator/node/test_generate.py
```

代表的な検証項目は次の通りです。

- `plusMinusAverage` の compound / enum 生成。
- quat-like compound の判定。
- `path_name` 優先。
- unsafe identifier / reserved name の escape。
- deprecated / 数字始まり / dotted short alias の skip。
- duplicate enum member name の suffix。
- `attribute_type is None` かつ `data_type` ありの解決。

全体検証では、生成済み snapshot の構文チェックも併用します。

```python
from pathlib import Path

errors = []
for path in Path("generate_test/src").rglob("*.py"):
    try:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    except SyntaxError as exc:
        errors.append((path, exc.lineno, exc.msg))

print(errors)
```

## 現状の注意点

- `generate_test/src` は生成結果確認用の snapshot です。後で削除予定ですが、現状は generator 差分確認のため git 管理しています。
- `attributeType=None, dataType=None` の attribute はまだ自動解決できません。
- 生成後は必ず git diff を確認します。
- 既存手書き class を上書きする場合は、生成差分が意味的に一致しているか確認します。
