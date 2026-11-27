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

C++ node の追加・変更では、[最初に読む資料](docs/README.md#最初に読む資料)の順に
ノードの基本、dirty 伝搬、検証方法を確認してください。

- [Dependency Node Basics](docs/node-basics.md)
- [Evaluation And Parallelism](docs/evaluation.md#dirty-propagation)
- [Testing And Debugging](docs/testing-debugging.md#dirty-propagation-tests)
- [DG, Parallel Evaluation, And Cached Playback](docs/dg-parallel-cache-playback.md)
- [Controller Shape](docs/controller-shape.md)
- [固定・変形 Cube の拡張指針と速度研究](experiments/fixed_cube/README.md#cube-extension-guide)
- [bdDeleteWithOwner](docs/delete-with-owner.md)
- [RBF Node Family And Roadmap](docs/rbf-roadmap.md)

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

固定 Cube `bdShpL_Cube` は `bdUtilNodes` に含まれ、上記の通常 build で更新します。
既存 `.mod` を利用し、Maya から `cmds.loadPlugin("bdUtilNodes")` でロードできます。
研究用 Geometry DLL は本体と同じノード・描画ソースをコンパイルする比較用です。
研究用 DLL は配布先へ配置せず、本体と同じ Maya process に同時ロードしません。
利用例と制約は[固定 Cube の速度研究](experiments/fixed_cube/README.md)を参照してください。
固定 Cube とフォーカス用シェイプの仕様は[静的シェイプの設計方針](experiments/fixed_cube/README.md#静的シェイプの設計方針)にまとめています。

### 変形対応 Cube

`bdShpL_DeformableCube` は、線の Cube を行列で変形する SubScene ノードです。
固定 Cube と同じ面位置・面スケール・静的変換で形状を組み立て、`shapeDeformMatrix`（`sdm`）のアフィン変換を適用してから、
親の DAG 階層の変換を反映します。
既定の基本形状は各軸 `±0.5 cm`、入力行列は単位行列です。行列は直接設定でき、毎フレーム変化する上流ノードにも接続できます。
両 Cube の `shapeGuideLine`（`sgl`、既定 `False`）を ON にすると、対向面の中央を結ぶ3本の通常線を追加します。ガイドは静的設定で、本体と同じ変形・表示に追従し、境界を広げません。
`shapeFin`（`sfn`、既定 `False`）で Plus 面に Fin を追加できます。本体と同じ描画アイテムで表示し、変形後の境界にも Fin の端点を含めます。[Fin の属性と寸法](../../bakedanuki/bakedanuki-util/README.md#固定-cube)
Cached Playback では各フレームの入力行列を復元します。SubScene 描画では、接続済みの変形行列を入力の変更通知まで再利用します。評価時に取得できた行列は、時刻と世代が一致する描画でも再利用します。
再生中に評価済み行列を使える場合は、`requiresUpdate()` でローカル行列と時刻・世代を保持し、`update()` で親のワールド行列と表示状態を確認して適用します。バウンディングボックスはその時点の入力行列から計算します。Node Editor の Custom Mode には `shapeDeformMatrix` が出ます。

```python
from maya import cmds

cmds.loadPlugin("bdUtilNodes", quiet=True)
control = cmds.createNode("transform", name="control")
shape = cmds.createNode("bdShpL_DeformableCube", parent=control, name="controlShape")
driver = cmds.createNode("transform", name="shapeDriver")
cmds.connectAttr(f"{driver}.matrix", f"{shape}.shapeDeformMatrix")
```

## Test

初回だけ、repository直下で固定versionのpytestを `.test` へ導入します。
`requirements-test.txt` と共通のsetup scriptを使います。

```powershell
.\scripts\setup-test.cmd
```

既存のテスト環境を明示的に再作成する場合は `-ForceRecreate` を指定します。
開発中のネイティブテストは、対象versionに対応する入口を使います。

```powershell
.\scripts\test-native-maya2025.cmd
.\scripts\test-native-maya2026.cmd
.\scripts\test-native-maya2027.cmd
```

作業完了前の統一検証は `.\scripts\verify.cmd -IncludeNative` を使います。
固定・変形対応 Cube の形状調整契約も通常の native test に含まれます。研究用の代替 DLL と
`.mod` 経由の本体ロードを併せて検証する場合は `-IncludeCubeResearch` を追加します。
Viewport 2.0の描画・選択は別のMaya GUIでも確認します。
手順は [Testing And Debugging](docs/testing-debugging.md#viewport-20描画テスト) を参照してください。

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
