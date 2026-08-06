# Double Angle Node Roadmap

scalar `doubleAngle` node familyの実装順、採用判断、完了境界の記録です。現行仕様は
[Double Angle Nodes](double-angle-nodes.md)を参照してください。

## Baseline

`bdDblA` familyは1軸のangle channelを対象とし、実装済みの通常演算22 nodeは
正規化されていない連続角度として計算します。`370 deg`、`720 deg`、`-450 deg`を
暗黙にwrapしません。

3軸orientationはQuaternionまたはrotate orderを持つEuler rotationの責務とし、
`DblA3` familyと`DblA3_Value`は作りません。

## Decisions

| 項目 | 方針 |
| --- | --- |
| 通常演算 | 連続角度を保持し、暗黙に正規化しない |
| 周期演算 | `Wrap`、`ShortestDelta`、`LerpShortest`として明示する |
| 最短経路補間 | 最短角度差を使うが、出力は正規化しない |
| 正規化が必要な補間 | `LerpShortest.output`を`Wrap.input`へ接続する |
| 3軸回転 | Quaternionまたはrotate order付きEuler nodeを使用する |
| angle default | C++ではradianで設定し、仕様上はdegreeも併記する |

## Implementation Order

| Phase | Scope | Node count | Status |
| ---: | --- | ---: | --- |
| 1 | scalar通常演算のparity完成 | 4 | 実装済み |
| 2 | angle固有の周期演算 | 3 | 実装済み |
| 3 | angle同士のdimensionless比率 | 1 | 実装済み |
| 4 | angle比較のConditionとCompose | 4 | 実装済み |

## Phase 1: Scalar Parity

`double`と`doubleLinear`の両方に存在する、単位を維持できるscalar演算を展開します。

| Node type | 入力 | 出力 | 仕様 |
| --- | --- | --- | --- |
| `bdDblA_Average` | `input1`, `input2` | `doubleAngle` | 2値の算術平均 |
| `bdDblA_AverageMulti` | `input[]` | `doubleAngle` | 既存要素の算術平均。空配列はzero |
| `bdDblA_WeightedSumMulti` | value / weight配列 | `doubleAngle` | `angle * weight`の合計 |
| `bdDblA_WeightedAverageMulti` | value / weight配列 | `doubleAngle` | weight合計で正規化した加重平均 |

すべて連続角度を扱うため、`Average(350 deg, 10 deg)`は`180 deg`です。周期方向の平均へ
暗黙に変更しません。sparse配列、zero weight、weight合計zero、非有限値の扱いは既存の
[Average Nodes](average.md)と[Weighted Average Nodes](weighted-average.md)へ揃えます。

## Phase 2: Periodic Angle Operations

### `bdDblA_Wrap`

| Attribute | 型 | Default | 用途 |
| --- | --- | --- | --- |
| `input` | `doubleAngle` | `0 deg` | 正規化する角度 |
| `min` | `doubleAngle` | `-180 deg` | 出力範囲の下端 |
| `max` | `doubleAngle` | `180 deg` | 出力範囲の上端 |
| `output` | `doubleAngle` | `0 deg` | `[min, max)`へwrapした値 |

出力範囲は半開区間`[min, max)`とします。defaultでは次の結果になります。

```text
180 deg  -> -180 deg
540 deg  -> -180 deg
-181 deg ->  179 deg
```

`NaN`を含む場合は`NaN`を出力します。`max <= min`では`min`を出力します。有効な順序の
範囲で`input`、境界、または範囲幅が非有限になる場合は`NaN`を出力します。この規則は
`Angle.h`へ集約し、境界テストで固定します。

### `bdDblA_ShortestDelta`

`input1`から`input2`への符号付き最短角度差を出力します。

```text
output = Wrap(input2 - input1, -180 deg, 180 deg)

350 deg -> 10 deg  =  20 deg
10 deg  -> 350 deg = -20 deg
0 deg   -> 180 deg = -180 deg
```

出力範囲は`[-180 deg, 180 deg)`です。正反対の角度は最短方向が一意でないため、
半開区間の規則に従い`-180 deg`へ寄せます。

### `bdDblA_LerpShortest`

`input1`から`input2`への最短角度差を使って補間します。`weight`は既存の
`bdDblA_Lerp`と同じdimensionlessな`0..1`とします。

```text
output = input1 + ShortestDelta(input1, input2) * weight

LerpShortest(350 deg, 10 deg, 0.0) = 350 deg
LerpShortest(350 deg, 10 deg, 0.5) = 360 deg
LerpShortest(350 deg, 10 deg, 1.0) = 370 deg
```

出力は正規化しません。これにより補間途中での数値上の360度jumpを避け、後段の差分、
追加回転、速度計算で連続性を維持します。正規化が必要な場合だけ`Wrap`を後段へ接続します。

## Phase 3: Angle Ratio

`bdDbl_RatioDblA`は2つの`doubleAngle`からdimensionlessな`double`を出力します。
type codeは出力型を先頭に置く既存のmixed-type命名へ従います。

| Attribute | 型 | Default | 用途 |
| --- | --- | --- | --- |
| `input` | `doubleAngle` | `0 deg` | 割られる角度 |
| `base` | `doubleAngle` | `360 deg` | 基準角度。C++内部値は2π radian |
| `output` | `double` | `0` | `input / base` |

```text
90 deg  / 360 deg = 0.25
360 deg / 360 deg = 1.0
720 deg / 360 deg = 2.0
```

zero付近の`base`は既存の`SafeDivision.h`と同じ方針で処理します。

## Phase 4: Condition

| Node type | 役割 |
| --- | --- |
| `bdAny_ConditionDblA` | scalar `doubleAngle`による単一条件比較 |
| `bdAny_ConditionDblAMulti` | scalar `doubleAngle`による条件配列比較 |
| `bdConditionDblAExtra_Compose` | `extra[index]`用compoundを構築 |
| `bdConditionDblACase_Compose` | `case[index]`用compoundを構築 |

比較する`input`と`compare`はともに`doubleAngle`とし、値は通常演算と同じ連続角度として
比較します。暗黙のwrapや最短角度比較は行いません。typed-any payload、条件の結合、
sparse配列の規則は[Condition Nodes](condition.md)へ揃えます。

## Deferred Candidates

### `bdDblA_ClosestEquivalent`

wrappedな入力と等価な値のうち、referenceへ最も近い連続角度を選ぶconvenience nodeです。
IK / FK切り替え、wrappedなtargetと累積rotate channelの接続などで利用できます。

```text
input = 10 deg, reference = 350 deg -> 370 deg
output = reference + ShortestDelta(reference, input)
```

`ShortestDelta`と`Add`で構成できるため初回実装対象から外します。同じ接続を繰り返す
実利用が確認できた場合に、graph短縮用nodeとして再検討します。

### Circular Average

`350 deg`と`10 deg`を同じ周期上の方向として平均する場合は、通常の`Average`とは別に
Circular Averageが必要です。反対方向同士で平均方向が定まらない場合の仕様が必要なため、
具体的な用途が得られるまで保留します。

## Out Of Scope

- 独自のSin / Cos / Tan、Asin / Acos / Atan / Atan2
  - 長さを基準に扱うMaya標準nodeを使用します。
- statefulなangle unwrap
  - 過去の評価結果へ依存するため、Parallel EvaluationやCached Playbackとの相性を
    考慮して実装しません。必要な場合はstatelessな`ShortestDelta`を組み合わせます。
- `DblA3`と`DblA3_Value`
  - 3軸orientationはQuaternionまたはrotate order付きEuler nodeで扱います。
- PowerとRight Triangleのangle版
  - angle単位を維持する汎用演算として成立しないため展開しません。

## Definition Of Done

各phaseは、C++ node、attribute、dirty伝搬、plug-in登録、`MTypeId`、NodeOperator生成、
型補完、Maya上の計算・境界・表示単位・評価mode・scene round-tripテスト、関連仕様書の
更新まで完了した時点で実装済みとします。

上記4 phaseはすべてこの完了条件を満たしています。今後の追加候補はDeferred Candidatesに
記載した実利用の確認を前提とし、現在の未完了項目としては扱いません。
