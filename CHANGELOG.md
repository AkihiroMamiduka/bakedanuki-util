# Changelog

このプロジェクトの注目すべき変更は、このファイルに記録します。

形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を参考にし、
バージョン番号は [Semantic Versioning](https://semver.org/lang/ja/) に従います。

## [Unreleased]

### Fixed

- byteのhard limitで下限0／上限255を個別に未指定扱いにしていた判定を修正。
  型既定の全範囲0～255だけを除外し、`overrideColor`の0～31などは両端を保持する。
  bdChannelBoxの整数Slider選別を修正し、既存の入力制限・設定・sceneの移行は不要。
- 整数・floatの`ValueStepSpinBox`で値欄を自動幅にしたとき、Step欄が表示領域の
  右外へ配置される不具合を修正。Step欄の固定幅をレイアウトでも確保する。
  API・scene・保存設定の移行は不要。

### Changed

- `Nodes()` の IDE 補完の既定値を `bd_util/config/typing.pyi` で選択可能にした。
  初期値は `Maya2025Plus` とし、単一版と `Plus` 範囲の全6プロファイルを用意する。
  プロジェクトの `stubPath` から上書きでき、明示した `typing_maya_version` を最優先する。
  コピー用テンプレートを同梱し、実行時の Maya 判定と `bdu.node_types` は維持する。
- 共有`bakedanuki`メニューと各categoryを`tearOff=True`で作成するよう変更。
  既存メニュー配下の配置でも、先頭の点線からMaya標準の独立Windowへ切り離せる。
  切り離し側の項目・設定は元メニューに同期し、元メニューの破棄で終了する。
  Maya再起動またはメニュー再生成で反映する。scene・保存設定の移行は不要。
- `bd_util.maya.ui.register_menu_item()`へスクリプト文字列と
  `source_type="mel" | "python"`を追加。文字列と言語をMayaへ直接登録し、
  Shelfやマーキングメニューに保存できる起動コマンドを扱える。
  既定はPythonで、引数なしのPython関数による既存の登録も維持する。
  関数にMELを指定した場合と空のスクリプトは拒否する。scene・設定の移行は不要。
- `bd_util.maya.node.inspection.inspect_scalar_attributes_by_type()`を追加。
  ノードを作成せず、抽象型を含む登録済み型の標準scalar属性・正式path・表示名・
  既定のkeyable／channelBoxフラグを取得する。配列配下・非対応型・個別ノードの追加属性は
  含まない。既存のノード調査APIとscene・保存設定の移行は不要。
- `RadioButtonSweep`と`CheckBoxSweep`の`add_button()`へ
  `apply_unchanged=False`と`group=None`を追加。基準の表示と同じ状態も明示要求でき、
  開始ボタンと同じgroupの登録だけになぞり入力を限定できる。
  ラジオ版には`on_change: Callable[[], None]`も追加し、入力先に表示同期を委ねられる。
  明示入力は一ドラッグ中に同じボタンへ一回だけ送り、通常クリック・キー入力と
  引数を省略した既存動作を維持する。scene・保存設定の移行は不要。
- `FloatSliderSpinBox`の`single_step`既定を`None`へ変更し、生成時に
  `unit_kind="angle"`なら1、通常数値・距離なら0.1を表示単位の刻み幅に使う。
  明示指定したstepは優先し、Slider分割数・小数精度・単位変更時のstep数値は維持する。
  従来の角度0.1刻みを使う場合は`single_step=0.1`を指定する。
  他のViewが明示して渡すstepは変更しない。scene・保存設定の移行は不要。
- 複数属性のscalar値Pasteで、候補Storeの構築中だけnode操作オブジェクトを共有。
  指定pathへの絞込み・一値の複数path展開後の属性数で判断し、単一属性は従来の経路を使う。
  共通の書込み計画へ渡す前に共有索引を解放し、初期除外・書込み順・定義変更の検出・
  削除監視・Undo・失敗復旧を維持する。公開API・scene・設定・clipboardの移行は不要。
- `bd_util.maya.ui.shared_scalar_plug_nodes()`を追加。明示した同期的な構築範囲内で、
  scalar resolverが同一実体の`NodeOperator`と`ModifierManager`を共有する。
  名前とDAG経路は毎回解決し、経路変更時は以後のwrapperを作り直す。
  属性path・型は毎回照合し、値・監視・検証・Undoの境界は維持する。
  入れ子は独立し、例外時も索引を解放する。既存呼出し・scene・設定の移行は不要。
- scalar値Pasteの対象ごとに重複していたenum定義・値の検証を、直後の共通書込み処理へ
  集約。操作開始・書込み直前・同値対象も含む終了検証、削除監視、Undoと復旧は維持する。
  定義変更の文言は対象側になり、複合異常では接続・状態変化を先に報告する場合がある。
  `enum_validation`の既定と適用規則、clipboard形式は変更せず、移行は不要。
- 複数enum属性の書込みで、同じ事前検証・書込み直前の段階内にあった対象値・定義の
  二重確認を共通の書込み計画へ集約。操作開始・各書込み直前・終了時の検証範囲、
  定義変更の検出、Undoと失敗復旧は維持する。定義と接続が同時に変わった場合は
  接続変化やそれに伴う状態変化を先に報告することがある。公開API・scene・設定の移行は不要。
- `inspect_scalar_attribute_types()`と`ScalarAttributeTypeInfo`を追加。
  正式path・scalar型だけを取得し、表示名・表示フラグ・値を読まずに操作対象を照合できる。
  属性解決・型分類・入力順・重複排除は`inspect_scalar_attributes()`と共有する。
  `bd_util.maya.ui.shared_plugs_lifetime()`の範囲内で生成した
  `monitor_lifetime=True`の複数Bindingは、nodeごとの削除callbackを共有する。
  各対象の削除履歴・全件検証・Undo・失敗復旧と、書込み中の監視保持を維持する。
  購読の終了は各Bindingの`dispose()`に従い、他の購読者やUndo後の新しいBindingを無効化しない。
  `MayaCallbackRegistry.remove_many()`で複数IDの解除をまとめ、残る登録順を維持する。
  既存APIの指定・scene・設定の移行は不要。
- scalar入力の書込み可否検証で、未接続かつ入力状態の追跡が不要な対象は
  表示用の属性名・状態データを生成せず、実体・自身と祖先のlock・writable・
  Mayaの変更許可を毎回確認する。接続または入力状態の追跡がある対象は
  従来の詳細検証を使い、代表と対象が同一なら可否の二重確認を省く。
  全件事前検証、書込み直前の再確認、削除監視、Undoと失敗復旧は維持する。
  公開API・scene・保存設定の変更や移行は不要。
- scalar数値の範囲検証を表示情報の生成から分離し、多数対象の入力時に
  単位表記・表示倍率・Presentationを繰り返し組み立てる処理を削減。
  hard limitは検証のたびに取得し、型固有の範囲・公開単位・格納精度・単位変更の検出を維持する。
  公開API・表示・Undo・失敗復旧の仕様は変更せず、scene・保存設定の移行は不要。
- `FloatSlider`・`IntSlider`へ読取り専用の`is_wheel_editing`を追加。
  wheelの開始・値要求・終了通知中だけTrueとなり、終了・例外後はFalseへ戻る。
  利用側で対象の準備寿命を分けるための情報で、既存の入力・Undo・focus仕様は維持する。
  scene・保存設定の移行は不要。
- 複数scalar Bindingと単一整数Bindingへ`monitor_lifetime=False`を追加。
  `monitor=False, monitor_lifetime=True`では値通知を同期せず、node単位の軽い監視で
  削除履歴だけを保持する。監視は表示用Registryから独立し、外部からの監視解除中も保つ。
  書込み・復旧前と同値対象を含む終了時に消失を確認し、同名再作成へ追従しない。
  書込み中のdisposeは入力を即停止し、復旧が終わるまで削除監視だけを保持する。
  既定の監視仕様とPasteの公開APIは維持し、scene・設定の移行は不要。
- scalar値Pasteは対象ごとに独立した一時Storeを使い、表示用Binding・ViewModel・
  Signal・連続編集用Undo管理を生成せずに既存の値変換と書込み準備を利用する。
  `apply_plugs_values()`と検証・書込み・Undo・失敗復旧の処理を共有し、
  候補件数、除外理由、`enum_validation`を含む公開APIと適用規則を維持する。
  操作中の対象削除を記録し、同名で再作成された別実体へ追従しない。
  外部処理による削除・再作成自体は復旧対象外とする。
  UI・scene・保存設定・clipboard形式の変更や移行は不要。
- `MayaChannelStateBinding`の重複判定と通知対象の探索を実体索引へ変更し、
  多数属性のlock・表示状態編集に伴う全対象の繰り返し走査を削減。
  hashが同じ別nodeを混同せず、削除履歴、親lock判定、Undo、失敗復旧、callback本数を維持する。
  `MayaCallbackRegistry`も登録IDの所属判定を索引化し、登録順・逆順解除と再入時の扱いを維持する。
  公開API・UI・scene・保存設定の変更や移行は不要。
- `apply_plugs_values(..., enum_validation="operation")`を追加。
  `apply_scalar_value_transfer()`、`apply_scalar_value_transfer_to_paths()`、
  `apply_scalar_value_to_paths()`も同じ指定を受け付ける。
  enum定義を開始時の整数値・項目名の対応へ固定し、書込み直前の基準と当該対象、
  終了時の全対象を新しく読み直して比較する。別実体のカスタムenumも全件再取得の
  繰り返しを減らせる。既定の`"per_write"`は従来どおり維持する。
  後続・既適用・readonly・同値対象や別行の変更検出が終了時まで遅れる場合がある。
  不一致では同じUndo／復旧処理内で値の復旧を試みるが、外部callbackの副作用と
  定義そのものは戻さず、復旧不能時はエラーにする。scene・設定の移行は不要。
- `MayaEnumPlugsBinding`の定義検証で、`MPlug.attribute()`の`MObject`実体を
  共有する対象の定義取得をまとめる。検証のたびに定義を新しく取得し、標準属性や
  動的属性という区分だけで不変とは扱わない。同名・同内容でも別実体は個別に検証する。
  定義変更の検出、Undo、途中失敗の復旧は維持する。別実体のカスタムenumだけを
  集めた場合の取得数は減らない。公開API・UI・scene・設定形式の移行は不要。
- 複数scalar Bindingへ`monitor=False`を追加。同期的な一括操作で監視を登録せず、
  既存の型・範囲検証、Undo、失敗復旧を利用できる。既定は従来どおり監視する。
  `inspect_scalar_attributes(..., paths=...)`で指定属性だけを取得できる。
  選択・Binding・一括編集の重複判定を実体索引で行い、多数対象の二重走査を削減。
  値Pasteも必要な属性だけを取得し、一時Bindingの監視を作らない。
  APIは追加のみで、scene・保存設定・clipboard schemaの移行は不要。
- `EnumComboBox`で同じ項目を明示的に選び直した場合も入力handlerへ通知する。
  値が変わる一回の操作は一回だけ通知し、外部同期は入力として扱わない。

- `MayaIntPlugBinding`／`MayaIntPlugsBinding`と整数値Pasteに`edit_connected`と
  `key_animated`を追加。既定の読み取り専用は維持し、明示指定で時間カーブ・SDK・
  short／longのAnimation Layerを既存型と同じ規則で編集する。
  整数カーブの小数補間をKey Alteredと誤認せず、32-bit端でも1の差を識別する。
  `IntSpinBox`はEnterを欄内で受理し、`select_all_on_mouse_focus`で初回クリックの
  全選択を指定できる。scene・保存設定・clipboard schemaの移行は不要。
- `inspect_scalar_attributes()`とscalar値搬送でbyte・short・longを整数値のまま扱う。
  `MayaIntValueEdit`と`MayaIntOffsetEdit`を公開し、複数属性への整数入力と一回Undoに対応。
  Clipboard書込みschemaはversion 3へ変更し、旧version 1・2は読み込める。
  旧版アプリへ新しいコピー内容を貼り付ける場合は、利用側を更新する。
  sceneと保存設定の移行は不要。
- `BytePlugOperator.get()` はMayaのbyte値128～255を符号反転せず返す。
  従来の負値を前提にした呼び出しは、byte属性の実値を使うよう修正する。
- `bd_util.py.path.icon_path(module_file, file_name)`を
  `resolve_relative_path(base_file, relative_path)`へ改名し、画像用途に限らないAPIとした。
  旧名は削除したため、importと呼び出し名を変更し、キーワード指定は
  `module_file`から`base_file`、`file_name`から`relative_path`へ置き換える。
  パスの組み立て方と戻り値型は維持し、scene・保存設定の移行は不要。
- `Nodes` の操作入口を保持する推奨変数名を `nodes` から `bd_nodes` へ変更。
  README、docs、サンプル、内部コードとテストを統一した。
  `Nodes` のクラス名と既存の公開 API は維持するため、利用者のスクリプトの修正は不要。
  推奨名に揃える場合は、操作入口を保持する変数とその参照だけを変更する。
- `installer.py` は `MAYA_ENV_DIR` と共通 `Maya.env` の探索順を考慮する。
  既存ファイルの変更時は元の内容をバックアップし、BOM・改行を維持して
  一時ファイルから置き換える。複数の `MAYA_MODULE_PATH` 定義と保存競合は拒否する。

- `bdControllerShape` の既定形状を `Cube`、既定の `boundsMode` を
  `ShapeCentered` に変更した。
- `bdControllerShape` の `3D` 系 Filled 矢印は直交する薄い三角面で描き、
  `OctahedronArrowFinFilled` は八面体と重ならない左右の Fin 面だけを塗る。
- `bdControllerShape` の選択色をビューポートごとの Selection Highlighting 設定に従わせ、
  オフでは通常色と軸色を保つ。
- `bdControllerShape` の基準軸を主軸 `+X`・補助軸 `+Y` の右手系へ変更した。
  `Square`・`Circle`・`CircleArrow2D` の基準面と作成時の表示面は YZ とし、
  `shape1stAxis` / `customBounds1stAxis` の既定値を `+X` に変更した。
  形状と Custom Bounds の Axis 系 X/Y/Z は主軸／補助軸／第３軸に対応し、
  `+3rdAxis` は「主軸 × 補助軸」の正方向とする。旧計算仕様は残さない。
- Maya上部の共有メニュー表示名を`bd`から`bakedanuki`へ変更した。
  内部UI名と所有権タグは維持し、既存セッションのメニューも再登録時に表示名を更新する。
  sceneと保存設定の移行は不要。
- `bakedanuki`メニューの起動時表示設定をMayaの`optionVar`から
  `prefs/bakedanuki/menu.json`の`show_menu_on_startup`へ移した。
  既存の`optionVar`は専用ファイルがない場合に読み取る。旧JSONキー`auto_install`も
  読み取り、次の切り替えまたはinstaller再D&Dで新しいキー名へ保存する。
  チェック操作とinstallerは`savePrefs`を呼ばず、Mayaの一般設定やShelfを
  明示的に保存しない。
- `MouseFocusSelectAllDoubleSpinBox`を使う数値欄は、通常Enter・テンキーEnterの
  確定操作を欄内で受理し、Mayaの親Windowのshortcutへ伝播させない。
- `Transform`／`Joint` の `round_translate()`、`round_rotate()`、
  `round_rotate_axis()`、`round_joint_orient()` は、Python の偶数丸めから
  十進の四捨五入へ変更する。従来の偶数丸めが必要な呼び出しは、
  `round()`で目標値を計算して対応する`set_*()`へ渡す方式へ移行する。
  既定の桁数の基準は従来どおり cm／度とし、
  `rounding_unit="display"` で現在の Maya 表示単位を指定できる。
  scene・設定の移行は不要。
- `StringLineEdit`はマウスでフォーカスを得た最初の左クリック後に文字列を全選択する。
  `select_all_on_mouse_focus=False`で無効化でき、設定の取得・変更も可能。
- `StringLineEdit`は通常EnterとテンキーEnterの確定キーをView内で処理し、
  フォーカス取得時と確定前に正本を再読込みする。UIの編集失敗は`edit_failed(str)`で
  通知し、確定値へ表示を戻す。プログラムからの変更要求は従来どおり例外を返す。
  親WindowのEnter処理に依存する利用側は、必要な処理を明示signalへ接続する。
  scene・設定の移行は不要。
- `StringLineEdit`へ`follow_source_during_edit`を追加。指定したViewでは、編集中に
  正本の確定値が変わると未確定入力を破棄して最新値を表示する。複数Maya属性では
  後続対象だけの値変更も対象とし、入力可能なままの状態通知では入力を維持する。
  既定の競合保持動作は維持し、scene・設定の移行は不要。

### Added

- Qtモーダル画面を指定したグローバル座標付近へ配置する`exec_dialog_near()`を追加。
  操作したモニターの作業領域へ外枠まで収め、過大な画面だけ縮小する。
  所有タイマーによる表示直後の補正を行い、終了・例外時に監視と制約変更を解除する。
- Qt版の保存先選択を同じ配置で開く`get_save_file_name_near()`を追加。
  初期フォルダー・ファイル名・拡張子・上書き確認を扱い、ファイルへの書込みは呼出し元へ委譲する。
- `MayaIntPlugBinding`／`MayaIntPlugsBinding.hard_limits`を追加。
  代表属性へ明示された下限・上限を取得し、型固有範囲とsoft limitを区別する。
  byteの型既定の全範囲0～255だけは両側未指定扱いとし、両側hard limitを使う整数Sliderの
  選別に対応する。既存の値検証と設定形式は維持し、移行は不要。
- 整数用の`IntSliderSpinBox`と`IntRangeSliderSpinBox`を追加。
  前者はSliderと値欄の並び順を選べ、後者は`[Min][Slider][Max][値][Step]`で
  View固有の操作範囲と正の整数Stepを編集する。既存の整数連続Undo基盤を利用する。
  `UiStateManager.register_int_range_slider_spin_box()`でMin・Max・Stepだけを
  JSON整数として保存・復元できる。既存の設定形式・sceneの移行は不要。
  操作サンプルは`bd_util._sample.maya.ui.int_sample.range_slider.show_demo()`。
- `IntSlider`と`IntViewModel`の連続編集APIを追加。整数演算で32-bit範囲を写像し、
  Maya正本・Python正本とMaya同期のドラッグを一回Undoにまとめる。
  floatと共通のUndo管理で操作切替・時刻移動・監視解除にも対応する。
  `int_sample.slider.show_demo()`で操作確認できる。既存API・scene・設定の移行は不要。

- `IntStepSpinBox`・`IntValueStepSpinBox`に、加算と10倍・整数除算による整数Step入力を追加。
  任意の正整数を入力でき、下限1、上限を超える増加は無効とする。
  `IntStepProfile`／`IntStepSetting`と`UiStateManager.register_int_step_profile()`で
  整数設定を独立したversion 1形式で保存する。`int_sample.step.show()`で確認できる。
  既存API・scene・保存設定の移行は不要。

- Python整数を正本としてQtとMayaのbyte・short・longを同期する`MayaIntBinding`と
  `MayaIntPlugView`を追加。初期同期はPythonからMayaへ適用し、Maya入力はsetterを通す。
  型範囲・hard limit・lock・接続による同期失敗ではPython値を維持し、状態と例外を公開する。
  Undo／Redoの復元中は追加書込みを保留して履歴を維持する。
  `int_sample.maya_view.show_demo()`で操作確認できる。既存API・scene・設定の移行は不要。

- `bd_util.maya.ui` に、byte・short・long属性用の
  `resolve_int_plug()`、`MayaIntPlugBinding`、`MayaIntPlugsBinding`を追加。
  単一属性とcompound子属性の監視、型固有範囲とhard limitの検証、
  複数属性の一括入力とMaya Undoに対応する。入力接続中は読み取り専用とし、
  既存scene・設定の移行は不要。
- `bd_util.py.path.resolve_relative_path(base_file, relative_path)`を追加。
  基準ファイルと相対pathから同梱リソースの絶対pathを解決し、
  tools・rigなど複数packageで共用できる。対象の検証・UI登録・状態の保存は行わない。
- 共有メニューの`register_menu_item()`に、省略可能な`icon_path: str | Path | None`を追加。
  画像の絶対pathをMayaへ渡し、再登録で画像の更新・解除も反映する。
  画像の欠落・破損では警告して画像なしで登録し、実表示はMayaの標準設定に従う。
  既存呼出しとscene・保存設定の移行は不要。
- `bakedanuki`共有メニューの配置先を`prefs/bakedanuki/config.toml`の
  `[menu].parent_menu`で指定できるようにした。キーがなければ最上位メニューに表示し、
  既存メニューのUIパスを指定するとその直下に配置する。個人用ファイルはMayaの
  設定ディレクトリへ初回だけ自動作成し、`BAKEDANUKI_CONFIG_FILE`で指定した
  外部TOMLを優先する。
- 共通配布ルートに `uninstaller.py` を追加した。現在の Maya が読む `Maya.env` から
  実行元の `modules` パスだけを確認後に解除する。共通ルートの同梱packageは
  次回起動からまとめて無効になり、配布ファイル・scene・個人設定は維持する。

- `bdControllerShape.shape` に94種類の形状を定義した。Gearを一覧の先頭、Cubeを
  初期値とし、矢印・フィン、部分template、軸色を含む複合形状を1つのshapeで描画する。
  `ColorSphere` は軸色の直交円だけを描き、`ColorCrossLine` と
  `ColorSphereCrossLine` の間に配置した。両者の間へ軸色の円と通常色の
  矢印を組み合わせた `ColorSphereArrow2D/3D` とその Filled 版を追加した。
  純線形状を除く44種類に `*Filled` を用意し、Gear の内円は穴、
  矢印・フィンは付属部分も面で描画する。template の本体面は選択不可にする。
- 共有`bakedanuki`メニューへ起動時自動表示のチェック項目を追加。既定はONで、OFFは次回起動から
  各packageの自動登録を抑止する。設定はMayaバージョンごとのユーザー設定へ保存する。
  共通`installer.py`の再D&Dでは、Module pathが登録済みでも確認後にONへ戻せる。
  既存設定がない環境ではONとして扱い、移行操作は不要。
- `bd_util.maya.ui`へ複数packageで共有する`bakedanuki`メインメニュー登録APIを追加。
  owner単位の解除、同一項目の再登録、batch時のUI作成抑止に対応する。
  利用者の`userSetup.py`、設定、sceneの移行は不要。
- `bd_util.maya.node.node_display_name()`を追加。一意なDAGノードは短名、同名ノードや
  インスタンスは指定したフルパス、DGノードはノード名をUI表示用に返す。
  追加APIのためscene・設定の移行は不要。
- `UiStateManager.register_combo_box()`を追加。候補の一意な文字列`itemData`を
  保存し、表示名や候補順が変わっても選択を復元する。保存値が現行候補にない場合は
  初期選択を維持する。既存の設定形式はそのまま利用でき、移行は不要。
- `bdUtilCommands`に`bdSetTranslateCompensateChildren`、
  `bdSetRotateCompensateChildren`、`bdSetRotateAxisCompensateChildren`、
  `bdSetJointOrientCompensateChildren`と型付きfacadeを追加。直接の子を補償し、
  local属性値またはworld位置・固定XYZ順の最終姿勢を設定する。移動のcm・回転の度と
  Maya表示単位を選べ、回転では子のworld位置を維持するかと子Jointの補償属性を選べる。
  複数ノードを一回のMaya Undoで処理する。追加APIのためscene・設定の移行は不要。
- `Transform`／`Joint`にsceneを変更せずlocal属性値とworld位置・固定XYZ順の
  最終姿勢を換算する`convert_transform_space_values()`を追加。
  `Joint`の`jointOrient`にも対応する。追加APIのためscene・設定の移行は不要。
- Bindingを持たない数値入力にも初回クリック時の全選択を利用できるよう、
  `MouseFocusSelectAllDoubleSpinBox`を`bd_util.ui`へ公開。既存の
  `FloatSpinBox`と`FloatStepSpinBox`の値管理は変更しない。
- `bdUtilCommands` に `bdSetRotationPreservingPose` と型付き facade
  `set_rotation_preserving_pose()`を追加。Transform／Joint の回転属性群へ共通の
  XYZ 値を設定し、別の属性群で差分を吸収して現在の姿勢を維持する。
  Joint は `rotateAxis` と `jointOrient` 間の補償にも対応する。
  複数ノードを一回の Maya Undo で処理し、途中失敗時は全体を復旧する。
  追加 API のため既存 scene・設定の移行は不要。
- Python プラグイン `bdUtilCommands` に、複数の Transform／Joint を対象とする
  `bdRoundTranslate`、`bdRoundRotate`、`bdRoundRotateAxis`、
  `bdRoundJointOrient` を追加する。NodeOperator の子補償を利用し、
  一回の Maya Undo／Redo と途中失敗時の復旧に対応する。型付き facade は
  `bd_util.maya.mpx_cmd.round_transform` から利用できる。
- `bd_util.maya.rounding` に十進四捨五入と Maya の cm／度・表示単位での
  丸めを共通化し、既存の数値属性 Binding と NodeOperator で共有する。
- `Transform`／`Joint`に`consolidated_rotation_values()`を追加。既存の回転集約と
  同じ検証・合成で集約先の角度をscene変更なしに取得し、Maya標準Undoを使うUIでも
  回転値を集約できる。既存API、scene、設定の移行は不要。
- `MayaFloatRoundEdit`を追加。複数float属性の各実値を現在の表示単位で十進四捨五入し、
  `apply_plugs_values()`から一括適用できる。0桁と正負の中間値、1回Undo・同値時の
  無Undoに対応する。公開APIの追加で、scene・設定の移行は不要。
- `selected_node_names(limit=...)`を追加。選択中の重複しないobject nodeが指定数に
  達した時点で取得を終える。省略時の全件取得、選択順、component・plugの除外、
  DAG instanceの重複除去は従来どおり。scene・設定の移行は不要。
- bool・float・enumの複数Maya属性Bindingと三つのscalar値貼り付けAPIへ
  `edit_connected=False`を追加。指定時は通常時間カーブ・SDK・Animation Layerに
  Maya標準の値入力を行い、時間キーとLayerはAuto Keyへ連動する。SDKは一時値のみ
  変更し、constraintを含む駆動とその他の未対応接続は編集しない。途中失敗では
  値と自動キー変更を復旧する。`MayaPlugTargetState.edit_description`と
  接続構成の入力不可理由を返す`connected_plug_edit_reason()`も公開する。
  既定の接続属性は読取り専用のまま。従来の常時キー編集は`key_animated=True`を
  維持し、標準入力へ移行する利用側は`edit_connected=True`へ置き換える。
  両方の同時指定は`ValueError`。scene・設定・clipboard schemaの移行は不要。
- `MayaNodeNameStore`と`MayaNodeNameBinding`を追加。単一の既存ノード名を正本とし、
  既存`StringLineEdit`と`StringLabel`から編集・共有表示できる。namespaceを維持し、
  Mayaの採番後の確定名、外部リネーム、Undo／Redo、編集可否、削除による終了を扱う。
  Shape名の追従は`rename_shapes=False`で抑止できる。固定ノードの編集サンプルを追加。
  既存API・scene・設定の移行は不要。
- `MayaPlugInputState`へ`driven_key`、`expression`、`animation_layer`、
  `animation_clip`、`muted`、`key_altered`、`nonkeyable`を追加。
  特殊な直結元、muteの有効状態、現在値とカーブ評価値、keyableフラグを読み取る。
  既存scene・設定の移行は不要。入力状態を網羅的に分岐している利用側は
  新しい7種類を扱うよう更新する。
- `MayaPlugTargetState.is_locked`で属性自身とcompound祖先の実効ロック状態を公開。
  入力接続の分類には`pair_blend`と`constraint`を追加し、直結元のノード型で
  親compoundへの接続も判定する。既存の`connected`はその他の接続を示す。
  scene・設定の移行は不要。利用側で入力状態を網羅的に分岐している場合は
  新しい2種類を追加する。
- Mayaの複数属性Bindingに`track_input_state`を追加し、各対象の
  `MayaPlugTargetState.input_state`で現在キー・時間カーブ・その他接続・未接続を
  読み取れるようにした。`inspect_plug_input_state()`も公開し、時刻・キー編集・
  接続変更に追従する。既定は追跡しないため既存利用側の動作は維持する。
  scene・設定の移行は不要。
- `nodes.create` に namespace 付きの名前と `namespace=` 指定を追加。
  未作成の namespace はノード実行時に作成し、Undo / Redo へ含める。
  `Nodes(namespace=...)` と `nodes.set_namespace()` で以後の作成先を設定でき、
  個別の `namespace=` または namespace 付きの名前を優先する。
- `node.move_to_namespace(namespace)` と
  `nodes.move_to_namespace(targets, namespace=...)` を追加。
  複数ノード版は `NodeOperator`・ノード名・`MObject` を混在して指定でき、
  全対象を検証した後に同じ `ModifierManager` の DG バッチへ移動を予約する。
- `inspect_scalar_attributes()`と状態Binding、複数属性編集、scalar値搬送へ
  単一typed string属性を追加。`MayaStringValueEdit`と
  `StringLineEdit.setValueRequestHandler()`を公開する。Clipboardの書込みschemaは
  version 2とし、従来のversion 1は引き続き読み込む。既存sceneの移行は不要。
- `MayaStringPlugsBinding`を追加。複数の単一typed string属性を先頭の値を代表として
  読み、明示入力時だけ編集可能な対象へ一回のUndoで適用する。混在、同値統一、
  空文字、対象ごとの編集可否、途中失敗の復旧、外部変更中の入力保護に対応する。
  複数jointの`.otherType`を対象とするサンプルを追加。既存scene・設定の移行は不要。
- 単一string値のMVVM基盤を追加。Python属性またはMaya typed string属性を正本とし、
  一行入力、共有ラベル、外部変更、Undo / Redo、編集中の競合検出に対応する。
  `joint.otherType`のサンプルを含む。Maya未設定値は空文字として扱い、
  既存API・scene・設定の移行は不要。
- `FloatSpinBox`と`FloatStepSpinBox`へ`select_all_on_mouse_focus`、
  `select_all_on_mouse_focus()`、`set_select_all_on_mouse_focus()`を追加。
  有効時は入力文字をマウスで初回フォーカスした左クリックだけ全選択し、再クリック、
  ドラッグ選択、矢印操作はQt標準動作を維持する。既定値は`False`。
  `FloatValueStepSpinBox`は値欄とStep欄を個別指定でき、`FloatSliderSpinBox`も値欄へ指定できる。
- `bd_util.ui.FloatStepProfile`、`FloatStepSetting`と
  `UiStateManager.register_float_step_profile()`を追加。任意の文字列keyと
  `number`／`distance`／`angle`の組ごとに、丸め前の正の有限Stepを保持する。
  複数項目の置換は一度だけ通知し、version付きJSONとして一つのUI stateへ保存する。
  不正な個別項目だけを除外し、未知versionや壊れたprofileは同じmanagerの他状態へ
  影響させず削除する。正本値、scene、Undo履歴は扱わない。
- `bd_util.maya.node`へ`ScalarAttributeDisplayFilter`、
  `matches_scalar_attribute_display_filter()`、`filter_scalar_attribute_paths()`を追加。
  scalar属性を`all`、`visible`、`keyable`、`channel_box`、`hidden`の共通規則で分類し、
  入力順を維持した正式pathを取得できる。sceneとclipboard schemaの移行は不要。
- `bd_util.ui.JsonClipboard`を追加。version付きの利用側schemaをcustom MIMEと
  marker付き`text/plain`へ同時保存し、別processでも復元できる。読込時は容量、UTF-8、
  JSON構文、重複key、非有限値を検証する。
- `bd_util.maya.ui`へ`MayaScalarValueTransfer`、型付きsnapshot、
  `MayaScalarValueClipboard`、取得・JSON変換・同path一括適用APIを追加。
  bool・数値・距離・角度・enumを公開単位で搬送し、正式な相対属性pathと型で照合する。
  欠落・型違い・enum定義違い・readonly属性を対象外として返し、適用対象は全件事前検証、
  一回Undo、途中失敗復旧で確定する。sceneと保存設定の移行は不要。
- `bd_util.maya.ui.apply_scalar_value_to_paths()`を追加。一つの型付き搬送値を、
  複数nodeの明示した複数正式pathへ展開する。数値・距離・角度・boolは同じ型区分、
  enumは同じ整数値・項目名定義だけを対象とし、既存の対象外理由・全件事前検証・
  一回Undo・途中失敗復旧を共用する。clipboard schemaと既存APIの移行は不要。
- `bd_util.maya.ui.capture_all_scalar_node_values()`と
  `apply_scalar_value_transfer_to_paths()`を追加。前者はnodeの対応scalar属性を表示状態に
  依存せず一括取得し、後者は複数搬送値から指定した正式pathとの共通部分だけを複数nodeへ
  適用する。clipboardにない指定pathは対象外理由へ含め、行順による対応付けは行わない。
  clipboard schemaと既存sceneの移行は不要。
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

- Windowsなどの遅延生成されるメニューへ`bakedanuki`を配置すると、標準項目が
  生成されなくなる問題を修正。配置先の初期化後に末尾へ追加し、既存項目と
  元の`postMenuCommand`・`postMenuCommandOnce`を維持する。
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
