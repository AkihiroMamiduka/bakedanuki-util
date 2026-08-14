# RBF Position Weight

複数のposition sourceを1組のdriverとして補間する場合は
[`bdRbf_MultiPositionWeight`](rbf-multi-position-weight.md)を使用します。

`bdRbf_PositionWeight` は、現在位置と登録済み pose 位置の3次元距離から、各 pose に
対応する補間 weight を計算する dependency node です。

各 pose の範囲を内側・外側半径で直接指定し、互いに独立した weight を軽量に計算したい
場合は [`bdRbf_PositionFalloffWeight`](rbf-position-falloff-weight.md) を使用します。

出力形式は `bdRbf_OrientationWeight.outputWeight[]` と同じです。回転driver版と同様に、
[`bdRbf_PoseBlend`](rbf-pose-blend.md) の `weight[]` へmulti attributeの親同士を
接続できます。

## Scope

初期版で扱う範囲は次のとおりです。

- driver は1つの3次元位置
- distance は通常のユークリッド距離
- 複数の `pose[]` に対する補間 weight
- Gaussian / Exponential / Linear / CompactCubic / CompactQuintic kernel
- Maya の `doubleLinear` 単位
- sparse logical index と pose ごとの無効化
- 補間不能状態の明示

初期版ではXYZ軸ごとのradiusや軸weightを持ちません。軸ごとの感度が必要になった場合は、
入力とpose位置を同じ規則で前処理してからこのnodeへ渡します。

## Distance And Coordinate Space

入力位置 `p` とpose位置 `c_i` の距離は次です。

```text
d(p, c_i) = sqrt(
    (p.x - c_i.x)^2
    + (p.y - c_i.y)^2
    + (p.z - c_i.z)^2
)
```

nodeは行列適用や座標変換を行いません。`inputPosition` と `pose[].position` は、利用者が
同じ座標空間の値で揃える必要があります。補助骨用途では、driver transformのローカル
`translate`をそのまま入力する使い方を基本とします。

数値として同じ空間ならworld位置や任意の計算済み位置も利用できます。ただし、
ローカル値とworld値を混在させることはできません。

## Kernel And Solve

`x = distance / radius` とし、kernel式と補間solveは
[`bdRbf_OrientationWeight`](rbf-orientation-weight.md) と共通です。

```text
K(i, j) = φ(d(c_i, c_j) / radius)
K(i, i) += regularization
k(i)    = φ(d(input, c_i) / radius)
K * weight = k
```

| `kernel` | `φ(x)` | support |
|---|---|---|
| `Gaussian` | `exp(-(x * x))` | global |
| `Exponential` | `exp(-x)` | global |
| `Linear` | `1 - x` (`x < 1`)、それ以外は`0` | compact |
| `CompactCubic` | `1 - 3x² + 2x³` (`x < 1`)、それ以外は`0` | compact |
| `CompactQuintic` | `1 - 10x³ + 15x⁴ - 6x⁵` (`x < 1`)、それ以外は`0` | compact |

同じ位置の有効poseが複数ある場合は、出力の帰属が曖昧になるため `DuplicatePose` として
失敗させます。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `inputPosition` | `doubleLinear3` | `(0, 0, 0)` | 現在のdriver位置 |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].position` | `doubleLinear3` | `(0, 0, 0)` | pose位置 |
| `pose[].enabled` | `bool` | `true` | solveへの参加切替 |
| `kernel` | enum | `CompactQuintic` | kernel関数 |
| `radius` | `doubleLinear` | `1 cm` | 距離のスケール |
| `regularization` | `double` | `1.0e-8` | 行列の対角へ加える非負値 |
| `allowNegativeWeights` | `bool` | `false` | `false`ならsolve後の負値を0へclamp |
| `outputWeight[]` | `double` multi | - | `pose[]`と同じlogical indexのweight |
| `isValid` | `bool` | - | solve成功時だけ`true` |
| `solveStatus` | enum | - | 失敗理由 |

無効化したposeにも対応する `outputWeight[index] = 0` を作ります。
`allowNegativeWeights = false` は負値を0へclampするだけで、weight合計を1へ再正規化
しません。

位置 `(0, 0, 0)` は有効なposeです。新しい `pose[]` 要素は `enabled = true` のため、
要素を作成した時点で原点poseとしてsolveへ参加します。

## Recommended Corrective-joint Defaults

補助骨correctiveでは次を開始点とします。

- `kernel = CompactQuintic`
- `regularization = 1.0e-8`
- `allowNegativeWeights = false`
- `pose[].enabled = true`

位置の移動量はrigごとに異なるため、`radius`だけはpose間隔に合わせて設定します。
隣接poseが約5 cm離れているなら、まず5〜7.5 cm程度から調整します。pose間に反応しない
領域があれば大きくし、離れたposeまで反応するなら小さくします。

## Solve Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | solve成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | radiusが0以下または非有限 |
| 3 | `InvalidRegularization` | regularizationが負または非有限 |
| 4 | `InvalidPosition` | inputまたは有効pose位置が非有限 |
| 5 | `DuplicatePose` | 同じ位置の有効poseが複数ある |
| 6 | `RankDeficient` | 補間行列がfull rankでない |
| 7 | `NumericalFailure` | 行列、kernel vector、solve結果が非有限 |
| 8 | `UnsupportedKernel` | 未対応のenum値 |

失敗時は、存在する全pose logical indexの出力を0にし、`isValid = false`にします。

## NodeOperator Example

driverのローカルtranslateで補助骨のTRS poseを駆動する例です。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

driver = nodes.existing("driver_joint")
corrective = nodes.existing("corrective_joint")

weight = nodes.create.bdRbf_PositionWeight(name="driver_position_rbf")
blend = nodes.create.bdRbf_PoseBlend(name="corrective_pose_blend")

weight.pose[0].position.set((0.0, 0.0, 0.0))
weight.pose[1].position.set((5.0, 0.0, 0.0))
weight.radius.set(5.0)

blend.pose[0].translate.set((0.0, 0.0, 0.0))
blend.pose[1].translate.set((0.0, 1.0, 0.5))
blend.pose[1].rotate.set((10.0, 0.0, -5.0))
blend.pose[1].scale.set((1.0, 1.05, 1.0))

driver.translate.connect(weight.inputPosition)
weight.outputWeight.connect(blend.weight)
blend.outputTranslate.connect(corrective.translate)
blend.outputRotate.connect(corrective.rotate)
blend.outputScale.connect(corrective.scale)

mod.do_it_dg()
```

このnodeは接続元を調べてlocal / worldを自動判定しません。上の例では
`driver.translate`を接続しているため、登録するpose位置も同じローカル空間の値にします。

## Performance And Cache

pose、kernel、radius、regularizationが変化したときだけ `N x N` 行列とQR分解を
再構築します。通常の評価で `inputPosition`だけが変化するときはfactorizationを再利用し、
kernel vectorとweightだけを計算します。cacheはnode instanceごとに持ち、Parallel評価中も
mutexで設定と入力評価の組み合わせを保護します。

radiusはrig構築時に調整する設定値として扱います。値の変更による再評価は行いますが、
毎フレームradiusをアニメーションする運用は想定せず、サポートおよび性能保証の対象外です。
