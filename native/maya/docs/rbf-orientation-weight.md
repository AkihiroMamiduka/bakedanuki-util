# RBF Orientation Weight

`bdRbf_OrientationWeight` は、現在の Quaternion と登録済み Quaternion pose の角度距離から、
各 pose に対応する補間 weight を計算する dependency node です。

複数のorientationを1組のdriverとして補間する場合は
[`bdRbf_MultiOrientationWeight`](rbf-multi-orientation-weight.md)を使用します。

poseごとのinner / outer半径で独立weightを計算する場合は
[`bdRbf_OrientationFalloffWeight`](rbf-orientation-falloff-weight.md)、BendとTwistを別の半径で評価する場合は
[`bdRbf_BendTwistFalloffWeight`](rbf-bend-twist-falloff-weight.md)を使用します。

「回転入力のRBF補間」と「型付き出力のblend」は別nodeに分離します。このnode自身は
`outputWeight[]`だけを返し、補助骨のtranslate、rotate、scaleは
[`bdRbf_PoseBlend`](rbf-pose-blend.md)でまとめて合成できます。

## Scope

初期版で扱う範囲は次のとおりです。

- driver は1つの Quaternion
- distance は Quaternion の最短角度距離
- 複数の `pose[]` に対する補間 weight
- Gaussian / Exponential / Linear / CompactCubic / CompactQuintic kernel
- sparse logical index と pose ごとの無効化
- 補間不能状態の明示

次は初期版の対象外です。

- translate driver（[`bdRbf_PositionWeight`](rbf-position-weight.md)で対応）
- translate と rotate を同じ距離空間へ混在させる処理
- swing / twist を別々に重み付けする rotation metric
- このweight node内部でのtranslate / rotate / scaleの最終出力blend

## Quaternion Distance

入力と各 pose Quaternion は計算前に正規化します。ゼロ長または非有限値を含む
Quaternion は無効です。

正規化済み Quaternion `q1`, `q2` の距離 `d` は次です。

```text
d(q1, q2) = 2 * acos(clamp(abs(dot(q1, q2)), 0, 1))
```

結果は `0` から `π` radians です。`abs(dot)` を使うため、`q` と `-q` は同じ回転として
扱います。Euler角の成分差を使わないので、rotate orderや360度境界には依存しません。

## Kernel

`x = distance / radius` として、各 kernelを次のように定義します。

| `kernel` | `φ(x)` | support |
|---|---|---|
| `Gaussian` | `exp(-(x * x))` | global |
| `Exponential` | `exp(-x)` | global |
| `Linear` | `1 - x` (`x < 1`)、それ以外は`0` | compact |
| `CompactCubic` | `1 - 3x² + 2x³` (`x < 1`)、それ以外は`0` | compact |
| `CompactQuintic` | `1 - 10x³ + 15x⁴ - 6x⁵` (`x < 1`)、それ以外は`0` | compact |

CompactCubic / CompactQuinticは、`r³` / `r⁵` のpolyharmonic splineではなく、
有限半径で0になるsmooth falloffです。enum value `3` / `4`は従来のCubic / Quinticと
同じで、表示名だけがcompact supportを明示します。

`radius` は `doubleAngle` です。UIでは現在の Maya angle unitで編集でき、内部では
radiansへ変換します。小さい radius は局所的、大きい radius は広い範囲の pose を
相互に影響させます。

## Interpolative Solve

有効な pose centerを `c_i` として、補間行列 `K` と現在入力の kernel vector `k` を
作ります。

```text
K(i, j) = φ(d(c_i, c_j) / radius)
K(i, i) += regularization
k(i)    = φ(d(input, c_i) / radius)
K * weight = k
```

実装は Eigen の column-pivoting Householder QR で連立一次方程式を解きます。逆行列は
作りません。`regularization = 0` では、行列が正則なら各 pose centerで対応weightが1、
他が0になります。正のregularizationは特異に近い行列を安定化できますが、pose
centerでの完全一致をわずかに緩めます。

同じ回転を表す有効poseが複数ある場合は、出力の帰属が曖昧になるため
`DuplicatePose` として失敗させます。regularizationを設定しても、この曖昧性は
許可しません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `inputQuat` | `double4` | `(0, 0, 0, 1)` | 現在のdriver orientation |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].poseQuat` | `double4` | `(0, 0, 0, 0)` | pose orientation。ゼロ値は未設定を表す無効値 |
| `pose[].enabled` | `bool` | `true` | solveへの参加切替 |
| `kernel` | enum | `CompactQuintic` | kernel関数 |
| `radius` | `doubleAngle` | `60 degrees` | 距離のスケール |
| `regularization` | `double` | `1.0e-8` | 行列の対角へ加える非負値 |
| `allowNegativeWeights` | `bool` | `false` | `false`ならsolve後の負値を0へclamp |
| `outputWeight[]` | `double` multi | - | `pose[]`と同じlogical indexのweight |
| `isValid` | `bool` | - | solve成功時だけ`true` |
| `solveStatus` | enum | - | 失敗理由 |

無効化したposeにも対応する `outputWeight[index] = 0` を作ります。
`allowNegativeWeights = false` は負値を0へclampするだけで、weight合計を1へ再正規化
しません。

pose Quaternionの既定値は、driverの`inputQuat`とは異なりゼロQuaternionです。
未設定要素をidentity poseとして誤ってsolveへ参加させず、identity `(0, 0, 0, 1)`を
明示設定したときにMaya ASCIIへ値とlogical indexが保存されるようにするためです。

## Recommended Corrective-joint Defaults

補助骨correctiveでは、局所的で境界が滑らかなCompactQuinticを初期値とします。

- `kernel = CompactQuintic`
- `radius = 60 degrees`
- `regularization = 1.0e-8`
- `allowNegativeWeights = false`

poseが約45度間隔ならradiusは45〜60度、0度と90度のように疎なら90度前後を開始点に
します。pose間に反応しない領域があればradiusを大きくし、離れたposeまで反応するなら
小さくします。

## Solve Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | solve成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | radiusが0以下または非有限 |
| 3 | `InvalidRegularization` | regularizationが負または非有限 |
| 4 | `InvalidQuaternion` | inputまたは有効pose Quaternionが無効 |
| 5 | `DuplicatePose` | 同じ回転の有効poseが複数ある |
| 6 | `RankDeficient` | 補間行列がfull rankでない |
| 7 | `NumericalFailure` | 行列、kernel vector、solve結果が非有限 |
| 8 | `UnsupportedKernel` | 未対応のenum値 |

失敗時は、存在する全pose logical indexの出力を0にし、`isValid = false`にします。

## NodeOperator Example

weight solveと補助骨TRSのblendを分離する例です。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

weight = nodes.create.bdRbf_OrientationWeight(name="shoulder_rbf_weight")
blend = nodes.create.bdRbf_PoseBlend(name="shoulder_rbf_blend")

weight.pose[0].poseQuat.set((0.0, 0.0, 0.0, 1.0))
weight.pose[1].poseQuat.set((0.382683, 0.0, 0.0, 0.923880))

blend.pose[0].translate.set((0.0, 0.0, 0.0))
blend.pose[0].rotate.set((0.0, 0.0, 0.0))
blend.pose[0].scale.set((1.0, 1.0, 1.0))
blend.pose[1].translate.set((0.0, 1.5, 0.5))
blend.pose[1].rotate.set((15.0, 0.0, -10.0))
blend.pose[1].scale.set((1.0, 1.1, 0.95))

weight.outputWeight.connect(blend.weight)

mod.do_it_dg()
```

実際のdriver Quaternionは、Eulerからの変換nodeや既存Quaternion networkから
`inputQuat`へ接続します。`outputWeight[]`と`weight[]`はmulti attributeの親同士を1回
接続するだけで、sparse logical indexも対応します。回転blendの詳細は
[`RBF Pose Blend`](rbf-pose-blend.md)を参照してください。

## Translate And Rotate Boundary

translate distanceは長さ、Quaternion distanceは角度なので、そのまま同じ数値空間へ
足すことはできません。両方を1 nodeで扱うには、軸ごとのtranslate scale、角度scale、
単位変換、どちらを重視するかというmetric設計が必要です。

そのためこのnodeはrotation driver専用です。translate driverには、Euclidean distanceを
使う別node [`bdRbf_PositionWeight`](rbf-position-weight.md) を使用します。どちらのweight
nodeも、型付き出力blenderとは分離します。

## Performance And Eigen

Eigen 5.0.1を `native/third_party/eigen-5.0.1` に固定して同梱します。header-onlyで
コンパイルされるため、Maya実行環境へ追加DLLやPython packageをインストールする
必要はありません。RBFの公開math headerにはEigen型を露出させません。

pose、kernel、radius、regularizationが変化したときに `N x N` 行列を作り、概ね
`O(N³)` のfactorizationを行います。`inputQuat`だけが変化する通常評価ではfactorizationを
再利用し、kernel vector構築とQR solveを行います。

cacheはnode instanceごとに持ち、設定値そのものを比較します。mutex内で設定の再構築から
input評価までを完結させるため、background evaluation contextが異なる設定を同時に要求
しても、別contextのfactorizationと入力を組み合わせません。異なる設定が交互に評価される
場合は正しさを優先して再構築します。
