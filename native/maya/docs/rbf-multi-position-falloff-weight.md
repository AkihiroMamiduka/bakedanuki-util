# RBF Multi Position Falloff Weight

`bdRbf_MultiPositionFalloffWeight`は、複数の3次元位置とposeの距離を加重RMSで1つにまとめ、
その距離へ直接falloffを適用するdependency nodeです。

単一driverでは[`bdRbf_PositionFalloffWeight`](rbf-position-falloff-weight.md)、補間solveが
必要な場合は[`bdRbf_MultiPositionWeight`](rbf-multi-position-weight.md)を使用します。

## Distance And Topology

```text
d_j = length(inputPosition_j - posePosition_j)
D   = sqrt(sum(influence_j * d_j^2) / sum(influence_j))
```

全positionは同じ座標空間の値として比較します。各有効poseの
`pose[].sourcePosition[]`には、`source[]`と同じlogical indexをすべて登録します。
一致しない場合は`IncompletePose`です。

`influence = 0`のsourceは距離とposition検証から除外しますが、index要素は必要です。
全sourceのinfluenceが0の場合は`InvalidInfluence`です。

## Falloff And Radius Override

統合距離`D`へ1回だけfalloffを適用します。通常はnode共通の`innerRadius` / `outerRadius`を
使い、特定poseだけ`pose[].useRadiusOverride`で上書きできます。各poseのweightは独立し、
合計1へ正規化しません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `source[]` | compound multi | empty | position source定義 |
| `source[].inputPosition` | `doubleLinear3` | `(0, 0, 0)` | 現在のsource position |
| `source[].influence` | `double` | `1` | 加重RMS距離への非負の影響度 |
| `innerRadius` | `doubleLinear` | `0 cm` | 共通のweight 1範囲 |
| `outerRadius` | `doubleLinear` | `1 cm` | 共通のweight 0境界 |
| `falloff` | enum | `CompactQuintic` | `Linear` / `CompactCubic` / `CompactQuintic` |
| `pose[]` | compound multi | empty | pose定義 |
| `pose[].sourcePosition[]` | `doubleLinear3` multi | `(0, 0, 0)` | sourceごとのpose position |
| `pose[].enabled` | `bool` | `true` | 評価への参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose固有半径を使うか |
| `pose[].innerRadiusOverride` | `doubleLinear` | `0 cm` | pose固有のweight 1範囲 |
| `pose[].outerRadiusOverride` | `doubleLinear` | `1 cm` | pose固有のweight 0境界 |
| `outputWeight[]` | `double` multi | - | poseと同じlogical indexの`[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ`true` |
| `falloffStatus` | enum | - | 失敗理由 |

`falloffStatus`は`Success = 0`、`NoPoses = 1`、`InvalidRadius = 2`、
`InvalidPosition = 3`、`UnsupportedFalloff = 4`、`NumericalFailure = 5`、
`NoSources = 6`、`InvalidInfluence = 7`、`IncompletePose = 8`です。

## Performance And Cache

通常評価は`O(NS)`です。pose position、topology、radius、falloffを設定cacheへ保存し、
source inputだけが変わる通常評価では再構築しません。radius系attributeの毎フレームanimationは
性能保証の対象外です。
