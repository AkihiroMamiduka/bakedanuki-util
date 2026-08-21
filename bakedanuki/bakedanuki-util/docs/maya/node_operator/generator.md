# Node Generator

このページは `python/bd_util/_dev/maya/node/operator/node/generate.py` の現行仕様をまとめます。
Generator は Maya の node type と attribute query 結果から、`NodeOperator` 用の Python class を生成する開発用ツールです。

## 目的

主な目的は、Maya 標準 DG / DAG ノードを `NodeOperator` として扱える形へ機械的に変換することです。

- Maya の node type から、`DG` / `DAG` / `Transform` / `Shape` を継承する生成 class を内部の `_generated` package に作る。
- 従来の公開 module path には、生成 class を継承する手書き可能な公開 wrapper を置く。
- compound attribute が必要な場合は `attr.define.node_attr` 側に専用 Field / AttrOperator / PlugOperator を生成する。
- 再生成時は生成 class だけを上書きし、公開 wrapper の手書き実装を保護する。
- 生成後の差分を git で確認し、attribute 差分や未対応型を炙り出す。
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

`generate_node_class_file(node_type, src_dir)` は、`src_dir` 以下の node kind ごとの
`_generated` package に生成 class を出力します。

```text
bd_util/maya/node/operator/node/dg/_generated/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/_generated/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/transform/_generated/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/shape/_generated/<node_type_snake>.py
```

生成 class は `GeneratedComposeMatrix` / `GeneratedJoint` のような名前を持ち、
内部の `_generated` package に配置したうえで、node kind に応じた基底 class を継承します。

```python
class GeneratedComposeMatrix(DG):
    ...
```

従来の公開 module path には、生成 class を継承する公開 wrapper を置きます。
公開 wrapper が存在しない場合は Generator が初期形を作成しますが、既存ファイルは
再生成時に上書きしません。

```text
bd_util/maya/node/operator/node/dg/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/transform/<node_type_snake>.py
bd_util/maya/node/operator/node/dag/shape/<node_type_snake>.py
```

```python
from ._generated.compose_matrix import GeneratedComposeMatrix


class ComposeMatrix(GeneratedComposeMatrix):
    __slots__ = ()

    NODE_TYPE = "composeMatrix"
```

### 名前変換

Maya node type、Python class、module pathは別の名前として扱います。
node type内の`_`はclass名ではPascalCaseの単語境界として除去し、module名では
snake_caseの区切りとして維持します。

| Maya node type | Python class | Generated class | Module |
| --- | --- | --- | --- |
| `bdDbl_Add` | `BdDblAdd` | `GeneratedBdDblAdd` | `bd_dbl_add.py` |
| `MASH_Audio` | `MASHAudio` | `GeneratedMASHAudio` | `mash_audio.py` |
| `multiplyDivide` | `MultiplyDivide` | `GeneratedMultiplyDivide` | `multiply_divide.py` |

`NodeCreator`と`ExistingNode`のmethod名は、Maya node typeをそのまま使用します。
そのため、`nodes.create.bdDbl_Add()`や`nodes.create.MASH_Audio()`として補完されます。

異なるnode typeが同じPython class名またはmodule名へ変換される場合、Generatorは
ファイルを書き出す前に`ValueError`を送出します。個別生成でも、正規化後の出力先が
別node typeの既存ファイルと衝突する場合は上書きしません。実際に衝突するnode typeが
追加された時点で、個別の名前overrideを検討します。

`transform` / `shape` 本体の公開 class は、それぞれ既存の `_core.py` に維持します。

```text
bd_util/maya/node/operator/node/dag/transform/_generated/transform.py
bd_util/maya/node/operator/node/dag/transform/_core.py
bd_util/maya/node/operator/node/dag/shape/_generated/shape.py
bd_util/maya/node/operator/node/dag/shape/_core.py
```

`node_attr` 側のファイルは、compound attribute 用の専用 class が必要な場合に出力されます。
単純な scalar / typed / enum attribute だけで構成できる場合は、node class 側だけで完結します。

custom attribute の生成コードは、深い実装 module を直接参照せず、
`attr.define.custom` の再エクスポートを import します。

```python
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float3Field,
)
```

node class から custom Field を直接使う場合も、同じ公開面を参照します。

```python
from ....attr.define.custom import Float3Field
```

これにより、生成物の import を短く保ち、custom 以下の実装階層を変更しても
生成コードへ影響が広がりにくくします。

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
  - `node/dg/_generated` に `Generated<NodeClass>(DG)` を出力します。
  - 公開 wrapper は従来どおり `node/dg/<node_type_snake>.py` に置きます。
- `dag`
  - `node/dag/_generated` に `Generated<NodeClass>(DAG)` を出力します。
  - 公開 wrapper は従来どおり `node/dag/<node_type_snake>.py` に置きます。
- `transform`
  - `node/dag/transform/_generated` に、通常は `Generated<NodeClass>(Transform)` を出力します。
  - `node_type == "transform"` の場合は `transform.py` に `GeneratedTransform(DAG)` を出力します。
  - 手書きの `_core.py` にある公開 `Transform` は `GeneratedTransform` を継承します。
  - `joint` など transform 派生 node では、`transform` で定義済みの attribute は生成しません。
    これにより、派生 class には固有 attribute だけが出力され、共通 attribute は `Transform` から継承されます。
  - attribute は node instance を作成せず、`MNodeClass` と
    `cmds.attributeQuery(..., type=<nodeType>)` から取得します。
  - 生成済み class は `nodes.existing` から利用できますが、`nodes.create` には
    `CREATABLE_TRANSFORM_NODE_TYPES` に明示した作成確認済み type だけを公開します。
- `shape`
  - `node/dag/shape/_generated` に、通常は `Generated<NodeClass>(Shape)` を出力します。
  - `node_type == "shape"` の場合は `shape.py` に `GeneratedShape(DAG)` を出力します。
  - 手書きの `_core.py` にある公開 `Shape` は `GeneratedShape` を継承します。
  - 抽象 `shape` の attribute は node instance を作成せず、`MNodeClass` と
    `cmds.attributeQuery(..., type="shape")` から取得します。
  - concrete shape では `Shape` に生成済みの共通 attribute を除外します。
- `auto`
  - Maya の `cmds.nodeType(..., inherited=True, isTypeName=True)` を使い、transform / shape / DAG / DG を自動判定します。

DG の既存呼び出しとの互換のため、デフォルトは `node_kind="dg"` です。

shape node は全生成と作成 API の公開を分けて扱います。生成済み class は
`nodes.existing` から利用できますが、`nodes.create` には親 Transform 必須の
作成テストを通した node type だけを明示的に公開します。

transform 派生 node も同じく、既存 node を具体型へ包む coverage と作成 API の
公開を分けます。`ikHandle` / `ikEffector` は最初の既存 node 用サンプルとして
生成しますが、特殊な作成手順を持つため `nodes.create` には公開しません。
次のグループとしてconstraint系14種も生成し、`nodes.existing` の具体型と
補完へ追加しています。constraint nodeも専用commandや接続を伴うため、
`nodes.create` には公開しません。
`transform` / `joint` は引き続き作成確認済み type として公開します。

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
- 生成する compound class 名が imported base class 名と衝突する場合は、
  `Value` suffix を追加する。
  - `LightDataField` -> `LightDataValueField`

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

### Arnold の不定な default 値

Maya 2025 / MtoA の一部 attribute は、`cmds.attributeQuery(..., listDefault=True)` と
OpenMaya の attribute default query の双方で、`mayapy` プロセスごとに異なる
未初期化値を返します。

Generator は、複数プロセスで不定になることを確認した Arnold の6ノードタイプ・
22 attribute だけ、生成時に `default_value` を省略します。通常の attribute query
結果は変更せず、安定して取得できる `0.0`、`1.0`、`NaN` などの default 値も維持します。
対象は数値の見た目では判定せず、`(node_type, canonical attribute name)`
の明示リストで限定します。

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

一部 plugin node の attribute は、`cmds.listAttr()` / `cmds.attributeQuery()` では参照できても、`MFnDependencyNode.findPlug()` が失敗する場合があります。
その場合は OpenMaya fallback を諦め、`cmds.attributeQuery()` で取得できた metadata を優先して生成を継続します。

解決できない attribute は TODO コメントとして残します。
全 DG 生成では、NodeOperator の通常利用対象から外れる特殊ノードを skip するため、生成 snapshot 側に TODO が残らない状態を目指します。

`polyFaces` は Maya の `mesh.face` などで使われる特殊な typed attribute です。
OpenMaya 上では `MFnTypedAttribute` として見えますが、標準的な `MFnData` 名へは解決できないため、Generator では `TypedField` として扱います。
現時点では get/set 対象ではなく、既存 plug の参照・接続用の Field として生成します。

## skipped node type

一部の DG node type は、生成対象から意図的に除外します。

現状の skip 対象は次の通りです。

- `nodeGraphEditorInfo`
  - Node Editor の UI 状態保存寄りの内部ノードです。
  - standalone mayapy では一部 attribute の型情報を十分に取得できません。
  - 通常の NodeOperator 操作対象としての実用性が低いため、全量生成から除外します。
- `caddyManipBase`
  - mayapy で node 作成時に native crash することを確認済みの manipulator 系ノードです。
  - 通常の DAG 全量生成からは既知危険ノードとして除外します。
- `*manip*`
  - Manipulator 系の node type です。
  - DAG 全量生成の安定性を優先するため、node type 名に `manip` を含むものは現状まとめて除外します。
- `placerTool`
  - Viewport 上に不安定な tool overlay を残すことを確認済みの node type です。
  - 新規シーン後も表示が残り、触ると Maya が落ちるケースがあるため除外します。

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
class OperationEnumPlugOperator(
    EnumPlugOperator["OperationEnumAttrOperator"]
):
    __slots__ = ()

    NO_OPERATION = 0
    SUM = 1
    SUBTRACT = 2
    AVERAGE = 3


class OperationEnumAttrOperator(
    EnumAttrOperator[OperationEnumPlugOperator]
):
    ...
```

Plug / Attr の具象 class は互いを generic 型引数として指定します。
先に定義する Plug 側では、後続の Attr class を文字列による前方参照にします。

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

`NAME_MAP` の key と label が 79 文字を超える場合は、生成時に label を
括弧付きの複数行表現へ折り返します。

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

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\python"

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

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\python"

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
出力対象が多いため、まずは `generate_test/python` へ出力し、TODO や import error を確認してから正式な `bakedanuki/bakedanuki-util/python` 側へ反映します。

```python
from bd_util._dev.maya.node.operator.node.generate import (
    generate_dag_node_class_files,
)

path = r"D:\develop\bakedanuki_dev\bakedanuki-util\generate_test\python"
generate_dag_node_class_files(path)
```

`caddyManipBase`、`*manip*`、`placerTool` など、DAG 全量生成中に Maya を不安定にすることを確認済みの node type は、通常生成から除外します。

`mayapy` で単体実行する場合は、必要に応じて `maya.standalone.initialize(name="python")` を先に呼びます。

```python
import maya.standalone
maya.standalone.initialize(name="python")
```

生成される attribute は、実行時に Maya へロードされている plugin に依存します。
例えば `mesh` の Arnold attribute を含めたい場合、mayapy では生成前に `mtoa` をロードします。

```python
import maya.cmds as cmds
cmds.loadPlugin("mtoa", quiet=True)
```

標準の shape snapshot は Maya 2025 で `mtoa` をロードした状態を基準とします。
現在の作成確認済みサンプルは `mesh` / `camera` / `nurbsCurve` / `locator` /
`nurbsSurface` です。concrete shape 81種は正式 snapshot へ生成済みですが、
再生成時もまず調査用出力先で TODO、構文、import、node type 名衝突を確認します。

shape の attribute 取得には `MNodeClass` と type 指定の `attributeQuery` を使い、
調査用 node instance は作成しません。これにより、作成時に特殊な初期化を要求する
shape や Maya を不安定にする shape を、一括生成中に `createNode()` することを避けます。
Maya 2025 + MtoA では、登録された shape 81 種すべてについて静的 query と
生成コードの構文確認が成功しています。別々の mayapy process 間でも snapshot を
比較し、MtoA が camera 系へ追加する未初期化 default は生成コードへ埋め込みません。

生成結果には、Maya実行環境と分離した共通のBlack設定を適用します。
正式な出力先へ生成した後は、リポジトリ直下で次を実行してください。

```powershell
.\scripts\format.cmd
```

これにより、生成器自体をBlackへ依存させず、手書きコードと生成コードに
同じformatを適用できます。整形後の状態は次で確認します。

```powershell
.\scripts\format.cmd -Check
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
for path in Path("generate_test/python").rglob("*.py"):
    try:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
    except SyntaxError as exc:
        errors.append((path, exc.lineno, exc.msg))

print(errors)
```

## ノードアクセス用の補完 stub

内部実装の `ExistingNode.decomposeMatrix()` のような型別メソッドは実行時には lazy に解決されます。
公開APIの `nodes.existing.decomposeMatrix()` は、共有 `ModifierManager` を束縛したうえで同じ型別アクセスを提供します。
IDE から具体的な戻り値型を追えるように、次のスクリプトが生成済み NodeOperator class を走査して、以下の3ファイルを生成します。

- `python/bd_util/maya/node/existing_node.pyi`
- `python/bd_util/maya/node/nodes.pyi`
- `python/bd_util/maya/node/creator/_shape_with_transform.pyi`

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" `
    python\bd_util\_dev\maya\node\operator\node\generate_existing_node_stub.py
```

新しい NodeOperator class を追加または再生成した場合は、3つのstubも再生成してください。
差分を発生させず、現在のstubが最新か確認する場合は `--check` を指定します。
`--check`はBlackによる折り返しなどのformat差分を無視し、Python ASTとして
生成内容が一致しているかを確認します。

公開基底クラスの `Shape` は、具体的な Maya node type ではありません。
そのため `Shape` クラス自体は継承用に維持しますが、実ノードを型別に包めない
`nodes.existing.shape()` / `ExistingNode.shape()` は補完 stub の生成対象から除外します。

`_shape_with_transform.pyi` は、一括作成を検証済み shape type に限定しながら、
`nodes.create.with_transform.mesh()` のようなアクセスで `(Transform, Mesh)` まで
具体的な戻り値型を追えるようにします。公開対象は
`creator/_shape_types.py` と共有するため、実行時 API と補完候補がずれません。

Python キーワードと module 名が衝突する `and` / `or` / `not` は、`NodeCreator` と同様に `and_()` / `or_()` / `not_()` として公開します。
これら3つだけは Python の import 構文で具体 class を参照できないため、stub 上の戻り値型を `NodeOperator` とします。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" `
    python\bd_util\_dev\maya\node\operator\node\generate_existing_node_stub.py `
    --check
```

## 現状の注意点

- `attributeType=None, dataType=None` の attribute はまだ自動解決できません。
- DAG / shape 系では DG では目立たなかった attribute type が出る場合があります。未対応型は TODO として残し、型定義を追加してから再生成します。
- 抽象 `shape` と concrete shape は、静的な node type query で属性を生成します。
- shape class の生成だけでは `nodes.create` の公開対象になりません。作成確認済み type を明示的に opt-in します。
- 生成後は必ず git diff を確認します。
- `_generated` package 以下は再生成時に上書きされるため、手書きコードを追加しません。
- 公開 wrapper は Generator が上書きしません。ノード固有のメソッドは公開 wrapper 側へ追加します。
