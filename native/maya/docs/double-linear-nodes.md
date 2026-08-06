# Double Linear Node Expansion

`bdUtilNodes`の`double` / `double3`数値演算node familyを、Mayaのlinear unit
attributeへ展開した設計・実装記録です。

距離を保つ18種の`DblL` / `DblL3` node、scalar `doubleLinear`を比較する
typed-any Condition 2種、linear valueとdimensionless factorを扱うMultiply / Divide
8種、距離同士からdimensionless比率を求めるRatio 2種、Right Triangle 1種、
Condition用Compose 2種を実装済みです。関連node typeは合計51種です。Power familyは
距離を出力する演算として単位が成立しないため、完了対象から明示的に除外しています。

## Goals

- `translateX`などの`doubleLinear` plugを、型を保ったまま演算できるようにする。
- `translate`のような3成分のlinear unit compoundをcomponent-wiseに演算できるようにする。
- 既存の`double` / `double3` familyと一貫したnode type名、attribute名、Python APIを
  提供する。
- Mayaの表示単位ではなく、unit attributeの内部値を扱うことを明示する。
- 距離として自然な演算と、内部数値だけを利用する演算を区別する。

## Terminology And Attribute Structure

### `doubleLinear`

この文書の`doubleLinear`は、`MFnUnitAttribute::kDistance`で作成するscalar
attributeを指します。値は`MDistance`として扱われ、`double`でdefaultを指定した場合は
centimeterとして解釈されます。

### `doubleLinear3`

Mayaには`doubleLinear3`という独立したatomic data typeはありません。この文書では、
次のnumeric compoundをプロジェクト内の呼称として`doubleLinear3`と呼びます。

```text
parent: double3 numeric compound
  childX: doubleLinear
  childY: doubleLinear
  childZ: doubleLinear
```

Mayaの`translate`も、親が`double3`、XYZの子が`doubleLinear`という構造です。
C++では3つの子を`MFnUnitAttribute::kDistance`で作成し、それらを
`MFnNumericAttribute::create()`へ渡して親compoundを作成します。

Python側では、この組み合わせは既に`DoubleLinear3AttrOperator`へ解決されます。

`doubleLinear`はMayaの距離単位を持つattribute型であり、非負値だけを許可する
「長さ型」ではありません。Add、Subtract、Negateなどは符号をそのまま扱います。
幾何学的な辺長を扱うRight Triangleだけが、入力を絶対値へ正規化します。

## Node Type Naming

linear unit familyのtype codeは次のとおりです。

| Attribute structure | Type code | Example |
| --- | --- | --- |
| scalar `doubleLinear` | `DblL` | `bdDblL_Add` |
| `doubleLinear`を3つ持つ`double3` compound | `DblL3` | `bdDblL3_Add` |

既存の命名規則どおり、node typeは次の形式にします。

```text
bd<TypeCode>_<Operation><Variant>
```

例です。

```text
bdDblL_Add
bdDblL_AddMulti
bdDblL3_Add
bdDblL3_AddMulti
bdDblL3_WeightedAverageMulti
```

生成されるPython名は既存の変換規則に従います。

| Surface | Scalar example | Compound example |
| --- | --- | --- |
| Maya node type | `bdDblL_Add` | `bdDblL3_Add` |
| Python class | `BdDblLAdd` | `BdDblL3Add` |
| Python module | `bd_dbl_l_add.py` | `bd_dbl_l3_add.py` |
| `NodeCreator` method | `nodes.create.bdDblL_Add()` | `nodes.create.bdDblL3_Add()` |

`DblL3`はMayaの正式な型名ではなく、このplug-inのtype codeです。node仕様では、
必ず「親`double3`、子`doubleLinear`」という実体も併記します。

Conditionは出力型ではなく比較型をnode type名で表すため、この命名規則の例外です。
typed-any payloadを表す`Any`を先に置き、比較型をoperation名の後ろに置きます。

```text
bdAny_Condition<ComparisonType><Variant>
```

例: `bdAny_ConditionDblL`、`bdAny_ConditionDblLMulti`

出力型と入力型が異なるRatioは、出力型を先頭に置き、入力型をoperation名の後ろへ
置きます。`bdDbl_RatioDblL`は`doubleLinear`同士から`double`を、
`bdDbl3_RatioDblL3`は`doubleLinear3`同士から`double3`を出力します。

Condition用ComposeはConditionとの対応を優先して
`bdConditionDblLExtra_Compose` / `bdConditionDblLCase_Compose`とします。
Right Triangleは入出力がscalar `doubleLinear`なので通常規則どおり
`bdDblL_RightTriangle`とします。

## Final Implementation Inventory

当初の機械的な展開候補を、単位を保つ演算、mixed-type演算、比較型を表すCondition、
用途固有nodeへ分類した最終結果です。Conditionはtyped-any payloadの出力型ではなく、
比較型ごとの独立familyとして数えます。

| Category | Variants / node types | Node count | Status |
| --- | --- | ---: | --- |
| 距離を保つscalar / 3成分演算 | 18 variants x 2 type codes | 36 | 実装済み |
| scalar `doubleLinear`比較のtyped-any Condition | Single / Multi | 2 | 実装済み |
| Condition compound Compose | Extra / Case | 2 | 実装済み |
| mixed-type Multiply / Divide | scalar / 3成分、固定 / Multi | 8 | 実装済み |
| distance Ratio | scalar / 3成分 | 2 | 実装済み |
| Right Triangle | scalar | 1 | 実装済み |
| **実装済み合計** |  | **51** | **完了** |
| Power / PowerMulti | scalar / 3成分、固定 / Multi | 4 | 完了対象外 |

## Directly Expandable Nodes

次の18種は実装済みです。入力された距離を加減、補間、集約し、距離を
出力します。既存の数値仕様とsparse array仕様を維持したまま、値を持つattributeを
`doubleLinear` / `doubleLinear3`へ置き換えています。

| Operation | Variants | Linear attributes | Attributes kept non-linear | Notes |
| --- | --- | --- | --- | --- |
| Value | `Value` | `value` | none | 保存、keyframe、双方向接続の仕様を維持する |
| Add | `Add`, `AddMulti` | inputs, `output` | none | 空配列はzero |
| Subtract | `Subtract`, `SubtractMulti` | inputs, `output` | none | `Multi`はlogical index順を維持する |
| Average | `Average`, `AverageMulti` | inputs, `output` | none | 要素数は内部のdimensionless count |
| Minimum | `Min`, `MinMulti` | inputs, `output` | none | component-wise |
| Maximum | `Max`, `MaxMulti` | inputs, `output` | none | component-wise |
| Clamp | `Clamp` | `input`, `min`, `max`, `output` | none | 逆転した上下限の既存仕様を維持する |
| Absolute | `Abs` | `input`, `output` | none | 負のtranslateにも使用できる |
| Negate | `Negate` | `input`, `output` | none | 符号反転 |
| Lerp | `Lerp` | `input1`, `input2`, `output` | `weight: double` | weightの`0..1` clampを維持する |
| Map Range | `MapRange` | `input`, source range, target range, `output` | `clamp: bool` | 距離から距離へのrange変換 |
| Weighted Sum | `WeightedSumMulti` | `value`, `output` | `weight: double` | weightはdimensionless |
| Weighted Average | `WeightedAverageMulti` | `value`, `output` | `weight: double` | weight合計による正規化を維持する |

この表の`Linear attributes`は、`DblL`版ではscalar `doubleLinear`、`DblL3`版では
`doubleLinear3`を意味します。`DblL3`版の演算はXYZごとに独立して行います。

### Map Range Scope

初回の`bdDblL_MapRange` / `bdDblL3_MapRange`は、SourceとTargetの両方をlinearにします。
この構成では、Source範囲内のdimensionless parameterを求め、Target距離へ適用するため、
演算の単位が保たれます。

`double`から`doubleLinear`、`doubleAngle`から`doubleLinear`など、異なる単位間の
Map Rangeも実用性があります。ただし、これは`DblL` familyの単純展開には含めず、
入力domainと出力rangeの型を名前と仕様で表せる別nodeとして検討します。

## Condition Nodes

`bdAny_ConditionDblL` / `bdAny_ConditionDblLMulti`は実装済みです。
node type名の`DblL`は選択値や出力ではなく、比較型を表します。`input`と`compare`は
scalar `doubleLinear`、選択候補と出力はMayaの`choice` nodeと同じ考え方の
typed-any attributeです。

### Single Condition

| Attribute | Type |
| --- | --- |
| `input` | `doubleLinear` |
| `operation` | enum |
| `compare` | `doubleLinear` |
| `extra[].logic` | enum (`And` / `Or`) |
| `extra[].comparison` | enum |
| `extra[].compareValue` | `doubleLinear` |
| `trueValue` | typed-any |
| `falseValue` | typed-any |
| `output` | typed-any |

### Multiple Conditions

| Attribute | Type |
| --- | --- |
| `input` | `doubleLinear` |
| `case[].operation` | enum |
| `case[].compare` | `doubleLinear` |
| `case[].extra[].logic` | enum (`And` / `Or`) |
| `case[].extra[].comparison` | enum |
| `case[].extra[].compareValue` | `doubleLinear` |
| `case[].value` | typed-any |
| `elseValue` | typed-any |
| `output` | typed-any |

1つのnodeへ接続するすべての選択候補と出力先は、同じMayaデータ型へ統一します。
`TypedPlugOperator`は接続専用として扱い、payloadの値をNodeOperatorの`.get()` /
`.set()`で操作しません。詳細は[Condition Nodes](condition.md)を参照してください。

### Compose Nodes

`bdConditionDblLExtra_Compose`と`bdConditionDblLCase_Compose`は、Conditionの
`extra[index]` / `case[index]`と同じcompound構造を出力します。`compareValue`と
`compare`は`doubleLinear`を維持し、親compound plugを1本接続するだけで設定を渡せます。
Case Composeの`value`はtyped-anyの接続専用です。詳しいattribute構成と接続例は
[Condition Nodes](condition.md#compose-nodes)を参照してください。

## Mixed-Type Factor Nodes

Multiply / Divideは、距離を表す`input`とdimensionlessな`factor`を分離した8種を
実装済みです。MultiplyとDivideでattribute名を`factor`へ統一し、node typeを
差し替えても同じplug名で接続できます。

| Node type | `input` | `factor` | `output` |
| --- | --- | --- | --- |
| `bdDblL_Multiply` | `doubleLinear` | `double` | `doubleLinear` |
| `bdDblL_MultiplyMulti` | `doubleLinear` | `double[]` | `doubleLinear` |
| `bdDblL3_Multiply` | `doubleLinear3` | `double3` | `doubleLinear3` |
| `bdDblL3_MultiplyMulti` | `doubleLinear3` | `double3[]` | `doubleLinear3` |
| `bdDblL_Divide` | `doubleLinear` | `double` | `doubleLinear` |
| `bdDblL_DivideMulti` | `doubleLinear` | `double[]` | `doubleLinear` |
| `bdDblL3_Divide` | `doubleLinear3` | `double3` | `doubleLinear3` |
| `bdDblL3_DivideMulti` | `doubleLinear3` | `double3[]` | `doubleLinear3` |

共通仕様は次のとおりです。

- `input`のdefaultは距離のzero、`factor`のelement defaultはdimensionless identityの`1`、
  `output`のdefaultは距離のzeroとする。
- `DblL3`版はXYZごとのcomponent-wise演算とする。scalar factor 1つを3軸へ
  broadcastする仕様にはしない。
- `Multi`版は単一の`input`から開始し、既存の`factor[]`をlogical index昇順で
  畳み込む。`factor[]`が空なら`input`をそのまま返す。
- Divideも除数のattribute名を`divisor`ではなく`factor`とする。
- Divideの各factorには既存`SafeDivision.h`と同じ`1.0e-9`のepsilonを適用し、
  zero付近では符号を維持する。epsilonはdimensionless値として扱う。
- `NaN`と無限値は、epsilon対象を除き通常のIEEE演算へ委ねる。

入力距離はMaya内部のcentimeter値で計算され、factorは表示単位の影響を受けません。
したがって`currentUnit(linear=...)`を変更しても物理的な出力距離は変化しません。
`translate` / `translateX`を`input`へ、`scale` / `scaleX`を`factor`へ直接接続できます。

## Ratio Nodes

距離同士の除算は出力が距離ではなくdimensionlessな比率になるため、`DblL` familyの
Divideではなく、出力型を先頭に表す独立したRatio 2種として実装しています。

| Node type | `input` | `base` | `output` |
| --- | --- | --- | --- |
| `bdDbl_RatioDblL` | `doubleLinear` | `doubleLinear` | `double` |
| `bdDbl3_RatioDblL3` | `doubleLinear3` | `doubleLinear3` | `double3` |

計算は`output = input / base`です。`base`は基準距離を表し、MayaのファイルReferenceとの
混同を避けるため`reference`は使用しません。3成分版はXYZごとのcomponent-wise比率で、
ベクトル長同士の比率ではありません。

`input`のdefaultはzero、`base`は`1 cm`、`output`はzeroです。zero付近の`base`には
既存`SafeDivision.h`の`1.0e-9`を適用します。このepsilonはMaya内部距離単位の
centimeter値です。入力と基準の物理距離が表示単位とともに同じ倍率で変換されるため、
ratioは`currentUnit(linear=...)`の影響を受けません。

Multi版は作りません。3つ以上の距離を連続除算すると、結果がdimensionlessな単純比率を
保たないためです。複数の比率が必要な場合は、Ratio nodeを必要な数だけ使用します。

## Right Triangle Node

`bdDblL_RightTriangle`は、直角三角形の既知の2辺から残りの1辺を求めます。
すべての辺と`output`は`doubleLinear`、計算対象を指定する`solveFor`はenum、
計算成立状態を返す`isValid`はbool outputです。

| `solveFor` | 使用する入力 | 計算 |
| --- | --- | --- |
| `Hypotenuse` (default) | `legA`, `legB` | `sqrt(legA^2 + legB^2)` |
| `LegA` | `hypotenuse`, `legB` | `sqrt(hypotenuse^2 - legB^2)` |
| `LegB` | `hypotenuse`, `legA` | `sqrt(hypotenuse^2 - legA^2)` |

`legA`、`legB`、`hypotenuse`、`output`のdefaultはzeroです。辺は方向を持たない長さとして
扱うため、負の入力は絶対値へ正規化します。斜辺を求める計算には`std::hypot()`を使い、
逆算には中間値の二乗と加算によるoverflowを避ける等価式を使用します。

逆算で`abs(hypotenuse) < abs(knownLeg)`の場合は成立しません。また、いずれのmodeでも
有限でない入力がある場合や有限な結果を表現できない場合は、後続DGへ`NaN`や無限値を
流さないため`output = 0`、`isValid = false`とします。斜辺と既知の脚が等しい場合は、
残る脚がzeroになる実数計算上の境界値として`output = 0`、`isValid = true`です。

1 nodeが1つの明確な幾何学的関係を表すため、Multi版と3成分版は作りません。
入力と出力はMaya内部のcentimeter値で一貫して計算され、表示距離単位を変更しても
物理的な結果は変わりません。

## Deliberately Deferred Node

### Power

`distance ^ exponent`は、exponentが`1`以外の場合、一般にはdistanceを出力しません。
内部centimeter値へ`std::pow()`を適用し、その結果をdistanceとして格納することは
可能ですが、unit attributeとして直感的なAPIにはなりません。

`Power` / `PowerMulti`は初回のlinear unit展開から外します。具体的なリグ用途と、
内部centimeter基準の数値演算であることを正当化できた場合だけ再検討します。

## C++ Attribute Implementation

既存の`NumericAttribute` / `Double3Attribute` helperは`MFnNumericData::kDouble`を
作成します。linear unit版は責務を混在させず、次の専用helperとして実装しています。

- `UnitAttribute`はscalar `doubleLinear`を`MFnUnitAttribute::kDistance`で作成し、
  input / outputの標準flagを設定する。
- `DoubleLinear3Attribute`は3つのdistance childとnumeric parentをまとめて作成する。
- min / maxなどnode固有の制約は、必要なattributeを作成したnode側で設定する。
- compound nodeは親と子の`MObject`をすべて保持し、dirty伝搬と子plug要求を明示する。

実装済みnodeは、scalarで`MDataHandle::asDouble()` / `setDouble()`、compoundで
`asDouble3()` / `set3Double()`を使用し、Mayaのinternal centimeter値を既存math
helperへ渡します。centimeter / meterの表示単位切替テストにより、内部距離と出力が
変化しないことを確認しています。plugを距離として検証する場合は
`MPlug::asMDistance()`を使用します。

math helperはMaya APIに依存しない`double`計算を維持できます。ただし、helperへ渡す値が
internal centimeterなのかdimensionlessなのかを、nodeごとのattribute仕様で明示します。

## Defaults And Unit Behavior

`MFnUnitAttribute`へ`double`で指定したdistance defaultはcentimeterとして解釈されます。
sceneの表示単位がmeterでも、default `1.0`は`0.01 m`と表示されます。

このため、既存nodeのdefaultを機械的に移植しません。

- additive nodeのzeroは、linear unitでも自然なdefaultとして維持できる。
- Lerpとweight系のweightはdimensionlessなので、既存defaultを維持できる。
- Multiply / Divideはlinear `input`をzero、dimensionless `factor`をidentity `1`とする。
  `Multi`版の空factor配列は`input`をそのまま返す。
- Powerのidentity `1`は、linear attributeでは`1 cm`になるため、attributeの役割を
  決めるまで実装しない。
- Map Rangeの`1`は`1 cm`のrange endpointとして有効だが、その意味をテストと
  node仕様に記載する。

UI表示値を直接計算値として使わず、内部centimeter値を基準にします。sceneの
`currentUnit(linear=...)`を変更しても、既存scene内の物理的な距離とnode出力が変化しない
ことを必須条件にします。

## Python API And Generation

NodeOperatorのattribute解決には、親`double3`、子`doubleLinear`、子数3の組み合わせを
`DoubleLinear3AttrOperator`へ解決する既存処理があります。実装済みnodeは既存generatorで
class / attribute定義を生成し、次を確認しています。

- `node.inputX` / `node.outputX`の子plugがlinear operatorとして生成される。
- 親plugが`DoubleLinear3AttrOperator`として生成される。
- `nodes.create.bdDblL_*()` / `nodes.create.bdDblL3_*()`が補完される。
- 生成class名とmodule名に衝突がない。
- 生成後にformat、import sweep、pytestを実行する。

## Implementation Order

1. scalar / compoundのlinear unit attribute helperと、最小のValue nodeを実装する。
   - 完了
2. Add、Subtract、Average、Min / Maxなど、距離を保つ基本演算を実装する。
   - 完了
3. Clamp、Abs、Negate、Lerp、Map Range、weight系を実装する。
   - 完了
4. scalar `doubleLinear`比較とtyped-any選択値を持つ`bdAny_ConditionDblL` /
   `bdAny_ConditionDblLMulti`を実装する。
   - 完了
5. Conditionの`extra[index]` / `case[index]`を1接続で設定するComposeを実装する。
   - 完了。`doubleLinear`比較用のExtra / Case 2 nodeを実装
6. Multiply / Divideのmixed-type attribute仕様とdefaultを確定し、固定版と
   `Multi`版を実装する。
   - 完了。単一`input`と`factor[]`へ分けた8 nodeを実装
7. `doubleLinear / doubleLinear -> double`のRatioと3成分版を実装する。
   - 完了。`input / base`の固定入力2 nodeを実装
8. 直角三角形の既知の2辺から残りの1辺を求めるnodeを実装する。
   - 完了。`bdDblL_RightTriangle`を実装
9. Power familyは単位が成立しないため、完了対象外として判断理由を記録する。

node typeは実装する単位だけ登録し、未実装分の`MTypeId`を先に消費しません。
IDは実装開始前に[Node ID Registry](../NODE_IDS.md)へ追加します。

## Completion Boundary

このfamilyは、上記51 node typeとNodeOperator、型情報、テスト、仕様文書の実装をもって
完了とします。次は未実装ではなく、意図的な境界です。

- Power / PowerMultiは、距離の累乗が通常は距離にならないため完了対象へ含めない。
- Ratioは距離同士の単純比率だけを表し、連続除算になるMulti版を作らない。
- Right Triangleは1つの幾何学的関係を表すscalar nodeとし、Multi版と3成分版を作らない。
- 異なるunit型の間を変換するMap Rangeは、入力domainと出力rangeを名前で表す別familyとする。
- Conditionのtyped-any plugは接続専用とし、NodeOperatorの値操作APIはこのfamilyで追加しない。

主な自動検証の担当は次のとおりです。

| Scope | Test |
| --- | --- |
| 距離を保つ36 node | [test_bd_double_linear.py](../../../tests/maya/node/operator/node/dg/test_bd_double_linear.py) |
| Condition 2 node | [test_bd_condition.py](../../../tests/maya/node/operator/node/dg/test_bd_condition.py) |
| Compose 2 node | [test_bd_condition_compose.py](../../../tests/maya/node/operator/node/dg/test_bd_condition_compose.py) |
| Multiply / Divide 8 node | [test_bd_double_linear_factor.py](../../../tests/maya/node/operator/node/dg/test_bd_double_linear_factor.py) |
| Ratio 2 node | [test_bd_ratio.py](../../../tests/maya/node/operator/node/dg/test_bd_ratio.py) |
| Right Triangle 1 node | [test_bd_right_triangle.py](../../../tests/maya/node/operator/node/dg/test_bd_right_triangle.py) |

## Handoff To Double Angle Development

`doubleAngle` familyで再利用できる実装パターンは多いものの、単純な型置換として開始せず、
少なくとも次を別途確認します。

- scalarは`MFnUnitAttribute::kAngle`を使用し、内部値がradianであることをdefault、epsilon、
  テスト期待値へ反映する。
- 3成分版を作る場合は、親`double3`と3つの`doubleAngle` childという実体をAPIで確認し、
  project内呼称とtype codeを決める。
- 値をraw angleとして扱うのか、周期を持つ方向として扱うのかをfamily単位で決める。
  これはEqual、Min / Max、Clamp、Average、Lerp、Map Rangeへ影響する。
- `rotate`の3成分をcomponent-wiseに演算するnodeと、Euler rotation / orientationを扱う
  nodeを混同しない。
- angleとdimensionless factorのMultiply / Divideは単位を保てるが、angle同士のRatio、
  wrap / normalize、shortest-path補間は用途を確認してから追加する。
- Conditionはscalar比較型を`doubleAngle`へ置き換え、typed-any payloadと接続専用方針を
  維持できる。対応するExtra / Case Composeも比較型ごとに分ける。
- Right Triangleは距離幾何に固有なので、`doubleAngle`へは展開しない。
- Powerは`doubleLinear`と同じ理由で機械的に展開しない。

## Verification Checklist

各nodeの既存テスト項目に加え、linear unit固有の次を確認します。

- Maya 2025以降でscalarとcompoundのattribute typeをAPIから確認する。
- `translateX`などのscalar `doubleLinear`と直接接続する。
- `translate`などの親compound、およびXYZの子plugを個別に接続する。
- 親または子が要求された場合のcompute、clean、dirty伝搬を確認する。
- `Multi`版ではsparse logical indexと空入力の結果を確認する。
- centimeter、meterなど複数のlinear表示単位で、内部距離と出力が変化しないことを確認する。
- defaultとattribute editor上の表示値を複数のlinear表示単位で確認する。
- Maya ASCII / Binaryのscene round-trip後も値、接続、attribute typeが保たれることを確認する。
- Serial / Parallel評価で結果が一致することを確認する。
- NodeOperator生成後の親子plug型とIDE補完を確認する。

共有attribute helper、node attr解決、生成classへ影響するため、実装時はtargeted testに加えて
原則としてfull pytest、format check、必要に応じてDG module import sweepを実行します。

## Decisions Summary

| Topic | Decision |
| --- | --- |
| Scalar type code | `DblL` |
| Three-component type code | `DblL3` |
| `doubleLinear3`の意味 | 親`double3`、子`doubleLinear` x 3のcompound |
| 値の符号 | unit型自体は負値を許可する。Right Triangleだけは辺長として絶対値へ正規化する |
| 初回展開 | 距離を保つ18種を実装済み |
| Condition比較型 | scalar `doubleLinear` |
| Condition選択値 / 出力 | typed-any。同じnode内では接続型を統一する |
| Condition展開 | `bdAny_ConditionDblL` / `bdAny_ConditionDblLMulti`を実装済み |
| Condition Compose | Extra / Caseを1 node = 1 elementで構築。比較型ごとに分ける |
| Multiply | `input: linear`と`factor: double / double3`のmixed-type。固定版 / Multi版を実装済み |
| Divide | Multiplyと同じ`factor`名を使用し、安全除算する。固定版 / Multi版を実装済み |
| Multiply / Divide Multi | 単一`input`と`factor[]`。空配列は`input`を返す |
| Ratio | `input / base`。scalarは`double`、3成分版は`double3`を出力する。Multi版なし |
| Right Triangle | `solveFor`で求める辺を選択し、`isValid`で成立状態を出力。Multi / 3成分版なし |
| Power family | 単位が成立しないため完了対象外。具体的用途が得られた場合だけ再検討する |
| Family完了 | 実装済み51 node typeをもって完了 |
