# bakedanuki-util

`bakedanuki-util` は、Autodesk Maya での Python ツール開発を扱いやすくするためのユーティリティパッケージです。

今後制作予定のリグシステムパッケージ `bakedanuki-rig` で使用するために開発しています。その中でも、リグシステム専用ではなく他の Maya ツール開発でも使える汎用部分を `util` として切り出しています。

現在は **v0.0.1 に向けた開発中パッケージ**です。正式リリース前のため API は今後変わる可能性がありますが、Maya のノード操作を Python から短く、読みやすく、できるだけ OpenMaya に近い形で扱えることを目指しています。

## Status

- Target: Maya 2025 / Python 3.11.4 以降
- Runtime: Maya 専用
- Stage: pre-1.0.0 / active development
- License: MIT

まだ一般利用向けのパッケージ整備や Maya Module 化は途中です。現時点では、開発中の Maya Python ユーティリティとして扱ってください。

## What This Package Provides

主な機能は次の通りです。

- `NodeOperator`
  - Maya ノードを Python クラスとして扱うためのラッパーです。
  - `node.input1D[0].set(10.0)` のように、プラグ操作をオブジェクト経由で書けます。
- `NodeCreater`
  - ノード作成用の入口です。
  - 各 `NodeOperator` クラスを個別に import せず、Maya の nodeType 名に近いメソッドから作成できます。
- `BDNode`
  - シーン上に既に存在するノードを、対応する `NodeOperator` として包む入口です。
- `ModifierManager`
  - `MDGModifier` / `MDagModifier` をまとめて扱う管理クラスです。
  - 将来的に MPxCommand の undo / redo へ組み込みやすい形を目指しています。
- Attribute / Plug helpers
  - `AttributeField`, `AttrOperator`, `PlugOperator` により、クラス定義とインスタンス操作を分けて扱います。
- Node class generator
  - Maya の DG ノード情報から `NodeOperator` 定義を生成する開発用ジェネレーターがあります。

## Quick Example

### Create Nodes

```python
import bd_util as bdu

mod = bdu.ModifierManager()
creater = bdu.NodeCreater(modifier_manager=mod)

pma = creater.plusMinusAverage(name="pma")
mult = creater.multiplyDivide(name="mult")

mod.do_it_dg()
```

`NodeCreater` の生成メソッド名は、基本的に Maya の nodeType 名に合わせています。

```python
compose = creater.composeMatrix(name="compose")
decompose = creater.decomposeMatrix(name="decompose")
```

Python キーワードと衝突する `and`, `or`, `not` などは、`and_()`, `or_()`, `not_()` のように末尾 `_` を付けます。

### Wrap Existing Nodes

```python
from maya import cmds
import bd_util as bdu

cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

pma = bdu.BDNode("test_plus_minus_ave")
pma.input1D[0].set(10.0)
pma.modifier_manager.do_it_dg()
```

`BDNode` は既存ノードを包むだけなので、初期状態では extra attribute を自動追加しません。必要な場合は `auto_add_attr=True` を渡してください。

```python
node = bdu.BDNode("my_node", auto_add_attr=True)
```

### Connect Plugs

```python
import bd_util as bdu

mod = bdu.ModifierManager()
creater = bdu.NodeCreater(mod)

a = creater.plusMinusAverage(name="a")
b = creater.plusMinusAverage(name="b")

a.output1D.connect(b.input1D[0])
mod.do_it_dg()
```

演算子を使った接続もできます。

```python
a.output1D > b.input1D[0]
mod.do_it_dg()
```

マルチアトリビュートへ次の空き index で接続したい場合は、`[next]` を使えます。

```python
cmp_m = creater.composeMatrix(name="cmp_m")
mult_m = creater.multMatrix(name="mult_m")

cmp_m.outputMatrix > mult_m.matrixIn[next]
mod.do_it_dg()
```

速度を重視する場合は、明示的に `.connect()` を使う方が意図も分かりやすくなります。

## Install / Setup

現時点では正式なインストール手順はまだ整備中です。

開発中に試す場合は、このリポジトリの `src` ディレクトリを Maya Python から見えるようにしてください。

PowerShell の例:

```powershell
$env:PYTHONPATH = "D:\develop\bakedanuki_dev\bakedanuki-util\src"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe"
```

Maya Script Editor などで利用する場合も、同様に `src` が `sys.path` に入っている必要があります。

Maya Module としての配布・導入手順は今後整備予定です。

## Testing

テストは `pytest` を使用しています。Maya API を使うため、通常の Python ではなく `mayapy` で実行します。

```powershell
$env:PYTHONPATH = (Join-Path $env:TEMP 'codex-mayapy-pytest')
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

環境によっては、Maya Python 側に `pytest` を追加する必要があります。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install --target $env:TEMP\codex-mayapy-pytest pytest
```

## Documentation

詳細な設計メモは `docs/` 以下にあります。

- [NodeOperator Overview](docs/maya/node_operator/README.md)
- [Attributes](docs/maya/node_operator/attributes.md)
- [Core](docs/maya/node_operator/core.md)
- [ModifierManager](docs/maya/node_operator/modifier_manager.md)
- [Generator](docs/maya/node_operator/generator.md)
- [Testing](docs/maya/node_operator/testing.md)
- [Roadmap](docs/maya/node_operator/roadmap.md)

## Current Notes

- まだ v1.0.0 未満のため、API は破壊的に変更される可能性があります。
- 現在は Maya 2025 以降を前提にしています。
- `NodeOperator` / `AttributeField` / `PlugOperator` 周辺は、利便性と速度の両立を重視して継続的に調整しています。
- 生成済み DG ノード定義は増えていますが、すべてのノード操作が十分に検証済みとは限りません。

## License

MIT License
