# 固定 Cube の描画速度研究

`bdShpL_Cube` はローカル座標が各軸 `±0.5 cm` の線のみ Cube です。
8 頂点と重複のない 12 辺を固定し、独自属性を追加しません。
親 DAG 階層の最終行列を反映し、pivot、rotateAxis、shear、jointOrient、
offsetParentMatrix を Maya 標準の計算へ委譲します。
頂点を TRS に分解した値で作り直す処理はありません。

## 研究用 DLL

| DLL | 描画方式 |
| --- | --- |
| `bdShpCubeGeometry.mll` | MPxLocatorNode + MPxGeometryOverride |
| `bdShpCubeSubScene.mll` | MPxLocatorNode + MPxSubSceneOverride |

どちらも同じ node type と `MTypeId=0x00142720` の代替実装です。
採用した Geometry 版は `bdUtilNodes` に統合しています。本体と研究用 Geometry は
同じノード・描画ソースをコンパイルします。上記の研究用 DLL と本体は同じ ID を
登録するため、同じ Maya process に同時ロードしません。
研究用 DLL / Baseline / Candidate は比較用で、package には配置しません。
配布先の更新には `scripts/build-native-maya<version>.cmd` を使用します。

Maya を再起動し、Python の Script Editor で試せます。

```python
from maya import cmds

cmds.loadPlugin("bdUtilNodes", quiet=True)
ctrl = cmds.createNode("transform", name="cube_ctrl")
cmds.createNode("bdShpL_Cube", parent=ctrl, name="cube_ctrlShape")
cmds.select(ctrl)
```

既に別配置の同プラグインをロードしている場合、`loadPlugin()` だけでは切り替わりません。
既存シーンを保存して Maya を再起動し、
`cmds.pluginInfo("bdUtilNodes", query=True, path=True)` で配布先を確認します。
NodeOperator の生成済み API と型補完にも `bdShpL_Cube` を追加しています。

通常の細線、不透明、標準 depth、オブジェクト選択、選択色、visibility、
Template / Reference を初期対象とします。独立した transform / shape を使用し、
DAG instance、component 編集、線幅、透明度、DrawOnTop、独自の形状変形は対象外です。
継承された locator の `localPosition` / `localScale` も固定形状には適用しません。
表示条件を広げる場合は、速度だけでなく基本操作・表示の対応範囲も比較します。
Selection Highlighting OFF でも選択色が残る既存制約があります。
通常の選択色、親・display layer の表示／色、キーによる色・可視性、
`hideOnPlayback` による再生中の非表示と復元は追加の GUI gate で確認しています。

Geometry 版は Maya の geometry 管理を使い、通常の更新で固定 stream / index の再生成を省きます。
Maya が geometry を再要求した場合は再生成します。
SubScene 版は vertex / index buffer を renderer ごとに共有し、行列を変更時だけ更新します。
両版とも同色の stock shader を共有します。
consolidation の指定は実際の draw call 削減を証明するものではありません。

## ビルドと契約検証

repository root から実行します。研究用の生成物は `build/fixed_cube/` へ保存し、
配布用 `bdUtilNodes` の生成物とは分離します。

```powershell
.\scripts\build-native-maya2025.cmd
.\native\maya\experiments\fixed_cube\check.ps1 -MayaVersion 2025
```

`check.ps1` は両 DLL を別の mayapy へロードし、ID / 属性 / bbox / draw classification、
transform と joint の親行列、複製と削除 Undo / Redo、保存・再読込を検証します。
さらに、配布先 `bdUtilNodes` と build の SHA256 が一致することを確認し、
隔離した設定の mayapy から `.mod` を通してプラグイン名でロードします。
実際のロード先・Module path・API version を照合し、同じ 6 件の契約を実行します。
配布先が古い場合や存在しない場合は失敗させ、通常の native build で更新します。
6件の契約は通常テストと研究ランナーで共有し、実装の分岐による検証漏れを防ぎます。
batch の成功は Viewport 描画やクリック選択の成功を意味しません。

最終検証の統一入口です。3 version の研究用 build / 契約検証も含みます。

```powershell
.\scripts\verify.cmd -IncludeNative -IncludeCubeResearch
```

`bdControllerShape`専用テストは既定検証から除外します。本体 Cube の契約は通常の
native test に含み、研究用 DLL と Module ロードの契約を `-IncludeCubeResearch`で追加します。
比較用に`bdControllerShape`を描画する
性能試験と、同ノードの専用回帰テストを含める`-IncludeControllerShape`は独立しています。

2026-11-17の検証範囲変更前の記録では、Maya 2025の既存native testは11,765件成功し、
Maya 2026の実行中に専用群を既定から外す方針へ変更したため中断しました。
`build/fixed_cube/verify_all.log`は統一検証全体の成功や研究DLLの検証完了を示す記録ではありません。
変更後の検証結果は、新しい既定範囲で再実行した結果として区別します。

## 性能評価

GUI runner の `launch.ps1` は mode ごとに独立した Maya process を使います。
各版の profile は `build/fixed_cube/profiles/maya<version>` に固定し、
ユーザーが手動でレビュー・保存した同じ設定を使います。
起動前・実行中・終了後の設定ファイルの有無と SHA256 を記録し、
正式比較の途中で設定が変わった場合は結果を採用しません。
`geometry` / `subscene` / `controller` / `curve` の 4 条件を、同じ版・配置数・
画面・選択・描画設定・暖機・試行数で比較します。
`curve` は履歴のない degree 1 の単一 open shape で全 12 辺を表現します。
最短の経路として 3 辺を重複する 15 区間・16 CV を使います。
shape の DAG instance と同じ vertex buffer の共有は区別します。

初期の主要指標は、1 個体と全体の親の回転設定 + 強制 refresh の wall ms / update です。
`individual` は配置した全個体のうち 1 個を回転し、`group` は全体の親を回転します。
静止 refresh、カメラ操作、実再生は別々の条件にします。
これは GPU 単体時間やマウス drag の HUD FPS ではありません。
DLL の SHA256、Maya / API / GPU、view、配置数、設定、試行値、画像、終了結果を保存します。
複数の独立起動と順序の入替で起動差を確認してから比較を判断します。

```powershell
.\native\maya\experiments\fixed_cube\study.ps1 -OutputDirectory build/fixed_cube/runs/smoke -SmokeOnly
.\native\maya\experiments\fixed_cube\study.ps1 -OutputDirectory build/fixed_cube/runs/study
.\.venv-format\Scripts\python.exe native/maya/experiments/fixed_cube/summarize.py build/fixed_cube/runs/study build/fixed_cube/study_summary.json
```

`study.ps1` は GUI を同時に複数起動せず、既存の Maya GUI がある場合は開始しません。
初期試験は 4 方式各 1 起動、正式試験は順序を反転した計 8 起動です。
正式試験は 1 / 100 / 1,000 個で各 5 操作、36 frame × 5 試行、暖機 8 回です。
結果保存後は試験 process 自身を `TerminateProcess` で終了します。
これは通常終了や resource 解放の検証ではありません。mayapy の契約検証は
明示 unload と `maya.standalone.uninitialize()` 後の通常終了も確認します。

`study.ps1` と `playback_study.ps1` は研究ディレクトリを `source_snapshot` へ保存します。
本体と共有する `BdShpLCubeNode.cpp`、`BdShpLCubeGeometryOverride.cpp`、
`BdShpLCubeNode.h`、`FixedCubeGeometry.h` も `source_snapshot/production_cube` 以下へ
本体内の相対パスを保って保存します。`source_snapshot_manifest.json` に全ファイルの
SHA256 を記録し、各起動の前後で現在のソース・保存済みコピー・manifest の不変を確認します。
測定中は研究ディレクトリと本体側のこの4ファイルを編集しないでください。

実際の DLL は build の固定配置先から読み込み、run 配下のコピーは記録用に保持します。
起動前に実体と archive の SHA256 を照合します。
Maya の `Untrusted Plugin Loading - Security Warning` が表示される場合は、
ユーザー本人が内容を確認し、読み込みを許可してから続行します。
信頼場所の追加やセキュリティ設定の自動変更は行いません。
確認待ちを描画処理の停止と混同せず、次の Maya を重ねて起動しません。
初期の `restart_smoke3/02_geometry` と `restart_geometry_debug1` はこの確認待ちで
timeout となった記録で、描画不具合や性能の測定結果には含めません。

### ユーザーによる信頼場所のレビュー

```powershell
.\native\maya\experiments\fixed_cube\trust_setup.ps1 -MayaVersion 2025
```

この入口は同じ固定 profile の空の Maya と Preferences を開くだけで、
研究プラグインをロードせず、信頼場所を設定しません。
本人が `Security > Plugins > My trusted plugin locations` で
研究 DLL の `build/fixed_cube/maya2025/Release` と、比較用の
`bakedanuki/bakedanuki-util/plug-ins/maya2025` をレビュー・追加し、
Preferences の Save 後に専用 Maya を閉じます。
`Secure plug-in loading` は有効のまま使用します。
2026 / 2027 の GUI を比較するときも、対象版の同じ手順でレビューします。
通常作業用 Maya の設定や、過去の試験 profile の信頼設定をコピーしません。

速度測定前に、非空描画、親変換後の描画、復元、選択・非表示の基本動作を確認します。
親変換の契約テストと、実際の画像に正しく変換が反映されたことは別の検証です。
Fill 専用 `bdShpF_Cube` と Fill + Line `bdShpFL_Cube` は線の研究後に検討します。

## 2026-11-17 の自動検証

最終の `verify.cmd -IncludeNative -IncludeCubeResearch` は終了コード 0 でした。
新しい既定範囲で、3 版それぞれ native 942 件、Qt UI 1,195 件、Maya UI 1,035 件が成功し、
2025 の full pytest は 8,337 件成功・1,082 件 skip・12,297 件 deselect でした。
Controller 専用群は native で各 10,823 件、Maya UI で各 1,471 件を除外しています。
これらの除外をテスト成功件数へ加算しません。
描画方式別の classification 契約を含む研究ノードの契約は、各版・各方式で 6 件、
計 36 件が成功しました。再生改善後の最終ログは `build/fixed_cube/verify_playback_20261117.log`、契約の JUnit は
`build/fixed_cube/contracts/maya<version>/<Geometry|SubScene>/junit.xml` です。
以前の `verify_opt_in_all.log` は classification 契約を追加する前の計 30 件の記録です。
`verify_final_20261117.log` は初回実装の 36 件、`verify_playback_20261117.log` は
並列更新経路を採用した後の 36 件を含む統一検証で、いずれも実際の終了コードは 0 でした。

初期の SubScene 試験 `trusted_smoke1/03_subscene` は初回描画でクラッシュしました。
SubScene 登録を `drawdb/subscene/bdShpL_Cube` へ修正し、契約テストにも追加しました。
Geometry 登録は `drawdb/geometry/bdShpL_Cube` です。
修正後の `trusted_subscene_gate5` と正式試験では描画・選択・変換に成功しました。
前面ウィンドウや active view が成立しなかった初期試行の時間は比較に含めません。

既存配布 DLL は検証で再生成したものと一致することを確認して Git の内容へ揃え、
検証時の build DLL は `build/native/` に保持しています。

## 2026-11-17 の最初の比較結果

`build/fixed_cube/runs/study_20261117_a` の正式 8 起動は終了コード 0、
`build/fixed_cube/study_20261117_a_summary.json` の監査結果は `audited` です。
Maya 2025.3.3、OpenGL、GeForce GTX 1660 SUPER、956 × 676 の VP2 で測定しました。
同じ専用 profile の設定 SHA256 は開始前から終了後まで一致しました。
以下は 1,000 個の結果です。各方式 2 独立起動 × 5 試行の計 10 試行の中央値を示します。
小さい値ほど短い時間で、単位は ms / requested frame です。

| 条件 | nurbsCurve | Geometry | SubScene | bdControllerShape |
| --- | ---: | ---: | ---: | ---: |
| 静止状態の強制 refresh | 1.758 | 1.682 | 8.365 | 8.784 |
| 1 個体の回転 + refresh | 1.861 | 1.918 | 8.485 | 9.092 |
| 全体の親の回転 + refresh | 8.461 | 8.290 | 12.542 | 14.335 |
| カメラ変更 + refresh | 1.933 | 1.909 | 8.167 | 9.091 |
| 全体の親をキー再生 | 3.301 | 6.557 | 10.999 | 12.509 |

Geometry の curve 比は個体操作で 1.031、全体操作で 0.980、再生で 1.987 でした。
個体操作の process ごとの中央値は Geometry 1.876 / 2.052、curve 1.852 / 1.869、
全体操作は Geometry 8.221 / 8.326、curve 8.500 / 8.411 です。
再生は Geometry 6.574 / 6.484、curve 3.321 / 3.281 でした。
数 % の差を普遍的な優位とは判断しません。1 個では方式差が小さく、
100 個の Geometry も概ね近い範囲ですが、再生は curve 比 1.128 でした。

現状は Geometry 方式を次の研究の基準にします。固定化だけで常に curve より速くなるとは
言えず、SubScene で個体ごとの表示状態と行列を確認する現実装にも利点は見られませんでした。
この比較だけで分岐数・属性数・consolidation のどれが差の原因かは特定できません。
次は再生時の geometry 更新要求・render item 更新・評価との同期を個別に計測し、
変更を 1 点ずつ比較するのが優先です。並列更新の旗だけを変更することは避けます。
初回の Geometry は `supportsEvaluationManagerParallelUpdate()` が `false` でした。
この時点の数値と、下記の再生改善後の数値を同時期の直接比較として混ぜません。

全 run で非空描画、変換の反映、復元画像の一致、画面座標からの選択を確認しました。
選択は `MGlobal.selectFromScreen` による 5 px 矩形で、実マウス drag の試験ではありません。
正面ビューでは辺の投影が重なるため、12 中点の選択成功は各辺の独立した選択の証明では
ありません。別途、`build/fixed_cube/image_audit.json` に画像の独立監査を保存しました。
GDI+ で 128 PNG を復号し、curve との 90 比較、同方式の反復間 60 比較で
色を含む画素が完全一致しました。1 / 100 / 1,000 個の初期配置画像も含みます。
非退化の回転画像では、別計算した 8 頂点と 12 辺の投影位置が全 8 起動で描線に
支持されました。描線の一致も速度比較の根拠に含めています。
物理マウス操作、DAG instance、各種表示条件、Maya 2026 / 2027 の GUI 性能は未検証です。
再生値は開始・停止を含む要求 frame 当たり時間で、GPU 単体時間や HUD FPS ではありません。
世界最速や、すべてのリグ・GPU・Maya 版での性能を保証する結果ではありません。

## 再生時の改善

Geometry 版の `supportsEvaluationManagerParallelUpdate()` を `true`、
`requiresUpdateRenderItems()` を `false` にし、固定形状を Evaluation Manager と
連携する更新経路へ変更しました。worker 側の `updateDG()` は空、
`populateGeometry()` は固定配列からの buffer 準備だけに限定します。
shader cache と表示状態の処理は foreground の `updateRenderItems()` に残し、
共有される `geometryDirty_` は atomic にしました。独自属性は増やしていません。
VP2 Custom Caching と Cached Playback は引き続き無効です。

### 同時期に測り直した比較

`build/fixed_cube/runs/playback_study_20261117_a` の A / B / C / C / B / A の
6 独立起動は終了コード 0、`build/fixed_cube/playback_study_20261117_a_summary.json`
の監査は `audited` でした。A は旧 Geometry、B は改善 Geometry、C は curve です。
版・GPU・viewport・選択・配置数・操作順・暖機・profile は同じ条件で、
各方式 2 起動 × 5 試行の中央値を比較しています。
起動・終了・DLL / source / profile SHA256 と、条件ごとの実描画数も一致を確認しました。
1,000 個配置の結果です。単位は ms / requested frame、小さいほど短時間です。

| 条件 | 旧 Geometry | 改善 Geometry | nurbsCurve |
| --- | ---: | ---: | ---: |
| 静止 refresh | 1.518 | 1.568 | 1.468 |
| 1 個体の回転 + refresh | 1.687 | 1.755 | 1.736 |
| 全体の親の回転 + refresh | 8.062 | 8.249 | 8.148 |
| カメラ変更 + refresh | 1.688 | 1.882 | 1.755 |
| 全体の親をキー再生 | 5.999 | 2.988 | 2.899 |

再生の旧版比は 0.498、curve 比は 1.031 です。要求 frame 当たり時間は約 50.2% 短縮し、
curve と近い範囲へ到達しました。独立起動ごとの再生中央値も、旧版 5.987 / 6.029、
改善版 3.006 / 2.971、curve 2.968 / 2.845 ms でした。
再生中は全方式・全試行で 35 回、他の操作は 36 回の対象 view の postRender を記録しています。
再生の frame 1 は計時前に描画済みなので、36 要求 frame に対して 35 回です。
これは 1 要求 frame = 1 描画を一般保証したものでも、HUD FPS でもありません。

操作系の小さい差は独立起動間のばらつきもあるため、改善・維持を一律には断定しません。
今回のカメラ変更は旧版より約 0.194 ms（11.5%）長く、再生改善との損得として記録します。
1 個・100 個の再生には大きな改善はなく、改善版の curve 比はそれぞれ 0.972 / 1.090 でした。
10 試行は 2 独立起動に従属した試行であり、10 回の独立起動や統計的有意差を意味しません。
全 450 試行の再計算と証跡の独立確認は
`build/fixed_cube/playback_study_20261117_a_independent_review.json` に保存しました。
主ウィンドウの pane 管理状態は計時ごとに記録していません。3 本の診断 trace は各 35 回の
SceneRender でしたが、正式全試行で他 view の描画が 0 だったことを独立に証明するものでは
ありません。GPU 単体値や単一 view 専有の描画時間として扱いません。

保存済み Baseline / Candidate の比較は次の入口で再現できます。
旧版と候補は同じ型名・ID のため同時ロードしません。
Baseline / Candidate の固定 DLL は比較記録用に残し、通常 build は標準の
`bdShpCubeGeometry.mll` を生成します。

```powershell
.\native\maya\experiments\fixed_cube\playback_study.ps1 -OutputDirectory build/fixed_cube/runs/new_playback_study
.\.venv-format\Scripts\python.exe -B native/maya/experiments/fixed_cube/summarize_playback.py build/fixed_cube/runs/new_playback_study build/fixed_cube/new_playback_summary.json
```

`bdShpCubeGeometryBaseline.mll` は初回実装の保存済み DLL で、SHA256 は
`16d90680769e8940ffd8e5507099f751f8ed1a4059d818821128c75c0010528f`、
候補の SHA256 は `64b09ea2108b9da1aacfe8c678632101e03801f15b1db51a76cf914908f3bb7b` です。
通常 build や検証で Baseline / Candidate を上書きしません。
`build.ps1` は既存 Candidate の上書きを拒否します。新規候補には
`-OutputSuffix Research<識別名>` を使い、過去の比較とは別に保存します。
比較開始から終了までは README を含む source directory の全ファイルを固定します。
共有ソース保存に対応した新規比較は manifest の schema 2 を使用します。
旧 schema 1 の証拠・保存済み監査プログラムは変更せず、両 schema とも保存時の
監査プログラムとの SHA256 一致を要求します。旧記録の再確認や、後日ソースを変更した場合は
対象 study の `source_snapshot/summarize_playback.py` を使用してください。
8起動の記録は対応する `source_snapshot/summarize.py` を使用します。結果は新規 JSON へ保存し、
固定 DLL・profile の一致など、元の監査条件を満たす必要があります。

### 診断と表示の確認

`build.ps1 -Profile` は callback の回数・時間を採る診断用 build です。
`launch.ps1 -NativeProfile` / `-MayaProfile` の時間や診断 DLL は正式集計から拒否します。
通常再生の旧版では独自の頂点生成・描画状態更新 callback は 0 回でした。
明示的な `setGeometryDrawDirty()` の対照操作では更新を 1,000 回検出したため、
通常再生の差を細かな表示判定の積み重ねに帰属させる仮説は採用しませんでした。

Maya profiler の区間比較は `build/fixed_cube/profile_playback_path_comparison.json`
に保存しています。旧版で重かった VP2 の準備・描画リスト構築が候補では curve と
同程度になり、描線の Beauty pass 自体の差は小さい結果でした。
これは少数の診断記録で、正式な速度比較とは区別します。
consolidation 無効化は操作・再生とも悪化し、SurfaceShape 化と更新要求だけの変更は
有意な再生改善が見られなかったため、採用していません。

`launch.ps1 -PlaybackGate` は性能計時と別に、対象 postRender 内で画像を取得します。
実再生の frame 2 / 9 / 17 の取得では追加 refresh を行わず、その後の静止参照と比較します。
候補の再生姿勢は curve と一致し、選択色・親／layer の表示・色変更、
キーによる可視性と RGB、再生中の非表示と復元も確認しました。
Selection Highlighting OFF の色だけは旧版・候補とも同じ不一致が残ります。
この拡張 gate の旧版・候補の raw status はその 1 件によって `failed` であり、
すべての表示条件が成功したとは報告しません。
`build/fixed_cube/display_gate_audit.json` では全 222 画像記録を独立に照合し、
旧版と候補の全 74 画像でファイル・RGBA・復号画素の完全一致を確認しました。
curve との差は OFF の 1 画像の色のみで、描線位置は一致しています。
`launch.ps1 -RendererResetGate` では `ogs(reset=True)` 後の同一画像と選択も確認しました。
これらの GUI gate は Maya 2025 / OpenGL の確認で、他版・他 backend の保証ではありません。

## 本体への統合確認（2026-11-17）

`bdUtilNodes` と研究 Geometry が同じ実装を使う状態で、統合 / 独立 / 独立 / 統合の
4独立起動を追加確認しました。Maya 2025 / OpenGL、1 / 100 / 1,000個、各5操作・
36要求frame × 5試行・暖機8回で、全processの終了コードは0でした。
各試行の対象postRenderは再生35回、他操作36回で一致しています。
機能確認を含む最初の2起動は56画像、残り2起動は共通36画像ずつ完全一致でした。
別のGUI確認でも `ogs(reset=True)` 後の画像一致と12辺の画面選択を確認しました。

1,000個の再生は各process中央値を集計して統合2.646 ms、独立2.614 ms（+1.2%）でした。
一方、1個の再生は+17.0%、1,000個の静止refreshは+12.2%で、
すべての条件で統合コストがないとは断定しません。各方式2起動の記述統計であり、
起動差・時間経過の影響を含みます。以前のcurve比較とは別の測定として扱います。
監査は `build/fixed_cube/integration_20261117_audit.json` に保存しました。
この確認は各runのDLL・runner・profileのhashと終了記録を検証していますが、
正式studyのような開始前のsource snapshotは作成していません。

## 追加改善の検討（2026-11-17）

commit `aad506e7` の実装を基準に、操作・再生の診断と
`MPxNode::schedulingType() = kParallel` の候補比較を行いました。
ノードの scheduling と、採用済み GeometryOverride の parallel update は別の設定です。
今回の候補は通常版へ採用していません。研究用マクロを指定した DLL だけに適用します。

Maya 2025 / OpenGL、Cached Playback 無効、共通親の下に独立した transform / shape を
1個または1,000個配置しました。Current / Parallel / curve / curve / Parallel / Current の
6独立起動で、各条件72要求frame × 5試行、暖機8回です。
各processの中央値を集計した1,000個の値は次の通りです（ms / 要求frame、小さいほど短い）。

| 条件 | 現行 | 並列候補 | nurbsCurve |
| --- | ---: | ---: | ---: |
| 静止 refresh | 1.434 | 1.372 | 1.360 |
| 単体回転 + refresh | 1.622 | 1.577 | 1.527 |
| 共通親の回転 + refresh | 7.641 | 7.501 | 7.888 |
| カメラ変更 + refresh | 1.699 | 1.624 | 1.668 |
| 共通親をキー再生 | 3.031 | 3.159 | 2.795 |

親操作の候補差は平均的な集計で -1.8% ですが、前半の組では +0.25%、後半では -3.83% と
方向が揃いません。再生は +4.2%、前後の組でも +1.61% / +6.78% で長くなりました。
1個の親操作・再生では短縮がありましたが、重視する1,000個の操作・再生を
安定して改善する根拠は得られていません。2processずつの記述統計であり、有意差の主張はしません。
再生の一部trialには現行10.265 / 8.969、候補9.180 / 5.865 msの大きい値もあり、
原因は未特定です。全300trialを除外せず保持し、再集計しました。
実描画数は全trialで再生71回、その他72回。HUD FPS・マウスの継続ドラッグ速度とは異なります。
全6起動で親変換の描画反映・12辺の画面選択を通過し、方式間の取得画像も一致しました。

原本は `build/fixed_cube/runs/improvement_study_20261117_a/`、最終監査は
`audit_after_06.json`、独立再集計は
`build/fixed_cube/improvement_20261117_independent_recalculation.json` です。
ソース・DLL・CMake設定・実行設定を保存し、各run前後に固定を確認しています。
今回の監査scriptは実行時の現在ソースも照合するため、このREADMEを含む後日の編集後には
そのまま再実行できません。比較完了時の監査結果とsnapshotを保持し、後日再確認する場合は
保存済み原本を読み取る監査を使ってください。`build/` の記録・専用runnerはGit管理外です。

### 診断から分かったこと

個体・親の回転更新では、計測した独自callbackはすべて0回でした。
再生中も表示更新・頂点生成は0回で、`requiresUpdateRenderItems()` の問い合わせだけが
35,000回（35描画 × 1,000個）ありました。dirty対照では表示更新を1,000回検出しています。
この条件では色・表示判定やshader検索の省略を、継続操作の高速化策とする根拠はありません。
親回転の Maya Profiler では、curveにも同様の表示準備・評価待ちがありました。
主threadの待機とworker、inclusive区間の親子は重複するため加算しません。

shader callbackを追加した描画診断では、親回転・再生のRenderItem観測数は
postRender当たり平均1、source mapping観測数は平均1,000で、consolidationとMultiDrawを確認しました。
静止・単体回転では平均33 itemでした。試行全体の平均であり、各frameの個数やGPU draw call数、
hardware instancing数ではありません。callback自体がbatchingを変える可能性もあるため、
通常版の集約数や速度はこの診断だけで断定しません。

実Move toolの診断でも、親・個体各1回の移動中に独自更新callbackは呼ばれませんでした。
親操作では全子孫のworld matrix、単体操作では対象だけが変わることを確認しました。
各5描画・移動値の変化1回だけなので、待機を含む時間や描画間隔をFPSへ換算しません。
初回の試験02は初期シーンの再表示でMaya内部のconsolidation関連stackを伴うaccess violation、
同じDLL・script・設定での試験03は成功しました。原因は未特定で、修正済みとは扱いません。
失敗した試験02は性能比較から除外し、ログを保持しています。

診断原本は `build/fixed_cube/runs/improvement_20261117/`、独立監査は
`build/fixed_cube/improvement_20261117_{current_profile,manipulator,curve_draw}_analysis.json` です。
将来の個別変形は、変更時だけローカル頂点を作り直し、親行列の更新はMayaへ委譲する方針を維持します。
多色や集約方式の変更は、その仕様を加えた条件で操作・再生を測定して判断します。

### 追加した研究入口

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -OutputSuffix ResearchCurrent
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -Variant NodeParallel
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -Profile
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -DrawProfile
```

成果物は順に `ResearchCurrent` / `ResearchParallel` / `ResearchProfile` / `ResearchDrawProfile` を
末尾に付けた Geometry DLL です。中間buildを分離し、DLLは従来の研究用Releaseフォルダへ出力します。
診断DLLでは `launch.ps1 -NativeProfile` を使い、`-MayaProfile` でMaya内部の記録も追加できます。
次はMove toolの実操作を記録する例です。出力先は未使用の名前にします。

```powershell
.\native\maya\experiments\fixed_cube\launch.ps1 -Mode geometry -OutputDirectory build/fixed_cube/runs/new_manipulator -PluginPath build/fixed_cube/maya2025/Release/bdShpCubeGeometryResearchProfile.mll -ManipulatorProbe -NativeProfile -ForceSelfExit
```

UIでgroup / individualを選び、Start → Moveハンドルをドラッグ → Finish の順に操作します。
両方の移動確認後、Save & Exitで結果保存と終了を行います。
研究版は本体や別のCube研究版と同時ロードしません。診断付きの数値は性能比較に混ぜません。
通常の `bdUtilNodes` buildでは、今回の並列候補・診断処理は有効になりません。

最終の `verify.cmd -IncludeNative -IncludeCubeResearch` は終了コード0でした。
Black 4,823ファイル、3versionの型確認・native各949件・Cube研究契約、Maya 2025 full pytest
8,344件、3versionのQt各1,195件・Maya UI各1,035件が通過しています。
初回はBlackの並列実行が停止したため中断し、`BLACK_NUM_WORKERS=1` の環境で
同じ統一入口を再実行しました。ログは `build/fixed_cube/verify_improvement_20261117_retry.log`。
配布DLLは3versionとも通常設定で再ビルド済みです。性能・実描画のGUI計測はMaya 2025 / OpenGLのみです。

## 参考

- [Autodesk Scene Overrides](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Viewport-2-0-API/Overview-of-the-Viewport-2-0-API/Maya_DEVHELP_Viewport_2_0_API_Overview_of_the_Viewport_2_0_API_Scene_Overrides_html.html)
- [MRenderItem](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_render_item.html)
- 既存調査: `build/controller_performance/cube_investigation/`（Git 管理外）

既存 `bdControllerShape` の過去の数値と今回の測定値を、同条件の直接比較として混ぜません。
