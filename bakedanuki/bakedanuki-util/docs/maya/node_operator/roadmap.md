# Roadmap

このページは `NodeOperator` 周辺の設計メモと今後の作業候補です。

1.0.0 までは開発中 API として扱います。将来の設計と使いやすさを優先し、互換性維持
よりも改善を選んで、必要な破壊的変更を積極的に行います。安定した API 互換性の提供は
1.0.0 以降を対象とします。破壊的変更は原則として `0.x.0` の minor release で行い、
`0.x.y` の patch release では意図的に行いません。変更内容と移行手順はルートの
`CHANGELOG.md` に記録します。

## 現在固まっている方針

- Maya 専用パッケージとして割り切る。
- Maya 2025 / 2026 / 2027、Python 3.11.4 以降を対象にする。
- `ModifierManager` を経由して `MDGModifier` / `MDagModifier` を扱う。
- `AttributeField` は entry point / descriptor に専念する。
- `AttrOperator` は定義情報を持つ。
- `PlugOperator` は scene 上の plug 操作を担当する。
- alias は同じ logical plug なら同じ instance を返す。
- plug値設定の`set_direct()`は便利用途として残すがundo対象外と明記する。
  `keyframe.set_direct()`は廃止済みで、互換aliasは提供しない。
- custom compound は低レベル型と意味付き alias を分ける。
- `Quat` と `Double4` は、4つの`float`を保持する`Scalar4[float]`を共有するが、
  継承関係を持たない別の具体型として扱う。plugの物理表現はdouble4を共有しても、
  値型の演算体系は分離する。

## 完了済みの大きな流れ

- pytest 導入。
- `plus_minus_average` / `wt_add_matrix` の代表的な挙動を pytest 化。
- `ModifierManager` 追加。
- NodeOperator / PlugOperator の modifier 参照を manager 経由へ移行。
- Pyright による node 作成、descriptor、compound / multi、戻り値型の
  contract test を追加。
- Maya 2025を基準に、2026 / 2027の変更・新規node schemaをsparse overlay化。
  実行Mayaの自動判定と、IDE専用の`typing_maya_version`を分離し、未指定時は
  3 version共通面、指定時はversion固有の補完を返すcontractを追加。
  version間比較用の固定plugin profileと専用CLIを用意し、Maya 2027実機での
  overlay生成まで完了。再生成後の受け入れ確認範囲は`testing.md`に分離して記録。
- plug cache / indexed plug cache / child direct index などの速度改善。
- custom scalar compound の階層整理。
- `double2` / `double3` / `double4` / `float2` / `float3` などを custom compound 側へ移行。
- `long2` / `long3` / `short2` / `short3` を custom compound 側へ移行。
- unit compound の `double_angle2/3`、`double_linear2/3`、`float_angle2/3`、`float_linear2/3` を追加。
- compound `get()` / `set()` / `set_direct()` を整備。
- 全`PlugOperator`のlock / unlock APIと、scalar / scalar compoundだけに現れる
  Channel Box 3状態のAPIを追加。undo対応のqueued methodと、即時反映するdirect methodを
  分離し、compound child展開、multi element制約、runtime / Pyrightのcapability contractを
  Maya 2025上で検証。
- compound child limit の public method 化。
- `lookup.py` の double4 / quat 解決対応。
- 18 種類の compound 専用値型を追加し、scalar compound の
  `get()` の戻り値へ接続。
- `MatrixPlugOperator.get()` / `DataMatrixPlugOperator.get()`を
  `TransformMatrix`へ統一し、matrix plugの値設定、`MMatrix`との乗算、
  typed matrixの未設定時エラーを同じ契約へ整理。
- `TransformMatrix`とmatrix plugの値設定に、row-majorのflat 16要素 / 4行4列の
  numeric sequence入力を追加。厳密な形状検証、snapshot、runtime / Pyright contractを
  Maya 2025上で検証。
- `TransformMatrix`に、translate / Euler rotate / quaternion / scale / shearを
  keyword-onlyで受け取るcomponent合成を追加。全componentの任意指定、matrix sourceとの
  排他、回転順序名とMayaの0〜5のindex、全Euler回転順序とquaternionの
  `composeMatrix`等価性をMaya 2025上で検証。
- `TransformMatrix`の分解値をplugの`get()`と同じcompound専用値型へ統一。
  translateはcentimeterの`DoubleLinear3`、Euler回転はdegreeの
  `DoubleAngle3`、scale / shearは`Double3`、quaternionは`Quat`を返す。
- `Quat`にidentity / sequence / `MQuaternion` constructor、Euler / axis-angle /
  2-vector / matrixからの作成、Quaternion積、変換、逆元、共役、正規化、
  shortest-path slerp、raw状態と等価性の照会を追加。
- `Double2` / `Double3` / `Double4`、`Float2` / `Float3`に、同じ具体型同士の
  加減算、scalarによる乗除算、符号反転を追加。immutable性と正確な戻り値型を維持し、
  unit値型、整数値型、`Quat`へは演算を波及させない構成へ分離。
- `MPxCommandBase`をAPI 2.0と`ModifierManager`へ統一。型付きparameter、明示的な
  DG / DAG実行境界、undo / redo、初回失敗時rollback、結果設定、複数commandの
  登録rollback、typed facadeの運用をruntime / Pyright testとsampleで固定。
- DAG の `full_path` / `is_instanced` / `parent` / `parents` と、親変更時の
  instancing 制約を追加。
- DAG traversal の `children()` / `ancestors()` / `descendants()` を追加。
  具体型解決、`ModifierManager`共有、実行済みscene状態、instancing時の列挙規則を
  Maya 2025上で検証。
- DAG traversalへShape filter、class-based type filter、完全一致option、
  固定child indexの`descendant_chain()`、`until`による境界指定を追加。
  `nodes.types`から具体classを参照できる型・補完contractも整備。
- 親 Transform 必須の raw shape 作成 API を追加。
- `camera` / `locator` / `mesh` / `nurbsCurve` / `nurbsSurface` を最初の
  作成確認済み shape として公開。
- 抽象 `shape` の共通 attribute を静的 query から生成し、concrete shape の
  重複生成から除外。
- concrete shape も node instance を作らない静的 query へ統一し、Maya 2025 +
  MtoA の shape 81 種で attribute 取得、TODO なしのコード生成、構文確認、
  別 mayapy process 間の snapshot 比較を完了。
- concrete shape 81種の generated class / public wrapper / node_attr を正式生成し、
  `nodes.existing` の具体的な補完 stub へ反映。
- Maya 2025 で作成可能な concrete shape 80種を、親 Transform 必須の
  `nodes.create.<nodeType>()` へ公開。
- 80種すべてについて `nodes.create.with_transform.<nodeType>()` を追加し、
  Transform と具体 Shape の一括作成、命名、undo / redo、戻り値型の補完を整備。
- transform 派生 NodeOperator の生成と作成 API を分離し、`nodes.create` は
  allowlist による段階公開へ変更。
- Maya 2025で作成可能なconcrete transform系52種すべてを、未接続・未初期化の
  rawノードとして`nodes.create.<nodeType>()`へ公開。親指定、具体型、命名、
  undo / redoと補完stubを検証。
- transform 派生 node の最初の既存 node 用サンプルとして、`ikHandle` /
  `ikEffector` の具体型と `nodes.existing` 補完を追加。
- transform 派生 node の第二グループとして、constraint 系14種の具体型と
  `nodes.existing` 補完を追加。専用command相当の接続はraw作成と分離。
- transform 派生 node の第三グループとして、field / emitter 系11種の具体型と
  `nodes.existing` 補完を追加。dynamics用の初期化・接続はraw作成と分離。
- transform 派生 node の第四グループとして、dynamics / deformer 周辺5種の
  具体型と `nodes.existing` 補完を追加。専用の作成手順・接続はraw作成と分離。
- transform 派生 node の第五グループとして、HIK 系5種の具体型と
  `nodes.existing` 補完を追加。`hikFKJoint` / `hikHandle` はnative継承に合わせて
  `Joint` / `IkHandle` を基底とし、専用作成手順はraw作成と分離。
- transform 派生 node の第六グループとして、scene / utility 系6種の具体型と
  `nodes.existing` 補完を追加。`lookAt` はnative継承に合わせて `AimConstraint` を
  基底とする。
- transform 派生 node の第七グループとして、VarGroup 系5種の具体型と
  `nodes.existing` 補完を追加。作成不能な抽象native基底 `baseGeometryVarGroup` も
  `BaseGeometryVarGroup` として型階層に保持し、抽象基底だけは`nodes.create`に非公開。
- transform 派生 node の第八グループとして、特殊transform
  `ufeProxyTransform` / `unknownTransform` の具体型と `nodes.existing` 補完を追加。
  `ufePath` はruntime-defined attributeとして補い、両方をraw作成へ公開。
- transformでもshapeでもない最後の汎用DAG `unknownDag` を、`DAG` 直系の
  `UnknownDag` として追加。Mayaが親Transformを自動作成するplaceholder nodeのため、
  `nodes.existing` のみに公開。
- `Transform` / `Joint`に、指定したDAGへDAG原点のworld位置を合わせる
  `match_position()`と、world姿勢を`rotate` / `rotateAxis` / `jointOrient`の
  いずれか1属性だけで合わせる属性別マッチAPIを追加。部分軸のworld / local /
  object基準、offsetParentMatrix、全rotateOrder、undo / redoをMaya 2025上で検証。
  子補償optionも設定APIと共通化し、目標値の計算後は対応する`set_*()`へ委譲。
  world姿勢のみ／位置を含む補償とJoint子の補償属性を個別に選択可能。
- `Transform` / `Joint`に、`translate` / `rotateAxis` / `rotate` / `jointOrient`の
  設定・丸めを行うnode-level APIを追加。丸めは共通の値設定経路を使用。子補償は
  既定で無効とし、world姿勢、world位置、Joint子の`rotate` / `jointOrient`補償を
  個別に選択可能。全rotateOrder、undo / redo、lock・入力接続・instanced DAGの拒否を
  Maya 2025上で検証。
- 上記の属性値設定APIへ`space="local"` / `"world"`を追加。既定のlocal属性値設定を
  維持し、world指定ではDAG原点または最終world姿勢を、対象の1属性だけで実現する
  local値へ変換。match APIとworld→local変換を共有し、offsetParentMatrix、全rotateOrder、
  非一様scale / shear、負scale、子補償、instanced DAGと非可逆な実効親行列の拒否を検証。
- `Transform` / `Joint`に、Transform系nodeまたは名前、world / local座標をターゲットに
  する属性別エイム姿勢APIを追加。任意のlocalエイム／アップ軸、明示的アップ、アップ
  省略時の最短回転、rotate pivot基準のsnapshot計算、子補償をMaya 2025上で検証。
- 直接のTransform系子へ向ける属性別エイム姿勢APIを追加。Shapeを除外した直接子index、
  親空間アップ方向、既定で親軸へ合わせるエンド処理、全直接子のworld姿勢・位置の必須
  補償、Joint子の既定`jointOrient`補償を検証。階層間で結果が依存する場合は各操作後の
  `do_it_dg()`を必要とするsnapshot契約を維持。
- 現在の合成姿勢を基準に、処理前の正軸を処理後の符号付き軸へ対応させる属性別の
  軸リマップAPIを追加。2軸だけを指定して残りを右手系から決定し、3種類の軸pair、
  処理後軸の全順列と全符号を組み合わせた72通り、全rotateOrder、子補償、undo / redo、
  lockとPyright contractを検証。入力接続の拒否は対応する属性設定APIの共通経路を使用。

## KeyframeManagerの開発状況と次の候補

### 次の最優先項目

指定範囲に実在するキーのtangent lock / weight lock一括変更と、
`node.keyframes` / `nodes.keyframes`単位の既存カーブに対するweighted一括切り替え、
`AnimationClip.reversed()`による独立した逆再生clipの作成、
`AnimationClip.extract(nodes=...)`によるnode単位の部分抽出、
`node.keyframes` / `nodes.keyframes`単位のEuler filterとキー削減を実装しました。

属性単位の部分抽出はnode抽出の利用状況を確認してから再検討します。
次の最優先項目はnode / nodes単位のキー削減の利用者確認後に決めます。
各項目の公開method名・引数と
対象なし・離散属性・layer・Undo / Redoの詳細契約は、着手時に現行APIと合わせて確定します。

2026-09-12時点で、Undo対応、キー設定のAPI経路・一括処理、値のsampling、
詳細データの保存・復元、指定範囲の境界補完まで実装し、利用者による動作確認も完了しています。
範囲切り出しの初期版を未着手の項目として再実装する必要はありません。
続く開発で詳細データ用の性能測定と範囲取得の改善、TA / TL / TUノードの`.keyframe`による
明示カーブ操作と、`find_anim_curves()`による接続調査用の上流候補取得を実装しました。
通常のquery・編集は、そのチャンネル自身のカーブを自動解決します。単位変換、
pairBlendの同じ軸・currentDriver入力、blendWeightedの入力index順の探索に対応し、
driven key・別軸・weight・constraintのdriverを対象から除外します。
続いて`anim_layer(name)`による「1 plug × 1 layer」の操作入口を実装しました。
既存layerを指定し、BaseAnimationと登録済み属性の取得・編集・詳細データ復元、
Mayaにlayerを明示したキー設定を、共通のModifierManagerで扱えます。
layer未指定の入口も、キー設定・取得・編集をsceneのベース（root）layerへ統一しました。
Mayaの選択layer・preferred・keying modeから独立し、rootの改名にも追従します。
layer作成と登録も実装しました。`nodes.create.animLayer()`の戻り値へ`add_plugs()` / `add_nodes()`で
対象を登録し、その戻り値を`anim_layer(layer)`へ渡してキー設定まで一括予約できます。
詳細データ復元も、登録済み属性のベース・指定layerにカーブがなければ自動作成します。
事前の仮キーは不要で、内部の作成用キーを残さず、同じ履歴で作成から復元まで扱えます。
この自動作成も利用者による動作確認まで完了しています。
続いてlayer構成・所属属性数を指定する性能測定を追加し、所属照会と復元時のlock検査を改善しました。
2026-09-14時点で、この性能改善も利用者による動作確認とcommit / pushまで完了しています。
2026-09-15、続いて[キーフレーム移動](#キーフレーム移動の実装)を追加しました。
相対・絶対移動、移動先キーの置換、任意の境界挿入を予約・Undo / Redo対応で扱います。
移動APIは利用者による動作確認とpushまで完了し、`218751db`へ反映済みです。
続いて、手動接線を維持するキー削減`reduce_keys()`を追加しました。
現行仕様は[キーフレーム](attributes.md#キーフレーム)、
履歴管理は[ModifierManager](modifier_manager.md)、検証方法は[testing.md](testing.md)を参照します。

### 完了した機能と用途

| 用途 | API / 状態 |
| --- | --- |
| 作成・挿入・接線変更・削除 | `set_key()` / `insert_key()` / `set_tangent()` / `set_tangents()` / `set_tangent_lock()` / `set_tangent_locks()` / `delete_key()` / `delete_keys()` / `delete_anim_curve()`。`tangent_type`によるin / out共通指定、個別側の上書き、単一・両端包含範囲・全キーの接線typeとキー単位のtangent / weight lock変更、Undo / Redo・rollbackに対応 |
| 時間方向への移動 | `move_frame()` / `move_frames()`。単一・両端包含範囲・全体の相対移動と絶対移動、衝突先の置換、任意の境界挿入。`move_frames()`はlinear / smoothstepで移動量を範囲の外側へならし、対象キー同士の衝突・順序逆転を拒否。属性・layer・明示カーブで同じ操作を使用 |
| 時間方向への拡縮 | `scale_frames()`。正の倍率・長さ・両端合わせ、任意時刻の`pivot`、最大4境界の補完、主区間配置先の部分置き換え（既定）とmerge。linear / smoothstepで時刻・接線Xへの影響度を補間し、Undo / Redo・rollbackに対応 |
| 値の設定・加算・拡縮 | `set_value(s)` / `add_value(s)` / `scale_value(s)`。単一・範囲・全体の生値を編集。ピボット、0・負の倍率、既存キーだけへのlinear / smoothstepの補間ウェイト、任意の境界挿入、接線・履歴保持に対応 |
| キー削減 | 属性・明示カーブの`reduce_keys()`と、`node.keyframes.reduce_keys()` / `nodes.keyframes.reduce_keys([...])`。TA / TL / TUの元カーブとの値の誤差を検査してキーだけを削除。残すキーの手動接線・範囲内両端・既定のbreakdown・step系の切り替わりを保持。node / nodesでは全カーブを計画後に一括変更 |
| 複数キーの設定 | `set_keys()`へ`(frame, value)`の列を渡す。単純なカーブではバッチ内で取得と変更キャッシュを共有 |
| 指定時刻の評価済み値 | plugの`sample_values()`。constraint・layer等の合成結果も取得し、`set_keys()`へ渡せる。新規layerの先頭値が古くなる問題は、上流カーブからの再評価伝播で修正 |
| plug入力のベイク | `bake()`。ベースまたは明示layerの生入力を等間隔に評価してTA / TL / TUへ全置換。連続・離散属性を分けた接線指定、上流nodeと非対象のcompound子・layerの維持、Undo / Redo・rollbackに対応 |
| nodeの接線一括変更 | `node.keyframes.set_tangents()` / `nodes.keyframes.set_tangents([...])`と各`set_tangent_locks()`。keyable / channelBoxまたは明示属性の既存カーブだけを対象にし、全対象を1単位で変更。接線typeでは連続・離散属性を分け、lockでは両方を対象にする |
| nodeのEuler filter | `node.keyframes.euler_filter()` / `nodes.keyframes.euler_filter([...])`。標準rotate 3軸の同期した既存キーを静的`rotateOrder`に従ってfilterし、範囲内先頭をanchorとして姿勢を維持。ベース・明示layer、全対象の事前検証、Undo / Redo・rollbackに対応 |
| node入力の一括ベイク | `node.keyframes.bake()`。明示属性またはkeyable / channelBox属性をscalar leafへ展開し、静的な対象も既定でカーブ化。接線指定、全対象の事前sampling、compound共有接続の一括分割、操作全体のUndo / Redo・rollbackに対応 |
| 複数node入力の一括ベイク | `nodes.keyframes.bake([...])`。nodeごとに存在する明示属性または自動収集した属性を全nodeで変更前にsampling。接線指定、node間を含むUndo / Redo・rollback、共通layer、総サンプル数上限に対応 |
| 実在キーの時刻・値 | `get_keys()`。指定範囲に存在するキーだけを返し、境界補完は行わない |
| 詳細なキー情報・カーブ全体 | `get_key_data()` / `set_key_data()`、`get_curve_data()` / `set_curve_data()`。JSON保存・復元と、未接続plug・登録済みlayerのカーブ自動作成に対応 |
| カーブ設定 | `get_weighted()` / `set_weighted()`。変更はUndo / Redoに対応 |
| 区間の切り出し | 両方の詳細取得APIに`start_frame` / `end_frame` / `include_boundaries=True`を実装。境界キーと調整後の接線を取得 |
| チャンネルの自動選択 | layer未指定はベース（root）に固定。layerなし・未所属属性は単位変換・pairBlend・blendWeighted越しの通常チャンネル探索を使用。キー設定の値解決はMayaに委譲し、query・挿入・削除・詳細データも同じ対象を扱う |
| layer指定 | `anim_layer(name)`は元managerを変えず、同じplugとModifierManagerを共有するKeyframeManagerを返す。既存layerのノード同一性・改名追従、BaseAnimationと登録済み属性、空カーブ、書込み時のlock / reference検査に対応 |
| layer作成・登録 | `nodes.create.animLayer(name=..., override=False)`でroot直下へ作成。rootがなければ同時作成。`add_plugs()`は明示leaf、`add_nodes()`はノード自身のkeyable・未lockの対応属性を登録。作成待ちlayerを`anim_layer()`へ渡し、登録・キー設定まで共通履歴で実行可能 |
| 明示カーブ操作 | TA / TL / TUノードの`.keyframe`は`CurveKeyframeManager`。ノード同一性を保持し、未接続・共有出力・時間入力接続を持つカーブ自身の取得・編集・削除・保存復元に対応 |
| 接続調査用の候補取得 | `find_anim_curves()`で具体ノードのtupleを取得。全8型、型filter、名前順、重複排除、各経路の最初のカーブでの停止に対応。通常の対象選択とは独立した補助API |
| 詳細データの性能測定 | 専用benchmarkで取得・予約・実行・Undo / Redo・JSON変換を分離。直接接続・ベース・加算・Overrideと所属属性数を指定可能。指定範囲だけの詳細取得に加え、所属確認とlock検査のPython巡回を削減 |

### 次の開発でも維持する契約

- queryは実行済みsceneだけを読み、保留中modifierを暗黙に実行しない。
  変更は同じModifierManagerへ予約し、MPxCommandのUndo / Redoと失敗時rollbackへ参加させる。
- layer未指定は、キー設定・query・編集・詳細データをsceneのベース（root）layerへ固定する。
  `BaseAnimation`の名前を固定せず、query・初回実行時にrootを解決する。
  選択layer・preferred・keying modeで対象を変えず、lockされていても別layerへ退避しない。
  layerなし・未所属属性は、そのチャンネル自身の最初の時間入力カーブを使用する。
  DG全体の候補列で先頭を選ばず、軸とkeying入力を保つ。pairBlendはcurrentDriver、
  blendWeightedは入力index順。空カーブも対象に含め、driven keyやconstraintのdriverへは進まない。
  未対応の中間ノードは明示エラーとし、キー設定のMayaによる値解決は維持する。
- layerを指定する場合は`anim_layer()`を使用する。元の入口は変更せず、別layerの入口とも
  ModifierManagerを共有する。指定layerの同一性を保持し、所属はquery・初回実行時に再検査する。
  キー設定は元のplugに対する値をMayaへ渡し、取得・詳細復元はlayer自身の生カーブ値を扱う。
  この入口でlayer作成・属性登録・選択layerへの自動切替は行わず、find_anim_curvesの診断範囲も変えない。
  作成・登録はAnimLayer側の明示APIを使う。add_nodesは自身の対応属性だけを実行時に列挙し、
  add_plugsは指定対象が未対応・lockならエラーにする。選択状態を変えず、同一batchのrollbackを保つ。
  sample_valuesは元のplugの合成後の評価値を返し、layerのカーブ値の取得とは分ける。
  取得前に関連する上流カーブから再評価を伝播するが、現在時刻・選択・modified flag・履歴や
  保留中modifierは変えない。公開find_anim_curvesの最初のカーブで停止する契約も維持する。
- `KeyData`は直接編集可能。予約時に再検証して独立コピーし、予約後の編集が実行内容や
  Undo / Redoに波及しない。`AnimCurveData`の共通設定は不変で、変更には`dataclasses.replace()`を使う。
- 詳細データの公開値はdegree / cm / unitless。接線XYは取得元のweightedによらずweighted相当の表現。
  Xは秒、Yは公開値と同じ単位。保存データの復元時は`seconds_per_frame`を保持する。
- `set_key_data()`は既存カーブのweightedを維持し、新規はnonweighted。
  weightedを含めて形状を復元する場合は`set_curve_data()`を使う。
  未接続plugと、登録済み属性のベース・指定layerの空き入力へカーブを自動作成する。
  内部の作成用キーは両APIとも除去する。set_curve_dataは全置換、set_key_dataは既存キーを維持した追加・上書き。
  layer自体の作成・属性登録は明示APIを先に予約する。対象カーブのないconstraint・driven key・
  pairBlend等の既存接続を自動で組み替えず、layerの入力側も同じ条件で検査する。
- 境界補完は既定で有効。範囲指定時は形状を優先して連続接線をfixed化し、接線・weightの
  lockを解除する。既存キーと元の接線情報だけが必要なら`include_boundaries=False`。
  範囲無指定では接線名・lockを維持した全体取得になる。
- 元カーブが-100 / 100の2キーでも、`get_key_data(-50, 50)`は補完した2キーを返す。
  同じ範囲の`get_keys()`は空list。毎フレームの値が必要な場合は`sample_values()`を使う。
- v1.0.0未満では互換aliasや旧形式の変換処理を残すことより、APIと実装の整理を優先する。
  現行JSONはschema 2のみ対応。旧schema 1の変換や廃止した`weighted`引数は復活させない。

### 未着手の候補と着手時の論点

通常のチャンネル選択、既定のベース選択、layer名による選択は実装済みです。
時間方向の移動と、手動接線を維持するキー削減も実装済みです。
複数node・属性の一括保存・復元は`bdu.AnimationClip`として実装しました。
合成保存とlayer保持、keyable / channelBox収集、名前空間・対象node順での対応付け、
追加・全置換・部分置換、schema 2 JSONを扱います。[仕様](animation_clip.md)を参照してください。
preserveの明示layerは名前に加え、liveなanimLayerの`NodeOperator` / `MObject`でも選択できます。
静的な属性は既定で除外し、`include_static=True`で含めます。
上流のアニメーションや、layer再現に必要な静的な生値は保持します。
`AnimationClip.restore()`の復元時刻指定も実装しました。`offset_frames` / `to_start_frame` /
`to_end_frame`で、保存区間・全nodeのキー・layerとrootの設定カーブを平行移動します。
続いて`time_scale` / `duration_frames`による正の時間拡縮と、開始・終了の両端指定による区間合わせを実装しました。
全キーとlayer設定の時刻・接線Xを変換します。フレーム引数は予約時のUI時間単位で捕捉し、
予約後のFPS変更でも秒単位の配置・長さを維持します。負の倍率は受け付けず、
逆再生は後から追加した`AnimationClip.reversed()`で独立clipを作成します。
さらにKeyframeManagerの`scale_frames()`を追加しました。既存キーの時間拡縮と、
配置先区間の部分置き換え（既定）・同時刻だけの上書き（merge）に対応します。
利用者による動作確認・pushまで完了しました（`66dee785`）。
続いて値編集の6メソッドと、複数キーへの補間ウェイトを追加しました。
`set`・`add`は手動接線を維持し、`scale`は実効倍率で接線Yを拡縮します。
nonweighted接線は正規化し、weighted接線は変換後の長さを保持します。
補間は既存キーの影響度だけを変え、自動サンプリングやイーズ再現用の接線調整は行いません。
`insert_missing=True`だけが、明示した最大4境界を補います。
現行仕様は[値編集](attributes.md#キーの値を編集する)を参照してください。
値編集は利用者による動作確認・pushまで完了しました（`ba5fc139`）。
続いて`move_frames()`へ同じ補間引数を追加しました。移動前の時刻から影響度を求め、
影響度0の端点を含めて対象キーの衝突・順序逆転を検査します。
補間移動も利用者確認・pushまで完了しました（`9a63af85`）。
続いて`scale_frames()`の補間を追加しました。時刻は`t + (F(t) - t) * w`、
接線Xは実効倍率`1 + w * (s - 1)`で変換します。主区間だけで拡縮基準と
部分置き換えの範囲を決め、影響度0の端点を含む対象キーの衝突・順序逆転を拒否します。
補間拡縮も利用者確認・pushまで完了しました（`fbf9c033`）。
続いて`pivot`を追加しました。省略時の開始基準を維持し、指定時は任意時刻を基準に拡縮します。
倍率・長さ・補間と併用でき、`offset`は拡縮後に加算します。
配置先の境界指定とは併用せず、ピボット指定によるキー追加もしません。
ピボット指定も利用者による動作確認・pushまで完了しました（`f0def8ab`）。
続いて時間方向の操作名を`move_frame()` / `move_frames()` / `scale_frames()`へ整理しました。
時間・値の編集引数を`offset` / `scale` / `pivot`等へ短縮し、旧名のaliasは提供しません。
対象を選ぶ`frame` / `start_frame` / `end_frame`と、既存の編集処理は維持します。
`AnimationClip.restore()`の引数は変更しません。対応表は[旧APIからの移行](attributes.md#旧apiからの移行)を参照してください。
名称整理も利用者による動作確認・pushまで完了しました（`b90965c0`）。
続いて`AnimationClip.reduce_keys()`を追加しました。時間範囲と許容誤差を指定して、
全nodeの属性チャンネルの保存カーブを削減した独立clipを返します。時間は保存フレーム単位です。
元clip・scene・保留中modifier、layerとrootの設定は維持します。既存の削減コアを共有し、
作業用カーブで評価します。許容誤差は各保存カーブに対するもので、復元先の最終合成値は保証しません。
クリップ削減も利用者確認・push済みです（`8a722b40`）。仕様は[AnimationClip](animation_clip.md#保存データのキー削減)を参照してください。
続いて`AnimationClip.restore(start_frame=..., end_frame=...)`による使用区間の指定を追加しました。
保存フレーム単位で区間を選び、境界補完・連続接線のfixed化後に拡縮・移動します。
layerとrootの設定も同じ区間で切り出し、既存の設定比較・全置換の契約を維持します。
範囲復元も利用者確認・push済みです（`9c405008`）。仕様は[復元に使用する範囲](animation_clip.md#復元に使用する範囲)を参照してください。
続いて`AnimationClip.save()` / `load()`によるJSONファイル保存・読込を追加しました。
汎用処理は`bd_util/py/json_file.py`へ分離し、`bdu.json_file.write()` / `read()`として公開します。
親フォルダ作成と上書きは既定で有効。保存先と同じフォルダの一時ファイルへ書き終えてから確定し、
clipは保存前・読込時にschema 2を検証します。ファイル操作は即時で、sceneとmodifierを変更しません。
仕様は[JSONファイル入出力](../../py/json_file.md)と[clipのファイルAPI](animation_clip.md#jsonファイルの保存読込)を参照してください。
続いてplug単位の`KeyframeManager.bake()`を追加しました。再生範囲または指定区間の
評価済み生入力を一定間隔で取得し、対象入力だけを時間入力カーブへ全置換します。
既定ベースと明示layer、constraint・expression等の入力切断、compound接続の兄弟保持、
既存カーブ再利用・共有カーブ分離、時間単位捕捉、反復Undo / Redo・rollbackに対応します。
各時刻は独立評価とし、simulationや履歴依存のdynamics、TTは初期版の対象外です。
仕様は[plug入力のベイク](attributes.md#評価済み入力をキーフレームへベイクする)を参照してください。
続いてnode単位の`node.keyframes.bake()`を追加しました。明示属性、keyable属性の自動収集、
channelBox属性の任意追加、静的値の既定ベイク、compound / 実在array要素の展開、指定layerに対応します。
全対象のsampling完了後に接続を変更し、1属性でも失敗すれば操作全体をrollbackします。
仕様は[nodeの複数属性をまとめてベイクする](attributes.md#nodeの複数属性をまとめてベイクする)を参照してください。
続いて複数node単位の`nodes.keyframes.bake([...])`を追加しました。明示属性名は存在するnodeだけへ
適用し、全nodeで見つからない名前はエラーにします。全node・全属性のsamplingを先行し、
上流・下流nodeの指定順に依存しない操作全体のUndo / Redo・rollbackに対応します。
仕様は[複数nodeをまとめてベイクする](attributes.md#複数nodeをまとめてベイクする)を参照してください。
続いて、範囲内の既存キーの接線typeをまとめて変更する`set_tangents()`を追加し、
`tangent_type`共通指定、node・複数nodeの一括変更、ベイク時の接線指定へ拡張しました。
続いて、接線・weight lockの範囲操作とnode / nodes単位のweighted切替を実装しました。
続いて`AnimationClip.reversed()`を追加しました。保存範囲の共通秒軸でchannelと
layer / root設定カーブを反転し、連続接線のin / out交換、step / stepnextの区間変換、
infinity交換、schema 2、元clipとの独立性と二重反転を扱います。
続いて`AnimationClip.extract(nodes=...)`を追加しました。captureではscene全体で一意なDAGを
namespace込みのshort name、同名DAGをfull pathとして保存し、階層変更への耐性と曖昧性の拒否を両立します。
抽出は旧schema 2のfull pathも一意なshort nameで選べ、指定node順、全channel、必要なlayerと祖先、
root設定、元clipとの独立性を維持します。保存名に加えてliveな`NodeOperator` / `MObject`を、
DAGでは現在のfull path完全一致、続いてshort nameの順でselectorにできます。
明示名付きpending `NodeOperator`は予約名で選択します。
名前なしpending `NodeOperator`とraw pending `MObject`は拒否し、保留中modifierを実行しません。
属性単位の抽出は保留しています。
続いて`node.keyframes.euler_filter()` / `nodes.keyframes.euler_filter([...])`を追加しました。
既存のrotate 3軸カーブだけを対象に、指定範囲の同期キーをnodeの静的`rotateOrder`でfilterします。
範囲内先頭キーをanchorとして姿勢を維持し、ベース・明示layer、全対象の事前検証、
Undo / Redo・rollbackに対応します。
続いて`node.keyframes.reduce_keys()` / `nodes.keyframes.reduce_keys([...])`を追加しました。
既存の削減コアと属性・layer選択を共有し、全対象の削減計画を完了してから1つの履歴で変更します。
同じmanagerへ先に予約したベイク結果も実行時に解決して削減します。
layer構造の管理や自動選択を追加する場合は、
ベースを既定とし、別layerを明示する現在の契約と分けて仕様を決めます。

| 候補 | 現状と、実装前に決めること |
| --- | --- |
| 移動の拡張 | 時間方向の移動、AnimationClip復元時とKeyframeManagerによる正の時間拡縮、既存キーの生値の設定・加算・拡縮は実装済み。値編集・`move_frames()`・`scale_frames()`の補間は既存キーへの重み付けのみ。合成結果を基準とする値編集等は個別に仕様化する |
| ベイクの拡張 | plug単位・node単位・複数node単位の独立時刻評価は実装済み。複数nodeでも全対象を変更前に一括samplingし、node間を含む操作全体をrollbackする。simulation・cache・dynamics向けの時系列評価は今後個別に仕様化する |
| キー削減の拡張・最適化 | 手動接線を維持する属性・明示カーブ・node・複数node操作とAnimationClipの保存チャンネル削減は実装済み。より多くのキーを削減する探索方法、大規模カーブの性能改善、TT対応、現在保守的に残すweighted区間の判定拡張が候補。接線を削減のために調整する機能は初期版の方針に含めない |
| アニメーションライブラリー向けの一括操作 | `AnimationClip`の一括保存・復元、復元に使う区間の指定、復元時刻指定、正の時間拡縮、独立した逆再生clip、node単位の部分抽出は実装済み。属性単位の部分抽出と、rig固有の属性対応・座標変換は未実装。汎用データ処理とrig固有処理の責務を分ける |
| layer操作の拡張 | ベース選択、明示指定、作成・属性登録、AnimationClipによる階層・順序・weight等の保存復元は実装済み。登録解除や階層・順序を個別編集する公開API、auto / best layerの選択は未実装。未指定のベース選択を維持し、scene変更の責務を個別に決める |
| 対応カーブ・接続の拡張 | 明示指定のTA / TL / TUは未接続・中間nodeへの出力・共有出力・時間入力接続に対応。TT詳細データ、driven key、quaternion補間、custom tangentは個別に仕様化する |
| 詳細データAPIの追加最適化 | 範囲取得、layer所属確認、通常の未lockカーブの検査を改善済み。境界補完は引き続き作業用カーブ全体へ依存する。コピー整理や作業用カーブの縮小は、形状・検証契約を維持できることを実測とテストで確かめてから行う。手順は[詳細データAPIの性能測定](testing.md#詳細データapiの性能測定)を参照 |

利用者の方針により、繰り返し領域の範囲切り出しは今後の実装候補から外します。
既存のconstant / linearの範囲外補完は維持し、cycle / cycleRelative / oscillateの
範囲外の詳細データ切り出しは引き続きエラーとします。

### 範囲内キーの接線type変更

`set_tangents(start_frame=None, end_frame=None, *, tangent_type=None,
in_tangent_type=None, out_tangent_type=None)`を追加しました。両端包含、`None`側は無制限、
両端省略は全キーです。`tangent_type`は両側の共通値で、個別指定は該当側を上書きします。
境界キーは補完せず、範囲内に実在するキーだけを変更します。片側のtypeを省略するとその側を
維持し、全接線指定省略・カーブなし・該当キーなしはno-opです。

値・時刻・breakdown・tangent / weight lock・weighted・infinityは維持し、typeに伴う
接線XYの再計算だけをMayaへ委ねます。属性・明示layer・明示TA / TL / TUカーブで同じ
対象resolverとlock / reference検査を使用し、1つの`MAnimCurveChange`として
Undo / Redo・rollbackへ参加します。既存`set_tangent()`は同じ範囲処理へ委譲します。
境界挿入、補間、lock操作、対応tangent typeの追加は行いません。
2026-09-20時点で、関連pytestはMaya 2025 / 2026 / 2027で各3,377件成功し、
3 versionの型・補完contractと`verify.cmd`も成功しています。
利用者によるMaya画面上での確認とcommit / pushも完了し、`3509264f`へ反映されています。

### キー単位のtangent / weight lock変更

属性・明示カーブには、単一キー用の
`set_tangent_lock(frame, *, tangents_locked=None, weights_locked=None)`と、範囲用の
`set_tangent_locks(start_frame=None, end_frame=None, *, tangents_locked=None,
weights_locked=None)`を追加しました。node・複数nodeには同じ範囲版を追加し、既存の
`set_tangents()`と同じ属性収集・layer選択・全対象の事前検証を使用します。

`tangents_locked`と`weights_locked`はどちらもキー単位で、in / out別の状態ではありません。
`None`は維持、両方省略はno-opです。両端包含、片側省略、全キーを扱い、境界キーや
カーブを作成しません。nonweightedカーブでもweight lockだけを保存し、カーブ全体の
`weighted`は変更しません。接線type・XY、値・時刻・breakdown・infinityも維持します。

Maya 2025で`MFnAnimCurve`のlock setter、Maya command、animCurve内部plugを実測しました。
`MAnimCurveChange`だけではlock setterのUndoが復元されないため、`keyTanLocked` /
`keyWeightLocked`配列を`MDGModifier`へ予約します。これによりModifierManagerの
Undo / Redoと途中失敗時rollbackを共通経路で扱います。

### 接線指定とnode一括操作の拡張

`set_key()` / `set_keys()` / `set_tangent()` / `set_tangents()`へ、in / out両側の共通値を
指定する`tangent_type`を追加しました。個別の`in_tangent_type` / `out_tangent_type`は
該当側だけ共通値を上書きします。単数版の接線引数もkeyword専用へ揃えました。

`node.keyframes.set_tangents()` / `nodes.keyframes.set_tangents([...])`は、ベイクと同じ
属性収集・layer選択を使い、既存カーブ・既存キーだけを1操作で変更します。通常の接線指定は
連続属性だけに適用し、bool・enum・整数系は`discrete_tangent_type`を明示した場合だけ
in / out両側を変更します。静的属性、カーブなし、該当キーなしはno-opです。

plug・node・複数nodeの各`bake()`にも同じ連続接線指定と`discrete_tangent_type`を追加しました。
未指定時は連続属性がauto / auto、離散属性がstep / stepです。接線指定は生成する
`AnimCurveData`へ含め、sampling・接続変更・復元・値検証と同じUndo / Redo・rollback単位で
適用します。生成キーはBreak Tangentsを解除した`tangents_locked=True`、
`weights_locked=False`とします。離散型判定は共通化し、enumとscalar整数系を同じ対象として扱います。

### plug入力ベイクの実装

`KeyframeManager.bake(start_frame=None, end_frame=None, *, sample_by=1.0, ...)`を追加しました。
範囲端の省略時は呼び出し時の再生範囲を捕捉し、初回実行時に対象の生入力を全時刻分
samplingしてから接続を変更します。終了端を必ず含め、負時刻・subframe・予約後のFPS変更に対応します。

内部処理は`_keyframe_bake.py`へ分離しました。既定ベースはlayer合成のinputA側、
明示layerはMayaのlayeredPlugを解決します。対象へ直接つながる非共有カーブだけを再利用し、
それ以外の入力接続を切って新しいカーブを作成します。親compound接続は対象子で分割して兄弟を維持します。
連続値は既定でauto / auto、離散値はstep / stepとし、専用引数で接線を変更できます。
範囲外はconstantとし、適用後に全サンプル値を再検査します。
接続元・接続先・layerのlock / reference検査、接続変更と全カーブ復元を同じmanagerの履歴へ含めます。
詳しい契約は[ベイクの現行仕様](attributes.md#評価済み入力をキーフレームへベイクする)、
検証範囲は[ベイクの検証](testing.md#plug入力ベイクの検証)を参照してください。

### node入力ベイクの実装

全`NodeOperator`へ`keyframes`プロパティを追加し、
`NodeKeyframeManager.bake(start_frame=None, end_frame=None, *, attributes=None,
include_channel_box=False, include_static=True, sample_by=1.0)`を公開しました。
自動収集はkeyableの対応leafを対象とし、channelBox属性は明示optionで追加します。
静的値は既定でカーブ化し、`include_static=False`でアニメーション依存のある入力へ絞ります。
明示属性では非keyable、compound、実在array要素を扱います。自動収集は未対応型・lock・
指定layerの未所属属性を除外し、明示指定では同じ状態をエラーにします。

plug版の内部処理を複数対象へ拡張し、全対象を初回実行時にsamplingしてから接続を変更します。
同じ親compound接続を共有する対象は1回の切断で処理し、対象外の兄弟だけを再接続します。
個々のカーブ復元と全サンプルの再検査を1つのModifierManager履歴へ含めるため、
途中失敗では全属性をrollbackします。指定layerの入口は`node.keyframes.anim_layer()`です。

### 複数node入力ベイクの実装

`Nodes`へ`keyframes`プロパティを追加し、
`NodesKeyframeManager.bake(nodes, start_frame=None, end_frame=None, *, attributes=None,
include_channel_box=False, include_static=True, sample_by=1.0)`を公開しました。
node列はNodeOperator / MObject / node名を受け取り、空列と重複nodeを拒否します。

自動収集はnodeごとに行い、対象0件のnodeをスキップします。明示属性は存在するnodeだけへ
適用し、全nodeで一度も見つからない名前をエラーにします。存在する未対応・lock・layer未所属属性は
単一node版と同じくエラーです。指定layerは`nodes.keyframes.anim_layer()`で全nodeへ共通適用します。

全nodeのtargetを1つの`queue_bakes()`へ渡すため、上流・下流nodeを同時指定しても
全サンプル取得後まで接続を変更しません。検証失敗を含む途中失敗では全nodeをrollbackし、
Undo / Redoも1単位です。総サンプル数はフレーム数と対象leaf数の積で数え、既存の
10,000,001点上限を全操作へ適用します。時系列simulationとworld-space bakeは対象外です。

### キーフレーム移動の実装

`move_frame(frame, *, offset=None, to=None, insert_missing=False)`と
`move_frames(start_frame=None, end_frame=None, *, offset=None, to_start=None,
to_end=None, interpolate_start=None, interpolate_end=None, interpolation="smoothstep",
insert_missing=False)`を共通の`_KeyframeOperations`へ追加しました。
対象は位置引数、移動方法は必ず1つのkeyword引数で指定します。
明示した開始・終了時刻を絶対移動の基準とし、基準側がNoneなら対象キーの端を使います。
移動先の対象外キーを置換し、途中のキーや移動対象同士は失いません。
`insert_missing=True`だけが明示境界を補い、空カーブや移動量0では挿入しません。
詳しい契約は[移動の現行仕様](attributes.md#キーを時間方向へ移動する)を参照してください。

補間を指定すると、補間区間の既存キーも対象にし、移動前の時刻から求めた影響度で
移動量を重み付けします。絶対移動の基準は補間区間を含める前の元範囲です。
影響度0の既存キーは移動せず、対象キー同士の衝突・順序逆転はエラーにします。
対象外キーとの同時刻衝突は従来どおり上書きします。`insert_missing=True`だけが
明示した最大4境界を補い、イーズを再現するための追加キー・接線調整は行いません。

内部処理は`_keyframe_move.py`へ分離しています。既存resolverで対象・lock / referenceを
初回実行時に検査し、1つの`MAnimCurveChange`で挿入から移動まで記録します。
順序維持可能なら正方向は後ろから、負方向は前から`setInput()`を適用します。
Maya 2025 / 2026 / 2027の`setInput()`は隣接キーを越えると直前で止まる場合があるため、
時刻を事前計算し、適用後も確認します。上書き・飛び越しでは移動対象と衝突キーだけを
削除し、元情報を移動先へ復元します。影響度0のキーは再挿入しません。
TA / TL / TUはbulk挿入で短いweighted接線やnonweightedの生XYを維持します。
TTは値をMTime、接線を角度・重みで保存し、再挿入で再現できないweighted接線はrollbackします。
公開の詳細データAPIの境界補完・nonweighted XY変換・全置換は経由しません。
部分移動のauto等の接線再計算は許可し、境界挿入時はMayaの接線調整を維持します。

検証範囲は[移動テスト](testing.md#キーフレーム移動の検証)を参照してください。

### キー削減の実装

`reduce_keys(start_frame=None, end_frame=None, *, tolerance, preserve_breakdowns=True)`を
共通の`_KeyframeOperations`へ追加しました。範囲・単位の指定は移動APIと整合させ、
値の許容誤差はdegree / cm / unitlessで明示します。TA / TL / TUに対応します。
仕様は[キー削減](attributes.md#手動接線を維持してキーを削減する)を参照してください。

`_keyframe_reduce.py`は未登録の作業用カーブで削除を試し、元カーブとの誤差、
手動接線・lock等の保持、範囲外形状とlinear infinityの傾きを検査します。
`_keyframe_error.py`はBezier区間の分割と誤差上界を扱います。
weightedの制御点時刻が逆転する区間や分割上限で未判定の候補は残します。
実カーブにはキー削除だけを適用し、削除後の再検査・Undo / Redo・rollbackに対応します。
キー数の最小化やMaya標準フィルタとの結果一致を保証するものではありません。

続いて同じ名前を`NodeKeyframeManager` / `NodesKeyframeManager`へ追加しました。
属性・channelBox・layer・上流カーブの選択は既存のnode一括操作と共通です。
複数カーブでは先に全削減計画を作成し、成功後に1つの`MAnimCurveChange`へ削除を記録します。
同じmanagerに先行するベイク・キー作成は実行時に解決し、後半カーブの計画失敗や後続処理の
失敗では操作全体をrollbackします。

### キーフレーム時間拡縮の実装

`scale_frames()`を両Manager共通の操作へ追加しました。
倍率・長さと配置の組み合わせ、移動先の両端指定、`insert_missing=False`を既定とする境界補完を扱います。
明示した元境界を基準にし、`None`側は対象キーの端を使います。
`pivot`で拡縮の基準時刻を変更でき、指定した基準で主区間の配置先も求めます。
`mode="replace_range"`を既定にし、変換後の基準区間内を置換します。`merge`は同時刻だけを上書きします。
いずれも元キーは移動し、重なった元区間・配置先も全対象を確保してから編集します。
補間指定では対象を前後へ広げ、元時刻の影響度で時刻と接線Xを変換します。
基準と置換範囲は主区間だけで決め、補間端点を含む対象キー同士の衝突・順序逆転は拒否します。

`_keyframe_scale.py`が引数捕捉、実行時の配置計画、削除・接線Xの拡縮・再挿入を扱います。
`_keyframe_move.py`の境界挿入・キー情報捕捉・復元helperを共有します。
TA / TL / TUは`addKeysWithTangents()`を使い、`setTangent()`で短いweighted接線が
下限補正されることを避けます。bulk挿入の種類・lock配列と、その後の種類設定を組み合わせ、
初回とRedoの両方でメタデータを維持します。TTの表現限界は検査し、再現できなければrollbackします。
仕様は[時間拡縮](attributes.md#キーを時間方向へ拡縮する)、検証は[時間拡縮テスト](testing.md#キーフレーム時間拡縮の検証)を参照してください。

### 新しいチャットでの開始手順

1. repository rootで`git status --short`と直近のcommitを確認し、`AGENTS.md`を読む。
   範囲内キーの接線・lock変更、node / nodes一括接線変更、ベイク時の接線指定と
   Break Tangents修正まで利用者確認・push済み（`be068260`）。
   既存変更を戻さず、利用者の許可なくcommit / pushしない。
2. この節の完了範囲・維持する契約・キーフレーム移動と時間拡縮の仕様を読み、
   `attributes.md`で現行API、`testing.md`で関連テストと直近の検証実績を確認する。
3. 以下の実装とテストを起点に、利用者が指定した次の機能を調査する。
   移動・キー削減・AnimationClip・時間拡縮・値編集を未実装として再開発しない。
   接線・weight lockの範囲操作とnode / nodes単位のweighted切替は実装済み。
   AnimationClipの逆再生とNodeOperator / MObject / 保存名によるnode単位の部分抽出、
   node / nodes単位のEuler filter・キー削減も実装済み。
   属性単位の抽出は保留し、次の項目は利用者確認後に決める。
   過去の実装・検証記録も本文では現行API名で表記する。
4. 実装時は関連テスト、型・IDE補完、ドキュメント更新まで進め、
   `AGENTS.md`に従って最後に`scripts/verify.cmd`を実行する。

### 実装を引き継ぐ際の参照先

- `python/bd_util/maya/node/operator/attr/_keyframe_euler.py`: rotate 3軸の既存カーブ、同期キー、
  静的`rotateOrder`を事前検証し、`MEulerRotation.closestSolution()`と`MAnimCurveChange`で
  filter・Undo / Redo・rollbackを行う。node入口は`operator/node/_keyframes.py`、
  回帰テストは`test_node_keyframe_euler.py`。
- `python/bd_util/maya/node/_animation_clip_range.py`: 復元用コピーの使用区間を保存時間単位で検証し、
  全属性とlayer / root設定を切り出す。`_keyframe_snapshot.clip_curve_data()`で未登録カーブを評価し、
  既存の境界補完処理を共有する。`_animation_clip_restore.py`で時間変換の前に適用する。
  `test_animation_clip_range.py`とMPxCommandの範囲指定が回帰テスト。
- `python/bd_util/maya/node/_animation_clip_reduce.py`: 保存時間単位による範囲と全チャンネルの処理。
  `_keyframe_snapshot.reduce_curve_data()`で未登録カーブへ復元し、`_keyframe_reduce.reduce_curve()`を共有する。
  削減後の接線情報を再取得して元のframe・valueと時間単位を維持する。`test_animation_clip_reduce.py`が回帰テスト。
- `python/bd_util/maya/node/operator/attr/keyframe.py`: 両Managerの共通操作、anim_layerの入口とキー設定の経路選択。
- 同階層の`_keyframe_move.py`: 移動引数の検証・捕捉、実行時の対象範囲と移動先の計画、
  境界挿入、setInputと削除・再挿入の経路。拡縮・値編集とも復元helperを共有する。
  `test_keyframe_move.py` / `test_keyframe_move_interpolation.py`が専用の回帰テスト。
- 同階層の`_keyframe_influence.py`: 移動・時間拡縮・値編集で共有する補間境界の検証・影響度計算。
- 同階層の`_keyframe_scale.py`: 時間拡縮の配置計画と部分置き換え、接線の変換・再挿入。
  `test_keyframe_scale.py` / `test_keyframe_scale_interpolation.py` / `test_keyframe_scale_pivot.py`と
  MPxCommandの専用fixtureが履歴を含む回帰テスト。
- 同階層の`_keyframe_value.py`: 生値の設定・加算・拡縮、補間ウェイト、nonweighted接線の正規化。
  `_keyframe_move.restore_keys()`を再利用する。`test_keyframe_value.py`が専用の回帰テスト。
- 同階層の`_keyframe_command.py`: native setKeyframeの予約、対象layerとUI単位の実行時解決。
  通常のキー設定と、詳細復元時のlayerカーブ作成で共有する。後者だけnoResolveとinsertBlend=Falseを使う。
- `python/bd_util/maya/node/operator/node/dg/_anim_layer.py`: layer作成と登録の共通mixin。
  作成待ちMObjectを保つため、rootとlayerはMDGModifierで作成し、rootのoverrideをTrueにする。
  native animLayerでparentと所属接続を構築し、登録後の照会は別のqueue_dg_modifierで行う。
  照会だけのpythonCommandToExecuteはMayaで失敗するため使用しない。
- `python/bd_util/maya/node/operator/attr/_keyframe_target.py`: チャンネル・既定ベース・指定layer・明示指定resolverと編集時のlock / reference検査。
  既定ベースはsceneのrootを解決し、明示layerは元のplugとMObjectを保持する。
  対象カーブはMayaの属性とlayerの対応から解決する。
  所属確認は全属性名の列挙ではなく、layeredPlugで対象plugのlayer入力を照会する。
  lockのない配列・compoundはMPlug.isFreeToChangeで子孫を検査し、必要な場合だけ個別に巡回する。
  BaseAnimationのfindCurveForPlugは通常の非所属属性を返さないため、チャンネル解決へ補完する。
  通常キー設定のAPI高速経路判定は、別の厳格な直接接続helperに維持する。
  作成待ちnodeは`MObjectHandle.object()`がnullになるため、明示対象は元のMObjectも保持する。
- 同階層の`_keyframe_discovery.py`: DG依存関係の候補列挙。iteratorには探索終了まで
  生存するroot MPlugを渡す。未接続出力の依存入力補完と、array indexの区別にも注意する。
  `curve_objects()`をsamplingの再評価準備にも使用する。samplingだけはカーブの入力側へ進み、
  未接続のカーブ出力ではinputを探索起点へ補完する。公開find_anim_curvesの停止条件は変えない。
- 同階層の`define/std/at/scalar/_base.py`: sample_valuesの入力捕捉、上流カーブからの
  再評価伝播、MDGContext切替と公開単位での読み取り。関連回帰テストは
  `test_scalar_sampling.py`と`test_scalar_sampling_layers.py`。
- 同階層の`keyframe_data.py`: KeyData / AnimCurveDataの型、単位表現、検証、JSON変換。
- 同階層の`_keyframe_snapshot.py`: 詳細データの型制約、snapshot、復元、境界補完。
  復元先の作成準備とMAnimCurveChangeによる復元を順に予約する。layerで新規作成した場合は
  API編集前に作成用キーを除去し、途中失敗では接続・ノードの作成までrollbackする。
  境界補完では`MDGModifier.createNode()`で確保した作業用カーブを使い、`doIt()`せずに
  Mayaの挿入処理を適用する。元カーブへの一時挿入とUndoに置き換えない。
  作業用nodeの解放と、API編集で変わるscene modified flagの復元を成功・例外時とも維持する。
- `tests/maya/node/operator/attr/test_keyframe_clip.py` / `test_keyframe_data.py`:
  形状・単位・履歴・副作用・例外時の解放を確認する主なテスト。
  MPxCommand連携は`tests/maya/mpx_cmd/test_command.py`、補完は`tests/typecheck/node_operator_contract.py`。
- `test_keyframe_undo.py`: API編集の予約実行・Undo / Redoと、途中失敗時rollback。
  キーフレーム移動の履歴検証も、この既存パターンを参照する。
- `test_keyframe_restore_creation.py`: 未作成のベース・指定layerカーブへの詳細復元、
  内部の作成用キー除去、既存キーを残す部分適用、同一batchの作成・登録・復元とrollback。
- `test_keyframe_target.py`: 対象選択、未対応接続の拒否、実行時再解決と失敗時rollback。
- `test_keyframe_channel.py`: pairBlend全6軸、currentDriver、単位変換、blendWeightedの入力順、
  空カーブ・入れ子・保留中接続、非対象カーブと中間ノードの保持、取得・編集・復元と履歴。
- `test_keyframe_anim_layer.py`: 指定layerとBaseAnimation、合成値と生カーブ値、未作成・空カーブ、
  改名・所属変更・lock、別layerの保持、予約実行と履歴。型補完はnode_operator_contract.py。
- `tests/maya/node/operator/node/dg/test_anim_layer.py`: 作成・登録・キー設定の一括実行、native比較、
  入力型・compound・配列・非keyable、ノード自身の属性列挙、重複・同一性・lock / reference、rollback。
- `test_keyframe_default_layer.py`: 未指定時のベース選択、選択layer・preferred・keying modeからの独立、
  rootの改名・予約後の作成、別layerの保持、ベースの取得・編集・復元と履歴。
- `test_curve_keyframe.py`: 明示カーブの単位、node同一性、共有・入力接続、layer lock、履歴、詳細データ。
- `test_keyframe_discovery.py`: 全8型、型filter、複数経路・weight・constraint、queryの副作用、
  候補選択後の明示編集と履歴。探索はlayer所属や現在値への寄与を判定するAPIではない。
- `python/bd_util/_dev/maya/benchmark_keyframe_data.py`: 現行コードまたは指定commitの詳細データ性能測定。

直近の自動検証と利用者による動作確認は、
[引き継ぎ時点の検証](testing.md#keyframemanagerの引き継ぎ時点の検証)を参照してください。
新しい変更の最終検証は、過去の結果で代用せずrepositoryの現行`AGENTS.md`に従って実行します。

## 完了済み: DAG / shape API roadmap

以下の順序で、DAG階層とshape作成APIを整備しました。

### 1. DAG path と instancing の方針（初期対応完了）

子孫・先祖 traversal の実装前に、`MDagPath` と instanced DAG node の
扱いを決めました。

現在の `NodeOperator` は `MObject` を中心に扱うため、同じ node が複数の
DAG path を持つ場合に、どの path の階層を返すかが曖昧になります。

初期版では `MDagPath.getAPathTo()` で path を保持し、複数 path が存在する
node の単一 `parent` 取得や親変更は `RuntimeError` にします。すべての直接親は
`parents` から取得できます。将来 path を明示的に選択する API が必要になった場合は、
`ExistingNode` の入力と保持方法を拡張します。

### 2. DAG 階層 traversal（初期対応完了）

DAG path / instancing の方針確定後、次の階層取得APIを追加しました。

traversal 中に transform 派生 node を具体型へ解決できない問題を避けるため、
先に transform 派生 NodeOperator の coverage を段階的に整備します。Maya 2025で
登録された transform 派生134種のうち、manipulator等82種を既存規則で除外し、
残る52種はinstanceを作らない静的query、コード生成、構文確認に成功しています。
最初の代表型 `ikHandle` / `ikEffector` に続き、constraint 系14種を追加しました。
さらにfield / emitter系11種、dynamics / deformer周辺5種、HIK系5種、
scene / utility系6種、VarGroup系5種、特殊transform 2種を追加し、
`transform` / `joint` を含む52種すべてを具体型へ解決できます。
さらにtransformでもshapeでもない `unknownDag` も具体型へ解決できます。
DAG具体型の事前整備を完了してからtraversalを実装しました。

- 直接の子。
- 直接親から root 方向へ辿る先祖。
- depth-first で辿る子孫。

第一段階として`children()`を追加しました。TransformとShapeを区別せず、
Mayaのchild index順で直接の子だけを返します。自分自身、world、孫は含めません。
戻り値は同じ`ModifierManager`を共有する具体的な`DAG`系`NodeOperator`です。
結果はcacheせず、未実行の`MDagModifier`の変更は含めません。instanced childは
MObject中心で取得し、保持pathは`MDagPath.getAPathTo()`が選ぶ現行方針を維持します。

第二段階として`ancestors()`を追加しました。保持中の`MDagPath.getAPathTo()`の
1つのpathを基準に、直接の親からroot方向へ列挙します。自分自身とworldは含めず、
`children()`と同じく具体型、`ModifierManager`共有、都度取得、実行済みscene状態の
契約を維持します。

第三段階として`descendants()`を追加しました。各階層のchild index順を維持した
depth-first pre-orderで、すべての子孫を列挙します。自分自身とworldは含めません。
instanced subtreeはMaya標準traversalと同様にDAG pathごとに再訪するため、同じ
`MObject`が複数回現れる場合があります。

これで`children()` / `ancestors()` / `descendants()`の初期DAG traversalは完了です。
Shape / type filterなどの利便APIも、後述のDAG traversal拡張として実装しました。
pathを明示的に選択するAPIは、必要な利用例が揃った段階で検討します。

### 3. 親 Transform 必須の shape 作成（段階公開完了）

最初の shape 作成 API は、親 `Transform` を必須として公開しました。

```python
mesh = nodes.create.mesh(
    name="meshShape",
    parent=transform,
)
```

親を指定せず `MDagModifier.createNode()` で shape type を作成すると、
Maya が transform を自動生成し、返される `MObject` も transform になる
場合があります。そのため、既存の DG / transform 作成 API と同じ形で
shape package 全体を無条件に公開しません。

作成可能なことを確認できた shape type から限定して公開します。第一サンプルとして
`camera` / `locator` / `mesh` / `nurbsCurve` / `nurbsSurface` の戻り値型、
undo / redo、命名、親との `ModifierManager` 共有を検証済みです。

第二段階として、Maya 標準 light shape の `ambientLight` / `areaLight` /
`directionalLight` / `pointLight` / `spotLight` / `volumeLight` も同じ条件で検証し、
`nodes.create` へ公開済みです。MtoA ロード時は、生成済みの Arnold attribute も
利用できます。

第三段階として、MtoA をロードした Maya 上で Arnold 固有 light shape の
`aiAreaLight` / `aiLightPortal` / `aiMeshLight` / `aiPhotometricLight` /
`aiSkyDomeLight` を検証し、`nodes.create` へ公開済みです。

第四段階として、残る Arnold 固有 shape の `aiCurveCollector` /
`aiLightBlocker` / `aiStandIn` / `aiVolume` も raw shape としての作成、命名、
親子関係、undo / redo を検証し、`nodes.create` へ公開済みです。ファイル指定や
geometry・shader 接続などの用途別初期化は、高レベル API の候補として分離します。

第五段階として、Maya 標準 geometry shape の `baseLattice` / `bezierCurve` /
`lattice` / `subdiv` を個別のシーンで検証し、`nodes.create` へ公開済みです。
geometry データや lattice 分割数などの内容初期化は raw shape 作成と分離します。

第六段階として、Maya 標準 primitive shape の `implicitBox` / `implicitCone` /
`implicitSphere` / `renderBox` / `renderCone` / `renderRect` / `renderSphere` を
個別のシーンで検証し、`nodes.create` へ公開済みです。size や radius などの
値設定は raw shape 作成と分離します。

第七段階として、Maya 標準の計測・注釈 shape `angleDimension` /
`annotationShape` / `arcLengthDimension` / `distanceDimShape` / `paramDimension` を
個別のシーンで検証し、`nodes.create` へ公開済みです。計測点、表示テキスト、
NURBS geometry との接続などの用途別初期化は raw shape 作成と分離します。

第八段階として、Maya 標準の補助 locator・marker・handle shape `clusterHandle` /
`directedDisc` / `dropoffLocator` / `hikFloorContactMarker` / `motionTrailShape` /
`orientationMarker` / `positionMarker` / `softModHandle` を個別のシーンで検証し、
`nodes.create` へ公開済みです。deformer、motion path、HIK などとの接続や
用途別初期化は raw shape 作成と分離します。`SphereLocator` は Maya 2025 の
標準状態で `invalid node type` となるため、未公開のまま維持します。

第九段階として、Maya 標準の非線形 deformer 表示 shape `deformBend` /
`deformFlare` / `deformSine` / `deformSquash` / `deformTwist` / `deformWave` を
個別のシーンで検証し、`nodes.create` へ公開済みです。対応する deformer node
との接続や `deformerData` の初期化は raw shape 作成と分離します。

第十段階として、Maya 標準の deformation connection helper shape
`clusterFlexorShape` / `flexorShape` / `geoConnectable` を個別のシーンで検証し、
`nodes.create` へ公開済みです。driver、flexor、surface geometry などとの接続は
raw shape 作成と分離します。

第十一段階として、Maya 標準のシーン表示・カメラ補助 shape `imagePlane` /
`sketchPlane` / `snapshotShape` / `stereoRigCamera` を個別のシーンで検証し、
`nodes.create` へ公開済みです。画像ファイル、描画内容、snapshot frame、
stereo camera 接続などの用途別初期化は raw shape 作成と分離します。

第十二段階として、Maya 標準のレンダリング・環境表現補助 shape `environmentFog` /
`fluidTexture2D` / `fluidTexture3D` / `heightField` を個別のシーンで検証し、
`nodes.create` へ公開済みです。camera、fluid data、texture、displacement などとの
接続や用途別初期化は raw shape 作成と分離します。

第十三段階として、Maya 標準の描画・Paint Effects 補助 shape `greasePlane` /
`greasePlaneRenderShape` / `lineModifier` / `pfxHair` / `pfxToon` / `stroke` を
個別のシーンで検証し、`nodes.create` へ公開済みです。image、brush、hair / toon
input、render geometry、line modifier などの接続や用途別初期化は raw shape 作成と
分離します。

第十四段階として、Maya 標準の hair・dynamics 補助 shape `dynamicConstraint` /
`dynHolder` / `follicle` / `hairConstraint` / `hairSystem` / `spring` を個別のシーンで
検証し、`nodes.create` へ公開済みです。simulation設定、constraint component、
hair curve、surface、solverなどとの接続や用途別初期化は raw shape 作成と分離します。

第十五段階として、Maya 標準の simulation body shape `fluidShape` / `nCloth` /
`nParticle` / `nRigid` / `particle` / `rigidBody` を個別のシーンで検証し、
`nodes.create` へ公開済みです。geometry・particle data、initial state、nucleus・
rigid solver などとの接続や用途別初期化は raw shape 作成と分離します。

第十六段階として、Maya 標準の `ufeProxyCameraShape` を標準起動状態で検証し、
`nodes.create` へ公開済みです。UFE scene item や camera との関連付けなどの用途別初期化は
raw shape 作成と分離します。残る `SphereLocator` は node type 自体が登録されておらず、
`MDagModifier.createNode()` が `invalid node type` となるため非公開のまま維持します。

全 shape class の生成後も、`nodes.create` には作成検証済み type だけを
明示的に opt-in します。生成済み concrete shape 81種のうち、Maya 2025 で
作成可能な80種を公開済みです。

### 4. transform と shape の一括作成（対応完了）

親 Transform 必須の raw shape 作成とは別に、次の一括作成 API を公開済みです。

```python
transform, mesh = nodes.create.with_transform.mesh(name="mesh")
mod.do_it_dag()
```

`name` は transform 名、`shape_name` は shape 名です。`shape_name` の省略時は
`name` に `Shape` を加えた名前を使います。戻り値は `(Transform, concrete Shape)`
とし、両方を同じ `ModifierManager` に積みます。作成する transform の親は
`parent` で指定できます。

検証済み80種すべてについて具体 shape 型の補完を提供し、raw 作成は引き続き
`nodes.create.<nodeType>(parent=transform)` として区別します。

同じ `nodes.create.<nodeType>()` の `parent` の有無で切り替える方式は採用しません。
その方式では、指定漏れによる意図しない Transform 作成、条件による戻り値型の変化、
`name` と `parent` の意味の変化が生じるためです。raw API は常に Shape のみ、
`with_transform` API は常に Transform と Shape の両方を作成する契約に固定します。

`polyCube` のように history node も生成する primitive 作成は、raw shape
作成とは別の高レベル API として扱います。

ここまでを shape 系 NodeOperator と shape 作成 API の一区切りとします。
その後、DAG path / instancing方針と初期DAG traversalまで実装し、当初予定した
DAG / shape API roadmapは完了しました。

## 完了済み: DAG traversal 拡張

初期traversalの契約を維持したまま、次の利便APIを実装しました。ここに記載する
引数名、戻り値型、探索規則は、Maya 2025の実挙動、IDE補完、Pyright contractを
確認して確定した現行仕様です。

共通方針です。

- filterは返す結果だけに適用し、対象外nodeの子孫も探索する。filterを理由に
  subtreeをpruneしない。
- 結果はcacheせず、実行済みscene状態を都度取得する。
- 自分自身とworldは含めない。
- 結果はscene上のnode typeに対応する具体的な`DAG`系`NodeOperator`とし、
  元nodeと同じ`ModifierManager`を共有する。
- instancingは現在のMObject中心と`MDagPath.getAPathTo()`の方針を維持する。

### 1. Shape filter

`children()` / `descendants()`へ`include_shapes: bool = True`を追加しました。
`False`ではMaya APIの`MFn.kShape`に一致するnodeを結果から除外します。Shapeだけへの
限定はclass-based type filterへ`Shape`を渡すことで表現し、`only` / `exclude` / `all`の
三状態を単一optionへ詰め込みません。type filterと併用した場合はAND条件です。

Shape filterも返す結果だけに適用し、`descendants()`の探索範囲は変更しません。
戻り値型は`filter_type`の有無に従う従来のPyright contractを維持します。

Maya 2025ではShapeを親にnodeを作成すると、通常childではなく
`shape->|child`形式のunderworld pathになります。`MFnDagNode(shape).childCount()`には
列挙されず、pathには現行`ExistingNode`未対応の暗黙`dagNode`も含まれるため、
underworld traversalは今回の対象外とします。Shapeが祖先になるのはこの対象外pathの
場合であるため、`ancestors()`には`include_shapes`を追加しません。

### 2. Type filter

Maya node type名の文字列ではなく、`Transform` / `Joint` / `Shape` / `Mesh`のような
`DAG`系Python classを受け取ります。`isinstance()`に基づくfilterなら
継承関係を利用でき、`type[T]`と組み合わせて戻り値を`tuple[T, ...]`として表現できます。

filter実装の事前整備として、生成済みNodeOperator classを
`nodes.types.Transform` / `nodes.types.Locator` のように参照できるAPIを追加しました。
PascalCase属性は具体的な`type[T]`をstubで公開し、実classはアクセス時に遅延importします。
`NodeOperator` / `DAG` / `Shape` / `BaseGeometryVarGroup` の基底classも参照できます。
動的なMaya node type名には `nodes.types.resolve("locator")` を使用します。

第一段階として、`children(filter_type=...)`へ単一のDAG系Python classを渡せるように
しました。filterは`isinstance()`に基づくため、`Transform`を指定すると`Joint`などの
派生型も含まれます。引数省略時と`None`は従来どおり`tuple[DAG, ...]`、
`type[T]`指定時は`tuple[T, ...]`としてPyright contractを固定しています。

第二段階として、同じclass filterを`descendants(filter_type=...)`へ拡張しました。
filterは結果だけに適用し、対象外nodeのsubtreeをpruneしません。depth-first pre-order、
instanced subtreeのpathごとの再訪、具体型と`ModifierManager`共有、実行済みscene状態を
都度取得する契約を維持します。

第三段階として、`children()` / `descendants()`へ`include_subclasses: bool = True`を
追加しました。初期値では従来どおり`isinstance()`で派生型を含め、`False`では
`type(node) is filter_type`による完全一致に切り替えます。探索範囲と列挙順は変えず、
`filter_type`なしの`False`は意味を持たないため拒否します。

第四段階として、`ancestors()`へ同じ型filterと完全一致optionを拡張しました。
保持中pathを直接親からrootまで辿る規則は維持し、filterは結果だけに適用します。
これで`children()` / `ancestors()` / `descendants()`のclass-based type filterは
同じ引数とPyright contractで利用できます。

filter対象外nodeも探索経路としては残します。例えば`Mesh`だけを要求した場合も、
途中の`Transform`で探索を止めません。Maya node type文字列は、実際の用途が必要に
なった段階で別optionとして検討します。

### 3. child indexを固定した末端までのchain

`descendant_chain(child_index: int = 0)`を追加しました。全子孫を列挙する
`descendants()`へmodeを追加せず、探索規則が異なる独立メソッドとしています。
各階層で同じchild indexだけを選び、そのindexの子が存在しない時点で終了します。
別indexへのfallbackは行わず、自分自身とworldは含めません。

結果はscene上のnode typeに対応する具体的な`DAG`系`NodeOperator`で、元nodeと同じ
`ModifierManager`を共有します。結果はcacheせず、未実行の`MDagModifier`変更は
`do_it_dag()`まで含めません。`child_index`は0以上のintとし、boolなどの非intと負数を
区別して拒否します。

### 4. 指定したDAGまでの範囲

第一段階として、`ancestors(until=...)`を追加しました。直接親から境界nodeまでを
inclusiveに探索し、指定したDAGが保持中path上に存在しない場合は`None`を返します。
自分自身は探索対象に含めないため、`until=self`も`None`です。

比較はPython instanceやnode名ではなく`MObject` identityを使い、別の`Nodes`や
`ModifierManager`から取得した同じscene nodeも境界として利用できます。instanced nodeは
保持中の1つのpathだけを対象とし、別pathに境界が存在しても`None`とします。未実行の
`MDagModifier`変更は`do_it_dag()`まで認識しません。

境界検出はtype filterから独立させます。境界がfilterに一致しない場合もそこで探索を
終了しますが、その境界は結果へ含めません。境界発見後の結果が0件なら空tuple、境界が
見つからなければ`None`です。引数省略時と`None`は従来の`tuple[T, ...]`、DAG指定時は
`tuple[T, ...] | None`になるoverloadをPyright contractで固定しました。

第二段階として、`descendant_chain(until=...)`へ同じ境界契約を拡張しました。各階層で
指定したchild indexだけを選ぶ既存規則を維持し、その固定chain上で境界を発見した場合だけ
境界までをinclusiveに返します。境界が別indexの兄弟や別subtreeにある場合、別方向へは
探索せず`None`を返します。

比較は`MObject` identityを使うため、別の`Nodes`や`ModifierManager`から取得した同じscene
nodeも指定できます。自分自身はchainの対象外なので`until=self`は`None`です。未実行の
`MDagModifier`変更は`do_it_dag()`まで含めず、引数省略時と`None`は従来の
`tuple[DAG, ...]`、DAG指定時は`tuple[DAG, ...] | None`となるPyright contractを固定しました。

これで当初予定したDAG traversal拡張のShape filter、class-based type filter、完全一致option、
固定child index chain、祖先・chainの境界指定は完了です。

## 将来の拡張候補

### Joint chain単位の姿勢設定

単一の`Transform` / `Joint`に対する値設定、姿勢マッチ、エイム、直接子エイム、軸リマップ
までは完了しています。現時点で単一nodeの薄いaliasは増やさず、複数階層の反復処理を
一貫した規則でまとめる必要が生じた場合に、Joint chain専用APIを検討します。

chain APIを追加する場合は、既存の単一node APIを計算単位として、次の境界を先に
固定します。

- `aim_axis`と`up_axis`はchain全体のlocal軸規約とする。非rootでは、明示指定がなければ
  `parent_up_vector=up_axis`として親の同じlocal軸方向を伝播する。
- rootだけはworldまたは実効親空間のアップ方向／ターゲットを上書きできるようにする。
  rootの規定値を決める際は、world固定か実効親空間かを引数名とともに明示する。
- branchの選択はShapeを除外した直接のTransform系子indexとする。Shapeを含む生のDAG
  indexを各階層で使う`descendant_chain()`とは別の契約として扱い、暗黙に流用しない。
- 選択した子以外を含む全直接子のworld姿勢・位置を維持し、Joint子の補償先は
  `jointOrient`を既定候補として、アニメーション用`rotate`を汚さない。
- エンドJointは既定で親軸へ合わせる。全回転属性の無条件なゼロ化とは区別し、対象の
  回転属性だけで合成ローカル回転を単位回転にする現行仕様を維持する。
- 親空間アップと補償後の子位置は、直前の階層で確定したscene状態に依存する。
  一括APIは階層ごとの`do_it_dg()`相当の評価とModifierManager履歴を明示的に管理し、
  未実行modifierの値を読めるように見せない。
- アップ方向とエイム方向が平行になる特異点では、現行どおりエラーを基本とする。
  previous frameやchain平面を使うfallbackが必要なら、暗黙処理ではなく独立optionとして
  仕様化する。

このchain APIは、実際のrig構築側で反復コードとroot／branch／pole処理の利用例が
集まってから追加します。現時点では、単一node APIを階層ごとに呼び、依存する操作間で
`mod.do_it_dg()`を実行する方法を正式な構成要素とします。

### Transform / Joint マッチの拡張境界

現行の位置・姿勢マッチは、非instanced DAGの評価済みscene状態を対象とする
初期仕様まで完了しています。今後機能を広げる場合も、既存メソッドの意味を
暗黙に変えず、次の境界を維持します。

- instanced DAG対応は、src / dstのDAG pathを利用者が明示できるAPIとセットで
  検討する。`MObject`から自動選択したpathへ黙ってマッチしない。
- 姿勢マッチ時のDAG原点補償は、現行メソッドへ暗黙に追加しない。必要になった場合は
  `translate`または`rotatePivotTranslate`のどちらで吸収するか、lock・入力接続、
  undo / redoの単位を含めた明示的なopt-in APIとして設計する。
- 姿勢の部分軸マッチを追加する場合は、Euler成分の単純な置換として扱わない。
  基準空間、回転積、特異点付近の解、残す姿勢成分を先に定義してから別機能として
  追加する。
- 未実行modifierを暗黙評価する仕組みは追加しない。複数のマッチ結果が依存する場合は、
  現行どおり操作間で`do_it_dg()`または`do_it_dag()`を実行する。

### compound 専用値型の演算（第一段階完了）

浮動小数点のnumeric値型である`Double2` / `Double3` / `Double4`、
`Float2` / `Float3`には、次の基本演算を追加しました。

- 同じ具体型同士の加算・減算
- `int` / `float` scalarとの乗算、scalarを左辺にした乗算、scalarによる除算
- 符号反転
- 元の値を変更せず、同じ具体型の新しい値を返す

要素積、内積、行列との演算、異なる型同士の暗黙変換は定義していません。
`bool`もscalarとして受け取りません。unit値型、整数値型、`Quat`には共通基底から
演算を波及させず、用途ごとに演算の意味を確定します。Quaternion固有の演算は
`Quat`へ実装済みです。

今後、要素積や内積が必要になった場合は、`*`へ複数の意味を持たせず、用途を表す
named methodとして検討します。unit値型や整数値型も、戻り値の次元・単位・丸め・
overflowの契約を先に決めてから個別に追加します。

### matrix plugの成分アクセス

matrix plugの主な値取得経路は、型やsnapshotの境界が明確な`get()`に統一します。

```python
tm = matrix_plug.get()
translate = tm.translate
```

現在、`DataMatrixPlugOperator`は`translate` / `rotate` / `get_rotate()` /
`scale` / `shear` / `quat`の委譲APIも持ちますが、`MatrixPlugOperator`は
`get()`だけを提供します。将来この差を整理する場合は、利用例を確認したうえで、
`MatrixPlugOperator`にも委譲APIを追加するか、両方を`get()`中心へ集約するかを
破壊的変更が可能なminor releaseで判断します。

委譲APIを維持・拡張する場合も、戻り値型、単位、未設定時の`ValueError`、
アクセスごとに新しいsnapshotを取得する評価規則は`TransformMatrix`と揃えます。

### connected plug の汎用解決

現在のconnection queryは、`ExistingNode`で型を解決でき、対象attributeが
`NodeOperator` / `AttributeField`に定義されているplugを`PlugOperator`として返します。
この範囲に含まれない未知のplug-in node typeやruntime extra attributeにも対応する場合は、
OpenMayaの`MObject` / `MPlug`から汎用wrapperへ解決する内部経路を追加する候補があります。

ただし、未知のattributeから専用の具象`PlugOperator`を常に復元できるとは限りません。
汎用fallbackを設ける場合は、次を先に決めます。

- 「接続なし」と「接続はあるがwrapperへ未対応」を区別し、未対応を黙って`None`や空tupleにしない。
- `cmds`へ戻さずOpenMayaで解決し、照会元の`ModifierManager`を共有する。
- 既存nodeを変更しない`auto_add_attr=False`の原則を維持する。
- scalar / compound / multi / message / typed attributeと未知のplug-in nodeをtest対象にする。
- public APIの戻り値型とIDE補完を、汎用fallbackの責務に合わせて更新する。

中間nodeを透過するconnection traversalはこの汎用解決とは別の機能です。
追加する場合も、`MPlug.connectedTo()`相当の直接接続を返す既定仕様は変更しません。

## DAG traversal 拡張後の作業候補

### 1. docs の継続更新

仕様変更後は `bakedanuki/bakedanuki-util/docs/maya/node_operator` を更新します。

特に API の使用例、未対応仕様、設計判断の理由はここに残すと後続作業が安定します。

### 2. lookup.py の追従

新しい attribute type や custom compound を追加したら `lookup_attr_cls()` の解決対象に追加します。

混在型や未対応型は fallback せず、明示的に unsupported として扱う方針です。

### 3. legacy test の整理

当初の優先候補だったextra attribute、custom compound、keyframe、transformの
built-in compound alias、connect / disconnect / next indexはpytest化済みです。

残る`bd_util/_test`は、現行pytestと重複する古い手動test、調査用script、benchmarkを
区別して整理します。仕様を追加で固定できるものだけpytestへ移し、benchmarkは
`_test`に残します。

### 4. MPxCommand の実commandへの展開

`ModifierManager`を組み込んだAPI 2.0の`MPxCommandBase`、失敗時rollback、登録helper、
typed facadeの基本設計は完了しました。現行仕様は[MPxCommand](../mpx_command.md)を
参照してください。

今後、独立したMaya undo単位が必要な利用者向け処理を追加するときは、再利用可能な
operationを先に定義し、MPxCommand adapterとtyped facadeを組み合わせます。

すべてのhelperをcommand化せず、UIやShelfなどから一つのCtrl+Zで戻したい公開操作だけを
対象にします。実commandの共通flagやresult schemaが複数集まった段階で、facadeやstubの
生成を追加するか判断します。

### 5. set_direct の扱い

plug値設定の`set_direct()`は高速で便利ですが、undoには参加しません。
KeyframeManagerの`set_direct()`は廃止済みです。

今後も明確に「即時編集用」として扱い、undo が必要な処理では `set()` と `ModifierManager` を使います。

### 6. 文字化けコメントの整理

一部ソース内に文字化けしたコメントや docstring が残っています。

実装に影響しない箇所でも、今後の保守性のために UTF-8 の日本語コメントへ修復する価値があります。

### 7. 1.0.0 前の API 整理

正式リリース前に次を整理します。

- 公開 API と内部 API の境界。
- deprecated なしで削除してよい旧実装。
- `AddAttr` へ公開する型。
- docs と README の導線。
- MayaModule への導入方法。

## watch points

- `NodeOperator.__getitem__()` の文字列パス解析は未確定です。
- plug値設定の`set_direct()`はundo非対応です。keyframeの変更APIはUndo対応です。
- `lookup.py` は型追加時に更新漏れが起きやすいです。
- unit 系の戻り値や入力単位は、実装と docs を常に揃える必要があります。
- matrix plugの主な取得経路は`get() -> TransformMatrix`とし、成分委譲APIを
  拡張するときも値型、単位、エラー、snapshotの契約を揃える必要があります。
- 速度改善は、利便性を壊さない範囲で行います。
