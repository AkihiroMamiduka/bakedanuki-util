# Condition Nodes

`Condition` family は scalar の比較結果に応じて、指定した値を出力します。
Maya 標準の `condition` node に馴染みのある用途を、`double` / `double3` と
複数条件へ拡張した node family です。

## Node Types

| Node type | 条件数 | 出力型 |
| --- | --- | --- |
| `bdDbl_Condition` | 1 | `double` |
| `bdDbl_ConditionMulti` | 0以上 | `double` |
| `bdDbl3_Condition` | 1 | `double3` |
| `bdDbl3_ConditionMulti` | 0以上 | `double3` |

`double3` 版も比較対象は scalar の `input` / `compare` です。vector の大小関係を
暗黙に定義せず、比較結果によって `double3` 全体を選択します。

## Operations

`operation` enum は Maya 標準 `condition` と同じ順序です。

| 値 | ラベル | 条件 |
| ---: | --- | --- |
| 0 | Equal | `input == compare` |
| 1 | Not Equal | `input != compare` |
| 2 | Greater Than | `input > compare` |
| 3 | Greater or Equal | `input >= compare` |
| 4 | Less Than | `input < compare` |
| 5 | Less or Equal | `input <= compare` |

比較は epsilon を暗黙に適用しない IEEE 754 の通常比較です。`NaN` では
Not Equal だけが true になり、それ以外は false になります。無限値は通常の
大小関係で比較します。

## Single Condition

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | `double` | `0` | 比較する入力値 |
| `operation` | `op` | enum | Equal | 比較演算 |
| `compare` | `cmp` | `double` | `0` | 比較対象値 |
| `trueValue` | `tv` | `double` / `double3` | zero | 条件成立時の値 |
| `falseValue` | `fv` | `double` / `double3` | zero | 条件不成立時の値 |
| `output` | `o` | `double` / `double3` | zero | 選択結果 |

```python
output = trueValue if compare(input, operation, compare) else falseValue
```

`trueValue` も true を数値化した `1` ではなく、選択値として中立な zero を
default にします。

## Multiple Conditions

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | `double` | `0` | 全 case で共有する入力値 |
| `case[]` | `cs[]` | compound multi | empty | 条件と選択値 |
| `case[].operation` | `op` | enum | Equal | case の比較演算 |
| `case[].compare` | `cmp` | `double` | `0` | case の比較対象値 |
| `case[].value` | `v` | `double` / `double3` | zero | case 成立時の値 |
| `elseValue` | `ev` | `double` / `double3` | zero | 一致しない場合の値 |
| `output` | `o` | `double` / `double3` | zero | 選択結果 |

`case[]` は sparse array を許可します。物理配置順ではなく logical index の
昇順で評価し、最初に成立した case の `value` を出力します。一致する case が
ない場合と空配列の場合は `elseValue` を出力します。

```python
for current_case in cases_in_logical_index_order:
    if compare(input, current_case.operation, current_case.compare):
        return current_case.value
return elseValue
```
