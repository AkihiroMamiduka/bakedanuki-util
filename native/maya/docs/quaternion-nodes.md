# Quaternion Nodes

3軸orientationの合成は、各軸を独立した`doubleAngle3`として計算せずQuaternionで扱います。
Maya標準の`quatProd`、`quatSlerp`、`quatNormalize`、`eulerToQuat`、`quatToEuler`などを
基本とし、標準nodeにない可変長積だけを`bdUtilNodes`で補います。

## Implemented Scope

| node type | 役割 | 状態 |
| --- | --- | --- |
| `bdQuat_MultiplyMulti` | 任意個のQuaternionを順序付きで乗算 | 実装済み |

固定2入力版はMaya標準の`quatProd`を使用します。独自の`bdQuat_Multiply`は作りません。
補間、正規化、共役、逆元、Euler変換についても、用途上の不足が確認されるまでは
標準nodeを利用します。

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

## Autodesk Reference

- [MQuaternion C++ API Reference](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_quaternion.html)
