# Maya C++ Plug-in Development

C++ source と build tree は配布用 `bakedanuki` フォルダから分離します。

```text
native/maya/                         C++ source / CMake
build/native/maya<version>/          local build tree (git ignored)
bakedanuki/bakedanuki-util/
  plug-ins/maya2025/bdUtilNodes.mll  Maya 2025 staged runtime binary
  plug-ins/maya2026/bdUtilNodes.mll  Maya 2026 staged runtime binary
  plug-ins/maya2027/bdUtilNodes.mll  Maya 2027 staged runtime binary
```

## Development Guide

C++ node の設計・実装・検証については
[Maya C++ Plug-in Development Guide](docs/README.md) を参照してください。

- [Dependency Node Basics](docs/node-basics.md)
- [RBF Node Family And Roadmap](docs/rbf-roadmap.md)
- [DG, Parallel Evaluation, And Cached Playback](docs/dg-parallel-cache-playback.md)
- [Evaluation And Parallelism](docs/evaluation.md)
- [Testing And Debugging](docs/testing-debugging.md)

## Requirements

- Autodesk Maya 2025 / 2026 / 2027
- Visual Studio 2022 17.8.3 以降（Desktop development with C++）
- CMake 3.27.3 以降

線形代数にはリポジトリ同梱の Eigen 5.0.1 を使用します。header-onlyのため、build
machineやMaya実行環境へEigenを別途インストールする必要はありません。出典、hash、
ライセンスは [native/third_party/README.md](../third_party/README.md) を参照してください。

各Mayaの同梱devkitを使用します。通常のbuild scriptはVisual Studio 2022を検出できない
場合に停止します。複数Maya versionの環境変数を恒久設定せず、buildごとに対象Mayaを
指定します。

## Build

Maya で `bdUtilNodes` がロード済みの場合は、先にアンロードするか Maya を終了します。
Windows はロード中の `.mll` を上書きできません。

```powershell
.\scripts\build-native-maya2025.cmd
.\scripts\build-native-maya2026.cmd
.\scripts\build-native-maya2027.cmd
```

成功すると各Maya versionの `Release` buildが、対応する
`bakedanuki/bakedanuki-util/plug-ins/maya<version>` へコピーされます。

Mayaで既存バイナリをロードしたままコンパイルだけ行う場合は、配布先へのコピーを
省略します。

```powershell
.\scripts\build-native-maya2025.cmd -SkipStage
```

デバッガを使用する場合は Debug build を生成します。

```powershell
.\scripts\build-native-maya2025.cmd -Configuration Debug
```

Debug build は配布用バイナリを上書きせず、
`build/native/maya2025/plugins/bdUtilNodes/Debug` にだけ出力されます。
Visual Studio から `maya.exe` へアタッチし、この `.mll` を絶対パスでロードします。
Maya 2026 / 2027を対象にする場合は、対応するbuild scriptへ読み替えてください。

## Test

初回だけ、Maya Python 用 pytest がない場合は一時ディレクトリへインストールします。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install `
    --target $env:TEMP\codex-mayapy-pytest pytest
```

```powershell
.\scripts\test-native-maya2025.cmd
.\scripts\test-native-maya2026.cmd
.\scripts\test-native-maya2027.cmd
```

テストは各versionのstaged plug-inを対応する`mayapy`へロードし、plug-in / Maya API
versionの一致、double3 / double版、
doubleLinear / doubleLinear3版、scalar doubleAngle版、Euler / Quaternion Value、Quaternion可変長積・基準変換、Quaternion / EulerのBend / Twist分解・合成・Twist専用分解の乗算・安全除算・距離比率・
角度比率・Wrap・最短角度差・最短経路補間・直角三角形計算、および加算・減算・
最小値・最大値・Clamp・Map Range・Absolute・Negate・Condition・Average・Weighted Averageについて、固定入力ノード、
可変長入力ノード、single / multi-source Quaternion orientation RBF interpolative / falloff weight、single / multi-source Bend-Twist falloff weight、single / multi-source position RBF interpolative / falloff weight、RBF weightによるTRS pose blend、空入力、sparse 配列、logical index 順、除数epsilon、`NaN`、無限値、
符号付きゼロ、逆転した上下限、方向付き範囲、Source幅0、外挿、絶対値、符号反転、条件分岐、最初の一致、算術平均、加重平均、weight合計0、合計値のオーバーフロー、element 削除、compound child の直接要求、compound dirty、DG / Serial /
Parallel、ノード接続、scene の保存と再読込、NodeOperator API を確認します。

## Node Implementation Rules

- `plugin.cpp` だけが `MFnPlugin.h` を include します。
- node registration と deregistration は逆順で管理します。
- `compute()` は data block の入力だけを読み、出力だけを書き換えます。
- multi attribute は logical index の連続性を仮定せず、既存要素を走査します。
- 純粋かつ thread-safe な計算ノードは `kParallel` を明示し、共有 mutable state を
  持ちません。
- background evaluation では、normal context の global state や単一 member cache に
  依存しません。
- 新しい node type を追加するときは [NODE_IDS.md](NODE_IDS.md) へ
  `MTypeId` を先に登録します。
- v1.0.0 未満では、`typeName`、attribute 構成・名前・default 値、計算仕様の破壊的変更を
  原則として `0.x.0` の minor release で行う場合があります。`0.x.y` の patch release
  では意図的に行いません。詳細は [Node Basics](docs/node-basics.md#compatibility-policy-before-v100)
  を参照してください。
- 一度公開した `MTypeId` は変更せず、削除した node の ID も別の node に再利用しません。
  旧仕様と新仕様を共存させる場合は、新しい node type と未使用の `MTypeId` を追加します。
