# 固定 Cube の描画速度研究

`bdShpL_Cube` は、既定のローカル座標が各軸 `±0.5 cm` の線のみ Cube です。
既定では8頂点・12辺を使い、軸と各面の位置を8個の静的な属性で調整します。
`shapeGuideLine` を ON にすると、対向する面の中央を結ぶ3本の線を追加します。
`shapeFin` を ON にすると、第2軸の Plus 面に Fin を追加します。
親 DAG 階層の最終行列を反映し、pivot、rotateAxis、shear、jointOrient、
offsetParentMatrix を Maya 標準の計算へ委譲します。
頂点を TRS に分解した値で作り直す処理はありません。

<a id="cube-extension-guide"></a>

## 次のコントローラー形状を開発するときに

2026-11-25 時点で、線の Cube 2型の速度改善を一区切りとしました。次の形状・機能を評価するときは、その時点の配布版 `bdUtilNodes` を基準にします。後続の節には、採用前の試作や取り下げた属性の計測も時系列で残しています。

| リグで実現したい動作 | 実装を参照する型 | 拡張時に引き継ぐ点 |
| --- | --- | --- |
| 作成時に軸・寸法を決め、アニメーションでは親階層に追従する | `bdShpL_Cube`（Geometry） | 軸・寸法8属性、ガイド、Fin は直接編集でき、キーと入力接続を禁止。設定を変えた個体のローカル形状を更新し、親の操作ではその形状を再利用する。 |
| 親階層への追従に加えて、シェイプ自体を行列で変形する | `bdShpL_DeformableCube`（SubScene） | 同じ静的属性で本体・ガイド・Fin を作る。`shapeDeformMatrix`（`sdm`）を直接設定または接続し、行列だけの変更では頂点を再利用する。描画行列の順序は `shapeDeformMatrix * 親のワールド行列`。 |
| 本体と独立した範囲にフォーカスする | `bdShpL_FocusBoundingBox`（Geometry） | 同じ transform の先頭に Box、その次に本体を置く。`showShape` で Box のプレビューを切り替える。 |

両 Cube は頂点・辺・境界の定義と、軸・寸法からローカル形状を組み立てる処理を共有します。新しい輪郭を実装するときはこの2か所から辿れます。[基準頂点・辺・境界](../../plugins/bdUtilNodes/include/bdUtilNodes/draw/FixedCubeGeometry.h)・[静的属性と形状構築](../../plugins/bdUtilNodes/include/bdUtilNodes/nodes/FixedCubeShape.h)

形状設定と変形行列は別々に失効させます。変形 Cube は通常の評価コンテキストで、時刻と変形入力の世代が合う評価済み行列を描画に利用します。再生中にその値を使えるときは、親行列と表示状態を適用時に確認します。DAG の付け替え、表示変更、描画アイテムの再作成などで前提が崩れた場合は通常の更新に戻ります。[dirty と独自キャッシュ](../../docs/evaluation.md#dirty-propagation)・[再生時の配布実装](#再生時の取得をまとめる処理を配布版に取り込み)

### 機能を追加する際の判断

- **静的属性を増やすとき**は、暖機後の親操作・再生で何回値を読み、形状やバッファを更新したかを調べます。軸・寸法の診断では、この区間で属性の読み取りと形状再生成は0回、1個の寸法を編集した対照では対象の形状再生成を1回検出しました。未参照の bool を100個追加した結果にも描画方式・条件による差があり、属性1個当たりのコストは求められていません。[静的属性の計装](#軸寸法と-fin-の静的属性の読み取り更新)・[未参照属性の比較](#未参照の-bool-100個と再生速度)
- **Fin や部分テンプレート線を追加するとき**は、必要なシェイプ型に絞ります。共通 Cube への追加試作では OFF でも一部の操作や再生に差が出ました。色や Fill で描画アイテムを増やす設計では、現行 SubScene の行列だけを更新する経路が、同一の描画アイテム1個を前提にしている点に注意します。複数アイテムで同じ経路を使うなら、全アイテムが変形・表示・選択に追従するかを確認します。[Fin](#cube-の-fin-の試作)・[部分テンプレート線](#cube-の部分テンプレート線の試作)・[SubScene の実装](../../plugins/bdUtilNodes/src/nodes/BdShpLDeformableCubeSubSceneOverride.cpp)
- **輪郭が変わるとき**は、描画した端点と境界を一緒に確認します。Cube 本体は8頂点が境界の8隅に一致するので、本体の境界を行列変換して変形後の範囲を求めます。Fin のような突出部は実端点を変換して境界へ加え、その端でフォーカスとクリック選択を確認します。[変形後の境界計算](../../plugins/bdUtilNodes/src/nodes/BdShpLDeformableCubeNode.cpp)・[フォーカス用シェイプの構成](#フォーカス用の兄弟シェイプ付きコントローラー)

### 拡張前後を比較する条件

1. **同じリグ操作を再現する。** Maya 2025 の基準シーンは、共通親の下に transform と shape を1,000組配置します。共通親ドラッグと、1個の shape の直親だけを動かす単体ドラッグを測ります。枝の追従を見る場合は動いた個数も記録します。行列変形の本番想定では個体別の入力を使い、未接続、接続して静止、一部または全個体が変形する場合を比べます。標準カーブを対照にする場合、固定は同形の1次カーブ、変形は各 CV に `pointMatrixMult` を接続した構成が比較元です。[描画方式と標準カーブ](#maya-2025-の描画方式と-cv-変形の比較)・[個別の行列入力](#個別の変形行列と-dirty-伝搬)
2. **未使用時の負荷と再生停止後の応答を測る。** 拡張前、拡張後の既定・未使用時、使用時を比較します。再生は Cached Playback OFF と充填済み ON で実描画数と代表フレームの画像を照合し、ms／実描画で記録します。変形再生を変更した場合は、停止直後の最初のドラッグも通常の単体ドラッグと別に測ります。描画やキャッシュの変更に応じて、同一フレームでの入力編集、親の付け替え、選択・表示変更、VP2 リセット後の表示も確認します。[停止直後と通常のドラッグ](#配布版の停止直後と通常の単体ドラッグ)・[描画・選択の検証](../../docs/testing-debugging.md)
3. **標準計測では Channel Box を閉じる。** 属性表示による操作時間の変動を抑えた条件で、拡張前、追加機能 OFF、使用時を比較します。ビューポートのピクセル寸法を各版で固定します。ドラッグでは操作対象を選択し、再生でも比較する試行の選択状態を揃えます。Channel Box の応答自体を調べる場合に、開閉を比較します。[GuideLine／Fin 追加後の Channel Box 開閉比較](#channel-box-performance)
4. **小さな差の再現性を確認する。** 同じ配布条件の Release DLL、カメラ、Move ツール、UI 表示で比較し、実行順を反転して各起動の中央値を見ます。原因を調べるときは、ドラッグの入力から描画後通知までと、その後のイベント処理の時間を確認し、通常計時と計装時の回数を照らし合わせます。Qt へ一定軌道を送った ms／入力と、手動操作中の HUD FPS は別の指標です。[部分階層での Geometry 呼び出し](#部分階層を動かしたときの-geometry-の処理回数)・[ドラッグと UI 更新](#10個が追従するドラッグと-maya-の-ui-更新)

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

`bdShpL_Cube` やフォーカス用シェイプに `shapeTransformMatrix` を追加した計測は、仕様変更前の研究記録です。固定 Cube に行列入力を持たせた試作を再検証するときは、研究 DLL のビルドに `-ShapeMatrix` を指定します。配布版の Cube 2型のうち、形状変形の行列入力を扱うのは `bdShpL_DeformableCube` で、属性名は `shapeDeformMatrix` です。

静的版は Maya 2025 の GUI で、Cube に立体または平面の Box を組み合わせ、フォーカス、プレビュー切替、Cube の辺の選択を確認しました。
共通親を移動・回転させて再生し、キャッシュ OFF・充填中・復元時に採取した描画を3姿勢の参照画像と照合しました。

## 静的な形状設定（2026-11-18）

本体と研究用 Geometry / SubScene 版の軸・寸法設定は次の8属性です。

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

### 中央ガイド線（2026-11-26）

両 Cube は `shapeGuideLine`（短縮名 `sgl`、bool、既定 `False`）を持ちます。
軸・寸法と同じ静的設定で、Channel Box から直接編集でき、キー設定と入力接続は禁止します。
`True` にすると、本体の中心を通って対向する6面の中央を結ぶ3本の通常線を追加します。
本体と同じ色・選択可否で描画し、`shapeGuideLineTemplate` は持ちません。
非対称な寸法、面の反転、平面・線・点への縮退でも本体の範囲を広げず、
DeformableCube では本体と同じ `shapeDeformMatrix` と親の行列に追従します。

OFF は8頂点・12辺、ON は14頂点・15辺で、いずれも描画アイテムは1個です。
設定を変えた個体の形状と辺の接続を更新し、親操作や変形行列だけの変更では再利用します。
SubScene の既定ガイド付きバッファは初回 ON 時に作り、renderer ごとに共有します。
OFF へ戻した個体は通常のバッファを使います。非既定寸法の個体専用バッファも、
既定形状へ戻った時点で共有バッファへ切り替えて解放します。

Maya 2025 の GUI では、両型の既定・非対称寸法・軸変更・平面・点、変形 Cube の
行列変形、ON/OFF 混在、Undo/Redo、VP2 リセット、保存・再読込を確認しました。
OFF に戻した画像は切替前と一致し、ガイド線の有無で境界は変わりません。
本体の辺から画面上で19px以上離したガイド上の点を各型6方向でクリックし、
ON のみ選択できることを確認しました。記録は
`build/fixed_cube/guideline_20261126/gate/summary_b1_retry4.json` です。

#### ガイド追加前後の速度比較

Maya 2025.3.3 / OpenGL / GeForce GTX 1660 SUPER で、変更前の配布 Release DLLを保全し、
追加前（A）、追加後 OFF（B）、追加後 ON（C）を比較しました。
1,000組の transform / shape を10枝に配置し、変形入力は個体別です。
各構成を `A1 → B1 → C1 → C2 → B2 → A2` の順で独立起動し、後半はドラッグ対象・キャッシュの順も反転しました。
5構成・30起動・18条件・540試行で、各起動内の条件ごとに5試行の中央値を求め、同じ版の2起動の中央値を以下へ示します。
CP は Cached Playback で、ON は要求71フレームのキャッシュ充填済みです。
再生は71実描画、ドラッグは72入力・72描画を照合しました。単位は再生が ms／実描画、
ドラッグが ms／入力で、GPU単体時間や手動操作の FPS ではありません。

| 型・変形入力 | 操作 | CP | 追加前 A | OFF B | ON C |
| --- | --- | --- | ---: | ---: | ---: |
| Cube | 共通親ドラッグ | OFF | 9.240 | 8.957 | 8.914 |
| Cube | 単体ドラッグ | OFF | 3.289 | 3.360 | 3.369 |
| Cube | 再生 | OFF | 3.112 | 3.204 | 3.333 |
| Cube | 再生 | ON | 4.031 | 4.041 | 3.668 |
| Deformable・未接続 | 共通親ドラッグ | OFF | 8.296 | 8.480 | 8.350 |
| Deformable・未接続 | 単体ドラッグ | OFF | 5.092 | 5.224 | 5.176 |
| Deformable・未接続 | 再生 | OFF | 6.099 | 6.708 | 6.231 |
| Deformable・未接続 | 再生 | ON | 6.818 | 6.844 | 6.909 |
| Deformable・接続して静止 | 共通親ドラッグ | OFF | 8.448 | 8.162 | 8.377 |
| Deformable・接続して静止 | 単体ドラッグ | OFF | 5.168 | 5.246 | 5.167 |
| Deformable・接続して静止 | 再生 | OFF | 6.680 | 6.187 | 6.310 |
| Deformable・接続して静止 | 再生 | ON | 6.818 | 6.941 | 7.139 |
| Deformable・100個変形 | 再生 | OFF | 6.968 | 6.890 | 6.923 |
| Deformable・100個変形 | 再生 | ON | 7.141 | 7.270 | 7.401 |
| Deformable・1,000個変形 | 再生 | OFF | 12.502 | 12.360 | 12.601 |
| Deformable・1,000個変形 | 再生 | ON | 10.753 | 11.019 | 11.206 |
| Deformable・1,000個変形 | 停止直後の単体ドラッグ | OFF | 5.321 | 5.177 | 5.415 |
| Deformable・1,000個変形 | 停止直後の単体ドラッグ | ON | 5.306 | 5.541 | 5.362 |

OFF は追加前と代表フレーム・操作後の画像が一致し、ON は正順・逆順の起動で画像が一致しました。
選択、カメラ、表示サイズ、移動量、キャッシュ、実際に読み込んだ DLL と計測コードの hash も照合しています。
停止直後の最初の入力から描画までの A / B は CP OFF で3.458 / 3.545 ms、
CP ON で3.685 / 3.599 msでした。停止から最初の入力後描画まででは、
それぞれ23.338 / 21.923 ms、23.969 / 23.950 msです。どちらも対ごとの差は正負に分かれました。

未接続 Deformable の CP OFF 再生は、最初の2対で OFF が +0.461 / +0.756 ms
（+7.70% / +12.18%）となったため、同じ入力・コードで `A1 → B1 → B2 → A2` の4起動を追加しました。
この80試行も画像・入力・キャッシュ・描画数の監査を通過しています。

| 未接続 Deformable の追加反復 | 追加前 A | OFF B | 2対の B − A |
| --- | ---: | ---: | ---: |
| 共通親ドラッグ | 8.134 | 8.301 | +0.268 / +0.067 |
| 単体ドラッグ | 5.087 | 5.085 | +0.170 / −0.173 |
| 再生・CP OFF | 6.300 | 6.085 | −0.569 / +0.138 |
| 再生・CP ON | 6.756 | 7.097 | +0.202 / +0.481 |

注目した CP OFF 再生の増加は、追加反復では −8.64% / +2.29%となり、一方向には再現しませんでした。
一方、CP ON などでは0.1〜0.5 ms程度の正差も観測しています。
OFF の速度は概ね近い範囲ですが、これらの小差を属性追加の影響と起動・試行の揺れに分離できていないため、
「追加負荷ゼロ」「すべての条件で同速」とは判定しません。
今回の実装では OFF の頂点・辺・描画アイテム数を維持し、通常の行列更新にガイド属性の読取りを追加していません。

本計測の記録は `build/fixed_cube/guideline_20261126/timing_v2/` に保存しています。
`audit_all30.json` が各起動の監査、`performance_summary.json` が上表と2対の差、
`interaction_detail.json` が初回応答と継続ドラッグの集計です。
追加反復は `runs/*_unconnected_retry1/` と、その4起動名を含む `summary_*.json` に保存しています。
`unconnected_followup.json` には初回と追加反復の4条件をまとめています。
初期ハーネスの `timing/runs/a1` は、追加前 DLL の2シーン目の初期描画で Maya が停止したため集計外です。
`timing_v2` は既存のドラッグ比較と同様に1起動1シーンとし、親のキーを切り替えてドラッグと再生を測っています。

Maya 2025 / 2026 / 2027 の配布 DLL を更新し、
`verify.cmd -IncludeNative -IncludeCubeResearch` は成功しました。
速度と実画面の比較は Maya 2025 のこの環境で行った結果で、2026 / 2027 の速度比較は行っていません。

[ガイド OFF の追加調査](guide_line_off_cost.md)には、同じ DLL を起動し直した際の揺れ、属性登録から完成版までの段階比較、通常操作と設定編集で実際に発生した処理回数を記録しています。

### 配布版の Fin

両 Cube は `shapeFin` を既定の `False` から `True` にすると、通常線の Fin を1枚表示します。
4属性の名前・短縮名・型と既定値は[パッケージの属性表](../../../../bakedanuki/bakedanuki-util/README.md#固定-cube)を参照してください。
`shapeGuideLine` と Fin はそれぞれ独立して設定でき、ガイドの端点は本体の対向面の中央です。

Fin の付け根は第2軸の論理 Plus 面、第3軸方向の位置は両面の中点です。面が反転すると外向きも反転し、
第2軸の厚みが0のときは、選んだ第2軸の正方向へ高さを取ります。
`Standard` は第1軸に平行な上辺と2本の立ち上がりを描き、`Tapered` は既定の向きで第1軸の Plus 側へ低くなります。
どちらも根元を閉じる線は省きます。幅倍率の絶対値が1を超える場合、`Standard` は立ち上がりも広がります。
`Tapered` は両根元を本体幅に収めて自由端を拡げます。高さ0では本体と指定されたガイドを描き、幅0では高さ方向の線が残ります。
DeformableCube の変形後の境界には、本体8隅に加えて変形した Fin の実端点を含めます。

#### 配布版の速度比較

Maya 2025 の1,000個のシーンで、`shapeGuideLine` 追加済みの前版と今回の配布版を比較しました。
`shapeGuideLine` は OFF とし、1起動1シーン、各条件5試行の中央値を起動ごとに集計しています。
前版との Fin OFF 比較と配布版内の Fin ON 比較は、合計24起動480試行です。
Fin OFF の各条件で、前版とビューポート画像が一致しました。

| 比較 | 条件 | 差 |
| --- | --- | --- |
| Fin OFF − 前版 | 変形行列未接続の DeformableCube の単体ドラッグ、初回 | +0.272 ms／入力 |
| Fin OFF − 前版 | 同条件、起動順を反転した追試 | +0.187 ms／入力 |
| Fin ON − OFF | 1,000個の変形行列を接続した DeformableCube の再生、Cached Playback OFF | +0.413 ms／描画フレーム |
| Fin ON − OFF | 同条件、Cached Playback ON | +0.088 ms／描画フレーム |

変形行列未接続の単体ドラッグは、Fin OFF で比較した全4組で遅くなりました。
計装版の固定 Cube と未接続の DeformableCube では、Fin OFF の反復操作中に Fin 設定の読み取り、
ジオメトリの再構築、頂点・インデックスバッファの更新は発生しませんでした。
同じ配布 DLL を使う別の4起動では、Fin 4属性の Channel Box 表示を外すと未接続の単体ドラッグが
平均0.138 ms／入力短くなりました。Channel Box には選択した Shape が表示されており、
属性の表示設定がこの条件の負荷の一因だと分かりました。配布版では4属性を Channel Box から編集できます。

<a id="channel-box-performance"></a>

#### GuideLine／Fin 追加後の Channel Box 開閉比較

Maya 2025 / OpenGL で、GuideLine と Fin を追加する直前の配布版（`cd163b4a`）と、両方を追加した配布版を比較しました。
追加後の版では `shapeGuideLine=False`、`shapeFin=False` とし、各シーンに Cube を1,000個配置しました。
3構成それぞれで、前版・追加後とパネルの開・閉を組み合わせた4条件を、起動順を反転して2回ずつ計測しました。
各操作の5試行の中央値を起動単位で集計し、計24起動・480試行を採用しました。
ビューポートを956×676ピクセルに固定し、比較する選択状態と描画画像の一致を確認しました。

表は、パネルの状態ごとに求めた「追加後 − 前版」の差です。正の値は追加後のほうが遅いことを示します。
ドラッグは ms／入力、再生は ms／描画フレームです。併記した値は Cached Playback OFF、ON の順です。

| シーン | 操作 | Channel Box 開 | Channel Box 閉 |
| --- | --- | ---: | ---: |
| 固定 Cube | 親ドラッグ | +0.006 | +0.001 |
| 固定 Cube | 単体ドラッグ | +0.242 | −0.060 |
| 固定 Cube | 再生 OFF／ON | +0.075／+0.016 | −0.090／−0.027 |
| DeformableCube・変形行列未接続 | 親ドラッグ | −0.036 | −0.002 |
| DeformableCube・変形行列未接続 | 単体ドラッグ | +0.123 | +0.046 |
| DeformableCube・変形行列未接続 | 再生 OFF／ON | −0.109／+0.108 | +0.065／+0.065 |
| DeformableCube・全個体の変形行列を接続 | 再生 OFF／ON | −0.039／+0.270 | −0.296／−0.278 |
| DeformableCube・全個体の変形行列を接続 | 再生停止直後の単体ドラッグ OFF／ON | +0.244／+0.268 | −0.120／+0.082 |

Channel Box を閉じた条件では、GuideLine と Fin が OFF の単純 Cube は、計測したドラッグ・再生で前版に近い速度でした。
開いた条件では、単体ドラッグの継続区間に含まれる Qt の `processEvents` の版間差が、閉じた条件より0.108〜0.154 ms／入力大きくなりました。
この増分は起動順を変えても観測でき、Fin 4属性だけを非表示にしたときの結果とも整合します。
未接続の単体ドラッグ全体では反復によって開閉の効果の向きが変わり、親ドラッグの結果も起動順によって変動しました。
今回の計測は GuideLine と Fin の合計の比較で、属性1個あたりの処理時間は求めていません。

全個体接続の再生では、同じシェイプを選択してパネルを開いても、計測前後の80回の確認で選択シェイプの属性行は表示されませんでした。
この条件の再生値は、ドックの開閉に対する結果として扱います。
集計と起動ごとの記録は `build/fixed_cube/channelbox_panel_20261126/`（Git 管理外）に保存しています。

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
静的属性の定義・軸の組合せ・非対称な各面の位置・ガイド切替時の境界不変・
キーと入力接続の拒否も対象です。
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

この記録はガイド追加前の DLL によるものです。現行ソースで `-StaticAttributesStudy` を再ビルドすると、`BaseAttributes` は `shapeGuideLine` も含むため、当時の8属性と固定値の比較と同じ属性構成にはなりません。

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

#### 共通親のドラッグと一部の Cube だけが変形する再生を再計測

Maya 2025.3.3／OpenGL で、旧配布 DLL（`8b108d14`）と現行配布 DLL（`34dd53d5`）を、旧 → 旧 → 現行 → 現行 → 旧 → 旧の順で独立起動しました。中央4起動で新旧を比較し、その前後の連続した旧版2起動を対照としました。1,000個・10枝のシーンで各 Cube に個別の行列を接続し、各条件5試行を計測しました。再生は71実描画、ドラッグは72回のマウス移動と72実描画です。ON は計測前後で充填を確認し、各起動の代表フレーム画像とドラッグの操作軌跡・移動量も照合しました。

| 条件 | 現行 − 旧 | 同じ旧 DLL を再起動したときの差 |
| --- | ---: | ---: |
| 共通親ドラッグ（1,000個、変形入力は固定） | +0.09／+0.15 | +0.04／+0.37 |
| 単体ドラッグ | +0.17／+0.52 | −0.05／+0.15 |
| 共通親移動・100個変形・充填済み ON | −0.16／−0.21 | −0.09／+0.44 |
| 共通親移動・1,000個変形・充填済み ON | −1.81／−3.09 | −0.07／−0.45 |

左／右は起動順を反転した2組の差です。再生は ms／実描画、ドラッグは ms／マウス移動で、いずれも各起動5試行の中央値を使います。同一 DLL の列は各組の連続起動における後 − 前です。共通親ドラッグの差は、前節の初回比較で見られた0.73〜1.08 msより小さく、旧 DLL の再起動でも0.37 msの差が出ました。100個変形・充填済み ON は今回は両組で差の向きが反転しました。単体ドラッグは現行 DLL の起動間にも0.37 msの差がありました。全変形・充填済み ON の短縮は今回も両組で確認しました。

両版と同じ描画コードに診断を加え、旧 → 現行 → 現行 → 旧の順で別起動し、各条件3試行を測りました。共通親ドラッグの診断区間は押下とリリースを含む74実描画で、全試行で親の行列だけを反映したものが68,000件、更新を省略したものが6,000件でした。変形入力の読み取りと通常の描画状態取得は両版とも0件でした。親に追従する Cube の処理は次の通りです（左／右は各巡3試行の中央値、診断のオーバーヘッドを含む ms／実描画）。

| 共通親ドラッグの計時区間 | 旧版 | 現行版 |
| --- | ---: | ---: |
| `requiresUpdate()` | 1.66／1.85 | 1.66／1.76 |
| ↳ 保持した DAG パスからワールド行列を取得 | 0.93／1.06 | 0.94／1.02 |
| ↳ 選択などの表示ステータスを確認 | 0.34／0.37 | 0.32／0.33 |
| `update()` | 1.38／1.48 | 1.42／1.49 |
| ↳ `setMatrix()` | 0.73／0.78 | 0.73／0.77 |

100個変形・充填済み ON の各71実描画では、親に追従する900個は両版とも計63,900件が行列だけを更新し、通常更新への復帰は0件でした。行列の読み取りは変形した7,100件に限られ、回数は両版で一致しました。通常の描画状態取得は旧版7,100件から現行版100件に減り、残る7,000件は前節で導入した行列のみの更新を使いました。全1,000個が変形する ON 条件でも、読み取りと `setMatrix()` の回数は両版同じで、`requiresUpdate()` は6.11／6.74 → 4.62／4.56 msでした。

共通親ドラッグと一部変形の再生で、親に追従する Cube が余分な更新へ進む挙動は観測されませんでした。配布版の計時と診断の結果から、今回の共通親ドラッグと100個変形の差を説明できる共通の処理は特定できませんでした。現行実装を基準とします。

使用した DLL のハッシュ、全試行、集計は `build/fixed_cube/parent_followup/`（Git 管理外）の `timing/summary_a1_control_a1_p1_p2_a2_a2_control.json`、`profile/summary_a1_p1_p2_a2.json` に保存しました。

#### 描画前に届く変形行列の確認

Maya 2025.3.3／OpenGL の Parallel 評価で、共通親の下に10枝×100個を配置し、各 `bdShpL_DeformableCube` に別々の `transform.matrix` を接続しました。共通親を動かし、変形入力のうち0個、100個、1,000個にアニメーションを付けました。研究用 DLL は現行の描画処理に診断を追加し、`setInternalValue()` で受け取ったデータハンドルから行列を取得して、同じ Cube・時刻で現行の描画処理が実際に取得した行列と比較します。

独立した2回の起動で条件順を反転し、キャッシュ OFF と充填済み ON について各条件の順再生23描画、逆再生23描画、時刻が連続しないスクラブ6描画を観測しました。実際の描画順と充填範囲を確認し、代表フレームの描画画像を OFF で取得した参照画像と照合しました。

| 変形入力を取得した際の観測（2起動の合計） | OFF | 充填済み ON |
| --- | ---: | ---: |
| 現行の描画処理が入力を取得 | 114,400 | 114,400 |
| 描画前に `setInternalValue()` が同じ行列を受領 | 114,400 | 0 |
| 描画の入力取得中に `setInternalValue()` が同じ行列を受領 | 0 | 114,400 |
| コールバックで受け取った行列と描画時の行列が不一致 | 0 | 0 |

変形入力がすべて固定の条件では、充填済み ON と OFF の両方で描画時の入力取得は0件でした。変形がある OFF では、全件で行列を受け取った後に `postEvaluation(kEvaluatedIndirectly)` が世代を進めました。受領時点の世代を描画時点と照合すると全件不一致です。充填済み ON では、全件で `postEvaluation(kEvaluatedDirectly)` が描画の入力取得に先行し、行列を渡す `setInternalValue()` はその取得中に呼ばれました。

別の診断 DLL で、`postEvaluation()` 時点のノードのデータブロックを `forceCache()` で取得し、`isClean()` で入力の状態を調べました。入力値を読む呼び出しは追加せず、同じ条件を2回実行しました。OFF と充填済み ON はそれぞれ114,400件すべてで clean と判定され、`setInternalValue()` の順序と描画時の入力取得回数は先の診断と一致しました。clean の判定から分かるのはプラグの状態です。描画の取得前に同じ行列値を得られるかは、実際の値を照合して判定します。[Autodesk の `MDataBlock` API](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_data_block.html)

充填済み ON の経路を調べる診断 DLL では、通常評価コンテキストの `postEvaluation(kEvaluatedDirectly)` で clean と判定された入力を `inputValue()` で読み、現行の描画取得値と比較しました。2起動の114,400件すべてで行列が一致し、この追加取得中に `setInternalValue()` の呼び出し、`postEvaluation()` の再入、変形世代の変化はいずれも0件でした。その後の通常描画の読み取りでは、先の診断と同じ114,400件の入力通知を観測しました。

全1,000個が変形する ON 条件の順再生・逆再生・スクラブでは、追加した `forceCache()` から行列の変換までの区間の合計が0.56〜0.59 ms、同じ診断で現行のプラグから値を取得した区間の合計が2.87〜3.57 ms／実描画でした。診断を含む個別区間の合計であり、値を評価側から描画に渡した場合の再生全体の所要時間は別途計測します。

診断 DLL・ソースと計測記録は `build/fixed_cube/matrix_arrival/`（Git 管理外）の `native/`、`post_input/`、`harness/summary_arr1_arr2.json`、`harness/summary_arr1_db_arr2_db.json`、`harness/summary_arr1_input_arr2_input.json` に保存しました。

##### 評価時に取得した行列を描画に渡す試作

最初の試作では、行列を受け取った直後の世代・時刻と、その後の `postEvaluation(kEvaluatedIndirectly)` の世代・時刻が対応する場合に値を保持します。描画では時刻と世代を照合し、その描画の行列更新に限って再利用します。条件が揃わない場合は現行の処理で行列を取得します。通常の取得も実行した照合版では、順再生・逆再生・スクラブの OFF で57,200件すべてが一致しました。同じ時刻での入力編集と接続変更も Parallel と DG 評価で確認しました。

照合を外した試作版で Maya 2025 GUI の373件の判定を通過し、配布版の静止画125枚、再生画像53枚、静止参照6枚、画面選択58件と一致しました。記録は `harness/shadow_summary.json` と `harness/reuse_gate_summary.json` にあります。

追加の試作では、`postEvaluation(kEvaluatedDirectly)` で取得できた行列も、取得中に時刻と世代が維持された場合に同じ経路へ渡します。照合版では OFF の57,200件と充填済み ON の53,900件が現行の入力取得値と一致しました。ON の照合件数は、順再生・逆再生・スクラブそれぞれで通常更新の1描画分だけ、対象となる入力取得の総数を下回りました。照合用に行った現行のプラグ取得では、ON の照合対象すべてで `setInternalValue()` が1回呼ばれて世代が1つ進みました。試作は先に取得した行列を使う場合、このプラグ取得を省きます。同一時刻での接続・値の編集に加え、`multMatrix` と `composeMatrix` を含む入力への接続変更で、Parallel と DG の両方の境界と描画を照合しました。

追加試作の診断なし DLL も Maya 2025 GUI の373件の判定を通過し、同じ配布版参照の画像・画面選択すべてと一致しました。ソースと DLL ハッシュは `reuse_native/` と `reuse_direct_native/`、追加試作の機能検証は `harness/shadow_direct_summary.json` と `harness/reuse_direct_gate_summary.json` に保存しました。

#### 行列を事前に取得する試作の速度比較

Maya 2025.3.3／OpenGL で、現行と同じ描画処理の対照版と、OFF／ON の両方で評価時に得た行列を使う追加試作を、同じ Release ビルド設定で作成しました。対照 → 試作 → 試作 → 対照の順で独立起動し、2巡目は条件順も反転しました。各条件5試行の中央値です。左／右は1巡目／2巡目を示します。再生は ms／実描画（71描画）、ドラッグは ms／マウス移動（72移動・72描画）です。ON の充填範囲、代表フレームの画像、ドラッグの軌跡と移動量を照合しました。

| 条件 | 対照版 | 追加試作 | 差（追加試作 − 対照版） |
| --- | ---: | ---: | ---: |
| 共通親固定・変形入力0個・OFF | 2.33／2.46 | 2.31／2.35 | −0.01／−0.11 |
| 共通親固定・変形入力0個・充填済み ON | 2.37／2.45 | 2.49／2.44 | +0.12／0.00 |
| 共通親移動・100個変形・OFF | 6.71／7.02 | 6.51／6.49 | −0.20／−0.53 |
| 共通親移動・100個変形・充填済み ON | 7.02／7.54 | 7.01／6.55 | −0.02／−0.99 |
| 共通親移動・1,000個変形・OFF | 13.00／13.20 | 11.78／11.28 | −1.22／−1.93 |
| 共通親移動・1,000個変形・充填済み ON | 13.53／13.31 | 10.14／9.89 | −3.39／−3.42 |
| 単体ドラッグ（変形入力は固定） | 4.27／4.40 | 4.57／4.54 | +0.30／+0.14 |
| 共通親ドラッグ（変形入力は固定） | 7.32／8.21 | 7.52／7.35 | +0.21／−0.86 |

全1,000個が変形する再生は、両組で OFF が約9〜15%、充填済み ON が約25〜26%短くなりました。100個変形の充填済み ON は起動順で短縮幅が変わりました。単体ドラッグは両組で0.14〜0.30 ms長く、共通親ドラッグは差の向きが反転しました。計時は各 Cube の接続元を別々の `transform.matrix` にした構成です。採用時の確認項目として、変形再生を停止した直後のドラッグと、複数種類の接続元を含むリグでの再生を残します。

各試行、DLL、集計は `build/fixed_cube/matrix_arrival/direct_timing/`（Git 管理外）の `runs/` と `summary_a1_p1_p2_a2.json` に保存しました。

#### 通常の単体ドラッグと変形再生停止直後の再計測

Maya 2025.3.3／OpenGL で、前節の診断なし対照 DLL と試作 DLL を独立起動して比較しました。1,000個の各 Cube に別々の `transform.matrix` を接続し、共通親と変形入力をすべて固定した通常条件と、共通親と1,000個すべての変形入力を動かした再生直後を測りました。後者はキャッシュ OFF と、対象フレームの充填を確認した ON で行いました。

停止位置での選択、Move ツール、ハンドルの座標は再生前に準備しました。フレーム2〜72の実描画を経て再生範囲の末尾で自動停止した直後、Qt のマウス押下、72回の移動、リリースを送ります。押下と第1移動の計時には各イベントの送信から最初の描画後コールバックまでを使いました。停止前後の描画の順序、72移動それぞれの実描画、移動量と軌跡を記録し、計時とは別の試行でドラッグ前、第1移動後、リリース後の画像を照合しました。

対照 → 対照 → 試作 → 試作 → 対照 → 対照の順で独立起動し、後半は操作条件とキャッシュ条件の順序を反転しました。各起動は1条件7試行です。全84回の再生後の操作で、停止通知から0.04〜1.09 msで押下し、その間の追加描画は0回でした。同じ条件の代表画像と実際の移動量・操作軌跡は全起動で一致しました。

表の左／右は2つの起動順による各7試行の中央値の差です。再起動差は同じ対照 DLL を続けて起動した際の後 − 前です。移動の平均は ms／移動、それ以外はイベントから描画後コールバックまでの ms です。

| 条件 | 試作 − 対照 | 対照の再起動差 |
| --- | ---: | ---: |
| 通常の単体ドラッグ・全72移動の平均 | −0.29／−0.53 | +0.41／−0.23 |
| 停止直後 OFF・押下 | +0.98／−1.14 | −1.13／+0.38 |
| 停止直後 OFF・第1移動 | +3.47／+3.41 | +0.01／+0.62 |
| 停止直後 OFF・第2移動 | +3.31／+3.09 | −0.12／+0.56 |
| 停止直後 OFF・第3移動 | +0.44／−0.32 | −0.53／−0.03 |
| 停止直後 OFF・第4〜72移動の平均 | −0.11／−0.50 | +0.18／+0.60 |
| 停止直後 ON・押下 | −2.35／−3.89 | −0.55／−0.94 |
| 停止直後 ON・第1移動 | +3.43／+1.73 | −0.39／−0.94 |
| 停止直後 ON・第2移動 | +3.44／+2.95 | +0.05／−0.32 |
| 停止直後 ON・第3移動 | +2.35／+1.11 | +0.08／−0.74 |
| 停止直後 ON・第4〜72移動の平均 | −0.12／−0.05 | +0.14／+0.01 |

通常の単体ドラッグで前節に見られた遅れは再現しませんでした。停止直後は OFF で第1〜2移動、充填済み ON で第1〜3移動まで遅れが再現しました。ON では押下から描画までが短くなり、再生停止通知から第1移動の描画までをまとめた所要時間の差は +0.70／−1.01 ms でした。OFF の同区間は +5.30／+1.43 ms でした。

各試行と集計は `build/fixed_cube/matrix_arrival/drag_followup/`（Git 管理外）の `runs/` と `summary_a1_control_a1_p1_p2_a2_a2_control.json` に保存しました。

同じ操作を診断用の対照・試作 DLL で各2試行行い、押下と第1〜4移動を個別に計数しました。下表は1描画当たりのプラグからの変形行列取得／通常の描画状態取得の件数です。4条件の全試行で表の件数は一致しました。どちらの版も押下での `setMatrix()` は0件、各移動では動かした Cube の1件でした。

| 操作 | 対照 OFF | 試作 OFF | 対照 ON | 試作 ON |
| --- | ---: | ---: | ---: | ---: |
| 押下 | 0／1,000 | 0／1,000 | 1,000／1,000 | 0／1,000 |
| 第1移動 | 0／0 | 1,000／1,000 | 0／1,000 | 1,000／1,000 |
| 第2移動 | 0／0 | 0／1,000 | 0／0 | 1,000／999 |
| 第3移動 | 0／0 | 0／0 | 0／0 | 0／1,000 |
| 第4移動 | 0／0 | 0／0 | 0／0 | 0／0 |

試作は押下で、評価時に取得した全1,000個の行列を参照し、合成行列が適用済みの値と同じことを確認しました。この経路では、通常の描画用行列キャッシュに現在の世代を反映しません。次の移動で全件のプラグ取得と描画状態の確認が走りました。充填済み ON ではそのプラグ取得中に全1,000個で `setInternalValue()` が呼ばれて世代が進み、第2移動でも行列を取り直しました。次の試作では、停止直後に取得済み行列と描画用キャッシュを同期できる条件を確認します。

診断 DLL のソースとハッシュ、および押下からリリースまでの計数は `build/fixed_cube/matrix_arrival/drag_followup/profile/`（Git 管理外）の `native/`、`runs/`、`summary_diag_control_diag_trial.json` に保存しました。

#### 停止直後に評価済みの行列を描画キャッシュへ引き継ぐ試作

前節の試作を基に、評価時に取得済みのローカル行列と親行列の積が、描画項目へ適用済みの行列と一致する場合を扱いました。通常評価コンテキストと時刻、変形・形状の世代、DAG、表示、描画項目が一致した場合に、そのローカル行列と親行列を描画用キャッシュへ保存します。後続の描画でも保存した時刻を照合し、時刻・世代・描画状態が変わった場合は現在の状態を確認します。合成行列が変わる場合は、前節と同じくその描画の行列更新に使います。

前節と同じ1,000個が変形する再生と停止直後のドラッグを診断版で OFF／ON 各2試行行いました。新しい試作では、両方の条件の押下で全1,000件が上記の再利用条件を満たしました。押下から第4移動まで、通常のプラグ入力取得と描画状態の全項目取得は各0件でした。各移動で描画項目に行列を渡す `setMatrix()` は、動かした Cube の1件です。前節の試作が第1移動で行った全1,000件のプラグ入力取得、充填済み ON の第2移動の全1,000件の再取得も省けました。操作の画像・移動量・軌跡は対照および前節の試作と一致しました。

診断を外した Maya 2025 用 DLL で、373件の GUI 判定を通過しました。前節の試作と静止画125枚、再生画像53枚、静止参照6枚、画面選択58件が一致しました。ステップ補間中に親の X スケールをゼロで保持してから戻すシーンを追加し、順方向・逆方向への時刻移動を含む22枚の画像も照合しました。前節の試作との比較とキャッシュ OFF／ON の比較で、対応する画像はすべて一致しました。

診断を外した前節の試作と今回の試作を、前節の試作 → 今回の試作 → 今回の試作 → 前節の試作の順で独立起動しました。後半の2起動では条件順も反転しました。ドラッグは1条件7試行で、軌跡・移動量・描画画像を照合しました。差は今回の試作 − 前節の試作で、左／右は各組の中央値の差です。

| 操作から描画後コールバックまで | キャッシュ OFF | 充填済み ON |
| --- | ---: | ---: |
| 押下 | −1.01／−0.70 ms | −1.42／−1.23 ms |
| 第1移動 | −3.24／−3.41 ms | −4.76／−4.67 ms |
| 第2移動 | −2.45／−2.10 ms | −3.48／−3.20 ms |
| 第3移動 | +0.26／−0.13 ms | −2.06／−2.19 ms |
| 停止通知から第1移動の描画まで | −3.89／−4.44 ms | −5.35／−5.63 ms |

停止直後の短縮は、前節でプラグ取得と描画状態の確認が増えていた移動で観測されました。通常の単体ドラッグ全72移動の平均は +0.01／+0.71 ms／移動でした。

同じ起動順で、再生を独立した4起動で測定しました。各起動は1条件5試行、各試行71実描画で、充填済みキャッシュの範囲と代表フレームの画像を照合しました。下表の差は今回の試作 − 前節の試作で、単位は ms／実描画です。

| 再生条件 | キャッシュ OFF | 充填済み ON |
| --- | ---: | ---: |
| 共通親と変形入力が固定 | +0.12／−0.38 | −0.02／+0.29 |
| 共通親と100個の変形入力が移動 | +0.19／+0.34 | +0.07／+0.55 |
| 共通親と1,000個の変形入力が移動 | −0.18／−0.37 | +0.22／+0.67 |

全1,000個が変形する OFF は両組で短くなり、充填済み ON は両組で長くなりました。100個変形では OFF／ON とも両組で長くなりました。これらは停止後の取得回数を計数した診断とは別の実測で、再生中の差が生じた区間は未特定です。

通常の単体ドラッグだけを、さらに同じ2組の起動順で各7試行計測しました。全72移動の平均の差は −0.39／−0.16 ms／移動で、再生停止直後の操作を含む比較での +0.71 ms／移動は再現しませんでした。

ソースと DLL ハッシュ、各試行、集計を `build/fixed_cube/matrix_arrival/settle/`（Git 管理外）に保存しました。診断の計数は `profile/summary.json`、GUI の照合は `edge_summary.json`、時刻計測の集計は `drag/`、`playback/`、`ordinary/` の各 `summary_b1_c1_c2_b2.json` です。

#### 配布版と時刻付き試作の直接比較

Maya 2025.3.3／OpenGL／Parallel で、配布先の `bdUtilNodes.mll` と前節の時刻付き試作を比較しました。1,000個の `bdShpL_DeformableCube` にそれぞれ別の `transform.matrix` を接続し、共通親と接続元のアニメーションを切り替えました。配布版 → 試作 → 試作 → 配布版の順で独立起動し、後半は各起動の条件順も反転しました。計測には診断を無効にした DLL を使いました。

##### 変形中の再生

各起動で1条件5試行、各試行はフレーム2〜72の71実描画です。キャッシュ ON は計測の前後で対象範囲の充填を確認しました。代表フレーム2、36、72の RGBA は、同じ条件の全起動とキャッシュ OFF／ON で一致しました。表の左／右は起動順を入れ替えた各組の中央値で、単位は ms／実描画です。

| 再生条件 | キャッシュ | 配布版 | 試作 | 試作 − 配布版 |
| --- | --- | ---: | ---: | ---: |
| 共通親と全変形入力が固定 | OFF | 2.45／2.37 | 2.82／2.32 | +0.37／−0.06 |
| 共通親と全変形入力が固定 | 充填済み ON | 2.43／2.44 | 2.59／2.48 | +0.16／+0.05 |
| 共通親と100個の変形入力が移動 | OFF | 6.86／6.84 | 6.43／6.27 | −0.43／−0.57 |
| 共通親と100個の変形入力が移動 | 充填済み ON | 7.81／6.91 | 7.01／6.66 | −0.80／−0.25 |
| 共通親と1,000個の変形入力が移動 | OFF | 13.34／12.81 | 11.21／11.54 | −2.12／−1.27 |
| 共通親と1,000個の変形入力が移動 | 充填済み ON | 13.50／13.33 | 10.01／9.69 | −3.49／−3.64 |

共通親と変形入力が動く4条件はすべて、両組で試作のほうが短時間でした。1,000個変形での短縮率は OFF が約10〜16%、充填済み ON が約26〜27%です。親と全変形入力が固定の充填済み ON では試作が0.05〜0.16 ms長く、OFF は差の向きが反転しました。

##### 停止直後の初回ドラッグ

各起動でキャッシュ OFF／ON を各7試行計測しました。共通親と全1,000個の変形入力を動かして範囲末尾で自動停止し、全56試行で停止通知から押下までの追加描画は0回でした。代表画像、選択状態、移動軌跡と移動量は版間で一致しました。

| 操作 | キャッシュ | 配布版 | 試作 | 試作 − 配布版 |
| --- | --- | ---: | ---: | ---: |
| 停止通知から最初の移動の描画まで（ms） | OFF | 16.89／17.26 | 16.54／15.82 | −0.36／−1.44 |
| 停止通知から最初の移動の描画まで（ms） | 充填済み ON | 20.84／20.61 | 16.50／15.93 | −4.34／−4.68 |
| 最初の移動入力から描画まで（ms） | OFF | 3.12／3.27 | 3.39／3.27 | +0.27／+0.01 |
| 最初の移動入力から描画まで（ms） | 充填済み ON | 5.18／5.30 | 3.31／3.36 | −1.87／−1.95 |
| 第4〜72移動の平均（ms／移動） | OFF | 4.03／4.59 | 4.46／4.61 | +0.43／+0.02 |
| 第4〜72移動の平均（ms／移動） | 充填済み ON | 4.17／4.26 | 4.39／4.44 | +0.22／+0.18 |

押下から描画までは OFF で1.00〜1.14 ms、充填済み ON で2.49〜3.01 ms短くなり、停止から初動が見えるまでの時間は両モードで短縮しました。停止直後の同じドラッグを続けた第4〜72移動では、充填済み ON で平均時間が0.18〜0.22 ms／移動長くなりました。各移動の入力から描画後コールバックまでに限定しても、この区間は +0.21／+0.16 ms／移動でした。

##### 通常の単体ドラッグ

キャッシュ OFF で共通親と全変形入力を固定し、1起動につき7試行を行いました。72移動の平均は配布版の4.05／4.45 ms／移動に対し、試作は4.12／4.31 ms／移動でした。差は +0.07／−0.14 ms／移動で、同方向の遅れは再現しませんでした。

変形再生と停止直後の初動を優先する場合、時刻付き試作は採用候補です。固定状態のキャッシュ ON 再生と、キャッシュ ON の再生停止直後にドラッグを続けた区間には、小幅な増加が見られました。両方の DLL のハッシュ、計測条件、描画画像と試行の記録は `build/fixed_cube/matrix_arrival/settle/direct/`（Git 管理外）に保存しました。集計は `playback/` および `drag/` の `summary_a1_c1_c2_a2.json` です。

#### 評価済み行列の再利用を配布版へ導入

時刻付き試作の行列取得と描画キャッシュの更新を `bdUtilNodes` の `bdShpL_DeformableCube` に取り込みました。評価時に取得した行列は、通常評価コンテキストで時刻と世代が一致する場合に描画へ渡します。描画済みの合成行列と一致する場合は、ローカル行列を時刻付きで描画用キャッシュへ引き継ぎます。取得または照合の条件を満たせない場合は、通常のプラグ読み取りを使います。

Maya 2025 の新しい配布 DLL で373件の GUI 判定を通過しました。取り込み前の配布 DLL と採用した試作の両方に対し、静止画125枚、再生画像53枚、参照画像6枚、画面選択58件が一致しました。ステップ補間と親のゼロスケールを含む22枚も、キャッシュ OFF／ON それぞれで試作の画像と一致しました。

Maya 2025.3.3／OpenGL／Parallel で、配布 DLL の取り込み前 → 取り込み後 → 取り込み後 → 取り込み前の順に独立起動して再計測しました。各 Cube に別々の `transform.matrix` をつなぎ、再生は各5試行、1試行71実描画です。表の左／右は起動順を入れ替えた各組の中央値で、単位は ms／実描画です。

| 再生条件 | キャッシュ | 取り込み前 | 取り込み後 | 差 |
| --- | --- | ---: | ---: | ---: |
| 共通親と全変形入力が固定 | OFF | 2.47／2.40 | 2.64／2.25 | +0.17／−0.16 |
| 共通親と全変形入力が固定 | 充填済み ON | 2.14／2.37 | 2.70／2.33 | +0.56／−0.04 |
| 共通親と100個の変形入力が移動 | OFF | 6.47／6.78 | 6.37／6.34 | −0.09／−0.44 |
| 共通親と100個の変形入力が移動 | 充填済み ON | 7.33／6.97 | 6.76／6.61 | −0.57／−0.36 |
| 共通親と1,000個の変形入力が移動 | OFF | 12.49／12.99 | 11.05／11.22 | −1.43／−1.77 |
| 共通親と1,000個の変形入力が移動 | 充填済み ON | 12.61／12.56 | 9.97／9.62 | −2.64／−2.94 |

共通親と変形入力が動く4条件は両組で短縮し、1,000個変形では OFF で約11〜14%、充填済み ON で約21〜23%短縮しました。共通親と全変形入力が固定の再生は、両モードで起動順によって差の向きが変わりました。代表フレームの画像は取り込み前後とキャッシュ OFF／ON で一致しました。

ドラッグも同じ起動順で各7試行を計測しました。停止直後の条件では共通親と全1,000個の変形入力を動かして範囲末尾で自動停止し、停止通知から押下までの追加描画が0回であることを全56試行で確認しました。通常の単体ドラッグは共通親・全変形入力を固定したキャッシュ OFF です。取り込み前後で代表画像、操作軌跡と移動量が一致しました。

| 操作 | キャッシュ | 取り込み前 | 取り込み後 | 差 |
| --- | --- | ---: | ---: | ---: |
| 停止通知から最初の移動の描画まで（ms） | OFF | 17.92／17.05 | 15.48／16.16 | −2.43／−0.89 |
| 停止通知から最初の移動の描画まで（ms） | 充填済み ON | 21.33／20.69 | 15.61／16.64 | −5.73／−4.05 |
| 最初の移動入力から描画まで（ms） | OFF | 3.14／3.05 | 3.17／3.27 | +0.02／+0.22 |
| 最初の移動入力から描画まで（ms） | 充填済み ON | 5.23／5.22 | 3.34／3.48 | −1.89／−1.74 |
| 停止後の第4〜72移動の平均（ms／移動） | OFF | 4.40／4.16 | 4.21／4.49 | −0.19／+0.33 |
| 停止後の第4〜72移動の平均（ms／移動） | 充填済み ON | 4.15／4.16 | 4.30／4.42 | +0.15／+0.26 |
| 通常の単体ドラッグの平均（ms／移動） | OFF | 3.95／4.03 | 4.09／4.03 | +0.14／−0.01 |

停止から最初の移動が描画されるまでの短縮は、配布版でも両モードで確認できました。充填済み ON の停止後の第4〜72移動には、試作と同様に平均時間の小幅な増加がありました。通常の単体ドラッグでは差の向きが変わりました。

Maya 2025・2026・2027 用の Release DLL を更新し、`scripts/verify.cmd -IncludeNative` が通過しました。Maya 2025 の GUI の集計は `build/fixed_cube/matrix_arrival/settle/adoption/summary_packaged.json`、速度計測は同じディレクトリの `timing/playback/` と `timing/drag/` にある各 `summary_a1_c1_c2_a2.json` です。

#### 評価済み行列の再利用を取り込んだ後の処理内訳

Maya 2025.3.3／OpenGL／Parallel で、`fc00dfe8` の配布 DLL と同じソースから診断用 DLL を作成しました。10枝×100個の Cube にそれぞれ別の `transform.matrix` を接続しました。共通親も変形入力も固定、共通親だけ移動、共通親と100個の変形入力が移動、共通親と1,000個の変形入力が移動の4条件を、キャッシュ OFF と充填済み ON で測りました。

配布版 → 診断版 → 診断版 → 配布版の順で独立起動し、後半の2起動では条件順を反転しました。配布版は1条件5試行、診断版は3試行で、1試行71実描画です。同じ条件の代表3フレームの画像は、キャッシュ OFF／ON と全起動で一致しました。配布版の実時間と診断版の区間時間は別起動で取得しています。診断区間はワーカースレッド間および親子の計時区間で重なり、合計から再生全体の内訳を差し引くことはできません。空の計時区間には約16〜21 nsかかりました。

| 再生条件 | 配布版 OFF（ms／実描画） | 配布版 ON（ms／実描画） | 親行列取得／表示ステータス確認／`setMatrix()`（回／実描画） |
| --- | ---: | ---: | ---: |
| 共通親と全変形入力を固定 | 2.76／2.83 | 3.73／2.69 | 1,000／1,000／0 |
| 共通親だけ移動 | 6.54／6.04 | 7.29／6.53 | 1,000／1,000／1,000 |
| 共通親と100個の変形入力が移動 | 7.17／6.65 | 7.00／6.94 | 1,100／1,100／1,000 |
| 共通親と1,000個の変形入力が移動 | 12.02／12.00 | 12.85／11.10 | 2,000／2,000／1,000 |

配布版の左／右は条件順を反転した起動ごとの中央値です。100個から1,000個へ変形を増やすと OFF で4.85／5.35 ms、ON で5.85／4.16 ms／実描画長くなりました。全変形 ON の絶対値は今回の同じ配布 DLL の2起動でも1.75 ms異なります。

配布版と同じ処理の診断では、全変形の `requiresUpdate()` に OFF で1.72〜1.84 ms、ON で1.68〜1.83 ms／実描画かかりました。`update()` は OFF で1.82〜2.05 ms、ON で1.86〜1.93 ms／実描画でした。`setMatrix()` は両モードを通じて0.75〜0.91 msで、共通親に追従する全件で実行されました。変形個数に従って増えたのは、`update()` に入ってからの親行列と表示ステータスの再取得です。全変形の場合、時刻・世代・表示と親行列を照合する `transientStillCurrent()` は1,000回で、OFF 約0.44 ms、ON 約0.42〜0.46 ms／実描画でした。追加の親行列取得約0.10〜0.11 msはこの区間に含まれます。

全変形では通常のプラグ取得と描画状態一式の再取得が0回で、評価済み行列の照合と取得は全1,000件が成功し、合計約0.15〜0.17 msでした。評価時の準備は、OFF の `setInternalValue()` が受け取った行列を保持する区間で0.67〜0.69 ms、ON の clean な入力取得区間で0.48〜0.60 msでした。これらは各スレッドの区間時間の合計です。

##### 停止後のドラッグにおける時刻照合

全変形再生を停止してから単体ドラッグする診断を、キャッシュの順を反転した2起動で各条件2試行行いました。代表画像、操作軌跡、移動量、描画回数は配布版の記録と一致し、停止通知から押下までと、診断コマンド実行中の追加描画は全試行で0回でした。

押下で評価済みの1,000件すべてが描画用キャッシュに引き継がれました。キャッシュ OFF／ON とも、第1〜3移動の各実描画と第4〜72移動の平均で、1実描画あたり入口1,000回、後段1,000回の現在時刻取得がありました。後段の1,000回は各 Cube の同じ `requiresUpdate()` 内での2回目の取得でした。

第4〜72移動の後段の照合全体は、両モードとも診断区間の中央値で約0.084 ms／実描画でした。内側の `MAnimControl::currentTime()` 区間は約0.021 msで、1回あたり約21 nsです。ドラッグ診断でも空スコープは1回約17 nsで、短い API 区間の計時は診断の影響を受けます。配布版の ON だけに見られた0.15〜0.26 ms／移動の差のうち、この照合に起因する時間は今回の診断からは確定できません。

再生側は変形する Cube にだけ生じる `requiresUpdate()` と `update()` の間の再照合を次の比較対象とします。2つのコールバックの間で親行列や表示状態が変わる条件を照合用の試作で確認し、再確認を減らせる範囲を調べます。停止後の時刻照合は、単一の `requiresUpdate()` 内で照合結果を共有した場合に限り比較できます。

ソース照合・診断 DLL の記録を `build/fixed_cube/current_cost/native/`、再生の集計を `playback/summary_a1_p1_p2_a2.json`、ドラッグを `drag/summary_current_drag1_current_drag2.json` に保存しました（いずれも Git 管理外）。

#### 行列の準備から適用までに変わる状態の観測

`fc00dfe8` の描画処理を使う Maya 2025.3.3／OpenGL 向けの診断用 DLL で調べました。行列のみを更新する分岐で `requiresUpdate()` が値を準備した時点と、対応する `update()` がそれを使う際の状態を比較しました。変形世代と形状世代、時刻と評価コンテキスト、DAG、親のワールド行列、表示ステータス・表示世代・表示スタイル、描画項目を記録しました。既存の適用判定は維持し、接続行列の経路で通常行う再取得と、親だけが動く経路などでの診断用の追加取得を別々に計数しました。

##### 1,000個の Cube を使った再生

前節と同じ4条件を、条件順を反転した2起動でキャッシュ OFF／充填済み ON 各3試行、各71実描画で計測しました。DAG 構成、対象キャッシュの充填、代表フレーム2、36、72の画像は配布版の記録と一致しました。両モードの合計は下表のとおりです。

| 再生条件 | 接続行列をその描画で使う適用数 | 保持したローカル行列などを使う適用数 | 親行列または表示ステータスの差 |
| --- | ---: | ---: | ---: |
| 共通親と全変形入力を固定 | 0 | 0 | 計測対象なし |
| 共通親だけ移動 | 0 | 852,000 | 0 |
| 共通親と100個の変形入力が移動 | 85,200 | 766,800 | 0 |
| 共通親と1,000個の変形入力が移動 | 852,000 | 0 | 0 |

準備した全2,556,000件を対応する `update()` で照合して適用しました。接続行列の経路937,200件では本来の親行列・表示ステータスの再取得を観測し、残り1,618,800件は同じ DAG パスが有効なときに診断で両方を追加取得しました。時刻、世代、描画項目の差、再照合による通常経路への復帰、後続の更新判定による準備内容の上書きも各0件でした。

##### 選択・表示・階層を変更した場合

3個の Cube を使い、選択の追加と順序変更、色と表示レイヤー、2ビューポートと Isolate Select、親の付け替えと Undo／Redo を、入力行列の編集とも組み合わせました。配布版と診断版の414件の判定が通過し、静止画148枚、再生画像53枚、参照画像6枚、画面選択58件、別途の時刻移動画像22枚が一致しました。各版の計測対象33区間で、306件の実描画を記録しました。

行列のみを準備して適用した167件のうち、58件は接続行列をその描画で使う経路、109件は保持していたローカル行列で親に追従するなどの経路でした。OFF／ON の順再生、ON の逆再生とスクラブ、同じ時刻での接続行列の編集で前者を観測しました。両経路の167件で親行列・表示ステータス・時刻を照合し、差は0件でした。選択順、色、表示レイヤー、Isolate Select、親の付け替えと Undo／Redo を変更した区間では、行列のみの更新を準備する前に通常の状態取得へ進みました。

Maya 2025 の公開 API は `requiresUpdate()` と `update()` の呼び出し順を定めています。両方のコールバックをまたいで状態を固定する記述は確認できませんでした。今回の観測を基に、再生時の親行列と表示ステータスの取得を適用直前に集約する案を比較対象にできます。時刻・世代・描画項目の確認と、状態に応じた通常更新を試作でも使い、表示・選択の一致と診断なしの実描画時間を確認する方針です。[Autodesk Maya 2025 MPxSubSceneOverride](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_px_sub_scene_override.html)

診断用ソースと DLL ハッシュは `build/fixed_cube/apply_gap/native/`、集計は `build/fixed_cube/apply_gap/` 以下の `playback/summary_p1_p2.json` と `interactions/summary_a1_retry2_p1.json` に保存しました（Git 管理外）。

#### 再生中の親行列と表示ステータスを適用直前に取得する試作

`fc00dfe8` を基に、再生中で変形入力が更新され、評価済みの接続行列を取得できた場合に限り、`requiresUpdate()` でローカル行列と時刻・世代を保持しました。`update()` で描画項目や世代を照合し、現在の親行列と表示ステータスを取得します。確認を通った場合はローカル行列と最新の親行列を合成し、条件が変わった場合は通常の状態取得に進みます。再生中かどうかは `MConditionMessage` の `playingBack` 通知を1つ登録して保持し、アンロード時に解除します。[Autodesk Maya 2025 MConditionMessage](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_condition_message.html)

Maya 2025.3.3／OpenGL の GUI 検証では、414件の判定、静止画148枚、再生画像53枚、参照画像6枚、画面選択58件、別途の時刻移動画像22枚が配布版と一致しました。さらに、別々の表示スタイルの2ビューポートで親・可視性・変形入力を同時に動かしました。キャッシュ OFF／充填済み ON の順再生・逆再生中に取得した両ビューの画像40枚が一致し、この構成を含む439件の判定が通過しました。

診断版では前節と同じ1,000個の再生シーンを使い、各条件3試行、各71実描画を計数しました。100個・1,000個変形のどちらも、変形した全件で親行列と表示ステータスを `update()` で各1回取得し、通常の状態取得への復帰は0件でした。各取得の合計は、100個変形で1,100→1,000回、1,000個変形で2,000→1,000回／実描画になりました。`setMatrix()` は共通親が動く条件で1,000回／実描画でした。

##### 診断を無効にした再生時間

配布版 → 試作 → 試作 → 配布版の順で独立起動し、後半は条件の順も反転しました。各条件5試行、各試行71実描画です。全起動で対象キャッシュの充填と代表3フレームの画像を照合しました。左／右は各組の中央値、単位は ms／実描画です。

| 再生条件 | キャッシュ | 配布版 | 試作 | 試作 − 配布版 |
| --- | --- | ---: | ---: | ---: |
| 共通親と変形入力を固定 | OFF | 2.52／2.51 | 2.44／2.75 | −0.08／+0.24 |
| 共通親と変形入力を固定 | 充填済み ON | 2.74／3.02 | 2.40／2.41 | −0.34／−0.61 |
| 共通親だけ移動 | OFF | 5.88／5.54 | 5.72／5.44 | −0.16／−0.10 |
| 共通親だけ移動 | 充填済み ON | 6.75／6.35 | 6.31／6.28 | −0.45／−0.07 |
| 共通親と100個の変形入力が移動 | OFF | 6.44／6.42 | 6.41／6.20 | −0.03／−0.22 |
| 共通親と100個の変形入力が移動 | 充填済み ON | 6.74／6.78 | 6.60／6.61 | −0.14／−0.18 |
| 共通親と1,000個の変形入力が移動 | OFF | 11.15／11.63 | 10.90／10.87 | −0.25／−0.76 |
| 共通親と1,000個の変形入力が移動 | 充填済み ON | 10.44／9.95 | 9.94／9.28 | −0.50／−0.67 |

1,000個変形は、起動順を反転した両組で OFF／ON とも短縮しました。試作の取得経路を使わない共通親だけの移動でも差が出ています。この移動を基準に全変形条件の追加時間を比較すると、試作 − 配布版は OFF −0.09／−0.66 ms、ON −0.06／−0.60 msでした。

##### 再生停止後と通常の単体ドラッグ

再生と別に同じ起動順で、各条件7試行を比較しました。1,000個変形の再生から範囲末尾で自動停止し、停止通知から押下までの追加描画が0回であることを、OFF／ON の計56試行で確認しました。通常の単体ドラッグでは共通親と変形入力を固定しました。両版で代表画像、軌跡、移動量が一致しました。

| 操作 | キャッシュ | 試作 − 配布版 |
| --- | --- | ---: |
| 停止通知から最初の移動の描画まで（ms） | OFF | −1.12／−0.03 |
| 停止通知から最初の移動の描画まで（ms） | 充填済み ON | +0.09／+0.76 |
| 停止後の第4〜72移動の平均（ms／移動） | OFF | +0.08／−0.06 |
| 停止後の第4〜72移動の平均（ms／移動） | 充填済み ON | −0.07／+0.41 |
| 通常の単体ドラッグの平均（ms／移動） | OFF | +0.56／+0.04 |

通常の単体ドラッグだけを独立した4起動で再計測しました。各7試行の72移動平均で、試作は +0.33／+0.07 ms／移動でした。通常操作はどちらの計測でも両組で試作が長く、差の大きさは起動順で変動しました。充填済み ON の停止から最初の移動が描画されるまでの時間も、両組で小幅に増えました。取得回数の削減と変形再生の短縮は確認でき、試作の採用判断は操作時の増加を切り分けてからとします。

検証には `verify.cmd` と `git diff --check` も通過しました。試作ソースと DLL ハッシュを `build/fixed_cube/deferred_apply/native/`、画像照合の集計を `gui/standard/summary_c1.json` と `gui/dual/summary_c1.json`、診断の計数を `profile/summary_p1.json` に保存しました。実描画の計時は `timing/playback/`、`timing/drag/`、`timing/ordinary/` 以下の `summary_a1_c1_c2_a2.json` です（いずれも Git 管理外）。

#### 通常ドラッグの再現性と描画処理の内訳

共通親と変形入力を固定し、キャッシュ OFF で1,000個のうち1個をドラッグしました。配布版 → 配布版 → 試作 → 試作 → 配布版 → 配布版の順で Maya 2025.3.3 を独立起動し、4回の配布版の起動には同一の DLL を使いました。各起動の7試行で72移動、72実描画を確認し、軌跡、移動量、代表画像も照合しました。表の左／右は比較した2組の中央値の差です。同一 DLL の再起動差は、各組で後の起動 − 前の起動です。

| 計時対象 | 試作 − 配布版 | 同一配布版の再起動差 |
| --- | ---: | ---: |
| 押下から描画後通知（ms） | −0.865／−0.047 | −0.284／−1.060 |
| 全72移動の平均（ms／移動） | −0.254／+0.476 | −0.497／−0.324 |
| 第4〜72移動の入力から描画後通知（ms／移動） | −0.251／+0.346 | −0.344／−0.253 |
| 同区間の描画後通知からイベント処理終了（ms／移動） | −0.031／+0.146 | −0.147／−0.055 |
| 同区間のイベント処理終了から次の入力まで（ms／移動） | 0.000／+0.001 | −0.001／−0.001 |

通常ドラッグの差は、起動順を反転した比較で向きが変わりました。同じ配布 DLL の再起動でも、前節の試作比較と同程度の差が見られました。時間差の多くは移動イベントから描画後通知までの区間にありましたが、区間内で変動した処理はこの計時では分かりません。

現行ソースと試作ソースを同じビルド設定で診断用にビルドしました。現行 → 試作 → 試作 → 現行と独立起動し、各3試行で押下、第1〜3移動、第4〜72移動、リリースを計数しました。選択された Cube、軌跡、移動量、代表画像が配布版と一致しました。描画前後の通知が対応したことを確認し、診断コマンドが実描画を追加したケースは0件でした。

両版とも、親のワールド行列取得と表示ステータス確認は1,000回／実描画でした。押下では `setMatrix()` が0回、最初の3移動では各1回、第4〜72移動の平均では約0.94回／実描画でした。形状変形を検出した回数、試作の再生判定へ進んだ回数、通常の描画状態の取得はいずれも0回でした。

第4〜72移動の診断区間では、`requiresUpdate()` の合計時間の試作 − 現行は −0.085／−0.034 ms／実描画、`update()` は +0.001／+0.001 ms でした。入力から描画前通知までは −0.203／−0.063 ms、描画前から描画後通知までは −0.119／+0.010 ms、描画後からイベント処理終了までは −0.104／−0.021 ms でした。これらは診断版の値です。描画通知の区間には Maya の他の処理も含まれます。

現行ソースを試作と同じ描画ノードの登録コード、コンパイラ設定、Release 設定でビルドし、診断を外して再比較しました。現行 → 試作 → 試作 → 現行の順で各7試行を計測し、全72移動の平均は試作 − 現行で −0.135／−0.132 ms／移動でした。押下から描画後通知までは −0.324／+0.044 ms、第4〜72移動では入力から描画後通知までが −0.085／−0.141 ms／移動でした。通常ドラッグで一貫した遅れは再現せず、診断でも試作固有の処理回数の増加は確認しませんでした。

今回の通常ドラッグはキャッシュ OFF で計測しました。試作の採用判断には、前節で増加した充填済みキャッシュ ON の再生停止直後の応答も残ります。

計測は `build/fixed_cube/deferred_drag/` 以下に保存しました。配布版との計時は `timing/ordinary/summary_a1_control_a1_c1_c2_a2_a2_control.json`、診断は `profile/summary_a1_retry1_c1_retry1_c2_retry1_a2_retry1.json`、ビルド条件をそろえた比較は `matched/ordinary/summary_a1_c1_c2_a2.json` です（いずれも Git 管理外）。

#### キャッシュを充填した変形再生の停止直後にドラッグ

Maya 2025.3.3／OpenGL で、共通親と1,000個それぞれの `shapeDeformMatrix` 入力が動くシーンを使いました。同一の配布 DLL を2回、試作 DLL を2回、同じ配布 DLL をさらに2回、順に独立起動しました。停止後ドラッグはキャッシュ OFF／充填済み ON 各7試行／起動です。ON では各試行前に要求範囲の71フレームがキャッシュ済みであることを確認しました。全84試行でフレーム72まで描画して自動停止し、停止通知から押下までの追加描画は0回でした。出力画像、マウスの軌跡、コントローラーの移動量も各版で一致しました。

充填済み ON の結果です。各列の左／右は起動順を反転した2組の比較です。同一配布版は、各組で後の起動の中央値から前の起動の中央値を引きました。

| 計時区間 | 試作 − 配布版 | 同一配布版の再起動差 |
| --- | ---: | ---: |
| 停止通知から最初の移動の描画後通知（ms） | −0.395／+0.140 | +0.517／−0.153 |
| 停止通知から押下（ms） | −0.003／−0.003 | +0.000／+0.019 |
| 押下から描画後通知（ms） | −1.423／+0.347 | +1.815／−0.226 |
| 押下の描画後通知からイベント処理終了（ms） | +0.292／+0.238 | −0.162／+0.361 |
| 最初の移動入力から描画後通知（ms） | +0.279／−0.109 | +0.184／+0.038 |
| 第4〜72移動の平均（ms／移動） | +0.328／+0.119 | +0.169／+0.018 |
| フレーム2〜72の再生間隔の平均（ms／フレーム） | −0.453／−0.378 | +0.636／+0.167 |

停止から最初の移動が描画されるまでの中央値は、配布版で15.78〜17.59 ms、試作で16.07〜17.19 ms でした。前回は試作が両組で長くなりましたが、今回は差の向きが分かれました。両組の差の絶対値は、同一 DLL を再起動して観測した最大差0.517 ms に収まりました。再生間隔は両組で短く、両端を除いたフレーム10〜69でも −0.447／−0.415 ms／フレームでした。OFF の停止から最初の移動までは +6.024／−1.552 ms で、こちらも起動順を反転すると差の向きが変わりました。

押下の描画後通知からイベント処理が終わるまでの区間は、前回と今回のいずれも試作の中央値が長くなりました。今回の増加は主に Qt の `sendEvent()` が戻ってから `processEvents()` が終わるまでにあり、この部分の差は +0.171／+0.189 ms、同一配布版の再起動差は +0.004／+0.377 ms でした。充填済み ON を先に実施した後半3起動で、最初の試行は同区間に約19 ms かかりました。この試行は試作の1起動と配布版の2起動で発生し、各起動の中央値にも含めました。

##### 停止後の描画処理の計数

同じビルド条件の現行・試作の診断 DLL を、現行 → 試作 → 試作 → 現行と独立起動しました。OFF／充填済み ON 各3試行／起動で、両版の画像と移動量が配布版の記録に一致しました。押下、72移動、リリースの計1,776描画で描画前後の通知が対応し、全描画が `sendEvent()` の実行中に発生しました。

OFF／ON とも、押下で両版が全1,000個のローカル変形行列、親のワールド行列、表示ステータスを各1,000回取得しました。押下中の `setMatrix()` は0回でした。試作では再生中かどうかの確認が1,000回あり、充填済み ON でこの計測区間の合計は約0.018 ms でした。押下からリリースまで、試作の再生用経路による行列の準備・適用は0回でした。最初の移動では両版ともローカル変形行列の再取得は0回、親のワールド行列と表示ステータスの取得は各1,000回、`setMatrix()` は1回でした。

診断版の充填済み ON では、押下の描画後通知からイベント処理が終わるまでの試作差は −0.240／+0.472 ms でした。`requiresUpdate()` の合計時間は −0.040／−0.050 ms でした。通常計時で見えた押下直後の区間の増加は、Cube の描画更新回数の増加には対応していませんでした。キャッシュを充填した変形再生の短縮が再現し、停止直後の初回応答の差は同一 DLL の再起動と同程度でした。

通常計時は `build/fixed_cube/deferred_drag/timing/drag/summary_a1_control_a1_c1_c2_a2_a2_control.json`、イベント処理の区間別集計は `build/fixed_cube/deferred_stop_analysis/` の `evaluation.json` と `off.json`、診断は `build/fixed_cube/deferred_stop_profile/summary_a1_c1_c2_a2.json` に保存しました（Git 管理外）。

#### 再生時の取得をまとめる処理を配布版に取り込み

`bdShpL_DeformableCube` は、再生中に評価済みの接続行列がある場合、`requiresUpdate()` でそのローカル行列と時刻・世代を保持します。`update()` で親のワールド行列と表示ステータスを取得し、DAG・描画項目・評価状態が一致すれば適用します。同じ時刻が続く場合や前提が変わった場合は通常の更新を使います。再生状態の通知はプラグインの表示監視が所有し、アンロード時に解除します。

Maya 2025・2026・2027 用の Release DLL を更新し、`verify.cmd -IncludeNative -IncludeCubeResearch` が通過しました。Maya 2025 の配布 DLL で通常の414件と2ビューポート構成の439件の GUI 判定が通過しました。試作と静止画148枚、再生画像53枚、参照画像6枚、画面選択58件、時刻移動の22枚、2ビューポートでの再生画像40枚が一致し、プラグインのアンロード・再読み込み後の描画と選択も確認しました。

##### 配布版の変形再生時間

Maya 2025.3.3／OpenGL／Parallel で、旧配布版 → 新配布版 → 新配布版 → 旧配布版の順に独立起動しました。各条件5試行、各試行71実描画です。キャッシュの充填と代表画像を全起動で照合しました。左／右は起動順を反転した各組の中央値で、単位は ms／実描画です。

| 再生条件 | キャッシュ | 旧配布版 | 新配布版 | 新 − 旧 |
| --- | --- | ---: | ---: | ---: |
| 共通親と変形入力を固定 | OFF | 2.397／2.396 | 2.367／2.431 | −0.030／+0.035 |
| 共通親と変形入力を固定 | 充填済み ON | 2.256／2.688 | 2.441／2.883 | +0.184／+0.195 |
| 共通親だけ移動 | OFF | 5.591／5.368 | 5.626／5.576 | +0.035／+0.208 |
| 共通親だけ移動 | 充填済み ON | 6.768／6.129 | 6.518／6.258 | −0.250／+0.129 |
| 共通親と100個の変形入力が移動 | OFF | 6.454／6.298 | 6.588／6.424 | +0.135／+0.126 |
| 共通親と100個の変形入力が移動 | 充填済み ON | 6.591／6.552 | 6.695／6.737 | +0.104／+0.186 |
| 共通親と1,000個の変形入力が移動 | OFF | 11.223／11.183 | 11.106／11.085 | −0.117／−0.098 |
| 共通親と1,000個の変形入力が移動 | 充填済み ON | 10.225／9.683 | 10.236／9.708 | +0.011／+0.025 |

1,000個変形では OFF が両組で約1%短縮し、ON はほぼ同水準でした。共通親だけを動かす条件からの追加時間を比べても、OFF は −0.152／−0.307 ms、ON は +0.261／−0.104 ms でした。100個変形は両モードで小幅に長くなりました。試作で見えた1,000個変形 ON の短縮幅は、今回の配布版比較では再現しませんでした。旧配布 DLL 自体も、試作の比較時から同条件で0.219／0.269 ms 短くなっています。試作と配布版の Release オブジェクトを照合し、`requiresUpdate()`、`update()`、行列の準備・解決と評価済み行列の取得の命令列がリンカーの再配置前に一致することも確認しました。

##### 配布版の停止直後と通常の単体ドラッグ

同じ起動順でドラッグを各条件7試行計測しました。変形再生後の計測では1個を選択して Move マニピュレータを表示した状態で、共通親と1,000個の変形入力を動かしました。フレーム72で自動停止し、すべての停止試行で停止通知から押下までの追加描画は0回でした。各移動に実描画が1回あり、旧版と新版で画像・操作軌跡・移動量が一致しました。

| 計時区間 | キャッシュ | 旧配布版 | 新配布版 | 新 − 旧 |
| --- | --- | ---: | ---: | ---: |
| 停止通知から最初の移動の描画まで（ms） | OFF | 16.343／16.168 | 16.353／15.846 | +0.009／−0.322 |
| 停止通知から最初の移動の描画まで（ms） | 充填済み ON | 15.493／15.604 | 16.498／16.108 | +1.005／+0.504 |
| 最初の移動入力から描画まで（ms） | OFF | 3.370／3.340 | 3.251／3.177 | −0.118／−0.163 |
| 最初の移動入力から描画まで（ms） | 充填済み ON | 3.186／3.191 | 3.232／3.364 | +0.046／+0.173 |
| 停止後の第4〜72移動の平均（ms／移動） | OFF | 4.666／4.288 | 4.414／4.303 | −0.252／+0.015 |
| 停止後の第4〜72移動の平均（ms／移動） | 充填済み ON | 4.279／4.238 | 4.319／4.433 | +0.041／+0.196 |
| 通常の単体ドラッグの平均（ms／移動） | OFF | 4.075／4.087 | 4.105／4.117 | +0.030／+0.030 |

充填済み ON の停止直後は、押下から描画後通知までが +0.664／+0.150 ms、押下の描画後通知からイベント処理終了までが +0.232／−0.214 ms でした。押下後に増えた区間は、前節の試作比較と今回で同じ傾向にはなりませんでした。このドラッグ試行に含まれる、コントローラーを選択した状態での ON 再生は、フレーム2〜72の平均間隔が −0.386／−0.287 ms／フレームでした。

計測結果と DLL のハッシュを `build/fixed_cube/deferred_adoption/` に保存しました。GUI 照合は `gui/standard/summary_c1.json` と `gui/dual/summary_c1.json`、速度比較は `timing/playback/` と `timing/drag/` の `summary_a1_c1_c2_a2.json`、停止からの区間別集計は `timing/drag/stop_intervals_evaluation.json` と `stop_intervals_off.json` です（Git 管理外）。

#### 共通親の移動と一部変形が重なる再生を、選択状態別に比較

前節の旧配布版（`fc00dfe8`）と新配布版（`a04f7be3`）を Maya 2025.3.3／OpenGL／Parallel、GeForce GTX 1660 SUPER で再比較しました。共通親の下に10枝 × 100個の `bdShpL_DeformableCube` を置き、1,000個すべてに個別の行列入力を接続しました。共通親は全条件で移動し、動く変形入力を0、100、1,000個に切り替えました。Move ツールをワールド座標にそろえ、選択なしと先頭のコントローラー1個選択を比較しました。100個・1,000個変形のとき、この1個は変形する側です。

旧 → 新 → 新 → 旧の4起動で、後半は選択・キャッシュ・変形数の実施順も反転しました。各条件5試行、計240再生です。各試行でフレーム2〜72が順に1回ずつ描画され、計17,040描画を記録しました。ON では再生前に71フレームのキャッシュ充填を確認しました。代表3フレームの画像は計時の外で取得し、同じ選択状態で版間・起動間の一致と、選択を変えたときの表示の違いを確認しました。

表は新版 − 旧版（ms）。左／右は起動順の異なる2組における中央値の差で、負値は新版の短縮です。「再生全体」は開始・終了処理を含む `cmds.play()` の所要時間を71実描画で割った値、「描画間隔」は**同じ再生**のフレーム2〜72の描画後通知間の平均（70区間）です。

| 変形数 | キャッシュ | 再生全体・選択なし | 再生全体・1個選択 | 描画間隔・選択なし | 描画間隔・1個選択 |
| ---: | --- | ---: | ---: | ---: | ---: |
| 0 | OFF | −0.13／+0.16 | +0.08／−0.09 | −0.16／+0.16 | +0.04／−0.11 |
| 0 | 充填済み ON | +0.70／−0.04 | +0.04／−0.10 | +0.71／−0.03 | −0.07／−0.08 |
| 100 | OFF | +0.59／+0.29 | −0.18／−0.32 | +0.67／+0.26 | −0.19／−0.19 |
| 100 | 充填済み ON | +0.21／−0.27 | −0.24／−0.27 | +0.21／−0.21 | −0.41／−0.27 |
| 1,000 | OFF | −0.79／+0.18 | −0.59／−0.53 | −0.75／+0.20 | −0.28／−0.51 |
| 1,000 | 充填済み ON | −0.01／−0.26 | −0.91／−0.35 | −0.03／−0.25 | −0.92／−0.25 |

100個変形・選択なし・OFF では、前節で観測した再生全体の遅れが再現しました。フレーム2〜10の間隔差は +0.97／+0.62 ms、10〜69は +0.58／−0.02 ms で、再生中盤の遅れは一方の組だけに出ました。選択なし・ON の差は起動順で逆転しました。1個選択では100個変形の OFF／ON とも新版が両組で短くなり、再生全体と描画間隔の両方に表れました。

1,000個変形・1個選択・ON は、フレーム10〜69でも −1.00／−0.31 ms と短縮しました。前節の停止後ドラッグ用試行で見えた再生の短縮が、今回はドラッグを伴わない再生で再現しました。ただし、同じ起動内で1個選択と選択なしの描画間隔を引くと、旧版が +0.32／−0.72 ms、新版が −0.58／−0.72 ms でした。選択によって新版の改善幅が広がったかについては、2組の結果がそろいません。

実測値、各試行の描画時刻、キャッシュ・画像の照合記録は `build/fixed_cube/partial_selection/` に置いています。4起動の集計は `summary_a1_retry1_c1_retry1_c2_retry1_a2_retry1.json` です。最初の起動は計測スクリプトのハッシュ照合で開始前に終了し、照合値を訂正して全4起動を実施しました（Git 管理外）。

##### 同じ描画で、変形する100個と親移動だけの900個を計時

旧版・新版の処理を基にした診断 DLL を別途4回、旧 → 新 → 新 → 旧の順に起動しました。選択なし・Select ツールで、0／100／1,000個変形とキャッシュ OFF／充填済み ON を各3試行、計5,112描画記録しました。`requiresUpdate()` が選んだ経路を対応する `update()` に引き継いで分類し、各コールバックの件数・区間時間の合計が分類前と一致することを各試行で照合しました。100個変形の全試行で、両コールバックとも1描画につき変形側100件、親移動だけの側900件、他の経路0件でした。

| 100個変形時の処理 | キャッシュ | 旧診断版（ms／描画） | 新診断版（ms／描画） |
| --- | --- | ---: | ---: |
| 変形する100個 | OFF | 0.418／0.390 | 0.354／0.344 |
| 親移動だけの900個 | OFF | 3.060／2.897 | 2.930／2.862 |
| 変形する100個 | 充填済み ON | 0.334／0.332 | 0.322／0.315 |
| 親移動だけの900個 | 充填済み ON | 2.443／2.441 | 2.614／2.587 |

各値は、同じ試行で両コールバックにかかった時間をグループ内で足し、71実描画で割った後の3試行の中央値です。診断コードの負荷を含みます。独立した配布版の実時間とは直接差し引けません。

100個変形では両キャッシュモードとも、親ワールド行列と表示ステータスの取得は各1,100 → 1,000回／描画、描画項目への `setMatrix()` は両版とも1,000回でした。新版で変形行列を再生用に準備・解決したのは各100件で、900個の固定入力まで毎回読み直す挙動は観測されませんでした。両版とも通常の状態取得への復帰、静的形状の再構築、頂点バッファの更新は0件でした。

OFF のコールバック全体は両組で短縮しました（−0.195／−0.082 ms）。配布版の選択なし・OFF で再生全体が長くなった現象を、Cube の描画コールバックの回数増加や変形する100個の処理時間からは説明できません。充填済み ON では変形する100個は小幅に短縮し、親移動だけの900個にかかった時間は +0.172／+0.146 ms でした。0個変形・ON では親移動だけの1,000個が逆に −0.462／−0.167 ms で、親に追従する処理に共通した退行は確認できません。親だけの経路が占める割合は新版の混在条件で約89%です。共通親が動くため、これら900個にも最終行列を反映する必要があります。

旧・新診断版の経路別集計は `build/fixed_cube/partial_profile/summary_a1_c1_c2_a2.json` に保存しました（Git 管理外）。

##### 1個選択したときの更新件数

100個変形の新版診断 DLL で、配布版の速度計測と同じ Move ツール・選択対象・画面設定を使い、選択とキャッシュの順を反転して2回起動しました。各条件3試行、計24再生・1,704描画です。代表画像はそれぞれの選択状態で配布版と一致しました。選択を変えても、`requiresUpdate()` と `update()` の内訳はどちらも親移動だけ900件・変形100件で、親ワールド行列取得・表示ステータス確認・`setMatrix()` はそれぞれ1,000回／描画でした。通常更新への復帰は0件で、記録した全項目の1描画あたりの件数の中央値が両選択状態で一致しました。

同じ起動内で「1個選択 − 選択なし」を取ると、両コールバックの合計時間は OFF が +0.108／+0.548 ms、充填済み ON が −0.084／−0.499 ms でした。診断なしの新版の同じ選択差（フレーム2〜72の描画間隔）は OFF −1.43／−0.29 ms、ON −0.14／−0.25 ms です。選択で計測時間が変わっても、Cube が別の描画更新経路に切り替わった形跡はありません。OFF の差は診断あり・なしで向きが異なり、増減の原因や描画の外で生じた時間の大きさは未特定です。

次の切り分けは、再現性のある「100個変形・キャッシュ OFF」に絞れます。選択する DAG パスを固定して変形する100個のうち1本を別の入力と入れ替えれば、選択対象自身が変形する場合と親移動だけの場合を比較できます。同じ選択のまま Select／Move ツールも切り替え、配布版で差が残る組み合わせに限って Maya Profiler で DG 評価と VP2 の描画準備の区間を記録します。

選択を切り替えた診断の集計は `build/fixed_cube/partial_selected_profile/summary_c1_c2.json` に保存しました（Git 管理外）。

#### 選択する Cube 自身の変形と、Select／Move ツールの影響

Maya 2025.3.3、共通親移動、独立入力1,000本中100本が変形、キャッシュ OFF で前節と同じ配布 DLL を使いました。選択対象は常に最初の枝の `transform1` です。この Cube と別の枝の先頭の Cube の変形行列接続を入れ替え、選択対象のワールド位置と変形総数を保ったまま、「自身も変形」と「親移動だけに追従」を作りました。両方の位置で、実際の接続、変形行列、形状の境界とピボットを確認しました。各構成で Select／Move、選択なし／1個選択の4通りを測りました。

旧 → 現行 → 現行 → 旧の4起動で、後半は条件順も反転しました。8条件 × 5試行 × 4起動で160再生、各試行でフレーム2〜72が1回ずつ、合計11,360回描画されました。各条件の代表3フレームは版間で画素単位に一致しました。選択すると選択色が加わり、同じ選択で Select／Move を切り替えた画像は一致しました。ワールドピボットは順番を反転した後のフレーム72で最大約1兆分の1 cm の丸め差があり、起動間の照合には絶対許容差 `1e-9` cm を使いました。最初の起動は旧計測用の OFF／ON 両方を要求する条件で、計時前に終了しました。OFF 専用の計測入口に修正して全4起動を通しています。

表は**現行 − 旧版**の時間です。左／右は起動順を反転した2組の中央値の差で、単位は ms／実描画です。「対象」は1個選択する際の Cube を表し、選択なしでは同じシーンのまま選択を解除しています。

| 対象 | ツール | 選択 | 再生全体 ÷ 71 | フレーム2〜72の描画間隔 |
| --- | --- | --- | ---: | ---: |
| 自身も変形 | Select | なし | +0.163／−0.226 | +0.175／−0.210 |
| 自身も変形 | Select | 1個 | −0.523／−0.164 | −0.438／−0.145 |
| 自身も変形 | Move | なし | +0.719／−0.071 | +0.788／−0.105 |
| 自身も変形 | Move | 1個 | +0.160／+0.260 | +0.042／+0.150 |
| 親移動だけ | Select | なし | −0.084／−0.004 | −0.076／−0.182 |
| 親移動だけ | Select | 1個 | −0.653／−0.285 | −0.608／−0.226 |
| 親移動だけ | Move | なし | −0.295／+0.875 | −0.279／+0.823 |
| 親移動だけ | Move | 1個 | −0.380／+0.124 | −0.361／+0.133 |

前節と同じ「自身も変形・Move・選択なし」では、前回の現行版の遅れは順番を反転すると再現しませんでした。同条件の軌道と代表画像は前回と一致しています。今回の各起動は100個変形・OFF に絞ったため、他の変形数やキャッシュ ON を含む前節とは計測前に通る条件が異なります。「自身も変形・Move・1個選択」も、今回は前回と逆に再生全体が両組で長くなりました。選択なしとの差を同じ起動内で取り、さらに Select と Move を比べると、このツール差の現行 − 旧版はフレーム2〜72で −0.13／+0.19 ms、10〜69で +0.02／−0.01 ms でした。現行版の Move ツールに固有の再生低下は確認できませんでした。

Select では別の傾向が4起動に共通しました。現行版で「1個選択 − 選択なし」の描画間隔は、親移動だけの Cube が +0.26／+0.40 ms、自身も変形する Cube が −0.28／+0.02 ms でした。各シーンの選択なしを基準にすると、親移動だけの Cube を選択した方が +0.54／+0.37 ms 余分にかかり、旧版でも +0.46／+0.48 ms でした。Move では再現しませんでした。同じ起動・同じ条件の5試行内にも最大約3.09 ms の幅があり、各条件間の小差は起動順をまたいで評価しています。

通常計時の各試行と対照を引いた差は `build/fixed_cube/role_tool/summary_a1_retry1_c1_retry1_c2_retry1_a2_retry1.json` に保存しました（Git 管理外）。

##### Select ツールでの Maya Profiler 照合

通常計時で4起動とも同じ傾向を示した Select の4条件に絞り、旧 → 現行 → 現行 → 旧の4起動で、同じ配布 DLL に Maya Profiler を有効にして再生しました。各条件2試行、計32再生・2,272実描画です。各トレースの `Vp2SceneRender` 71件が描画後通知の71フレームと一致し、イベント総数は397,942〜397,945件でした。対応する通常計時の入力接続、ピボット、選択状態と代表画像も照合しました。

表は「親移動だけの Cube を選択した際の追加時間 − 自身も変形する Cube を選択した際の追加時間」です。各追加時間は、同じ起動・同じ接続での「1個選択 − 選択なし」で求めました。正値は親移動だけの Cube を選択した方が余分に時間がかかることを表します。単位は ms／描画です。

| 計時区間 | 旧・1巡目 | 現行・1巡目 | 現行・逆順 | 旧・逆順 |
| --- | ---: | ---: | ---: | ---: |
| 通常計時の描画間隔（2〜72） | +0.460 | +0.541 | +0.374 | +0.483 |
| Profiler 記録中の描画間隔（2〜72） | −2.304 | −1.603 | −0.476 | −1.097 |
| ↳ メインスレッド `EvaluationGraphExecution` | −0.198 | −0.257 | −0.147 | −0.061 |
| ↳ メインスレッド `Vp2PrepareToUpdate` | −1.227 | −1.081 | −0.409 | −0.623 |
| ↳ メインスレッド `Vp2BuildRenderLists` | −0.025 | −0.026 | −0.009 | −0.011 |
| ↳ メインスレッド `Vp2Draw3dBeautyPass` | −0.657 | −0.012 | +0.195 | −0.200 |

Profiler の各区間は内側の処理を含み、合算はできません。メインスレッドの評価グラフ実行と上表の VP2 区間はいずれも毎描画1回でした。Profiler 記録中は描画間隔の差自体が全4起動で逆転し、再生全体でも同じ逆転が起きました。通常再生で増えた時間を、これらの区間のいずれかに帰属させる根拠は得られませんでした。今回の選択差を理由とした配布実装の変更は見送ります。

Maya Profiler の記録と区間集計は `build/fixed_cube/role_tool_profile/summary_select_a1_select_c1_select_c2_select_a2.json` に保存しました（Git 管理外）。

## 固定 Cube の単体ドラッグを区間別に再計測

Maya 2025.3.3／OpenGL／Parallel で、`a04f7be3` の配布版 `bdShpL_Cube` と同じ輪郭の標準 `nurbsCurve` を比較しました。共通親の下に1,000個の transform を置き、それぞれがシェイプを1個持ちます。フォーカス用シェイプと変形入力は使いません。Cube は ±0.5 の12辺、カーブは同じ12辺を通る1次・16 CV の開曲線です。標準カーブは全1,000本の CV 座標と `.create` が未接続であることを確認しました。

最初の比較では Cube → カーブ → カーブ → Cube と独立起動し、標準カーブ側は `bdUtilNodes.mll` をロードせず、後半は操作・再生条件の実施順も反転しました。各起動で単体と共通親の Move ドラッグ、共通親を3 cm移動する再生をキャッシュ OFF／充填済み ON で各5試行しました。ドラッグ時はキャッシュ OFF で、選択した transform の X 軸ハンドルに押下、72移動、解放を送りました。全40ドラッグで各入力に1回ずつ描画後通知があり、全40再生でフレーム2〜72が1回ずつ描画されました。ON の全試行で71フレームの充填を確認しました。カメラ・選択・入力座標・X 移動量を照合し、ドラッグと再生の代表画像は型間、起動間で画素単位に一致しました。画像取得は通常計時の外です。

| 計時区間 | 固定 Cube | 標準カーブ | Cube − カーブ |
| --- | ---: | ---: | ---: |
| 単体ドラッグ・72移動の平均（ms／移動） | 3.758／3.049 | 3.066／2.743 | +0.692／+0.306 |
| 押下からその描画後通知まで（ms） | 5.639／5.260 | 7.375／5.445 | −1.735／−0.185 |
| 押下から最初の移動の描画後通知まで（ms） | 11.509／10.302 | 13.246／10.652 | −1.737／−0.350 |
| 最初の移動入力からその描画後通知まで（ms） | 2.077／1.733 | 1.928／1.920 | +0.149／−0.187 |
| 第4〜72移動の平均（ms／移動） | 3.795／3.074 | 3.077／2.677 | +0.719／+0.398 |
| 同区間の移動入力から描画後通知まで（ms／移動） | 2.031／1.556 | 1.703／1.533 | +0.328／+0.024 |
| 同区間の描画後通知からイベント処理終了まで（ms／移動） | 1.756／1.511 | 1.367／1.138 | +0.389／+0.373 |
| 共通親ドラッグ・72移動の平均（ms／移動） | 10.530／9.254 | 10.098／9.554 | +0.432／−0.300 |
| 共通親の再生 OFF（ms／実描画） | 3.034／3.230 | 2.837／3.967 | +0.198／−0.737 |
| 共通親の再生・充填済み ON（ms／実描画） | 4.261／4.258 | 3.950／4.075 | +0.312／+0.183 |

左／右は起動順の異なる2組です。各区間を試行ごとに集計してから5試行の中央値を求めました。各区間の中央値の和は全体の中央値と異なる場合があります。再生は開始・停止を含む `cmds.play()` の所要時間を71実描画で割った値です。

単体移動の平均では過去に観測した差が再現し、押下から最初の移動が描画されるまでは両組で固定 Cube が短くなりました。継続移動で両組に同程度の差が出たのは描画後通知から Qt のイベント処理が終わるまでです。この区間には `sendEvent()` が戻るまでと、その直後の `processEvents()` が戻るまでの両方が入ります。単体ドラッグ全体の集計は `build/fixed_cube/fixed_drag_baseline/summary_g1_n1_n2_g2.json` に保存しました（Git 管理外）。

### 両方のシーンで同じ配布 DLL をロードした比較

実際の使用環境に合わせ、標準カーブ側でも同じ `bdUtilNodes.mll` をロードしました。カーブのシーンには標準カーブ1,000本があり、固定 Cube のノードは0個です。起動順は固定 Cube → カーブ → カーブ → 固定 Cube です。表の左側は試験条件を正順で実行した組、右側は逆順で実行した組です。各欄は起動ごとに5試行の中央値を取りました。各組でカメラ、選択、操作ハンドルの軌道、移動量、ドラッグと再生の代表画像が一致しました。

| 操作 | 固定 Cube | 標準カーブ | Cube − カーブ |
| --- | ---: | ---: | ---: |
| 単体ドラッグ（ms／移動） | 3.511／3.049 | 2.920／3.505 | +0.591／−0.457 |
| 共通親ドラッグ（ms／移動） | 9.720／9.254 | 9.600／9.455 | +0.120／−0.200 |
| 共通親の再生・キャッシュ OFF（ms／実描画） | 3.264／3.230 | 2.714／2.866 | +0.550／+0.363 |
| 共通親の再生・充填済み ON（ms／実描画） | 4.020／4.258 | 4.273／3.811 | −0.253／+0.446 |

単体と共通親のドラッグはどちらも、組によって順位が入れ替わりました。単体ドラッグの第4〜72移動で、描画後通知からイベント処理終了までの差も +0.309／−0.213 ms です。標準カーブ単独で DLL ロード有無を比較しても順位が入れ替わっており、先の比較で出た差の原因をロード有無に帰属できません。共通親のキャッシュ OFF 再生は、開始・停止を除いたフレーム10〜69の描画間隔でも固定 Cube が +0.497／+0.453 ms 長くなりました。

通常版の比較と区間の内訳は `build/fixed_cube/fixed_drag_baseline/package_comparison_g2_l2_l1_g1_retry1.json`、標準カーブだけのロード有無の比較は `build/fixed_cube/fixed_curve_loaded/summary_l2_l1.json` に保存しました（Git 管理外）。

### 単体ドラッグ時の Geometry と VP2 の診断

配布版と同じ固定 Cube の Geometry 実装を使う診断 DLL で、暖機後の押下1回、移動72回、解放1回を3試行計測しました。各入力で1回ずつ、計222回の実描画がありました。全区間で `requiresGeometryUpdate()`、`requiresUpdateRenderItems()`、`updateDG()`、`updateRenderItems()`、`populateGeometry()` はいずれも0回です。静的属性の読み取り、ローカル形状の取得・再生成、境界取得、頂点・インデックスバッファの確定も0回でした。この操作では親 transform の移動に合わせて、固定 Cube が形状を組み立て直す処理は発生していません。

さらに配布版と、DLL をロードせずに起動した標準カーブを Maya Profiler 付きで各2回起動しました。各起動で、暖機後の72移動を3試行記録しました。Cube とカーブの `Vp2SceneRender` の差は −0.339／+0.237 ms／描画で、描画準備、描画リスト作成、Beauty、UI 描画の各区間も組ごとに符号が変わりました。この対照で継続移動時にそろった差は、`sendEvent()` が戻ってから `processEvents()` が終わるまでの +0.267／+0.468 ms／移動です。この計時にはキューに残ったアプリケーションの処理が含まれます。どの処理に時間がかかったかは特定できません。Profiler の値は診断にだけ使用しました。

診断の回数と区間の集計は `build/fixed_cube/fixed_drag_diagnostic/summary_p1_g1_n1_n2_g2.json` と `intervals_g1_n1_n2_g2.json` に保存しました（Git 管理外）。

### 同じ Maya 内でシーンを入れ替えたキャッシュ OFF 再生

独立起動の両組で差が出た共通親の OFF 再生を再確認しました。配布 DLL をロードしたまま、1起動目は Cube → カーブ → カーブ → Cube、2起動目は逆の順でシーンを作り直しました。毎回、新規シーンで旧グループと両形状型が0個であることを確認してから、共通親と1,000個のシェイプを作成しました。1回の暖機再生後に5試行、全8シーンで計40再生を測定しました。各試行でフレーム2〜72の71描画を確認し、各シーンのフレーム2・36・72の代表画像は最初の比較と一致しました。

| 同じ起動内で隣接するシーン | 固定 Cube（ms／実描画） | 標準カーブ（ms／実描画） | Cube − カーブ | フレーム10〜69の描画間隔の差（ms） |
| --- | ---: | ---: | ---: | ---: |
| 1起動目・前半（Cube → カーブ） | 3.157 | 3.122 | +0.035 | +0.109 |
| 1起動目・後半（カーブ → Cube） | 3.275 | 3.554 | −0.279 | −0.269 |
| 2起動目・前半（カーブ → Cube） | 3.281 | 3.249 | +0.031 | +0.123 |
| 2起動目・後半（Cube → カーブ） | 3.822 | 3.433 | +0.389 | +0.327 |

各シーンの5試行の中央値を使い、前半と後半の差を等しく重み付けすると、Cube − カーブは1起動目で −0.122、2起動目で +0.210 ms／実描画でした。起動をまたいだ比較で見えた約0.36〜0.55 ms の遅れは、同じプロセス内の比較で一貫して再現しませんでした。単体ドラッグ中に固定 Cube 側がローカル形状を更新する処理も検出されず、今回の条件から配布版に取り込む最適化はありません。

計測記録は `build/fixed_cube/fixed_playback_crossover/summary_x1_retry1_x2_retry1.json` に保存しました（Git 管理外）。予備の起動では、新規シーンで再作成された同じシェイプ名を旧ノードの残留と判定して検査が停止しました。表には、シェイプ作成前に空の DAG を確認する手順で完走した2起動を使っています。

## 固定 Cube の一部の子階層が動く場合

共通親の下に1,000個のコントローラーを置き、1個のコントローラーを動かすとその子だけが追従する場合を調べました。移動数は、操作対象自身を含めて10・100・500個です。各コントローラーは transform とシェイプ1個で構成し、操作対象の直下にはそれぞれ9・99・499個の子 transform を置きます。残りの990・900・500個は共通親の下で静止します。コンストレイント、変形入力、フォーカス用シェイプは使用しません。

### 独立起動での比較

Maya 2025.3.3、OpenGL、Parallel の同一環境で、固定 Cube → 標準カーブ → 標準カーブ → 固定 Cube の順に独立起動しました。両方で同じ配布 DLL（`a04f7be3`）をロードし、標準カーブは同じ12辺を通る1次・16 CV の形状を使いました。各サイズで新規シーンを作り、画面中央の同じ transform を操作します。ドラッグは Move の X 軸ハンドルへ同じ軌道の72移動を送ります。再生は選択を解除し、フレーム1〜72で同じ transform の X を0から3 cmに動かしました。ON は71フレームのキャッシュが充填されたことを各試行で確認しています。

表の正順／逆順はサイズと操作の実施順です。各起動で1条件につき暖機後5試行の中央値を取りました。ドラッグは ms／移動、再生は開始・停止を含む ms／実描画です。全60ドラッグで押下・各移動・解放に1描画ずつ、全120再生でフレーム2〜72に71描画を確認しました。計時外で1,000個のワールド位置を検査し、対象の枝だけが指定の変位に追従しました。型間でドラッグの入力軌道、ワールド変位、同条件のドラッグと再生の代表画像が一致しました。

| 動く個数 | 操作 | 固定 Cube | 標準カーブ | Cube − カーブ |
| ---: | --- | ---: | ---: | ---: |
| 10 | ドラッグ | 4.293／3.523 | 3.403／2.972 | +0.890／+0.551 |
| 10 | 再生 OFF | 1.573／1.879 | 4.712／1.614 | −3.138／+0.265 |
| 10 | 再生 ON | 1.655／1.777 | 2.153／2.293 | −0.498／−0.516 |
| 100 | ドラッグ | 3.799／4.287 | 3.446／4.024 | +0.353／+0.262 |
| 100 | 再生 OFF | 2.136／1.756 | 1.854／1.776 | +0.282／−0.020 |
| 100 | 再生 ON | 2.463／2.059 | 1.890／1.883 | +0.573／+0.176 |
| 500 | ドラッグ | 6.472／6.758 | 6.349／6.522 | +0.123／+0.237 |
| 500 | 再生 OFF | 3.037／2.825 | 3.288／2.322 | −0.251／+0.504 |
| 500 | 再生 ON | 2.818／3.401 | 3.187／2.795 | −0.369／+0.606 |

最初の固定 Cube の起動は部分階層を構築する前の VP2 初期描画で停止しました。表は新しいプロセスで完走した4起動の結果です。集計は `build/fixed_cube/fixed_branch_study/summary_g1_retry1_c1_c2_g2.json` に保存しました（Git 管理外）。

### 同じ Maya 内で両形状を入れ替えた比較

独立起動の差が普段の作業に近い環境でも再現するか、全9条件を同一プロセス内で再比較しました。配布 DLL を両方でロードしたまま、各サイズで1起動目は Cube → カーブ → カーブ → Cube、2起動目はカーブ → Cube → Cube → カーブの順に新しいシーンを作成しました。2起動目はサイズと操作の順序も反転しました。全24シーン、各5試行、計120ドラッグ・240再生で入力、移動量、描画数、キャッシュ状態、代表画像を通常版の同条件と照合しました。

各欄は Cube − カーブの差です。ドラッグは ms／移動、再生は ms／実描画で表します。1シーンの値は5試行の中央値です。隣接する2シーンを1組として差を算出し、起動内平均では前半・後半の2組を同じ重みで集計しました。

| 動く個数 | 操作 | 1起動目の前半／後半 | 2起動目の前半／後半 | 起動内平均の差（1回目／2回目） |
| ---: | --- | ---: | ---: | ---: |
| 10 | ドラッグ | +1.168／−0.260 | +0.465／+0.414 | +0.454／+0.439 |
| 10 | 再生 OFF | −0.253／+0.208 | +0.423／+0.214 | −0.023／+0.319 |
| 10 | 再生 ON | +0.241／+0.197 | +0.139／+0.043 | +0.219／+0.091 |
| 100 | ドラッグ | +1.556／+0.021 | +0.237／+0.463 | +0.788／+0.350 |
| 100 | 再生 OFF | −0.258／−0.112 | +0.312／−0.039 | −0.185／+0.137 |
| 100 | 再生 ON | +0.550／−0.610 | −0.257／−0.732 | −0.030／−0.494 |
| 500 | ドラッグ | −0.173／+1.056 | +0.902／+0.063 | +0.442／+0.482 |
| 500 | 再生 OFF | +0.441／−0.209 | −0.471／+0.183 | +0.116／−0.144 |
| 500 | 再生 ON | −0.963／−0.266 | +0.026／+0.385 | −0.615／+0.205 |

この部分階層のドラッグでは、3サイズとも独立起動と同一プロセス内の2起動平均で、固定 Cube の1移動が長くなりました。同一プロセス内では隣接12組中10組が同方向で、100個の場合は4組とも同方向でした。追従する個数に比例して型間差が広がる傾向は見られません。再生では、10個と100個の充填済み ON は独立起動時とは逆の結果になりました。全体として固定 Cube と標準カーブのどちらかに一貫した再生速度の利点を認めるには至りませんでした。

集計は `build/fixed_cube/fixed_branch_crossover/summary_x1_x2.json` に保存しました（Git 管理外）。

### 継続ドラッグのどの区間で差が出たか

通常計測と同一プロセス内比較を合わせた180ドラッグを、保存済みの入力時刻で再集計しました。全12,960移動で描画後通知が `sendEvent()` の実行中に届きました。下表は第4〜72移動の12,420件について、`sendEvent()` が戻ってから、その直後に呼ぶ `processEvents()` が戻るまでの時間を比較したものです。各試行内で69移動の平均を求め、各シーンで5試行の中央値を使いました。

| 動く個数 | 独立起動の2組（ms／移動） | 同じ Maya 内の隣接4組（ms／移動） |
| ---: | ---: | ---: |
| 10 | +0.486／+0.361 | +0.572／+0.213／+0.503／+0.320 |
| 100 | +0.345／+0.308 | +0.513／+0.277／+0.313／+0.415 |
| 500 | +0.252／+0.328 | +0.233／+0.452／+0.321／+0.247 |

全18組でこの区間が固定 Cube の方で長く、差は +0.21〜+0.57 ms／移動でした。描画後通知から `sendEvent()` が戻るまでの差は、比較順によって符号が変わりました。描画後通知は GPU 完了時刻を表しません。また、`processEvents()` の区間にはアプリケーションが保留していた処理も含まれ、どのイベント処理や待ち時間が差を生んだかは未特定です。これは Qt で Move ハンドルへ入力を送った条件での結果です。

次に調べる候補は、差が再現した `processEvents()` に届くイベントの種類・対象・件数と、通常のマウス入力で同じ差が出るかです。シェイプ内部に追加する処理の根拠は、今回の計測からは得られませんでした。生タイムスタンプからの集計は `build/fixed_cube/fixed_branch_crossover/drag_intervals_g1_retry1_c1_c2_g2_x1_x2.json` に保存しました（Git 管理外）。

### 部分階層を動かしたときの Geometry の処理回数

固定 Cube の Geometry 実装を計装した別 DLL で、同じ9条件を各3試行調べました。各条件で画面・入力・ワールド変位を通常版と照合しました。ドラッグは各試行で押下1、移動72、解放1の区間を個別に記録しました。10・100・500個の全9ドラッグ、計666実描画で、計装した13項目はすべて0回でした。親の移動に追従する子が500個あっても、固定 Cube の更新判定や形状の再生成は発生していません。

| 再生1描画あたりの呼び出し回数（全シェイプの合計） | 10個移動 | 100個移動 | 500個移動 |
| --- | ---: | ---: | ---: |
| OFF・`requiresUpdateRenderItems()` | 10 | 100 | 500 |
| OFF・`requiresGeometryUpdate()` | 0 | 0 | 0 |
| 充填済み ON・`requiresUpdateRenderItems()` | 10 | 100 | 500 |
| 充填済み ON・`requiresGeometryUpdate()` | 20 | 200 | 1,000 |

各71描画・3試行で回数はそろいました。この回数は全個体の合計で、個体別の呼び出し履歴は採取していません。全再生で `updateDG()`、`updateRenderItems()`、`populateGeometry()`、静的属性の読み取り、境界取得、ローカル形状の再生成、頂点・インデックスバッファの更新はすべて0回でした。500個移動時に2つの判定関数内で測った時間の合計は、OFF・ON とも約0.08 ms／描画相当でした。これは計装を含む各呼び出し時間の合計で、Maya 側の呼び出し準備やスレッド間の重なりは評価していません。診断の集計は `build/fixed_cube/fixed_branch_diagnostic/summary_p1.json` に保存しました（Git 管理外）。

## 10個が追従するドラッグと Maya の UI 更新

Maya 2025.3.3／OpenGL／Parallel で、前節と同じ1,000個のうち、選択した transform と子9個が追従するシーンを使いました。配布 DLL を両型でロードしたまま、1起動目は固定 Cube → 標準カーブ → 標準カーブ → 固定 Cube、2起動目は逆順にシーンを作り直しました。時間差の符号は Cube − カーブ、ドラッグ中の単位は ms／移動です。

### 継続移動中に届く Qt イベント

各シーンで同じ Move ハンドルへの72移動を、無計装、イベントの種類だけを記録、種類と受信先を記録する3方式で各5試行実施しました。モードの順序を交代し、全120ドラッグで入力軌道、移動した10個・静止した990個、描画と代表画像を照合しました。第4〜72移動の `processEvents()` の区間で求めた起動内平均差は、無計装で +0.284／+0.330、種類だけで +0.420／+0.278、受信先まで記録すると +0.336／+0.350 でした。

メインウィンドウへの `UpdateRequest` とヘルプラインおよび親ウィジェットへの `Paint` が毎移動で届きました。チャンネルボックスの表への `Paint` は、両型とも69移動中の同じ33移動で届きました。受信先を記録した全40試行で、その33個の入力番号が一致しています。

| 第4〜72移動の内訳 | 移動数／試行 | 受信先を記録した試行の差 | 同じ入力番号で分類した無計装試行の差 |
| --- | ---: | ---: | ---: |
| チャンネルボックスへの `Paint` が届いた移動 | 33 | +0.910／+0.675 | +0.435／+0.625 |
| その他の移動 | 36 | +0.032／+0.019 | +0.108／+0.161 |

この計時は各移動の `processEvents()` 全体です。イベントフィルターは対象の処理が始まる前に呼ばれるため、受信時刻から個別の `paintEvent()` の実行時間は分かりません。無計装試行は入力番号だけを照合しました。[Qt のイベントフィルター](https://doc.qt.io/qt-6/eventsandfilters.html#event-filters)

通常試行・診断試行の結果は `build/fixed_cube/fixed_branch_queue/summary_q1_q2.json`、入力番号別の集計は同じディレクトリの `channel_box_strata_q1_q2.json` に保存しました（Git 管理外）。

### チャンネルボックスとヘルプラインの表示を切り替えた比較

試験用 Maya で通常表示、チャンネルボックスの表を含む `ChannelBoxForm` のみ非表示、ヘルプラインの `helpLine1` のみ非表示、両方非表示の4条件を交代させました。各シーンで transform を選択してから表示状態を変え、ビューポートの位置・サイズ、カメラ、入力軌道をそろえました。各条件の5試行はイベントフィルターを外して計時し、別の1試行で対象への `Paint` を数えました。

下表は第4〜72移動の結果です。各欄は1起動目／逆順の2起動目を示します。シーンごとに5試行の中央値を取り、各起動内で隣接する2組の Cube − カーブの差を平均しました。全8シーン・計160回の計時で、移動した個体と静止した個体、代表画像を通常試行と照合しました。

| UI の表示条件 | `processEvents()` の差（ms／移動） | 移動全体の差（ms／移動） |
| --- | ---: | ---: |
| 通常表示 | +0.420／+0.386 | +0.222／+0.311 |
| チャンネルボックスの表だけ非表示 | +0.113／+0.033 | +0.444／−0.139 |
| ヘルプラインだけ非表示 | +0.144／+0.395 | −0.310／+0.247 |
| 両方非表示 | −0.047／−0.064 | −0.283／−0.231 |

通常表示から両方非表示にすると、移動全体は固定 Cube で 4.23 → 2.39／4.24 → 2.37 ms、カーブで 4.01 → 2.67／3.93 → 2.60 ms に短縮しました。別に行った描画イベントの確認では、各型・各起動とも2シーンの合計で、通常表示時はチャンネルボックスの表が74回、ヘルプラインが148回再描画されました。各対象を非表示にした条件では、その対象への `Paint` は0回でした。

チャンネルボックスの表を隠すと両起動で `processEvents()` の型間差が縮み、両方隠すと通常表示で見られた Cube の遅れは移動全体でも消えました。ヘルプラインだけ隠したときの差の縮み方や、表だけ隠したときの移動全体の順位は、起動順によって変わりました。表には固定 Cube の8つの静的属性を表示できますが、個々の行の評価・描画時間は未計測です。今回の結果からは、固定 Cube の形状キャッシュや配布版の属性表示を変更する根拠は得られませんでした。集計は `build/fixed_cube/fixed_branch_ui_control/summary_u1_retry1_u2_retry1.json` に保存しました（Git 管理外）。

### Windows 経由のドラッグ

別の2起動で同じ2通りのシーン順を使い、各シーンで2回ずつ、Windows 側から X ハンドルを128ピクセル動かしました。Maya の通常のイベントループでビューポートが受信した入力と VP2 の描画後通知を記録しました。16回すべてで押下・移動1回・解放が届き、移動後の描画を1回ずつ対応づけられました。動いた10個の移動量は +45.444 cm、静止した990個の位置と最終画像は両型で一致しました。

移動受信から最初の描画後通知までの Cube − カーブの差は、1起動目が +0.440 ms、逆順の2起動目が −0.489 ms でした。Windows 経由の単発入力では、一貫して遅い側はありませんでした。今回の入力手段で観測できたのは各ドラッグの1移動までです。マウスを動かし続けた際の FPS や、上記の第4〜72移動の差が通常入力で再現するかは未確認です。集計は `build/fixed_cube/fixed_branch_mouse/summary_m1_m2.json` に保存しました（Git 管理外）。

## 参考

- [Autodesk Scene Overrides](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Viewport-2-0-API/Overview-of-the-Viewport-2-0-API/Maya_DEVHELP_Viewport_2_0_API_Overview_of_the_Viewport_2_0_API_Scene_Overrides_html.html)
- [MRenderItem](https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_h_w_render_1_1_m_render_item.html)
- 既存調査: `build/controller_performance/cube_investigation/`（Git 管理外）

既存 `bdControllerShape` の過去の数値と今回の測定値を、同条件の直接比較として混ぜません。
