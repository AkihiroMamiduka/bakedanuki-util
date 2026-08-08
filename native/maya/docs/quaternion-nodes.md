# Quaternion Nodes

3軸orientationの合成は、各軸を独立した`doubleAngle3`として計算せずQuaternionで扱います。
Maya標準の`quatProd`、`quatSlerp`、`quatNormalize`、`eulerToQuat`、`quatToEuler`などを
基本とし、標準nodeにない可変長積だけを`bdUtilNodes`で補います。

## Implemented Scope

| node type | 役割 | 状態 |
| --- | --- | --- |
| `bdQuat_MultiplyMulti` | 任意個のQuaternionを順序付きで乗算 | 実装済み |
| `bdQuat_DecomposeBendTwist` | Quaternionを捻り・横曲げ・縦曲げへ分解 | 実装済み |
| `bdQuat_ComposeBendTwist` | 捻り・横曲げ・縦曲げをQuaternionへ合成 | 実装済み |
| `bdQuat_DecomposeTwist` | Quaternionからtwist角度だけを抽出 | 実装済み |
| `bdEuler_DecomposeTwist` | Euler rotationからtwist角度だけを抽出 | 実装済み |

固定2入力版はMaya標準の`quatProd`を使用します。独自の`bdQuat_Multiply`は作りません。
補間、正規化、共役、逆元、Euler変換についても、用途上の不足が確認されるまでは
標準nodeを利用します。

曲げ・捻り分解は3軸を独立したEuler角として扱う処理ではありません。Quaternionを
swing–twist分解し、swingを2次元の回転ベクトルとして表します。この用途はMaya標準
Quaternion nodeだけでは直接構成できないため、相互に対応する分解・合成nodeを提供します。
twistだけが必要な場合は、bend成分を算出しない`bdQuat_DecomposeTwist`を使用できます。
transformの`rotate`からtwistだけが必要な場合は、Euler→Quaternion変換を内包した
`bdEuler_DecomposeTwist`を使用できます。

node typeにはプロジェクト共通の演算名`Multiply`を使用します。Maya標準名の`Prod`は
数学的には正確ですが、`bdDbl_MultiplyMulti`や`bdDbl3_MultiplyMulti`と同じ規則で
検索・予測できることを優先しました。`Mult`は`Multi`と見分けにくいため使用しません。

## Attributes

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputQuat[]` | `iq` | double4 compound multi | `(0, 0, 0, 1)` | Quaternion入力 |
| `inputQuatX/Y/Z/W` | `iqx/iqy/iqz/iqw` | double | `0/0/0/1` | 入力成分 |
| `outputQuat` | `oq` | double4 compound | `(0, 0, 0, 1)` | 乗算結果 |
| `outputQuatX/Y/Z/W` | `oqx/oqy/oqz/oqw` | double | `0/0/0/1` | 出力成分 |

親attribute名に`Quat`を含め、Maya標準Quaternion nodeと直接接続できるdouble4 compoundに
します。NodeOperatorもこの構造をQuaternionとして認識し、値取得時は`bdu.Quat`を返します。

## Multiplication Order

既存elementをlogical indexの昇順に並べ、左から乗算します。

```text
outputQuat = ((inputQuat[index0] * inputQuat[index1])
    * inputQuat[index2]) ...

index0 < index1 < index2 < ...
```

Quaternion積は可換ではないため、physical storage orderやelementの作成順は演算順に
使用しません。例えば`inputQuat[20]`、`inputQuat[2]`、`inputQuat[9]`の順に作成しても、
結果は`inputQuat[2] * inputQuat[9] * inputQuat[20]`です。この積の向きはMaya標準の
`quatProd`を同じ順序で連結した結果、および`MQuaternion::operator*`と一致します。

空入力の結果は乗法単位元`(0, 0, 0, 1)`です。1要素の場合は、その値を変更せず返します。

## Raw-value Policy

このnodeは合成だけを担当し、次の処理は行いません。

- 単位Quaternionへの自動正規化
- `q`と`-q`の符号統一
- zero Quaternionの置換
- `NaN` / 無限値のclamp、warning、validation

非正規化値を含む積も`MQuaternion`の浮動小数点演算結果をそのまま返します。正規化が
必要な用途では、意図が明示されるようMaya標準の`quatNormalize`を後段へ接続します。

## NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

product = nodes.create.bdQuat_MultiplyMulti(name="product")
to_euler = nodes.create.quatToEuler(name="to_euler")

product.inputQuat[next].set((0.0, 0.0, 0.0, 1.0))
product.outputQuat > to_euler.inputQuat
mod.do_it_dg()
```

`inputQuat[next]`は次に利用可能なlogical indexを選びます。演算順をscene上で明示的に
固定したい場合は、`inputQuat[0]`、`inputQuat[10]`のようにindexを直接指定できます。

## Evaluation And Persistence

`bdQuat_MultiplyMulti`は共有mutable stateを持たない純粋なDG計算nodeで、
`MPxNode::kParallel`として評価します。入力親・各XYZW childから出力compoundへのdirty
依存を登録し、出力親と各childの直接要求に対応します。

node type、attribute名、logical index昇順の積、空入力のidentity、自動正規化をしない方針は
sceneの結果を左右する永続APIとして扱います。

## Bend / Twist Convention

`bdQuat_DecomposeBendTwist`と`bdQuat_ComposeBendTwist`は、意味上の基準座標で次の軸を
使用します。

- X軸: twist
- Y軸: horizontal bendを生む回転軸
- Z軸: vertical bendを生む回転軸

`outputBendH = H`、`outputBendV = V`とすると、bendの総角度と回転軸は次の通りです。

```text
bendAngle = hypot(H, V)
bendAxis  = (0, H / bendAngle, V / bendAngle)
```

したがって`hypot(H, V)`が実際の総曲げ角度です。HとVを同じ比率で縮小すると、bendを
identityへ向かって球面上で同じ比率に縮小できます。H / VはEuler角ではなく、bend平面の
回転ベクトル成分です。

`order`はQuaternionの積順を明示します。

| enum | value | 合成式 | default |
| --- | ---: | --- | --- |
| `TwistBend` | 0 | `Q = Q_twist * Q_bend` | Yes |
| `BendTwist` | 1 | `Q = Q_bend * Q_twist` | No |

積はMayaの`MQuaternion::operator*`および`quatProd`と同じ規約です。2つのnodeで同じ
`order`を使用すると、正規範囲内では成分を往復できます。

## Bend / Twist Attributes

### `bdQuat_DecomposeBendTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputQuat` | `iq` | double4 compound | `(0, 0, 0, 1)` | 分解対象 |
| `axisQuat` | `aq` | double4 compound | `(0, 0, 0, 1)` | 意味上のXYZ基準への変換 |
| `order` | `ord` | enum | `TwistBend` | factorの積順 |
| `output` | `o` | compound | `(0°, 0°, 0°)` | 3成分の親出力 |
| `outputTwist` | `otw` | doubleAngle | `0°` | X軸twist |
| `outputBendH` | `obh` | doubleAngle | `0°` | bend回転ベクトルのY成分 |
| `outputBendV` | `obv` | doubleAngle | `0°` | bend回転ベクトルのZ成分 |
| `bendRatio` | `br` | double | `0.0` | 総bend角度を0～180°で正規化した値 |

### `bdQuat_DecomposeTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputQuat` | `iq` | double4 compound | `(0, 0, 0, 1)` | 分解対象 |
| `axisQuat` | `aq` | double4 compound | `(0, 0, 0, 1)` | 意味上のXYZ基準への変換 |
| `outputTwist` | `otw` | doubleAngle | `0°` | canonical X軸まわりのtwist角度 |

twist射影は`TwistBend`と`BendTwist`で共通なので、このnodeは`order`を持ちません。
`bdQuat_DecomposeBendTwist.outputTwist`と同じ正規化済み角度を返します。

### `bdEuler_DecomposeTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputRotate` | `ir` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 分解対象のEuler rotation |
| `inputRotateX/Y/Z` | `irx/iry/irz` | doubleAngle | `0°` | 入力回転成分 |
| `inputRotateOrder` | `iro` | enum | `xyz` | `inputRotate`の回転順序 |
| `axisRotate` | `ar` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 意味上のXYZ基準への変換をEulerで指定 |
| `axisRotateX/Y/Z` | `arx/ary/arz` | doubleAngle | `0°` | 軸基準回転成分 |
| `axisRotateOrder` | `aro` | enum | `xyz` | `axisRotate`の回転順序 |
| `outputTwist` | `otw` | doubleAngle | `0°` | canonical X軸まわりのtwist角度 |

両rotate orderはMayaのtransformと同じ`xyz / yzx / zxy / xzy / yxz / zyx`を使用します。
node内で2つのEuler rotationをQuaternionへ変換し、`bdQuat_DecomposeTwist`と同じ処理へ
渡します。

```text
Qinput = quaternion(inputRotate, inputRotateOrder)
A      = quaternion(axisRotate, axisRotateOrder)
outputTwist = decomposeTwist(Qinput, A)
```

`axisRotate`は`axisQuat = A`をEuler表現したものです。実際の意味座標`F`をそのままEuler化
する入力ではなく、Quaternion版と同様に`A = inverse(F)`を指定します。Euler変換を内包する
だけなので、出力範囲、特異点、無効入力fallbackはQuaternion版と一致します。

transformからは変換nodeを挟まず、次の4本を直接接続できます。

```text
source.rotate      -> bdEuler_DecomposeTwist.inputRotate
source.rotateOrder -> bdEuler_DecomposeTwist.inputRotateOrder
axis.rotate        -> bdEuler_DecomposeTwist.axisRotate
axis.rotateOrder   -> bdEuler_DecomposeTwist.axisRotateOrder
```

出力はtwist角度だけです。QuaternionとEuler orientationは回転数の履歴を持たないため、
例えばX回転`450°`は`90°`として分解され、`outputTwist`は`[-180°, 180°)`へ正規化されます。

### `bdQuat_ComposeBendTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | compound | `(0°, 0°, 0°)` | 3成分の親入力 |
| `inputTwist` | `itw` | doubleAngle | `0°` | X軸twist |
| `inputBendH` | `ibh` | doubleAngle | `0°` | bend回転ベクトルのY成分 |
| `inputBendV` | `ibv` | doubleAngle | `0°` | bend回転ベクトルのZ成分 |
| `axisQuat` | `aq` | double4 compound | `(0, 0, 0, 1)` | 意味上のXYZ基準への変換 |
| `order` | `ord` | enum | `TwistBend` | factorの積順 |
| `outputQuat` | `oq` | double4 compound | `(0, 0, 0, 1)` | 合成結果 |

`output`のchild順と`input`のchild順は、どちらもtwist、horizontal、verticalです。このため
親compoundを直接接続できます。Quaternion compoundもMaya標準nodeと直接接続できます。

分解nodeは角度成分だけを返し、Twist / Bend factor Quaternionは出力しません。factorが
必要な場合は`bdQuat_ComposeBendTwist`で必要な成分だけを再構成します。

- Twistのみ: `inputBendH = inputBendV = 0°`
- Bendのみ: `inputTwist = 0°`
- 入力側の意味座標で得る: 分解nodeと同じ`axisQuat`を設定
- canonical座標で得る: `axisQuat`をidentityにする

片方のfactorがidentityになるため、Twistのみ・Bendのみの再構成結果は`order`に依存しません。

## Axis Orientation

`axisQuat = A`は、入力orientationそのものを追加回転する値ではなく、分解に使う
意味上の座標基準です。identityでは上記のcanonical XYZをそのまま使います。

```text
decompose: Qcanonical = A * Qinput * inverse(A)
compose:   Qoutput    = inverse(A) * Qcanonical * A
```

実際の意味座標を表すQuaternionをFとし、FのX / Y / Zが入力空間におけるtwist / H / V軸を
向く場合は、`A = inverse(F)`を設定します。分解と合成のAは一致させてください。

## Bend Ratio

`bendRatio`はcanonical +Xのtwist基準方向が、回転後に反対方向へ向くまでの総bend角度を
線形に正規化した値です。

```text
bendAngle = hypot(outputBendH, outputBendV)
bendRatio = bendAngle / 180°
```

| twist軸の方向 | bend角度 | `bendRatio` |
| --- | ---: | ---: |
| 基準方向 | 0° | `0.0` |
| 基準軸と直交 | 90° | `0.5` |
| 基準方向の反対 | 180° | `1.0` |

範囲は`[0, 1]`で、Quaternionのfactor order、`q` / `-q`の符号差には依存しません。
180°特異点へ近づく度合いとして、`MapRange`や`remapValue`で任意のdriver curveへ変換できます。

## Canonicalization And Singularity

Quaternionは回転数の履歴を持たず、`q`と`-q`が同じorientationを表します。分解結果は
orientationだけから一意に扱える正規表現へ統一します。

- `outputTwist`は`[-180°, 180°)`。
- bendの総角度`hypot(horizontal, vertical)`は`[0°, 180°]`。
- `q`、`-q`、非zero scalar倍したQuaternionは同じ意味成分を返す。
- 複数回転したtwistのturn数は復元しない。

総bendが180°でtwist射影がzeroになる姿勢では、twistとbendの分け方が数学的に一意では
ありません。この場合は`twist = 0°`とし、orientation全体をcanonical bendとして返します。
このとき`bendRatio = 1.0`です。特異点近傍ではTwist / Bend成分が本質的に不安定になり得る
ため、必要に応じて`bendRatio`をremapし、別driverへ連続的にブレンドします。

両nodeは有限かつ十分な長さを持つQuaternionを内部で単位化します。zeroに近いQuaternion、
`NaN`、無限値、無効な`axisQuat`では安全なfallbackを返します。

- Decompose: 全角度`0°`、`bendRatio = 0.0`
- Compose: identity Quaternion

Composeの角度入力は連続値として受け取り、三角関数の周期でorientationへ写像します。正規範囲
外の値をComposeして再度Decomposeすると、上記canonical rangeへ正規化されます。

## Bend / Twist NodeOperator Example

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

compose = nodes.create.bdQuat_ComposeBendTwist(name="compose_bend_twist")
decompose = nodes.create.bdQuat_DecomposeBendTwist(name="decompose_bend_twist")
decompose_twist = nodes.create.bdQuat_DecomposeTwist(name="decompose_twist")
recompose = nodes.create.bdQuat_ComposeBendTwist(name="recompose_bend_twist")

compose.input.set((30.0, 45.0, -20.0))
compose.outputQuat > decompose.inputQuat
compose.outputQuat > decompose_twist.inputQuat
decompose.output > recompose.input
mod.do_it_dg()
```

角度値のNodeOperator APIは、ほかの`doubleAngle` attributeと同じくdegree単位で扱います。
内部のC++計算はMayaのinternal angle unitであるradianです。

## Autodesk Reference

- [MQuaternion C++ API Reference](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_quaternion.html)
