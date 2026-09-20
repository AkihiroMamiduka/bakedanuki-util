# Changelog

このプロジェクトの注目すべき変更は、このファイルに記録します。

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を参考にし、
バージョン番号は [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

### Added

- `UiStateManager.register_checkable_action()`を追加。checkableな`QAction`のチェック状態を
  他のWidget内部状態と同じMaya用INIへ保存し、dockable UIのclose・復元・Maya終了処理へ
  統合できる。既存のsettings pathと登録APIの動作は維持する。
- `MayaFloatOffsetEdit`を追加し、複数の数値属性群へ各現在値を保った同じ公開単位の増減量を適用する。
  `apply_plugs_values(..., edit_session=...)`で複数行の連続入力を1回のUndoへまとめられる。
  `FloatSpinBox`、`FloatSlider`、`BoolCheckBox`、`EnumComboBox`には任意入力handlerを追加し、
  利用側が既存Viewの入力を選択属性などの一括操作へ委譲できる。Sliderは編集開始・終了も通知する。
  handlerを設定しない既存動作は維持し、scene・設定の移行は不要。
- `bd_util.maya.ui.apply_plugs_values()`と`MayaBoolValueEdit` /
  `MayaFloatValueEdit` / `MayaEnumValueEdit`、union型`MayaPlugsValueEdit`を追加。
  複数のBindingへ異なる公開単位の値を渡し、距離・角度・数値・bool・enumを
  全件事前検証、一回Undo、全行の途中失敗復旧でまとめて確定できる。
  既存の型・範囲・readonly規則を共用し、重複対象を変更前に拒否する。
  従来の単一Binding API・scene・設定の移行は不要。
- `bd_util.ui.CheckBoxSweep`を追加。チェックボックスの押下時がOFF・混在ならON、
  ONならOFFへなぞった対象を揃える。同じ対象は一操作一回だけ入力し、
  `add_button(..., on_change=...)`でBindingなどへ明示入力を委譲できる。
  マウス追跡と中断処理は`RadioButtonSweep`と共用し、既存の公開APIを維持する。
- `MayaChannelStateBinding.set_locked()`へ任意の`edit_session`引数を追加し、
  複数行のlock変更も共有Undoに対応。省略時の動作は維持し、既存呼出し・scene・設定の移行は不要。
- `bd_util.ui.RadioButtonSweep`を追加。標準ラジオボタンへ任意参加の左ドラッグ選択を
  追加し、表示範囲内の通過順判定、通常クリック・キー入力、中断と監視解除を扱う。
- `bd_util.maya.ui.MayaEditSession`を追加。複数の入力先へまたがる書込みを一回の
  Undoにまとめ、差分の初回書込みまでchunkを遅延し、再入した終了要求は書込み後に処理する。
  `MayaChannelStateBinding.set_display_state()`へ任意の`edit_session`引数を追加。
  引数省略時の一回Undoは維持し、既存呼出し・scene・保存設定の移行は不要。
- `MayaChannelStateBinding`を追加。複数scalar属性のKeyable / ChannelBox / Hideと
  lockを値入力から独立して編集できる。混在表示、操作別の編集可否、親lockの説明、
  差分だけの一回Undo、途中失敗の復旧、外部変更の同期、callback解放に対応する。
  enumの項目定義が異なる対象も扱える。HideはChannel Boxの公開状態だけを変更し、
  `MFnAttribute.hidden`や属性値、入力接続は変更しない。既存scene・設定の移行は不要。
- `bd_util.maya.ui.read_enum_definition(plug)`を追加。Bindingやcallbackを作らず、
  scalar enumの現在の実定義を`EnumDefinition`として取得する。scene・値・Undoは変更しない。
- `inspect_scalar_attributes()`の列挙対象と`ScalarAttributeKind`に`enum`を追加。
  配列配下ではないcompound子にも対応する。既存利用側は`kind == "enum"`を処理するか
  明示的に除外すること。Channel Editorはenum対応版toolsと組み合わせて更新する。
  既存scene・保存設定の変換は不要。

- `FloatValueStepSpinBox` を追加。値欄とstep欄を組み合わせ、加算・桁変更によるstep編集、
  表示単位への追従、設定変更通知に対応する。step変更は正本・Undo履歴を変更しない。
  `bd_util.ui` から利用でき、既存の単一・複数属性Bindingを受け取る。
  既存API・scene・設定の移行は不要。
- `MayaBoolPlugsBinding` / `MayaFloatPlugsBinding` を追加。先頭を代表として複数属性を
  既存MVVM Viewへ接続し、明示入力時だけ編集可能な対象へ一括適用する。
  混在値・対象ごとの編集可否と理由、代表値への明示統一、全対象の事前検証、
  一回のUndo、Slider連続編集、途中失敗時の復旧、callback解放に対応する。
- `bd_util.maya.node` に `selected_node_names()` / `inspect_scalar_attributes()` と
  immutableな `ScalarAttributeInfo` を追加。sceneを作成・変更せず、object選択と
  bool・float・距離・角度の既存scalar属性情報を取得する。
- bool / float plug resolverがcompoundの相対属性pathに対応する。
  bool Bindingはcompound子属性と、祖先のlock・接続・値変更の監視にも対応する。
  従来の最上位属性名・短名は維持する。非一意な子名は正式pathを指定する。
  既存scene・設定の移行は不要。
- `set_curve_data()` / `set_key_data()`で、登録済み属性のベース・指定layerにカーブを自動作成する。
  事前の`set_key()`が不要になり、内部の作成用キーも残さない。全置換／追加・上書き、
  weighted・時間単位の契約を維持し、layer作成・登録との一括予約、Undo / Redo・rollbackに対応。
  layer入力にあるconstraint・driven key・空入力のpairBlend等の接続は自動で組み替えない。
- `nodes.create.animLayer(name=..., override=False)`で、ベースと階層接続を含めたlayer作成を予約する。
  `AnimLayer.add_plugs()`は明示プラグ、`add_nodes()`はノード自身のkeyable・未lockの対応属性を登録する。
  compound・既存配列要素の展開、重複排除、選択状態の保持、実行時検査、Undo / Redo・rollbackに対応。
  作成待ちの`AnimLayer`も`KeyframeManager.anim_layer()`へ渡せ、作成・登録・キー設定を一括実行できる。
- `KeyframeManager.anim_layer(name)`で、指定した既存animation layer用の操作入口を取得する。
  元のmanagerを変えずに同じ`ModifierManager`を共有し、BaseAnimationと登録済み属性の
  キー設定・取得・編集・詳細データ復元に対応。layerの改名に追従してノード同一性を保持する。
  キー設定はMayaへlayerを明示して値を解決し、取得・詳細復元は選択カーブ自身の値を扱う。
  空カーブ、実行時の所属・lock / reference検査、Undo / Redo、失敗時rollbackに対応する。
- 調査用の`KeyframeManager.find_anim_curves()`で上流のanimCurve候補を列挙し、具体ノード型の
  tupleとして返す。型filter、名前順、重複排除、各経路の最初のカーブでの探索停止に対応。
  layer・blend weight・未対応のdriven keyも候補として扱い、選択したTA / TL / TUは
  共通の`ModifierManager`で明示編集できる。
- TA / TL / TUノードに`keyframe: CurveKeyframeManager`を追加。カーブを明示して
  生の値・接線・詳細データを取得・編集でき、未接続・共有出力・時間入力接続にも対応する。
  ノード同一性、予約時の独立コピー、Undo / Redo、失敗時rollbackを保持する。
  Maya 2027を含む補完stubにも、schemaとは独立した共通操作を生成する。
- 詳細データAPI用benchmarkを追加。全体・範囲取得、境界補完、復元の予約・実行・
  Undo / Redo、JSON変換を個別測定し、指定commitとの比較も可能にする。
- `get_curve_data()`に範囲指定を追加し、`get_key_data()`と共通の境界補完を実装。
  既定の`include_boundaries=True`では、元カーブを変更せずに境界キーと調整後の接線を取得する。
  連続接線をfixed化し、step / stepnext、weighted、単位を保持して区間を切り出す。
  constant / linearの範囲外補完に対応。cycle系の範囲外補完は明示的に拒否する。
- `KeyframeManager.get_weighted()` / `set_weighted()`を追加。チャンネルのカーブの
  weightedを照会・変更し、接線の変換はMaya標準処理に委譲する。変更は予約実行とUndo / Redoに対応。
- `KeyData` / `AnimCurveData`と、`KeyframeManager`の`get_key_data()` /
  `set_key_data()` / `get_curve_data()` / `set_curve_data()`を追加。
  TA/TL/TUカーブについて、接線・lock・breakdown・weighted・infinityを
  JSON経由でも保存・復元できる。degree / cmと保存時の時間単位を保持し、
  遅延実行・Undo / Redo・途中失敗時rollbackに対応する。
- scalar plugに`sample_values(*, frames)`を追加。constraint・layer・計算ノードを含む
  指定時刻の評価済み値を、`set_keys()`へ渡せる`(frame, value)`のlistで取得する。
  公開単位と入力順を維持し、現在時刻・Undo履歴・保留中modifierを変更しない。
- `KeyframeManager.get_keys(start_frame=None, end_frame=None)`を追加。チャンネルの
  time-inputカーブに実在するキーを、範囲の両端を含む`(frame, value)`のlistで返す。
  予約中の操作は実行せず、値の単位は取得したカーブ型から換算する。
- `KeyframeManager.set_keys(keys, ...)`を追加。`keys`は`(frame, value)`の列。
  単位・tangent・予約実行とUndo / Redoは`set_key()`と共通で、全入力を捕捉・検証してから入力順に
  設定する。単純なカーブではバッチ内の取得と変更キャッシュを共有し、新規作成や
  複雑な接続ではMaya標準のキー設定を使用する。
- `Quat`をimmutableなraw Quaternion値のまま拡張。identity / sequence /
  `MQuaternion` constructor、Euler / axis-angle / 2-vector / matrixからの作成、
  Quaternion積、変換、逆元、共役、正規化、shortest-path slerp、状態と等価性の
  照会に対応。Euler変換の`rotate_order`は回転順序名とMayaの0〜5のindexを受け取る。
- `Double2` / `Double3` / `Double4`、`Float2` / `Float3`に、同じ具体型同士の
  加減算、scalarによる乗除算、符号反転を追加。
- `Transform` / `Joint`に、指定したDAGノードへDAG原点のworld位置を合わせる
  `match_position()`を追加。合わせる軸と、world / local / objectの基準空間を
  指定できる。
- `Transform` / `Joint`に、world姿勢を`rotate` / `rotateAxis` / `jointOrient`の
  いずれか1属性だけで合わせる属性別マッチAPIを追加。非対象の回転属性と
  translate / pivotは変更せず、rotate pivotに対する位置補償は行わない。

### Changed

- `EnumComboBox`へ`wheel_requires_focus`とスネークケースの取得・変更APIを追加し、
  フォーカスのないホイール入力を親Widgetへ渡せるようにする。`True`では
  ホイールによる自動フォーカス取得を防ぎ、クリック・Tabでフォーカスを得た後の操作は維持する。
  `FloatSpinBox`と`FloatStepSpinBox`の独自APIも`wheel_requires_focus()`／
  `set_wheel_requires_focus()`へ統一する。従来の`wheelRequiresFocus()`／
  `setWheelRequiresFocus()`を使用する場合は新名称へ変更する必要がある。
- `FloatSpinBox`と`FloatStepSpinBox`へ`wheel_requires_focus`を追加し、
  非フォーカス時のホイール入力を受け付けるか選択可能にする。
  `FloatValueStepSpinBox`は値欄とstep欄を個別指定できる。
  値欄は従来どおり`False`、step欄は誤操作を避ける従来どおり`True`を既定値とし、
  既存利用側の挙動、scene、保存設定の移行は不要。
  `FloatSpinBox`は`True`時に`StrongFocus`へ切り替え、ネイティブホイール入力が
  判定前にフォーカスを取得して値を変更する不具合を修正する。クリック・Tabによる
  フォーカス取得後は編集でき、`False`では従来の`WheelFocus`を維持する。
  この値欄を使う`FloatValueStepSpinBox`と`FloatSliderSpinBox`にも適用される。
- 既存属性の解決で、名前が一意な属性はMaya APIから直接取得する。
  長名・短名と完全な親pathを確認し、非一意名は既存の全件検索で判定する。
  aliasの拒否、曖昧な名前のエラー、配列制限を維持し、キャッシュは追加しない。
- `FloatStepSpinBox`の初期化順を調整し、下限設定時に不要な極小値を一時表示する
  処理を省く。初期値、精度、最小値・最大値、加算・倍率操作は維持する。
  どちらも既存API・scene・保存設定の移行は不要。
- `MayaBoolPlugsBinding` / `MayaFloatPlugsBinding` / `MayaEnumPlugsBinding`の
  dirty通知を対象plug・compound祖先へ絞り込み、無関係な属性変更での再同期を抑える。
  各nodeのcallbackへ所属対象だけを渡し、複数選択時の全node走査も省く。
  接続先・時間変更・親属性の同期、単位変更、Undo／Redo、削除と終了時の解放は維持する。
  公開API・scene・保存設定の移行は不要。
- `FloatValueStepSpinBox`のstep欄を4桁表示できる68 pxへ縮小し、`value_width`と
  `step_width`で各欄の固定幅を指定できるようにする。固定した欄は左へ詰め、
  余白を右端へ配置する。`FloatSliderSpinBox`へ`layout_order`を追加し、
  従来の`"slider_value"`に加えて`"value_slider"`を選択可能にする。
  既定のSlider順序、値、scene、設定形式の移行は不要。
- `FloatSpinBox`の単位文字表示と`FloatValueStepSpinBox.step_show_unit`の既定値を
  非表示へ変更する。`FloatSliderSpinBox`、`Float3SpinBox`、
  `Float3SliderSpinBox`の値欄にも適用される。
  従来の表示が必要な場合は値欄へ`setUnitVisible(True)`、step欄の生成時に
  `step_show_unit=True`を明示する。数値の単位換算は維持し、scene・設定の移行は不要。
- animation layerへの所属確認を、全属性の列挙から対象plugのnative照会へ変更する。
  配列・compoundのlock検査もMPlug.isFreeToChangeを使い、通常の未lockカーブのPython巡回を削減する。
  所属・lockの実行時再検査、個別キーのlock拒否、Undo / Redoとrollbackは維持する。
  詳細データbenchmarkに直接接続・ベース・加算・Overrideと所属属性数の指定を追加する。
- layer未指定の`KeyframeManager`は、キー設定・取得・編集・詳細データ操作をsceneの
  ベース（root）layerへ統一する破壊的変更。Mayaの選択layer・preferred・keying modeに
  設定先を委ねず、rootの改名にも追従する。layerがないsceneは通常のチャンネルを扱う。
  別layerは`anim_layer(name)`で指定する。`sample_values()`の合成後のplug評価と
  `find_anim_curves()`の診断範囲、Undo / Redo・rollbackは維持する。
- KeyframeManagerのquery・挿入・接線変更・削除・詳細データ操作を、そのチャンネル自身の
  時間入力カーブへ統一。単位変換、pairBlendの同軸・currentDriver入力、blendWeightedの
  入力index順に対応し、DG全体で最初のカーブを選ぶ旧探索を置き換える破壊的変更。
  driven key・別軸・weight・constraintのdriverは除外し、空カーブも対象にする。
  layer付き属性は既定のベースまたは`anim_layer()`で指定したlayerを対象とし、
  未対応utility、共有出力は明示エラー。キー設定のMayaによる値解決と、Undo / Redo・rollbackは維持する。
  詳細データの自動新規復元は未接続plugと登録済みlayerの空き入力を対象とし、
  対象カーブのないその他の既存接続は上書きしない。
- 詳細データの補完なし範囲取得と、境界補完後の再取得を必要なキー範囲に限定し、
  範囲外の詳細データ生成・重複コピーを削減する。隣接時刻による接線換算と形状保持は維持する。
- `get_key_data(start_frame, end_frame)`は、既定で境界を補完する破壊的変更。
  既存キーと元の接線情報だけを取得する場合は`include_boundaries=False`を指定する。
  範囲無指定の取得と`get_keys()`の仕様は維持する。
- `KeyData`を直接編集可能に変更。設定予約時とJSON出力時に再検証し、独立コピーを保持する。
  `set_key_data()`の`weighted`引数を廃止し、既存カーブの設定を維持、新規はnonweightedとする。
  接線XYをweighted相当の共通表現へ統一し、保存schemaを2へ更新。
  `AnimCurveData.from_dict()`はschema 2のみを受け付け、旧形式の変換処理は提供しない。
- `KeyframeManager.set_keys()`の入力を、別々の`values` / `frames`から
  `(frame, value)`のpair列へ変更する破壊的変更。旧引数は提供しない。
  `set_keys(zip(frames, values, strict=True), ...)`で移行でき、単位・共通tangent・
  予約実行・Undo / Redoの仕様は維持する。
- `KeyframeManager.set()`を`set_key()`へ、`insert()`を`insert_key()`へ改名する
  破壊的変更。旧名のaliasは提供せず、`plug.keyframe.set_key()` /
  `plug.keyframe.insert_key()`へ移行する。引数、`None`戻り値、予約実行、
  Undo / Redoの仕様は維持する。
- `Quat`を`Double4`の派生型から、`Scalar4[float]`を直接共有する独立した具体型へ変更。
  double4 plugの物理表現は共有しつつ、numeric値型のcomponent-wise演算が
  Quaternionへ波及しない型階層へ整理。
- `PlugOperator` の接続照会を `MPlug.connectedTo()` ベースへ変更。
  接続先を具体的な `PlugOperator` として返し、`nodes.types` によるnode type filterと
  subclassの包含指定に対応。ノード名・plug名は専用メソッドで取得する。
- `MatrixPlugOperator.get()` と `DataMatrixPlugOperator.get()` の戻り値を
  `TransformMatrix` に統一。未設定のtyped matrix plugはidentity matrixや`None`へ
  補完せず、値を取得できない場合は`ValueError`を送出する。
- matrix plugの値設定が`TransformMatrix` / `MMatrix` /
  `MTransformationMatrix`を受け取れるように変更。
- `TransformMatrix`と`MMatrix`の左右両方向の乗算に対応し、結果を
  `TransformMatrix`として返すように変更。
- `TransformMatrix`の分解値をtupleからcompound専用値型へ変更。
  `translate`は`DoubleLinear3`、`rotate` / `get_rotate()`は`DoubleAngle3`、
  `scale` / `shear`は`Double3`、`quat`は`Quat`を返す。
- `TransformMatrix.get_rotate()`の引数名を`order`から`rotate_order`へ変更し、
  回転順序名に加えてMayaの`rotateOrder` indexを受け取るように変更。

### Removed

- matrix plugの`transform_matrix`プロパティを削除。`get()`が返す
  `TransformMatrix`を使用する。

## [0.2.0] - 2026-08-14

v0.1.0 以降の NodeOperator 基盤の改善に加え、Windows版 Maya 2025 / 2026 /
2027 向けのネイティブ C++ plug-in `bdUtilNodes.mll` を初めて同梱するリリースです。

### Added

- Windows版 Maya 2025 / 2026 / 2027 向けのネイティブ C++ plug-in
  `bdUtilNodes.mll` を追加。
  `double`、`double3`、`doubleLinear`、`doubleLinear3`、`doubleAngle` の算術・
  補間・範囲・条件・平均系ノードを追加。
- Quaternion / Euler の値、積、基底変換、Bend / Twist の分解・合成・制限を扱う
  ネイティブノードを追加。
- position、orientation、Bend / Twist の RBF weight / falloff weight と、
  RBF weight から TRS pose を合成する pose blend ノードを追加。
- ネイティブ plug-in の線形代数実装に Eigen 5.0.1 を追加し、配布物へ第三者
  ライセンスと notice を同梱。
- `Double2` / `Double3` / `Double4`、`Float2` / `Float3`、`Long2` / `Long3`、
  `Short2` / `Short3`、unit compound、`Quat` の snapshot value 型を公開 API に追加。
- `PlugOperator` に、接続先から接続元を指定する `connect_from()` と
  `disconnect_from()` を追加。接続元には `PlugOperator`、`"node.attr"`、
  `["node", "attr"]`、`("node", "attr")` を指定可能。
- Pyright による `nodes.create` / `nodes.existing`、plug、value 型の型・補完
  contract を追加。
- Maya versionごとのAPI versionをplug-in metadataへ登録し、Python package versionとの
  整合性を各Maya実行環境で検証するテストを追加。
- Autodeskから取得した固有Node ID block `0x00142680` - `0x0014277F` を、
  配布する全ネイティブノードへ割り当て。

### Changed

- scalar / compound attribute の型階層と値変換を整理し、公開 API の型注釈と
  IDE 補完を改善。
- NodeOperator のノード作成、plug 解決、値取得の処理を高速化。
- node class generator と生成 stub を、現在の型階層およびネイティブノードへ対応。
- v1.0.0 未満の互換性方針を明文化。破壊的変更は原則として minor release で行い、
  patch release では意図的に行わず、一度公開した `MTypeId` は変更・再利用しない方針を追加。

### Fixed

- 新規animation layerへの初回キー設定直後に`sample_values()`の先頭値が古い値になる問題を修正。
  対象plugの上流カーブから再評価を伝播してから読み取り、現在時刻・選択・modified flag・
  Undo / Redo履歴・保留中modifierを保持する。計算出力やdriven curve越しの依存関係にも対応。
- キー設定のMaya commandへ完全なplugパスを渡し、別のDAG階層にある同名nodeを
  巻き込んでキー設定する問題を修正。layerの所属確認・対象照会でもaliasと配列indexを区別する。
- `FltMatrix` と `longLongInt` attribute の値取得・設定が動作しない問題を修正。
- compound attribute の一部で不定な default value を生成する問題を修正。
- Maya command へ文字列ではなく `MPlug` を渡していた箇所を修正。

### Removed

- `PlugOperator` の接続・切断用演算子オーバーロード `__gt__()`、`__lt__()`、
  `__or__()`、`__ror__()` を削除。接続には `connect()` / `connect_from()`、
  切断には `disconnect()` / `disconnect_from()` を使用する。

## [0.1.0] - 2026-07-24

`bakedanuki-util` の最初の公開リリースです。
v1.0.0 未満の開発中 API のため、今後のリリースで破壊的変更が入る可能性があります。

### Added

- Windows / Maya 2025 以降を対象とした Maya Module 形式の配布構成を追加。
  `installer.py`、Maya 2025 / 2026 / 2027 用ランチャー、既存ランチャーへの組み込みに対応。
- ノードの作成と既存ノードのラップを統合する `Nodes` API を追加。
  `nodes.create` / `nodes.existing` から具体的な `NodeOperator` 型へアクセス可能。
- Maya の DG / DAG ノードを Python クラスとして扱う `NodeOperator` と、
  `AttributeField` / `AttrOperator` / `PlugOperator` による attribute・plug 操作を追加。
- plug の値取得・設定、接続・切断、multi attribute の空き index 取得、
  extra attribute の追加、キーフレームの作成・照会・削除・tangent 操作に対応。
- `MDGModifier` / `MDagModifier` の操作、実行履歴、undo / redo を管理する
  `ModifierManager` を追加。
- matrix の合成・乗算・逆行列・TRS 分解を扱う `TransformMatrix` と、
  matrix plug からの translate・rotate・scale・shear・quaternion 取得を追加。
- DAG の親子操作、循環する親子関係の防止、world transform を維持した親変更、
  DAG 間の relative matrix・local matrix 取得に対応。
- Maya node type から生成クラスと手書き可能な公開 wrapper を作成する
  NodeOperator generator と、`nodes.create` / `nodes.existing` の補完 stub 生成を追加。
- Maya 実行環境で公開 API、NodeOperator、attribute・plug、matrix、generator を検証する
  pytest スイートと開発ドキュメントを追加。

[Unreleased]: https://github.com/AkihiroMamiduka/bakedanuki-util/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/AkihiroMamiduka/bakedanuki-util/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/AkihiroMamiduka/bakedanuki-util/releases/tag/v0.1.0
