# Condition Nodes

`Condition` familyはscalar値の比較結果に応じて、接続されたデータを選択して出力します。
比較型だけをnode typeで固定し、選択値と出力にはMaya標準`choice`と同じ
typed-any attributeを使用します。基本条件へ`extra[]`を`And` / `Or`で順番に結合し、
1つの選択肢へ複数の比較条件を指定できます。

## Node Types

| Node type | 条件数 | 比較型 | 選択値 / 出力 |
| --- | ---: | --- | --- |
| `bdAny_ConditionDbl` | 1 | scalar `double` | typed-any |
| `bdAny_ConditionDblMulti` | 0以上 | scalar `double` | typed-any |
| `bdAny_ConditionDblL` | 1 | scalar `doubleLinear` | typed-any |
| `bdAny_ConditionDblLMulti` | 0以上 | scalar `doubleLinear` | typed-any |

node type名は次の要素で構成します。

```text
bdAny_ConditionDblLMulti
  Any       選択値と出力がtyped-any
  Condition 比較結果による選択
  DblL      inputとcompareがdoubleLinear
  Multi     複数条件版
```

比較型は`input`と`compare`の両方に適用します。将来`doubleAngle`版を追加する場合も、
同じ方針で両方を`doubleAngle`にします。

## Typed-any Payload

選択値と出力は`MFnTypedAttribute`を`MFnData::kAny`で作成します。attribute宣言は
常に`typed`ですが、選択された入力の具体的なデータが`MDataHandle::copy()`で出力へ
渡されます。

`double`、`doubleLinear`、`doubleAngle`、`double3`、matrix、stringなどを接続できます。
ただし、1つのConditionへ接続するすべての選択候補と出力先は、同じMayaデータ型、
または明確に互換性のある型へ統一してください。typed-anyは異種型の接続自体を
拒否しないため、型を混在させると単位の内部値が別単位として解釈されたり、
互換性のない出力がzeroになる可能性があります。

NodeOperatorではtyped-any plugを接続専用として扱います。`trueValue`、`falseValue`、
`case[].value`、`elseValue`、`output`では`.connect()`または`>`を使用し、`.get()` /
`.set()`は使用しません。値を固定したい場合も、型が確定したValue nodeなどから
接続します。

## Operations

`operation` enumはMaya標準`condition`と同じ順序です。

| 値 | ラベル | 条件 |
| ---: | --- | --- |
| 0 | Equal | `input == compare` |
| 1 | Not Equal | `input != compare` |
| 2 | Greater Than | `input > compare` |
| 3 | Greater or Equal | `input >= compare` |
| 4 | Less Than | `input < compare` |
| 5 | Less or Equal | `input <= compare` |

比較はepsilonを暗黙に適用しないIEEE 754の通常比較です。`NaN`ではNot Equalだけが
trueになり、それ以外はfalseになります。無限値は通常の大小関係で比較します。

`doubleLinear`比較はMaya内部のdistance値で行います。`input`と`compare`が同じ
unit attributeなので、表示単位を変更しても比較する距離の意味は維持されます。

## Extra Conditions

追加条件は次のcompound arrayです。

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `extra[]` | `ex[]` | compound multi | empty | 追加条件 |
| `extra[].logic` | `lgc` | enum | And | 直前までの結果との結合方法 |
| `extra[].comparison` | `cpr` | enum | Equal | 追加の比較演算 |
| `extra[].compareValue` | `cv` | `double` / `doubleLinear` | `0` | 追加の比較対象値 |

`logic`は`And = 0`、`Or = 1`です。`comparison`は基本条件の`operation`と同じ
6種類の比較演算を使用します。`compareValue`はnode typeで指定された比較型に従います。

基本条件の結果から開始し、`extra[]`をlogical indexの昇順で左から畳み込みます。
通常の演算子優先順位や暗黙のグループ化は適用しません。

```python
result = compare(input, operation, compare)
for extra_condition in extras_in_logical_index_order:
    current = compare(
        input,
        extra_condition.comparison,
        extra_condition.compareValue,
    )
    result = apply_logic(result, extra_condition.logic, current)
```

例えば基本条件が`input < 10`、`extra[0]`が`And`と`input > 0`なら、最終条件は
`input < 10 and input > 0`です。`extra[]`が空の場合は、追加前と同じ基本条件だけを
評価します。

## Single Condition

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | `double` / `doubleLinear` | `0` | 比較する入力値 |
| `operation` | `op` | enum | Equal | 比較演算 |
| `compare` | `cmp` | `double` / `doubleLinear` | `0` | 比較対象値 |
| `extra[]` | `ex[]` | compound multi | empty | 基本条件へ結合する追加条件 |
| `trueValue` | `tv` | typed-any | null | 条件成立時の接続値 |
| `falseValue` | `fv` | typed-any | null | 条件不成立時の接続値 |
| `output` | `o` | typed-any | null | 選択結果 |

```python
output = trueValue if compare(input, operation, compare) else falseValue
```

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

true_value = nodes.create.bdDblL_Value(name="true_value")
false_value = nodes.create.bdDblL_Value(name="false_value")
condition = nodes.create.bdAny_ConditionDblL(name="condition")
result = nodes.create.bdDblL_Add(name="result")

true_value.value.set(10.0)
false_value.value.set(-10.0)
condition.input.set(5.0)
condition.operation.set(condition.operation.GREATER_THAN)
condition.compare.set(3.0)
condition.extra[0].logic.set(condition.extra[0].logic.AND)
condition.extra[0].comparison.set(
    condition.extra[0].comparison.LESS_THAN
)
condition.extra[0].compareValue.set(10.0)

true_value.value > condition.trueValue
false_value.value > condition.falseValue
condition.output > result.input1

mod.do_it_dg()
```

## Multiple Conditions

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | `double` / `doubleLinear` | `0` | 全caseで共有する入力値 |
| `case[]` | `cs[]` | compound multi | empty | 条件と選択値 |
| `case[].operation` | `op` | enum | Equal | caseの比較演算 |
| `case[].compare` | `cmp` | `double` / `doubleLinear` | `0` | caseの比較対象値 |
| `case[].extra[]` | `ex[]` | compound multi | empty | caseの基本条件へ結合する追加条件 |
| `case[].value` | `v` | typed-any | null | case成立時の接続値 |
| `elseValue` | `ev` | typed-any | null | 一致しない場合の接続値 |
| `output` | `o` | typed-any | null | 選択結果 |

各caseの`extra[]`はSingle版と同じattribute構造です。`case[]`と各`extra[]`は
sparse arrayを許可し、それぞれ物理配置順ではなくlogical indexの昇順で評価します。
最初に最終条件が成立したcaseの`value`を出力します。一致するcaseがない場合と
空配列の場合は`elseValue`を出力します。

```python
for current_case in cases_in_logical_index_order:
    result = compare(input, current_case.operation, current_case.compare)
    for extra_condition in current_case.extras_in_logical_index_order:
        current = compare(
            input,
            extra_condition.comparison,
            extra_condition.compareValue,
        )
        result = apply_logic(result, extra_condition.logic, current)
    if result:
        return current_case.value
return elseValue
```

選択される可能性があるpayloadはすべて接続することを推奨します。未接続のtyped-any
attributeはnull dataであり、固定のscalar zeroやzero vectorを共通defaultとして
保証しません。
