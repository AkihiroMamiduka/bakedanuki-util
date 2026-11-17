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

既定のnative test、full pytest、UI互換性testでは、`bdControllerShape`専用群を
`deselect`します。`verify.cmd -IncludeNative`と`verify.cmd -Release`も同じ対象範囲です。
専用群を含める場合は検証scriptへ`-IncludeControllerShape`を明示します。
pytestを直接呼ぶ場合は`--include-controller-shape`を指定します。

```powershell
.\scripts\verify.cmd -IncludeNative -IncludeControllerShape
.\scripts\test-native-maya2025.cmd -IncludeControllerShape
```

専用テストファイルを明示指定した場合は、そのファイルを追加flagなしで実行できます。
以下の`bdControllerShape`専用テストは、同ノードの開発時に変更範囲に応じて選ぶ対象です。
過去の検証記録にある件数は当時の収集範囲のまま残し、現在の既定範囲とは区別します。
固定Cube研究の契約テストは別枠の`-IncludeCubeResearch`で追加します。

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

### bdControllerShapeの回帰対象

変更した仕様に応じて次の数値テストを選び、描画・選択・フォーカスの変更は下記のGUIテストでも確認します。

| 数値テスト | 主な確認対象 |
| --- | --- |
| [test_bd_controller_fin_axis.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_fin_axis.py) | Finの属性構造と既定表示、Height / WidthScaleの独立した正負・0・履歴、Standardの軸平行とTaperedの高さ基準。静的属性への接続・キー拒否はstatic contractで確認 |
| [test_bd_controller_shape.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_shape.py) / [test_bd_controller_custom_bounds.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_custom_bounds.py) | `boundsMode` の既定Shape、3モード、行列、プレビュー、`viewFit` とCustom Boundsの独立性 |
| [test_bd_controller_cage_straight_edges.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_cage_straight_edges.py) | 元頂点だけを変形した範囲、Circleの既存64サンプル、Template境界を加えても変わらない輪郭 |
| [test_bd_controller_capsule.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_capsule.py) | 端別の半径と倍率、接合面、反転・中心間0・退化、Part・Finと保存再読込 |
| [test_bd_controller_arrow_family.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_arrow_family.py) | Planar / Axial / Spatialの本体構成、横径由来の母体寸法、各オプションと軸交換 |
| [test_bd_controller_node_editor_template.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_node_editor_template.py) | テンプレートとネイティブ属性の対応、66個の表示対象と順序、Finの4属性 |

Finとフォーカスの変更を切り分ける例です。

```powershell
.\scripts\test-pytest-maya2025.cmd -RequirePlugin tests\maya\node\operator\node\dag\shape\test_bd_controller_fin_axis.py tests\maya\node\operator\node\dag\shape\test_bd_controller_shape.py -k "fin or bounds or focus or view_fit or defaults"
```

対象を絞った成功に加え、ネイティブ変更の最終確認では `verify.cmd -IncludeNative` を実行します。
`bdControllerShape`専用群もまとめて確認する場合は`-IncludeControllerShape`を追加します。
GUIの結果は検証したDLLの絶対path・buildと対応付け、配布先へ置くDLLが同じ内容であることも確認します。
一時的なhelperやテスト件数の固定値を再実行手順の前提にせず、以下のGUI実行例と終了コード・JUnit XMLを使います。

## Viewport 2.0描画テスト

`bdControllerShape` の描画比較は次のファイルに分かれています。

| ファイル | 主な確認対象 |
| --- | --- |
| [test_controller_shape_viewport.py](../../../tests/maya/ui/test_controller_shape_viewport.py) | 面の表裏、Part・Fin・GuideLineの接合、軸交換、Template区間、選択・表示種別 |
| [test_controller_shape_wide_surfaces.py](../../../tests/maya/ui/test_controller_shape_wide_surfaces.py) | 立体Wideの帯・開口・選択面、Sphereの混色、幅0、透明線による塗り面の深度欠け |
| [test_controller_shape_display_colors.py](../../../tests/maya/ui/test_controller_shape_display_colors.py) | 無効なoverrideの保存色と、実際の非選択表示・Selection Highlighting OFFの一致 |
| [test_controller_shape_display_cache.py](../../../tests/maya/ui/test_controller_shape_display_cache.py) | 表示4属性の直接編集・Undo/Redo・接続変更・保存再読込・複製後の初回描画、スクラブ・実再生中の更新 |
| [test_controller_shape_wire.py](../../../tests/maya/ui/test_controller_shape_wire.py) | 全32シェイプの親・個体の移動と復帰、選択色、形状・描画経路の切替、接続行列の実再生、複数viewの表示設定の独立性 |
| [test_controller_shape_fill.py](../../../tests/maya/ui/test_controller_shape_fill.py) | 全32シェイプとWide・Part・FinのFill保持描画、描画経路の切替、反転と内側カリング、複数view、Cached Playback ON / OFFの実再生 |
| [test_controller_shape_gear_template.py](../../../tests/maya/ui/test_controller_shape_gear_template.py) | Gearの実長・周期区間、歯先中央の両側、Wideの位相、線と面の独立した選択、他形状による遮蔽 |
| [test_controller_shape_cage_attachments.py](../../../tests/maya/ui/test_controller_shape_cage_attachments.py) | 面倍率で変形した本体とPart・Fin・GuideLineの接合、局所寸法、巻き付けPartとCrossの境界 |
| [test_controller_shape_part_guides.py](../../../tests/maya/ui/test_controller_shape_part_guides.py) | 頂点からArrow先端へつなぐGuideLine、Triangleの折れ線、Partの欠落方向、色付きコーナーの保持 |
| [test_controller_shape_capsule.py](../../../tests/maya/ui/test_controller_shape_capsule.py) | Capsuleの横径由来のキャップ半径・円筒・面倍率、円筒長0でのSphere一致、Wide・Template・Wireframe、両端PartとGuideLine |
| [test_controller_shape_arrow_shapes.py](../../../tests/maya/ui/test_controller_shape_arrow_shapes.py) | Planar・Axial・Spatialの11本体の肩・本体中心と基準半径、母体維持と伸長、接線接合と不要な接合円の省略、面の表裏、Part・Fin・GuideLine・Wide・Template |
| [test_controller_shape_axis_fins.py](../../../tests/maya/ui/test_controller_shape_axis_fins.py) | 元の直線を保つ面変形・Wide・Template、Capsuleの左右独立半球、AxialのMinus起点Guide、Finの軸平行・下降線・独立寸法と高さ0、既定Shapeの `viewFit` とOffsetLine |

形状の仕様と手動で確認する項目は [Controller Shape](controller-shape.md) を参照してください。

このテストは実際のViewport 2.0を持つMaya GUIで実行します。
既定の収集では専用群を`deselect`し、明示実行しても`mayapy`のbatch環境ではskipします。
そのため、`test-ui-maya*.cmd`や`verify.cmd -IncludeNative`の成功だけでは、
`-IncludeControllerShape`を付けた場合も画像比較の成功を確認できません。
`offScreen=True` はplayblastの取得方法であり、GUIを不要にする設定ではありません。

対象バージョンのplug-inをbuild / stageした後、作業中のMayaとは別の空のMaya GUIを起動し、
PythonのScript Editorから次を実行します。テストはsceneを新規作成するため、
必要なsceneや作業状態のない専用プロセスを使用してください。
`repo_root` は実際のcheckoutへ変更します。pytestは `setup-test.cmd` で用意した `.test` を使います。
以下の例でこれらのファイルを実行でき、`build/` 内の一時的な起動helperは必要ありません。

```python
import sys
import tempfile
from pathlib import Path

from maya import utils

repo_root = Path(r"D:\develop\bakedanuki_dev\bakedanuki-util")
sys.path[:0] = [
    str(repo_root / ".test"),
    str(repo_root / "bakedanuki/bakedanuki-util/python"),
    str(repo_root / "tests"),
    str(repo_root / "tests/maya/ui"),
]


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
            str(repo_root / "tests/maya/ui/test_controller_shape_wide_surfaces.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_display_colors.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_display_cache.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_wire.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_fill.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_gear_template.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_cage_attachments.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_part_guides.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_capsule.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_arrow_shapes.py"),
            str(repo_root / "tests/maya/ui/test_controller_shape_axis_fins.py"),
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
`tests` と `tests/maya/ui` のimport pathは、テスト専用の形状設定と共通の画像取得helperに使います。
GuideLineの変更だけを切り分ける場合は、`pytest.main()` の引数へ
`"-k", "guide_line or arrow_tip_connection"` を追加できます。
対象を絞った確認後は、変更範囲に応じて関連する描画テストを実行します。
描画・選択・Templateの共通処理を変更した場合はフィルターを外してこれらのファイルを確認し、
最終の統一検証も行います。

既定では実行中のMayaバージョンに対応した配布先 `.mll` をロードします。
別のbinaryを検証する場合は、Mayaを起動する前に `BD_UTIL_NODES_PLUGIN_PATH` へその絶対pathを指定します。
Maya 2025 / 2026 / 2027の各GUIで同じ手順を使い、pytestの終了コードとJUnit XMLを確認します。
終了コード0に加え、XMLの実行対象とtests・failures・errors・skippedを照合します。
件数はテスト追加で変わるため固定値を成功条件にせず、0件や全件skipをGUI成功と扱いません。
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
- 片面表示の向きを検証するときは、カメラを対象面の外側へ置き、必要に応じてfar clipで反対側の面を除く。
  反転した裏側の面が同じpixelへ映り込むと、面向きの誤りを見逃す場合がある。
  Fill ON/OFFの差と、反転・AxisSwapを組み合わせた両側の面を確認する。
- GuideLineの色・接続を測る点は、本体の辺、Partの中心線、ColorCornerCubeの小四角に
  隠れない位置を選ぶ。GuideLineのON/OFFを比較し、既存の線や面を新しいガイドと誤認しない。
  Templateの選択確認では、ガイドだけをクリックした場合と本体の通常線をクリックした場合を分ける。
- Normal・Template・穴は画素と選択可否をそれぞれ確認し、線選択と面選択を使い分ける。
  色を周辺3×3 pixelから採るhelperと、中心から±2 pixelのクリック矩形があるため、
  境界や別の線をその範囲へ入れない。狭い区間ではズームを上げ、測定点が基準輪郭上にあることも確認する。
- RGBの数値は色管理・表示変換後のPNGと直接一致するとは限らない。
  たとえば混色の成分0.75を8 bit値191に固定せず、同じraw RGBをoverrideに指定した通常Shapeの面を
  同じカメラ・背景・透明度・色管理で撮り、参照色と比較する。
- Selection Highlighting OFFは、選択前に撮った実際の非選択画像と比較する。
  shape・親・祖先・Display Layerの有効なoverride継承と、無効なoverrideに保存されたRGB色・index色を分けて確認する。
  Maya 2025のprobeでは `MFnDagNode::drawOverrideColor()` がoverride無効時にも保存RGB色を返したため、
  採用前に `MDagPath::getDrawOverrideInfo().fOverrideEnabled` で実効状態を確認する。
- 不透明なTemplate面に通常線が隠れる場合は、同一深度の競合を確認する。
  面には `MRenderItem::sDormantFilledDepthPriority`、線には `sDormantWireDepthPriority` を使い、
  状態がリセットされる各 `beginDrawable()` の後で指定する。
  `shapeDrawOnTop=false` で前方の不透明な別形状が線と面を遮ることも確認する。

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

### bdControllerShapeの面内Scaleと描画キャッシュ

`bdControllerShape` の形状調整は直接編集専用です。親・子の変更通知による
描画キャッシュの更新と、入力接続・キーの拒否を確認します。
`MNodeMessage` は親への直接設定を親だけに通知する場合があります。実装上の経路は
[面内Scaleの保守](controller-shape.md#基準空間の面内scaleを保守するとき) を参照してください。

`shape.shapeBaseSpace1stAxisPlusScale.set(0.5, 1.5)` は現在の共通PlugOperatorで子ごとの
modifier操作を積みます。この経路と、Mayaの `setAttr(..., type="double2")` による
親への直接設定は分けて検証します。

1. `boundingBox()` を一度取得してキャッシュを作る。範囲が変わる値を使い、親の一括設定では両成分、
   子の単独設定では対象成分だけが更新され、もう一方が保持されることを確認する。
2. 親と子を直接編集し、Undo/Redo・保存再読込後も値と範囲を確認する。
3. 親・子への `connectAttr()`、`MDGModifier` の入力接続を拒否し、明示的なキー設定でもanimCurve入力を作らないことを確認する。
4. Maya GUIで親の直接編集とUndoを行い、画素と必要な選択範囲が更新されるか確認する。
5. `shapeAnimationTransformMatrix` の接続と接続元の数値属性のキー、表示属性・Bounds設定の接続とキーによる動的更新を確認する。

テスト用のdynamic `double2` は、親と両子の `addAttr()` を完了してから子へ値・キー・接続を設定します。
子を1つだけ追加した途中状態で操作すると、属性が見つからないことがあります。

属性構造・API・キャッシュは
[test_bd_controller_base_space_face_scale.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_base_space_face_scale.py)、
静的属性の入力接続・キー拒否と直接編集の履歴は
[test_bd_controller_static_contract.py](../../../tests/maya/node/operator/node/dag/shape/test_bd_controller_static_contract.py)、
実描画での親設定とUndoは
[test_controller_shape_cage_attachments.py](../../../tests/maya/ui/test_controller_shape_cage_attachments.py)
で確認します。これらの入力経路がテストで実際に実行されていることを確認してください。

### bdControllerShapeのindexed描画データ

2026-11-10時点の描画データは、連続する同styleの2点ストロークをまとめた線群と、
FillPartごとにbit同一の座標を共有します。論理プリミティブ数・分割数・描画順は維持します。
形状生成用の配列と、描画用の一意な座標・静的index列を区別して確認してください。

- indexを展開した線分・三角形とその順序、重複数、style・marker・singleSided、boundsが
  共有前の独立した参照計算と一致する。`MPoint` のx・y・z・wをbit単位で比較し、
  signed zero・NaN payload・wが異なる点を統合しない。長い `lineStrip` の座標と分割を保つ。
- `shapeAnimationTransformMatrix` の正・負・ゼロの行列式、シアー、射影変換を確認する。
  片面Fillの逆向きindex切替と、退化・輪郭付近のカリングfallbackが同じ3点・演算順を使う。
  個別には射影変換を含み、合成するとaffineに見える組合せもfallbackを通す。
- 実GUIで通常・Xray・太線・半透明、Normal / Templateの色と選択、Wireframeへの切替を比較する。
  boundsの一致だけで画像・選択の一致を判断せず、前述の描画テストを使って確認する。
- 親transformだけの変更では基準座標と行列適用後の座標を再生成せず、
  必要な可視indexを更新する。カメラ移動、選択色、表示属性の変更にも追従する。

描画データの保持には `MPxSubSceneOverride::areUIDrawablesDirty()` を使います。
各viewで形状・可視面・表示属性を比較し、変更がある場合だけUI描画データを再提出します。
通常refreshの最初のpostRender画像で、複数viewの片面Fillと色、親・shape・layerの
非表示と復帰、viewportとoverrideLODのBounding Box表示を確認してください。
`test_controller_shape_viewport.py` の `retained_ui` テストは非表示とBounding Boxの回帰を扱います。
mayapyではskipするため、統一検証の成功とは別に実GUIでの実行が必要です。
仕様と測定段階の区別は [処理負荷の測定](controller-shape.md#処理負荷の測定) を参照してください。

### 保持UIのversion別確認（2026-11-12）

Maya 2026 / 2027の通常Release DLLを、それぞれ同versionの旧DLLと比較しました。
Maya 2025で確認した本体ソースを維持し、DAG instanceではなく各transformに独立したshapeを置いています。
画像は通常更新の対象ViewportのpostRender内で取得し、画像取得前の強制refreshで補修しません。

| 確認対象 | 各versionの結果 |
| --- | --- |
| Cube / Sphere Fillの表示・カメラ・色・表示切替 | 80操作、初期画像を含む82画像が旧版と一致。対象とmainの両viewで実postRenderを記録 |
| Bounds、非表示と復帰、Sphereのviewport / override Bounding Box | 36操作、初期画像を含む37画像が旧版と一致 |
| 通常 / Bounding Boxの実マウス選択 | 各4件、計8件成功。クリック・矩形は選択、Template / Referenceは非選択 |
| Cube / Sphere Fillの親TRS・行列更新・再生 | 72操作と4実再生が成功、初期を含む74比較画像が一致 |
| Cached Playback OFF / ON | `syncOnly` は60操作・8実再生・64画像、`syncAsync` は30操作・4実再生・32画像が一致 |
| `retained_ui` の実GUI回帰 | 非表示と復帰、SphereのBounding Boxと復帰の4件が成功。mayapyでのskipとは別に確認 |

Cached Playbackでは設定ONだけでなくcache状態と復元記録も保存します。
親transformの復元経路と、`composeMatrix`・shape自身が既定のcaching pointではない経路を区別し、
後者の再生成功を「shape自身のcache復元成功」とは扱いません。
2026 / 2027では通常DLLの時間と実画像を確認しており、2025の別診断DLLのnative回数を転用しません。

Module経由の起動確認と後続の検証・速度計測では、候補DLLは正式配布先の
`plug-ins/maya2026` / `plug-ins/maya2027` と既存の `bd_util.mod` を使い、
旧DLLは保存archiveを指す検証専用moduleでロードしています。
2026の初期表示・選択・Fill検証はbuild先の候補DLLを使い、正式配布先とのSHA256一致を確認しています。
実load path・SHA256・Maya / plug-in API versionを照合し、trustやセキュリティ設定は変更しません。
同version別processの通常DLLによるABBA計時と限界は
[追加比較](controller-shape.md#maya-2026--2027での追加比較2026-11-12) を参照してください。

2026 / 2027の統一検証は終了コード0です。2027の当初の実行では、
nativeテストとfull pytestのassert完了後にprocessが `0xC0000374` で終了しました。
コマンドテストfixtureの登録・解除寿命を共有した版で、本体ソースを変えずに再検証し、
native・full pytest・UIと差分確認まで正常終了しました。
旧失敗の記録は保持し、この再検証だけで原因やMaya固有の不具合を断定しません。

### 表示設定キャッシュのMaya 2026確認（2026-11-12）

前節の保持UI版に表示4属性のキャッシュを追加した版を、Maya 2026.3.3
（Maya / plug-in API `20260303`）で確認しました。同版の旧DLL `0c610309` と新DLL
`579e6400` を別processで比較し、両版とも正式配布先と既存の `bd_util.mod` を使っています。
実load path・SHA256・API版を照合し、trustやセキュリティ設定は変更していません。

GUI回帰は旧・新とも42件成功しました。各313画像のうち、名前を対応させた静止281画像の
寸法・RGBAが完全一致し、実再生32画像は4属性それぞれの2姿勢の集合が一致しています。
30件は対象panelの通常postRender、既存の色比較12件はplayblastによる取得です。
必須の機能guard281件も全件成立しました。線幅のquick gateでは通常10操作と実再生4条件
（各9画像）が成功し、再生中の未接続値の直接設定と接続・切断も追従しました。

Cube 1個で4属性のCached Playbackを標準EVAL規則・`syncOnly` で確認し、CacheOFF参照、CacheONの
初回構築・2周目再生、逆向きスクラブを分けています。全属性で表示挙動が成功し、
1–9フレームのcache範囲と、上流 `displayDriver` transformの直接復元を各属性で
2周目7回・逆スクラブ8回確認しました。下流のcompose / decomposeは再計算され、
numeric utility・animCurve・locator自身の直接復元は確認していません。
このため `functional_behavior_passed=true` と `cache_scope_complete=false` を分離し、
厳格なgateの失敗・各終了コード1はそのまま保持します。見た目の成功をnumeric直接復元の
成功や、通常の終了コード0へ読み替えません。

通常DLLによる実再生ABBAの結果と条件は
[Maya 2026での表示設定キャッシュ比較](controller-shape.md#表示設定キャッシュのmaya-2026確認2026-11-12) を参照してください。
本節はGUI・Cacheの検証範囲と実再生比較を示します。統一検証の結果は
[表示設定キャッシュ版の統一検証](#表示設定キャッシュ版の統一検証2026-11-12) を参照してください。

### 表示設定キャッシュのMaya 2027確認（2026-11-12）

Maya 2027.2（Maya / plug-in API `20270200`）で、同版の旧DLL `4d74bc19` と新DLL
`59c0fd5b` に同じ42件のGUI回帰を実行し、両版とも正常終了しました。各313画像を取得し、
静止281画像の名前・寸法・RGBAが完全一致、実再生32画像は4属性それぞれの2姿勢の集合が
一致しています。両版の必須機能guard281件は全件成立し、scene cleanupも完了しました。
通常postRender30件と既存playblast12件を区別し、再生のcallback連番を別process間の
厳密なフレーム対応とは扱いません。
線幅のquick gateも通常10操作・実再生4条件（各9画像・2状態）が成功し、不一致は0、
必須view guard15件も全件成立しました。再生中の未接続値の直接設定と接続・切断に追従しています。

Cube 1個の4属性を標準EVAL規則・`syncOnly` で確認し、計152画像と8実再生、逆スクラブ32時刻で
CacheOFF参照へ追従しました。各属性で1–9フレームのcache範囲と、上流 `displayDriver`
transformの直接復元を2周目7回・逆スクラブ8回記録しています。compose / decomposeは
再計算され、numeric utility・animCurve・locator自身の直接復元は確認していません。
4属性とも表示挙動は成功ですが、厳格なnumeric復元gateは未成立で、各終了コード1を保持します。

正式配布先・既存の `bd_util.mod` と実load SHA256・API版を照合し、新DLLに対応する保存済み
本体6ソースはMaya 2025受入版と同一内容です。同版内の通常DLL実再生ABBAと限界は
[Maya 2027の表示設定キャッシュ比較](controller-shape.md#表示設定キャッシュのmaya-2027確認2026-11-12) を参照してください。
本節の結果はGUI・Cache確認と条件を固定した実再生比較の範囲です。統一検証の結果は次節を参照してください。

### 表示設定キャッシュ版の統一検証（2026-11-12）

正式配布先の今回の新版DLLを使い、統一入口をMaya版ごとに実行しました。

```powershell
.\scripts\verify.cmd -IncludeNative -MayaVersion 2026
.\scripts\verify.cmd -IncludeNative -MayaVersion 2027
```

両版とも実processの終了コード0を確認しました。Blackは4809ファイル変更不要、
Pyrightはerror・warningとも0で、native build / stageと差分確認も成功しています。

| Maya | native | full pytest | Qt UI | Maya UI |
| --- | ---: | ---: | ---: | ---: |
| 2026 | 11765 passed | 19080 passed / 2392 skipped | 1195 passed | 1035 passed / 1310 skipped |
| 2027 | 11765 passed | 19080 passed / 2392 skipped | 1195 passed | 1035 passed / 1310 skipped |

実Viewportが必要な画像テストのbatch実行時skipと、前述の各版42件の実GUI成功は区別します。
Cached Playbackの厳格なnumeric復元gateの終了コード1も、今回の統一検証の終了コード0とは別の結果として保持します。

### Fill保持描画のMaya 2025確認（2026-11-15〜16）

`BdControllerShapeFill.inc` の本体統合を、Maya 2025で先に確認しました。
この初期検証は2025に限定しました。後続の2026 / 2027への展開は、版別の確認として後述します。
試作の環境変数・health command・計測counterは本体へ追加しません。

通常のGUI更新では全32基本形状に加え、Wide・Part・Fin・軸色・常設marker、
太線・透明線・DrawOnTop等の従来描画との往復、片面／両面、親／静的形状／接続行列の反転、
初回から負の親行列、不透明面の内側、独立した2 view、Selection Highlighting OFFと
階層／Display Layerのoverride色を確認しました。
実再生は親と `shapeAnimationTransformMatrix` の接続元へ2姿勢のstep keyを設定し、
Cached Playback ON / OFFで2回ずつ再生します。

開発記録は `build/controller_performance/fill_production_20261115/` に保存します。
全74条件の機能assertは成功し、552固定画像のうち545画像は従来版とRGBAが完全一致しました。
残る7画像はColorSphereとColorCubeの色境界の合計23画素で、alphaと描画範囲は一致します。
実再生8条件の姿勢集合は一致しています。
厳密比較のexit 1は原本のまま残し、無条件の画像許容値へ置き換えません。
`visual_acceptance_v6.json` に視認可能な形状・挙動を維持する判断と、その限定範囲を記録しています。
複数色の半透明面とPart / Finの併用は、従来の混色順を維持するためUI描画へ戻します。

実入力はCornerの塗りmarkerクリック、輪郭クリック、空白・範囲選択、Template / Referenceの
非選択、MoveハンドルのdragとUndoを確認します。10段階の操作で座標・選択・画像が復元しました。
この入力fixtureの終了は強制自己終了のため、通常終了の証拠には含めません。
別fixtureでnode削除・file new・unload / reloadを2回繰り返し、最後の実表示後に直接 `cmds.quit` を要求します。
成功判定にはPython launcherとMaya processの実終了を必要とし、要求直前のJSON成功だけでは判定しません。
本体v6で記録した約427秒／440秒の終了時間は、終了処理の性能値として使用しません。
ユーザーから、検証用Mayaの終了時にMASHの `userSetup.py` に対する
`Secure UserSetup Checksum verification` が残っているとの報告がありました。
検証用の新規profileには、通常profileに保存されているMASHのchecksum記録がありません。
確認待ちが混ざった可能性があるため、実終了コード0という事実と、自動での終了確認を区別します。
プラグイン未ロードの標準meshでもrefreshと終了要求が成功し、
ユーザーが当該確認画面でNoを選んだ後に実終了コード0へ達しました。
これは本人の確認を含む終了であり、自動での通常終了成功やDLL起因の否定には使いません。
セキュリティ設定や保存済みchecksumを変更・コピーして回避せず、画面の確認はユーザーが行います。

新規profileの `quit(abort=True)` だけでは、scene保存確認とMASHのchecksum確認が残りました。
通常profileを直接読む別試験ではchecksum確認は出ませんでしたが、
`force=True, abort=True` でもscene保存確認が残り、Mayaが通常の `userPrefs.mel` を再保存しました。
元ファイルとSHAが異なり長さは1byte減りました。元原本と一致するbackupがなく、変更内容を特定できず元へ戻せていません。
この方式を定常検証へ採用せず、以後は専用profileを使います。詳細は `normal_profile_guard.json` に記録します。
これらの終了方法の試験は、Fill本体・機能fixture・画像比較の判定を変更していません。

最終検証は統一入口 `scripts/verify.cmd -IncludeNative -MayaVersion 2025` が終了コード0で成功しました。
Black・Pyright・2025 buildに加え、native 11,765件、full pytest 19,080件、
Qt UI 1,195件、Maya UI 1,035件が成功しています。
fullの2,553件とMaya UIの1,471件のskipはUI配下で、実Viewport描画をbatchで実行した結果には含めません。
GUI 74条件と厳密画像比較のexit 1は別証拠のまま保持します。
logと `unified_verification_maya2025_v6.json` を開発記録へ保存しています。
速度は同一条件の独立processで比較し、scriptによる回転とrefreshのwall時間を
HUD FPS・実マウスdrag・GPU単体時間・実再生速度と混同しません。
2形状それぞれの旧→新→新→旧の計8processと、通常profileを使わない専用設定で計測しています。
速度計測の強制自己終了は、通常終了の解放や確認画面の有無を検証する手順とは区別します。

### Fill OFF早期除外のMaya 2025確認（2026-11-16）

面のない形状に対するFill描画可否の照会を入口で省く修正版 `f7db2774` を確認しました。
`shapeFill` だけを見て省略せず、常設マーカー等の面がある場合は既存の判定を続けます。
描画itemの停止処理は維持し、Fill ON / OFFや従来描画との切替時の後片付けは省きません。
形状生成・キャッシュ・アニメーション行列、属性・callbackは変更していません。

専用profileのGUIで全74機能条件が成功しました。
前記のFill本体v6 `a6fc48fd` と修正版の552固定画像はRGBAが完全一致し、
実再生8条件の姿勢集合も一致しました。
比較元の古いUI版との厳密画像gateのexit 1と、今回のv6対修正版の一致は別々の記録として保持します。
`functional_fastreject_v1_audit.json` にfixtureの機能部分の同一性と画像の照合結果を記録しています。

実入力では、輪郭・常設markerのクリック、空白・範囲選択、Template / Reference、
形状切替、Moveハンドルdrag、Undoの10段階が成功しました。
Undo後の選択・姿勢・tool・画像は復元しました。
ユーザー中断で入力前に止まった初回runは成功に含めず、別profileの再実行を採用しています。
この再実行の原本は `wire_shapes_20261113/harness/runs/pick_production2025_fastreject_v1_resume1/`、
監査結果は今回taskの `native_pick_C_audit.json` です。

修正版の統一入口 `scripts/verify.cmd -IncludeNative -MayaVersion 2025` は終了コード0でした。
Black・Pyright・2025 build、native 11,765件、full pytest 19,080件、
Qt UI 1,195件、Maya UI 1,035件が成功しています。
fullの2,553件とMaya UIの1,471件のUI skipは、実GUI確認とは分けます。
`verification_exit.json` と `verification_audit.json` で終了コード・log・source・DLLを対応付けています。

速度は線のみGPU版・Fill保持描画版・修正版をA→B→C→C→B→Aの6独立processで比較しました。
各processのCube 1,000個が最初からFill OFF・DrawOnTop OFFであることを確認し、
DLL・module/API・入力source・profile・配置・選択・view・表示設定・実終了を照合します。
結果と測定範囲は [Fill OFFの比較](controller-shape.md) を参照してください。
通常profileを使わず、終了は強制自己終了とし、通常終了や設定保存の検証には含めません。
この2025のFill OFF比較では、Maya 2026 / 2027を更新・検証対象に含めていません。
開発記録は `build/controller_performance/fill_off_20261116/` に保存します。

### Fillの既定値とMaya 2026 / 2027対応（2026-11-16）

2025でのユーザー操作確認後、3版の `shapeFillTransparency` の既定値を `0`（不透明）へ変更しました。
native描画データの初期値・読取失敗時の不透明度は `1`、生成Python Fieldの透明度は `0` とし、
新規ノードとUndoで既定値へ戻るテストも揃えています。
新旧DLLの画像比較では、半透明は `0.85`、不透明は `0` を明示し、
何も設定していない新規ノードの既定値確認と分けます。

2026 / 2027は各74機能条件と実入力10段階が成功しました。
通常の表示切替・反転・2 view・Cached Playback ON / OFFでの実再生を確認しています。
旧版との厳密画像比較で残る7画像・合計23画素の色境界差は、既存2025の受容署名と一致しました。
旧DLL側のoverride色の6条件の不具合と、新DLL側の8条件の表示判定成功も別に記録します。
厳密比較のexit 1は原本を保持し、無条件の画像許容値や統一検証の成功へ読み替えません。

初回の版別統一入口は3版とも、native 11,765件、full pytest 19,080件、
Qt UI 1,195件、Maya UI 1,035件が成功しました。
batch / offscreenのUI skipは実Viewport確認と区別します。
旧GUIの線と暗い面の輝度差を確認する3関数には、半透明値 `0.85` を明示しました。
閾値とassertは変更せず、その後のMaya 2025最終統一再検証も終了コード0でした。
native 11,765件、full pytest 19,080件、Qt UI 1,195件、Maya UI 1,035件が成功しています。

事前の既定値確認用ノードを作らない構成では、2026 / 2027ともnode削除・file new・
unload / reloadを各2回行う9段階が、元の厳密なblank判定を含めて成功しました。
最後のlive描画も確認しています。終了は強制自己終了で、通常の自然終了は試していません。

事前の確認用ノードを作成・削除する2026の構成では、loop対象の削除後に原点の青い線が残り、
blank判定は失敗しました。確認用ノードを原点から離しても同じ原点の線が残ります。
旧26 Wire版 `7f763843` でも同じ3画像・RGBAと失敗が再現したため、
新Fill固有の回帰とは分類しません。ただし根因と後続描画への持続性は未解決で、
失敗原本を正常な解放や解決済みの記録に置き換えません。

速度は2026 / 2027それぞれ旧→新→新→旧の4独立processで比較し、各DLL2起動・各processの条件／操作ごと5試行を監査しました。
Cube 1,000個を同じprocess内でFill OFF→不透明0→半透明0.85の順に測り、各条件を独立起動とは数えません。
個体／上位操作の回転設定と強制VP2 refreshのwall時間で、HUD・drag・実再生FPSやGPU単体時間とは区別します。
不透明は個体約27〜30%・上位約73%短く、半透明は個体約9〜11%長く・上位約58〜60%短い結果でした。
Fill OFFは約−1.2〜+2.6%の小幅な増減で、2027の個体約1.4%・上位約2.6%の増加も残る差として扱います。
起動変動を含む記述統計で、小さな回帰傾向を排除せず、統計的有意差や全条件での改善は主張しません。
2026の旧版A2初回は開始前のフォーカス確認不成立で数値閲覧前に除外し、新規processのA2再実行を採用しました。
除外原本と `perf2026_A2_protocol_deviation.json` を保持しています。
測定結果と条件表は [版別Fillの速度比較](controller-shape.md) を参照し、
`performance2026_audit.json` / `performance2027_audit.json` にsource・DLL・表示条件・前後guard・実終了を対応付けます。
測定後は3版の正式DLLを最終候補へ戻しています。計測の終了は強制自己終了で、通常終了の証明には使いません。
開発記録と失敗原本は `build/controller_performance/fill_cross_versions_20261116/` に保存します。

### Controller Shapeの検証を再開するとき

2026-11-16に3版のユーザー操作確認が完了しました。次回は
[開発の区切りと再開事項](controller-shape.md#開発の区切りと再開事項2026-11-16) を入口とし、
過去の実装・測定記録と、その後に変更する版の結果を分けます。

- 比較元のDLLは新しいbuildやstageの前に保存し、source revision・未commit差分・DLLのSHA256・Maya / plug-in API版を対応付ける。
- 専用profileと正式配布先の `.mod` を使う。通常profileを再利用せず、計測中は他のMaya検証や重い処理を並行実行しない。
- 新規ノードの既定値確認と表示比較を分け、Fill OFF・不透明0・半透明0.85を明示する。個体操作と親全体操作も別々に評価する。
- 削除後の線残りを調べる場合は、事前ノードの作成・削除の有無、離した位置での作成、旧／新版を別条件で記録する。最初の通常postRenderの失敗を追加refreshで成功に置き換えず、後続描画の観測は別に残す。

本文で参照する `build/` 配下のhelper・DLL archive・JSON・画像・logはGit管理外です。
別checkoutに存在する前提にせず、比較DLL・凍結sourceとrunner・raw結果・実終了記録・画像・受容／除外判断の原本は別途保管します。
原本がない場合、過去の集計値や成功記録を新しいDLLの検証証拠へ転用せず、同じ条件で取得し直します。
新しいrunでは使用source・実load DLL・表示条件・実終了を改めて記録し、失敗・除外したrunも保持してください。

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

`bdControllerShape` は `scripts/benchmark_controller_shape.py` で独立したMaya GUIを起動し、
静止・親transform・再生・形状行列を分けて測定します。結果JSONでは実loadと保存archiveの
path・SHA256、EM、Cached Playback無効、単位、Viewport実寸、全配置が画面内に収まる条件、
空でない画像、試行ごとの有限な時間を照合します。GPU単独の時間やdraw call数とは区別します。
`--foreground` を両runに揃える場合は、Qtの表示・アクティブ・非最小化と
application状態を計測区間の前後で確認し、未アクティブのまま測定を続けません。
`--adaptive-heavy` の有無と各個数のframes / trials / warmupも一致させます。
保存画像のRGBA差は確認対象として列挙し、背景だけの画像同士の一致を成功にしません。
最初のキャッシュ最適化（index化前）と最終indexed版の結果は別の比較として記録します。

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
