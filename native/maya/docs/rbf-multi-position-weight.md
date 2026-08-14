# RBF Multi Position Weight

`bdRbf_MultiPositionWeight`は、複数の3次元位置を1組のdriverとして扱い、登録済みposeとの
一致度から補間weightを計算するdependency nodeです。単一driverでは
[`bdRbf_PositionWeight`](rbf-position-weight.md)を使用します。

## Source And Pose Layout

`source[]`のlogical indexがdriverの次元を定義し、各有効poseの
`pose[].sourcePosition[]`には同じlogical indexをすべて登録します。

```text
source[2].inputPosition
source[8].inputPosition

pose[3].sourcePosition[2]
pose[3].sourcePosition[8]
```

不足または余分なsource indexがある有効poseは`IncompletePose`です。無効poseは検証と
solveから除外され、対応する出力は0になります。座標空間の変換は行わず、全入力を同じ空間の
値としてそのまま比較します。

## Multi-Source Distance

source `j`のEuclidean distanceを`d_j`、非負の影響度を`a_j`として、加重RMS距離を使います。

```text
d_j = length(inputPosition_j - posePosition_j)
D   = sqrt(sum(a_j * d_j^2) / sum(a_j))
```

`D`はlinear unitです。source数で正規化するため、同じ距離だけずれたsourceを増やしても
`radius`の意味は変わりません。sourceが1つなら`bdRbf_PositionWeight`と同じ距離です。

`influence = 0`のsourceは距離とposition検証から除外しますが、pose内のindex対応は必要です。
全sourceのinfluenceが0の場合は`InvalidInfluence`です。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `source[]` | compound multi | empty | position source定義 |
| `source[].inputPosition` | `doubleLinear3` | `(0, 0, 0)` | 現在のsource position |
| `source[].influence` | `double` | `1` | 加重RMS距離への非負の影響度 |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].sourcePosition[]` | `doubleLinear3` multi | `(0, 0, 0)` | source indexごとのpose position |
| `pose[].enabled` | `bool` | `true` | solveへの参加切替 |
| `kernel` | enum | `CompactQuintic` | RBF kernel |
| `radius` | `doubleLinear` | `1 cm` | 加重RMS距離のスケール |
| `regularization` | `double` | `1.0e-8` | 補間行列の対角へ加える非負値 |
| `allowNegativeWeights` | `bool` | `false` | `false`なら負weightを0へclamp |
| `outputWeight[]` | `double` multi | - | poseと同じlogical indexのweight |
| `isValid` | `bool` | - | solve成功時だけ`true` |
| `solveStatus` | enum | - | 失敗理由 |

`solveStatus`は単一position版の0～8に加え、`NoSources = 10`、
`InvalidInfluence = 11`、`IncompletePose = 12`を使用します。

## Performance And Cache

pose数を`N`、source数を`S`とすると、設定変更時の距離行列構築は`O(N^2 S)`、
factorizationは概ね`O(N^3)`です。通常評価ではfactorizationを再利用し、`O(NS)`の
kernel vector構築とQR solveを行います。

pose、source index、influence、kernel、radius、regularizationの変更時だけcacheを
再構築します。radiusの毎フレームanimationは性能保証の対象外です。
