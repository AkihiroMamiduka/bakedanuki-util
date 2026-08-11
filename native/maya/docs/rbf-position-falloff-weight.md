# RBF Position Falloff Weight

`bdRbf_PositionFalloffWeight` は、現在位置と各 pose 位置の3次元距離から、pose ごとに
独立した falloff weight を計算する dependency node です。

補間行列を解く [`bdRbf_PositionWeight`](rbf-position-weight.md) とは異なり、他の pose の
位置や数によって個々の weight は変化しません。補助骨の「この範囲内では最大、そこから
外側へ滑らかに0まで減衰させる」という用途を、少ない計算量で直接表現します。

出力形式は他の RBF weight node と共通です。
[`bdRbf_PoseBlend`](rbf-pose-blend.md) の `weight[]` へ multi attribute の親同士を1回で
接続できます。

## Distance And Coordinate Space

入力位置 `p` と pose 位置 `c_i` の距離には通常の3次元ユークリッド距離を使います。

```text
d_i = sqrt(
    (p.x - c_i.x)^2
    + (p.y - c_i.y)^2
    + (p.z - c_i.z)^2
)
```

node は行列適用や座標変換を行いません。`inputPosition` と `pose[].position` は、利用者が
同じ座標空間の値で揃えます。補助骨用途では driver transform のローカル `translate` を
そのまま入力し、pose 位置も同じローカル空間で登録する使い方を基本とします。

## Inner And Outer Radius

各 pose は内側半径 `inner` と外側半径 `outer` を持ちます。

```text
d <= inner : weight = 1
d >= outer : weight = 0
otherwise  : t = (d - inner) / (outer - inner)
             weight = falloff(t)
```

有効な半径は `0 <= inner < outer` です。内側半径を0にすると pose 位置だけが厳密に1に
なり、従来の「中心から外側へ減衰する」形になります。内側半径を大きくすると、pose の
近傍に weight 1 の plateau を作れます。

| `falloff` | `0 < t < 1` の式 | 境界の性質 |
|---|---|---|
| `Linear` | `1 - t` | 一定勾配 |
| `CompactCubic` | `1 - 3t² + 2t³` | 両端で1階微分が0 |
| `CompactQuintic` | `1 - 10t³ + 15t⁴ - 6t⁵` | 両端で1階・2階微分が0 |

補助骨用途の既定値は、境界の変化が最も滑らかな `CompactQuintic` です。

## Per-pose Radius Override

通常は全 pose が node 共通の `innerRadius` / `outerRadius` を使います。特定の pose だけ
範囲を変えたい場合は `pose[].useRadiusOverride = true` にし、
`pose[].innerRadiusOverride` / `pose[].outerRadiusOverride` を設定します。

上書きは2つの半径を一組として切り替えます。個々の pose に常に半径を複製しないため、
共通設定の変更は上書きしていない全 pose へそのまま反映されます。無効な pose の上書き値は
評価対象になりません。

## Independent Weights

各 weight は他の pose から独立して計算し、合計1への正規化は行いません。このため、範囲が
重なると複数の weight が同時に1になることがあり、合計が1を超える場合もあります。
同じ位置へ複数の pose を置くことも有効です。

`bdRbf_PoseBlend` は base から各 pose への差分を weight で加算するため、重なりを利用した
複数補正も、そのまま意図的に構成できます。合計1に保つ補間が必要な場合は
`bdRbf_PositionWeight` を使用します。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `inputPosition` | `doubleLinear3` | `(0, 0, 0)` | 現在の driver 位置 |
| `innerRadius` | `doubleLinear` | `0 cm` | 共通の weight 1 範囲 |
| `outerRadius` | `doubleLinear` | `1 cm` | 共通の weight 0 境界 |
| `falloff` | enum | `CompactQuintic` | 1から0への減衰曲線 |
| `pose[]` | compound multi | empty | pose 定義。logical index は出力と対応 |
| `pose[].position` | `doubleLinear3` | `(0, 0, 0)` | falloff の中心位置 |
| `pose[].enabled` | `bool` | `true` | pose の参加切替 |
| `pose[].useRadiusOverride` | `bool` | `false` | pose 固有半径を使うか |
| `pose[].innerRadiusOverride` | `doubleLinear` | `0 cm` | pose 固有の内側半径 |
| `pose[].outerRadiusOverride` | `doubleLinear` | `1 cm` | pose 固有の外側半径 |
| `outputWeight[]` | `double` multi | - | `pose[]` と同じ logical index の `[0, 1]` weight |
| `isValid` | `bool` | - | 評価成功時だけ `true` |
| `falloffStatus` | enum | - | 失敗理由 |

無効化した pose にも対応する `outputWeight[index] = 0` を作ります。位置 `(0, 0, 0)` は
有効な pose です。新しい `pose[]` 要素は `enabled = true` で作られます。

## Falloff Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | 評価成功 |
| 1 | `NoPoses` | 有効 pose がない |
| 2 | `InvalidRadius` | 有効 pose が使用する半径が非有限、または `0 <= inner < outer` でない |
| 3 | `InvalidPosition` | input または有効 pose 位置が非有限 |
| 4 | `UnsupportedFalloff` | 未対応の enum 値 |
| 5 | `NumericalFailure` | 距離または weight の計算結果が非有限 |

失敗時は、存在する全 pose logical index の出力を0にし、`isValid = false` にします。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

driver = nodes.existing("driver_joint")
corrective = nodes.existing("corrective_joint")

weight = nodes.create.bdRbf_PositionFalloffWeight(name="driver_falloff")
blend = nodes.create.bdRbf_PoseBlend(name="corrective_pose_blend")

weight.innerRadius.set(1.0)
weight.outerRadius.set(5.0)
weight.pose[0].position.set((0.0, 0.0, 0.0))
weight.pose[1].position.set((8.0, 0.0, 0.0))
weight.pose[1].useRadiusOverride.set(True)
weight.pose[1].innerRadiusOverride.set(2.0)
weight.pose[1].outerRadiusOverride.set(7.0)

blend.pose[0].translate.set((0.0, 1.0, 0.0))
blend.pose[1].rotate.set((0.0, 0.0, 15.0))

driver.translate.connect(weight.inputPosition)
weight.outputWeight.connect(blend.weight)
blend.outputTranslate.connect(corrective.translate)
blend.outputRotate.connect(corrective.rotate)
blend.outputScale.connect(corrective.scale)

mod.do_it_dg()
```

## Performance And Animation Policy

評価は pose 数を `N` として `O(N)`、追加メモリも `O(N)` です。補間行列、Eigen、QR 分解、
node instance 内の mutable cache は使用せず、`MPxNode::kParallel` で評価します。

radius 系 attribute は rig 構築時に調整する設定値として扱います。値の変更による dirty と
再評価は行いますが、毎フレーム radius をアニメーションする運用は想定せず、サポートおよび
性能保証の対象外です。通常は `inputPosition` だけをアニメーションさせます。
