# 固定 Cube の描画速度研究

`bdShpL_Cube` は、既定のローカル座標が各軸 `±0.5 cm` の線のみ Cube です。
8 頂点と重複のない 12 辺を維持し、軸と各面の位置を8個の静的な属性で調整します。
親 DAG 階層の最終行列を反映し、pivot、rotateAxis、shear、jointOrient、
offsetParentMatrix を Maya 標準の計算へ委譲します。
頂点を TRS に分解した値で作り直す処理はありません。

## 静的シェイプの設計方針

`bdShpL_Cube` と `bdShpL_FocusBoundingBox` は、形状属性を直接編集してローカル形状とフォーカス範囲を定義します。
これらの形状属性はキーと接続を禁止し、今後追加する形状設定にも同じ制約を適用します。
リグの移動・回転・スケールや再生では、Maya が計算する親 transform の変換を使います。
フォーカス範囲は Box で指定し、`showShape` でプレビュー表示を切り替えます。
平面を囲む場合は、平面に垂直なローカル軸の Plus と Minus を 0 に設定します。

描画は Geometry を基準とします。Maya 2025 の1,000個の比較では、行列未実装と実装済み未接続の Geometry はどちらも単体ドラッグ約2.9 ms／入力、共通親再生約3.2 ms／描画フレーム（Evaluation Cache 充填済み）でした。
単位行列を接続して共通親を動かすと、同じ再生で33.81〜35.01 msに増えました。
配布版の Cube と Box から `shapeTransformMatrix` と行列入力専用の変形処理を削除しました。
ローカル形状を静的な値で定義し、形状入力の接続による追加負荷を避けます。

形状自体のアニメーションには、SubSceneMatrix の検証をもとに追加した `bdShpL_DeformableCube` を使用します。
`bdUtilNodes` 内に固有の `MTypeId` を持つ別ノードとして登録しています。使い方は[変形対応 Cube](../../README.md#変形対応-cube)を参照してください。
固定頂点を使う試作は、行列を毎フレーム変更する条件で Geometry の46.71 ms（OFF）／50.92 ms（ON）を16.85 ms（OFF）／17.51 ms（ON）に短縮しました。
以前の診断で計った頂点変換と境界の再生成は1,000個合計で約0.12〜0.29 ms／描画フレームでした。
回転用や拡縮用の属性へ分ける場合も、速度の検討は Viewport 2.0 の描画更新とバッファの再利用を優先します。

以下の行列入力付きの計測は、仕様変更前の研究記録です。
行列入力を再検証するときは、研究 DLL のビルドに `-ShapeMatrix` を指定します。

静的版は Maya 2025 の GUI で、Cube に立体または平面の Box を組み合わせ、フォーカス、プレビュー切替、Cube の辺の選択を確認しました。
共通親を移動・回転させて再生し、キャッシュ OFF・充填中・復元時に採取した描画を3姿勢の参照画像と照合しました。

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
実際のロード先・Module path・API version を照合し、同じ静的 Cube の契約を実行します。
配布先が古い場合や存在しない場合は失敗させ、通常の native build で更新します。
静的 Cube の契約は通常テストと研究ランナーで共有します。
行列入力を有効にした研究 DLL には、`test_contract.py` の `--shape-matrix` を指定して行列の契約も検証します。
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
`BdShpLCubeNode.h`、`FixedCubeGeometry.h`、`LocatorChannelBox.h`、`SignedShapeAxes.h` も
`source_snapshot/production_cube` 以下へ本体内の相対パスを保って保存します。
`source_snapshot_manifest.json` に全ファイルの
SHA256 を記録し、各起動の前後で現在のソース・保存済みコピー・manifest の不変を確認します。
測定中は研究ディレクトリと本体側のこれらのファイルを編集しないでください。

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

### 形状アニメーション行列の追加

Maya 2025.3.3 / OpenGL で、固定した親の下の Cube を `composeMatrix.outputMatrix` で変形させました。
Evaluation / Viewport Software / Viewport Hardware の充填中と復元後、および Evaluation のバックグラウンド充填後で、
3つの描画フレームがキャッシュ OFF の参照画像と一致しました。時間を前後させたときの境界と、移動先での選択も確認しました。
Evaluation Cache を有効にしたまま接続を切断・再接続し、再充填後も同じ画像が復元されることを確認しました。

未接続・単位行列の Cube 本体1,000個で、追加前の配布版と最終候補を2回ずつ独立に起動しました。
各起動で5試行し、起動ごとの中央値を集計しました。操作は72回の Move 入力の ms / 入力、再生は ms / 描画フレームです。

| DLL | キャッシュ | 共通親ドラッグ | 単体ドラッグ | 再生 |
| --- | --- | ---: | ---: | ---: |
| 追加前 | OFF | 7.922 | 2.829 | 2.465 |
| 追加後 | OFF | 7.728 | 2.705 | 2.406 |
| 追加前 | Evaluation Cache | 6.453 | 2.853 | 3.019 |
| 追加後 | Evaluation Cache | 6.378 | 2.764 | 2.932 |

再生は測定順を反転した両方の比較で従来と同等の範囲に収まりました。キャッシュ ON の共通親ドラッグは起動によって増減が分かれました。
記録は `build/fixed_cube/animation_matrix_20261119/`（Git 管理外）にあります。

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

## フォーカス用プレビュー形状の比較

Box に一本化する前の計測です。各形状の計測結果を開発の記録として残します。
Maya 2025.3.3 / OpenGL で、フォーカス用シェイプと `bdShpL_Cube` を持つ1,000組を計測しました。
4形状を同じ DLL で2回ずつ独立起動し、プレビューと Evaluation Cache をそれぞれ ON／OFF にしました。
Box と3軸十字は同じ3D範囲、四角と2D十字は同じ平面範囲を使い、プレビューの線と本体の線が重ならないように配置しました。
操作は Move マニピュレータで共通親と単体をドラッグし、再生は共通親をアニメーションして計測しました。

| フォーカス形状 | 頂点／辺 | キャッシュ ON・非表示の再生 | キャッシュ ON・表示の再生 |
| --- | ---: | ---: | ---: |
| Box | 8／12 | 3.715 ms | 8.517 ms |
| 3軸十字 | 6／3 | 3.901 ms | 8.716 ms |
| 四角 | 4／4 | 3.612 ms | 8.702 ms |
| 2D十字 | 4／2 | 3.617 ms | 8.838 ms |

値は各起動で3試行した、描画フレーム当たりの時間の中央値を集約したものです。
非表示・キャッシュ ON の再生では、起動間のばらつきが形状間の差と同程度でした。
表示時にフォーカス用1,000ノードがキャッシュ対象に加わり、全形状で再生時間が増えました。
操作とキャッシュ OFF の結果、F キー相当のフレーミング、プレビューと本体の選択の記録は
`build/fixed_cube/focus_variants_2d_20261119/`（Git 管理外）にあります。

## フォーカス用シェイプの行列入力

Maya 2025.3.3 / OpenGL で、`showShape=OFF` の Box と Cube 本体を1,000組配置しました。
接続条件では各組に `composeMatrix` を置き、既存版は本体へ、新版は本体と Box へ同じ出力を接続しました。
同じ条件順で完走した起動の3試行の中央値です。操作は ms／入力、再生は ms／描画フレームです。

| 行列入力 | Evaluation Cache | 共通親ドラッグ 既存→新版 | 単体ドラッグ 既存→新版 | 再生 既存→新版 |
| --- | --- | ---: | ---: | ---: |
| 未接続 | OFF | 13.40 → 13.56 | 3.48 → 3.67 | 4.22 → 3.86 |
| 未接続 | ON | 9.57 → 9.95 | 3.64 → 3.85 | 4.47 → 3.94 |
| 接続 | OFF | 13.25 → 13.69 | 3.48 → 3.64 | 51.65 → 90.93 |
| 接続 | ON | 55.81 → 94.41 | 3.87 → 3.66 | 58.93 → 71.95 |

未接続時の操作と再生は既存版の起動間のばらつきに近い範囲でした。1,000組すべてを接続すると、再生とキャッシュ ON の共通親ドラッグに追加コストが残りました。
非表示の Box に接続した行列を再生中も境界照会で反映する試作は、キャッシュ ON の1,000組で応答が止まりました。
再生中の読み取りを省いた版では完走し、Box と Square の停止直後・フレーム移動後のフォーカスも確認できました。
再生前後にはビューポートの線の画素位置を照合しました。接続・キャッシュ ON では一部の選択色に差が出たため、元画像とハッシュを記録しています。
計測と機能検証の記録は `build/fixed_cube/focus_matrix_20261119/runs/`（Git 管理外）にあります。

## Cube 本体の行列入力を毎フレーム更新する再生（2026-11-20）

Maya 2025.3.3 / OpenGL で、フォーカス用シェイプを含まない `bdShpL_Cube` を1,000個配置しました。
行列入力ありの条件では、独立した1つの `transform.matrix` をすべての `shapeTransformMatrix` に直接接続しました。
アニメーション条件では、その transform の3軸のスケールを1から5まで変化させます。
1〜72フレームを3試行ずつ全フレーム再生し、71回の対象ビューの `postRender` 当たり時間を集計しました。
ON は対象範囲を充填済みの Evaluation Cache です。フレーム 2 / 36 / 72 の再生画像は、キャッシュ OFF の参照画像と照合しました。

基準版 `00bf94aa` の未接続と固定行列の接続は各試行組の中央値が約1.2〜1.5 ms／描画フレームでした。
行列が毎フレーム変化すると、OFF は46.12〜47.35 ms、ON は48.08〜48.95 msでした。
診断付きの起動では、71回の描画に対して `updateRenderItems` と `populateGeometry` が各71,000回呼ばれました。
Maya Profiler でも VP2 の DAG オブジェクト更新やジオメトリバッファ更新の時間が大きく、拡縮の行列計算と8頂点の再生成に使った時間は相対的に小さくなりました。
キャッシュ充填後の再生でも、姿勢に合わせて VP2 の境界と頂点の更新が発生します。

アニメーション部分を描画行列で適用する試作は、接続切替後のクリック選択と1,000個での安定性を満たせませんでした。
描画アイテム更新を省く試作は充填済みキャッシュからの復元に失敗し、復元できる設定では再生時間が増えました。
描画集約を無効にした試作でも再生時間が増えました。

位置バッファを再利用する試作は、初回のキャッシュ OFF で43.88 msまで短縮しました。
配布用と同じビルド設定で、各測定順を揃えて比較すると、安定した短縮は確認できませんでした。

| 測定順 | Cached Playback | 基準版 | 位置バッファ再利用試作 |
| --- | --- | ---: | ---: |
| 未接続 → 固定 → アニメーション | OFF | 47.35 | 46.67 |
| 未接続 → 固定 → アニメーション | ON | 48.08 | 50.43 |
| アニメーション → 固定 → 未接続 | OFF | 46.12 | 47.75 |
| アニメーション → 固定 → 未接続 | ON | 48.95 | 47.94 |

表はアニメーション接続時の ms／描画フレームです。配布版の描画経路は基準版と同じです。
研究用プロファイルで、行列読み取りと頂点・境界の再生成を個別に計時できます。

計測と画像の記録は `build/fixed_cube/cube_matrix_playback_20261120/runs/`（Git 管理外）にあります。

### 固定頂点と描画行列を使う SubScene の追加調査

`SubSceneMatrix` は、各 Cube の軸と6方向の寸法から頂点バッファを作り、`shapeTransformMatrix` と親階層のワールド行列を掛け合わせて描画します。
形状の寸法が異なる Cube はそれぞれの頂点を保持します。軸と寸法が一定の間、行列アニメーションには同じ頂点バッファを使います。
Maya の DAG 境界には従来どおり変形後のローカル境界を返します。

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -Variant SubSceneMatrix -ShapeMatrix
```

`bdShpCubeSubSceneResearchSubSceneShapeMatrix.mll` を生成します。同じノード名と `MTypeId` を持つため、配布版と研究版はそれぞれ独立した Maya プロセスで比較します。
研究用 SubScene は各シェイプについて1本の DAG パスを描画します。以下の SubScene の計測対象は、それぞれ独立したシェイプを持つ1,000個の transform です。

Maya 2025 の機能検証では、非対称な Cube に回転・スケール・シアー・移動を加え、通常再生とキャッシュ復元の画像、ローカル境界、移動後の線のクリック選択を確認しました。
直接設定した行列から接続への切替、切断、旧位置が画面外にあるときの描画と選択、VP2 リセット後の選択も確認しました。
Geometry 側で描画集約を無効にし、行列と固定境界の再設定を抑える試作では、接続切替後に移動先の線をクリックしても選択できませんでした。

Maya 2025.3.3 / OpenGL で1〜72を全フレーム再生しました。各欄は3試行の中央値で、単位は ms／実描画フレームです。各試行で71回の描画を確認し、Evaluation Cache は全区間の充填後に計測しました。

| 入力とアニメーション | 配布 Geometry OFF | SubSceneMatrix OFF | 配布 Geometry ON | SubSceneMatrix ON |
| --- | ---: | ---: | ---: | ---: |
| 同じ形状1,000個、共通の入力行列で拡縮 | 59.00 | 15.87 | 57.59 | 16.14 |
| 998個の軸・寸法を個別に設定、共通の入力行列で拡縮 | 41.79 | 15.97 | 45.81 | 16.49 |
| 行列未接続、共通親を0〜3 cm移動 | 3.16 | 10.47 | 3.75 | 10.81 |
| 行列未接続、親も Cube も静止 | 1.13 | 6.86 | 1.10 | 7.36 |

同じ形状の拡縮は、最初の起動でも配布版48.84 / 52.40 ms、試作15.26 / 16.13 msでした（OFF / ON）。表の同一形状・静止の行は試作を再ビルドし、条件と ON / OFF の順を反転した比較です。
従来の研究用 SubScene で変形済み頂点を毎フレーム渡す場合は36.31 / 36.53 msでした。SubScene 内でも、頂点バッファを固定して描画行列を更新することで再生時間が短縮しました。
各構成でフレーム2・36・72の描画は両方式の間で画素単位で一致しました。寸法を変えた構成では、代表10個のローカル境界も計算値と照合しました。
参考として、配布 Geometry で同じシェイプ1個を1,000個の親に DAG インスタンスとして配置すると、同一形状の拡縮は29.42 / 30.54 msでした。この構成では個体が軸・寸法・入力行列を共有します。

画像、条件、試行ごとの時間は `build/fixed_cube/cube_matrix_followup/runs/`（Git 管理外）にあります。

### Maya 2025 の描画方式と CV 変形の比較

`-Variant Draw` は `MPxDrawOverride` と `MUIDrawManager` で Cube の12辺を描画します。
基準空間の頂点と辺を用意し、`transform()` で入力行列と親階層のワールド行列を合成します。
Geometry、Draw、SubSceneMatrix の比較 DLL は既定で静的版を生成します。行列入力を含む比較条件には `-ShapeMatrix` を指定します。
3方式とも同じ `bdShpL_Cube` を登録するため、各 DLL は個別の Maya プロセスで読み込みました。

`build/fixed_cube/cube_draw_42/` に計測スクリプト、起動条件、各試行の時間、再生画像を保存しました。
すべて Maya 2025.3.3 / OpenGL で、956 × 676 px のビューポートを使い、共通親の下に独立した transform と Cube を1,000組配置しました。
表は各条件3試行の中央値です。
ドラッグは Cached Playback OFF で Move マニピュレータに72回の入力を与え、ms／入力を集計しました。
再生は1〜72フレームの全フレーム再生で、71回の実描画を確認して ms／描画フレームを集計しました。
ON は Evaluation Cache の充填後に計時し、3つのフレームの描画をキャッシュ OFF の参照画像と照合しました。
行列が未実装・未接続・固定値接続の再生では共通親を0〜3 cm移動しました。固定値接続には単位行列を使いました。
行列アニメーションでは親を固定し、独立した1個の transform の `.matrix` を共通入力として、XYZ スケールを1から5に変化させました。

`nurbsCurve` は `.create` に入力のない1次開曲線を1本ずつ使用しました。12辺を16 CVで辿るため、3辺が重複します。
各 CV の元座標を `pointMatrixMult.inPoint` に設定し、各 `.output` を対応する `controlPoints[i]` に接続しました。
この構成では1,000個で `pointMatrixMult` が16,000個になります。
未実装はカーブのみ、未接続は CV へ出力をつないだまま `inMatrix` を単位行列にした状態です。
固定値接続とアニメーション接続では、共通の `transform.matrix` を全 `pointMatrixMult.inMatrix` に接続しました。
ノード作成、キャッシュ充填、座標と画像の照合は計時区間の外で行いました。

| 行列入力の状態 | 操作・再生 | Draw | Geometry | SubSceneMatrix | `nurbsCurve` |
| --- | --- | ---: | ---: | ---: | ---: |
| 未実装 | 共通親ドラッグ | 11.59 | 8.15 | 12.61 | 8.05 |
| 未実装 | 単体ドラッグ | 7.09 | 2.87 | 8.66 | 2.54 |
| 未実装 | 共通親再生 OFF | 8.55 | 2.78 | 9.94 | 3.38 |
| 未実装 | 共通親再生 ON | 8.84 | 3.24 | 10.32 | 3.53 |
| 未接続 | 共通親ドラッグ | 11.96 | 8.22 | 12.68 | 7.90 |
| 未接続 | 単体ドラッグ | 6.95 | 2.82 | 9.29 | 2.56 |
| 未接続 | 共通親再生 OFF | 8.65 | 2.59 | 10.54 | 2.74 |
| 未接続 | 共通親再生 ON | 9.16 | 3.22 | 10.78 | 3.58 |
| 固定値接続 | 共通親ドラッグ | 13.66 | 8.04 | 13.95 | 8.11 |
| 固定値接続 | 単体ドラッグ | 7.14 | 2.76 | 10.03 | 2.73 |
| 固定値接続 | 共通親再生 OFF | 10.65 | 5.32 | 11.68 | 2.54 |
| 固定値接続 | 共通親再生 ON | 10.98 | 35.01 | 12.32 | 3.23 |
| アニメーション接続 | 入力行列再生 OFF | 92.69 | 46.71 | 16.85 | 22.79 |
| アニメーション接続 | 入力行列再生 ON | 97.01 | 50.92 | 17.51 | 17.31 |

Draw・Geometry・SubSceneMatrix は前回の126試行、`nurbsCurve` は同条件での追加42試行です。
ドラッグの入力数と描画数は各72回、再生は各71描画でした。
3方式の対応するドラッグの最終変位が一致し、各再生条件で採取したフレーム2・36・72の画像も3方式間で画素単位で一致しました。
Draw の単体機能試験で、行列の接続・切断、キャッシュ復元、移動後の線の選択、VP2 リセット後の描画と選択を確認しました。
Geometry の固定値接続時の共通親再生は、キャッシュ ON で35.01 msでした。
固定値接続を先に、キャッシュ ON を OFF より先に測る別起動でも33.81 msでした。
同じ別起動での未接続・ON は3.24 ms、固定値接続・OFF は5.38 msでした。

`nurbsCurve` は、初期の単位行列で1,000個のカーブの全16,000 CV が元の座標を保つことを確認しました。
再生時はフレーム2・36・72で代表2個の CV 座標を期待値と照合し、各条件でキャッシュ ON／OFF の描画が参照画像と画素単位で一致しました。
追加計測のスクリプト、試行ごとの時間と画像、集計は `build/fixed_cube/nurbs_cv_matrix_20261120/`（Git 管理外）に保存しました。

追試では `nurbsCurve` のアニメーション接続を固定値接続より先に計測し、両方式でキャッシュ ON を先に測りました。
`SubSceneMatrix` は前回と同じ DLL です。以下も各3試行の中央値で、単位は ms／描画フレームです。

| 構成 | 初回 OFF | 初回 ON | 追試 OFF | 追試 ON |
| --- | ---: | ---: | ---: | ---: |
| `nurbsCurve` ＋ CV ごとの `pointMatrixMult` | 22.79 | 17.31 | 22.45 | 16.77 |
| `SubSceneMatrix` | 16.85 | 17.51 | 16.09 | 16.38 |

キャッシュ OFF では、両計測とも `SubSceneMatrix` が約6 ms／フレーム短くなりました。
キャッシュ ON では、中央値に0.2〜0.4 msの差があり、初回と追試で順位が入れ替わりました。
固定値を接続した `nurbsCurve` の共通親再生は、初回 OFF／ON が2.54／3.23 ms、追試が2.94／3.28 msです。
この構成では `pointMatrixMult` が16,000個あっても、固定行列での親再生は標準カーブと同程度で、毎フレーム CV が変形する条件で再生時間が増えました。

### 固定形状での SubScene 更新処理

Maya 2025.3.3 / OpenGL で、形状行列入力のない `SubSceneMatrix` と標準 `nurbsCurve` を1,000個ずつ比較しました。
共通親の下に各 Cube の transform を配置し、静止、先頭の Cube だけの移動、共通親の移動を再生しました。
静止条件ではシェイプから独立した transform を動かしました。各条件の再生範囲は1〜72で、1本のアニメーションカーブで X を3 cm動かしました。
代表フレームで全 Cube のワールド X 座標と先頭・末尾の Cube のローカル境界を検証し、キャッシュ OFF で取得した参照画像と各再生の画像を照合しました。

| 再生 | `nurbsCurve` OFF | `nurbsCurve` ON | SubScene OFF | SubScene ON |
| --- | ---: | ---: | ---: | ---: |
| 静止 | 1.14 | 1.11 | 7.49 | 6.96 |
| 単体移動 | 1.18 | 1.18 | 6.77 | 6.74 |
| 共通親移動 | 2.45 | 3.25 | 9.60 | 10.06 |

単位は ms／実描画フレームで、各3試行の中央値です。全試行で実描画は71回、ON の計時区間は Evaluation Cache 充填済みです。
別試行の Maya Profiler では、メインスレッドの `Vp2PrepareToUpdate` が、静止で `nurbsCurve` の0.010／0.015 msに対し SubScene は6.29／6.43 ms、
共通親移動で0.015／0.016 msに対し8.52／8.07 msでした（OFF／ON）。SubScene の同区間には `Vp2UpdateSubScene` が含まれます。
描画リスト構築と `Vp2Draw3dBeautyPass` の差は、いずれも0.33 ms／描画以下でした。
`nurbsCurve` の共通親移動・キャッシュ OFF では、ワーカースレッドに `Vp2UpdateFlattenedHierarchies` が71回記録され、1描画当たり約0.51 msでした。

研究用 `bdCubeProfile` を追加して別に記録した、SubScene の描画1回当たりの呼び出し回数です。キャッシュ OFF／ON で回数は一致しました。

| 再生 | `requiresUpdate` | 表示状態取得 | `update` | `setMatrix` | 頂点バッファの登録 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 静止 | 1,000 | 1,000 | 0 | 0 | 0 |
| 単体移動 | 1,000 | 1,000 | 1 | 1 | 0 |
| 共通親移動 | 1,000 | 1,000 | 1,000 | 1,000 | 0 |

診断ビルドでは表示状態の取得に2.77〜2.95 ms／描画、共通親移動の `setMatrix` 呼び出しに0.85〜0.88 ms／描画かかりました。
表示状態の取得は `requiresUpdate` の内側で、`setMatrix` は `update` の内側で計測しているため、これらの値は重なります。
別に1個の Cube の寸法を編集すると、頂点バッファの登録が1回記録されました。

表示状態を一定にした検証シーンで、別の研究ビルドは再生中に前回の表示状態を再利用し、行列の変更は毎回反映しました。

| 再生 | 表示状態再利用 OFF | 表示状態再利用 ON |
| --- | ---: | ---: |
| 静止 | 3.87 | 4.04 |
| 単体移動 | 4.02 | 3.93 |
| 共通親移動 | 6.96 | 7.44 |

列の OFF／ON は Evaluation Cache の状態です。通常の SubScene と比較して、共通親移動は約2.6 ms／描画短縮しました。
別試行の `Vp2PrepareToUpdate` も、共通親移動で8.52／8.07 msから5.54／5.49 msに短縮しました（OFF／ON）。
各条件の代表フレームは通常ビルドと画素単位で一致しました。実用化には、色・可視性・選択状態などの変更を検知し、保持した状態を更新する仕組みが必要です。
再利用版でも標準カーブとの差は残り、`requiresUpdate` の他の処理や Maya 内部の描画準備には調査の余地があります。
実行条件、各試行の時刻、Profiler の原本、画像、カウンター、比較ビルドのソースは `build/fixed_cube/parent_update_20261120/`（Git 管理外）に保存しました。

### SubScene の更新判定と親 transform の追従

同じ Maya 2025.3.3 / OpenGL で、Cube 1,000個の形状と位置を固定し、別の transform だけを再生しました。
更新判定省略版は、描画アイテムが準備済みで再生中の場合、`requiresUpdate()` から即座に `false` を返します。
OFF／ON は Evaluation Cache の状態です。ON は充填済みです。各条件で5試行し、71回の実描画に対する時間の中央値を示します。

| 静止シーンでの再生 | キャッシュ OFF | キャッシュ ON |
| --- | ---: | ---: |
| `nurbsCurve` | 1.91 ms | 1.69 ms |
| SubScene、表示状態を再利用 | 3.32 ms | 3.40 ms |
| SubScene、再生中の更新判定を省略 | 1.63 ms | 1.71 ms |

3つのビルドの代表フレーム画像は OFF／ON の全6枚で画素単位に一致しました。
更新判定の省略で約1.69 ms／実描画を回収できました。別試行の `Vp2PrepareToUpdate` は3.17／3.04 msから1.47／1.54 msになりました。
静止条件の標準カーブに近い再生時間は、DAG や表示状態の変化がない計測シーンで得たものです。

離れた2個の Cube では、初期位置、共通親の移動、共通親の回転、個別 transform の移動と回転の4姿勢を比較しました。
`MRenderItem::setMatrix()` を省いて描画の集約を有効にした試作では、表示位置が固定されたまま、クリック選択は transform に追従しました。
`setWantConsolidation(false)` を指定した試作では、`setMatrix()` を省いても全4姿勢の画像が行列明示版と画素単位に一致しました。
新しい位置の2個を各姿勢でクリック選択でき、移動前の位置を選択しないことも確認しました。

1,000個では、描画集約を使わず自動追従させる試作に、再生中の `requiresUpdate()` を省く判定を組み合わせました。
Cube の形状および表示設定を固定し、親の移動だけを再生しました。

| 再生 | ビルド | キャッシュ OFF | キャッシュ ON |
| --- | --- | ---: | ---: |
| 単体移動 | `nurbsCurve` | 1.35 ms | 1.35 ms |
| 単体移動 | SubScene、表示状態を再利用して行列を明示 | 4.24 ms | 4.30 ms |
| 単体移動 | SubScene、描画集約を外して自動追従 | 4.72 ms | 4.86 ms |
| 共通親移動 | `nurbsCurve` | 3.10 ms | 3.60 ms |
| 共通親移動 | SubScene、表示状態を再利用して行列を明示 | 7.25 ms | 7.72 ms |
| 共通親移動 | SubScene、描画集約を外して自動追従 | 5.85 ms | 6.61 ms |

単体移動・共通親移動とも、OFF／ON の代表フレーム全12枚が3方式で一致しました。
共通親移動は1.1〜1.4 ms 短縮し、単体移動は0.5〜0.6 ms 増加しました。
別試行のキャッシュ ON・共通親移動では、自動追従版の `Vp2PrepareToUpdate` が6.47 ms から2.59 ms に短縮しました。
`Vp2BuildRenderLists` と `Vp2Draw3dBeautyPass` の合計は0.85 ms から2.91 ms に増えました。

形状も変形する試験では、1,000個の `shapeTransformMatrix` を同じ `transform.matrix` に接続しました。
入力元で3軸のスケールを1から5へ変えながら、共通親を X 方向に3 cm 動かしました。
3つの試作はいずれも現フレームの行列を合成して `setMatrix()` に渡し、キャッシュの設定ごとに5試行しました。

| 共通親移動と形状変形を同時に再生 | キャッシュ OFF | キャッシュ ON |
| --- | ---: | ---: |
| SubScene、通常の更新判定 | 17.89 ms | 18.48 ms |
| SubScene、表示状態を再利用 | 15.33 ms | 16.09 ms |
| SubScene、表示状態と DAG パスを再利用 | 14.99 ms | 15.55 ms |

各試作で OFF／ON の代表フレーム全6枚が画素単位で一致しました。
短縮の大部分は表示状態の再利用で得られ、DAG パスの再利用による追加短縮は0.34／0.54 ms でした（OFF／ON）。
ビルドごとに1起動を計測したため、小さい差の起動間再現性には追試が必要です。
表示状態と DAG パスを再利用する試作では、再生中の表示設定と階層を固定しています。
実用化には、色・可視性・選択状態と DAG の変更に応じて保持情報を更新する仕組みが必要です。

試作用ソース、計測条件、実描画画像、クリック選択の結果、Profiler と集計は `build/fixed_cube/subscene_followup_20261121/`（Git 管理外）に保存しました。

### 配布版の変形対応 Cube

Maya 2025.3.3 / OpenGL で `bdUtilNodes.mll` の `bdShpL_DeformableCube` を1,000個作成しました。
上と同じ条件で、共通の入力行列の3軸スケールを1から5へ変えながら、Cube の共通親を X 方向に3 cm移動しました。
5試行の中央値は実描画1フレーム当たり、キャッシュ OFF で12.32 ms、充填済みの ON で12.99 ms でした。
1試行は71描画です。両条件で代表3フレームの形状とキャッシュ OFF の参照画像を照合し、以前の行列明示版とも画素単位で一致しました。
この計測は配布版の1起動で得た値です。ビルド間の速度差を比較する場合は、揃えた条件での再計測が必要です。

単体の GUI 検証では、行列変形後の辺のクリック選択と `F` キー相当のフレーミング、選択色・可視性・色の更新、Viewport 2.0 のリセット後の描画を確認しました。
計測と GUI 検証の記録は `build/fixed_cube/deformable_cube_product/run01/`（Git 管理外）にあります。

### Cube の部分テンプレート線の試作

`bdShpL_Cube`（Geometry）と `bdShpL_DeformableCube`（SubScene）の両方で、各辺の部分テンプレート表示を試作しました。
`shapeTemplateLine` で有効化し、`shapeTemplateLineRate` で辺の中央の割合を指定し、`shapeTemplateLineInvert` で通常線とテンプレート線の区間を入れ替える仕様です。
試作の既定値は順に `false`、`0.7`、`false` で、テンプレート区間はクリック選択の対象外としました。

Maya 2025 / OpenGL で、transform と Cube シェイプの組を1,000個作り、共通親の下に配置しました。線色は全シェイプで揃えました。
追加前の `bbbd2b34` の配布 DLL と追加後の配布 DLL を2起動ずつ比較し、2組目は DLL・テンプレート設定・キャッシュの順序を逆にしました。
各起動で5試行し、起動ごとの中央値を集約しました。表の各セルは追加前／追加後 OFF／追加後 ON（割合 `0.7`、反転なし）の順です。
操作は Move マニピュレータのマウスイベント1回当たり、再生は実描画1フレーム当たりの ms です。
Cached Playback ON は Evaluation Cache 充填済みで、各試行は71描画です。
再生では共通親を X 方向に3 cm 移動しました。
行列接続条件では、全 Cube の `shapeDeformMatrix` を同じ `transform.matrix` に接続し、入力元の3軸スケールを1から5まで変化させました。

| シェイプ | 共通親ドラッグ | 単体ドラッグ | 再生・キャッシュ OFF | 再生・キャッシュ ON |
| --- | ---: | ---: | ---: | ---: |
| `bdShpL_Cube` | 7.70／7.80／8.66 | 2.71／2.81／2.93 | 2.48／2.59／2.73 | 3.09／3.08／3.33 |
| `bdShpL_DeformableCube`、行列未接続 | 11.87／12.39／13.09 | 8.46／9.03／8.96 | 9.54／9.73／11.03 | 10.72／10.19／11.19 |
| `bdShpL_DeformableCube`、行列を毎フレーム更新 | 13.60／13.59／14.88 | 10.17／10.19／10.51 | 11.86／12.63／13.25 | 12.54／12.94／13.83 |

固定版の OFF では、起動ごとの変更前との差は最大約0.34 msでした。変形対応版の OFF では、行列未接続の単体ドラッグと、行列変形中の再生が2組とも遅くなりました。
行列変形中の増分はキャッシュ OFF で0.44〜1.10 ms、ON で0.38〜0.41 msでした。表示を ON にすると、共通親ドラッグと両キャッシュ状態の再生が3条件とも長くなりました。

OFF と追加前の再生画像は、キャッシュ OFF／ON の各代表フレームで画素単位に一致しました。
OFF の描画は8頂点・12辺を1描画アイテムで扱い、属性の読み取りはベース形状の更新時に行いました。
SubScene の `requiresUpdate()` と `update()` では、OFF 時も線の分割や追加の描画アイテムに関する判定が残りました。
これらの判定は速度差の要因の候補です。計測はビルド全体の比較で、個々の処理の寄与は未特定です。
通常線とテンプレート線が混在する場合は、各辺の分割結果をローカル頂点として保持し、両方の描画アイテムで頂点バッファを共有しました。
変形対応版の再生では、同じローカル頂点を使い、両方の描画アイテムへ同じ行列を適用しました。
単体の GUI 検証では両ノードで中央と端のクリック選択、反転、割合 `0`／`1`、OFF に戻した後の表示とローカル境界を確認しました。
全試行・GUI 検証結果は `build/fixed_cube/template_line_20261121/summary.json`（Git 管理外）に保存しました。

#### 採用方針

部分テンプレート線は両 Cube への採用を見送り、追加前の仕様に戻しました。
今後は、部分テンプレート線の属性と描画処理を、その機能が必要なシェイプ型に限って実装します。
機能を追加するときは、対象の型ごとに追加前・追加後の未使用時・使用時を同じシーンで比較します。
共通親と単体のマニピュレータ操作に加え、Cached Playback OFF とキャッシュ充填済み ON の再生を測ります。

### Cube の Fin の試作

`bdShpL_Cube` と `bdShpL_DeformableCube` に、`shapeFin`、`shapeFinType`、`shapeFinHeight`、`shapeFinWidthScale` を静的な設定として追加する試作を行いました。
設定値を読むのは形状キャッシュの更新時に限り、本体の第2軸の Plus 面を基準に Fin を生成しました。
ON 時の Fin は本体と同じ描画アイテムに通常線として追加しました。変形対応版ではローカル頂点を再利用し、本体と同じ行列を適用しました。
OFF 時は8頂点・12辺の Cube を使い、再生中の描画更新は既存の形状リビジョンで判断しました。
SubScene では必要な場合に Fin データを確保し、描画状態の比較に使うデータから分離しました。
変形後の境界は、ロック中に取得した形状データを使い、変形後の Cube の8隅と Fin の頂点を含む範囲として求めました。

Maya 2025 / OpenGL で、共通親の下に transform と Cube の組を1,000個配置し、線色を揃えました。
`fa621ecf` の配布 DLL と Fin 追加版を2起動ずつ計測し、追加前後の起動順を入れ替えました。
各起動の5試行の中央値を集約し、表では追加前／追加後の Fin OFF／Fin ON（既定の `Standard`）の順に示します。
ドラッグは Move マニピュレータのマウス入力1回当たり、再生は実描画1フレーム当たりの ms です。
再生は共通親を X 方向に3 cm 移動する71描画です。行列接続条件では同時に入力の3軸スケールを1から5に変えました。
キャッシュ ON は Evaluation Cache を充填してから計測しました。

| シェイプ | 共通親ドラッグ | 単体ドラッグ | 再生・キャッシュ OFF | 再生・キャッシュ ON |
| --- | ---: | ---: | ---: | ---: |
| `bdShpL_Cube` | 8.11／8.22／8.52 | 3.06／3.31／3.26 | 2.58／2.69／2.60 | 3.14／3.13／3.24 |
| `bdShpL_DeformableCube`、行列未接続 | 12.31／12.54／12.52 | 8.78／8.95／9.20 | 9.96／10.19／10.10 | 10.40／10.79／10.62 |
| `bdShpL_DeformableCube`、行列を毎フレーム更新 | 13.95／14.00／14.07 | 10.22／10.22／10.23 | 12.43／12.77／12.70 | 12.96／13.27／13.26 |

固定版の Fin OFF はキャッシュ ON の再生で追加前に近く、単体ドラッグは両組で0.23〜0.27 ms 長くなりました。
変形対応版で行列を毎フレーム更新する単体ドラッグは、キャッシュ構造を調整する前の0.44〜0.67 ms の増分が、調整後の2組では0.09 ms 以内の差になりました。
再生には差が残り、行列接続中の Fin OFF でキャッシュ OFF は0.32〜0.37 ms、キャッシュ ON は0.25〜0.38 ms 長くなりました。
行列未接続でキャッシュ ON の再生では、Fin OFF が両組で約0.39 ms 長くなりました。
Fin ON と OFF の差は、全条件・各起動の中央値で最大0.48 msでした。

再生の代表フレームは Fin OFF と追加前で画素単位に一致し、Fin ON の画像はキャッシュ OFF／ON で一致しました。
単体の GUI では両ノードの Fin のクリック選択、`Standard`／`Tapered` の切り替え、幅0・高さ0、OFF への復帰と境界を確認しました。
計測データと画像は `build/fixed_cube/fin_20261121/` に保存しました（Git 管理外）。最終版の比較は `summary.json` にあります。

#### 採用方針

静的な形状キャッシュを使った試作でも、Fin OFF 時に追加前より時間がかかる条件が両組で確認されました。この比較はビルド全体の差を示しており、個々の処理の寄与は未特定です。
両 Cube への組み込みは見送り、追加前の仕様に戻しました。
今後は、Fin が必要な用途に専用のノード型を用意します。既存の Cube と同じシーンで、専用型の描画、マニピュレータ操作、Cached Playback OFF／ON の再生を評価します。

### Fin 専用型の寸法固定版と静的属性版

`bdShpL_CubeWithFin` は Geometry、`bdShpL_DeformableCubeWithFin` は SubScene を使います。
どちらも本体の軸・寸法に追従して Fin を生成し、本体と Fin を1つの描画アイテムで描きます。
変形対応版ではローカル頂点を共有し、本体と Fin に同じ `shapeDeformMatrix` を適用します。

| 研究 DLL | Fin の設定 |
| --- | --- |
| `bdShpCubeWithFinResearchFixed.mll` | `Standard`、高さ0.5 cm、幅倍率1.0を型の仕様で固定 |
| `bdShpCubeWithFinResearchAttributes.mll` | 同じ既定値で、静的な `shapeFinType`、`shapeFinHeight`、`shapeFinWidthScale` を追加 |

Fin 付きの両版は既定の形状で12頂点・15辺です。静的属性版で値を読むのは形状キャッシュの更新時だけです。
2つの DLL は同じノード型名と ID を使うため、版ごとに独立した Maya で読み込みます。
研究用 DLL は次のコマンドで `build/fixed_cube/maya2025/Release/` に生成します。

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -FinStudy
```

比較元は `991d8d86` の配布 DLL です。Maya 2025 / OpenGL で共通親の下に各型を1,000個置き、線色、カメラ、親子階層、行列入力を揃えました。
各版を2回起動し、1組目は現行 Cube、Fin 寸法固定、Fin 静的属性の順、2組目は逆順です。
各起動、各条件の5試行の中央値を使い、2起動の値を集約しました。
ドラッグは Move マニピュレータのマウス入力1回当たり、再生は実描画1フレーム当たりの ms です。
再生は共通親を X 方向に3 cm 移動する71描画で、行列接続条件では同時に入力元の3軸スケールを1から5まで変化させました。
Cached Playback ON は Evaluation Cache を充填してから計時しました。

各欄は現行 Cube／Fin 寸法固定／Fin 静的属性の順です。

| 描画方式・行列入力 | 共通親ドラッグ | 単体ドラッグ | 再生・キャッシュ OFF | 再生・キャッシュ ON |
| --- | ---: | ---: | ---: | ---: |
| Geometry | 8.11／8.39／8.28 | 3.02／3.05／3.22 | 2.57／2.53／2.67 | 3.11／3.15／3.17 |
| SubScene、行列未接続 | 12.37／12.26／12.40 | 8.79／8.80／9.62 | 9.88／10.05／10.24 | 10.41／10.29／10.61 |
| SubScene、行列を毎フレーム更新 | 13.82／13.66／14.02 | 10.06／9.84／10.21 | 12.56／12.16／12.58 | 13.05／12.61／13.24 |

Fin 寸法固定は、現行 Cube と比較した Geometry の共通親ドラッグが両組で0.25〜0.31 ms 長くなりました。
SubScene の行列変形中は、Fin 寸法固定の再生が両キャッシュ状態で0.30〜0.49 ms 短い値でした。この差には境界の計算と表示する形状の変更も含まれます。

同じ Fin の形状で比較すると、静的属性版では SubScene の行列変形中の再生がキャッシュ OFF で約0.42 ms、ON で0.59〜0.67 ms 長くなりました。
行列未接続の単体ドラッグは0.14 ms と1.50 ms の差で、起動によって増分が変わりました。
この比較は静的属性を備えるビルド全体の差を示し、Maya の評価と個々の処理の寄与は未特定です。

Fin 付き2版の再生の代表画像36枚と単体の画像は画素単位で一致しました。Fin の先端のクリック選択と、キャッシュ OFF／ON の描画一致も確認しました。
逆順の寸法固定版は計時前の初回描画で Viewport 2.0 が1回異常終了し、同じ DLL と条件で完了した再試行を集計に使用しました。
全試行の画像、計測、異常終了ログは `build/fixed_cube/fin_nodes_20261121/` にあります（Git 管理外）。集計は `summary.json` に保存しました。

### 未参照の bool 100個と再生速度

Fin 寸法固定の `bdShpL_CubeWithFin`（Geometry）と `bdShpL_DeformableCubeWithFin`（SubScene）で、比較用 `bool` の登録数を0個と100個にしました。
2つの研究 DLL はノードと描画のオブジェクトファイルを共有し、型の初期化で登録する比較用属性の数だけを変えています。
比較用属性の既定値は `false` です。キー・接続・Channel Box 表示の対象外で、外観やワールド空間への影響を持たず、計算・描画から参照される箇所もありません。

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -DummyBoolStudy
```

`build/fixed_cube/maya2025/Release/` に `bdShpCubeWithFinResearchBool0.mll` と `bdShpCubeWithFinResearchBool100.mll` を生成します。
型名と ID を揃え、独立した Maya で比較します。

Maya 2025 / OpenGL で同じ共通親の下に1,000個を配置し、Fin の形状・色・カメラを揃えました。
Geometry と SubScene の共通親を X 方向に3 cm 移動し、SubScene は同時に `shapeDeformMatrix` を変える条件も測りました。
行列接続条件では、入力元の3軸スケールを1から5まで変化させます。
0個と100個を別々に起動し、起動順とキャッシュ条件の順を逆にした比較も行いました。集計は正順・逆順の2組です。
シーン構築とキャッシュ充填を済ませた後の再生を計時し、各起動・条件の5試行の中央値を求めました。1試行は71回の実描画です。

表は起動ごとの中央値を2組で集約した値です。単位は ms／実描画です。組ごとの増分は100個版の値から0個版の値を引いています。

| 描画方式と再生条件 | キャッシュ | 0個 | 100個 | 組ごとの増分（正順／逆順） |
| --- | --- | ---: | ---: | ---: |
| Geometry・共通親 | OFF | 2.640 | 2.637 | +0.073／−0.080 |
| Geometry・共通親 | ON | 3.211 | 3.214 | −0.036／+0.043 |
| SubScene・共通親、行列未接続 | OFF | 10.079 | 10.139 | +0.084／+0.037 |
| SubScene・共通親、行列未接続 | ON | 10.505 | 10.679 | +0.176／+0.172 |
| SubScene・共通親と行列変形 | OFF | 12.654 | 12.757 | +0.576／−0.371 |
| SubScene・共通親と行列変形 | ON | 13.037 | 13.160 | +0.345／−0.099 |

Geometry は、増分の絶対値が最大0.080 ms で、組によって増減の向きが変わりました。
SubScene の行列未接続は両組で100個版の時間が延び、キャッシュ ON は約0.17 ms（約1.7%）の差でした。
毎フレームの行列変形を含む再生では、両キャッシュ条件で組によって増減の向きが変わりました。
この試験では属性を100個登録した条件で比較しており、少数の静的属性の増分や Maya 内部の要因は特定できていません。

キャッシュ ON では全71フレームが充填された状態を確認し、2組それぞれで0個版と100個版の代表フレーム画像が画素単位で一致しました（36比較）。
逆順の0個版は計時前に前面状態の確認で中断し、同じ設定の再試行を使用しました。追加反復の初回は、計時前の初期描画で Maya が異常終了しました。
集計は `build/fixed_cube/dummy_bools_20261121/summary.json`、各回の設定・結果・画像・中断ログは同ディレクトリ以下にあります（Git 管理外）。

### 軸・寸法と Fin の静的属性の読み取り・更新

同じローカル形状で、Geometry と SubScene の軸・寸法8属性を調べました。Cube は既定値を固定した版と、同じ値を属性から読む版を比較します。Fin 付き Cube は両版とも軸・寸法8属性を持ち、Fin の設定を寸法固定と静的3属性で比較します。

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -StaticAttributesStudy
```

`build/fixed_cube/maya2025/Release/` に `bdShpCubeStaticStudy{BaseFixed,BaseAttributes,FinFixed,FinAttributes}` の通常版と、名前末尾に `Profile` が付く診断版を生成します。同じ形状の比較ペアは描画と登録のオブジェクトファイルを共有します。比較する DLL は、専用プロファイルの Maya に1本ずつ読み込みます。

Maya 2025 / OpenGL で1,000個を配置し、共通親と単体を Move マニピュレータで操作しました。再生では共通親を3 cm 移動しました。SubScene では、共有 `transform.matrix` を `shapeDeformMatrix` に接続して、毎フレーム3軸スケールも変化させる条件を追加しました。

通常版の計時では、各条件の5試行から中央値を取りました。操作は1試行72個の Qt Move イベントで、1イベントあたりの時間を測ります。再生は1試行71実描画で、1実描画あたりの時間を測ります。再生はキャッシュ OFF と充填済み ON の両方で、代表3フレームの画素を照合します。

診断版の `bdCubeProfile` は、最初の描画と暖機後にリセットしました。軸・寸法8値の読み取り、Fin 3値の読み取り、ローカル形状へのアクセスと再生成、行列取得・適用、バッファ確定・関連付けを記録します。読み取りは、属性群をまとめて読む1回の処理を1と数えます。バッファの値は Maya SDK での処理回数です。診断版の時間は、計測自体の負荷を含むため通常版の比較から外します。

表は、正順・逆順それぞれの起動内中央値を2組で集約した値です。単位はドラッグが ms／イベント、再生が ms／実描画です。括弧内は組ごとの「属性版 − 固定版」の差を正順、逆順の順に記しています。

| 描画方式・行列の状態 | 操作・キャッシュ | 軸・寸法8属性（固定 → 属性、差） | Fin 3属性（固定 → 属性、差） |
| --- | --- | ---: | ---: |
| Geometry | 親ドラッグ | 8.141 → 8.419（+0.716／−0.160） | 9.210 → 8.299（−0.463／−1.359） |
| Geometry | 単体ドラッグ | 2.739 → 3.231（+0.673／+0.311） | 3.343 → 3.327（−0.149／+0.117） |
| Geometry | 再生 OFF | 2.659 → 2.698（+0.070／+0.008） | 2.777 → 2.759（+0.089／−0.124） |
| Geometry | 再生 ON | 3.384 → 3.409（+0.170／−0.120） | 3.377 → 3.259（−0.041／−0.196） |
| SubScene・未接続 | 親ドラッグ | 12.930 → 13.183（+0.472／+0.034） | 13.027 → 13.247（+0.476／−0.036） |
| SubScene・未接続 | 単体ドラッグ | 8.779 → 9.194（+0.907／−0.078） | 9.114 → 9.730（+0.296／+0.937） |
| SubScene・未接続 | 再生 OFF | 10.039 → 10.546（+0.615／+0.399） | 10.421 → 10.349（−0.207／+0.063） |
| SubScene・未接続 | 再生 ON | 10.497 → 11.085（+1.050／+0.126） | 11.018 → 10.844（−0.526／+0.178） |
| SubScene・行列接続 | 親ドラッグ | 13.990 → 14.589（+1.240／−0.041） | 14.722 → 14.188（−0.788／−0.279） |
| SubScene・行列接続 | 単体ドラッグ | 10.390 → 10.669（+0.912／−0.353） | 10.549 → 10.766（−0.239／+0.673） |
| SubScene・毎フレーム行列変形 | 再生 OFF | 12.633 → 13.177（+1.012／+0.078） | 12.781 → 13.060（+0.032／+0.527） |
| SubScene・毎フレーム行列変形 | 再生 ON | 13.039 → 13.509（+0.824／+0.116） | 13.429 → 13.424（−0.027／+0.016） |

軸・寸法8属性を持つ版は、Geometry の単体ドラッグで両組とも0.31〜0.67 ms／イベント、SubScene の行列未接続・キャッシュ OFF 再生で両組とも0.40〜0.62 ms／実描画長くなりました。Fin 属性付き版は、SubScene の行列未接続・単体ドラッグで0.30〜0.94 ms／イベント長くなり、親ドラッグは条件によって両組で短くなりました。同じペアの代表画像はすべて画素単位で一致しました（再生72比較）。

診断は既定形状の4起動に、非対称に寸法を調整した軸・寸法属性版と Fin 属性版の2起動を加えました。暖機後の計72条件で、軸・寸法と Fin の属性読み取り、ローカル形状キャッシュの取得・再生成、境界取得、頂点・インデックスバッファの確定・関連付けはすべて0回でした。Geometry の `updateDG()`、`updateRenderItems()`、`populateGeometry()` も0回でした。Geometry の再生では `requiresUpdateRenderItems()` が実描画ごとに1,000回呼ばれています。

1個の `shapeBaseSpace1stAxisPlus` または `shapeFinHeight` を変更する対照試験は14件実施しました。全件で該当ノードの境界が変わり、軸・寸法の読み取り、形状再生成、描画への反映を各1回検出しました。Fin 属性版は、この再生成の中で Fin 3値も1回読みました。

| SubScene の診断条件 | 実描画 | 表示状態の取得 | `shapeDeformMatrix` の取得 | `setMatrix()` |
| --- | ---: | ---: | ---: | ---: |
| 単体ドラッグ・行列未接続 | 74 | 74,000 | 0 | 68 |
| 共通親の再生・行列未接続 | 71 | 71,000 | 0 | 71,000 |
| 共通親の再生・毎フレーム行列変形 | 71 | 71,000 | 71,000 | 71,000 |

表の回数は比較ペアと調整済み形状で一致しました。再生の回数はキャッシュ OFF／ON とも同じです。ドラッグの診断区間はマウスの押下・解放も含みます。

基準形状の属性版で確認した速度差について、診断したプラグイン内の属性読み取り、形状再生成、描画更新の呼び出し回数は同じでした。Maya 内部の属性構成や属性フラグごとの寄与は未特定です。

SubScene の単体ドラッグでは、`requiresUpdate()` が全1,000個の表示状態を取得し、行列を設定する対象は移動した1個でした。表示状態の取得は、軸・寸法属性版の診断で約2.89 ms／実描画でした。先行試作で表示状態を再利用した結果を踏まえ、選択・色・可視性の変更を検知して必要なときにだけ取り直す方式が改善候補です。診断時間にはカウンターの計測負荷が含まれます。

集計は `build/fixed_cube/static_shape_attributes_20261121/summary.json`、設定・結果・画像・各起動のログは同ディレクトリ以下にあります（Git 管理外）。

### SubScene の軸・寸法8属性の再生差を再測定

前回の軸・寸法の固定値版（A）と8属性版（B）の通常 DLL を同じ SHA-256 のまま使用しました。Maya 2025 / OpenGL で SubScene の Cube 1,000個を行列未接続にし、キャッシュ OFF で共通親の X を0から3 cmまで動かしました。各起動で1回暖機再生し、71実描画の試行を5回計時して中央値を取りました。

独立した Maya の起動を A・A・B と B・A・A の順で2組ずつ行いました。A/A は後の固定値版から先の固定値版を引いた値、A/B は属性版から同じ組で直前または直後に起動した固定値版を引いた値です。各組の2種類の差には、共通の固定値版1起動が含まれます。

最初の4組では、シーンを組み立てたときに描画されない補助 `transform` が選択されていました。前回の選択なしの状態を再現するため、暖機前に選択を解除し、全試行の選択状態を照合した4組も計測しました。

単位は ms／実描画です。正の差は後者（A/A は後の起動、A/B は属性版）の時間が長いことを示します。

| 組 | 起動順 | 選択なし A/A | 選択なし A/B | 補助 transform 選択あり A/A | 補助 transform 選択あり A/B |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | A・A・B | −0.299 | −0.137 | +0.347 | −0.170 |
| 2 | B・A・A | +0.151 | +0.126 | −0.139 | +0.082 |
| 3 | A・A・B | +0.749 | −0.826 | +0.169 | +0.211 |
| 4 | B・A・A | +0.038 | +0.288 | −0.292 | −0.488 |

選択なしでは、A/A の差の絶対値の中央値は0.225 ms、最大は0.749 msでした。A/B の符号付き中央値は −0.006 msで、属性版が長い組と短い組が2組ずつでした。第3組は固定値版同士で0.749 ms離れ、属性版は先の固定値版と0.077 ms差でした。同じ DLL の起動間でも前回の +0.399／+0.615 ms に相当する差が出ました。

補助 transform 選択ありでも、属性版が長い組と短い組は2組ずつでした。扱った選択条件のどちらでも前回の方向・大きさの差は再現せず、今回は反復比較で判定しました。前回の差の発生要因は未特定です。

24起動すべてで実描画数、ビューポート、評価条件、DLL ハッシュを検証しました。各起動の代表3フレームは前回の画像と画素単位で一致しました（72比較）。集計は `build/fixed_cube/static_attributes_repeat_20261121/summary.json` と同ディレクトリの `selection_clear/summary.json` に保存しました（Git 管理外）。

### SubScene の表示状態の再利用

`bdShpL_DeformableCube` の描画で、色・可視性・選択可否などの表示状態を再利用する研究版を作りました。ノードと祖先の表示属性、シーンの色・選択、DAG や接続の変更を通知で確認します。ハイライト解除などを扱うため、各更新判定で `MGeometryUtilities::displayStatus()` とビューポートの表示スタイルを確認します。形状変形行列と DAG の最終行列は更新判定ごとに取得します。

表示レイヤーやアニメーションから表示属性に入力接続がある場合は、表示状態をその都度取得します。DAG の変更時には監視対象を再構築し、監視を確立できない場合も通常の取得経路を使います。Maya の属性変更通知は、再生・スクラブ中の変化について制約があります。 [Maya 2025 MNodeMessage](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_node_message.html)

```powershell
.\native\maya\experiments\fixed_cube\build.ps1 -MayaVersion 2025 -DisplayStateStudy
```

`build/fixed_cube/maya2025/Release/` に `bdShpCubeDisplayStateBaseline.mll` と `bdShpCubeDisplayStateCache.mll`、それぞれの `Profile` 版を生成します。

初回試作では、すべての更新判定で表示状態を取得しました。`MFnDependencyNode::getConnections()` が接続のないノードに返す `MS::kFailure` の判定が原因でした。有効なノードで結果が空の場合を未接続として扱うように修正し、Maya 2025 の C++ プローブで、未接続、行列のみ接続、表示属性への入力接続、祖先の表示属性への入力接続、表示レイヤーの各判定を確認しました。 [Maya 2025 MFnDependencyNode](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_fn_dependency_node.html)

Maya 2025 / OpenGL で基準版と研究版を独立して開き、選択・解除、ハイライト、RGB とインデックス色、表示レイヤーとテンプレート・参照、親の可視性、親変更、複製と削除を検証しました。接続による色と変形行列の変化、およびアニメーションした親の可視性は、キャッシュ OFF／ON の再生で照合しました。親の可視性はフレームジャンプでも確認しました。各版117件の判定、代表画像72比較、クリック選択14比較が一致しました。

再生時の非表示は `overridePlayback` を変更し、両版で同じ結果を確認しました。この検証シーンでは、Maya の DAG 表示フラグが非表示を示す状態でも、基準版と研究版の両方で再生中に描線が残りました。

速度比較は 1,000 個、単体と共通親の Move マニピュレータ操作、キャッシュ OFF／充填済み ON の再生で実施しました。行列未接続と、共有入力から `shapeDeformMatrix` が変わる場面を比較しました。操作は1試行72個の Qt Move イベント、再生は1試行71実描画です。通常版は各起動・条件で5試行の中央値を取り、基準版同士の起動と、順序を反転した基準版・研究版の起動を比較します。診断版は1試行で表示状態取得と更新を計数します。

| 条件 | 操作・キャッシュ | 基準版 → 研究版 | 研究版 − 基準版（正順／逆順） | 基準版同士（正順側／逆順側） |
| --- | --- | ---: | ---: | ---: |
| 行列未接続 | 共通親ドラッグ | 12.611 → 10.178 | −2.464／−2.402 | +0.234／+0.566 |
| 行列未接続 | 単体ドラッグ | 9.330 → 6.725 | −2.357／−2.852 | +0.108／−0.379 |
| 行列未接続 | 再生 OFF | 9.801 → 7.840 | −2.087／−1.835 | +0.322／−0.095 |
| 行列未接続 | 再生 ON | 10.187 → 8.443 | −1.539／−1.949 | +0.105／+0.195 |
| 行列接続 | 共通親ドラッグ | 13.643 → 12.013 | −1.643／−1.616 | −0.043／+0.109 |
| 行列接続 | 単体ドラッグ | 10.136 → 8.223 | −1.982／−1.844 | +0.400／−0.200 |
| 毎フレーム行列変形 | 再生 OFF | 12.064 → 12.279 | +0.387／+0.043 | −0.129／+0.164 |
| 毎フレーム行列変形 | 再生 ON | 12.734 → 12.848 | −0.066／+0.295 | +0.303／+0.278 |

単位はドラッグが ms／イベント、再生が ms／実描画です。各版の値は2起動の中央値を集約しています。行列未接続の4条件と行列接続のドラッグ2条件は両組で短縮しました。行列変形を含む再生は、キャッシュ OFF で両組とも延び、キャッシュ ON で差の向きが変わりました。通常版6起動と診断版2起動の代表画像はすべて画素単位で一致しました。

診断の全8条件で、基準版の色・可視性などをまとめて取得する処理は1実描画あたり1,000回、研究版では0回でした。研究版の `displayStatus()` 確認は1実描画あたり1,000回で、0.212〜0.296 ms／実描画でした。行列未接続・単体ドラッグでは `readState()` の診断時間が4.458から1.902 ms／実描画に短縮し、行列設定は両版とも74描画中68回でした。

行列変形の再生では両版とも、1実描画あたり行列の取得と `setMatrix()` が各1,000回でした。`readState()` の診断時間はキャッシュ OFF で5.639から3.484 ms、ON で6.147から4.138 ms／実描画に短縮しました。通常版の再生全体で短縮に結びつかなかった要因は未特定です。

画像・クリック選択の照合と計時の集計は `build/fixed_cube/subscene_display_cache_20261122/cache_active/summary.json` に保存しました。初回の判定修正前の比較は `build/fixed_cube/subscene_display_cache_20261122/summary.json` にあります（Git 管理外）。

### SubScene 表示状態キャッシュの導入前検証

毎フレーム行列を変える再生に絞り、前回の基準版（A）と研究版（B）の DLL をハッシュを揃えて再使用しました。Maya 2025 / OpenGL、1,000個で共有 `shapeDeformMatrix` と共通親の変換を変化させ、キャッシュ OFF と充填済み ON を測りました。各起動で条件ごとに71実描画を5試行し、中央値を集計しました。代表3フレームを前回と照合しました。

A・A・B、B・A・A を2組ずつ行いました。A/A は後の A から先の A を引いた差、A/B は B から同じ組で隣接する A を引いた差です。単位は ms／実描画です。

| 組 | 起動順 | キャッシュ OFF A/A | キャッシュ OFF A/B | キャッシュ ON A/A | キャッシュ ON A/B |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | A・A・B | −1.700 | −0.062 | +0.365 | −0.411 |
| 2 | B・A・A | +0.016 | −0.338 | +0.094 | +0.205 |
| 3 | A・A・B | +0.274 | −1.426 | +0.538 | −1.078 |
| 4 | B・A・A | −0.193 | −0.673 | −0.197 | −0.883 |

前回のキャッシュ OFF の遅れは再現しませんでした。A/B の中央値は OFF が −0.506 ms、ON が −0.647 msです。ON の第2組は0.205 ms延びた一方、A/A の起動差の絶対値は最大0.538 msでした。差の再現を条件とした Maya Profiler の診断は、今回は反復比較だけで判定しました。集計は `build/fixed_cube/subscene_display_adoption_20261122/repeat/summary.json` に保存しました（Git 管理外）。

同時に開いた2つのビューポートで、別々の表示スタイル、ハイライト、Isolate Select を検証しました。祖先およびシェイプ直上の transform を表示レイヤーへ所属させ、キャッシュ OFF／ON でアニメーションした祖先の可視性を照合しました。描画済みのノードを削除して DLL を通常の手順でアンロードし、同じ DLL を再読み込みして描画とクリック選択を確認しました。初回の比較は各版79件の判定を通過し、画像43比較とクリック選択10比較が一致しました。

GUI 検証は専用の Maya プロファイルで行いました。Maya 本体の通常終了を試した際は終了通知後も試験プロセスが残り、専用設定が保存されました。最終比較では同じ専用設定から起動し、DLL の再読み込みと描画を確認した後に、試験プロセスを自己終了させました。この手順では両版の起動前後でプロファイルのハッシュが一致しました。

さらに、1,000個のうち500個の直上の transform を同じ表示レイヤーへ入れました。残る500個は既定レイヤーに置き、同じ共通親の下に配置しました。単体ドラッグは既定レイヤーのコントローラー1個を操作しました。基準版と初回の研究版を正順・逆順で起動しました。各条件は1起動につき5試行、ドラッグは1試行72個の Qt Move イベント、再生は1試行71実描画です。

| 条件 | 操作・キャッシュ | 基準版 → 初回研究版 | 初回研究版 − 基準版（正順／逆順） |
| --- | --- | ---: | ---: |
| 行列未接続 | 共通親ドラッグ | 12.524 → 11.817 | −0.497／−0.916 |
| 行列未接続 | 単体ドラッグ | 8.818 → 8.285 | −0.236／−0.830 |
| 行列未接続 | 再生 OFF | 9.667 → 9.162 | −0.275／−0.735 |
| 行列未接続 | 再生 ON | 10.169 → 9.649 | −0.260／−0.779 |
| 行列接続 | 共通親ドラッグ | 13.903 → 12.927 | −0.851／−1.101 |
| 行列接続 | 単体ドラッグ | 9.847 → 9.633 | −0.086／−0.343 |
| 毎フレーム行列変形 | 再生 OFF | 12.031 → 13.026 | +1.280／+0.711 |
| 毎フレーム行列変形 | 再生 ON | 12.641 → 13.725 | +1.515／+0.652 |

単位はドラッグが ms／イベント、再生が ms／実描画です。診断では、毎実描画で表示状態の完全取得が1,000回から500回に減りました。行列変形再生の時間は、キャッシュ OFF／ON ともに両順で延びました。初回の実装は表示状態を毎回取得するパスにも属性変更と dirty の通知を登録していたため、表示状態を再利用するパスだけに登録するよう研究版を修正しました。表示レイヤーの所属変更や付け替えは、シーン全体の通知でパスを再判定します。最初の GUI 比較と混在レイヤーの集計は `build/fixed_cube/subscene_display_adoption_20261122/readiness/` の `correctness_summary.json` と `layers_summary.json` に保存しました（Git 管理外）。

修正版と基準版の GUI 比較は各116件の判定を通過し、画像53比較とクリック選択16比較が一致しました。同じ親を持つコントローラーの片方を描画中に表示レイヤーへ追加し、親の色・可視性変更を両方で照合しました。既定レイヤーへ戻した後も、親の色変更が両方へ反映されました。Maya 2025 の C++ プローブでは、表示レイヤーや祖先のアニメーション表示接続があるパスだけで使われるノードに属性監視が登録されず、再利用可能な兄弟と共有する祖先には監視が残り、接続解除後に監視が再登録されることを確認しました。GUI の集計は `build/fixed_cube/subscene_display_adoption_20261122/readiness_refined/correctness_summary.json` に保存しました（Git 管理外）。

同じ混在レイヤーのシーンで、基準版と修正版を新しく起動して再比較しました。両順で同じ基準版の DLL を使用しました。

| 条件 | 操作・キャッシュ | 基準版 → 修正版 | 修正版 − 基準版（正順／逆順） |
| --- | --- | ---: | ---: |
| 行列未接続 | 共通親ドラッグ | 12.957 → 11.751 | −1.912／−0.500 |
| 行列未接続 | 単体ドラッグ | 9.288 → 7.776 | −1.584／−1.440 |
| 行列未接続 | 再生 OFF | 10.002 → 9.076 | −0.932／−0.920 |
| 行列未接続 | 再生 ON | 10.692 → 10.008 | −0.883／−0.484 |
| 行列接続 | 共通親ドラッグ | 13.894 → 13.493 | −0.770／−0.031 |
| 行列接続 | 単体ドラッグ | 10.320 → 9.785 | −0.537／−0.532 |
| 毎フレーム行列変形 | 再生 OFF | 12.952 → 12.645 | −0.315／−0.300 |
| 毎フレーム行列変形 | 再生 ON | 13.006 → 12.979 | −0.369／+0.314 |

ドラッグと行列未接続の再生は両順で短縮しました。行列変形の再生 OFF も両順で約0.3 ms短縮し、ON は基準版とほぼ同じでした。診断版では修正後も、全8条件で完全取得が1実描画あたり1,000回から500回に減りました。再生の代表画像は両版で一致しました。集計と DLL ハッシュは `build/fixed_cube/subscene_display_adoption_20261122/readiness_refined/` の `layers_summary.json` と `artifact_hashes.json` に保存しました（Git 管理外）。

初回実装で見られた混在レイヤーの再生低下が再現しなかったため、修正版を既存の `bdShpL_DeformableCube` に採用しました。ノード型名、MTypeId、属性の契約を保ち、`bdUtilNodes` の登録完了後に監視を開始します。ノードと描画オーバーライドを登録解除できた時点で監視を解除します。表示状態取得の比較ビルドでは、引き続き基準版だけを監視なしでビルドします。

Maya 2025 の配布用 `bdUtilNodes.mll` を同じ GUI 手順で照合し、116件の判定、基準版との画像53比較とクリック選択16比較、再読み込み後の描画と選択が通りました。Maya 2026／2027 のスタンドアロン C++ プローブでは、各配布 DLL を読み込み、表示状態の再利用可否、共有祖先の監視、接続解除後の監視の再登録、アンロードを確認しました。3バージョンのリリース統一検証は `verify.cmd -IncludeNative -Release -IncludeCubeResearch` で通過しました。GUI とプローブの結果は `build/fixed_cube/subscene_display_adoption_20261122/` の `packaged/` と `packaged_headless/` に保存しました（Git 管理外）。

### SubScene の行列取得と DAG パスの再利用

表示状態を再利用する配布版（`be0697a4`）を基準に、Maya 2025.3.3 / OpenGL で1,000個の `bdShpL_DeformableCube` を計測しました。各シェイプは個別の transform を持ち、その上に共通親があります。再生中はすべての条件で共通親を X 方向に3 cm 移動しました。行列未接続、共有 `transform.matrix` の単位行列を接続、同じ入力を3軸スケール1から5まで変化させる、の3条件です。Cached Playback は OFF と充填済みの Evaluation Cache を比較しました。

ネイティブ診断版では、1実描画あたりの累積時間を以下のように観測しました。計測処理の負荷が入り、入力プラグの取得は形状行列取得の内側にあります。

| 再生時の区間 | 行列未接続 OFF／ON | 単位行列の接続 OFF／ON | 行列変形 OFF／ON |
| --- | ---: | ---: | ---: |
| DAG パス取得と有効性の確認 | 1.10／1.01 | 1.14／1.09 | 1.27／1.11 |
| 親階層を含むワールド行列の取得 | 0.17／0.15 | 0.17／0.16 | 0.19／0.17 |
| 形状行列の取得 | 0.16／0.16 | 1.78／1.75 | 2.08／2.56 |
| うち `MPlug::asMObject()` | 0.00／0.00 | 1.35／1.34 | 1.55／2.16 |
| 2行列の積 | 0.04／0.04 | 0.04／0.04 | 0.05／0.04 |
| `MRenderItem::setMatrix()` | 0.80／0.80 | 0.95／0.95 | 1.09／1.03 |

単位は ms／実描画です。行列を接続すると、単位行列で固定していても、1実描画につき1,000回のプラグ取得が発生しました。単体ドラッグでは行列設定はほぼ1回／実描画でしたが、DAG パスの取得は1,000回で、約1.0〜1.3 ms／実描画でした。

別起動で配布 DLL を Maya Profiler で記録したところ、`Vp2PrepareToUpdate` は未接続で6.02／6.14 ms、固定行列を接続すると7.63／7.50 ms、毎フレーム変形では7.59／9.04 msでした（OFF／ON、いずれも ms／実描画）。`Vp2Draw3dBeautyPass` は全6条件で0.64〜0.76 msでした。プロファイルは各条件1試行で、ネイティブ区間計測とは別の試行です。

DAG パスの再利用版は、既存の DAG や接続の変更通知を利用してパスを取得し直します。変形行列とワールド行列は、両版で各更新判定時に取得します。診断版では暖機後の全12条件で、`MFnDagNode::getPath()` の呼び出しが1,000回／実描画から0回になりました。

2つのビューポートで各版142件の判定を通過し、画像59比較と画面選択23比較が一致しました。直上の親と祖先の付け替え、付け替え後の Undo／Redo、transform 名の変更、移動前の辺が選択されないことを確認しました。両版でプラグインを再読み込みし、描画と選択を確認した後に試験プロセスを自己終了させました。

計時は診断なしで基準版（A）と再利用版（B）を A・A・B、B・A・A の順で起動し、各条件で5試行しました。ドラッグは1試行72個の Qt Move イベント、再生は1試行71実描画です。各版の値は同じ組で隣接する A と B の起動別中央値を、2組で集約しました。A/B は B から隣接する A を引いた差、A/A は後の A から先の A を引いた差です。曲線の対照は別の1起動で測り、未接続の行は制御点接続なし、行列アニメーションありの行は1本16個の `pointMatrixMult` で CV を駆動しました。すべての再生で共通親を同じ軌跡で動かし、ドラッグは入力スケール1のフレームで行いました。

| 行列の条件 | 操作 | 基準版 | 再利用版 | A/B（正順／逆順） | A/A（正順／逆順） | `nurbsCurve` |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 未接続 | 共通親ドラッグ | 10.341 | 10.376 | −0.049／+0.120 | +0.169／−0.048 | 8.110 |
| 未接続 | 単体ドラッグ | 6.695 | 6.625 | −0.232／+0.090 | +0.391／−0.014 | 2.876 |
| 未接続 | 再生 OFF | 7.905 | 7.593 | −0.573／−0.050 | +0.204／+0.331 | 2.638 |
| 未接続 | 再生 ON | 8.710 | 8.155 | −0.807／−0.303 | +0.660／+0.147 | 3.263 |
| 単位行列を接続 | 共通親ドラッグ | 12.019 | 12.068 | +0.261／−0.162 | −0.197／−0.044 | — |
| 単位行列を接続 | 単体ドラッグ | 8.434 | 8.352 | −0.521／+0.357 | +0.073／+0.130 | — |
| 単位行列を接続 | 再生 OFF | 9.706 | 9.762 | −0.037／+0.149 | −0.131／+0.288 | — |
| 単位行列を接続 | 再生 ON | 10.184 | 10.402 | +0.155／+0.282 | −0.465／+0.699 | — |
| 行列アニメーションあり | 共通親ドラッグ | 12.025 | 12.299 | +0.061／+0.487 | +0.139／+0.761 | 8.552 |
| 行列アニメーションあり | 単体ドラッグ | 8.495 | 8.481 | −0.141／+0.114 | −0.169／+0.272 | 2.533 |
| 行列アニメーションあり | 再生 OFF | 11.937 | 12.308 | +0.038／+0.703 | +0.296／+0.700 | 24.034 |
| 行列アニメーションあり | 再生 ON | 12.662 | 12.828 | −0.174／+0.508 | +0.096／+0.577 | 18.964 |

表の単位はドラッグが ms／イベント、再生が ms／実描画です。行列未接続の再生は両方の起動順で短縮し、ON の短縮幅は0.30〜0.81 msでした。ドラッグでは、共通親・単体を通じて両順で短縮した条件はありませんでした。行列変形を伴う再生の差は、同じ基準版を起動し直したときの差の範囲に収まるか、ほぼ同じ大きさでした。再利用版は研究用のビルドとして保管し、配布版への採用を見送りました。

試作ソース、DLL ハッシュ、起動ごとの計測と Profiler 出力、画像、集計 `summary.json`、機能比較 `correctness.json` は `build/fixed_cube/subscene_matrix_path_20261122/` に保存しました（Git 管理外）。

### 個別の変形行列と dirty 伝搬

本番リグに合わせ、Maya 2025.3.3／OpenGL で `bdShpL_DeformableCube` 1,000個に、別々の `transform.matrix` を1本ずつ直接接続しました。3条件とも共通親を X 方向に3 cm 動かし、変形入力のうち0個、1個、1,000個に XYZ スケールのキーを付けました。独立した入力の終端スケールは4〜5に分布させました。配布版 `be0697a4` の Maya 2025 DLL で、キャッシュ OFF → ON と ON → OFF の順に別起動し、各条件で5試行、1試行71実描画を測りました。ON は `syncOnly` で充填し、全計時フレームが有効なことを確認しました。各条件で再生中に記録した3フレームの画像は、キャッシュ OFF の参照画像と一致しました。

| 変化する変形入力 | OFF → ON の起動での OFF／ON | ON → OFF の起動での OFF／ON | ON − OFF（正順／逆順） |
| --- | ---: | ---: | ---: |
| 1,000個 | 14.37／14.28 | 14.92／14.52 | −0.09／−0.39 |
| 1個 | 9.44／9.93 | 9.70／10.16 | +0.49／+0.47 |
| 0個 | 10.59／10.43 | 9.69／10.02 | −0.16／+0.33 |

単位は ms／実描画で、OFF／ON は各起動の中央値です。1,000個とも変形すると再生時間は近く、1個だけ変形させると ON が両起動で約0.5 ms 長くなりました。固定入力では差の符号が起動順で入れ替わりました。

別起動で配布 DLL を Maya Profiler で記録しました。最初の35実描画の記録では全変形の OFF がバッファ上限に達したため、23実描画で取り直し、全6条件でトレース内の描画数と描画コールバック数が一致しました。表はメインスレッドの各区間の経過時間（ms／実描画、OFF／ON）です。

| 変化する変形入力 | `EvaluationGraphExecution` | `Vp2PrepareToUpdate` |
| --- | ---: | ---: |
| 1,000個 | 8.50／6.65 | 8.46／10.43 |
| 1個 | 0.89／2.57 | 8.27／9.26 |
| 0個 | 0.89／2.24 | 8.17／8.02 |

OFF の `EvaluateNode` に記録された Cube は、変化する入力数と同じ1,000個、1個、0個でした。ON の `RestoreNodeCache` には、全条件で Cube 1,000個と各 Cube の親 transform 1,000個が記録されました。変形入力元は変化する数だけ復元されました。全変形では、ON で短くなった評価グラフ区間と長くなった描画準備区間が各約2 ms でした。固定・1個だけ変形の条件では、再評価する変形入力が少なく、ON 側の評価グラフ区間が長くなりました。Profiler の計時には記録の負荷が入ります。

診断 DLL では、`shapeDeformMatrix` に対する `setDependentsDirty()`、評価フック、描画が観測したローカル変形行列を計数しました。表は71実描画の平均呼び出し数で、OFF／ON の順です。`dirtyPlugExists()` が真だったフックだけを「入力 dirty」として数えています。

| 変化する変形入力 | `setDependentsDirty()` | `preEvaluation()` の入力 dirty | `postEvaluation()` 全体 | `postEvaluation()` の入力 dirty | 描画で取得した変形行列 | 描画で値が変わった変形行列 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1,000個 | 0／0 | 1,000／0 | 1,000／1,000 | 1,000／1,000 | 1,000／1,000 | 1,000／1,000 |
| 1個 | 0／0 | 1／0 | 1／1,000 | 1／1 | 1,000／1,000 | 1／1 |
| 0個 | 0／0 | 0／0 | 0／1,000 | 0／0 | 1,000／1,000 | 0／0 |

充填済み ON では全条件で `preEvaluation()` が0回、通常コンテキストの `postEvaluation()` が1,000回／実描画でした。Autodesk の Maya 2025 API リファレンスではキャッシュ復元処理中の `preEvaluation()`／`postEvaluation()` 呼び出しを否定しています。ここで観測したのは充填済み再生区間における呼び出しであり、復元処理内のどの段階から呼ばれたかは未確認です。[Autodesk Maya 2025 MPxNode](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_px_node.html)

フレーム1のまま入力1個の値を設定したときは、DG と Parallel の両方で対象1個の `setDependentsDirty()` を観測し、`preEvaluation()`／`postEvaluation()` は0回でした。Parallel で入力元を Move マニピュレータで動かした実描画でも、対象1個に同じ dirty 通知が届き、描画行列の変更と境界の移動を確認しました。これらの実描画でも、1,000個すべての入力を読みました。共通親の移動を伴う再生では、全条件で `MRenderItem::setMatrix()` が1,000回／実描画でした。固定入力の再利用を試す場合は、ワールド行列の反映を維持しつつローカル変形行列の取得だけを減らせるかが比較点です。

診断 DLL での `MPlug::asMObject()` の累積計時は、全入力変形で1.43／2.63 ms、1個だけ変形で1.35／1.62 ms、固定入力で1.39／1.38 ms でした（OFF／ON、ms／実描画）。全入力変形では1,000個すべてで新しい値を扱うため、入力 dirty で不要な読み取りを減らす試作とは別に、変更された入力を1個読むコストも調べる余地があります。

配布版の計時、画像、診断 DLL と生成スクリプト、Profiler トレース、集計 `summary.json` と `profile_summary.json` は `build/fixed_cube/individual_matrix_dirty_20261123/` に保存しました（Git 管理外）。

### 変形行列の取得方法と dirty による再利用

Maya 2025.3.3／OpenGL で、前節と同じ独立した入力元1,000個を用いました。診断版で `MPlug` の生成と `asMObject()` の値の取得を個別に計時しました。表は71実描画の累積時間を実描画数で割った値（ms／実描画、OFF／ON）です。各区間で毎描画1,000件を計数しており、診断版の計測処理が入ります。

| 変化する変形入力 | `MPlug` 生成 | `asMObject()` |
| --- | ---: | ---: |
| 1,000個 | 0.14／0.14 | 1.72／3.42 |
| 1個 | 0.12／0.12 | 1.47／1.47 |
| 0個 | 0.12／0.12 | 1.56／1.44 |

行列取得の研究版は、ノードごとに non-networked `MPlug` の参照を保持する版と、都度 `asMDataHandle()` で取得したデータを `MFnMatrixData` で読む版を用意しました。初期の `MDataHandle::asMatrix()` 版は初期描画で失敗しました。`shapeDeformMatrix` は `MFnTypedAttribute` の matrix であり、`asMatrix()` は `MFnMatrixAttribute` で作られた属性向けです。[Autodesk Maya 2025 MPlug](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_plug.html) · [Autodesk Maya 2025 MDataHandle](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_data_handle.html)

dirty 研究版は、通常の評価コンテキストで接続済み行列の値を SubScene の描画側で保持し、`setDependentsDirty()` と `postEvaluation()` の入力 dirty、直接設定・接続・切断で失効させます。バウンディングボックスには現行と同じ直接取得を使います。診断版では、変化する入力が1,000個／1個／0個の場合に、OFF／充填済み ON とも毎描画の読み取りがそれぞれ1,000／1／0件でした。同一フレームで数値を編集すると、DG と Parallel の両方で対象1個を読み直しました。

診断なしの計時は、同じソースとビルド設定の研究用基準版から始める順序と、dirty 版・ハンドル経由版・プラグ再利用版を経て基準版に戻る逆順で行いました。各 DLL は別起動し、キャッシュ ON／OFF の順序も反転しました。各条件で5試行の中央値を使い、再生は71実描画、ドラッグは72個の Qt Move イベントすべてで実描画を確認しました。取得方法の2版は全入力が変形する再生を、dirty 版は3種の再生と、固定入力での共通親・1個の入力元のドラッグを比較しました。

| 研究版 | 全入力変形の再生 | 正順の 基準 → 研究版 | 逆順の 基準 → 研究版 |
| --- | --- | ---: | ---: |
| `MPlug` 再利用 | OFF | 15.78 → 15.06 | 14.70 → 15.01 |
| `MPlug` 再利用 | ON | 15.30 → 15.43 | 15.08 → 15.16 |
| 型に対応したハンドル経由 | OFF | 15.78 → 15.79 | 14.70 → 15.08 |
| 型に対応したハンドル経由 | ON | 15.30 → 15.16 | 15.08 → 15.07 |

| dirty 版の条件 | 正順の 基準 → 研究版 | 逆順の 基準 → 研究版 |
| --- | ---: | ---: |
| 全入力変形・再生 OFF | 15.78 → 15.73 | 14.70 → 15.06 |
| 全入力変形・再生 ON | 15.30 → 14.88 | 15.08 → 15.02 |
| 1個の入力が変形・再生 OFF | 10.55 → 8.73 | 9.88 → 7.99 |
| 1個の入力が変形・再生 ON | 10.74 → 9.00 | 10.30 → 8.85 |
| 固定入力・再生 OFF | 10.14 → 8.36 | 10.12 → 8.21 |
| 固定入力・再生 ON | 10.63 → 8.86 | 10.79 → 8.85 |
| 固定入力・共通親の Move | 12.85 → 10.96 | 12.36 → 11.12 |
| 固定入力・1個の入力元の Move | 8.56 → 7.04 | 8.39 → 6.42 |

単位は再生が ms／実描画、ドラッグが ms／イベントです。行列取得方法の2版では、全入力変形の再生を安定して短縮できませんでした。dirty 版は1個だけ変形する再生、固定入力の再生、2種類のドラッグが両順で1.24〜1.97 ms 短縮しました。全入力変形では OFF の差の符号が変わり、ON の短縮幅は0.07〜0.42 msでした。

9個の Cube の機能試験では、診断なしの3研究版とも47枚の画像が基準版と一致しました。OFF の参照16枚、充填済み ON の逆再生15枚と順序を飛ばしたスクラブ8枚、同一フレームでの編集・Undo／Redo・接続差し替えとその Undo・切断・再接続の8枚です。スクラブと編集ではローカル境界を数値でも照合しました。dirty 診断版では逆再生・スクラブ256回と同一フレーム編集65回の再利用を直接取得値と比較し、不一致は0件でした。配布前の候補として、dirty 版は各 Maya バージョンと本番に近い接続構成での追加確認に値します。

研究版のソース、DLL ハッシュ、起動ごとの計測と画像、集計 `summary.json` は `build/fixed_cube/matrix_read_followup/` に保存しました（Git 管理外）。

### 変形行列の再利用を配布版へ導入

`bdShpL_DeformableCube` の SubScene 描画へ接続済み行列の再利用を導入しました。接続、値の直接編集、`setDependentsDirty()` と通常コンテキストの `postEvaluation()` で行列の世代を進め、描画側では同じ世代の行列を使います。評価側が触るのは原子的な世代番号で、描画で保持する行列は各オーバーライドが管理します。バウンディングボックスの照会には直接取得を使います。

配布 DLL の導入前後を Maya 2025／OpenGL、1,000個で比較しました。再生中は共通親を X 方向に3 cm 動かし、未接続、独立した1,000本の固定入力、1個だけ変形、1,000個すべて変形を測りました。旧版・更新版の起動順とキャッシュ ON／OFF の順を反転し、各条件を5試行しました。表は実描画71回の再生または72回の Qt Move イベントの中央値で、更新版から旧版を引いた値です。

| 条件 | 操作 | 正順 | 逆順 |
| --- | --- | ---: | ---: |
| 未接続 | 再生 OFF | −0.26 | −0.15 |
| 未接続 | 再生 ON | −0.24 | −0.06 |
| 未接続 | 共通親 Move | −0.75 | +0.03 |
| 未接続 | 単体 Move | −0.56 | −0.65 |
| 固定入力 | 再生 OFF | −2.66 | −2.01 |
| 固定入力 | 再生 ON | −2.48 | −2.22 |
| 固定入力 | 共通親 Move | −2.40 | −1.81 |
| 固定入力 | 1個の入力元の Move | −1.47 | −2.42 |
| 1個だけ変形 | 再生 OFF | −2.02 | −2.18 |
| 1個だけ変形 | 再生 ON | −2.18 | −1.85 |
| 全入力変形 | 再生 OFF | −0.58 | −0.05 |
| 全入力変形 | 再生 ON | −0.34 | +0.09 |

単位は再生が ms／実描画、Move は ms／イベントです。1個だけの変形、固定入力の再生と Move が両順で短縮しました。未接続の共通親 Move と全入力変形の ON では、起動順によって差の符号が変わりました。

Maya 2025／2026／2027 の実描画では、充填済み ON の順再生16フレーム、逆再生15フレームとスクラブ8回で、各バージョンの OFF の参照と一致しました。同一フレームでの値設定、Undo／Redo、接続の差し替えとその Undo、切断、再接続も確認しました。Maya 2025 では、研究用基準版との画像47枚も一致しました。固定の `bdShpL_Cube` と `bdShpL_FocusBoundingBox` は既存の静的属性によるキャッシュ無効化を使用し、3バージョンで寸法編集と Undo／Redo 後の描画・境界を確認しました。フォーカス用 Box は `showShape=OFF` で寸法を編集した後もフレーミングが追従する回帰テストを追加しました。

配布 DLL のハッシュ、画像、各試行と集計 `summary.json` は `build/fixed_cube/production_matrix_dirty/` に保存しました（Git 管理外）。

### 共通親を固定した場合と移動した場合の再生

行列再利用を導入した配布版（`c5ae427d`）を Maya 2025.3.3／OpenGL で計測しました。共通親の直下に個別の transform を1,000個置き、それぞれに `bdShpL_DeformableCube` と専用の `transform.matrix` を1本ずつ割り当てました。変形入力0個、1個、1,000個の XYZ スケールを変え、共通親の X 移動を0 cm固定と0〜3 cmの2通りで比較しました。

全条件で共通親から独立した短い標準カーブ1本を画面上部で動かし、Cube がすべて静止する条件でも再生による実描画を数えました。静止条件ではカーブの位置だけが変わり、Cube の領域はフレーム2と72で画素単位に一致しました。他の5条件では両領域の変化を確認しました。全条件で OFF と充填済み ON の再生画像3枚を OFF の参照画像と照合しました。

各条件で71実描画を5回計時しました。表の値は起動ごとの試行中央値（ms／実描画）で、条件とキャッシュの順序を反転した2起動を「正順／逆順」で示します。ON は計時前後とも71フレームのキャッシュが有効でした。

| 変化する入力 | キャッシュ | 共通親固定 | 共通親移動 | 移動 − 固定 |
| ---: | --- | ---: | ---: | ---: |
| 0個 | OFF | 4.93／5.40 | 7.91／8.36 | +2.98／+2.96 |
| 0個 | ON | 4.85／5.08 | 8.39／8.67 | +3.54／+3.60 |
| 1個 | OFF | 4.88／5.64 | 8.51／8.41 | +3.63／+2.76 |
| 1個 | ON | 5.06／5.03 | 8.70／9.34 | +3.64／+4.31 |
| 1,000個 | OFF | 14.38／14.74 | 15.43／15.54 | +1.05／+0.80 |
| 1,000個 | ON | 13.69／13.94 | 15.38／15.12 | +1.69／+1.19 |

1個だけ変形する再生では、共通親を動かすと2.76〜4.31 ms／実描画増えました。1,000個すべてが変形する再生は、共通親を固定した場合も13.69〜14.74 ms／実描画かかりました。

配布版と同じ描画処理に計数と計時を加えた診断版では、OFF／ON とも同じ回数を観測しました。以下は1実描画あたりです。`update()` と `setMatrix()` の回数は全条件で一致しました。

| 共通親 | 変化する入力 | `requiresUpdate()` | うち更新不要 | `update()`／`setMatrix()` | 変形行列のプラグ取得 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 固定 | 0個 | 1,000 | 1,000 | 各0 | 0 |
| 固定 | 1個 | 1,000 | 999 | 各1 | 1 |
| 固定 | 1,000個 | 1,000 | 0 | 各1,000 | 1,000 |
| 移動 | 0個 | 1,000 | 0 | 各1,000 | 0 |
| 移動 | 1個 | 1,000 | 0 | 各1,000 | 1 |
| 移動 | 1,000個 | 1,000 | 0 | 各1,000 | 1,000 |

共通親固定・1個変形では、更新不要と返した999個の判定に診断版で3.08／3.00 ms（OFF／ON）かかりました。その描画で1,000個分行った DAG パス取得と有効性確認は1.20／1.07 ms、ワールド行列取得は0.17／0.18 msでした。これらは `requiresUpdate()` 内の区間で、診断処理の負荷を含みます。全12条件で暖機後の表示値の再取得とジオメトリの再登録は0回でした。

別起動の Maya Profiler では、各条件で23実描画を記録し、描画コールバックとトレースの件数を照合しました。以下の時間はメインスレッドの ms／実描画です。採取処理の負荷を含みます。

| 変化する入力 | 共通親 | `EvaluationGraphExecution` OFF／ON | `Vp2PrepareToUpdate` OFF／ON |
| ---: | --- | ---: | ---: |
| 0個 | 固定 | 0.19／0.15 | 4.43／4.31 |
| 0個 | 移動 | 0.99／2.48 | 6.53／6.24 |
| 1個 | 固定 | 0.27／0.21 | 5.27／4.30 |
| 1個 | 移動 | 1.01／2.76 | 6.72／8.05 |
| 1,000個 | 固定 | 7.62／4.85 | 8.50／10.51 |
| 1,000個 | 移動 | 8.47／6.33 | 8.62／9.74 |

充填済み ON の1個変形では、`RestoreNodeCache` に記録された Cube の shape と直上の transform は、共通親固定で1／0個、移動で1,000／1,000個でした。配布版の計時でも、共通親固定・1個変形で ON が一貫して遅くなる結果は出ず、共通親を動かす場合は両起動で ON の時間が長くなりました。

少数のコントローラーだけが変形する場面では、変更のない Cube の更新判定を早く終了できるかが次の調査候補です。共通親や個別 transform の行列、表示・選択、レンダラーの変更が描画に反映されることも判定短縮の前提になります。全入力が変形する場面では、共通親固定でも1,000個の `setMatrix()` と1,000本のプラグ取得があり、評価グラフと描画準備の両方に時間がかかります。

集計 `summary.json`、Profiler の集計 `profile_summary.json`、試行ごとの結果と画像、診断版のソースとハッシュを `build/fixed_cube/sparse_parent_playback/` に保存しました（Git 管理外）。

### SubScene の更新不要判定を短縮する試作

Maya 2025.3.3／OpenGL で、`requiresUpdate()` が毎回組み立てる描画状態を、変更のない場合に再利用する試作を作りました。DAG や接続の変更を監視してパスを取り直します。保持したパスからワールド行列を毎回読み、形状行列と寸法の世代、表示状態の世代・表示スタイル・選択などの表示ステータス、レンダラーとコンテナの状態を確認します。値がすべて一致する場合は、ローカル行列との合成や描画状態の再構築を省きます。照合版は省いた判定を独立に計算し直し、不一致なら取得した状態で描画を更新します。

ワールド行列の取得を通知だけに置き換えられるかも調べました。Autodesk の仕様では、`MDagMessage::addWorldMatrixModifiedCallback()` は変換を汚した最初の変更で呼ばれます。試験では変換が変わった189件のうち174件で、ワールド行列を読み取る前に通知が届きませんでした。親・子の移動と回転を試した区間は11件すべてで通知を確認しましたが、親の回転・子の `offsetParentMatrix`・形状変形を組み合わせた順再生では、OFF、充填済み ON とも51件すべてで通知を確認できませんでした。試作の計時にはワールド行列を読み続ける版を使いました。[Autodesk Maya 2025 MDagMessage](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_dag_message.html)

1,000個を使った照合でも、共通親移動中の行列変化426,000件すべてで、読み取り前に通知が来ないことを確認しました。共通親固定では、変形入力0個のとき1実描画あたり1,000件、1個変形のとき999件の判定を短縮できました。全12条件で短縮の対象になった283,858件を比較し、不一致は0件でした。

配布版、照合版、診断を外した試作版は各290項目の動作確認を通過しました。2ビューポートの静止画像102枚、再生画像53枚、参照画像6枚、画面選択35件が配布版と一致しました。親階層の付け替え、`offsetParentMatrix`、形状入力の編集と再接続、表示・選択・レイヤー、Undo／Redo、レンダラーの再設定、プラグインの再読み込み、充填済みキャッシュの順再生・逆再生・スクラブを含みます。

計時は直前の共通親比較と同じ1,000個の構成を使い、配布版（A）→試作版（B）、試作版（B）→配布版（A）の順で起動しました。後半の2起動は再生条件とキャッシュ ON／OFF の順も反転しました。再生は各条件5試行、1試行につき71実描画です。ドラッグは親と入力を固定した構成で各5試行、1試行72回の Qt Move 入力すべてで実描画を確認しました。再生画像とドラッグの変位は4起動間で一致しました。

| 変形する入力 | 操作 | 正順 A → B | 逆順 A → B | B − A（正順／逆順） |
| ---: | --- | ---: | ---: | ---: |
| 0個 | 親固定・再生 OFF | 4.46 → 2.16 | 5.35 → 1.99 | −2.30／−3.36 |
| 0個 | 親固定・再生 ON | 4.80 → 2.66 | 4.73 → 2.27 | −2.14／−2.46 |
| 1個 | 親固定・再生 OFF | 4.64 → 2.39 | 5.20 → 3.02 | −2.24／−2.18 |
| 1個 | 親固定・再生 ON | 4.53 → 2.54 | 5.11 → 2.43 | −1.99／−2.68 |
| 1,000個 | 親固定・再生 OFF | 15.66 → 14.12 | 14.16 → 14.30 | −1.54／+0.14 |
| 1,000個 | 親固定・再生 ON | 13.23 → 13.35 | 13.68 → 13.14 | +0.12／−0.54 |
| 0個 | 親移動・再生 OFF | 7.84 → 8.05 | 8.73 → 8.00 | +0.20／−0.73 |
| 0個 | 親移動・再生 ON | 7.92 → 8.50 | 8.47 → 8.77 | +0.58／+0.29 |
| 1個 | 親移動・再生 OFF | 7.75 → 8.17 | 7.99 → 8.18 | +0.42／+0.20 |
| 1個 | 親移動・再生 ON | 8.28 → 8.57 | 8.97 → 8.63 | +0.29／−0.34 |
| 1,000個 | 親移動・再生 OFF | 14.93 → 15.05 | 15.40 → 14.88 | +0.12／−0.52 |
| 1,000個 | 親移動・再生 ON | 15.40 → 15.23 | 15.01 → 15.07 | −0.16／+0.06 |
| 0個 | 共通親ドラッグ | 9.57 → 9.97 | 10.91 → 10.02 | +0.40／−0.89 |
| 0個 | 単体ドラッグ | 6.12 → 4.15 | 7.14 → 4.35 | −1.97／−2.79 |

単位は再生が ms／実描画、ドラッグが ms／入力です。親固定・0〜1個変形の再生と単体ドラッグは両起動順で約2 ms以上短縮しました。全変形や共通親ドラッグでは差の符号が起動順で変わりました。親移動・0個変形のキャッシュ ON と親移動・1個変形の OFF は両順で0.20〜0.58 ms長くなり、配布時の再確認候補です。

試作は研究用 DLL として保管しました。ソースとビルドのハッシュ、全試行の集計 `summary.json`、照合結果と画像は `build/fixed_cube/early_requires_update/`（Git 管理外）にあります。

#### ワールド行列の一致比較の単体計測

Maya 2025.3.3 の OpenMaya にリンクした MSVC x64 Release の C++ 実行ファイルで、試作と同じ `MMatrix::operator==` を計測しました。行列を事前に作り、1,000組の比較と一致数の集計を512回まとめて計時しました。各条件21試行の中央値を示します。行列2枚の組は256 Bです。連続配置と、4組につき1組を参照する配置を比べました。

| 1,000組の条件 | 連続配置 | 4組につき1組 |
| --- | ---: | ---: |
| 全組が一致 | 0.00695 | 0.00719 |
| 全組で X 移動だけが異なる | 0.00568 | 0.00592 |
| 全組で回転が異なる | 0.00212 | 0.00213 |
| 1組だけ X 移動が異なる | 0.00701 | 0.00714 |

単位は ms／1,000組です。ループと一致数の集計を含み、行列取得や VP2 の処理は計時区間の外です。同じ配列で X 移動の1要素だけを比較する対照は0.00080〜0.00104 ms／1,000組でした。この配置での行列比較の時間は、前節の親移動で増えた再生時間0.20〜0.58 msより小さい値でした。

比較のソース、実行ファイルと Maya ライブラリのハッシュ、全試行と集計は `build/fixed_cube/early_requires_update/matrix_equality/`（Git 管理外）に保存しました。

#### 直親の `worldMatrix` を接続した場合の dirty と描画時間

Maya 2025.3.3／OpenGL で、各 `bdShpL_DeformableCube` の直親の `worldMatrix[0]` を、研究用の非表示入力 `parentWorldMatrixInput` へ接続しました。比較の基準は前節の、変更がない Cube の描画更新を早期終了する研究版です。各版で同じローカル形状と `shapeDeformMatrix` の処理を使いました。

| 版 | 親行列を使う方法 |
| --- | --- |
| A・接続なし | 描画時に DAG パスの `inclusiveMatrix()` を取得する |
| W・接続追加 | 接続済み入力を Evaluation Cache の対象に加え、描画時は A と同じ方法で取得する |
| B・世代を監視 | W に加え、dirty の世代が進むと中継出力から入力を読み、描画には DAG パスの行列を使う |
| C・世代で再利用 | B と同じ世代管理で、直親と入力元が合致する通常コンテキストでは取得済みの入力行列を描画に使う |

`parentWorldMatrixSample` は入力に依存する中継出力です。入力を読み、出力を clean にして次の dirty を受けられるようにしています。診断版では C が選んだ値を、その描画の `inclusiveMatrix()` と毎回比較しました。補正前の不一致を記録し、計時には診断を含まない DLL を使いました。

1,000個の比較では、共通親の下に10個の枝を置き、それぞれに100組の transform と Cube を配置しました。各 Cube の `shapeDeformMatrix` は個別の別 transform の `matrix` に接続しました。「変形入力1個」はそのうち1本のスケールだけが変わる条件です。ローカル形状の変形は親のワールド行列の変化数に含めません。

| 1,000個の診断条件 | 照合した行列 | 前回から値が変わった件数 | 中継出力の再取得 |
| --- | ---: | ---: | ---: |
| 単体ドラッグ | 74,000 | 68 | 68 |
| 1枝をドラッグ | 74,000 | 6,800 | 6,800 |
| 共通親をドラッグ | 74,000 | 68,000 | 68,000 |
| 親固定で再生（変形入力0／1個 × キャッシュ OFF／充填済み ON の合計） | 284,000 | 0 | 0 |
| 共通親を移動して再生（同じ4条件の合計） | 284,000 | 284,000 | 284,000 |

暖機後の790,000件を照合し、再利用431,132件、再取得358,868件とも DAG の行列との不一致は0件でした。ドラッグの診断区間は各74描画で、実際に位置が変わった68回に対して、動いた対象数の1／100／1,000倍だけ取得しました。速度計測の区間は各72回のマウス移動と72描画です。

計時は1版につき2回の独立した Maya 起動で行いました。起動順は A→W→B→C、C→B→W→A、後半は各起動内の条件順も反転しました。各セルの左／右は前半／後半の各3試行の中央値です。ドラッグは ms／マウス移動、再生は ms／実描画で、小さいほど高速です。再生は各試行71描画、キャッシュ ON は計測区間の全フレームが充填済みであることを開始前と終了後に確認しました。描画画像とマニピュレータの移動量も版間で照合しました。

| 条件 | A・接続なし | W・接続追加 | B・世代を監視 | C・世代で再利用 |
| --- | ---: | ---: | ---: | ---: |
| 単体ドラッグ | 4.31／4.50 | 4.70／4.35 | 5.24／5.17 | 4.99／4.77 |
| 1枝をドラッグ（100個） | 5.01／5.50 | 5.01／5.75 | 7.28／6.85 | 6.52／6.44 |
| 共通親をドラッグ（1,000個） | 11.18／10.51 | 11.13／11.31 | 22.20／21.95 | 21.79／21.36 |
| 親固定・変形入力0個・再生 OFF | 3.50／3.69 | 2.64／3.54 | 2.88／4.43 | 2.71／3.50 |
| 親固定・変形入力0個・再生 ON | 3.41／2.59 | 2.60／2.50 | 3.60／2.85 | 3.09／3.31 |
| 親固定・変形入力1個・再生 OFF | 3.26／2.60 | 5.49／2.51 | 3.83／2.74 | 3.07／2.76 |
| 親固定・変形入力1個・再生 ON | 3.32／3.59 | 3.15／2.55 | 3.55／3.51 | 2.90／3.59 |
| 親移動・変形入力0個・再生 OFF | 8.37／8.36 | 12.12／12.08 | 15.45／14.14 | 13.93／14.10 |
| 親移動・変形入力0個・再生 ON | 8.54／9.08 | 13.01／12.12 | 14.15／14.31 | 14.10／13.95 |
| 親移動・変形入力1個・再生 OFF | 10.01／8.30 | 13.07／12.50 | 16.38／15.68 | 14.45／14.09 |
| 親移動・変形入力1個・再生 ON | 9.38／10.10 | 11.74／11.56 | 14.84／13.92 | 13.60／15.00 |

共通親が動く再生では、W の時点で A より1.47〜4.47 ms／実描画長く、C は A より4.22〜5.79 ms長くなりました。この W の差には入力接続、描画に影響する属性の登録、接続済み入力のキャッシュ設定を含みます。親固定・変形入力0個の再生 OFF は C が両順で0.19〜0.79 ms短く、親固定の他の再生条件では同程度か起動順で差の方向が変わりました。

ドラッグは B から C へ切り替えると3条件すべてで0.25〜0.76 ms／入力短縮しました。それでも A に対しては単体で0.27〜0.69 ms、1枝で0.94〜1.51 ms、共通親で10.61〜10.85 ms長くなりました。動いた対象だけを読み直すことはできましたが、この構成では、共通親が動く場面での評価と中継出力の取得を含めた総時間が増えます。配布版には明示接続や研究用属性を採用しません。

4個の GUI シーンでは、直親の移動、1枝の回転、共通親の移動、`offsetParentMatrix` のアニメーションについて、順再生・逆再生・スクラブをキャッシュ OFF と充填済み ON で確認しました。誤って別の transform をつないだ場合は DAG の値に戻り、正しい接続に戻すと再利用を再開しました。通常の親 transform の付け替えでも描画と画面選択が追従しました。診断による補正を含まない C と配布版で、静止画77枚、再生中の56枚、画面選択11件が一致しました。

shape 自体を `parent -shape -relative` で別の transform に移した直後は、配布版と研究版の両方で、その1個の描画と画面選択が欠けました。付け替え直後の診断では描画判定に来たのは残り3個でした。このシーンでは VP2 を `ogs(reset=True)` でリセットすると4個が表示され、付け替えた shape も新しい親の位置で選択できました。

生データ、研究用 DLL のビルド手順とハッシュ、診断結果は `build/fixed_cube/world_input_study/`（Git 管理外）に保存しました。1,000個の速度比較は `timing/summary_a1_w1_b1_c1_c2_b2_w2_a2.json`、行列の照合件数は `large_oracle_summary.json` にあります。

#### シェイプを直接付け替えたときの VP2 の追従

Maya 2025.3.3／OpenGL で、`parent -shape -relative` による shape の付け替えを最小シーンで比較しました。空の transform と、既存の shape を持つ transform への付け替えを試し、DAG パス、ワールド位置、移動先と移動元の画像、画面選択を記録しました。

配布版 `bdShpL_DeformableCube` は、DAG パスとワールド位置が移動先へ変わった時点で、両位置から描線と画面選択が消えました。その後の Undo／Redo、移動先の移動、shape の `visibility` の切り替えでも復帰しませんでした。メインの透視ビューでイベント処理を待っても同じ結果でした。`bdShpL_Cube` と、`cmds.curve()` で作り `nodeType()` で確認した標準 `nurbsCurve` は、描画と画面選択が移動先に追従しました。標準カーブは `bdUtilNodes` の読み込み有無の両方で確認しました。shape を持つ transform ごと付け替えた場合も描画と選択は追従しました。

初回の標準カーブ用シーンは、検証スクリプトが描画用の基底クラスを取り違え、実際には `bdShpL_DeformableCube` を作成していました。ノード型の照合を追加し、標準カーブの結果を取り直しました。

`bdShpL_DeformableCube` の診断版では、付け替え操作で親と子の追加・削除通知が各1回あり、既存の `MPxSubSceneOverride` が破棄されました。その後の描画では新規オーバーライドの生成と `requiresUpdate()` の呼び出しがどちらも0回でした。構造変更通知の中と、コマンド終了後に `MRenderer::setGeometryDrawDirty(shape, true)` を呼びました。どちらも描画対象への復帰は確認できませんでした。[Maya 2025 `MRenderer`](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_renderer.html)

`MDagModifier.reparentNode()` でも `bdShpL_DeformableCube` で同じ症状が出ました。新しい親に `parent -add -shape -relative` でパスを追加し、その後に旧パスを `parent -removeObject -shape` で外す手順では、3種類とも shape の UUID を保ったまま表示・画面選択が追従しました。2コマンドを1つの Undo チャンクにまとめ、Undo／Redo と移動先の transform を動かした後の追従も確認しました。[Maya 2025 `parent`](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/parent.html)

以下は移動元の shape と移動先の transform をフルパスで指定した検証と同じ手順です。

```python
from maya import cmds

shape = "|source|controllerShape"
destination = "|destination"
cmds.undoInfo(openChunk=True, chunkName="transferControllerShape")
try:
    cmds.parent(shape, destination, addObject=True, shape=True, relative=True)
    cmds.parent(shape, removeObject=True, shape=True)
finally:
    cmds.undoInfo(closeChunk=True)
```

検証スクリプト、画像、DAG パスと画面選択の記録は `build/fixed_cube/shape_reparent/`、診断版のソースとハッシュは `build/fixed_cube/shape_reparent_study/native/` にあります（Git 管理外）。通常の付け替え、2ステップの付け替え、`MDagModifier` の型照合済み結果は、それぞれ `runs/baseline_checked`、`runs/add_remove_checked`、`runs/mdag_modifier_checked` にあります。

#### 親のワールド行列だけが変わるときの描画更新

前節の速度計測と同じ10枝×100個のシーンで、共通親を移動し、`shapeDeformMatrix` の値は全 Cube で固定しました。配布版と同じ描画処理に計時を加えた結果を示します。各値は1,000個分の ms／実描画で、診断の計時処理を含みます。描画状態の取得は `requiresUpdate()` の内側、`setMatrix()` は `update()` の内側の時間です。

| 処理 | キャッシュ OFF | 充填済み ON |
| --- | ---: | ---: |
| `requiresUpdate()` | 3.25 | 3.59 |
| ↳ 描画状態の取得全体 | 2.24 | 2.44 |
| ↳ DAG パス取得と有効性確認 | 1.19 | 1.26 |
| ↳ ワールド行列の取得 | 0.17 | 0.19 |
| ↳ ローカル行列の取得とワールド行列との合成 | 0.20 | 0.22 |
| ↳ 表示ステータスの確認 | 0.29 | 0.33 |
| `update()` | 1.73 | 1.92 |
| ↳ `setMatrix()` | 0.88 | 0.99 |

研究版では、追加配線なしの早期終了試作を基に、ローカルの変形・形状、選択、表示条件、描画リソース、DAG パスの変化を確認しました。ワールド行列だけが変化した場合は、保持したローカル行列と合成し、既存の描画アイテムへ行列を設定します。照合版は、この経路で得た行列・表示状態・パスを、従来どおり一式を取得した結果と比較しました。

共通親が動き、変形入力が固定の再生では、OFF／ON とも実描画あたり1,000個で行列だけを更新できました。変形入力が1個動く場合は999個がこの経路を通り、変形入力が動く1個は通常の更新へ進みました。すべての入力が動く場合は全1,000個が通常の更新へ進みました。全15条件で、何も変化しないと判断した430,990件と、行列のみ更新した358,726件を照合し、不一致は0件でした。

3個の GUI 検証では、色・表示・選択の変更、2ビューポート、レンダラーのリセット、親 transform の付け替えと Cached Playback の順再生・逆再生・スクラブを確認しました。配布版と比べ、静止画102枚、再生中の画像53枚、画面選択35件が一致しました。行列のみを更新する109件の照合でも不一致は0件でした。

配布版、更新不要のときだけ早く終了する既存試作、今回の行列更新試作を、同一のハーネスで2回ずつ起動して計測しました。後半は起動順と条件順を反転しました。各セルの左／右は前半／後半の各3試行の中央値です。単位は再生が ms／実描画（各71描画）、ドラッグが ms／マウス移動（各72回・72描画）です。ON は計測区間の充填を開始前と終了後に確認しました。各版の再生画像とドラッグの移動量は一致しました。前半の行列更新版は前面状態を失った試行を除外し、新規起動で取り直しました。

| 条件 | 配布版 | 既存の早期終了試作 | 親行列だけを更新する試作 |
| --- | ---: | ---: | ---: |
| 単体ドラッグ | 6.66／8.35 | 4.69／6.23 | 4.54／5.36 |
| 1枝をドラッグ（100個） | 6.53／7.36 | 5.17／5.29 | 5.34／4.80 |
| 共通親をドラッグ（1,000個） | 10.04／12.00 | 12.33／12.11 | 8.34／9.14 |
| 親固定・変形入力0個・再生 OFF | 4.58／5.54 | 2.90／2.75 | 3.18／3.38 |
| 親固定・変形入力0個・再生 ON | 5.38／6.29 | 3.57／3.67 | 4.57／3.45 |
| 親固定・変形入力1個・再生 OFF | 6.52／5.27 | 3.26／3.73 | 3.77／3.37 |
| 親固定・変形入力1個・再生 ON | 4.69／6.20 | 2.65／2.99 | 3.47／3.70 |
| 親移動・変形入力0個・再生 OFF | 9.63／8.63 | 8.99／9.70 | 6.63／6.53 |
| 親移動・変形入力0個・再生 ON | 9.35／10.11 | 9.19／10.55 | 7.19／6.94 |
| 親移動・変形入力1個・再生 OFF | 9.25／8.96 | 9.36／9.54 | 6.44／6.79 |
| 親移動・変形入力1個・再生 ON | 9.06／10.50 | 9.26／11.54 | 6.75／6.55 |
| 親固定・変形入力1,000個・再生 OFF | 16.14／15.82 | 15.42／18.05 | 15.41／16.53 |
| 親固定・変形入力1,000個・再生 ON | 13.87／15.82 | 14.26／15.87 | 16.03／15.81 |
| 親移動・変形入力1,000個・再生 OFF | 15.68／17.79 | 16.93／17.42 | 17.55／16.69 |
| 親移動・変形入力1,000個・再生 ON | 16.35／15.56 | 17.31／16.94 | 17.14／16.61 |

共通親を動かし、変形入力が0〜1個だけ動く再生では、今回の試作は配布版より OFF で2.11〜3.01 ms、ON で2.15〜3.96 ms／実描画短縮しました。既存の早期終了試作と比べても、同じ4条件が両起動順で2.00〜4.99 ms短縮しました。単体・枝・共通親のドラッグも、配布版より両順で1.18〜2.99 ms／入力短縮しました。

共通親と全1,000個の変形入力が動くキャッシュ ON 再生は、配布版より0.79／1.05 ms長くなりました。親固定・全変形の ON でも片方の順で2.16 ms長く、他方の差は0.02 ms未満でした。行列だけを更新できる場面で得た改善を活かすには、全変形で通常更新に進む場合の追加コストを調べる余地があります。今回のコードは研究版に保存しました。

生データ、ソース、DLL のハッシュ、15条件の `summary_a1_b1_c1_retry1_c2_b2_a2.json`、診断集計 `profiles_summary.json` は `build/fixed_cube/world_only_update/`（Git 管理外）にあります。

### 変形入力の世代を先に確認する試作

全1,000個の変形入力が動くと、前節の試作では全ノードが通常更新へ進みます。この条件で親行列だけを更新するための準備を省けるか、`requiresUpdate()` の入口で `shapeDeformMatrix` の世代を確認する方法を試しました。前回読み取った世代から進んだ場合は、配布版と同じ順でパス・ワールド行列・変形行列・表示状態を取得し、更新の要否を判定します。この経路では親行列の再利用用データを無効にします。世代が安定した最初の描画で再利用用データを取り直すため、その後は親行列のみの更新と、状態が変わらない Cube の更新省略が再び可能になります。

同じ Maya 2025.3.3 の並列評価・Viewport 2.0 OpenGL で、配布版、前節の親行列更新試作、今回の変形世代を先に確認する試作を比較しました。各 Cube は個別の transform の `matrix` に接続し、変形入力0、1、1,000個が動く条件を使いました。共通親の固定・移動と Cached Playback OFF・充填済み ON の12条件、単体・1枝・共通親の Move ドラッグ3条件です。2巡目では DLL の起動順と測定条件の順を反転しました。

各セルの左／右は1巡目／2巡目の各3試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。全6起動でシーン構成、再生画像、マウスの移動経路と transform の移動量が一致し、キャッシュ ON では計測の前後とも71フレームが充填されていました。

| 条件 | 配布版 | 親行列更新試作 | 変形世代を先に確認する試作 |
| --- | ---: | ---: | ---: |
| 単体ドラッグ | 6.31／6.65 | 4.66／5.16 | 4.56／5.00 |
| 1枝をドラッグ（100個） | 7.23／7.19 | 5.12／4.80 | 5.10／4.77 |
| 共通親をドラッグ（1,000個） | 10.96／10.55 | 7.77／8.47 | 8.14／8.19 |
| 親固定・変形入力0個・再生 OFF | 5.06／4.92 | 2.61／2.73 | 3.08／2.88 |
| 親固定・変形入力0個・再生 ON | 4.87／4.68 | 3.56／3.17 | 3.41／3.22 |
| 親固定・変形入力1個・再生 OFF | 6.58／5.29 | 3.37／2.96 | 3.54／2.99 |
| 親固定・変形入力1個・再生 ON | 5.96／5.11 | 3.01／3.24 | 2.99／3.45 |
| 親移動・変形入力0個・再生 OFF | 8.77／8.78 | 5.88／6.41 | 6.11／6.29 |
| 親移動・変形入力0個・再生 ON | 8.50／8.89 | 6.53／6.51 | 7.11／6.30 |
| 親移動・変形入力1個・再生 OFF | 10.43／8.51 | 5.87／6.30 | 6.18／6.33 |
| 親移動・変形入力1個・再生 ON | 9.53／8.88 | 6.29／6.47 | 6.70／6.39 |
| 親固定・変形入力1,000個・再生 OFF | 15.24／14.46 | 15.52／16.10 | 15.44／14.91 |
| 親固定・変形入力1,000個・再生 ON | 14.68／13.93 | 14.34／14.25 | 14.42／14.23 |
| 親移動・変形入力1,000個・再生 OFF | 16.49／15.89 | 15.97／16.12 | 16.12／16.16 |
| 親移動・変形入力1,000個・再生 ON | 15.25／15.87 | 16.04／16.10 | 16.02／15.99 |

共通親と全1,000個の変形入力が動くキャッシュ ON 再生では、今回の試作は親行列更新試作より0.02／0.11 ms短縮し、配布版より0.77／0.12 ms長くなりました。OFF では親行列更新試作より0.15／0.04 ms長くなりました。共通親が動き、変形入力が0〜1個の再生では、今回の試作も配布版より OFF で2.18〜4.26 ms、ON で1.40〜2.83 ms／実描画短縮しました。3種類のドラッグは配布版より1.66〜2.82 ms／入力短縮しました。

今回の分岐は、親行列の再利用に備えた判定と状態の保存を省く代わりに、毎回 `MFnDagNode::getPath()` でパスを取得します。親行列更新試作は階層の世代が一致すればパスを再利用できるため、通常更新に入るまでの判定時間とパスを再取得する時間を今回の差分から個別に求めることはできません。全変形のキャッシュ ON で短縮幅が小さかったため、研究版として記録します。

診断版では、変形0個の再生で毎描画0件、変形1個で1件、全変形で1,000件が新しい分岐に進みました。新しい分岐284,284件と親行列のみの更新358,726件を通常の読み取りと照合し、不一致は0件でした。3個の GUI 検証でも、変形行列の直接設定・接続変更と Undo／Redo、2ビューポート、表示状態の変更、親 transform の付け替え、キャッシュ済みの順再生・逆再生・スクラブを確認しました。配布版と静止画102枚、再生画像53枚、参照画像6枚、画面選択35件が一致しました。

試作ソースと DLL のハッシュ、全6起動分の生データ、集計 `timing/summary_a1_c1_d1_d2_c2_a2.json`、診断版の集計 `timing/oracle_summary.json` と `gate/comparison.json` は `build/fixed_cube/deform_dirty_gate/`（Git 管理外）にあります。

### 変形中の DAG パス再利用

前節の試作に、`shapeDeformMatrix` が更新された描画でも `MDagPath` を再利用する経路を加えました。既存の DAG・接続変更の監視で世代が進み、次に描画が必要になった時点でパスを取得し直します。世代が一致する間は保存したパスから現在のワールド行列を取得します。変形行列と表示状態を読む処理は前節と同じです。パス取得時は取得の前後で世代が一致し、有効なパスを得られた場合に保存します。

配布版、変形世代を先に確認する試作、その試作に DAG パスの再利用を加えた版を Maya 2025.3.3 の並列評価・Viewport 2.0 OpenGL で比較しました。各 Cube には個別の変形入力があります。前節の15条件に、共通親と1枝の100個の変形入力が動き、残り900個の変形入力が固定の再生をキャッシュ OFF・充填済み ON で加えました。2巡目は DLL の起動順と各条件の順を反転しました。

各セルの左／右は1巡目／2巡目の各3試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。全6起動でシーン構成、参照フレームの描画、マウスの移動経路と transform の移動量が一致し、キャッシュ ON では計測の前後とも71フレームが充填されていました。

| 条件 | 配布版 | 変形世代を先に確認 | 変形中の DAG パス再利用 |
| --- | ---: | ---: | ---: |
| 単体ドラッグ | 9.26／6.44 | 4.49／4.32 | 4.24／4.58 |
| 1枝をドラッグ（100個） | 6.77／6.38 | 4.41／4.90 | 4.41／4.83 |
| 共通親をドラッグ（1,000個） | 10.81／9.86 | 8.21／7.90 | 8.11／7.73 |
| 親固定・変形入力0個・再生 OFF | 5.06／4.96 | 2.43／3.20 | 2.42／2.87 |
| 親固定・変形入力0個・再生 ON | 4.27／4.61 | 2.49／2.62 | 2.49／2.38 |
| 親固定・変形入力1個・再生 OFF | 4.30／5.04 | 2.64／3.28 | 2.56／3.22 |
| 親固定・変形入力1個・再生 ON | 5.25／4.79 | 2.94／2.62 | 2.94／2.63 |
| 親固定・変形入力1,000個・再生 OFF | 15.52／14.76 | 14.72／14.22 | 14.38／14.36 |
| 親固定・変形入力1,000個・再生 ON | 13.19／13.53 | 13.77／13.49 | 13.73／13.59 |
| 親移動・変形入力0個・再生 OFF | 8.13／7.84 | 6.29／5.56 | 6.60／5.69 |
| 親移動・変形入力0個・再生 ON | 8.93／8.30 | 6.44／6.92 | 6.28／6.62 |
| 親移動・変形入力1個・再生 OFF | 8.52／7.95 | 6.42／5.46 | 6.28／5.69 |
| 親移動・変形入力1個・再生 ON | 8.77／8.45 | 6.62／6.79 | 6.83／6.88 |
| 親移動・変形入力100個・再生 OFF | 8.62／9.17 | 7.24／6.74 | 7.13／7.00 |
| 親移動・変形入力100個・再生 ON | 9.14／9.46 | 7.05／7.49 | 7.13／7.58 |
| 親移動・変形入力1,000個・再生 OFF | 15.20／15.47 | 15.77／15.13 | 15.37／15.02 |
| 親移動・変形入力1,000個・再生 ON | 15.16／14.87 | 15.37／14.45 | 15.04／14.70 |

共通親と全1,000個の変形入力が動くキャッシュ ON では、パス再利用版は配布版より0.12／0.17 ms短縮しました。前節の試作に対しては1巡目で0.33 ms短く、2巡目で0.24 ms長くなりました。同じ条件の OFF では前節の試作より両巡で0.40／0.11 ms短くなりました。共通親が固定で全変形のキャッシュ ON は配布版より0.54／0.06 ms長くかかりました。

共通親と100個の変形入力が動くキャッシュ ON では、パス再利用版は配布版より2.01／1.87 ms短縮しました。前節の試作との差は0.08／0.09 ms増でした。変形が少ない再生やドラッグで配布版との差は維持できました。パス再利用を追加した効果は条件と起動順で変わり、全変形で安定して短縮するかは今回の計時では確認できませんでした。

診断版では、暖機後に変形入力が更新された298,484件のすべてでパスを再利用し、この経路での `getPath()` の呼び出しは0件でした。変形入力が100個／1,000個動く再生では、前節の試作が変形した各 Cube のパスを取り直す箇所に相当します。診断用の独立したパス取得と比較し、描画用のパス・行列・表示状態の不一致は0件でした。親の行列だけを更新した486,526件も、独立した読み取りと一致しました。

3個の GUI 検証では、シェイプ直上の transform またはその祖先の付け替えと `shapeDeformMatrix` の変更を1操作にまとめました。付け替え・Undo・Redo の計6操作で、それぞれ変形が変更された Cube のパスを1回取り直しました。旧位置の辺を選択できなくなり、新位置で選択できることを確かめました。配布版との比較では各333件の判定を通過し、静止画110枚、再生画像53枚、参照画像6枚、画面選択49件が一致しました。

パス再利用版は研究版として保存しました。ソースと DLL のハッシュ、全6起動の生データ、集計 `timing/summary_a1_d1_e1_e2_d2_a2.json`、診断版の集計 `timing/oracle_summary.json` と `gate/comparison.json` は `build/fixed_cube/deform_dag_path/`（Git 管理外）にあります。

### `bdShpL_DeformableCube` への採用

親のワールド行列だけが変わった場合に描画項目の行列だけを更新する処理と、変形中の DAG パス再利用を `bdUtilNodes` に取り込みました。DAG・接続変更は既存の監視を使い、階層の世代が変わった場合は描画時にパスを取得し直します。変形行列、形状、表示状態や描画項目が変わった場合は、現在の状態に基づいて描画を更新します。研究版で使った照合は別ビルドで実行し、配布版は通常の Release 設定でビルドしました。

Maya 2025.3.3／OpenGL で、採用前と更新後の配布 DLL を前節と同じ17条件で比べました。左／右は1巡目／起動順と条件順を反転した2巡目の各3試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。4起動でシーン構成、参照フレーム画像、マウスの移動経路と transform の移動量が一致しました。

| 条件 | 採用前 | 更新後 |
| --- | ---: | ---: |
| 単体ドラッグ | 6.41／6.97 | 4.35／4.67 |
| 1枝をドラッグ（100個） | 6.21／6.83 | 4.19／4.53 |
| 共通親をドラッグ（1,000個） | 10.05／10.25 | 7.64／7.62 |
| 親固定・変形入力0個・再生 OFF | 4.27／5.18 | 2.37／2.56 |
| 親固定・変形入力0個・再生 ON | 5.00／4.34 | 2.35／2.51 |
| 親固定・変形入力1個・再生 OFF | 5.49／4.93 | 2.43／3.07 |
| 親固定・変形入力1個・再生 ON | 4.77／4.59 | 3.01／3.13 |
| 親固定・変形入力1,000個・再生 OFF | 14.63／14.60 | 13.85／14.26 |
| 親固定・変形入力1,000個・再生 ON | 13.77／14.06 | 13.27／13.57 |
| 親移動・変形入力0個・再生 OFF | 8.68／7.74 | 6.11／6.11 |
| 親移動・変形入力0個・再生 ON | 8.25／8.41 | 6.24／7.41 |
| 親移動・変形入力1個・再生 OFF | 8.54／7.73 | 6.06／5.79 |
| 親移動・変形入力1個・再生 ON | 8.48／8.30 | 6.03／6.76 |
| 親移動・変形入力100個・再生 OFF | 9.23／9.02 | 6.77／7.28 |
| 親移動・変形入力100個・再生 ON | 9.46／10.09 | 7.33／7.66 |
| 親移動・変形入力1,000個・再生 OFF | 16.16／15.32 | 15.26／15.04 |
| 親移動・変形入力1,000個・再生 ON | 15.55／14.83 | 14.53／14.82 |

共通親と100個の変形入力が動く再生は、キャッシュ ON で2.13／2.43 ms、OFF で2.46／1.75 ms／実描画短縮しました。共通親と全1,000個の変形入力が動く再生は、ON で1.03／0.01 ms、OFF で0.90／0.28 ms短くなりました。ON の2巡目は両版がほぼ同じ値でした。3種類のドラッグは2.02〜2.64 ms／入力短縮しました。

更新後の配布 DLL で、変形と直上の transform・祖先の付け替えを同時に行ったときの Undo／Redo、表示と選択、キャッシュ済みの順再生・逆再生・スクラブを確認しました。採用前と同じ333件の判定を通過し、静止画110枚、再生画像53枚、参照画像6枚、画面選択49件が一致しました。

全4起動の生データ、配布 DLL のハッシュ、集計 `timing/summary_a1_p1_p2_a2.json`、GUI 照合の `gate/comparison.json` は `build/fixed_cube/deform_dag_adoption/`（Git 管理外）にあります。

### 毎フレーム変形する Cube の描画更新

DAG パス再利用を採用した配布版 `e5caf91f` を基準に、Maya 2025.3.3／OpenGL で調べました。前節と同じ10枝×100個の構成で、各 Cube に別々の `transform.matrix` を接続しました。診断では共通親と100個の変形入力が動く条件と、共通親と全1,000個の変形入力が動く条件を測りました。

| 共通親と一緒に変形する Cube の数 | 100個 OFF／ON | 1,000個 OFF／ON |
| --- | ---: | ---: |
| 評価グラフの実行 | 1.90／3.16 | 9.07／6.62 |
| VP2 の描画準備 | 5.08／5.70 | 9.28／10.24 |
| 描画用の変形行列を読む `MPlug::asMObject()` | 0.17／0.38 | 2.03／3.08 |
| 変形した Cube の表示キャッシュ確認 | 0.07／0.07 | 1.00／0.78 |
| `MRenderItem::setMatrix()` | 0.82／0.89 | 1.30／1.08 |

単位は ms／実描画です。評価グラフと描画準備は配布 DLL を使った Maya Profiler の各23実描画、下3行は診断 DLL の各71実描画です。右側の ON は充填済み Evaluation Cache です。別起動で行った計時で、描画準備はプラグイン処理を含みます。

行列入力を読む回数は、各実描画で値が変わった100件または1,000件でした。共通親が動くので、いずれの条件でも `setMatrix()` は各実描画で1,000件です。同じ区間でシェーダーと頂点バッファの再設定、境界の取得、表示状態の全項目の読み取りは0件でした。表示キャッシュの確認には、選択やハイライトに連動する表示ステータスの照会が含まれます。

試作では、変形入力が更新されても表示状態、基準形状、DAG パス、描画アイテムの一致を確認できる場合は、現在の変形行列と親のワールド行列を合成して既存アイテムへ渡します。条件を満たさないときは通常の更新経路を使います。変形入力が変わらない場合の経路は従来と同じです。

配布版と試作版の両方で GUI の373件の判定を通過しました。2つのビューポートでの選択、変形と色・テンプレート・可視性・寸法の同一フレーム編集、Undo／Redo、充填済みキャッシュでの順再生・逆再生・スクラブを含みます。静止画125枚、再生画像53枚、参照画像6枚、画面選択58件が一致しました。

計時では対照版と試作版に同じ研究用プラグイン登録と Release ビルド設定を使用しました。対照版は配布版と同じ Cube の描画コードです。対照 → 試作、試作 → 対照の順で別起動し、2巡目は条件の順も反転しました。各セルは1巡目／2巡目それぞれの3試行の中央値です。再生は ms／実描画（各71描画）、ドラッグは ms／マウス移動（各72移動・72描画）です。全4起動で再生の代表フレームの画像、マウスの軌跡、操作対象の移動量が一致し、キャッシュ ON では測定前後とも71フレームの充填を確認しました。

| 条件 | 対照版 | 試作版 | 差（試作 − 対照） |
| --- | ---: | ---: | ---: |
| 共通親固定・変形入力0個・再生 OFF | 3.15／3.53 | 3.34／3.21 | +0.19／−0.33 |
| 共通親固定・変形入力0個・再生 ON | 3.16／3.58 | 3.12／3.09 | −0.04／−0.49 |
| 共通親移動・変形入力0個・再生 OFF | 6.22／6.33 | 6.98／6.23 | +0.76／−0.10 |
| 共通親移動・変形入力0個・再生 ON | 6.79／6.74 | 6.90／6.86 | +0.11／+0.11 |
| 共通親移動・変形入力100個・再生 OFF | 7.22／8.10 | 7.51／7.28 | +0.29／−0.83 |
| 共通親移動・変形入力100個・再生 ON | 7.67／8.88 | 9.59／8.14 | +1.93／−0.75 |
| 共通親移動・変形入力1,000個・再生 OFF | 16.46／19.19 | 15.14／14.33 | −1.32／−4.86 |
| 共通親移動・変形入力1,000個・再生 ON | 16.07／16.60 | 17.65／17.48 | +1.59／+0.89 |
| 単体ドラッグ | 5.32／5.72 | 5.22／5.27 | −0.09／−0.45 |
| 1枝のドラッグ（100個） | 5.03／5.40 | 5.31／5.09 | +0.27／−0.32 |
| 共通親のドラッグ（1,000個） | 8.63／9.36 | 8.70／8.71 | +0.07／−0.65 |

全変形の再生では、キャッシュ OFF が両順で短く、充填済み ON は両順で長くなりました。OFF は対照版だけでも2巡間で2.73 msの差があり、短縮幅の見積もりには幅があります。100個だけが変形する再生は OFF／ON とも起動順で差の符号が変わりました。充填済み ON を含めた一貫した改善が得られなかったため、試作は研究用 DLL として保存しました。

別の照合ビルドでは、キャッシュ OFF の100個／1,000個の変形で行列だけを更新する経路がそれぞれ7,100／71,000件実行されました。DAG パス、合成行列、表示状態をキャッシュとは独立に取得した値と照合し、不一致は0件でした。充填済み ON ではそれぞれ7,100／71,000件の全件で通常経路に進みました。この照合ビルドの所要時間は通常 DLL の速度比較に含めていません。

最初に失敗した判定を区別する診断では、充填済み ON の78,100件すべてで、初回の行列読み取り中に変形の世代番号が進みました。`shapeDrawMatrix()` は読み取り前後で世代が一致したときに値を描画用キャッシュへ保存します。この条件を満たさず、試作は通常経路で同じ入力を読み直しました。各実描画の入力読み取り回数は、100個の条件で100回から200回、1,000個の条件で1,000回から2,000回に増えました。世代を進めたコールバックの内訳は未計測です。

同じ対照版と試作版を使った Maya Profiler の各23実描画で、全変形時の VP2 描画準備は OFF で10.41 → 7.22 ms、充填済み ON で10.21 → 11.59 msでした。評価グラフは OFF で9.42 → 8.73 ms、ON で6.64 → 6.79 msでした。各条件1試行で、区間の時間は Profiler 自体の負荷を含みます。次に試す場合は、通常経路へ切り替える際に取得済みの行列を同じ描画内で再利用しつつ、描画をまたぐキャッシュへの保存は既存の世代判定で守る方針です。

研究用ソースと DLL ハッシュ、対照版・試作版の計時と `timing/summary_a1_focus_p1_focus_p2_focus_a2_focus.json`、現行版の `profile/summary.json`、判定の内訳 `trial_guards/summary.json`、GUI 比較 `gate/comparison.json` は `build/fixed_cube/deform_matrix_only/` に保存しました（Git 管理外）。

### 同じ描画内で取得済みの変形行列を通常更新へ渡す試作

前節の試作で入力を二度読んだ条件を調べました。新しい試作は、接続中の `shapeDeformMatrix` の読み取りに成功したとき、その値と読み取り直後の世代番号を `requiresUpdate()` のローカル変数に保持します。同じ呼び出しで通常更新へ進み、DAG パスの世代と取得後の行列世代が一致し、評価コンテキストが通常であれば、取得済みの値を描画状態の計算へ渡します。読み取り中に世代が変わった値の有効範囲はその呼び出し内です。

Maya 2025.3.3／OpenGL で、配布版と同じ描画コードの対照版、前節の試作、今回の試作を同じ Release ビルド設定で比較しました。各 Cube は独立した `transform.matrix` に接続し、同じ10枝×100個のシーンを使います。計時用の各版は独立した Maya で起動し、2巡目は DLL と操作条件の両方の順序を反転します。

表の左／右は各巡3試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。キャッシュ ON は計測の前後で71フレームの充填を確認しました。6起動で代表フレームの画像、ドラッグの軌跡・移動量が一致しました。

| 条件 | 配布版相当 | 前回試作 | 今回試作 |
| --- | ---: | ---: | ---: |
| 共通親固定・変形入力0個・再生 OFF | 3.01／2.89 | 3.26／2.77 | 3.95／2.81 |
| 共通親固定・変形入力0個・再生 ON | 3.40／3.05 | 3.08／2.79 | 2.96／2.72 |
| 共通親移動・変形入力0個・再生 OFF | 5.98／6.02 | 6.33／5.80 | 5.91／6.04 |
| 共通親移動・変形入力0個・再生 ON | 6.33／7.17 | 6.53／7.03 | 6.60／6.98 |
| 共通親移動・変形入力100個・再生 OFF | 6.94／7.06 | 6.79／6.91 | 6.65／6.97 |
| 共通親移動・変形入力100個・再生 ON | 7.25／7.76 | 7.52／7.42 | 7.33／7.55 |
| 共通親移動・変形入力1,000個・再生 OFF | 15.32／15.52 | 13.38／13.14 | 13.20／13.40 |
| 共通親移動・変形入力1,000個・再生 ON | 15.77／15.57 | 17.65／16.56 | 15.65／16.01 |
| 単体ドラッグ | 7.18／5.01 | 4.67／4.86 | 4.48／4.93 |
| 1枝のドラッグ（100個） | 4.87／4.97 | 5.02／5.23 | 4.68／5.19 |
| 共通親のドラッグ（1,000個） | 8.00／8.70 | 8.08／8.57 | 8.03／8.27 |

全1,000個の変形で、今回試作の充填済み ON は前回試作より2.00／0.55 ms短縮し、配布版相当との差は −0.12／+0.44 msでした。OFF は配布版相当より2.12／2.13 ms短縮しました。変形が100個の再生とドラッグでは、配布版相当との差の大きさや向きが条件・起動順によって変わりました。

診断版では充填済み ON の各71実描画で、100個が変形する条件の入力読み取りが前回試作の14,200回から7,100回、1,000個が変形する条件では142,000回から71,000回に減りました。どちらも配布版相当と同じ回数です。このうち通常更新で取得済みの行列を使ったのは7,000件と70,000件でした。照合用 DLL でこの77,000件すべての値を独立に取得し直し、行列が一致しました。OFF は変形した7,100件と71,000件すべてが行列だけを更新する経路に進みました。

診断を外した今回試作で GUI の373件の判定を通過し、配布版の静止画125枚、再生画像53枚、参照画像6枚、画面選択58件と一致しました。同じ検証を照合用 DLL で実行し、充填済みキャッシュで行列を引き継いだ順再生16件、逆再生16件、スクラブ8件のすべてで直接取得値と一致しました。

全1,000個が変形する条件に絞り、配布版相当 → 今回試作 → 今回試作 → 配布版相当の順でさらに4回起動しました。各条件5試行の中央値は次の通りです（ms／実描画、各試行71描画）。

| 全変形の再計測 | 配布版相当 | 今回試作 | 差（今回試作 − 配布版相当） |
| --- | ---: | ---: | ---: |
| キャッシュ OFF | 15.30／16.03 | 13.48／13.57 | −1.82／−2.46 |
| 充填済み ON | 16.15／15.57 | 15.96／15.69 | −0.19／+0.12 |

11条件の比較と追加計測を合わせた4組すべてで、全変形・OFF は配布版相当より1.82〜2.46 ms短くなりました。全変形・充填済み ON は −0.19〜+0.44 msの範囲で差の向きが変わり、前回試作で起動順を問わず見られた遅れは再現しませんでした。二重読み取りの解消と OFF の短縮を根拠に、この試作を配布版への取り込み候補とします。性能と実描画の検証対象は Maya 2025 です。

研究版ソースと DLL ハッシュは `build/fixed_cube/deform_matrix_carry/native/`、各試行と集計は同研究フォルダの `timing/summary_a1_b1_c1_c2_b2_a2.json` と `repeat/summary_a1_c1_c2_a2.json`、行列・画像・選択の検証記録は `checks/` に保存しました（Git 管理外）。

### 変形中の行列更新を配布版へ導入

`bdUtilNodes` の `bdShpL_DeformableCube` へ、適用済みの表示状態と基準形状を再利用できるときに、変形中も既存の描画項目の行列だけを更新する処理を取り込みました。入力取得中に世代が変わって通常更新へ戻る場合は、読み取り直後の世代と DAG パスを照合し、同じ描画呼び出し内で取得済みの行列を使います。描画をまたぐ行列キャッシュには、取得前後で世代が一致した値を保存します。

Maya 2025.3.3／OpenGL で旧配布 DLL と更新した配布 DLL を、前節と同じ1,000個の構成で比較しました。DLL と条件の順序を2巡目で反転し、各起動で11条件を3試行ずつ測定しました。表は共通親も動く再生条件の中央値です（1巡目／2巡目、ms／実描画）。

| 条件 | 旧配布版 | 更新版 | 差（更新版 − 旧配布版） |
| --- | ---: | ---: | ---: |
| 100個変形・キャッシュ OFF | 7.40／7.09 | 6.79／6.70 | −0.62／−0.39 |
| 100個変形・充填済み ON | 7.66／7.93 | 7.53／7.45 | −0.13／−0.48 |
| 1,000個変形・キャッシュ OFF | 15.73／16.12 | 13.63／13.22 | −2.10／−2.90 |
| 1,000個変形・充填済み ON | 15.98／15.45 | 17.15／15.18 | +1.17／−0.27 |

単体ドラッグは0.31／0.61 ms、共通親のドラッグは0.29／0.07 ms／マウス移動短縮しました。1枝のドラッグは −0.44／+0.30 ms でした。4起動で代表フレームの画像とドラッグの軌跡・移動量が一致しました。

全1,000個の変形に絞って各条件5試行で再計測しました。差は OFF が −2.67／−2.61 ms、充填済み ON が −0.01／+0.48 ms でした。全変形の OFF は2回の比較を通して4組すべてで短縮し、ON は起動順・試行によるばらつきがありました。

更新した Maya 2025 配布 DLL で GUI の373件の判定を通過しました。旧配布版による静止画125枚、再生画像53枚、参照画像6枚、画面選択58件とすべて一致しました。

各試行および集計は `build/fixed_cube/deform_matrix_carry_adoption/` の `timing/summary_a1_p1_p2_a2.json`、`repeat/summary_a1_p1_p2_a2.json`、`gate/packaged_summary.json` に保存しました（Git 管理外）。

### 充填済みキャッシュで変形行列を読むときの描画更新

`8b108d14` の `requiresUpdate()` では、接続中の `shapeDeformMatrix` を読み、読み取り前後の変形の世代番号を照合します。世代番号は入力の更新通知を受けたことを記録する番号です。行列値の一致とは別に扱います。

- 読み取り前後で世代が一致すると、描画用の行列キャッシュを更新できます。表示状態・基準形状・DAG パスも有効で、合成行列が変わった場合は、既存の描画項目の行列を更新します。
- 読み取り中に世代が進むと、その値を使える範囲を同じ `requiresUpdate()` 呼び出しに限ります。取得直後の世代と DAG パスがまだ有効なら、取得済みの行列を `readState()` へ渡します。ここでは親との合成行列と表示状態を確認します。続く `update()` は、変更された項目を描画へ反映します。形状の世代が同じならローカル頂点やバッファを再生成する必要はありません。

前節の実装に対応する診断 DLL の既存記録では、共通親と独立した1,000個の変形入力がすべて動いた71実描画で、OFF は71,000件すべてが行列のみの更新へ進みました。充填済み ON は通常の `readState()` が71,000回、そのうち直前に取得した行列を渡したものが70,000回でした。両条件で入力の読み取りは71,000回でした。キャッシュの設定を直接判定する分岐はなく、各描画で観測した世代と描画状態に応じて経路が決まります。

#### 行列読み取り中に世代を進めた通知

Maya 2025.3.3／OpenGL、Parallel 評価で、各 Cube に別々の `transform.matrix` を接続し、共通親と100個または1,000個の入力を動かしました。現行コードに通知元ごとのカウンターを加えた診断 DLL を別々の Maya で2回起動し、2巡目は入力数と OFF／ON の順序を反転しました。各条件3試行、各試行71実描画です。ON は計測前後とも対象71フレームの充填を確認し、代表フレームの画像を配布版と照合しました。

| 入力が変化した Cube 1個・1実描画当たり | OFF | 充填済み ON |
| --- | ---: | ---: |
| 行列読み取り中の `setInternalValue(shapeDeformMatrix)` | 0回 | 1回 |
| 行列読み取りの外の同じ通知 | 1回 | 0回 |
| 行列読み取りの外で入力 dirty を報告した `postEvaluation()` | 1回（`kEvaluatedIndirectly`） | 1回（`kEvaluatedDirectly`） |
| 行列読み取り前後の世代番号の増分 | 0 | 1 |

両起動の全試行で同じ回数でした。充填済み ON で読み取り中に進んだ全世代を、同じ Cube・同じスレッドでの `setInternalValue()` で説明できました。内訳は1試行当たり100個で7,100件、1,000個で71,000件です。他の通知元による読み取り中の増分は0件でした。`setInternalValue()` は現行コードの `dirtyMatrix()` を通じて世代を進め、VP2 に描画の更新を通知します。これは Maya からプラグインに届いた呼び出しを観測した結果です。

| 診断 DLL の区間（ms／実描画） | 100個 OFF | 100個 ON | 1,000個 OFF | 1,000個 ON |
| --- | ---: | ---: | ---: | ---: |
| 入力に接続した行列の読み取り | 0.22／0.22 | 0.45／0.36 | 2.05／2.35 | 3.36／3.61 |
| 取得済みの行列を渡した `readState()` の呼び出し区間 | 0／0 | 0.25／0.23 | 0／0 | 2.04／2.19 |
| 行列のみの経路に入った `update()` | 1.37／1.40 | 1.33／1.23 | 1.61／1.75 | 0／0 |
| 通常経路に入った `update()` | 0／0 | 0.23／0.20 | 0／0 | 2.17／2.34 |

左／右は各巡3試行の中央値です。入力100個の ON でも共通親は全1,000個を動かすため、変形しない900個が行列のみの `update()` に入ります。1,000個の ON では全件が通常更新に入り、各試行で70,000件が取得済みの行列を引き継ぎました。上の時間には診断処理が入り、`update()` は必要な `setMatrix()` の時間も含みます。短縮できる時間は診断なしの DLL で比較します。

別の診断 DLL で同じ4条件を2巡計測し、`setInternalValue()` が呼ぶ `dirtyMatrix()` にかかる時間を分けました。1,000個変形・充填済み ON では、接続行列の読み取り全体が3.32／3.20 ms、その中の `dirtyMatrix()` が0.129／0.124 ms、さらにその中の `MRenderer::setGeometryDrawDirty()` が0.063／0.059 msでした。OFF の `dirtyMatrix()` は読み取りの外で0.244／0.242 msでした。通知の呼び出しから戻るまでの時間は、ON で通常更新へ切り替わった後の時間より小さく、通知後に Maya が別途行う処理はこの通知の区間計時に含みません。

#### 取得直後の世代を使って、その描画の行列だけを更新する試作

研究版は、接続行列を読んだ後の世代番号、時刻、親のワールド行列を `requiresUpdate()` から対応する `update()` まで保持します。`update()` で時刻、通常評価コンテキスト、入力と基準形状の世代、DAG、ワールド行列、表示状態、描画項目を照合できた場合、準備した合成行列を既存の描画項目に渡します。次の描画のローカル行列には持ち越しません。

照合用 DLL は、採用したパス、合成行列、表示状態を別途取り直しました。充填済み ON の71実描画で試作経路に進んだ7,000件（100個変形）と70,000件（1,000個変形）は全件一致しました。別の GUI 試験では、順再生16件、逆再生15件、スクラブ7件、手動編集1件でこの経路を照合し、すべて一致しました。診断なしの試作と現行配布版はそれぞれ373件の GUI 判定を通過し、静止画125枚、再生画像53枚、静止参照6枚、画面選択58件が一致しました。

計時は、現行版と同じ描画コードの対照 DLL と試作 DLL を同じノード登録・Release ビルド設定で作り、診断を外して比較しました。対照 → 試作 → 試作 → 対照の順で独立起動し、2巡目は条件順も反転しました。左／右は各巡5試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。

| 条件 | 対照版 | 試作版 |
| --- | ---: | ---: |
| 共通親移動・100個変形・OFF | 7.41／6.97 | 7.52／7.17 |
| 共通親移動・100個変形・充填済み ON | 7.39／7.85 | 7.62／7.15 |
| 共通親移動・1,000個変形・OFF | 13.50／14.42 | 13.78／13.74 |
| 共通親移動・1,000個変形・充填済み ON | 15.97／15.77 | 14.32／13.60 |
| 単体ドラッグ | 4.51／4.85 | 4.53／5.34 |
| 枝のドラッグ（100個） | 4.61／4.97 | 4.64／4.66 |
| 共通親ドラッグ（1,000個） | 7.93／8.14 | 7.94／8.01 |

全変形の再生と固定入力での単体ドラッグを独立した4起動で再計測しました（同じ起動順、各5試行）。全変形・充填済み ON は対照版15.93／16.27 → 試作13.35／14.67 ms／実描画で、2.58／1.60 ms短縮しました。全変形・OFF は13.51／13.66 → 13.44／13.54 msでした。単体ドラッグは4.78／4.92 → 4.44／4.73 ms／移動で、最初の比較の2巡目に出た0.49 msの遅れは再現しませんでした。

全変形・充填済み ON は計4組すべてで1.60〜2.58 ms／実描画（約10〜16%）短くなりました。100個変形・充填済み ON は初回比較で +0.24／−0.70 ms、ドラッグと全変形 OFF も差の向きや大きさにばらつきがありました。Maya 2025 の全変形・充填済み ON 向けの取り込み候補とします。対象バージョンの配布 DLL への組み込みと、そのバイナリでの機能・速度確認は次の段階です。

生データと再実行スクリプトは `build/fixed_cube/cached_revision_study/`（Git 管理外）にあります。通知と区間計時は `profile/summary_rev1_rev2.json` と `setter_profile/summary_rev1_rev2.json`、照合は `oracle_profile/counts_summary.json` と `gate/{gui,oracle}_summary.json`、診断なしの計時は `timing/summary_a1_c1_c2_a2.json` と `repeat/summary_a1_c1_c2_a2.json` です。

#### 充填済みキャッシュの行列更新を配布版へ導入

`bdUtilNodes` に試作の更新処理を取り込みました。接続行列の読み取り中に世代が進んだ場合は、`update()` で取得後の世代と時刻、DAG、基準形状、ワールド行列、表示状態、描画項目を再確認します。条件が揃えば既存の描画項目に合成行列を渡します。条件が変わった場合は現在の値から描画状態を読み直します。

Maya 2025.3.3／OpenGL で、新旧の配布 DLL を4回の独立した起動で比較しました。共通親の下に10枝×100個を配置し、各 Cube に個別の変形入力を接続しています。2巡目は DLL と条件の順を反転しました。左／右は各巡3試行の中央値です。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。

| 条件 | 旧配布版 | 更新版 |
| --- | ---: | ---: |
| 共通親移動・100個変形・OFF | 6.65／6.45 | 6.65／6.65 |
| 共通親移動・100個変形・充填済み ON | 7.17／7.03 | 7.75／7.19 |
| 共通親移動・1,000個変形・OFF | 12.77／12.63 | 13.08／13.11 |
| 共通親移動・1,000個変形・充填済み ON | 15.37／14.68 | 13.80／13.48 |
| 単体ドラッグ | 4.45／4.77 | 4.79／4.69 |
| 枝のドラッグ（100個） | 4.29／4.70 | 4.88／4.76 |
| 共通親ドラッグ（1,000個） | 7.57／7.41 | 8.30／8.48 |

全変形の再生と固定入力の単体・共通親ドラッグは、同じDLLで独立した4起動による各5試行の比較を追加しました。

| 再計測の条件 | 旧配布版 | 更新版 |
| --- | ---: | ---: |
| 共通親移動・1,000個変形・OFF | 12.74／12.78 | 12.67／12.77 |
| 共通親移動・1,000個変形・充填済み ON | 15.12／14.44 | 13.32／13.04 |
| 単体ドラッグ | 4.26／4.31 | 4.16／4.57 |
| 共通親ドラッグ（1,000個） | 7.48／7.35 | 7.19／7.87 |

全変形・充填済み ON は、2回の計測を通じて4組すべてで1.20〜1.80 ms／実描画（約8〜12%）短縮しました。全変形・OFF は最初の比較で0.31／0.48 ms長く、再計測では0.07／0.01 ms短くなりました。共通親ドラッグは最初の比較で0.73／1.08 ms長く、再計測では0.30 ms短い回と0.51 ms長い回がありました。共通親ドラッグの所要時間には、配布版でも試行間のばらつきが残ります。

更新した Maya 2025 配布 DLL で GUI の373件の判定を通過しました。順再生・逆再生・スクラブや、変形と表示編集が同じフレームにある条件を含め、静止画125枚、再生画像53枚、参照画像6枚、画面選択58件が旧版と一致しました。

各試行、読み込んだ DLL、照合結果は `build/fixed_cube/cached_revision_adoption/`（Git 管理外）の `timing/summary_a1_p1_p2_a2.json`、`repeat/summary_a1_p1_p2_a2.json`、`gate/packaged_summary.json` に保存しました。

## 参考

- [Autodesk Scene Overrides](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Viewport-2-0-API/Overview-of-the-Viewport-2-0-API/Maya_DEVHELP_Viewport_2_0_API_Overview_of_the_Viewport_2_0_API_Scene_Overrides_html.html)
- [MRenderItem](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_render_item.html)
- 既存調査: `build/controller_performance/cube_investigation/`（Git 管理外）

既存 `bdControllerShape` の過去の数値と今回の測定値を、同条件の直接比較として混ぜません。
