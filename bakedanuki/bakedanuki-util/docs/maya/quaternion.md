# Quat

`Quat`は、Maya規約のQuaternionを`(x, y, z, w)`順で保持する読み取り専用の
snapshot値です。Quaternionの作成、変換、積、逆元、正規化、補間を、mutableな
`MQuaternion`を共有せずに扱えます。

`Quat`はraw値を保存します。作成時の自動正規化、`q`と`-q`の符号統一、zeroや
非有限値の置換は行いません。この方針はQuaternion compound plugと
`bdUtilNodes`のQuaternion nodeに共通です。

## 作成

公開APIから利用できます。

```python
from maya.api import OpenMaya as om
import bd_util as bdu

identity = bdu.Quat()
from_components = bdu.Quat(0.0, 0.0, 0.0, 1.0)
from_sequence = bdu.Quat((0.0, 0.0, 0.0, 1.0))
from_quat = bdu.Quat(from_components)
from_maya = bdu.Quat(om.MQuaternion())
```

コンストラクタは次の形式を受け取ります。

- 引数なし: identity Quaternion `(0, 0, 0, 1)`
- 4つのnumeric component
- 4要素のnumeric `Sequence`
- `Quat`
- `MQuaternion`

componentは`float`へ変換して保存します。sequenceは正確に4要素である必要があり、
generatorのような一度だけ走査する`Iterable`ではなく、長さを持つ`Sequence`を
受け取ります。入力値は作成時にコピーされるため、元のlistや`MQuaternion`を後から
変更してもsnapshotには影響しません。

### Euler回転から作成

`from_euler()`はdegree単位のXYZ componentと回転順序を受け取ります。

```python
quat = bdu.Quat.from_euler(
    (10.0, 20.0, 30.0),
    rotate_order="zyx",
)
```

`rotate_order`には回転順序名、またはMayaの`transform.rotateOrder`から取得した
integer indexを渡せます。

| index | name |
| ---: | --- |
| `0` | `"xyz"` |
| `1` | `"yzx"` |
| `2` | `"zxy"` |
| `3` | `"xzy"` |
| `4` | `"yxz"` |
| `5` | `"zyx"` |

回転順序名の大文字と小文字は区別しません。integerは
`MEulerRotation` / `transform.rotateOrder`の0〜5を意味し、値体系が異なる
`MTransformationMatrix`のrotation order定数は受け取りません。

### axis-angleから作成

`from_axis_angle()`のangleはdegreeです。

```python
quat = bdu.Quat.from_axis_angle(
    axis=(0.0, 1.0, 0.0),
    angle=45.0,
)
```

axisの扱いは`MQuaternion(angle, axis)`と同じです。

### 2つのvectorから作成

`from_vectors()`はsourceをtargetへ向けるQuaternionを返します。

```python
quat = bdu.Quat.from_vectors(
    source=(1.0, 0.0, 0.0),
    target=(0.0, 1.0, 0.0),
    factor=1.0,
)
```

`factor=0.0`はidentity、`factor=1.0`はsourceからtargetまでの全回転です。
範囲外のfactorもclampせず、`MQuaternion(source, target, factor)`へ渡します。

### matrixから作成

`from_matrix()`はtransform matrixを分解し、回転成分を返します。

```python
quat = bdu.Quat.from_matrix(matrix)
```

次の値を受け取ります。

- `TransformMatrix`
- `MMatrix`
- `MTransformationMatrix`
- row-majorのflat 16要素のmatrix sequence
- 4行4列のmatrix sequence

matrixに負scaleやshearが含まれる場合は、`TransformMatrix.quat`と同じ等価な分解結果を
返します。

## 値と状態

`Quat`はimmutable、hashableな4要素の`Sequence`です。

```python
quat = bdu.Quat(1.0, 2.0, 3.0, 4.0)

x = quat.x
w = quat.w
x, y, z, w = quat
raw = quat.as_tuple()

length = quat.length
length_squared = quat.length_squared
finite = quat.is_finite()
zero = quat.is_zero()
unit = quat.is_unit()
```

`is_zero()`と`is_unit()`の既定toleranceは`MQuaternion.kTolerance`です。
toleranceは有限かつ0以上である必要があります。

mutableなOpenMaya値が必要な場合は、コピーを取得できます。

```python
maya_quat = quat.quaternion
```

返された`MQuaternion`を変更しても元の`Quat`は変わりません。

## 変換

### Euler回転

`to_euler()`は指定した回転順序の`DoubleAngle3`をdegreeで返します。

```python
rotate = quat.to_euler(rotate_order="zyx")
dst.r.set(quat.to_euler(rotate_order=dst.rotateOrder.get()))
```

QuaternionはEulerのturn数や元の回転順序を保持しません。戻り値は指定した回転順序で
同じorientationを表す等価なEuler解です。

### axis-angle

`to_axis_angle()`は`(axis, angle)`を返します。axisは`Double3`、angleはdegreeの
`float`です。

```python
axis, angle = quat.to_axis_angle()
```

`q`と`-q`は同じorientationですが、`MQuaternion.asAxisAngle()`と同様に異なるaxis-angle
表現を返す場合があります。

### TransformMatrix

`to_transform_matrix()`は回転だけを持つ`TransformMatrix`を返します。

```python
matrix = quat.to_transform_matrix()
```

次の書き方と同じ結果です。

```python
matrix = bdu.TransformMatrix(quat=quat)
```

zero Quaternionは有効な回転行列を作れないため`ValueError`です。

## Quaternion積

`Quat`または`MQuaternion`と`*`で乗算でき、新しい`Quat`を返します。

```python
result = first * second
result = first * maya_quat
result = maya_quat * second
```

積の順序はMayaの`MQuaternion.operator*()`、標準`quatProd`、
`bdQuat_MultiplyMulti`と同じです。Quaternion積は可換ではありません。

scalarとの乗算やcomponent-wise乗算は提供しません。

## 逆元・共役・正規化・符号反転

すべて元の値を変更せず、新しい`Quat`を返します。

```python
inverse = quat.inverse()
conjugate = quat.conjugate()
normalized = quat.normalized()
opposite_sign = -quat
```

演算結果は`MQuaternion.inverse()` / `conjugate()` / `normal()` / unary `-`と
一致します。自動的な事前正規化は行いません。

Maya 2025 / 2026 / 2027では、zero Quaternionの`normal()`はidentity、`inverse()`は
全成分が`NaN`のQuaternionを返します。`Quat`もこの挙動を維持します。

## 補間

`slerp()`はMayaのshortest-path球面線形補間を行います。

```python
result = source.slerp(target, weight=0.5)
```

targetには`Quat`または`MQuaternion`を渡せます。weightは`[0, 1]`へclampしないため、
範囲外の値による外挿も`MQuaternion.slerp()`と同じ規則で扱います。

## equalityとQuaternion等価性

`==`は保存されたraw componentと型を比較します。hashも同じraw値に基づきます。

```python
quat == same_raw_value
```

`is_equivalent()`は`MQuaternion.isEquivalent()`と同じ規則でQuaternion空間の距離を
比較し、`q`と`-q`を等価として扱います。

```python
quat.is_equivalent(-quat)
```

非単位Quaternionの非zero scalar倍はraw lengthが異なるため、そのままでは等価と
判定されません。orientationだけを比較する場合は、両方を明示的に`normalized()`して
から比較します。

## Quaternion plugとの連携

Quaternion compound plugの`get()`は`Quat`を返し、`set()` / `set_direct()`は`Quat`を
4要素sequenceとして受け取ります。

```python
value = node.inputQuat.get()
result = value.inverse()
node.inputQuat.set(result)
```

`Quat`コンストラクタはplug名や`MPlug`を直接解決しません。scene値の取得と設定は
`PlugOperator`、Quaternion値の計算は`Quat`が担当します。

## 設計契約と今後の拡張

現時点で`Quat`は、Quaternionの作成、Mayaで日常的に必要な形式との相互変換、
合成、逆元、正規化、補間、状態と等価性の照会を持ち、value-level APIとしての
完了条件を満たしています。

今後も次の契約を維持します。

- `Quat`はsceneやplugへの参照を持たない、immutableなraw snapshot値とする。
- component順は`(x, y, z, w)`、公開APIのangleはdegreeとする。
- 演算は暗黙に正規化、符号統一、clamp、zeroや非有限値の置換を行わない。
- Maya APIに対応する演算は、通常値だけでなくzeroなどの境界挙動も
  `MQuaternion`と一致させる。
- `==`とhashは保存されたraw値、orientationの比較は`is_equivalent()`で扱う。
- scene値の取得と設定は`PlugOperator`、行列の合成と分解は`TransformMatrix`へ
  分離する。

scalar / component-wise乗算、Eulerのturn数や元の回転順序の復元、plug名や`MPlug`の
直接解決は、責務や意味が異なるため意図的に提供しません。

vector回転、dot、nlerp、squadなどを将来追加する場合は、一般的なQuaternion APIを
網羅すること自体を目的にせず、具体的な利用例、単位、raw値への扱い、zeroでの挙動、
戻り値型を先に確定します。Maya APIに対応する処理は実挙動を確認し、runtime testと
Pyright contractを同時に追加します。
