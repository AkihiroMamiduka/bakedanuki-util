# RBF Multi Bend Twist Falloff Weight

`bdRbf_MultiBendTwistFalloffWeight`は、複数のQuaternion sourceをそれぞれBendとTwistへ
分解し、Bend距離とTwist距離を別々の加重RMSへまとめて直接falloffを適用するdependency
nodeです。

単一driverでは
[`bdRbf_BendTwistFalloffWeight`](rbf-bend-twist-falloff-weight.md)を使用します。出力は
[`bdRbf_PoseBlend`](rbf-pose-blend.md)の`weight[]`へmulti attributeの親同士で接続できます。

## Source Decomposition

各`source[]`は、現在のorientationに加えて固有のBend/Twist分解設定を持ちます。

- `axisQuat`: 意味上のcanonical XYZ基準への変換
- `order`: `TwistBend`または`BendTwist`のfactor順
- `influence`: source距離の非負の影響度

canonical X軸がTwist軸、Y/Z軸がBend平面です。分解規約は
[`bdQuat_DecomposeBendTwist`](quaternion-nodes.md#bend--twist-convention)と共通です。
各sourceの`axisQuat` / `order`は、現在値と全poseの同じsource indexへ共通して適用します。

## Distance Aggregation

source `j`のBend方向角度差を`b_j`、Twist最短角度差を`t_j`、非負の影響度を`a_j`として、
2つの距離を別々に統合します。

```text
B = sqrt(sum(a_j * b_j^2) / sum(a_j))
T = sqrt(sum(a_j * t_j^2) / sum(a_j))
```

Bend距離は、Bend factorでcanonical X軸を回転した2方向間の角度です。Bend量と曲がる方角の
両方を含み、Twistだけの違いは含みません。Twist距離は`[-180°, 180°)`の最短角度差です。

各有効poseの`pose[].sourceQuat[]`は、`source[]`と同じlogical index構成が必要です。
一致しない場合は`IncompletePose`です。`influence = 0`のsourceは距離、Quaternion、軸、
orderの検証から除外しますが、index要素自体は必要です。

## Weight Combination

統合したBend距離とTwist距離へ、それぞれ一度だけfalloffを適用します。

```text
bendWeight  = falloff(B, bendInnerRadius, bendOuterRadius)
twistWeight = falloff(T, twistInnerRadius, twistOuterRadius)

BendTwist mode: weight = bendWeight * twistWeight
BendOnly mode:  weight = bendWeight
```

sourceごとのweightは乗算しないため、source数を増やしても影響範囲が過度に狭くなりません。
`BendOnly`ではTwist距離、Twist半径、Twist radius overrideを評価しません。各poseのweightは
独立し、合計1へ正規化しません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `source[]` | compound multi | empty | Quaternion source定義 |
| `source[].inputQuat` | `double4` | identity | 現在のsource orientation |
| `source[].axisQuat` | `double4` | identity | source固有のBend/Twist基準変換 |
| `source[].order` | enum | `TwistBend` | source固有のfactor積順 |
| `source[].influence` | `double` | `1` | Bend/Twist加重RMSに共通する非負の影響度 |
| `mode` | enum | `BendTwist` | Twistも評価するか |
| `bendInnerRadius` | `doubleAngle` | `0°` | 共通Bend weight 1範囲 |
| `bendOuterRadius` | `doubleAngle` | `60°` | 共通Bend weight 0境界 |
| `twistInnerRadius` | `doubleAngle` | `0°` | 共通Twist weight 1範囲 |
| `twistOuterRadius` | `doubleAngle` | `60°` | 共通Twist weight 0境界 |
| `falloff` | enum | `CompactQuintic` | `Linear` / `CompactCubic` / `CompactQuintic` |
| `pose[]` | compound multi | empty | pose定義 |
| `pose[].sourceQuat[]` | `double4` multi | zero | source indexごとのpose orientation |
| `pose[].enabled` | `bool` | `true` | 評価への参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose固有の4半径を使うか |
| `pose[].bendInnerRadiusOverride` | `doubleAngle` | `0°` | pose固有Bend inner radius |
| `pose[].bendOuterRadiusOverride` | `doubleAngle` | `60°` | pose固有Bend outer radius |
| `pose[].twistInnerRadiusOverride` | `doubleAngle` | `0°` | pose固有Twist inner radius |
| `pose[].twistOuterRadiusOverride` | `doubleAngle` | `60°` | pose固有Twist outer radius |
| `outputWeight[]` | `double` multi | - | poseと同じlogical indexの`[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ`true` |
| `falloffStatus` | enum | - | 失敗理由 |

## Falloff Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | 評価成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | 評価対象の半径が無効 |
| 3 | `InvalidQuaternion` | 有効sourceのinput、axis、またはpose Quaternionが無効 |
| 4 | `UnsupportedFalloff` | 未対応のfalloff enum |
| 5 | `UnsupportedMode` | 未対応のmode enum |
| 6 | `UnsupportedOrder` | 有効sourceのorder enumが未対応 |
| 7 | `NumericalFailure` | 分解、距離、weight計算が非有限 |
| 8 | `NoSources` | sourceがない |
| 9 | `InvalidInfluence` | influenceが負、非有限、または有効合計が0 |
| 10 | `IncompletePose` | sourceと有効poseのindex構成が不一致 |

失敗時は全pose logical indexのweightを0にし、`isValid = false`にします。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

weight = nodes.create.bdRbf_MultiBendTwistFalloffWeight(
    name="arm_multi_bend_twist"
)
blend = nodes.create.bdRbf_PoseBlend(name="arm_corrective_blend")

weight.mode.set(weight.mode.BENDONLY)
weight.source[0].inputQuat.set((0.0, 0.0, 0.0, 1.0))
weight.source[0].axisQuat.set((0.0, 0.0, 0.0, 1.0))
weight.source[1].inputQuat.set((0.0, 0.0, 0.0, 1.0))
weight.source[1].influence.set(0.5)
weight.pose[0].sourceQuat[0].set((0.0, 0.0, 0.0, 1.0))
weight.pose[0].sourceQuat[1].set((0.0, 0.0, 0.0, 1.0))

weight.outputWeight.connect(blend.weight)
mod.do_it_dg()
```

## Performance And Animation Policy

通常評価はpose数を`N`、source数を`S`として`O(NS)`です。pose Quaternionの正規化、
Bend方向、Twist角、topology、radius、sourceの軸・order・influenceを設定cacheへ保存します。
source inputだけが変わる通常評価ではcacheを再構築せず、現在sourceを各1回だけ分解します。
Eigenや補間行列は使用しません。node instanceごとのmutexでcacheを保護し、
`MPxNode::kParallel`で評価します。

radius、axis、order、influence、mode、falloff、poseはrig構築時の設定値です。値変更時の再評価は
行いますが、毎フレームこれらをアニメーションする運用はサポートおよび性能保証の対象外です。
