# RBF Orientation Falloff Weight

複数のorientation sourceを1組のdriverとして扱う場合は
[`bdRbf_MultiOrientationFalloffWeight`](rbf-multi-orientation-falloff-weight.md)を使用します。

`bdRbf_OrientationFalloffWeight` は、現在の Quaternion と各 pose Quaternion の最短角度距離から、
pose ごとに独立した falloff weight を計算する dependency node です。

補間行列を解く [`bdRbf_OrientationWeight`](rbf-orientation-weight.md) と異なり、他の pose の位置や数は
個々の weight に影響しません。pose 固有半径、weight 1 の範囲、明示的な0境界が必要な
補助骨correctiveを `O(N)` で評価します。

## Quaternion Distance

入力と pose Quaternion は単位Quaternionへ正規化し、`q` と `-q` を同じorientationとして
扱います。

```text
d(q1, q2) = 2 * acos(clamp(abs(dot(q1, q2)), 0, 1))
```

距離は `0°` から `180°` です。zero Quaternionまたは非有限値は無効です。

## Inner And Outer Radius

```text
d <= innerRadius : weight = 1
d >= outerRadius : weight = 0
otherwise        : t = (d - innerRadius) / (outerRadius - innerRadius)
                   weight = falloff(t)
```

有効な半径は `0 <= innerRadius < outerRadius` です。通常は共通半径を使用し、特定の pose
だけ `pose[].useRadiusOverride = true` にして固有半径へ切り替えます。

| `falloff` | `0 < t < 1` の式 |
|---|---|
| `Linear` | `1 - t` |
| `CompactCubic` | `1 - 3t² + 2t³` |
| `CompactQuintic` | `1 - 10t³ + 15t⁴ - 6t⁵` |

既定値は境界の1階・2階微分が0になる `CompactQuintic` です。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `inputQuat` | `double4` | `(0, 0, 0, 1)` | 現在のdriver orientation |
| `innerRadius` | `doubleAngle` | `0°` | 共通のweight 1範囲 |
| `outerRadius` | `doubleAngle` | `60°` | 共通のweight 0境界 |
| `falloff` | enum | `CompactQuintic` | 1から0への減衰曲線 |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].poseQuat` | `double4` | `(0, 0, 0, 0)` | pose orientation。zeroは未設定 |
| `pose[].enabled` | `bool` | `true` | poseの参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose固有半径を使うか |
| `pose[].innerRadiusOverride` | `doubleAngle` | `0°` | pose固有のweight 1範囲 |
| `pose[].outerRadiusOverride` | `doubleAngle` | `60°` | pose固有のweight 0境界 |
| `outputWeight[]` | `double` multi | - | `pose[]`と同じlogical indexの`[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ`true` |
| `falloffStatus` | enum | - | 失敗理由 |

各weightは独立し、合計1へ正規化しません。同じorientationのposeも許容し、範囲が重なると
weight合計が1を超える場合があります。無効poseには対応する0出力を作ります。

## Falloff Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | 評価成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | 使用する半径が非有限、または`0 <= inner < outer`でない |
| 3 | `InvalidQuaternion` | inputまたは有効pose Quaternionが無効 |
| 4 | `UnsupportedFalloff` | 未対応のenum値 |
| 5 | `NumericalFailure` | 距離またはweight計算が非有限 |

失敗時は全pose logical indexのweightを0にし、`isValid = false`にします。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

weight = nodes.create.bdRbf_OrientationFalloffWeight(
    name="shoulder_orientation_falloff"
)
blend = nodes.create.bdRbf_PoseBlend(name="shoulder_corrective_blend")

weight.pose[0].poseQuat.set((0.0, 0.0, 0.0, 1.0))
weight.pose[1].poseQuat.set((0.382683, 0.0, 0.0, 0.923880))
weight.innerRadius.set(10.0)
weight.outerRadius.set(60.0)

blend.pose[1].translate.set((0.0, 1.5, 0.5))
blend.pose[1].rotate.set((15.0, 0.0, -10.0))

weight.outputWeight.connect(blend.weight)
mod.do_it_dg()
```

## Performance And Animation Policy

評価はpose数を`N`として時間・追加メモリとも `O(N)` です。Eigen、補間行列、QR solve、
mutable cacheは使用せず、`MPxNode::kParallel`で評価します。

radius系attributeはrig構築時の設定値です。変更時のdirtyと再評価は行いますが、毎フレーム
radiusをアニメーションする運用はサポートおよび性能保証の対象外です。
