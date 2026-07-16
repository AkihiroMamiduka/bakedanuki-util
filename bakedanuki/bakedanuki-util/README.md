# bakedanuki-util

`bakedanuki-util` は、Autodesk Maya での Python ツール開発を扱いやすくするためのユーティリティパッケージです。

今後制作予定のリグシステムパッケージ `bakedanuki-rig` で使用するために開発しています。その中でも、リグシステム専用ではなく他の Maya ツール開発でも使える汎用部分を `util` として切り出しています。

現在は **v0.0.1 に向けた開発中パッケージ**です。正式リリース前のため API は今後変わる可能性がありますが、Maya のノード操作を Python から短く、読みやすく、できるだけ OpenMaya に近い形で扱えることを目指しています。

## Status

- Target: Maya 2025 以降 / Python 3.11.4 以降
- Runtime: Maya 専用
- Distribution: Maya Module
- Stage: pre-1.0.0 / active development
- License: MIT

現時点では開発中の Maya Python ユーティリティとして扱ってください。

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
creater = bdu.NodeCreater(modifier_manager=mod)

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

`bakedanuki-util` は Maya Module として配布する想定です。

配布フォルダの基本構成は次の通りです。

```text
bakedanuki/
  installer.py
  Maya.env
  launchers/
    maya2025.bat
    maya2026.bat
    maya2027.bat
  modules/
    bd_util.mod
  bakedanuki-util/
    README.md
    LICENSE
    docs/
    python/
      bd_util/
```

`bakedanuki/modules/bd_util.mod` には、`bakedanuki-util/python` を Python path に追加する設定が入っています。

```text
+ bd_util 0.0.0 ../bakedanuki-util
PYTHONPATH+:=python
```

そのため、Maya から使う場合は `bakedanuki/modules` を `MAYA_MODULE_PATH` に追加してください。

### installer.py

最も簡単な導入方法は、`bakedanuki/installer.py` を Maya のビューポートへドラッグ&ドロップする方法です。

`installer.py` は、自分自身と同じ階層にある `modules` フォルダを検出し、現在起動している Maya バージョン用の `Maya.env` に `MAYA_MODULE_PATH` を追加します。

追加前には確認ダイアログが表示され、`OK` を選んだ場合だけ `Maya.env` を更新します。`Cancel` を選んだ場合は何も変更しません。`Maya.env` が存在しない場合は新しく作成します。

同じ modules パスが既に登録されている場合は重複して追加しません。パスの大文字・小文字、区切り文字の `\` / `/`、末尾の区切り文字の違いも同じパスとして扱います。

別の bakedanuki フォルダを指すパスが登録されている場合は、置き換え確認のダイアログが表示されます。置き換え時も、bakedanuki 以外の module パスはそのまま維持されます。

新規追加または置き換えられるパスは `/` 区切りで記述され、後から別のパスを追加しやすいように末尾へ `;` が付きます。

変更を反映するには、Maya を再起動してください。

### Maya.env

ユーザー自身の利用する Maya バージョン用 `Maya.env` に次の行を追加します。

```env
MAYA_MODULE_PATH=D:/path/to/bakedanuki/modules;
```

Windows の標準的な配置先は次の通りです。Maya 2026 / 2027 を使う場合は、パス中の `2025` を利用するバージョンに読み替えてください。

```text
%USERPROFILE%\Documents\maya\2025\Maya.env
```

すでに `MAYA_MODULE_PATH` がある場合は、別行を作らず同じ行へ `;` 区切りで追加してください。

```env
MAYA_MODULE_PATH=D:/path/to/bakedanuki/modules;D:/another/maya/modules;
```

このリポジトリには、追記例として [../Maya.env](../Maya.env) を同梱しています。

### bat

試用向けに、Maya を起動する bat も同梱しています。

- [../launchers/maya2025.bat](../launchers/maya2025.bat)
- [../launchers/maya2026.bat](../launchers/maya2026.bat)
- [../launchers/maya2027.bat](../launchers/maya2027.bat)

これらの bat は、`bakedanuki/modules` を `MAYA_MODULE_PATH` に追加してから、対応する Maya を起動します。

```bat
set "BAKEDANUKI_MODULES=%BAKEDANUKI_ROOT%\modules"
```

Maya のインストール先が標準と異なる場合は、各 bat 内の `MAYA_EXE` を環境に合わせて変更してください。

### Import Check

Maya 起動後、Script Editor などで次を実行し、`bd_util` の import 先が `bakedanuki-util/python` 配下になっていれば導入できています。

```python
import bd_util as bdu

print(bdu.__file__)
```

## Testing

テストは `pytest` を使用しています。Maya API を使うため、通常の Python ではなく `mayapy` で実行します。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
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
