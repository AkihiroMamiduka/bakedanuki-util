# Maya C++ Plug-in Development

C++ source と build tree は配布用 `bakedanuki` フォルダから分離します。

```text
native/maya/                         C++ source / CMake
build/native/maya2025/               local build tree (git ignored)
bakedanuki/bakedanuki-util/
  plug-ins/maya2025/bdUtilNodes.mll  staged runtime binary
```

## Requirements

- Autodesk Maya 2025
- Visual Studio 2022 17.8.3 以降（Desktop development with C++）
- CMake 3.27.3 以降

Maya 2025 の公式 devkit 要件に合わせ、通常の build script は Visual Studio
2022 を検出できない場合に停止します。複数 Maya version の環境変数を恒久設定せず、
build ごとに対象 Maya を指定します。

## Build

Maya で `bdUtilNodes` がロード済みの場合は、先にアンロードするか Maya を終了します。
Windows はロード中の `.mll` を上書きできません。

```powershell
.\scripts\build-native-maya2025.cmd
```

成功すると `Release` build の `bdUtilNodes.mll` が
`bakedanuki/bakedanuki-util/plug-ins/maya2025` へコピーされます。

デバッガを使用する場合は Debug build を生成します。

```powershell
.\scripts\build-native-maya2025.cmd -Configuration Debug
```

Debug build は配布用バイナリを上書きせず、
`build/native/maya2025/plugins/bdUtilNodes/Debug` にだけ出力されます。
Visual Studio から `maya.exe` へアタッチし、この `.mll` を絶対パスでロードします。

## Test

初回だけ、Maya Python 用 pytest がない場合は一時ディレクトリへインストールします。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install `
    --target $env:TEMP\codex-mayapy-pytest pytest
```

```powershell
.\scripts\test-native-maya2025.cmd
```

テストは staged plug-in を Maya 2025 の `mayapy` へロードし、
`bdDouble3Mult` の空入力、sparse 配列、ノード接続、scene の保存と再読込、
NodeOperator API を確認します。

## Node Implementation Rules

- `plugin.cpp` だけが `MFnPlugin.h` を include します。
- node registration と deregistration は逆順で管理します。
- `compute()` は data block の入力だけを読み、出力だけを書き換えます。
- multi attribute は logical index の連続性を仮定せず、既存要素を走査します。
- 純粋な計算ノードは `kParallel` を明示し、共有 mutable state を持ちません。
- 新しい node type を追加するときは [NODE_IDS.md](NODE_IDS.md) へ
  `MTypeId` を先に登録します。
- production scene へ保存した `MTypeId`、attribute の long name / short name は
  後から変更しません。
