# Average Nodes

`Average` family は `double` / `double3` の算術平均を出力します。2値を直接扱う
固定2入力版と、0個以上の値を扱う `Multi` 版を用意します。

## Node Types

| Node type | 入力数 | 出力型 |
| --- | ---: | --- |
| `bdDbl_Average` | 2 | `double` |
| `bdDbl_AverageMulti` | 0以上 | `double` |
| `bdDbl3_Average` | 2 | `double3` |
| `bdDbl3_AverageMulti` | 0以上 | `double3` |

`double3` 版は XYZ の各成分を独立して平均します。

## Fixed Two Inputs

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input1` | `i1` | `double` / `double3` | zero | 1つ目の入力値 |
| `input2` | `i2` | `double` / `double3` | zero | 2つ目の入力値 |
| `output` | `o` | `double` / `double3` | zero | 算術平均 |

計算は単純合計方式です。

```python
output = (input1 + input2) / 2
```

## Multiple Inputs

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input[]` | `i[]` | `double` / `double3` multi | empty | 平均する入力値 |
| `output` | `o` | `double` / `double3` | zero | 算術平均 |

`input[]` は sparse array を許可します。既存要素だけを logical index の昇順で
合計し、既存要素数で割ります。logical index の最大値や未作成の隙間は要素数に
含めません。

```python
values = existing_values_in_logical_index_order
output = sum(values) / len(values) if values else 0
```

空配列は zero、要素が1つだけの場合はその値を出力します。

## Numeric Behavior

速度と実装の単純さを優先し、段階的に平均を更新せず、すべての値を合計してから
要素数で割ります。このため、最終的な平均が有限値に収まる組み合わせでも、中間の
合計値が `double` の範囲を超えると `inf` になる場合があります。

`NaN` は通常の IEEE 754 演算どおり伝播します。同符号の無限値は同じ無限値を、
正負の無限値が混在する合計は `NaN` を出力します。有限値だけの一般的なリグ用途では、
追加の分岐を持たない単純合計方式を標準とします。
