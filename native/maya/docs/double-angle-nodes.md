# Double Angle Nodes

`bdUtilNodes`のscalar `doubleAngle`演算node familyです。type codeは`DblA`とし、
1軸の回転channel、twist、roll、hinge、bank、回転制限、angle driverなどを対象にします。

## Scope And Angle Policy

このfamilyの角度は、周期的なorientationではなく、正規化されていない連続値として
扱います。Mayaの`rotateX`などと同様に、`370 deg`、`720 deg`、`-450 deg`をそのまま
保持して演算します。

```text
350 deg + 20 deg = 370 deg
10 deg - 350 deg = -340 deg
lerp(350 deg, 10 deg, 0.5) = 180 deg
```

通常演算は`-180..180`や`0..360`へwrapしません。Wrap、最短角度差、最短経路補間は、
後続のangle固有nodeとして通常演算と分けて設計します。

3軸のorientation計算はQuaternionまたはrotate orderを持つEuler rotationとして扱うため、
`DblA3`演算nodeと`DblA3_Value`はこのfamilyの対象外です。3つの独立したangle channelが
必要な場合はscalar nodeを各軸へ接続します。

## Implemented Nodes

| Node type | Angle inputs | Non-angle inputs | Result |
| --- | --- | --- | --- |
| `bdDblA_Value` | `value` | none | 保存・編集・接続可能なangle value |
| `bdDblA_Add` | `input1`, `input2` | none | `input1 + input2` |
| `bdDblA_AddMulti` | `input[]` | none | 既存要素の合計。空配列はzero |
| `bdDblA_Subtract` | `input1`, `input2` | none | `input1 - input2` |
| `bdDblA_SubtractMulti` | `input[]` | none | logical index順の左畳み込み。空配列はzero |
| `bdDblA_Negate` | `input` | none | `-input` |
| `bdDblA_Abs` | `input` | none | raw angle値の絶対値 |
| `bdDblA_Multiply` | `input` | `factor: double` | `input * factor` |
| `bdDblA_MultiplyMulti` | `input` | `factor[]: double` | factorを畳み込む。空配列はinput |
| `bdDblA_Divide` | `input` | `factor: double` | `input / factor` |
| `bdDblA_DivideMulti` | `input` | `factor[]: double` | factorをlogical index順に除算。空配列はinput |
| `bdDblA_Clamp` | `input`, `min`, `max` | none | raw angle rangeへclamp |
| `bdDblA_MapRange` | input、Source / Target range | `clamp: bool` | angle rangeからangle rangeへ変換 |
| `bdDblA_Lerp` | `input1`, `input2` | `weight: double` | raw angle値の線形補間 |
| `bdDblA_Min` | `input1`, `input2` | none | 小さいraw angle値を選択 |
| `bdDblA_MinMulti` | `input[]` | none | 既存要素の最小値。空配列はzero |
| `bdDblA_Max` | `input1`, `input2` | none | 大きいraw angle値を選択 |
| `bdDblA_MaxMulti` | `input[]` | none | 既存要素の最大値。空配列はzero |

Multiply / Divideの`factor`はdimensionlessです。angle同士の乗除算ではありません。
Divideは既存の`SafeDivision.h`を使用し、絶対値が`1.0e-9`未満のfactorを符号付きepsilonへ
置き換えます。

## Units And Defaults

attributeは`MFnUnitAttribute::kAngle`で作成し、C++の`MDataHandle::asDouble()` /
`setDouble()`ではMaya内部単位のradianを扱います。PythonのNodeOperator APIは既存の
`DoubleAngleField`に従いdegreeで`.get()` / `.set()`します。

zero defaultは単位表示に依存しません。`Clamp.max`、`MapRange.srcMax`、
`MapRange.dstMax`のdefaultは1回転を表す360度（内部値は2π radian）です。
`factor`のdefault `1.0`はdimensionless identityです。

angle表示単位をdegree / radian間で切り替えても、scene内の物理角度と計算結果は
変化しません。`rotateX`などの`doubleAngle` plugとはunit conversion nodeなしで
直接接続できます。

## Orientation Boundary

このfamilyは1軸のangle channel計算だけを担当します。3軸回転について、次の処理を
component-wise angle演算で代用しません。

- orientationの合成と相対回転
- rotate orderを考慮したEuler変換
- Euler解の選択
- Quaternion Slerp

これらはMayaの`eulerToQuat`、`quatToEuler`、`quatProd`、`quatInvert`、`quatSlerp`
などを使用します。

## Verification

[test_bd_double_angle.py](../../../tests/maya/node/operator/node/dg/test_bd_double_angle.py)で、
18 node typeのIDとattribute型、連続角度演算、sparse multi、表示単位、`rotateX`接続、
DG / Serial / Parallel、NodeOperator API、scene round-tripを確認します。
