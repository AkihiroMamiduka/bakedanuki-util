# RBF Pose Blend

`bdRbf_PoseBlend`は、RBF weight nodeの`outputWeight[]`と同じlogical indexに登録した
poseのtranslate、rotate、scaleをブレンドするdependency nodeです。

RBF solveと出力値の合成は別nodeに保ちます。これにより、同じweight solverから複数の
補助骨を駆動したり、weightを別用途へ分岐したりできます。

## Weight Connection

`weight[]`は`bdRbf_OrientationWeight.outputWeight[]`、
`bdRbf_MultiOrientationWeight.outputWeight[]`、orientation falloff系、
`bdRbf_BendTwistFalloffWeight.outputWeight[]`、position weight / falloff系の単一・複数source版を
multi attributeの親同士で接続できます。

```python
weight.outputWeight.connect(blend.weight)
```

接続は1回だけです。sourceとdestinationのlogical indexは自動的に対応します。

```text
outputWeight[2] -> weight[2] -> pose[2]
outputWeight[8] -> weight[8] -> pose[8]
```

接続後にsource側へ新しいlogical indexが追加された場合も、親接続を作り直す必要は
ありません。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `baseTranslate` | `doubleLinear3` | `(0, 0, 0)` | 全weightが0のときのtranslate |
| `baseRotate` | `doubleAngle3` | `(0, 0, 0)` | 全weightが0のときのrotate |
| `baseScale` | `double3` | `(1, 1, 1)` | 全weightが0のときのscale |
| `rotateOrder` | enum | `xyz` | base、pose、outputで共有するEuler rotate order |
| `pose[]` | compound multi | empty | logical indexごとの目標TRS |
| `pose[].translate` | `doubleLinear3` | `(0, 0, 0)` | poseの目標translate |
| `pose[].rotate` | `doubleAngle3` | `(0, 0, 0)` | poseの目標rotate |
| `pose[].scale` | `double3` | `(1, 1, 1)` | poseの目標scale |
| `pose[].enabled` | `bool` | `true` | pose valueの参加切替 |
| `weight[]` | `double` multi | empty | poseと同じlogical indexのweight |
| `outputTranslate` | `doubleLinear3` | - | blend後のtranslate |
| `outputRotate` | `doubleAngle3` | - | `rotateOrder`で表現したblend後のrotate |
| `outputQuat` | `double4` | - | blend後の単位Quaternion |
| `outputScale` | `double3` | - | blend後のscale |
| `isValid` | `bool` | - | blend成功時だけ`true` |
| `blendStatus` | enum | - | 失敗理由 |

`pose[i]`と`weight[i]`の両方が存在し、poseがenabledで、weightがexact zeroではない場合だけ
計算へ参加します。片方だけ存在するlogical indexは無視します。したがって、1つの
RBF weight nodeから複数のblend nodeを駆動し、各blend nodeへ必要なposeだけ
登録できます。

poseのTRSはbaseからのoffsetではなく、そのposeにおける絶対的なchannel目標値です。
baseが既定値以外の場合は、各poseのtranslate、rotate、scaleをすべて記録してください。
未編集childの既定値も、そのposeの目標値として計算されます。

## Translate And Scale Blend

translateとscaleはbaseから各poseへの差分を加重和します。

```text
outputTranslate = baseTranslate
    + sum(weight[i] * (pose[i].translate - baseTranslate))

outputScale = baseScale
    + sum(weight[i] * (pose[i].scale - baseScale))
```

全weightが0ならbase値を返し、1つのposeのweightが1ならそのpose値を返します。
weight合計による再正規化は行いません。weight `0.5`を補正量50%として維持するためです。
負のweightはbaseからposeと反対方向への外挿として、そのまま計算します。

scaleはlog scaleではなく、baseからの線形差分です。zeroまたは負のscaleも有限値なら
そのまま計算します。

## Quaternion Rotation Blend

Euler成分は直接加重和しません。`baseRotate`と各`pose[].rotate`を`rotateOrder`で
Quaternionへ変換し、baseからの相対回転をlog/expで合成します。

```text
relative[i] = inverse(baseQuat) * poseQuat[i]
rotationVector[i] = Log(shortest(relative[i]))

blendedRelative = Exp(sum(weight[i] * rotationVector[i]))
outputQuat = baseQuat * blendedRelative
```

各relative Quaternionは正規化し、`q`と`-q`のうち回転角が180度以下になる側を選びます。
ちょうど180度ではXYZ成分の辞書順で符号を固定し、同じorientationから同じ結果を得ます。

`outputRotate`は`outputQuat`と同じorientationを`rotateOrder`でEuler化した値です。
Euler表現のturn数や入力channel値そのものの連続性は保証しません。Quaternionのまま後段へ
渡せる場合は`outputQuat`を使用できます。

## Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | blend成功。空入力もbaseを返す成功状態 |
| 1 | `InvalidWeight` | 参加するweightが非有限 |
| 2 | `InvalidTranslate` | baseまたは参加poseのtranslateが非有限 |
| 3 | `InvalidRotate` | baseまたは参加poseのrotateから有効なQuaternionを作れない |
| 4 | `InvalidScale` | baseまたは参加poseのscaleが非有限 |
| 5 | `UnsupportedRotateOrder` | rotate order enumが未対応 |
| 6 | `NumericalFailure` | 加重和またはQuaternion合成結果が非有限 |

失敗時は可能な限りbase TRSを返し、`isValid = false`にします。RBF solve自体が失敗した
場合、どちらのweight nodeもweightを0にするため、blend nodeはbase TRSへ安全に
戻ります。

## NodeOperator Example

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

blend.outputTranslate.connect("shoulder_corrective.translate")
blend.outputRotate.connect("shoulder_corrective.rotate")
blend.outputScale.connect("shoulder_corrective.scale")

mod.do_it_dg()
```

補助骨の`rotateOrder`とblend nodeの`rotateOrder`は同じ値にします。jointOrient、rotateAxis、
pivot、shearはこのnodeでは変更しません。出力は接続先transformのローカルTRS channel値です。

## Evaluation

nodeは共有mutable stateを持たず、`MPxNode::kParallel`で評価します。poseはlogical index順に
処理するため、physical storage orderやelement作成順によって浮動小数点の加算順が
変化しません。
