# Double Linear Node Expansion

`bdUtilNodes`の`double` / `double3`数値演算node familyを、Mayaのlinear unit
attributeへ展開するための設計方針です。

距離を保つ18種の`DblL` / `DblL3` nodeと、scalar `doubleLinear`を比較する
typed-any Condition 2種は実装済みです。Multiply、Divide、Power familyは、
ここに記載した方針と未確定事項に従って今後実装します。

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

## Existing Family Inventory

Conditionを出力型ごとのfamilyから分離したため、`double` / `double3`から
`DblL` / `DblL3`へ機械的に展開する候補は、各24種です。Conditionは比較型ごとに
typed-any値を扱う独立familyとして数えます。

展開判断は次の3段階に分けます。

| Decision | Variants per type code | New node types | Status |
| --- | ---: | ---: | --- |
| 距離を保つため、そのまま展開する | 18 | 36 | 実装済み |
| scalar `doubleLinear`比較のtyped-any Condition | - | 2 | 実装済み |
| 型構成または演算意味を再設計する | 6 | 12 | 未確定または保留 |

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

## Nodes Requiring Redesign

### Multiply

すべての入出力を`doubleLinear`にする実装は技術的に可能です。Maya標準の
`multDoubleLinear`も、`input1`、`input2`、`output`のすべてが`doubleLinear`です。

ただし、その計算は距離の次元解析ではなく、内部のcentimeter値を使う数値演算です。
例えば`2 cm * 3 cm`は`6 cm`となり、表示単位をmeterへ変更すると
`0.02 * 0.03 -> 0.06`と表示されます。値はsceneの表示単位変更に対して安定しますが、
表示数値同士の乗算にはなりません。

リグ用途では、固定入力版を次のmixed-type演算として再設計する方向を優先します。

```text
bdDblL_Multiply:  doubleLinear  * double  -> doubleLinear
bdDblL3_Multiply: doubleLinear3 * double3 -> doubleLinear3
```

`input1`をvalue、`input2`をfactorとして扱う場合、defaultも現在の対称な`1` / `1`を
そのまま移植せず、valueのzeroとfactorのidentity `1`を候補に再検討します。

`MultiplyMulti`は同型の`input[]`ではmixed-type演算を表現できません。実装前に、
少なくとも次を比較します。

- Maya標準と同様に、すべてのelementをlinearとして内部数値を乗算する。
- `value: doubleLinear`と`factor[]: double`へattribute構造を変更する。
- 明確な利用例が得られるまで`Multi`版を作らない。

### Divide

linear valueに対する除算には、異なる2つの自然な結果があります。

```text
doubleLinear / double       -> doubleLinear
doubleLinear / doubleLinear -> double
```

`DblL` / `DblL3` familyとしては、距離をdimensionless factorで割り、距離を返す
前者を優先します。

```text
bdDblL_Divide:  doubleLinear  / double  -> doubleLinear
bdDblL3_Divide: doubleLinear3 / double3 -> doubleLinear3
```

距離同士の比率は出力が`double`になるため、`DblL` familyへ含めません。必要になった
時点でratio nodeとして別に設計します。

`DivideMulti`も同型配列を直接移植せず、`value`と`divisor[]`を分ける案、または
実装を見送る案を比較します。安全除算のepsilonは、divisorを`double`にする場合は
dimensionless値として定義します。

### Power

`distance ^ exponent`は、exponentが`1`以外の場合、一般にはdistanceを出力しません。
内部centimeter値へ`std::pow()`を適用し、その結果をdistanceとして格納することは
可能ですが、unit attributeとして直感的なAPIにはなりません。

`Power` / `PowerMulti`は初回のlinear unit展開から外します。具体的なリグ用途と、
内部centimeter基準の数値演算であることを正当化できた場合だけ再検討します。

## C++ Attribute Implementation Direction

既存の`NumericAttribute` / `Double3Attribute` helperは`MFnNumericData::kDouble`を
作成します。linear unit版では、責務を混在させず専用helperを追加する方向とします。

想定する責務です。

- scalar `doubleLinear`を`MFnUnitAttribute::kDistance`で作成する。
- XYZのunit childとnumeric parentをまとめて作成する。
- input / outputの標準flagをnumeric attributeとunit attributeの両方へ適用する。
- default、min / max、soft min / soft maxを`MDistance`として指定できるようにする。
- compoundの親と子の`MObject`をすべて保持し、dirty伝搬と子plug要求を明示する。

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
- Multiply / Divide / Powerのidentity `1`は、linear attributeでは`1 cm`になるため、
  attributeの役割を決めてからdefaultを確定する。
- Map Rangeの`1`は`1 cm`のrange endpointとして有効だが、その意味をテストと
  node仕様に記載する。

UI表示値を直接計算値として使わず、内部centimeter値を基準にします。sceneの
`currentUnit(linear=...)`を変更しても、既存scene内の物理的な距離とnode出力が変化しない
ことを必須条件にします。

## Python API And Generation

NodeOperatorのattribute解決には、親`double3`、子`doubleLinear`、子数3の組み合わせを
`DoubleLinear3AttrOperator`へ解決する既存処理があります。そのため、plugin nodeを
登録した後のclass / attribute生成は、既存generatorを利用できる見込みです。

実装時には見込みだけで完了とせず、次を確認します。

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
5. Multiply / Divideの固定入力版について、mixed-type attribute仕様とdefaultを確定する。
6. 実用性を確認してからMultiply / Divideの`Multi`版を判断する。
7. Power familyは具体的な用途が提示されるまで保留する。

node typeは実装する単位だけ登録し、未実装分の`MTypeId`を先に消費しません。
IDは実装開始前に[Node ID Registry](../NODE_IDS.md)へ追加します。

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
| 初回展開 | 距離を保つ18種を実装済み |
| Condition比較型 | scalar `doubleLinear` |
| Condition選択値 / 出力 | typed-any。同じnode内では接続型を統一する |
| Condition展開 | `bdAny_ConditionDblL` / `bdAny_ConditionDblLMulti`を実装済み |
| Multiply固定版 | linear valueとdimensionless factorのmixed-typeを優先検討 |
| Divide固定版 | linear valueをdimensionless divisorで割る仕様を優先検討 |
| Multiply / Divide Multi | attribute構造を確定するまで未実装 |
| Power family | 具体的用途が得られるまで保留 |
