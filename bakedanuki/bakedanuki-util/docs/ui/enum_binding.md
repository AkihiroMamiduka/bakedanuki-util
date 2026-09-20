# enum binding

Python属性またはMaya enum属性の整数値を正本とし、コンボボックス・ラジオボタン・表示ラベルで共有します。
値は`int`、同期と選択肢の管理は`EnumViewModel`が担当します。
Pythonの`Enum`／`IntEnum` classを作る必要はありません。

今回の実装は複数Mayaプラグの一括編集まで完了しています。
完了範囲・設計判断・拡張時の注意点・確認記録は
[enum MVVMの到達点と今後の拡張](enum_roadmap.md)を参照してください。

## Python属性を正本にする

```python
from dataclasses import dataclass

from bd_util.ui import EnumBinding, EnumComboBox, EnumDefinition, EnumLabel, qt


@dataclass
class Settings:
    mode: int = 5


class ModeWidget(qt.QWidget):
    def __init__(self, data: Settings, parent=None):
        super().__init__(parent)
        definition = EnumDefinition.from_mapping(
            {0: "Off", 5: "Preview", 10: "Final"}
        )
        self.binding = EnumBinding.from_attribute(
            data, "mode", definition=definition, parent=self
        )
        self.combo_box = EnumComboBox(self.binding, self)
        self.label = EnumLabel(self.binding, self)
        layout = qt.QHBoxLayout(self)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.label)
```

属性への直接代入後は`binding.refresh()`で読み直します。
`set_value()`とViewからの入力はsetter適用後の実値を採用します。
dataclass、slots、property、descriptorを扱い、frozen dataclassとsetterのないpropertyは
表示専用です。getter失敗や不正な型で読み直せなくなった場合は入力を停止し、
属性の修復後に`refresh()`すると復帰します。Python単独の変更はMaya Undoへ登録しません。

## Maya属性を正本にする

```python
import bd_util as bdu
from bd_util.maya.ui import MayaEnumPlugBinding
from bd_util.ui import EnumComboBox

nodes = bdu.Nodes()
node = nodes.existing.transform("pCube1")
binding = MayaEnumPlugBinding(node.rotateOrder, parent=owner)
combo_box = EnumComboBox(binding, parent=widget)
binding.set_value(node.rotateOrder.ZYX)
```

`wheel_requires_focus=True`を指定すると、フォーカスのないComboBox上のホイールを
値変更に使わず、親Widgetへ渡します。クリック・Tabでフォーカスを得た後は変更できます。
生成後は`wheel_requires_focus()`と`set_wheel_requires_focus()`で切り替えられます。

`owner`はBindingの寿命を管理するQObject、`widget`はViewを配置するQWidgetです。
名前から取得する場合は`resolve_enum_plug("settings", "mode")`を使用します。
長名、短名、compound内のscalar enumの相対pathを解決します。
配列と配列要素、および配列配下のcompound子は対象外です。

作成時はMayaの現在値と実際の属性定義を読み、初期値を書き戻しません。
標準属性と追加属性の両方に対応します。生成classの`NAME_MAP`ではなく、シーン上の
項目定義を優先します。整数値はOpenMayaの`MPlug.asShort()`から読み取ります。
項目一覧は標準属性の`attributeQuery(listEnum=True)`または追加属性の
`addAttr(query=True, enumName=True)`から読み、値と項目名を`MFnEnumAttribute`で確認します。
飛び番や負数を含む定義を扱い、定義文字列が同じ場合は解析結果を再利用します。

Viewからの変更は`cmds.setAttr()`で即時確定し、MayaのUndo／Redoに追従します。
ModifierManagerへ操作を積む`EnumPlugOperator.set()`は、この即時編集には使いません。
外部変更はcallbackから読み直し、同じ値を書き戻しません。
lock、親compoundのlock、入力接続は編集を無効化しますが、読み取りと表示は継続します。
上流のdirty通知後は次のQt event loopで値を読み直します。

## 複数のMaya属性を一括編集する

`MayaEnumPlugsBinding([plug_a, plug_b], parent=owner)`を同じEnum Viewへ渡せます。
先頭の値・選択肢を表示し、ユーザー入力時だけ編集可能な対象へ同じ整数値を適用します。
構築・refresh・外部変更では他の属性へ書き戻しません。
全対象で整数値と項目名の対応を一致させ、実行中の不一致では一括入力を停止します。

`is_mixed`、`target_states`、`writable_count`、`state_changed`で混在や入力可否を表示できます。
`apply_representative_value()`は代表と同値の入力を明示的に全対象へ適用します。
詳細とサンプルは[複数プラグ基盤](plugs_binding.md#enum属性群)を参照してください。

## Python正本とMayaを双方向同期する

```python
from bd_util.maya.ui import MayaEnumBinding, resolve_enum_plug

binding = MayaEnumBinding.from_attribute(
    data,
    "mode",
    definition=definition,
    maya_plug=resolve_enum_plug("settings", "mode"),
    parent=owner,
)
```

初期同期はPythonからMayaへ行います。項目定義はPython側で明示し、Maya側と
**値と項目名の対応が一致すること**を要求します。項目の表示順は比較しません。
項目名の別名変換やMayaのenum定義の書き換えは行いません。
初期不一致は例外となり、構築中のcallbackを解除します。
`maya_plug=None`ではPythonとQtのみを接続します。

Maya入力はcallback中に書き戻さず、次のQt event loopでCommandへ渡します。
同値のPython Commandや`refresh()`も、先に届いていた未処理のMaya入力より優先します。
Mayaのlock、入力接続、定義不一致ではPython正本を維持し、Python側の編集を継続します。
定義や書き込み可否が復旧した後はPython値を再同期します。

`binding.maya_view`は`is_synchronized`、`last_sync_error`、`sync_failed`、
`sync_from_view_model()`を公開します。同期失敗はPythonの変更を巻き戻しません。
Undo／Redoで復元された値がPythonのsetterで補正された場合、復元値への再書き込みを
保留してRedo履歴を維持します。Python Command、`refresh()`、明示再同期で再適用できます。
PythonとMayaをまとめたUndo transactionは提供しません。
1つのViewModelに接続できるMaya Viewは1つです。

## 値・定義・通知

Binding構築前に対象の定義を比較する場合は、`bd_util.maya.ui`の
`read_enum_definition(resolve_enum_plug(node_name, attribute_path))`を使います。
現在のMaya属性から`EnumDefinition`を取得し、callbackの登録やscene・値・Undoの変更は
行いません。生成classの`NAME_MAP`ではなく、呼び出した時点の実定義を読みます。
`definition.matches(other)`で表示順に依存しない値と項目名の一致を判定できます。

| API | 内容 |
| --- | --- |
| `EnumItem(value, name)` | 整数値と空でない項目名。不変データ |
| `EnumDefinition(items)` | EnumItemのtuple。値と項目名はそれぞれ一意 |
| `EnumDefinition.from_mapping({value: name})` | mappingの順序を保って定義を作る |
| `definition.item_for_value(value)` | 対応するEnumItem。未定義ならNone |
| `EnumValueStore` | read／write、definition、is_available、is_writableの契約 |
| `binding.value` / `changed` | 最後に同期した整数値と、実値が変わったときの通知 |
| `binding.definition` / `definition_changed` | 最後に同期した選択肢と、その変更通知 |
| `binding.is_value_defined` | 公開値が現在の選択肢に含まれるか |
| `binding.set_value(value)` | 変更要求。正本の実値が変わったかboolで返す |
| `binding.refresh()` | 値・定義・編集可否の再取得。公開値が変わったか返す |
| `binding.store.instance` | Python正本のobject。具体型とIDE補完を維持する |
| `binding.dispose()` | 入力と同期を終了する |

Python属性には生成時の不変な定義を指定します。実行中に定義を変更する独自Storeは、
新しい`EnumDefinition`を返した後に`refresh()`を呼びます。Maya Storeでは通常の
`addAttr(edit=True, enumName=...)`とUndo／Redoのcallbackで再取得します。
独自plug-inなど通知を出さない経路で定義を変えた場合も、`refresh()`で再取得できます。

項目名だけの変更では`definition_changed`だけを通知します。
値と定義は通知前に一緒に確定し、通知slotから読み取る状態の不一致を防ぎます。
Valueは読み取り専用で、変更はCommandを通します。Storeなしの低レベル利用では
`EnumViewModel(value=5, definition=definition)`でメモリ上の値を扱えます。

## 未定義値とView

Maya enumには飛び番の間の未定義値が入ることがあり、選択中の項目を定義から削除しても
現在値は残ります。この基盤では、書き込み要求は定義内の整数に限定し、読み取りでは
正本の未定義整数をそのまま保持します。自動clampや先頭項目への置換は行いません。
bool、float、文字列、Noneからの暗黙変換は拒否します。

`EnumComboBox`と`EnumLabel`は未定義値を`未定義 (5)`のように表示します。
ComboBoxのcurrentIndexは-1になり、有効な項目を選ぶことで正本を修正できます。
空の定義は表示可能ですが、Commandと入力Viewを無効化します。
setterが返した未定義整数も正本の確定値として表示します。

Viewは`EnumBinding[EnumValueStore]`または`EnumViewModel`を受け取ります。
同じBindingを複数のViewへ渡せます。ComboBoxの位置はenumの整数値と独立し、
各itemDataは`EnumItem`です。`currentData().value`で整数値を取得できます。
Python整数をQtの固定幅整数へ狭めず、Maya側だけがenumのshort値を扱います。
ラベルは項目名をplain textで表示し、文字の選択・コピーを許可します。

`combo_box.setInputEnabled(False)`はそのViewからの編集だけを停止します。
他Viewからの変更と表示更新は継続し、Storeのlock解除後もこの設定を維持します。
表示更新はsignalを抑制して行い、Commandへ折り返しません。

Bindingは専用ViewModelと内部生成したMaya adapterを所有します。外部Storeの所有権は
移しません。ViewはBindingを参照保持しますが、閉じたViewが共有Bindingを終了することは
ありません。共有する場合は各Windowから独立したownerを指定してください。
node／対象属性削除ではcallbackを終了し、削除Undo後は新しいBindingを作ります。
Maya Viewだけが終了した場合はPythonの編集を継続できます。

## ラジオボタンで選択する

```python
from bd_util.ui import EnumRadioButtonGroup, qt

radio_group = EnumRadioButtonGroup(binding, parent=widget)
vertical_group = EnumRadioButtonGroup(
    binding, parent=widget, orientation=qt.Qt.Orientation.Vertical
)
```

`EnumRadioButtonGroup`も同じBindingまたはViewModelを受け取り、3種類の正本・同期方式で
共通に使用できます。`orientation`の既定は`Horizontal`です。配置方向は構築時に指定し、
`orientation()`で取得します。

ボタンは定義順に並び、位置やQtのbutton IDとは独立したPython整数でCommandへ渡します。
負数・飛び番・大きなPython整数も扱えます。項目名の`&`は文字として表示します。
未定義値では全ボタンの選択を解除し、定義が空でなければ選び直せます。
未定義の整数値も表示したい場合は、同じBindingの`EnumLabel`を併置してください。
定義の変更はボタンの追加・削除・名前・順序へ反映し、値を書き戻しません。

`buttons`は現在の定義順の`tuple[QRadioButton, ...]`、
`button_for_value(value)`は対応するボタンまたは`None`を返します。
定義変更時はボタンを作り直すため、ボタン参照を長期間保持せず必要時に取得してください。
値の変更には`binding.set_value()`を使い、ボタンの`setChecked()`は使いません。
選択済みボタンをクリックした場合も同値のCommandを実行します。

`setInputEnabled(False)`はそのViewの入力だけを停止し、表示更新は継続します。
Storeのlock解除後もこの設定を維持します。setterの拒否・補正・例外時には正本の実値へ
選択を戻し、Bindingの終了時には入力を無効化します。

## サンプルと検証

```python
from bd_util._sample.maya.ui.enum_sample import minimal, maya_plug, maya_view

window = minimal.show()  # nodeを作らずPython属性を共有する
window.data.mode = 1
window.binding.refresh()  # 未定義値を表示する

window = maya_plug.show("pCube1")  # rotateOrderの現在値を正本にする
window = maya_view.show("pCube1")  # Python初期値5をrotateOrderへ適用する
```

任意の追加属性は`maya_plug.show("settings", "mode")`で指定します。
Python正本のサンプルでは`maya_view.show(..., definition=definition)`で対応する定義を
渡せます。各moduleの`dispose()`で終了します。Maya nodeは作成・削除しません。
全サンプルに横並び・縦並びのラジオボタンを配置し、コンボボックス・ラベルと共有します。

- `tests/ui/test_enum_binding.py`: 型、属性、共有View、未定義値、通知、寿命。
- `tests/ui/test_enum_radio_button_group.py`: 配置、定義変更、整数値、入力可否、寿命、Maya Undo／Redo。
- `tests/ui/test_enum_sample.py`: サンプルの共有と終了。
- `tests/maya/ui/test_enum_plug_binding.py`: 実定義、Undo／Redo、callback、lock・接続。
- `tests/maya/ui/test_enum_plug_view.py`: 双方向同期、定義不一致、Python正本の保持。
- `tests/maya/ui/test_enum_plugs_binding.py`: 複数属性の定義一致、混在、Undo、失敗復旧、寿命。
- `tests/ui/test_enum_plugs_binding_views.py`: 一括編集用Viewとサンプル。
- `tests/typecheck/enum_binding_contract.py`: 公開APIと正本objectの型・補完。

最終検証は`scripts/verify.cmd`を使用し、Maya 2025／2026／2027の型・UI互換性を確認します。
