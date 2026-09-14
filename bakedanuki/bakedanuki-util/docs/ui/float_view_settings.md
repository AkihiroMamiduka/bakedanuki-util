# Min／Max・stepの保存と復元

`FloatRangeSliderSpinBox`と`Float3RangeSliderSpinBox`の操作設定を、既存の`UiStateManager`へ
明示登録して保存できます。登録しないViewは従来どおり、生成時の設定を使用します。

## 登録とWindowの寿命

通常Windowでは、Viewを構築してから保存対象を登録し、初回表示前にtrackerを接続します。
以下の`editor`は単一値View、`axes_editor`は3成分View、`window`はそれらを所有するWindowです。

```python
from bd_util.maya.ui import MayaUiStateTracker, create_ui_state_manager

window.editor_settings = create_ui_state_manager("my_tool/editor_settings/main")
window.editor_settings.register_float_range_slider_spin_box("value", editor)
window.editor_settings.register_float3_range_slider_spin_box("translate", axes_editor)
window.editor_settings_tracker = MayaUiStateTracker.for_window(
    window.editor_settings, window
)
```

dockable Windowでは最後の行を`MayaUiStateTracker.for_dockable(manager, window)`に置き換えます。
managerとtrackerはWindowのメンバーとして保持してください。

通常Windowは初回Show後、dockable Windowは初回dock接続後に、Qtのevent loopで復元します。
同じWindowを隠して再表示する場合は再適用しません。close・完全破棄・Maya終了時には、
変更通知で退避済みの確定設定を保存します。Bindingが先に終了しても、終了前の退避値を使用します。
trackerを手動で`dispose()`する場合、必要な保存はその前に`save()`で行ってください。

独自の寿命管理では`manager.restore()`、`save()`、`save_cached()`を直接使用できます。
`save()`は生存中のViewを読み取り、`save_cached()`は退避値だけを保存します。
両方とも保存結果をboolで返すので、ツール側で失敗の表示や再試行を扱えます。
保存先の準備はBinding構築より先に行うと、保存先へのアクセス失敗時にMaya callbackを残さずに済みます。

## 保存先とキー

Mayaのversion別preferences内にある、既存のtool単位の`ui.ini`を使用します。
ファイルは`manager.file_name`で確認できます。Window配置とは**別のsettings_path**へ登録してください。

| 用途 | settings_pathの例 |
| --- | --- |
| Window配置、Splitter、Tab | `my_tool/windows/main` |
| Min／Max・step | `my_tool/editor_settings/main` |

この分離により、`reset_ui_layout()`／`reset_and_show_ui_layout()`へWindow配置のpathを渡しても、
Min／Max・stepは保持されます。同じpathへ混在させると、配置リセットで数値設定も削除されます。

keyは固定のASCII Python識別子です。node名やUUIDをkeyにせず、tool・Window・Viewの役割で決めます。
別nodeを表示しても同じViewの操作設定を再利用します。同じBindingを共有するViewも別keyに登録してください。

3成分の`"translate"`は`"translate_x"`・`"translate_y"`・`"translate_z"`へ展開されます。
`registered_keys`と`restore()`の返り値も展開後のkeyです。登録時は全軸の重複・寿命を検証してから追加します。
単一値側で同名keyを使わないでください。`restore()`は成功したkeyだけを`frozenset[str]`で返します。

## 保存する値と単位

| 項目 | 内容 |
| --- | --- |
| Min・Max | 行の`floatRange()`が返す、公開単位の丸め前の範囲 |
| step | 行の`singleStep()`が返す、表示単位で解釈する数値 |
| 形式version・単位種別 | 読み取り時の互換性判定用 |

距離の公開単位はcm、角度はdegree、通常数値は単位なしです。
例えば範囲±100 cmは、表示単位をmへ変更して再起動すると±1 mと表示します。
stepは数値を維持する既存仕様に従い、0.1 cmで保存したstepも、m表示では0.1 mになります。

範囲はMin／Max欄の表示値や`effectiveFloatRange()`から取得しません。
表示0桁でも設定精度を保ち、現在のhard limitで操作できなくてもユーザーの範囲を保持します。
復元後の操作可能範囲・範囲外表示・入力可否は、現在のBindingとViewの既存仕様で決まります。

現在値、hard limit、表示桁数、幅、enabled、ボタンや単位文字の表示、stepモード、
step欄自身の増減幅、Slider分割数は保存しません。これらは従来どおり構築時の設定を使用します。
保存・復元は正本を変更せず、MayaのUndo履歴にも追加しません。

単位種別は`FloatPresentation.unit_kind`で表し、型は
`FloatUnitKind = Literal["number", "distance", "angle"]`です。
Maya連携では属性型から自動で設定します。PythonのみのBindingは既定が`"number"`で、
距離・角度として扱う場合は公開値をcm・degreeに揃え、presentationへ種別を明示してください。
suffixやscaleからは種別を推測しません。

## 確定通知と不正データ

単一値Viewの`settingsChanged`は、確定した範囲・step・単位種別が変わったときに通知します。
UI編集と`setFloatRange()`／`setSingleStep()`の両方が対象です。
現在値のドラッグ、未確定テキスト、表示単位や表示桁数だけの変更では通知しません。
3成分では各`x_editor`／`y_editor`／`z_editor`が独立して通知します。
複合Viewのstepをコードから変更するときは、子の現在値欄ではなく行の`setSingleStep()`を使います。

通知ではmemoryへの退避だけを行い、ファイルへの書き込みはsave時にまとめます。
Mayaの属性型や値を保存用に再取得せず、各ドラッグ位置の同期経路にも保存処理を追加しません。

内部形式は既存の`ui_state/widgets/<key>`配下にある型識別子とQByteArrayです。
QByteArray内のJSONには`version=1`、`unit_kind`、`minimum`、`maximum`、`single_step`を格納します。
読み取り時にversion・種別の一致、有限な範囲、Min < Max、stepの正数・表現可能範囲、
現在の表示単位への変換可能性を全て検証してから、1行へ適用します。
不正な行は設定を適用せず保存データを除去し、現在の設定を維持します。初回復元なら生成時設定が残ります。
他View・他軸の有効な保存データは引き続き復元します。形式全体の未知schemaは既存managerの仕様で無視します。

## 開発時の引き継ぎ

### 既定値・保存キー・形式を変更するとき

登録時にはその時点の設定も退避するため、ユーザーが編集していない初期設定も終了時に保存します。
有効な保存値がある場合は、次のWindow生成時に引数で指定したMin／Max・stepより保存値が優先されます。
サンプルや製品の既定値を変更して確認するときは、一時INIなど保存値のない環境と、既存設定のある環境の両方を使用してください。

settings_path・key・XYZへ展開するkeyは保存データの識別子です。変更しても旧データを自動で移動・削除しません。
既存設定を引き継ぐなら移行処理を用意し、引き継がないなら新しい識別子を使う意図を明確にします。
同じkeyの役割や公開単位を変更するときは、旧設定を誤って適用しないかも確認してください。

manager全体の`SCHEMA_VERSION`と、各行のJSONの`version`は別のものです。
範囲・stepの保存形式を拡張する場合は、まず行のadapter内で互換性・移行・拒否方針を決め、
SplitterやTabにも影響するmanager全体のschema変更が必要か判断してください。
現在は旧形式からの自動移行を提供せず、対応外の行versionは不正な行として削除します。

`FloatPresentation`の等価比較には`unit_kind`も含まれます。
表示倍率・suffix・hard limitが同じでも、距離・角度・通常数値の種別が違えば別のpresentationです。
Maya adapterを変更した場合は、種別の引き継ぎと、比較するテストの期待値も確認してください。

### リセットと終了処理を拡張するとき

`manager.clear()`はそのsettings_pathの`ui_state`全体と、そのmanagerの退避値を消去します。
登録したViewや画面上のMin／Max・stepは変更しません。1行だけの削除APIでもありません。
表示中の設定を保持したまま`save()`や設定変更を行うと、その設定が再び保存対象になります。
別managerのmemory内の退避値も消去しないため、終了前保存との順序にも注意してください。
将来の初期設定リセットでは、対象Viewへの初期値適用と次回起動時の保存結果を一緒に検証します。

終了時は退避済みの値を使う構成を維持します。新しいadapterでも、QWidgetが生存しているだけで
Bindingも利用できるとは判断せず、取得不能なら退避値と保存済みデータを保持してください。
設定変更通知を追加する場合も、現在値のドラッグごとの再取得やファイル書き込みは増やさない方針です。

### 実装の入口

以下は内部実装の参照先です。ツールからは上記の公開登録APIとViewのsetterを使用します。

| 変更内容 | 主な参照先 |
| --- | --- |
| 確定設定の通知 | [FloatRangeSliderSpinBox](../../python/bd_util/ui/binding/float/view/range_slider_spin_box.py) |
| 行の保存形式・単位判定・事前検証 | [FloatRangeStateAdapter](../../python/bd_util/ui/_float_view_state.py) |
| 登録・XYZ展開・退避・保存 | [UiStateManager](../../python/bd_util/ui/ui_state.py) |
| Window／dock／Maya終了との接続 | [MayaUiStateTracker](../../python/bd_util/maya/ui/ui_state.py) |

## サンプルと確認

`float_sample`と`float3_sample`の`maya_plug.py`・`maya_view.py`・`minimal.py`は保存を有効にしています。
pathは`float_sample/editor_settings/<sample>`または`float3_sample/editor_settings/<sample>`です。
例えば、既存transformに対して次のように設定します。

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
window.widget.translate.x_editor.setFloatRange(-250, 250)
window.widget.translate.x_editor.setSingleStep(2.5)
```

Windowを閉じてから再度`maya_plug.show("pCube1")`を呼び、範囲とstepが復元されることを確認します。
UI上から編集できる欄でも同じ動作です。Pythonサンプルの正本データの生成・初期同期は従来どおりです。
Maya再起動後の復元、cm／m・deg／rad変更、他View・他軸の独立性も手動確認の対象です。

自動テストは`tests/ui/test_float_view_settings.py`と`test_float_view_settings_maya.py`で、
精度、不正データ、単位、正本・Undo不変、Window再生成、配置リセット、終了通知とdock通知を検証します。
実際のMaya process終了やworkspaceControl表示は自動テストに含みません。
サンプルのテストでは一時INIへ差し替え、ユーザーの保存設定は変更しません。
ドラッグ時のMaya読み取り回数は`test_float3_slider_spin_box_maya.py`で登録済みViewも確認します。
