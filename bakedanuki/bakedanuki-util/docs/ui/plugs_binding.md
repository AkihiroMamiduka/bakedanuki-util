# 複数のMaya属性を一つの入力で編集する

`MayaBoolPlugsBinding`、`MayaFloatPlugsBinding`、`MayaEnumPlugsBinding`は、順序付きの属性群を既存の
`BoolComboBox`、`FloatSpinBox`、`FloatSliderSpinBox`、`EnumComboBox`、`EnumRadioButtonGroup`などへ接続します。
先頭属性を代表として表示し、ユーザーの入力時だけ編集可能な対象へ同じ値を適用します。

```python
from bd_util.maya.ui import MayaFloatPlugsBinding, resolve_float_plug
from bd_util.ui import FloatSpinBox, qt

owner = qt.QWidget()
binding = MayaFloatPlugsBinding(
    [resolve_float_plug(name, "tx") for name in ("pCube1", "pCube2")],
    parent=owner,
)
editor = FloatSpinBox(binding, owner)
binding.set_value(10.0)  # 全対象のtranslateXを10cmへ設定する
```

属性の列挙、表示条件、選択順、同名属性の組み合わせは利用側が決めます。
Bindingは空の属性群、重複する実体、非対応型を拒否します。
floatの数値・距離・角度の単位種別は全対象で一致させてください。
異なるnodeや長名・短名から解決した属性も、同じ単位種別なら扱えます。

## 公開する状態と操作

| API | 内容 |
| --- | --- |
| `value` / `changed` / `view_model` | 代表の確定値と、既存Viewへの接続先 |
| `set_value(value)` | 編集可能な対象へ絶対値を適用し、変更があればboolで返す |
| `apply_representative_value()` | 代表の現在の未丸め実値を他の編集可能な対象へ揃える |
| `is_mixed` | 利用可能な対象の値が代表と異なるか |
| `target_count` / `writable_count` | 登録した対象数と、個別に書込み可能な対象数 |
| `target_states` | 対象順の`tuple[MayaPlugTargetState, ...]` |
| `state_changed` | 対象値、混在、編集可否の変更を引数なしで通知するsignal |
| `edit_failed` | 入力拒否や実行失敗の説明をstrで通知するsignal |
| `refresh()` / `dispose()` | 全対象の再同期とcallbackの明示終了 |

`MayaPlugTargetState`はimmutableな`name`、`is_available`、`is_writable`、
`reason`を持ちます。`name`は同名DAGを区別する属性名です。
後続の削除・lock・入力接続はその属性だけを入力対象から除外します。
代表が書込み不可の場合は全体の入力を止めます。この場合も`writable_count`は
個別に書込み可能な対象数を示すため、0になるとは限りません。
アニメーション接続を含む入力接続は、キーを暗黙に変更せず読取り専用です。

`changed`は代表値の変更通知です。代表値を変えず後続だけが変わる入力では、
`state_changed`を用いて混在表示や件数を更新してください。
readonlyの後続に異なる値が残る場合、入力後も`is_mixed`はTrueです。
既存のComboBoxやSpinBoxは未変更の入力をCommandにしません。
表示と同じ値へ揃える操作は、明示的なボタンなどから
`apply_representative_value()`を呼び出してください。
`EnumRadioButtonGroup`は選択済みボタンのクリックもCommandへ渡すため、
現在選択中の項目をクリックして揃えることもできます。

## enum属性群

```python
from bd_util.maya.ui import MayaEnumPlugsBinding, resolve_enum_plug
from bd_util.ui import EnumComboBox, EnumLabel, EnumRadioButtonGroup

binding = MayaEnumPlugsBinding(
    [resolve_enum_plug(name, "rotateOrder") for name in ("pCube1", "pCube2")],
    parent=owner,
)
combo_box = EnumComboBox(binding, parent=widget)
radio_group = EnumRadioButtonGroup(binding, parent=widget)
label = EnumLabel(binding, parent=widget)
binding.set_value(5)  # 編集可能な全対象のrotateOrderをzyxへ設定する
```

`owner`はBindingを所有するQObject、`widget`はViewの親QWidgetです。
生成済みの`node.rotateOrder`など、型付きEnumPlugOperatorの列も指定できます。
scalar enumと配列配下ではないcompound子に対応し、配列・配列要素は対象外です。
標準属性と追加属性を同じAPIで扱います。

全対象で**整数値と項目名の対応**を一致させてください。項目の並び順は一致条件に含めず、
先頭属性の定義順で表示します。構築時の不一致は、ロックされた対象も含めて例外にします。
実行中に利用可能な対象の定義が不一致になった場合は、全体のCommandを無効化します。
不一致の対象は`target_states`の`is_writable=False`と`reason`で確認できます。
定義が再び揃えば入力を再開し、削除済み対象の定義は比較から除外します。
定義そのものや項目名を自動で変更しません。

`writable_count`はロック・接続・定義不一致を除いた対象数です。
代表のロックや定義不一致でグループ全体が停止している間も、0とは限りません。
グループの入力可否は`view_model.set_value_command.can_execute`を参照してください。
定義変更も`state_changed`で通知します。`definition`／`definition_changed`は代表の定義、
`is_mixed`は整数値の混在を示します。

負数・飛び番・未定義の現在値は、[単一enum基盤](enum_binding.md)と同じように保持します。
`set_value()`と`apply_representative_value()`で新たに書き込めるのは定義内の整数だけです。
未定義の代表値を揃える要求は、書込み前に例外にします。
入力直前にも定義を再確認し、先行する書込みのcallbackが後続の定義を変更した場合は
残りの入力を停止して値を復旧します。外部処理が変更した定義の書き戻しは行いません。

Maya属性群が正本なので、Python正本用の`MayaEnumPlugView`は追加接続できません。
同じBindingをQt View間で共有して使用してください。

## 表示と入力の分離

構築、`refresh()`、単位変更、外部操作、Undo／Redo、混在状態の更新では
Maya属性へ書き戻しません。`changed`を別属性の書込みへ接続して同期させる構成は
不要です。選択変更で対象を変える場合は古いBindingを`dispose()`し、作り直します。

floatの公開単位は単一属性Bindingと同じで、距離はcm、角度はdegreeです。
表示の単位・hard min/maxは先頭属性の`FloatPresentation`を保ちます。
後続の範囲に合わせて表示をクランプせず、代表の実値をそのまま確認できます。

入力時は編集可能な全対象のhard min/max、有限値、float32の格納範囲を
**書込み前に**検証します。後続の範囲に違反する入力は`edit_failed`で説明し、
例外を送出します。silent clampや一部の対象だけへの範囲内適用は行いません。
Sliderに代表の範囲を使った場合もこの検証は同じです。
soft limitは入力制限に使いません。

## 異なる属性群を一操作で編集する

複数行の値をまとめて確定する場合は、`bd_util.maya.ui.apply_plugs_values()`へ
型付きの入力を並べます。一つの`MayaFloatPlugsBinding`では単位種別を揃えたまま、
Binding間では距離・角度・単位なしの数値、bool、enumを混在できます。

```python
from bd_util.maya.ui import MayaFloatValueEdit, apply_plugs_values

# tx_bindingとrx_bindingは、それぞれの行が所有するMayaFloatPlugsBinding
display_value = 5.0
changed = apply_plugs_values(
    [
        MayaFloatValueEdit(
            tx_binding,
            tx_binding.view_model.presentation.from_display(display_value),
        ),
        MayaFloatValueEdit(
            rx_binding,
            rx_binding.view_model.presentation.from_display(display_value),
        ),
    ]
)
```

`MayaBoolValueEdit(binding, bool)`、`MayaFloatValueEdit(binding, float)`、
`MayaEnumValueEdit(binding, int)`を受け取り、union型は`MayaPlugsValueEdit`です。
値は各Bindingの公開単位で指定します。画面の同じ数値を入力する場合は、上記のように
**各行の**`presentation.from_display()`を使用してください。距離がm、角度がradの
表示でも、それぞれ画面上で5になります。各行の未丸め代表値へ揃える場合は、
対応するEditへその行の`binding.value`を渡します。

利用側は選択行と入力可能な行を決め、明示入力だけをこのAPIへ渡します。
APIは全要求の型・範囲・enum定義を実書込み前に検証し、対象群をまたぐ差分を
一回のUndoで適用します。空入力・全て同値の入力はFalseを返し、Undoを追加しません。
同じBindingまたは同じplugを二度含む要求は、無変更の対象も含めて変更前に拒否します。
各行の後続readonly属性は既存仕様どおり除外します。代表が削除・lock・接続・
enum定義不一致などで編集不可の場合は、他行も含めて例外で停止します。

各書込み直前にも状態・範囲・単位・enum定義を確認し、途中失敗では先に成功した
別行も含めて今回の入力を復旧します。対象の外部lockやenum定義を自動で元に戻しません。
復旧にも失敗した場合は`ExceptionGroup`を送出し、各Bindingの`edit_failed`へ通知します。
このAPIは単発の確定入力です。複数行にまたがる連続ドラッグのUndo集約は行いません。

## Undo、失敗復旧、終了

bool・enum・数値の確定は対象群をまとめてUndo一回になります。
floatのドラッグは、各位置を全対象へ即時反映し、全ドラッグをUndo一回にまとめます。
全てが同じ格納値になる要求では書込みやUndoを追加しません。
代表と同値でも後続に差分がある場合は、一括入力を実行します。

適用途中で失敗した場合、今回の入力で変更した対象を同じUndo chunk内で
元へ戻します。ドラッグでは直前の成功した位置を維持し、ドラッグを終了します。
復旧処理も失敗する外部変更があった場合は、元の失敗と復旧失敗を
`ExceptionGroup`として通知します。復旧に成功した失敗操作は、値を変えない
Undo項目として残る場合があります。既存のUndo履歴を削除して隠しません。

callbackはBinding内でnodeごとにまとめ、各callbackへそのnodeの対象だけを渡します。
複数選択でも通知のたびに全nodeの対象を走査しません。同じnodeの複数属性も維持します。
dirty通知は対象plugとcompound祖先だけを照合し、関係するBindingの再読取りを
次のQt event loopへ集約します。無関係な属性のdirtyでは値・編集可否・ViewModelを更新しません。
接続先の再計算やアニメーションによるdirtyも同じ対象判定で同期します。
単位変更・Undo／Redo・明示的な`refresh()`では従来どおり全対象を再同期します。
対象削除は無効状態として保持し、削除Undoや同名再作成へ自動再接続しません。
明示終了・Qt ownerの破棄・Maya終了でcallbackと開いているUndoを解除します。
選択変更やWindow closeを所有するcontrollerは、Viewを破棄する前にBindingを終了させてください。

## 検証

既存のノードを使うenumサンプルです。起動時に値を揃えたり、ノードを作成・削除したりしません。

```python
from bd_util._sample.maya.ui.enum_sample import maya_plugs

window = maya_plugs.show(["pCube1", "pCube2"])
# 追加属性の場合: maya_plugs.show(["settingsA", "settingsB"], "mode")
```

ComboBox・RadioButtonGroup・Labelに加え、混在、編集可能件数、対象ごとの除外理由を表示します。
「代表値に揃える」は明示入力、Refreshは読取り専用です。`maya_plugs.dispose()`で終了します。

- `tests/maya/ui/test_plugs_binding.py`: 無書込み初期表示、混在、同値揃え、範囲、
  単位、lock・接続、単発・連続Undo、部分失敗の復旧、削除とcallback解放。
- `tests/ui/test_plugs_binding_views.py`: 既存ComboBox・SpinBox・Sliderとの接続。
- `tests/typecheck/maya_plugs_binding_contract.py`: 状態APIと既存Viewへの受け渡し型。
- `tests/maya/ui/test_plugs_value_edits.py`: 異単位・異種・複数行の一括入力、全件事前検証、
  readonly、重複拒否、一回Undo、全行の失敗復旧。
- `tests/typecheck/maya_plugs_value_edits_contract.py`: 型付き入力とunionの補完契約。
- `tests/maya/ui/test_enum_plugs_binding.py`: enum定義の一致・変更、未定義値、混在、Undo、途中失敗、寿命。
- `tests/maya/ui/test_plugs_binding_notifications.py`: 無関係なdirtyによる再読取りの抑止、
  接続先・計算出力・時間変更の同期、親compound、同一nodeの複数対象、削除と遅延同期の終了。
- `tests/ui/test_enum_plugs_binding_views.py`: enum Viewの共有、同値選択、複数プラグのサンプル。
- `tests/typecheck/enum_binding_contract.py`: enum属性群の値・状態・Viewへの受け渡し型。

開発中はtargeted pytest、最終確認は`scripts/verify.cmd`を使用します。
