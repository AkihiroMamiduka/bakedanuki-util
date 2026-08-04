# Weighted Average Nodes

`Weighted Average` familyは、valueごとのscalar weightを合計値で正規化し、
`double` / `double3` の加重平均を出力します。任意個の入力を同じ構造で扱えるため、
固定2入力版は設けず `Multi` 版だけを用意します。

## Node Types

| Node type | value型 | weight型 | 出力型 |
| --- | --- | --- | --- |
| `bdDbl_WeightedAverageMulti` | `double` | `double` | `double` |
| `bdDbl3_WeightedAverageMulti` | `double3` | `double` | `double3` |

`double3`版では、1つのscalar weightをXYZの各成分へ適用します。

## Attributes

| Attribute | Short | 型 | Default | 用途 |
| --- | --- | --- | --- | --- |
| `input[]` | `i[]` | compound multi | empty | value / weightの入力配列 |
| `input[].value` | `v` | `double` / `double3` | zero | 加重する値 |
| `input[].weight` | `w` | `double` | `0` | valueへ掛けるweight |
| `output` | `o` | `double` / `double3` | zero | 正規化した加重平均 |

weightのdefaultは`0`です。作成しただけの要素は平均へ影響せず、weightを明示した
要素だけが有効になります。weightへmin / max制限は設けず、負のweightによる外挿も
許可します。

## Calculation

`input[]`はsparse arrayを許可します。既存要素のうちweightが非zeroの要素を
logical indexの昇順で単純加算します。

```python
active = [item for item in existing_items if item.weight != 0]
weighted_sum = sum(item.value * item.weight for item in active)
weight_sum = sum(item.weight for item in active)
output = weighted_sum / weight_sum if weight_sum != 0 else 0
```

weight合計の判定にはepsilonを使用しません。非常に小さくても正確に非zeroなら通常の
除算を行うため、すべてのweightを同じ倍率で拡大・縮小しても加重平均の意味を保てます。

空配列、全weightがzeroの場合、正負のweightが正確に相殺した場合はzeroを出力します。
この判定はweighted sumの状態より優先します。

## Zero Weight And Non-finite Values

`weight == 0.0`の要素はvalueを読み込まず完全に無視します。このため、そのvalueが
`NaN`や無限値でも出力へ影響しません。`-0.0`もzero weightとして扱います。

非zero weightを持つ`NaN`、無限値、または非有限weightは、通常のIEEE 754演算どおり
伝播します。weighted sumとweight sumは段階的な安定化を行わない単純合計方式なので、
中間値が`double`の範囲を超えた場合も通常どおり`inf`になる場合があります。
