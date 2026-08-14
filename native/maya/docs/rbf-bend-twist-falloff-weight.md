# RBF Bend Twist Falloff Weight

`bdRbf_BendTwistFalloffWeight` は、QuaternionをBendとTwistへ分解し、それぞれの一致度を
別の半径で評価する独立falloff weight nodeです。

`BendTwist` modeではBendとTwistの両方を比較し、`BendOnly` modeではTwistを完全に無視して
骨の向きだけを比較します。出力は [`bdRbf_PoseBlend`](rbf-pose-blend.md) の `weight[]`へ
multi attributeの親同士で接続できます。

複数driverを1つの距離へ統合する場合は
[`bdRbf_MultiBendTwistFalloffWeight`](rbf-multi-bend-twist-falloff-weight.md)を使用します。

## Axis And Order

分解規約は [`bdQuat_DecomposeBendTwist`](quaternion-nodes.md#bend--twist-convention) と共通です。

- canonical X軸: Twist軸
- canonical Y/Z軸: Bend平面
- `axisQuat`: 意味上のXYZ基準への変換
- `order`: `TwistBend`または`BendTwist`のfactor順

inputと全poseに同じ `axisQuat` / `order` を適用します。Twist軸がdriverのローカルX軸なら
既定のidentity `axisQuat`を使用できます。

## Bend Distance

Bend factorからcanonical X軸を回転した単位ベクトルを作り、現在方向とpose方向の角度を
比較します。

```text
inputDirection = rotate((1, 0, 0), inputBend)
poseDirection  = rotate((1, 0, 0), poseBend)
bendDistance   = acos(clamp(dot(inputDirection, poseDirection), -1, 1))
```

この距離はBendの量と曲がる方角の両方を含みます。同じBendでTwistだけが異なるorientationは
`bendDistance = 0`です。Bend量を無視して曲がる方角だけを比較する処理ではありません。

## Twist Distance

Twistは周期角度なので、`[-180°, 180°)`の最短角度差を使います。

```text
twistDistance = abs(shortestAngleDelta(inputTwist, poseTwist))
```

したがって `170°` と `-170°` の距離は `20°` です。180° BendのTwist射影特異点では、既存の
Bend/Twist分解規約と同様にTwistを0°へ固定します。

## Weight Combination

BendとTwistはそれぞれ独立したinner/outer radiusでfalloffを計算します。

```text
bendWeight  = falloff(bendDistance,  bendInnerRadius,  bendOuterRadius)
twistWeight = falloff(twistDistance, twistInnerRadius, twistOuterRadius)

BendTwist mode: weight = bendWeight * twistWeight
BendOnly mode:  weight = bendWeight
```

積を使うため、どちらかがouter radius以上ならweightは0です。両方が中間値の場合は双方の
不一致が重なってweightをさらに下げます。`BendOnly`ではTwist factorの距離、Twist半径、
Twist override値をweight判定に使用しません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `inputQuat` | `double4` | `(0, 0, 0, 1)` | 現在のdriver orientation |
| `axisQuat` | `double4` | `(0, 0, 0, 1)` | Bend/Twist基準変換 |
| `order` | enum | `TwistBend` | factorの積順 |
| `mode` | enum | `BendTwist` | Twistを評価するか |
| `bendInnerRadius` | `doubleAngle` | `0°` | Bend weight 1範囲 |
| `bendOuterRadius` | `doubleAngle` | `60°` | Bend weight 0境界 |
| `twistInnerRadius` | `doubleAngle` | `0°` | Twist weight 1範囲 |
| `twistOuterRadius` | `doubleAngle` | `60°` | Twist weight 0境界 |
| `falloff` | enum | `CompactQuintic` | Bend/Twist共通の減衰曲線 |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].poseQuat` | `double4` | `(0, 0, 0, 0)` | pose orientation。zeroは未設定 |
| `pose[].enabled` | `bool` | `true` | poseの参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose固有の4半径を使うか |
| `pose[].bendInnerRadiusOverride` | `doubleAngle` | `0°` | pose固有Bend inner radius |
| `pose[].bendOuterRadiusOverride` | `doubleAngle` | `60°` | pose固有Bend outer radius |
| `pose[].twistInnerRadiusOverride` | `doubleAngle` | `0°` | pose固有Twist inner radius |
| `pose[].twistOuterRadiusOverride` | `doubleAngle` | `60°` | pose固有Twist outer radius |
| `outputWeight[]` | `double` multi | - | poseと同じlogical indexの`[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ`true` |
| `falloffStatus` | enum | - | 失敗理由 |

各weightは独立し、合計1へ正規化しません。BendOnlyでBendが同じposeが複数ある場合は、同じ
weightを同時に出力します。最終補正が加算されることを意図してposeを構成してください。

## Falloff Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | 評価成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | 評価対象の半径が無効 |
| 3 | `InvalidQuaternion` | input、axis、または有効pose Quaternionが無効 |
| 4 | `UnsupportedFalloff` | 未対応のfalloff enum |
| 5 | `UnsupportedMode` | 未対応のmode enum |
| 6 | `UnsupportedOrder` | 未対応のorder enum |
| 7 | `NumericalFailure` | 分解、距離、weight計算が非有限 |

失敗時は全pose logical indexのweightを0にし、`isValid = false`にします。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

weight = nodes.create.bdRbf_BendTwistFalloffWeight(
    name="shoulder_bend_falloff"
)
blend = nodes.create.bdRbf_PoseBlend(name="shoulder_corrective_blend")

weight.mode.set(weight.mode.BENDONLY)
weight.pose[0].poseQuat.set((0.0, 0.0, 0.0, 1.0))
weight.pose[1].poseQuat.set((0.0, 0.382683, 0.0, 0.923880))
weight.bendInnerRadius.set(10.0)
weight.bendOuterRadius.set(60.0)

blend.pose[1].translate.set((0.0, 1.5, 0.5))
weight.outputWeight.connect(blend.weight)
mod.do_it_dg()
```

## Performance And Animation Policy

評価はpose数を`N`として `O(N)` です。各poseのQuaternion分解と方向・Twist距離を直接計算し、
Eigen、補間行列、QR solve、mutable cacheは使用しません。nodeは`MPxNode::kParallel`です。

radius、axis、order、modeはrig構築時の設定値です。値変更時の再評価は行いますが、毎フレーム
これらをアニメーションする運用はサポートおよび性能保証の対象外です。
