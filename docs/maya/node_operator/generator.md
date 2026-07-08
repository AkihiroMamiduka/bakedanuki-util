# Node Generator

このページは `src/bd_util/_dev/maya/node/operator/node/generate.py` の現行仕様をまとめます。
Generator は Maya の node type と attribute query 結果から、`NodeOperator` 用の Python class を生成する開発用ツールです。

## 目的

主な目的は、Maya 標準 DG / DAG ノードを `NodeOperator` として扱える形へ機械的に変換することです。

- Maya の node type から `DG` / `DAG` / `Transform` / `Shape` 継承 class を生成する。
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
- `default_value`
- `min_value`
- `max_value`
- `soft_min_value`
- `soft_max_value`
- `readable`
- `writable`
- `category`
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
bd_util/maya/node/operator/node/dag/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/transform/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/shape/<node_type_snake>.py
bd_util/maya/node/operator/attr/define/node_attr/<node_type_snake>.py
```

`transform` 本体は transform 派生 node の基底でもあるため、`node_kind="transform"` で生成する場合だけ次の特殊な出力先になります。

```text
bd_util/maya/node/operator/node/dag/transform/_core.py
```

将来的に `shape` 本体を生成対象にする場合も、同じ理由で `dag/shape/_core.py` へ出力します。

`node_attr` 側のファイルは、compound attribute 用の専用 class が必要な場合に出力されます。
単純な scalar / typed / enum attribute だけで構成できる場合は、node class 側だけで完結します。

## node kind

`generate_node_class_code()` / `generate_node_class_file()` は `node_kind` を受け取ります。

```python
generate_node_class_file("plusMinusAverage", path, node_kind="dg")
generate_node_class_file("joint", path, node_kind="transform")
generate_node_class_file("mesh", path, node_kind="shape")
generate_node_class_file("transform", path, node_kind="transform")
```

指定できる値は次の通りです。

- `dg`
  - `node/dg` に出力し、`DG` を継承します。
- `dag`
  - `node/dag` に出力し、`DAG` を継承します。
- `transform`
  - `node/dag/transform` に出力し、`Transform` を継承します。
  - `node_type == "transform"` の場合は `_core.py` に出力し、`DAG` を継承します。
  - `joint` など transform 派生 node では、`transform` で定義済みの attribute は生成しません。
    これにより、派生 class には固有 attribute だけが出力され、共通 attribute は `Transform` から継承されます。
- `shape`
  - `node/dag/shape` に出力し、`Shape` を継承します。
  - `node_type == "shape"` の場合は `_core.py` に出力し、`DAG` を継承します。
- `auto`
  - Maya の `cmds.nodeType(..., inherited=True, isTypeName=True)` を使い、transform / shape / DAG / DG を自動判定します。

DG の既存呼び出しとの互換のため、デフォルトは `node_kind="dg"` です。

現段階では、DAG node の生成は主に `BDNode` で既存 node を包む準備段階です。
特に shape node の作成 API は transform 親の扱いが絡むため、`NodeCreater` への接続や shape 作成メソッドは後段で設計します。

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

## Field constructor metadata

Generator は取得できた attribute metadata を、Field constructor 引数へ反映します。

主な生成対象は次の通りです。

- `multi`
- `default_value`
- `min_value`
- `max_value`
- `soft_min_value`
- `soft_max_value`
- `readable`
- `writable`
- `category`

`cmds.attributeQuery(..., listDefault=True)` などは `[0.0]` のような list を返すことがあります。
単一要素 list は scalar に畳み、複数要素 list は tuple として生成します。

```python
input = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
vector = Float3Field(default_value=(1.0, 2.0, 3.0))
```

bool / int / enum 系は、Maya query が `0.0` / `1.0` のような float を返しても、Field の意味に合わせて正規化します。

```python
visible = BoolField(default_value=True)
count = LongField(default_value=3, min_value=0, max_value=10)
mode = ModeEnumField(default_value=2)
```

bool と enum の `min_value` / `max_value` / `soft_min_value` / `soft_max_value` は、Field 定義としては冗長なため生成しません。

`readable=True` / `writable=True` は Maya attribute の一般的な状態なので、生成コードを冗長にしないため出力しません。
`readable=False` / `writable=False` の場合だけ明示します。

```python
output = DoubleField(default_value=0.0, writable=False)
```

`category` は現行の `AttributeField(category=...)` に合わせ、取得できた最初の category を文字列として出力します。

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

compound child が enum の場合も、素の `EnumField()` ではなく専用の enum class を `node_attr` ファイル内に生成します。
これにより、親 compound 経由や node 直下 alias 経由で child enum にアクセスした場合も `NAME_MAP` を保持できます。

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

DG / DAG を混ぜて調査用に出力する場合は、`node_kind="auto"` を指定します。

```python
from bd_util._dev.maya.node.operator.node.generate import generate_node_class_file

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\src"

node_types = [
    "transform",
    "joint",
    "mesh",
    "camera",
]

for node_type in node_types:
    generate_node_class_file(
        node_type=node_type,
        src_dir=path,
        node_kind="auto",
    )
```

DAG 全体を一括生成したい場合は、次の helper を使います。
出力対象が多いため、まずは `generate_test/src` へ出力し、TODO や import error を確認してから正式な `src` 側へ反映します。

```python
from bd_util._dev.maya.node.operator.node.generate import (
    generate_dag_node_class_files,
)

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\src"
generate_dag_node_class_files(path)
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
- DAG / shape 系では `polyFaces` のような DG では目立たなかった attribute type が出る場合があります。未対応型は TODO として残し、型定義を追加してから再生成します。
- 生成後は必ず git diff を確認します。
- 既存手書き class を上書きする場合は、生成差分が意味的に一致しているか確認します。
