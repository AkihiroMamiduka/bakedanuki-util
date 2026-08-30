# Numeric Compound Values

`Double2` / `Double3` / `Double4`、`Float2` / `Float3`は、複数の浮動小数点componentを
immutableに保持するsnapshot値です。plugから取得した値の保存に加えて、基本的な
component-wise演算を行えます。

## 対応する演算

加算と減算は、左右が同じ具体型の場合だけ対応します。演算結果は元の値を変更せず、
同じ具体型の新しい値として返します。

```python
import bd_util as bdu

left = bdu.Double3(1.0, 2.0, 3.0)
right = bdu.Double3(4.0, 5.0, 6.0)

added = left + right
subtracted = left - right

assert isinstance(added, bdu.Double3)
assert tuple(left) == (1.0, 2.0, 3.0)
```

`int`または`float`のscalarによる乗算・除算と、符号反転にも対応します。
scalarを左辺にした乗算も可能です。

```python
doubled = left * 2
also_doubled = 2.0 * left
halved = left / 2.0
negated = -left
```

`bool`はPythonでは`int`の派生型ですが、数値scalarとして受け取りません。0による除算は
通常のPython演算と同じく`ZeroDivisionError`です。

## 意図的に対応しない演算

次の演算は、意味や戻り値を暗黙に決めないため`TypeError`になります。

- `Double3 + Float3`のような異なる具体型同士の加減算
- valueとtuple / listなどのsequenceとの演算
- value同士の乗算・除算
- scalarとの加算・減算、scalarを左辺にした除算
- `bool`による乗算・除算

value同士の`*`を要素積、内積、別の数学的操作のどれとするかは型や用途によって
異なります。必要になった場合は、意味を名前で表すnamed methodとして個別に追加します。

## 演算を持たない値型

`Long2` / `Long3`、`Short2` / `Short3`には、除算結果、丸め、overflowの契約を
定めていないため、現時点では演算を追加していません。

`DoubleLinear2/3`、`FloatLinear2/3`、`DoubleAngle2/3`、`FloatAngle2/3`にも
演算を追加していません。長さ同士の乗算は面積になり、Euler角のcomponent演算は
orientationの合成と一致しないためです。単位や次元を伴う演算が必要になった時点で、
戻り値型を含めて個別に設計します。

`Quat`は4つの`float`を保持しますが、`Double4`とは継承関係を持たない独立した意味型です。
component-wiseなnumeric演算ではなく、Quaternion積、逆元、正規化、補間などを提供します。
詳細は[Quat](quaternion.md)を参照してください。

## 型とplugの境界

double4 compound plugとQuaternion compound plugは、Maya上では同じ4つのdouble childを
持つ物理表現を共有できます。一方、`get()`が返す値型はplugの意味に従い、通常の
double4は`Double4`、Quaternionは`Quat`です。物理的な保存形式を共有しても、公開APIの
型と演算体系は分離します。
