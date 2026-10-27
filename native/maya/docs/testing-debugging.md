# Testing And Debugging

C++ node は compile に成功しても、dirty 伝搬、scene 保存、Parallel 評価で初めて現れる
不具合があります。この文書では、`bdUtilNodes` の build 後に行う検証をまとめます。

## Build Variants

通常の動作確認と性能計測には Release build を使います。

```powershell
.\scripts\build-native-maya2025.cmd
.\scripts\build-native-maya2026.cmd
.\scripts\build-native-maya2027.cmd
```

Maya が staged `.mll` をロード中で、build tree の生成だけを続けたい場合は stage を
省略します。

```powershell
.\scripts\build-native-maya2025.cmd -SkipStage
```

Visual Studio で source-level debugging を行う場合は Debug build を使います。

```powershell
.\scripts\build-native-maya2025.cmd -Configuration Debug
```

Debug binary と PDB は次に出力されます。

```text
build/native/maya2025/plugins/bdUtilNodes/Debug/
```

同じ path の `.mll` を Maya がロードしている間、Windows は上書きを拒否します。
再 build 前に plug-in をアンロードするか、scene 内の対象 node を削除してから Maya を
終了します。コンパイルだけなら `-SkipStage` で別の staged binary の file lock を
避けられます。

## Automated Tests

native nodeの標準テストは、配布対象のMaya 2025 / 2026 / 2027それぞれの`mayapy`で
実行します。

```powershell
.\scripts\test-native-maya2025.cmd
.\scripts\test-native-maya2026.cmd
.\scripts\test-native-maya2027.cmd
```

関連テストは次にあります。

- [test_bd_dbl3_multiply.py](../../../tests/maya/node/operator/node/dg/test_bd_dbl3_multiply.py)
- [test_bd_delete_with_owner.py](../../../tests/maya/node/operator/node/dg/test_bd_delete_with_owner.py)
- [test_bd_controller_shape.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py)

新しい node では、少なくとも次を自動化します。

| Category | Test |
| --- | --- |
| Registration | plug-in load、node type の作成 |
| Defaults | 未接続時の input と output |
| Values | 代表値、0、負数、小数 |
| Compound | 親 plug と各 child plug の設定・取得 |
| Dirty | 各 input または child の変更後に output が更新される |
| Connections | node 間を接続した状態で downstream が更新される |
| Multi | 空、1要素、複数要素、sparse logical index |
| Persistence | scene 保存・再読込後の type、値、接続 |
| Public API | NodeOperator wrapper と型付き attribute access |
| Failure path | 不正な plug、load / unload 条件、必要な error handling |

`compute()` を直接 C++ unit test するだけでは Maya の dirty propagation と evaluation
schedule を検証できません。最終的な correctness test は、Maya に plug-in をロードして
実際の DG を評価します。

## Viewport 2.0描画テスト

`bdControllerShape` の描画比較は
[test_controller_shape_viewport.py](../../../tests/maya/ui/test_controller_shape_viewport.py) にあります。
立体の外向きの面、薄い面の両面表示、Fillの表示条件による線の切り替え、
矢印先端への接続、Arrow3Dの追加面、Selection Highlightingと表示種別の組み合わせを確認します。
形状の仕様と手動で確認する項目は [Controller Shape](controller-shape.md) を参照してください。

このテストは実際のViewport 2.0を持つMaya GUIで実行します。
`mayapy` のbatch環境ではskipするため、`test-ui-maya*.cmd` や
`verify.cmd -IncludeNative` の成功だけでは画像比較の成功を確認できません。
`offScreen=True` はplayblastの取得方法であり、GUIを不要にする設定ではありません。

対象バージョンのplug-inをbuild / stageした後、作業中のMayaとは別の空のMaya GUIを起動し、
PythonのScript Editorから次を実行します。テストはsceneを新規作成するため、
必要なsceneや作業状態のない専用プロセスを使用してください。
`repo_root` は実際のcheckoutへ変更します。pytestは `setup-test.cmd` で用意した `.test` を使います。

```python
import sys
import tempfile
from pathlib import Path

from maya import utils

repo_root = Path(r"D:\develop\bakedanuki_dev\bakedanuki-util")
sys.path.insert(0, str(repo_root / ".test"))
sys.path.insert(0, str(repo_root / "bakedanuki/bakedanuki-util/python"))


def run_controller_viewport_tests():
    import pytest

    output_dir = Path(tempfile.mkdtemp(prefix="bd-controller-vp2-"))
    exit_code = pytest.main(
        [
            "-p",
            "no:cacheprovider",
            "-q",
            "--confcutdir",
            str(repo_root / "tests/maya"),
            str(repo_root / "tests/maya/ui/test_controller_shape_viewport.py"),
            "--basetemp",
            str(output_dir / "pytest"),
            "--junitxml",
            str(output_dir / "results.xml"),
        ]
    )
    print(f"Viewport pytest: {exit_code}, results: {output_dir}")


utils.executeDeferred(run_controller_viewport_tests)
```

`--confcutdir` は `tests/maya/conftest.py` のfixtureを使い、
上位の `tests/conftest.py` によるstandalone初期化をGUIから呼ばないための指定です。
GuideLineの変更だけを切り分ける場合は、`pytest.main()` の引数へ
`"-k", "guide_line or arrow_tip_connection"` を追加できます。
対象を絞った確認後は、変更範囲に応じた回帰と統一検証も行います。

既定では実行中のMayaバージョンに対応した配布先 `.mll` をロードします。
別のbinaryを検証する場合は、Mayaを起動する前に `BD_UTIL_NODES_PLUGIN_PATH` へその絶対pathを指定します。
Maya 2025 / 2026 / 2027の各GUIで同じ手順を使い、pytestの終了コードとJUnit XMLを確認します。
テストのPNGは `output_dir / "pytest"` 以下に残ります。
検証後は専用Mayaを終了してからstaged binaryを更新してください。
テスト用Mayaが残っている場合もWindowsのfile lockでstageに失敗します。
Maya自身のplug-in読み込み確認が表示された場合は、利用者が許可してから実行を再開します。
確認ダイアログで停止している間は、テストの完了として扱いません。

画像比較を変更する際は、既存の `_capture_view()` を基準にします。

- パネルへfocusを移してidle処理を進め、`cmds.playblast(editorPanelName=..., offScreen=True, ...)` でPNGを取得する。
  この検証環境では `M3dView.readColorBuffer()` で空や更新前の画像を得たことがあるため、
  単に `refresh()` を増やす方法へ戻さない。
- PNGは `MImage.readFromFile()` で読み、`pixels()` のポインタから
  `ctypes.string_at(..., width * height * 4)` でRGBAを取得する。
- 黒いReference線と透明な背景はRGBが同じになる場合があるため、画像全体の一致や背景判定にはAlphaも含める。
  線が見えることを先に確認し、空の画像同士の一致を成功と扱わない。
- カメラ・ズーム・背景・アンチエイリアス・表示種別を固定する。
  矢印内部の線を判定するときは、Arrow3Dの別の面や辺が同じpixelへ投影されない視点を使う。
- GuideLineの色・接続を測る点は、本体の辺、Partの中心線、ColorCornerCubeの小四角に
  隠れない位置を選ぶ。GuideLineのON/OFFを比較し、既存の線や面を新しいガイドと誤認しない。
  Templateの選択確認では、ガイドだけをクリックした場合と本体の通常線をクリックした場合を分ける。

## DG, Serial, And Parallel

Evaluation Manager の問題を切り分けるときは、同じ scene と入力列を DG、Serial、
Parallel の順に実行し、出力を比較します。

Python から現在の mode を保存して一時的に切り替える例です。

```python
from maya import cmds

previous_mode = cmds.evaluationManager(query=True, mode=True)[0]
try:
    for mode in ("off", "serial", "parallel"):
        cmds.evaluationManager(mode=mode)
        # input または time を変化させ、output を取得して比較する。
finally:
    cmds.evaluationManager(mode=previous_mode)
```

mode の意味は次の通りです。

| Mode | 確認対象 |
| --- | --- |
| `off` | 従来の DG evaluation、dirty と `compute()` の基礎 |
| `serial` | Evaluation Manager の graph と順序を単一 thread で評価 |
| `parallel` | Evaluation Manager graph の並列実行 |

単に同じ clean output を3回読むだけではテストになりません。mode ごとに input 値、
接続元、または time を変更して対象 branch を dirty にし、最終 output を実際に要求
します。結果は tolerance を明示して比較します。

大量 node のテストでは、すべての output が最終 consumer まで接続されていることを
確認します。未使用 branch は Maya が評価せず、不具合も性能コストも観測できない場合が
あります。

## Cached Playback And Context

DG / Serial / Parallel が一致しても、Cached Playback の background evaluation で
初めて現れる context bug があります。特に、node instance の class member へ「現在の
状態」を保存する実装、global current time を読む実装、context 外の plug value を読む
実装が対象です。

Evaluation Toolkit の Caching Correctness Tests では、次を確認できます。

| Test | 確認対象 |
| --- | --- |
| `DB All` / `DB Shp` | datablock cache と通常の Parallel evaluation の結果比較 |
| `VP2 Sft` / `VP2 Hdw` | VP2 software / hardware cache と通常結果の比較 |
| `BG CC` | background evaluation と通常 evaluation の結果比較 |
| `BG CI AA` | animated attribute の context isolation |
| `BG CI AN` | animated node 全体の context isolation |
| `BG CI SA` | static node を含む広い context isolation |

手動テストでは次の順に確認します。

1. Cached Playback を無効にし、Parallel mode の baseline output を記録する。
2. Evaluation Cache を有効にし、playback fill で全 frame を cache する。
3. 同じ frame 列の output が baseline と一致することを確認する。
4. input animation の一部を変更し、必要な時間範囲が invalidation されることを確認する。
5. background fill を有効にし、Maya の current frame と異なる frame を cache させる。
6. fill 完了後の結果、scrub、逆再生、再度の input 変更を確認する。

単純な算術 node でも、animated upstream へ接続した scene を使います。time に依存しない
固定値だけの node では background context の違いを十分に通過できません。

Maya 2025 の `MPxNode::getCacheSetup()` は、default では Cached Playback 対応と扱う
一方、その node 自体を default caching point にはしません。テスト時は
Evaluation Toolkit または `cmds.cacheEvaluator(query=True, cachingPoints=True)` で、
実際の caching point を確認します。

## Dirty Propagation Tests

compound node では、親だけでなく各 child を個別に変更します。

```python
node = cmds.createNode("bdDbl3_Multiply")
cmds.setAttr(f"{node}.input1", 2.0, 3.0, 4.0, type="double3")
cmds.setAttr(f"{node}.input2", 5.0, 6.0, 7.0, type="double3")

assert cmds.getAttr(f"{node}.output")[0] == (10.0, 18.0, 28.0)

cmds.setAttr(f"{node}.input1X", 8.0)
assert cmds.getAttr(f"{node}.outputX") == 40.0
```

次に parent / child connection の組み合わせを検証します。

- compound parent -> compound parent
- child -> child
- parent の一部だけ接続し、残りを直接設定
- downstream output child だけを要求

入力変更後も古い結果が返る場合は、次の順に確認します。

1. 変更した input または child が `attributeAffects()` の入力側にあるか。
2. 要求した output または child が出力側にあるか。
3. `compute()` がその要求 plug を受け付けているか。
4. output handle へ書き込み、要求 plug を clean にしているか。
5. Maya 外部の状態を入力として暗黙に参照していないか。

## Sparse Multi Tests

multi attribute では連続 index だけのテストでは不十分です。

```python
node = cmds.createNode("bdDbl3_MultiplyMulti")
cmds.setAttr(f"{node}.input[0]", 2.0, 3.0, 4.0, type="double3")
cmds.setAttr(f"{node}.input[10]", 5.0, 6.0, 7.0, type="double3")

assert cmds.getAttr(f"{node}.output")[0] == (10.0, 18.0, 28.0)
```

追加で次を確認します。

- element が0個のときに単位元を返す。
- logical index `0` が存在しなくても全要素を処理する。
- 中間 element の削除後も残った要素だけで計算する。
- child 単位の接続と値変更が output を dirty にする。
- scene round-trip 後も sparse index と接続が維持される。

## Visual Studio Debugging

1. Debug build を生成する。
2. Maya を起動する。
3. Debug directory の `bdUtilNodes.mll` を絶対 path でロードする。
4. Visual Studio で **Debug > Attach to Process** を開く。
5. `maya.exe` を選び、Native code debugger で attach する。
6. `compute()`、`initialize()`、plug-in entry point へ breakpoint を置く。
7. Maya で input を変更し、output を要求する。

breakpoint が有効にならない場合は次を確認します。

- Maya が Debug directory の `.mll` をロードしている。
- `.mll` と同じ build の `.pdb` が存在する。
- Visual Studio の Modules window で symbol がロードされている。
- 別の staged Release binary が先にロードされていない。

`MStatus` の失敗箇所には、一時的に `status.perror()` を置くと Maya の Script Editor で
API error を確認できます。恒常的な高頻度ログを `compute()` に残すと、性能と Parallel
evaluation に影響するため、調査後に削除します。

## Evaluation Toolkit

Maya の Evaluation Toolkit では evaluation graph、dirty plug、scheduling の状態を
可視化できます。次のような場合に使います。

- 変更した input から期待する output へ dirty が届いているか確認する。
- node が Parallel schedule に分類されているか確認する。
- 予想外に大きな graph が再評価されていないか確認する。
- Serial / Parallel で評価対象が異ならないか確認する。
- caching point、cache memory、background fill の状態を確認する。
- Caching Correctness / Context Correctness test を実行する。

tool の表示は原因そのものではなく Maya が認識している graph です。表示された欠落や
過剰な依存を、`attributeAffects()`、connection、暗黙の外部状態と照合します。

## Performance Measurement

性能を比較するときは、次の条件を固定します。

- Release build を使う。
- 同じ Maya version、scene、node 数、接続構造、入力値を使う。
- graph 構築時間と evaluation 時間を分ける。
- 全 branch の結果を最終 consumer から要求する。
- 計測前に warm-up evaluation を行う。
- 各試行で input または time を変え、対象を dirty にする。
- 複数回計測し、外れ値1回ではなく中央値や分布を見る。
- DG / Serial / Parallel の mode を記録する。
- Python loop や大量の `cmds.getAttr()` の時間を C++ node の計算時間に混ぜない。

固定2入力版と multi 版を比較する場合は、同じ2入力、同じ node 数、同じ downstream
graph で評価します。作成時間と計算時間を別々に記録し、API の使いやすさを犠牲にする
価値がある差かを判断します。

`bdDbl_Multiply` のチェーンと `bdDbl_MultiplyMulti` の再実行可能なベンチマークは次で
実行します。

```powershell
.\scripts\benchmark-native-maya2025.cmd
```

測定条件、境界値、dirty位置による違いは
[bdDbl Multiplication Benchmark](bd-dbl-multiply-benchmark.md) に記録します。

Maya Profiler を使うときは、node 自体の時間だけでなく、evaluation 回数と dirty 範囲も
確認します。1回の `compute()` を数 ns 改善するより、不要な再評価を1回なくす方が
効果的な場合があります。

## Failure Guide

| Symptom | First checks |
| --- | --- |
| `createNode` が unknown type | plug-in の load path、登録名、`registerNode()` の status |
| input 変更後も古い output | `attributeAffects()`、要求 plug 判定、clean 処理 |
| parent は動くが child が更新されない | compound の親・子 dependency と child request |
| DG は正しいが Serial で誤る | Evaluation Manager に見えない依存、外部状態、副作用 |
| Serial は正しいが Parallel で誤る | static/global mutable state、thread-unsafe API、cache |
| Parallel は正しいが Cached Playback で誤る | evaluation context、member state、cache schema / invalidation |
| build は成功するが stage に失敗 | Maya が staged `.mll` をロードしていないか |
| plug-in を unload できない | scene 内にその plug-in の node が残っていないか |
| breakpoint が入らない | 実際の loaded path、PDB、Debug/Release の取り違え |
| 大規模 scene だけ遅い | dirty 範囲、compute 回数、lock、allocation、未使用 branch |

## Before Review

- [ ] Release build が成功する。
- [ ] native targeted test が成功する。
- [ ] default、代表値、parent / child、connection をテストした。
- [ ] multi node は空配列と sparse index をテストした。
- [ ] scene 保存・再読込をテストした。
- [ ] DG、Serial、Parallel で結果が一致する。
- [ ] Cached Playback と background context の結果が一致する。
- [ ] `kParallel` の thread-safety 条件をコード上で確認した。
- [ ] `git diff --check` が成功する。
- [ ] node 名、attribute 名、ID、挙動を関連文書へ反映した。

## Autodesk References

- [Troubleshoot Evaluation Manager correctness](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Customizing/files/GUID-4EDEF082-0EAC-493B-9256-647A8F6BD039.htm)
- [Evaluation Toolkit](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-E22B253D-914B-4056-93F5-755702A6C998.htm)
- [Cached Playback](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Customizing/files/GUID-D3D1DC33-D0CE-4BE3-B287-CDD4DC0B72C3.htm)
- [Using the Evaluation Manager](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Customizing/files/GUID-190D97E7-9AC0-4D67-8A07-1AF3A9DBAF15.htm)
- [loadPlugin command](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/Commands/loadPlugin.html)
- [MArrayDataHandle C++ API Reference](https://help.autodesk.com/cloudhelp/2024/ENU/MAYA-API-REF/cpp_ref/class_m_array_data_handle.html)
