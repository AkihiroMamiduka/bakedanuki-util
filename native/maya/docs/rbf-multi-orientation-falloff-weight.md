# RBF Multi Orientation Falloff Weight

`bdRbf_MultiOrientationFalloffWeight`は、複数のQuaternion orientationとposeの距離を
加重RMSで1つにまとめ、その距離へ直接falloffを適用するdependency nodeです。

単一driverでは[`bdRbf_OrientationFalloffWeight`](rbf-orientation-falloff-weight.md)、
補間solveが必要な場合は
[`bdRbf_MultiOrientationWeight`](rbf-multi-orientation-weight.md)を使用します。

## Distance And Topology

各sourceのQuaternion最短角度距離を`d_j`、非負の影響度を`a_j`として計算します。

```text
d_j = 2 * acos(clamp(abs(dot(input_j, pose_j)), 0, 1))
D   = sqrt(sum(a_j * d_j^2) / sum(a_j))
```

各有効poseの`pose[].sourceQuat[]`は、`source[]`と同じlogical index構成が必要です。
一致しない場合は`IncompletePose`です。`influence = 0`のsourceは距離とQuaternion検証から
除外しますが、index要素自体は必要です。

## Falloff

統合距離`D`へ1回だけfalloffを適用します。sourceごとのweightを乗算しないため、source数を
増やしても減衰が過度に狭くなりません。

```text
D <= innerRadius : weight = 1
D >= outerRadius : weight = 0
otherwise        : falloff((D - innerRadius) / (outerRadius - innerRadius))
```

特定poseだけ範囲を変える場合は`pose[].useRadiusOverride`とpose固有のinner / outer radiusを
使用します。各poseのweightは独立し、合計1へ正規化しません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `source[]` | compound multi | empty | orientation source定義 |
| `source[].inputQuat` | `double4` | identity | 現在のsource orientation |
| `source[].influence` | `double` | `1` | 加重RMS距離への非負の影響度 |
| `innerRadius` | `doubleAngle` | `0°` | 共通のweight 1範囲 |
| `outerRadius` | `doubleAngle` | `60°` | 共通のweight 0境界 |
| `falloff` | enum | `CompactQuintic` | `Linear` / `CompactCubic` / `CompactQuintic` |
| `pose[]` | compound multi | empty | pose定義 |
| `pose[].sourceQuat[]` | `double4` multi | zero | source indexごとのpose orientation |
| `pose[].enabled` | `bool` | `true` | 評価への参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose固有半径を使うか |
| `pose[].innerRadiusOverride` | `doubleAngle` | `0°` | pose固有のweight 1範囲 |
| `pose[].outerRadiusOverride` | `doubleAngle` | `60°` | pose固有のweight 0境界 |
| `outputWeight[]` | `double` multi | - | poseと同じlogical indexの`[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ`true` |
| `falloffStatus` | enum | - | 失敗理由 |

`falloffStatus`は`Success = 0`、`NoPoses = 1`、`InvalidRadius = 2`、
`InvalidQuaternion = 3`、`UnsupportedFalloff = 4`、`NumericalFailure = 5`、
`NoSources = 6`、`InvalidInfluence = 7`、`IncompletePose = 8`です。

## Performance And Cache

通常評価は`O(NS)`です。pose Quaternionの正規化、topology、radius、falloffは設定cacheへ
保存し、source inputだけが変わる通常評価では再構築しません。node instanceごとのmutexで
cacheを保護し、`MPxNode::kParallel`で評価します。
