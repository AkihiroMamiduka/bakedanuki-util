# RBF Multi Orientation Weight

`bdRbf_MultiOrientationWeight`は、複数のQuaternion orientationを1組のdriverとして扱い、
登録済みposeとの一致度から補間weightを計算するdependency nodeです。

例えば肩・肘・手首のorientationの組み合わせを1つのpose centerとして登録できます。
複数の独立したRBF出力を後から乗算する処理とは異なり、orientationの組み合わせ自体を
1つの補間空間としてsolveします。

単一driverには、より簡潔な
[`bdRbf_OrientationWeight`](rbf-orientation-weight.md)を使用します。

## Source And Pose Layout

`source[]`のlogical indexがdriverの次元を定義します。各有効poseの
`pose[].sourceQuat[]`には、同じlogical indexをすべて登録します。

```text
source[2].inputQuat
source[8].inputQuat

pose[3].sourceQuat[2]
pose[3].sourceQuat[8]

pose[9].sourceQuat[2]
pose[9].sourceQuat[8]
```

有効poseでsource indexが不足または一致しない場合は、identityで補完せず
`IncompletePose`として失敗します。無効poseは検証とsolveから除外し、対応する出力を
0にします。

## Multi-Source Distance

source `j`のQuaternion最短角度距離を`d_j`、非負の影響度を`a_j`として、加重RMS距離を
使用します。

```text
d_j = 2 * acos(clamp(abs(dot(input_j, pose_j)), 0, 1))

D = sqrt(sum(a_j * d_j^2) / sum(a_j))
```

`D`はradiansです。source数で正規化するため、すべてのsourceが同じ角度だけずれた場合、
source数を増やしても`radius`の意味は変わりません。sourceが1つなら
`bdRbf_OrientationWeight`と同じ距離になります。

`influence = 0`のsourceは距離とQuaternion検証から除外します。ただしpose配列のindex対応は
維持する必要があります。全sourceのinfluenceが0の場合は`InvalidInfluence`です。

## Kernel And Solve

補間行列とkernelは`bdRbf_OrientationWeight`と同じです。

```text
K(i, j) = phi(D(pose_i, pose_j) / radius)
K(i, i) += regularization
k(i)    = phi(D(input, pose_i) / radius)
K * weight = k
```

kernelは`Gaussian`、`Exponential`、`Linear`、`CompactCubic`、
`CompactQuintic`から選択します。既定値は`CompactQuintic`です。

全sourceの組み合わせが同じ有効poseが複数ある場合は`DuplicatePose`です。1つのsourceだけが
一致していても、他のsourceが異なれば別poseとして扱います。

## Attributes

| attribute | type | default | meaning |
|---|---|---:|---|
| `source[]` | compound multi | empty | orientation source定義 |
| `source[].inputQuat` | `double4` | `(0, 0, 0, 1)` | 現在のsource orientation |
| `source[].influence` | `double` | `1` | 加重RMS距離への非負の影響度 |
| `pose[]` | compound multi | empty | pose定義。logical indexは出力と対応 |
| `pose[].sourceQuat[]` | `double4` multi | `(0, 0, 0, 0)` | source indexごとのpose orientation |
| `pose[].enabled` | `bool` | `true` | solveへの参加切替 |
| `kernel` | enum | `CompactQuintic` | RBF kernel |
| `radius` | `doubleAngle` | `60 degrees` | 加重RMS角度距離のスケール |
| `regularization` | `double` | `1.0e-8` | 補間行列の対角へ加える非負値 |
| `allowNegativeWeights` | `bool` | `false` | `false`ならsolve後の負値を0へclamp |
| `outputWeight[]` | `double` multi | - | `pose[]`と同じlogical indexのweight |
| `isValid` | `bool` | - | solve成功時だけ`true` |
| `solveStatus` | enum | - | 失敗理由 |

## Solve Status

| value | name | condition |
|---:|---|---|
| 0 | `Success` | solve成功 |
| 1 | `NoPoses` | 有効poseがない |
| 2 | `InvalidRadius` | radiusが0以下または非有限 |
| 3 | `InvalidRegularization` | regularizationが負または非有限 |
| 4 | `InvalidQuaternion` | 有効sourceのinputまたはpose Quaternionが無効 |
| 5 | `DuplicatePose` | 全有効sourceのorientationが同じposeが複数ある |
| 6 | `RankDeficient` | 補間行列がfull rankでない |
| 7 | `NumericalFailure` | 行列、kernel vector、solve結果が非有限 |
| 8 | `UnsupportedKernel` | 未対応のkernel enum |
| 10 | `NoSources` | sourceがない |
| 11 | `InvalidInfluence` | influenceが負・非有限、または合計0 |
| 12 | `IncompletePose` | 有効poseのsource index構成が一致しない |

失敗時は存在する全pose logical indexの出力を0にします。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

weight = nodes.create.bdRbf_MultiOrientationWeight(
    name="arm_multi_orientation_weight"
)
blend = nodes.create.bdRbf_PoseBlend(name="arm_corrective_blend")

shoulder_index = 2
elbow_index = 8
pose_index = 3

weight.source[shoulder_index].inputQuat.set((0.0, 0.0, 0.0, 1.0))
weight.source[elbow_index].inputQuat.set((0.0, 0.0, 0.0, 1.0))
weight.source[elbow_index].influence.set(2.0)

weight.pose[pose_index].sourceQuat[shoulder_index].set(
    (0.0, 0.258819, 0.0, 0.965926)
)
weight.pose[pose_index].sourceQuat[elbow_index].set(
    (0.382683, 0.0, 0.0, 0.923880)
)

blend.pose[pose_index].translate.set((0.0, 1.5, 0.5))
blend.pose[pose_index].rotate.set((15.0, 0.0, -10.0))

weight.outputWeight.connect(blend.weight)
mod.do_it_dg()
```

## Performance And Cache

pose数を`N`、source数を`S`とすると、設定変更時の距離行列構築は`O(N^2 S)`、
factorizationは概ね`O(N^3)`です。通常のsource input評価ではfactorizationを再利用し、
`O(NS)`のkernel vector構築とQR solveを行います。

pose、source index、influence、kernel、radius、regularizationを変更するとcacheを再構築します。
node instanceごとのmutexでcacheを保護し、`MPxNode::kParallel`で評価します。
