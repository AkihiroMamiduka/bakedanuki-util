# Quaternion Nodes

3軸orientationの合成は、各軸を独立した`doubleAngle3`として計算せずQuaternionで扱います。
Maya標準の`quatProd`、`quatSlerp`、`quatNormalize`、`eulerToQuat`、`quatToEuler`などを
基本とし、標準nodeにない可変長積だけを`bdUtilNodes`で補います。

## Implemented Scope

| node type | 役割 | 状態 |
| --- | --- | --- |
| `bdQuat_MultiplyMulti` | 任意個のQuaternionを順序付きで乗算 | 実装済み |
| `bdQuat_ChangeBasis` | Quaternionの回転軸を別の基準へ変換 | 実装済み |
| `bdQuat_DecomposeBendTwist` | Quaternionを捻り・横曲げ・縦曲げへ分解 | 実装済み |
| `bdQuat_ComposeBendTwist` | 捻り・横曲げ・縦曲げをQuaternionへ合成 | 実装済み |
| `bdQuat_DecomposeTwist` | Quaternionからtwist角度だけを抽出 | 実装済み |
| `bdEuler_DecomposeTwist` | Euler rotationからtwist角度だけを抽出 | 実装済み |
| `bdEuler_DecomposeBendTwist` | Euler rotationを捻り・横曲げ・縦曲げへ分解 | 実装済み |
| `bdEuler_ComposeBendTwist` | 捻り・横曲げ・縦曲げをEuler rotationへ合成 | 実装済み |
| `bdQuat_LimitBendTwist` | 分解した回転成分をBoxまたは楕円で制限しQuaternionへ再合成 | 実装済み |
| `bdEuler_LimitBendTwist` | Euler rotationを回転成分ごとに制限してEulerへ再合成 | 実装済み |
| `bdEuler_Value` | Euler rotationとrotate orderを保存・中継 | 実装済み |
| `bdQuat_Value` | Quaternionの生値を保存・中継 | 実装済み |

固定2入力版はMaya標準の`quatProd`を使用します。独自の`bdQuat_Multiply`は作りません。
補間、正規化、共役、逆元、Euler変換についても、用途上の不足が確認されるまでは
標準nodeを利用します。

曲げ・捻り分解は3軸を独立したEuler角として扱う処理ではありません。Quaternionを
swing–twist分解し、swingを2次元の回転ベクトルとして表します。この用途はMaya標準
Quaternion nodeだけでは直接構成できないため、相互に対応する分解・合成nodeを提供します。
twistだけが必要な場合は、bend成分を算出しない`bdQuat_DecomposeTwist`を使用できます。
transformの`rotate`からtwistだけが必要な場合は、Euler→Quaternion変換を内包した
`bdEuler_DecomposeTwist`を使用できます。
分解・合成の前後をtransformの`rotate`へ直接つなぐ場合は、同じ変換を内包した
`bdEuler_DecomposeBendTwist`と`bdEuler_ComposeBendTwist`を使用できます。

node typeにはプロジェクト共通の演算名`Multiply`を使用します。Maya標準名の`Prod`は
数学的には正確ですが、`bdDbl_MultiplyMulti`や`bdDbl3_MultiplyMulti`と同じ規則で
検索・予測できることを優先しました。`Mult`は`Multi`と見分けにくいため使用しません。

## Stored Rotation Values

`bdEuler_Value`と`bdQuat_Value`は計算nodeではなく、rotation値をsceneに保存しながら
接続元・接続先の両方として使える中継nodeです。

### `bdEuler_Value`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `value` | `v` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | Euler成分の保存・中継 |
| `valueX/Y/Z` | `vx/vy/vz` | doubleAngle | `0°` | Euler各成分 |
| `rotateOrder` | `ro` | enum | `xyz` | `value`の回転順序 |

`value`は連続角度として扱います。360°を超えるturn数を保持し、正規化や別Euler表現への
canonicalizeは行いません。Euler rotationの意味を失わないよう、利用時は`value`と
`rotateOrder`を組として接続します。

```text
source.rotate      -> bdEuler_Value.value       -> target.rotate
source.rotateOrder -> bdEuler_Value.rotateOrder -> target.rotateOrder
```

### `bdQuat_Value`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `value` | `v` | double4 compound | `(0, 0, 0, 1)` | Quaternion生値の保存・中継 |
| `valueX/Y/Z/W` | `vx/vy/vz/vw` | double | `0/0/0/1` | Quaternion各成分 |

自動正規化、`q`と`-q`の符号統一、zeroや非有限値の置換は行いません。NodeOperatorは
名前が`value`であってもこのcompoundをQuaternionとして扱い、`value.get()`から
`bdu.Quat`を返します。

両nodeのattributeはreadable、writable、storable、keyableです。値を別outputへコピーする
`compute()`や`attributeAffects()`は持たず、incoming connection、keyframe、scene保存、
downstream dirty伝搬はMayaのplug機構へ任せます。

## `bdQuat_ChangeBasis`

Quaternionの回転角度とraw scaleを保ちながら、回転軸を`axisQuat`で指定した基準へ
変換します。数学的にはgroup conjugation / similarity transformationに相当し、
Maya標準nodeでは`quatInvert` 1個と`quatProd` 2個で構成する処理です。

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputQuat` | `iq` | double4 compound | `(0, 0, 0, 1)` | 基準変換するQuaternion `B` |
| `inputQuatX/Y/Z/W` | `iqx/iqy/iqz/iqw` | double | `0/0/0/1` | 入力成分 |
| `axisQuat` | `aq` | double4 compound | `(0, 0, 0, 1)` | 基準を表すQuaternion `A` |
| `axisQuatX/Y/Z/W` | `aqx/aqy/aqz/aqw` | double | `0/0/0/1` | 基準成分 |
| `direction` | `dir` | enum | `ApplyAxis` | 基準変換の向き |
| `outputQuat` | `oq` | double4 compound | `(0, 0, 0, 1)` | 変換結果 |
| `outputQuatX/Y/Z/W` | `oqx/oqy/oqz/oqw` | double | `0/0/0/1` | 出力成分 |

```text
ApplyAxis:
outputQuat = inverse(axisQuat) * inputQuat * axisQuat

RemoveAxis:
outputQuat = axisQuat * inputQuat * inverse(axisQuat)
```

MayaのQuaternion規約では、`ApplyAxis`は`inputQuat`の回転軸を`axisQuat`で回転し、
`RemoveAxis`はその逆向きへ回転します。同じ`axisQuat`で`ApplyAxis`の結果を
`RemoveAxis`へ渡すと、元の`inputQuat`へ戻ります。

自動正規化、`q` / `-q`の符号統一、zero / 非有限値のfallbackは行いません。
非単位Quaternionも`MQuaternion::inverse()`と積の結果をそのまま返し、zero
`axisQuat`は無効な逆元として非有限値を伝搬します。正規化が必要な場合は
Maya標準の`quatNormalize`を明示的に接続します。

```python
change_basis = nodes.create.bdQuat_ChangeBasis(name="change_basis")
change_basis.inputQuat.set((0.0, 0.0, 0.0, 1.0))
change_basis.axisQuat.set((0.0, 0.0, 0.0, 1.0))
change_basis.direction.set(change_basis.direction.APPLYAXIS)
mod.do_it_dg()
```

## `bdQuat_MultiplyMulti` Attributes

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
product.outputQuat.connect(to_euler.inputQuat)
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

### `bdEuler_DecomposeBendTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputRotate` | `ir` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 分解対象のEuler rotation |
| `inputRotateX/Y/Z` | `irx/iry/irz` | doubleAngle | `0°` | 入力回転成分 |
| `inputRotateOrder` | `iro` | enum | `xyz` | `inputRotate`の回転順序 |
| `axisRotate` | `ar` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 意味上のXYZ基準への変換をEulerで指定 |
| `axisRotateX/Y/Z` | `arx/ary/arz` | doubleAngle | `0°` | 軸基準回転成分 |
| `axisRotateOrder` | `aro` | enum | `xyz` | `axisRotate`の回転順序 |
| `order` | `ord` | enum | `TwistBend` | factorの積順 |
| `output` | `o` | compound | `(0°, 0°, 0°)` | 3成分の親出力 |
| `outputTwist` | `otw` | doubleAngle | `0°` | X軸twist |
| `outputBendH` | `obh` | doubleAngle | `0°` | bend回転ベクトルのY成分 |
| `outputBendV` | `obv` | doubleAngle | `0°` | bend回転ベクトルのZ成分 |
| `bendRatio` | `br` | double | `0.0` | 総bend角度を0～180°で正規化した値 |

`inputRotate`と`axisRotate`をそれぞれのrotate orderでQuaternionへ変換し、
`bdQuat_DecomposeBendTwist`と同じ分解を行います。出力範囲、`bendRatio`、180° bendの
特異点処理、無効入力fallbackもQuaternion版と同一です。

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

### `bdEuler_ComposeBendTwist`

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `input` | `i` | compound | `(0°, 0°, 0°)` | 3成分の親入力 |
| `inputTwist` | `itw` | doubleAngle | `0°` | X軸twist |
| `inputBendH` | `ibh` | doubleAngle | `0°` | bend回転ベクトルのY成分 |
| `inputBendV` | `ibv` | doubleAngle | `0°` | bend回転ベクトルのZ成分 |
| `axisRotate` | `ar` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 意味上のXYZ基準への変換をEulerで指定 |
| `axisRotateX/Y/Z` | `arx/ary/arz` | doubleAngle | `0°` | 軸基準回転成分 |
| `axisRotateOrder` | `aro` | enum | `xyz` | `axisRotate`の回転順序 |
| `order` | `ord` | enum | `TwistBend` | factorの積順 |
| `outputRotateOrder` | `oro` | enum | `xyz` | `outputRotate`のEuler回転順序を指定する入力 |
| `outputRotate` | `ort` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 合成したEuler rotation |
| `outputRotateX/Y/Z` | `orx/ory/orz` | doubleAngle | `0°` | 出力回転成分 |

内部では`bdQuat_ComposeBendTwist`と同じQuaternionを合成し、`outputRotateOrder`で指定した
Euler表現へ変換します。`outputRotateOrder`は名前に`output`を含みますが、出力値ではなく
出力表現を選ぶ入力パラメーターです。destination transformの`rotateOrder`から接続できます。

Euler角は同じorientationに複数の表現があるため、入力したEuler成分やturn数を復元する
nodeではありません。Compose→Decomposeの往復保証はorientationとcanonical Bend / Twist
成分に対するもので、Euler XYZ値そのものの連続性は保証しません。

`output`のchild順と`input`のchild順は、どちらもtwist、horizontal、verticalです。このため
親compoundを直接接続できます。Quaternion compoundもMaya標準nodeと直接接続できます。

分解nodeは角度成分だけを返し、Twist / Bend factor Quaternionは出力しません。factorが
必要な場合は`bdQuat_ComposeBendTwist`で必要な成分だけを再構成します。

- Twistのみ: `inputBendH = inputBendV = 0°`
- Bendのみ: `inputTwist = 0°`
- 入力側の意味座標で得る: 分解nodeと同じ`axisQuat`を設定
- canonical座標で得る: `axisQuat`をidentityにする

片方のfactorがidentityになるため、Twistのみ・Bendのみの再構成結果は`order`に依存しません。

Euler版では上記の`axisQuat`を`axisRotate` + `axisRotateOrder`で指定します。分解nodeの
`output`を合成nodeの`input`へ親compoundのまま接続でき、transformとは次のように
変換nodeなしで接続できます。

```text
source.rotate      -> bdEuler_DecomposeBendTwist.inputRotate
source.rotateOrder -> bdEuler_DecomposeBendTwist.inputRotateOrder
decompose.output   -> bdEuler_ComposeBendTwist.input
target.rotateOrder -> bdEuler_ComposeBendTwist.outputRotateOrder
compose.outputRotate -> target.rotate
```

## Bend / Twist Limit

`bdQuat_LimitBendTwist`と`bdEuler_LimitBendTwist`は、入力orientationをTwist / BendH /
BendVへ分解し、制限後の成分からorientationを再合成します。Euler XYZを直接clampしないため、
回転順序による軸の混在を避けながら、意味上の曲げ・捻り範囲を設定できます。

共通の制限attributeです。

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `bendLimitMode` | `blm` | enum | `Ellipse` | BendH/Vの制限形状 |
| `min` | `mn` | 3つのdoubleAngleを持つcompound | `(-180°, -180°, -180°)` | 最小制限の親入力 |
| `minTwist` | `mntw` | doubleAngle | `-180°` | twist最小値 |
| `minBendH` | `mnbh` | doubleAngle | `-180°` | H負方向の制限値 |
| `minBendV` | `mnbv` | doubleAngle | `-180°` | V負方向の制限値 |
| `max` | `mx` | 3つのdoubleAngleを持つcompound | `(180°, 180°, 180°)` | 最大制限の親入力 |
| `maxTwist` | `mxtw` | doubleAngle | `180°` | twist最大値 |
| `maxBendH` | `mxbh` | doubleAngle | `180°` | H正方向の制限値 |
| `maxBendV` | `mxbv` | doubleAngle | `180°` | V正方向の制限値 |
| `output` | `o` | compound | `(0°, 0°, 0°)` | 制限後のTwist / BendH / BendV |
| `outputTwist` | `otw` | doubleAngle | `0°` | 制限後のtwist |
| `outputBendH` | `obh` | doubleAngle | `0°` | 制限後のbend H成分 |
| `outputBendV` | `obv` | doubleAngle | `0°` | 制限後のbend V成分 |

`min`と`max`のchild順、および`output`のchild順はTwist、BendH、BendVです。初期値では
canonical範囲全体を許可するため、入力orientationを変更しません。各成分で`min > max`の場合は、
`bdDblA_Clamp`と同様に2値を並べ替えて使用します。Twistはどちらのmodeでも通常の区間clampです。

### Bend Limit Mode

| enum | value | 制限形状 | 特徴 |
| --- | ---: | --- | --- |
| `Box` | 0 | H/V平面上の長方形 | BendHとBendVを独立してclamp |
| `Ellipse` | 1 | H/V平面上の楕円 | 方向を保ちながら境界へ放射投影（default） |

`Ellipse`では入力成分の符号に応じて、H/Vそれぞれの負方向または正方向の半径を選びます。

```text
HRadius = H < 0 ? max(0, -minBendH) : max(0, maxBendH)
VRadius = V < 0 ? max(0, -minBendV) : max(0, maxBendV)
ratio   = sqrt((H / HRadius)^2 + (V / VRadius)^2)

ratio > 1:
    H = H / ratio
    V = V / ratio
```

例えばHの正方向を90°、Vの正方向を45°とし、`H=80°`、`V=40°`を入力すると、
`ratio ≈ 1.257`なので出力はおよそ`H=63.6°`、`V=31.8°`です。H:Vを維持するため、
bend回転軸の方向を変えず、総bend量だけを縮小します。負方向には`minBendH/V`の絶対値を
別半径として使用できるため、上下左右で非対称なconeを表現できます。

楕円はneutralの0°を中心とする制限です。ある符号方向の範囲が0°をまたがない場合、その方向の
有効半径は0°まで縮退します。実用上は`minBendH/V <= 0° <= maxBendH/V`として設定してください。
選択方向の半径が0°で、対応する入力成分が0°でない場合、放射方向を維持できる許容点は原点だけに
なるため、BendH/Vを両方0°へ戻します。

Box制限後またはEllipse投影後の総bend角度が180°を超える場合は、H:Vを保ったまま180°へ
縮小します。これはBend/Twistのcanonical範囲を守る安全処理です。180° bend自体はtwist分解の
特異点なので、通常のjoint limitには180°未満を設定することを推奨します。

### Quaternion / Euler Attributes

`bdQuat_LimitBendTwist`は共通制限attributeに加えて、次を持ちます。

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputQuat` | `iq` | double4 compound | `(0, 0, 0, 1)` | 制限対象 |
| `axisQuat` | `aq` | double4 compound | `(0, 0, 0, 1)` | 意味上のXYZ基準への変換 |
| `order` | `ord` | enum | `TwistBend` | 分解・再合成のfactor順 |
| `outputQuat` | `oq` | double4 compound | `(0, 0, 0, 1)` | 制限後のQuaternion |

`bdEuler_LimitBendTwist`はtransformへ直接接続するため、次を持ちます。

| long name | short name | 型 | default | 用途 |
| --- | --- | --- | --- | --- |
| `inputRotate` | `ir` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 制限対象 |
| `inputRotateOrder` | `iro` | enum | `xyz` | 入力Eulerの回転順序 |
| `axisRotate` | `ar` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 意味上のXYZ基準への変換 |
| `axisRotateOrder` | `aro` | enum | `xyz` | 軸基準Eulerの回転順序 |
| `order` | `ord` | enum | `TwistBend` | 分解・再合成のfactor順 |
| `outputRotateOrder` | `oro` | enum | `xyz` | 出力Eulerの回転順序を指定する入力 |
| `outputRotate` | `ort` | 3つのdoubleAngleを持つcompound | `(0°, 0°, 0°)` | 制限後のEuler rotation |

Euler版も内部計算はQuaternion版と同じです。`outputRotate`は指定したrotate orderにおける同じ
orientationを保証しますが、入力Euler channelやturn数の連続性は保証しません。Quaternionや
軸基準がzeroに近い場合、非有限値、未対応enumでは、既存のBend/Twist nodeと同じくidentityと
0°成分へfallbackします。

```text
source.rotate      -> bdEuler_LimitBendTwist.inputRotate
source.rotateOrder -> bdEuler_LimitBendTwist.inputRotateOrder
axis.rotate        -> bdEuler_LimitBendTwist.axisRotate
axis.rotateOrder   -> bdEuler_LimitBendTwist.axisRotateOrder
target.rotateOrder -> bdEuler_LimitBendTwist.outputRotateOrder
bdEuler_LimitBendTwist.outputRotate -> target.rotate
```

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

Quaternion版nodeは有限かつ十分な長さを持つQuaternionを内部で単位化します。zeroに近いQuaternion、
`NaN`、無限値、無効な`axisQuat`では安全なfallbackを返します。

- Decompose: 全角度`0°`、`bendRatio = 0.0`
- Compose: identity Quaternion

Euler版も非有限なrotate / angle入力では同じfallbackを使用します。

- Decompose: 全角度`0°`、`bendRatio = 0.0`
- Compose: `outputRotate = (0°, 0°, 0°)`

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
compose.outputQuat.connect(decompose.inputQuat)
compose.outputQuat.connect(decompose_twist.inputQuat)
decompose.output.connect(recompose.input)
mod.do_it_dg()
```

角度値のNodeOperator APIは、ほかの`doubleAngle` attributeと同じくdegree単位で扱います。
内部のC++計算はMayaのinternal angle unitであるradianです。

## Autodesk Reference

- [MQuaternion C++ API Reference](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_quaternion.html)
