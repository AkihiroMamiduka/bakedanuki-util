# 固定 Cube の描画速度研究

`bdShpL_Cube` は、既定のローカル座標が各軸 `±0.5 cm` の線のみ Cube です。
8 頂点と重複のない 12 辺を維持し、軸と各面の位置を8個の静的な属性で調整します。
親 DAG 階層の最終行列を反映し、pivot、rotateAxis、shear、jointOrient、
offsetParentMatrix を Maya 標準の計算へ委譲します。
頂点を TRS に分解した値で作り直す処理はありません。

## 静的な形状設定（2026-11-18）

本体と研究用 Geometry / SubScene 版の形状設定は次の8属性です。

| 属性 | 短縮名 | 型 | 既定値 |
| --- | --- | --- | --- |
| `shape1stAxis` | `s1a` | enum | `+X`（0） |
| `shape2ndAxis` | `s2a` | enum | `+Y`（2） |
| `shapeBaseSpace1stAxisPlus` | `sbsp1p` | doubleLinear | 0.5 cm |
| `shapeBaseSpace1stAxisMinus` | `sbsp1m` | doubleLinear | 0.5 cm |
| `shapeBaseSpace2ndAxisPlus` | `sbsp2p` | doubleLinear | 0.5 cm |
| `shapeBaseSpace2ndAxisMinus` | `sbsp2m` | doubleLinear | 0.5 cm |
| `shapeBaseSpace3rdAxisPlus` | `sbsp3p` | doubleLinear | 0.5 cm |
| `shapeBaseSpace3rdAxisMinus` | `sbsp3m` | doubleLinear | 0.5 cm |

軸 enum は `+X / -X / +Y / -Y / +Z / -Z` の順に `0..5` です。
第3軸は第1軸と第2軸の外積です。同じ軸を指定した場合、第1軸が `±Y` なら
第2軸を `+Z`、それ以外なら `+Y` として形状を計算します。
各軸の Plus 側は設定値、Minus 側は設定値の符号を反転した位置です。
距離は負値・ゼロ・面の反転を許容し、clamp しません。
8属性は直接編集できますが、キー設定と入力接続は禁止します。
通常のアニメーションには親 transform を使用します。
NodeOperator では各属性の長い名前・短縮名と enum 定数を補完できます。
`DoubleLinearPlugOperator.set()` / `.get()` の距離単位は cm です。

後述の2026-11-17までの性能・表示記録は、独自の形状属性を持たなかった版の結果です。
過去の証拠はそのまま保存し、属性追加後の性能・表示確認と区別します。

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
DAG instance、component 編集、線幅、透明度、DrawOnTop は対象外です。
継承された locator の `localPosition` / `localScale` も形状には適用しません。
表示条件を広げる場合は、速度だけでなく基本操作・表示の対応範囲も比較します。
Selection Highlighting OFF でも選択色が残る既存制約があります。
通常の選択色、親・display layer の表示／色、キーによる色・可視性、
`hideOnPlayback` による再生中の非表示と復元は追加の GUI gate で確認しています。

Geometry 版は Maya の geometry 管理を使い、形状設定を変更したときにローカル頂点を更新します。
親 transform だけの変更では頂点を作り直さず、Maya が geometry を再要求した場合は再生成します。
SubScene 版は既定頂点の vertex buffer と固定 index buffer を renderer ごとに共有します。
調整した頂点が既定と異なるノードは専用 vertex buffer を持ち、形状設定の変更時に更新します。
既定頂点へ戻すと共有 buffer に戻し、専用 buffer を解放します。行列も変更時だけ更新します。
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
8個の静的属性の定義・軸の組合せ・非対称な各面の位置・キーと入力接続の拒否も対象です。
さらに、配布先 `bdUtilNodes` と build の SHA256 が一致することを確認し、
隔離した設定の mayapy から `.mod` を通してプラグイン名でロードします。
実際のロード先・Module path・API version を照合し、同じ 66 件の契約を実行します。
配布先が古い場合や存在しない場合は失敗させ、通常の native build で更新します。
66件の契約は通常テストと研究ランナーで共有し、実装の分岐による検証漏れを防ぎます。
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
この節の計測は Cached Playback を無効にして実施しました。

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

## 2026-11-18 の静的な軸・基準空間属性の追加検証

`shape1stAxis` / `shape2ndAxis` と6方向の `shapeBaseSpace` 距離を追加し、
属性なし版の `5e4f4fa4` を基準として比較しました。8属性は直接編集用で、
キーと入力接続を拒否します。形状変更時に8頂点と境界を更新し、通常の親操作・再生では
保持した形状を使用します。辺の接続情報と同色のshaderも再利用します。

Maya 2025 / OpenGL、独立した1,000個のtransform / shapeを共通親へ配置しました。
既定形状は変更前 / 変更後 / 変更後 / 変更前、調整済み形状は変更後 / nurbsCurve /
nurbsCurve / 変更後の順で、各72要求frame × 5試行、暖機8回を測定しました。
調整済み条件は全ノードが異なる軸・非対称距離の組み合わせで、curveにも同じローカル頂点を使います。
旧版は既定形状だけで比較し、親transformによる形状の代用は行いません。

各起動内の5試行の中央値を取り、さらに2起動の中央値を集計した処理時間です。
単位はms / 要求frame、小さいほど高速です。親・単体操作は選択したtransformの
回転設定と強制refreshを含み、実マウス操作のHUD FPSではありません。

| 条件 | 追加前・既定形状 | 追加後・既定形状 | 追加後・調整済み | nurbsCurve・調整済み |
| --- | ---: | ---: | ---: | ---: |
| 静止refresh | 1.631 | 1.294 | 1.370 | 1.355 |
| 単体操作 | 1.604 | 1.488 | 1.468 | 1.497 |
| 共通親操作 | 7.583 | 7.413 | 7.488 | 7.228 |
| カメラ操作 | 1.567 | 1.583 | 1.481 | 1.523 |
| 再生 | 2.674 | 2.654 | 2.610 | 2.551 |

既定形状の追加後 / 追加前は、親操作 −2.25%、単体操作 −7.25%、再生 −0.76%でした。
親操作の前後ペアは +0.37% / −4.75%、再生は −1.66% / +0.16%で、
今回の条件では一貫した負荷増は確認していません。
調整済み形状の追加後 / curveは、親操作 +3.60%、単体操作 −1.90%、再生 +2.32%でした。
各条件2起動の記述比較で、起動差と試行差を含みます。調整済みの親操作は
全試行をまとめた中央値では差の向きが変わるため、数％の差を確定的な優劣とは扱いません。
全200試行を除外せず保持し、再生の最大3.401 ms、調整済み親操作の最大8.378 msも含めています。

全起動の実終了は0で、timeoutはありません。DLL / ソース / 設定のSHA、
同条件のfixtureと採取画像、12辺の選択、6種類の親変換を照合しました。
実描画通知は各試行72回、再生は71回で全起動が一致します。
これは対象viewの通知数であり、全viewの描画数やGPU draw call数ではありません。
画像は採取した姿勢の検証で、計時した全frameの画像検証ではありません。
通常のmain view-paneの状態も独立した記録対象にはしていません。

追加後の既定形状・調整済み形状と、配布用 `bdUtilNodes.mll` の3つのGUI smokeも成功しました。
配布DLLの52画像は研究版の調整済みsmokeと一致し、属性変更、Undo / Redo、
非表示中の編集後の再表示、変更後と再表示後の辺の選択を確認しています。
smokeの計時値は正式比較へ含めません。

証拠は `build/fixed_cube/static_axes_20261118/`（Git管理外）に保存しています。
正式結果は `formal_01/audit_after_08.json`、独立再計算は
`independent_recalculation_01.json`、本節追記直前の全入力一致と配布smokeの最終監査は
`final_freeze_audit_01.json` です。実行時のソースと入力はsnapshotに保存済みです。
現ソースとの一致を要求する再監査は本節追記前に完了しています。本節追記後はREADMEの
差分が検出されるため、実行時のsnapshotと保存済みの最終監査を証拠として参照します。

`verify.cmd -IncludeNative -IncludeCubeResearch` は終了コード0でした。
Black 4,823ファイル、3版の型確認・native各1,009件・Cube契約各方式66件、
Maya 2025 full pytest 8,404件、3版のQt各1,195件・Maya UI各1,035件が成功しました。
制限環境でBlackが停止した実行は中断し、通常環境で同じ統一入口を再実行しています。
ログは `build/fixed_cube/static_axes_20261118/verify_20261118_unrestricted.log` です。
配布DLLは3版とも通常設定で更新済みで、実Viewportと性能の確認範囲はMaya 2025 / OpenGLです。

## Cached Playback の復元（2026-11-18）

修正前の `bdShpL_Cube` は、キャッシュ済みのフレームで親のワールド行列が復元されても、
Viewport にその姿勢が反映されない場合がありました。形状調整属性の追加前の DLL でも再現し、
同じ階層の標準 `nurbsCurve` と `locator` は正しく再生されました。
Maya は `MPxLocatorNode` の派生ノードを既定ではキャッシュしないため、
`BdShpLCubeNode::getCacheSetup()` で `kWantToCacheByDefault` を有効にします。
[Autodesk Maya 2025 Cached Playback](https://damassets.autodesk.net/content/dam/autodesk/www/html/maya-cached-playback/2025/MayaCachedPlaybackWhitePaper.html)

Maya 2025 / OpenGL で、共通親と各 Cube の直接の親に移動・回転キーを設定しました。
Evaluation Cache、Viewport Software、Viewport Hardware の各設定で、修正版の充填中と充填後の
再生画像を3フレームずつ採取し、Cached Playback OFF の静止参照と一致することを確認しました。
静的な形状調整を適用した Cube では、バックグラウンド充填後の Evaluation Cache からの復元も確認しました。

既定の復元確認は、専用 Maya プロファイルを用意して次のように実行できます。

```powershell
.\native\maya\experiments\fixed_cube\launch.ps1 -Mode geometry `
    -PluginPath bakedanuki/bakedanuki-util/plug-ins/maya2025/bdUtilNodes.mll `
    -OutputDirectory build/fixed_cube/runs/cached_playback -CachedPlaybackProbe -ForceSelfExit
```

`-RunMetadataPath` で対象（`targets` に `group`、`individual`）とキャッシュモード
（`cache_modes` に `evaluation`、`software`、`hardware`）を指定できます。
計時する場合は `measure` を `true` にし、`cache_modes` を `evaluation` または `off` の1要素にします。
描画の一致判定と実際のキャッシュ範囲は `results.json` に記録します。

### Cube 1,000個での計時

Maya 2025 / OpenGL の単一 VP2 ビュー（956 × 676）で、独立した1,000個の transform / shape を
同じ共通親の下に置きました。72要求フレーム × 5試行を各条件2起動で計測しています。
各起動の中央値を取り、その2値の中央値を示します。単位は ms / 要求フレームです。
操作は回転設定と VP2 の強制更新、再生は開始・停止を含む Maya の全フレーム再生です。

| 条件 | 共通親操作 | 単体操作 | 再生 |
| --- | ---: | ---: | ---: |
| 修正前 / OFF | 7.426 | 1.353 | 2.628 |
| 修正後 / OFF | 7.152 | 1.469 | 2.489 |
| 修正後 / ON | 7.279 | 1.354 | 3.223 |
| 同形状の `nurbsCurve` / ON | 7.219 | 1.342 | 3.190 |

ON は Evaluation Cache です。操作でキャッシュが無効化されることと、再生の全試行で
対象区間のキャッシュが計時前後に有効であることを確認しました。120試行の VP2 描画通知は
操作72回、再生71回で一致しました。単体操作の OFF 前後差は2起動の組で増減が分かれました。
ON の再生は、このシーンでは修正版の OFF に対して約0.73 ms / フレーム長く、
同じ ON 条件の `nurbsCurve` とは約0.03 ms / フレームの差でした。

移動マニピュレータは、修正版の X 軸ハンドルに同じ72回のドラッグ入力を送り、
ON / OFF を各2起動・5試行で計測しました。全40試行で入力に対応する72回の VP2 描画と
同じ移動量を確認しました。表は Maya の入力処理と描画を含む ms / 入力です。

| 移動マニピュレータ | OFF | ON |
| --- | ---: | ---: |
| 共通親 | 6.275 | 6.303 |
| 単体 | 3.160 | 2.962 |

再現と性能の証拠は `build/fixed_cube/cached_playback_20261118/`（Git 管理外）、
再集計と監査は同フォルダの `timing_audit.json` と `drag_audit.json` です。

## フォーカス用の兄弟シェイプ付きコントローラー

Maya 2025.3.3 / OpenGL で、共通親の下にコントローラーを1,000組配置しました。
各コントローラーは、先頭に非表示のフォーカス用シェイプ、2番目に同形状の Cube 本体を持ちます。
`nurbsCurve` 2枚構成では先頭を `overrideVisibility` で隠し、
プラグイン構成では `bdShpL_FocusBoundingBox.showShape` を OFF にしました。
配布版はプレビュー表示中だけフォーカス用ノードを Evaluation Cache の既定対象にします。

各構成を独立した2回の起動で測定し、各起動5試行の中央値を集計しました。
操作は Maya の移動マニピュレータへ送った72入力の1入力あたり、
再生は Maya の全フレーム再生で描画された71フレームの1フレームあたりです。単位は ms です。

| 構成 | Cached Playback | 共通親操作 | 単体操作 | 再生 |
| --- | --- | ---: | ---: | ---: |
| `nurbsCurve` 2枚 | OFF | 7.51 | 2.72 | 3.02 |
| Focus Bounding Box + Cube | OFF | 8.73 | 3.35 | 3.29 |
| `nurbsCurve` 2枚 | Evaluation Cache | 7.64 | 2.53 | 4.10 |
| Focus Bounding Box + Cube | Evaluation Cache | 8.99 | 3.54 | 3.53 |

単体と共通親の再生時に、表示したプレビューが通常再生および Evaluation / VP2 Software /
VP2 Hardware Cache の復元フレームと一致することを画像で確認しました。
速度計測と描画検証の記録は `build/fixed_cube/focus_bbox_20261118/`（Git 管理外）にあります。

### マニピュレータ操作とフォーカス用シェイプの表示設定

この節は表示オーバーライドを切り替えたときの比較記録です。
現在の配布版は再生を優先し、作成時にフォーカス用シェイプの `overrideEnabled` を OFF でロックします。

Maya 2025.3.3 / OpenGL で、同じ共通親の下にコントローラーを1,000組配置しました。
移動マニピュレータの X 軸へ72入力を送り、その移動軌跡と同じ `translateX` の値変更と描画更新も測りました。
各構成を独立に2回起動し、起動ごとの5試行の中央値を集計しています。各入力の描画と、両操作の移動値・最終行列を照合しました。

| キャッシュ OFF の構成 | 共通親ドラッグ | 共通親の値変更＋描画 | 単体ドラッグ |
| --- | ---: | ---: | ---: |
| `nurbsCurve` 本体のみ | 7.86 ms | 7.14 ms | 2.41 ms |
| `nurbsCurve` 2枚 | 8.89 ms | 8.29 ms | 2.50 ms |
| `bdShpL_Cube` 本体のみ | 7.72 ms | 6.99 ms | 3.00 ms |
| Focus Bounding Box + Cube | 11.61 ms | 11.13 ms | 3.09 ms |

共通親でフォーカス用シェイプを追加した差は、ドラッグと値変更の両方に出ました。
36描画の Profiler 診断では、Geometry の共通親ドラッグ時に `Vp2PrepareToUpdate` が
1.06 → 2.01 ms、`Vp2BuildRenderLists` が 2.48 → 3.69 ms に増えました。
後述の表示オーバーライドを使用すると、同じ診断でそれぞれ 1.05 ms、2.36 ms になりました。
フォーカス用ノードの GeometryOverride で並列更新を外した試作の共通親ドラッグは、
キャッシュ OFF の2起動で 11.86 ms と 11.66 ms、同時期の配布版は 11.67 ms でした。

表示オーバーライドの比較では、フォーカス用シェイプの `showShape=OFF` と `visibility=ON` を揃えました。
表示オーバーライド併用時は `overrideEnabled=ON`、`overrideVisibility=OFF` を指定しました。
各設定を2起動、5試行ずつ測定しました。ドラッグは ms／入力、再生は ms／描画フレームです。
ON は Evaluation Cache で、再生の計時前後とも対象範囲のキャッシュが有効でした。

| フォーカス用シェイプの設定 | キャッシュ | 共通親ドラッグ | 単体ドラッグ | 再生 |
| --- | --- | ---: | ---: | ---: |
| `showShape=OFF` | OFF | 11.53 | 3.14 | 3.23 |
| 表示オーバーライド併用 | OFF | 8.59 | 2.90 | 3.56 |
| `showShape=OFF` | ON | 8.73 | 3.25 | 3.41 |
| 表示オーバーライド併用 | ON | 8.07 | 3.97 | 4.00 |

`showShape=OFF` の2設定はキャッシュ対象がいずれも2,001ノードでした。
`showShape=ON` のまま表示オーバーライドで隠した追加診断は3,001ノードとなり、成功した1起動の再生中央値は
5.88 ms でした。同条件のもう1起動では、初回描画中に Maya が異常終了しました。
表示オーバーライド併用時にも `F` の範囲と本体の描画・選択を確認し、プレビューの表示切替を検証しました。
計測、回帰確認、Profiler の記録は `build/fixed_cube/manipulator_20261119/`（Git 管理外）にあります。

## 参考

- [Autodesk Scene Overrides](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Viewport-2-0-API/Overview-of-the-Viewport-2-0-API/Maya_DEVHELP_Viewport_2_0_API_Overview_of_the_Viewport_2_0_API_Scene_Overrides_html.html)
- [MRenderItem](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_render_item.html)
- 既存調査: `build/controller_performance/cube_investigation/`（Git 管理外）

既存 `bdControllerShape` の過去の数値と今回の測定値を、同条件の直接比較として混ぜません。
