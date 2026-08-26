# bakedanuki-util

`bakedanuki-util` は、Autodesk Maya での Python ツール開発を扱いやすくするためのユーティリティパッケージです。

今後制作予定のリグシステムパッケージ `bakedanuki-rig` で使用するために開発しています。その中でも、リグシステム専用ではなく他の Maya ツール開発でも使える汎用部分を `util` として切り出しています。

現在は **v0.2.0 / pre-1.0.0 の開発中パッケージ**です。API は今後変わる可能性がありますが、Maya のノード操作を Python から短く、読みやすく、できるだけ OpenMaya に近い形で扱えることを目指しています。

## Status

- Target: Maya 2025 以降 / Python 3.11.4 以降
- Release verification: Windows / Maya 2025 / 2026 / 2027
- Bundled native plug-in: Windows / Maya 2025 / 2026 / 2027
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
- `Nodes`
  - ノード作成と既存ノード変換を、同じ `ModifierManager` から扱う統合入口です。
  - `nodes.create.transform()` / `nodes.existing.transform()` のように用途を明示できます。
- `ModifierManager`
  - `MDGModifier` / `MDagModifier` をまとめて扱う管理クラスです。
  - 将来的に MPxCommand の undo / redo へ組み込みやすい形を目指しています。
- `TransformMatrix`
  - matrix plug や `MMatrix` を、合成・逆行列・TRS 分解が可能なスナップショット値として扱います。
- Attribute / Plug helpers
  - `AttributeField`, `AttrOperator`, `PlugOperator` により、クラス定義とインスタンス操作を分けて扱います。
- Node class generator
  - Maya の DG ノード情報から `NodeOperator` 定義を生成する開発用ジェネレーターがあります。
- Maya UI foundation
  - PySide6のbinding facade、通常Window、workspaceControlを使うdockable Window、状態保存、
    配置reset、Maya callback lifecycleを共通化します。
  - Maya 2025 / 2026 / 2027で同じUI互換性テストを実行できます。
  - 詳細は[UI utilities](docs/ui/README.md)を参照してください。

## Quick Example

### Transform Matrix

```python
from maya import cmds
import bd_util as bdu

src = cmds.createNode("transform", name="src")
dst = cmds.createNode("transform", name="dst")

nodes = bdu.Nodes()
src_dag = nodes.existing.transform(src)
dst_dag = nodes.existing.transform(dst)

local_tm = src_dag.get_local_matrix(dst_dag)
translate = local_tm.translate
inverse_tm = local_tm.inverse()

world_tm = src_dag.worldMatrix[0].get()
world_translate = world_tm.translate
```

matrix plug の `get()` は `TransformMatrix` を返します。`translate` / `rotate` / `scale` / `shear` / `quat` は、float の tuple として取得できます。`rotate` は XYZ order の degree です。

詳細は [TransformMatrix](docs/maya/transform_matrix.md) を参照してください。

### Unified Node Access

```python
from maya import cmds
import bd_util as bdu

cmds.createNode("transform", name="existing_node")

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

created = nodes.create.transform(name="new_node")
existing = nodes.existing.transform("existing_node")

mod.do_it_dag()
```

`nodes.create` と `nodes.existing` は同じ `ModifierManager` を共有します。
`nodes.existing("nodeName")` と呼ぶと、既存ノードの nodeType を自動判定できます。

### Create Nodes

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

pma = nodes.create.plusMinusAverage(name="pma")
mult = nodes.create.multiplyDivide(name="mult")

mod.do_it_dg()
```

`nodes.create` は、同じ `ModifierManager` を使うノード作成アクセサです。
生成メソッド名は、基本的に Maya の nodeType 名に合わせています。

```python
compose = nodes.create.composeMatrix(name="compose")
decompose = nodes.create.decomposeMatrix(name="decompose")
```

Python キーワードと衝突する `and`, `or`, `not` などは、`and_()`, `or_()`, `not_()` のように末尾 `_` を付けます。

### Native Plug-in Node

v0.2.0 には、Windows版 Maya 2025 / 2026 / 2027 向けの
`bdUtilNodes.mll` をそれぞれ同梱します。Maya Moduleが実行中のMaya versionに対応する
`plug-ins/maya<version>` をplug-in pathへ追加します。

Maya の Plug-in Manager で `bdUtilNodes.mll` をロードすると、
固定2入力の `bdDbl3_Multiply` と、可変長入力の `bdDbl3_MultiplyMulti` を
`Nodes` から使用できます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

mult = nodes.create.bdDbl3_Multiply(name="mult")
mult.input1.set((2.0, 3.0, 4.0))
mult.input2.set((5.0, 6.0, 7.0))

mod.do_it_dg()

print(mult.output.get().as_tuple())  # (10.0, 18.0, 28.0)
```

`bdDbl3_Multiply` の `input1` と `input2` は `double3` です。2入力を成分ごとに
乗算します。

任意個の `double3` を乗算する場合は `bdDbl3_MultiplyMulti` の multi attribute
`input` を使用します。既存要素を成分ごとに乗算し、要素がない場合は
`(1.0, 1.0, 1.0)` を返します。

```python
multi = nodes.create.bdDbl3_MultiplyMulti(name="multi")
multi.input[0].set((2.0, 3.0, 4.0))
multi.input[3].set((5.0, 6.0, 7.0))
```

### Wrap Existing Nodes

```python
from maya import cmds
import bd_util as bdu

cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

nodes = bdu.Nodes()
pma = nodes.existing("test_plus_minus_ave")
pma.input1D[0].set(10.0)
pma.modifier_manager.do_it_dg()
```

nodeType を自動判定させる代わりに、対応するメソッドを明示することもできます。
通常の nodeType では、各メソッドの戻り値が具体的な `NodeOperator` 型として補完されます。

```python
mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

cmds.createNode("decomposeMatrix", name="dcmp_m")
dcmp_m = nodes.existing.decomposeMatrix("dcmp_m")
```

指定したメソッドと Maya 上の実際の nodeType が異なる場合は `TypeError` を送出します。
例えば `nodes.existing.decomposeMatrix()` に `composeMatrix` ノードを渡すことはできません。

`nodes.existing` は既存ノードを包むだけなので、初期状態では extra attribute を自動追加しません。必要な場合は `auto_add_attr=True` を渡してください。

```python
nodes = bdu.Nodes()
node = nodes.existing("my_node", auto_add_attr=True)
```

### Connect Plugs

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

a = nodes.create.plusMinusAverage(name="a")
b = nodes.create.plusMinusAverage(name="b")

a.output1D.connect(b.input1D[0])
mod.do_it_dg()
```

接続先から既存plugのpathを指定する場合は、`connect_from()` を使います。

```python
b.input1D[0].connect_from("a.output1D")
mod.do_it_dg()

b.input1D[0].disconnect_from(["a", "output1D"])
mod.do_it_dg()
```

マルチアトリビュートへ次の空き index で接続したい場合は、`[next]` を使えます。

```python
cmp_m = nodes.create.composeMatrix(name="cmp_m")
mult_m = nodes.create.multMatrix(name="mult_m")

cmp_m.outputMatrix.connect(mult_m.matrixIn[next])
mod.do_it_dg()
```

## Install / Setup

`bakedanuki-util` は Maya Module として配布する想定です。

配布フォルダの基本構成は次の通りです。

```text
bakedanuki/
  installer.py
  launchers/
    maya2025.bat
    maya2026.bat
    maya2027.bat
  modules/
    bd_util.mod
  bakedanuki-util/
    README.md
    LICENSE
    THIRD_PARTY_NOTICES.md
    docs/
    licenses/
    plug-ins/
      maya2025/
        bdUtilNodes.mll
      maya2026/
        bdUtilNodes.mll
      maya2027/
        bdUtilNodes.mll
    python/
      bd_util/
```

`bakedanuki/modules/bd_util.mod` には、`bakedanuki-util/python` を Python path に追加する設定が入っています。

```text
+ bd_util 0.2.0 ../bakedanuki-util
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

実行時に生成された `installer.py` 自身の bytecode cache は処理終了時に削除されます。`__pycache__` 内に他の cache がある場合は、それらを残してフォルダも維持します。

変更を反映するには、Maya を再起動してください。

### Maya.env

`installer.py` を使用しない場合は、ユーザー自身の利用する Maya バージョン用 `Maya.env` に次の行を追加します。

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

- [TransformMatrix](docs/maya/transform_matrix.md)
- [NodeOperator Overview](docs/maya/node_operator/README.md)
- [Attributes](docs/maya/node_operator/attributes.md)
- [Core](docs/maya/node_operator/core.md)
- [ModifierManager](docs/maya/node_operator/modifier_manager.md)
- [Generator](docs/maya/node_operator/generator.md)
- [Testing](docs/maya/node_operator/testing.md)
- [Roadmap](docs/maya/node_operator/roadmap.md)

## Current Notes

- v1.0.0 未満では将来の設計と使いやすさを優先し、互換性維持よりも改善を選びます。
  破壊的変更は原則として `0.x.0` の minor release で行い、`0.x.y` の patch release
  では意図的に行いません。安定した API 互換性の提供は v1.0.0 以降を対象とします。
- 変更対象には公開 Python API のほか、ネイティブノードの `typeName`、attribute 構成・
  名前・default 値、計算仕様も含まれます。既存 scene の移行やノードの再作成が必要に
  なる場合があり、破壊的変更と移行手順はルートの `CHANGELOG.md` に記録します。
- 一度公開した `MTypeId` は v1.0.0 未満でも変更・再利用しません。旧仕様と新仕様を
  共存させる場合は、新しい node type と未使用の `MTypeId` を追加します。
- 現在は Maya 2025 以降を前提にしています。
- `NodeOperator` / `AttributeField` / `PlugOperator` 周辺は、利便性と速度の両立を重視して継続的に調整しています。
- 生成済み DG ノード定義は増えていますが、すべてのノード操作が十分に検証済みとは限りません。

## License

MIT License

`bdUtilNodes.mll` が使用する第三者ライブラリについては
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) を参照してください。
