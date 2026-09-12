# UI utilities

UI utilityは、利用場所ではなく依存関係で分けます。

- `bd_util.ui`には、Mayaを直接importしない汎用Qt処理を置きます。
- `bd_util.maya.ui`には、Maya main windowやUI lifecycleとの連携処理を置きます。
- 依存は`bd_util.maya.ui`から`bd_util.ui`への一方向とし、逆方向には依存させません。

## 新しいtoolへの導入

新しいMaya toolでは、次の順にUI基盤を組み込みます。

1. Mayaの通常Windowには`MayaWindowController`、workspaceControlを使うUIには
   `MayaDockableWindowController`を選ぶ。
2. controllerをmodule単位で1つ生成し、dockable Windowでは`control_id`と
   `DockRestoreSpec`のmodule・functionをrelease後も維持する。
3. 永続化する場合は`tool_name/windows/main`のような固定`settings_path`を決める。
4. Widget内部状態は全Widgetを`UiStateManager`へ登録した後、通常Windowでは
   `MayaUiStateTracker.for_window()`、dockable Windowでは`for_dockable()`へ接続する。
5. tool固有のMaya callbackはWindowをownerとする`MayaCallbackRegistry`へ登録する。
6. UIのreset操作には`reset_and_show_ui_layout()`を使い、破棄、保存状態削除、再表示の
   順序をtool側で組み直さない。
7. module reload前は`dispose()`で古いWindow、workspaceControl、Maya callbackを完全に
   破棄してからreloadする。

controllerの`retain`は既定で`False`です。タイトルバーのcloseと`controller.close()`は
Windowを完全破棄し、Windowが所有するMaya callbackも解除します。close後の再表示でも同じ
instanceとcallbackを維持する必要があるtoolだけ、`retain=True`を明示します。`dispose()`は
設定にかかわらず完全破棄するため、module reload前とUI配置resetに使用します。

## Qt binding facade

`bd_util.ui.qt`は、Maya同梱Qt bindingのimport先を集約します。toolやパッケージ内部では
`PySide`や`shiboken`を直接importせず、このmoduleを入口として使用します。

```python
from bd_util.ui import qt


class MyWidget(qt.QWidget):
    changed = qt.Signal()

    def __init__(self) -> None:
        super().__init__()

        label = qt.QLabel("My tool")
        layout = qt.QVBoxLayout(self)
        layout.addWidget(label)
```

頻出classは`qt.QLabel`のような短いaliasで公開します。公開aliasへ含まれないAPIも、元module
から利用できます。

```python
painter_path = qt.QtGui.QPainterPath()
```

`QtCore`、`QtGui`、`QtWidgets`に加えて、`wrapInstance()`、`getCppPointer()`、`isValid()`も
同じ入口から利用できます。診断用に現在のbinding情報も公開します。

```python
qt.QT_BINDING
qt.QT_BINDING_VERSION
qt.QT_BINDING_MAJOR_VERSION
```

実行時は新しいbinding候補から順に確認し、root packageが存在しない場合だけ次の候補へ
切り替えます。発見したbinding内部のimport errorやDLLの読み込み失敗はfallbackで隠さず、
そのまま送出します。PySideとshibokenは同じversionの組み合わせで読み込みます。

現在の対応MayaはすべてPySide6です。将来bindingのimport先が変わった場合は`qt.py`の候補へ
PySideとshibokenの組み合わせを追加します。module、頻出alias、利用側のimport方法は変更
しません。公開aliasはversion間の互換性を維持する小さな集合に限定し、利用頻度の低いclassを
網羅的に列挙しません。

## WindowController

`WindowController`は、factoryが生成した表示中のwidgetを1つ管理します。表示中に`show()`を
繰り返しても同じwidgetを返すため、意図しないtool windowの重複を防げます。

既定の`retain=False`では`WA_DeleteOnClose`を有効にし、タイトルバーのcloseと
`controller.close()`でwindowを完全破棄します。次の`show()`ではfactoryから新しいwindowを
生成します。`retain=True`ではclose後もinstanceを保持し、次の`show()`で同じwindowを
再表示します。`dispose()`は`retain`にかかわらずwindowを閉じ、Qt event loopへ削除を
予約します。

`MayaWindowController`は同じlifecycle管理にMaya main windowのparentingを加えます。
factoryはMaya main windowを引数として受け取ります。

```python
from bd_util.maya.ui import MayaWindowController
from bd_util.ui import qt


class MyWindow(qt.QDialog):
    def __init__(self, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("My Maya tool")


controller = MayaWindowController(MyWindow)


def show() -> MyWindow:
    return controller.show()
```

非表示中も同じWindowとcallbackを維持するtoolでは保持を明示します。

```python
controller = MayaWindowController(
    MyWindow,
    retain=True,
)
```

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import simple_window

simple_window.show()
```

`get_main_window()`はbatch MayaとMaya初期化前には`None`を返します。そのため、これらの
環境でmoduleをimportしてもMaya UIを取得しに行きません。

## StoreベースのMVVMによるbool値同期

通常の利用では、`BoolBinding.from_attribute()`でPythonのbool属性とViewModelを
まとめて作成し、Bindingを必要なViewへ渡します。

```python
from dataclasses import dataclass
from bd_util.ui import BoolBinding, BoolCheckBox, qt


@dataclass
class ToolData:
    visible: bool = True


class ToolWidget(qt.QWidget):
    def __init__(self, data: ToolData, parent=None):
        super().__init__(parent)
        self.binding = BoolBinding.from_attribute(data, "visible", parent=self)
        self.check_box = BoolCheckBox(self.binding, "Visible", self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.check_box)
```

5種類のQt Bool Viewは、第1引数に`BoolBinding`（`MayaBoolBinding`・`MayaBoolPlugBinding`を含む）と
`BoolViewModel`の両方を受け付けます。View内部の入力・表示はどちらでも同じViewModelへ
接続され、`view.view_model`から具体的な`BoolViewModel`を取得できます。
既存の`view_model=`キーワードも使用できます。

```python
check_box = BoolCheckBox(binding, "Visible")
another_view = BoolCheckBox(view_model=binding.view_model, text="Visible")
assert check_box.view_model is another_view.view_model
```

Bindingを渡したViewは、そのBindingも参照保持します。Viewを閉じる際にBindingの
`dispose()`を呼んだり、BindingやViewModelのQt parentを変更したりはしません。
共有Bindingの終了は引き続きownerが管理します。Bindingの明示終了やQt親の破棄は
Viewからの参照保持では防がず、残っているViewは従来の終了・破棄通知で無効になります。
終了済みのBindingを新しいViewへ渡すと`RuntimeError`になります。

`binding.set_value(False)`はUIと同じCommandを実行し、正本の実値が変わったか返します。
`binding.value`は最後に同期した確定値です。`data.visible`へ直接代入した場合は
`binding.refresh()`で読み直します。正本をその場で確認する場合は`binding.store.read()`を使います。
`binding.store.instance`には渡したdataの具体型が残り、IDEで属性を補完できます。
独自のPython Storeを使う場合は`BoolBinding(store, parent=owner)`で接続できます。

値の変更は`binding.changed.connect(callback)`で購読できます。callbackには確定後のbool値を
渡し、Qt操作・`set_value()`・`refresh()`のどの経路でも公開値が変わったときだけ通知します。
`MayaBoolBinding`・`MayaBoolPlugBinding`でも同じAPIを使用でき、Mayaから取り込んだ値変更も対象です。

```python
def on_changed(value: bool) -> None:
    print(f"Visible: {value}")


binding.changed.connect(on_changed)
# 購読を解除する場合。
binding.changed.disconnect(on_changed)
```

接続時に現在値を再通知する機能はありません。初期表示には`binding.value`を使います。
同値の設定・refreshや、要求が拒否されて実値が変わらなかった場合も通知しません。
Python属性への直接代入は`refresh()`まで通知されません。Maya同期の成功・失敗は
後述の`maya_view`で確認します。`changed`は既存の`view_model.value.changed`を返すpropertyで、
終了後の取得は`value`と同様に`RuntimeError`になります。

bindingは専用ViewModelをQtの子として所有します。単一Widgetでは`parent=self`を指定し、
複数Windowで共有する場合はWindowから独立したbindingをManagerなどで保持して、各Windowへ
同じBindingまたは`binding.view_model`を渡します。`dispose()`は直ちに入力と同期を停止し、bindingと
ViewModelのQObjectを遅延破棄します。親の破棄でも終了し、`is_disposed`で確認できます。
終了したbindingは再利用しません。Pythonデータや外部から渡されたStore自体は破棄・再parentしません。

Mayaにも同期する場合は`bd_util.maya.ui.MayaBoolBinding`を使います。

```python
from bd_util.maya.ui import MayaBoolBinding, resolve_bool_plug

self.binding = MayaBoolBinding.from_attribute(
    data, "visible",
    maya_plug=resolve_bool_plug("myTransform", "visibility"),
    parent=self,
)
# 型付きNodeOperatorがあればmaya_plug=node.visibilityと直接渡せます。
```

`MayaBoolBinding`もPython側を正本とし、作成時にはその値をMayaへ反映します。
`maya_plug=None`ならPythonのみで動作します。Maya plug自体を正本にする場合は、
次の`MayaBoolPlugBinding`を使用します。
`resolve_bool_plug(node_name, attribute_name)`は既存nodeの最上位scalar boolを取得する入口です。
標準・追加attributeの長い名前と短い名前を扱い、配列、compound、子attribute、属性パスは拒否します。
nodeやattributeの作成は行いません。

Maya同期の状態は`binding.maya_view.is_synchronized`、直近の失敗は`last_sync_error`／
`sync_failed`、明示再試行は`sync_from_view_model()`から扱います（Maya指定がある場合）。
lockなどによるMaya側の同期失敗でPython側の編集は停止しません。`dispose()`ではMaya callbackを
即座に解除し、保留中のMaya入力も取り消します。初期同期の失敗時もcallbackを残しません。
Mayaのundo / redoはadapterのMaya書き込みに対して働き、Pythonだけの変更を登録する機能ではありません。

Maya plugを正本にする場合は、StoreとViewModelをまとめて作る`MayaBoolPlugBinding`を使います。

```python
from bd_util.maya.ui import MayaBoolPlugBinding, resolve_bool_plug
from bd_util.ui import BoolCheckBox

self.binding = MayaBoolPlugBinding(
    resolve_bool_plug("myTransform", "visibility"), parent=self
)
self.check_box = BoolCheckBox(self.binding, "Visible", self)
# 型付きNodeOperatorがあればMayaBoolPlugBinding(node.visibility, parent=self)。
```

作成時にはMayaの現在値を読み取り、初期値を書き戻しません。`value`・`changed`・
`set_value()`・`refresh()`・`dispose()`は通常のBindingと同じです。
`binding.store`は具体的な`MayaBoolPlugStore`で、`store.plug_operator`から対象plugを取得できます。
Qt操作とPython入力はMayaのundo対象になり、Maya側の変更・undo / redoもViewへ反映されます。
lockや入力接続があると入力用Viewは無効になり、読み取り専用Viewは現在値を表示します。

このBindingはStoreと専用ViewModelを所有します。単一Widgetでは`parent=self`を指定し、
複数Windowで共有する場合はWindowから独立したownerを使います。親なしで使う場合は
Managerなどが保持して`dispose()`を呼びます。Maya callbackもownerを参照するため、
Python参照の消滅や最後のViewを閉じる操作を、callbackの終了条件として使いません。
`dispose()`はcallbackを即座に解除し、QObjectの削除を予約します。Maya nodeや属性値は残します。
node削除などでStoreが終了した場合は入力を停止します。対象を再作成した場合はBindingも新しく作ります。

| 正本 | 組み立てAPI | 作成時の動作 |
| --- | --- | --- |
| Python属性 | `BoolBinding.from_attribute(data, "visible")` | Python属性を読み取る |
| Python属性＋Mayaへの同期 | `MayaBoolBinding.from_attribute(data, "visible", maya_plug=plug)` | Python属性をMayaへ反映する |
| Maya plug | `MayaBoolPlugBinding(plug)` | Mayaの現在値を読み取る |

最小sample → 複数属性とUI連動 → Maya同期付きの例 → 全View一覧 → 複数Window共有の順に確認できます。

```python
from bd_util._sample.maya.ui.bool_sample import minimal

window = minimal.show()
window.widget.binding.changed.connect(print)
window.widget.binding.set_value(False)
minimal.dispose()
```

複数属性の例は`from bd_util._sample.maya.ui.bool_sample import multi_attribute`、
`multi_attribute.show()`で開きます。詳しい使い方は後述の「複数のbool属性とUI連動のsample」を参照してください。

以下では、これらの組み立てAPIが利用している各部品と低レベルAPIを説明します。

このドキュメントでは、この構成を「StoreベースのMVVM」と呼びます。
Model・ViewModel・Viewを基本とし、値へのアクセスをStore、現在値と変更通知をValue、
変更要求をCommandに分けています。Bindingはこれらの組み立て・操作・終了をまとめます。

各名称の役割、入力と表示の流れ、Bindingを使うコードとの対応は
[このパッケージでのMVVMの役割](mvvm_roles.md)にまとめています。

設計判断の理由、破棄時の注意点、今後の拡張時に確認する項目は
[bool bindingの設計・保守メモ](bool_binding_design.md)にまとめています。
用語と役割の理解には上記ページ、公開APIと実行例にはこのREADME、
実装を読み進める際の補足には設計・保守メモを使ってください。

- Model: dataclassやMaya nodeなど、tool固有のデータと規則を持つ本体
- Store: Model内の1つのbool値を、共通の読み書き契約としてViewModelへ公開するModel層の境界
- Value: 読み取り専用の現在値と変更通知を公開する
- Command: 値の変更要求を受け付け、実行可否を公開する
- ViewModel: Storeの実値を確定し、ValueとCommandをViewへ公開する
- View: bool値を表示・入力するQt Widgetや`MayaBoolPlugView`
- Binding: Storeと専用ViewModelの組み立て、利用者向けの操作、寿命管理をまとめる

```text
Model
  ↕
BoolValueStore
  ↕
BoolViewModel
  ├─ BoolCheckBox
  ├─ BoolComboBox
  ├─ BoolPushButton
  ├─ BoolRadioButtonGroup
  ├─ BoolStatusLabel
  └─ MayaBoolPlugView
```

Storeは広い意味ではModel側に属しますが、tool全体のModelそのものではありません。
たとえばdataclassを正本にする場合、dataclassがModel、`PythonBoolAttributeStore`が
その中の指定された1属性を公開する境界です。Maya plugを正本にする場合は
`MayaBoolPlugStore`を使い、Python Storeを正本にしてMaya plugを同期先とする場合は
`MayaBoolPlugView`を使います。

複数のViewは互いを直接参照しません。同じViewModelを参照することで、Viewが増えても
正本と同期経路を1つに保ちます。

ViewModelの`parent`には、Viewの生成順ではなくbinding全体の寿命を管理するownerを
指定します。1つのFeature Widgetだけで利用する場合は、そのWidgetを生成時からparentに
指定できます。ViewModelの破棄通知は次のevent loopでViewへ反映されるため、QObjectの
子登録順を利用側で調整する必要はありません。

複数Windowで共有する場合は、いずれかのWindowではなく、両方より長く存続するtoolの
ControllerなどをViewModelのownerにします。各WindowのViewは同じViewModelを参照するだけ
なので、一方のWindowを閉じても残ったViewとの同期を継続できます。

```text
Tool Controller
├─ BoolViewModel
├─ Window A ─ Bool View ─┐
└─ Window B ─ Bool View ─┴─→ 共通のBoolViewModel
```

低レベルAPIでは、共通ownerとViewModelをtoolのControllerなどが保持し、各Windowには
Viewだけを配置します。

```python
from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolViewModel,
    PythonBoolAttributeStore,
    qt,
)

binding_owner = qt.QObject()  # 実際のtoolではControllerが保持する。
view_model = BoolViewModel(parent=binding_owner)
view_model.attach_store(PythonBoolAttributeStore(data, "visible"))

first_view = BoolCheckBox(view_model, parent=window_a)
second_view = BoolComboBox(view_model, parent=window_b)
```

Maya plugも共有する場合、`MayaBoolPlugView`はWindowごとに作らず、同じ共通ownerの下へ
1つだけ作成します。すべてのWindowを閉じても同期を維持するか、tool終了時に破棄するかは、
View数ではなくControllerのlifecycleで決めます。

`BoolViewModel`は、読み取り専用の`BoolValue`と、UI／Pythonから共有する
`SetBoolCommand`を管理します。各ViewはViewModelだけを参照し、入力可能なViewはユーザー入力を
Commandへ渡し、すべてのViewが`BoolValue.changed`から表示を更新します。

`BoolValueStore`は、ViewModelがbool値の正本を読み書きするための共通境界です。Storeを
接続しない場合はViewModel内の`BoolValue`が値を保持し、Storeを接続した場合は
Storeの確定値を`BoolValue`からViewへ公開します。

実装は役割ごとに分け、交換可能なViewだけを`view`以下へまとめています。

```text
bd_util/ui/binding/bool/
├─ binding.py
├─ value.py
├─ store.py
├─ command.py
├─ view_model.py
└─ view/
   ├─ _connection.py
   ├─ check_box.py
   ├─ combo_box.py
   ├─ push_button.py
   ├─ radio_button_group.py
   └─ status_label.py
```

利用側は内部配置へ依存せず、従来どおり`bd_util.ui`からimportできます。

```python
from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
)

view_model = BoolViewModel(False)
checkbox = BoolCheckBox(view_model, "Enabled")
combo_box = BoolComboBox(view_model, false_text="Off", true_text="On")
push_button = BoolPushButton(view_model, false_text="Off", true_text="On")
radio_group = BoolRadioButtonGroup(view_model, false_text="Off", true_text="On")
status_label = BoolStatusLabel(
    view_model,
    false_text="Status: Off",
    true_text="Status: On",
)

# Pythonからの入力も入力可能なViewと同じCommandを使用する。
view_model.set_value_command.execute(True)
```

`BoolValue.changed`は値が実際に変わった場合だけ通知します。ViewModelからQt Viewへ値を
適用するときはsignalをblockするため、表示更新からCommandが再実行されません。
`BoolComboBox`の表示文字列とbool値は分離され、各項目のitem dataに`False`／`True`を
保持します。そのため、表示を翻訳した場合や同じ文字列にした場合も値の意味は変わりません。

各Qt Viewの役割は次のとおりです。

| View | 入力 | 表現 |
| --- | --- | --- |
| `BoolCheckBox` | あり | checked状態 |
| `BoolComboBox` | あり | boolのitem dataを持つFalse／True項目 |
| `BoolPushButton` | あり | checkableな押下状態とFalse／True文字列 |
| `BoolRadioButtonGroup` | あり | `false_button`と`true_button`の排他選択 |
| `BoolStatusLabel` | なし | False／True文字列だけを表示 |

入力可能なViewは`SetBoolCommand.can_execute`に有効状態を合わせます。
`BoolStatusLabel`は読み取り専用なので、Storeが書き込み不可でも現在値を表示し続けます。

### Python objectのbool attributeを正本にする

`PythonBoolAttributeStore`は、dataclassを含む任意のPython objectとattribute名を受け取り、
そのbool attributeをViewModelの正本として接続します。リグ固有の型には依存しません。

```python
from dataclasses import dataclass

from bd_util.ui import BoolCheckBox, BoolViewModel, PythonBoolAttributeStore


@dataclass
class ToolData:
    visible_by_default: bool = True


data = ToolData()
store = PythonBoolAttributeStore(data, "visible_by_default")

view_model = BoolViewModel()
view_model.attach_store(store)
checkbox = BoolCheckBox(view_model, "Visible by default")

# UIと同じCommandからdataclass fieldを書き換える。
view_model.set_value_command.execute(False)
assert data.visible_by_default is False
```

構築時にattributeの存在と現在値のbool型を検証します。mutable dataclass、slots付き
dataclass、通常attribute、propertyを扱い、frozen dataclassとsetterを持たないpropertyは
読み取り専用です。任意objectの書き込み可否は完全には事前判定できないため、独自の
`__setattr__()`や状態依存setterが拒否した例外は書き込み時にそのまま通知します。
`__getattr__()`だけで動的に生成されるattributeは対象外です。

plain dataclassは変更通知を持ちません。外部から直接代入した場合は、接続したStoreを指定して
明示的に再読み込みします。常時同期したい変更はCommand経由に統一してください。

```python
data.visible_by_default = True
view_model.refresh_from_store(store)
```

1つの`BoolViewModel`へ接続できるStoreは1つです。Storeの動的な差し替えは
行いません。

### Maya bool plugを正本にする

`MayaBoolPlugStore`はMaya bool plug自体を正本とします。構築しただけではViewModelへ
接続せず、`attach_store()`で明示的に接続します。

```python
from bd_util.maya.ui import MayaBoolPlugStore
from bd_util.ui import BoolViewModel

maya_view_model = BoolViewModel()
maya_store = MayaBoolPlugStore(maya_view_model, node.visibility, owner)
maya_view_model.attach_store(maya_store)
```

UI／Pythonからの要求は`cmds.setAttr()`でMayaへ書き込まれるため、Maya標準のundo / redoへ
入ります。Maya外部からの直接変更、undo / redo、入力接続やアニメーションによる評価変更は、
Maya callbackから実値を読み直してViewModelへ反映します。callbackは既存の
`MayaCallbackRegistry`でownerと同じ寿命に管理されます。

同期対象がlock済み、入力接続済み、または削除済みの場合、Commandと入力可能なQt Viewは
無効になります。読み取り専用Viewは最後に確定した値を表示します。

### Python Storeの値をMaya bool plugへ同期する

`MayaBoolPlugView`は、ViewModelに接続済みのPython Storeを正本とし、Maya bool plugを
入力・表示装置として同期します。生成前にStoreをViewModelへ接続してください。

```python
from bd_util.maya.ui import MayaBoolPlugView

view_model.attach_store(store)
maya_view = MayaBoolPlugView(view_model, node.visibility, owner)
```

Storeの確定値はMaya plugへ反映されます。Attribute EditorやMaya Pythonからの外部入力は、
Maya callback完了後の次のQt event loopでCommandを経由してStoreへ反映されます。

Maya plugがlock済みまたは入力接続済みで、Storeとplugの値が一致しない場合は、
Storeの確定値を変更せず非同期状態にします。`is_synchronized`で同期状態、
`last_sync_error`または`sync_failed` signalで直近の同期失敗を確認できます。
再び書き込み可能になった時は最新のStore値を自動的に再適用します。明示的に再試行する
場合は`sync_from_view_model()`を使用できます。

1つの`BoolViewModel`へ接続できる`MayaBoolPlugView`は1つです。Viewを`dispose()`すると
接続枠が解放され、同じViewModelへ新しいMaya Viewを接続できます。

### Maya plugを正本にするsample

`maya_plug`は、シーン上の既存bool属性をCheckBoxとStatusLabelで表示・編集します。
MayaのScript Editorから次を実行してください。`pCube1`は対象node名へ置き換えます。

```python
from bd_util._sample.maya.ui.bool_sample import maya_plug

window = maya_plug.show("pCube1", "visibility")
window.widget.binding.changed.connect(print)
window.widget.binding.set_value(False)
```

中心の実装は[maya_plug.py](../../python/bd_util/_sample/maya/ui/bool_sample/maya_plug.py)です。
`show()`は対象を解決してから前のサンプルWindowを置き換えます。閉じた後の再表示では、
その時点のMayaの値を読み取ります。対象が見つからない場合は、表示中のWindowを維持して例外を返します。
`maya_plug.dispose()`でWindowとBindingを終了できます。サンプルはnodeを作成・削除しません。

Attribute Editorからの変更、lockの切り替え、undo / redo、Windowの閉じ直しで、
値と編集可否が追従することを確認できます。自作Windowには`MayaPlugBoolWidget(plug, parent=...)`を組み込めます。

### 複数のbool属性とUI連動のsample

`multi_attribute`は、1つのdataclassにある3属性を、それぞれの`BoolBinding`で編集する例です。
MayaのScript Editorから表示でき、Qtのプレビューで表示設定の効果を確認できます。

```python
from bd_util._sample.maya.ui.bool_sample import multi_attribute

window = multi_attribute.show()
widget = window.widget
```

| 操作 | データ属性 | 変更時の動作 |
| --- | --- | --- |
| Visible | `visible` | プレビュー全体を表示・非表示にする |
| Show labels | `show_labels` | プレビュー内のラベルを表示・非表示にする |
| Allow editing | `allow_editing` | Display options欄の編集を許可・禁止する |

`Visible`をオフにしても`show_labels`の値は保持されます。`Allow editing`をオフにしても
表示設定の値は保持され、Pythonからの変更は引き続き表示へ反映されます。
編集禁止はこの画面の操作可否であり、Storeへの書き込み禁止を設定するものではありません。

```python
widget.editing_binding.set_value(False)
widget.labels_binding.set_value(False)  # 編集禁止中でもPython入力は反映する。
widget.editing_binding.set_value(True)

# データへ直接代入した場合は、3つのBindingを明示的に読み直す。
widget.data.visible = False
widget.data.show_labels = True
widget.refresh_from_data()

multi_attribute.dispose()
```

中心の実装は[multi_attribute/widget.py](../../python/bd_util/_sample/maya/ui/bool_sample/multi_attribute/widget.py)です。
各Bool ViewへBindingを直接渡し、`changed`をプレビューや設定欄へ接続しています。

```python
self.editing_binding.changed.connect(self.options_group.setEnabled)
self.options_group.setEnabled(self.editing_binding.value)
```

`changed`は接続時に現在値を通知しないため、初期表示を別途適用します。
編集可否は親の設定欄へ適用し、Bool View自身が持つCommandの実行可否と両立させます。
表示と編集可否の連動規則はこのFeature Widgetへ置き、bool共通基盤へ追加していません。

自作Windowへ組み込む場合は、`DisplayOptionsWidget(data, parent=...)`へ
`DisplayOptionsData`を渡します。3つのBindingはWidgetをownerとし、Widgetと一緒に終了します。
サンプルのWindowを閉じた後に`show()`すると、新しいデータと初期設定で再表示します。

### bool Views sample

bool系sampleは`bd_util/_sample/maya/ui/bool_sample/`以下へまとめています。
最小版と共通data・任意引数の検証を直下へ置き、複数属性版・全View一覧・共有Window版をそれぞれのpackageで
管理します。plugの解決は基盤の`resolve_bool_plug()`へ委譲します。

```text
bd_util/_sample/maya/ui/bool_sample/
├─ __init__.py
├─ bool_plug.py              # sampleの任意Maya指定の検証
├─ data.py                   # 共通のVisibilityData
├─ minimal.py                # Python属性＋CheckBoxの最小版
├─ maya_plug.py              # 既存Maya bool plugを正本にする版
├─ multi_attribute/          # 複数bool属性とUI連動
│  ├─ __init__.py
│  ├─ data.py
│  ├─ widget.py
│  └─ window.py
├─ bool_views/               # 単一Window版
│  ├─ __init__.py
│  ├─ widget.py
│  └─ window.py
└─ shared_bool_views/        # 共有Window版
   ├─ __init__.py
   ├─ manager.py
   ├─ widget.py
   └─ window.py
```

MayaのScript Editorで次を実行すると、任意のPython object内のbool attributeを正本とし、
作成したcubeの`visibility`を任意のMaya Viewとして同期する全bool Viewを表示できます。

```python
from maya import cmds
from bd_util._sample.maya.ui.bool_sample import bool_views

data = bool_views.VisibilityData()
node = cmds.polyCube(name="bdVisibilityBindingSample")[0]
window = bool_views.show(
    data,
    "visible_by_default",
    maya_node_name=node,
    maya_attribute_name="visibility",
)
```

`data`にはdataclassに限らず、書き込み可能なbool attributeを持つPython objectを渡せます。
第2引数には、そのobject内で正本として扱うattribute名を指定します。
`maya_node_name`と`maya_attribute_name`は組で指定する任意引数です。両方を省略すると、
Maya nodeとは同期せず、PythonデータとQt Viewだけで動作します。

```python
window = bool_views.show(data, "visible_by_default")
```

内部では`MayaBoolBinding.from_attribute()`でPython属性と任意のMaya Viewを接続します。
Maya側にはtransformの`visibility`に限らず、最上位のscalar bool attributeを指定できます。

`BoolViewsWidget`には`BoolCheckBox`、`BoolComboBox`、`BoolPushButton`、
`BoolRadioButtonGroup`、`BoolStatusLabel`を配置します。Maya Viewを指定した場合、入力可能な
4つのQt View、Attribute Editor、次のPython入力、Mayaのundo / redoのいずれから変更しても、
Python object、全Qt View、Maya plugが同じ値へ同期します。Mayaからの外部入力は、スクリプトの
実行がQtに制御を返した次のevent loopでPython Storeへ反映されます。

Windowの`Print Data Value`ボタンを押すと、その時点の内部データをMaya Script Editorへ
`VisibilityData.visible_by_default = True`の形式で出力します。

```python
bool_views.set_value(False)
cmds.setAttr(f"{node}.visibility", True)
cmds.undo()
cmds.redo()
```

Python objectを別処理から直接変更した場合は、明示的に正本から再読込できます。

```python
data.visible_by_default = False
bool_views.refresh_from_data()
```

`BoolViewsWindow`はWidgetと生成時のMaya指定を保持し、`BoolViewsWidget`はbindingとQt Viewを
所有します。bindingがViewModelと任意のMaya Viewを所有するため、Widgetの破棄時には
その一式も終了します。`BoolViewsWindowManager`はWindowの再利用判定、生成引数、lifecycleを管理し、module-levelの
`show()`、`set_value()`、`refresh_from_data()`、`dispose()`は既定Managerへ処理を委譲します。

この`BoolViewsWidget`は1つのWindow内でbinding一式を確認する自己完結sampleです。複数Windowで
共有する場合はtoolのControllerがWindowから独立した`MayaBoolBinding`を1つ保持します。
後述の`shared_bool_views`が、その実行可能なsampleです。
複数の値型でも同じ共有構成が必要になった段階で、これらを束ねる`BindingSession`の共通化を
検討します。

ManagerはWindow生成中だけ引数を保持し、生成後には破棄します。そのため、module-levelの
可変な引数や関数内の`global`宣言を必要とせず、最後に渡したdataへの不要な参照も残しません。

既存Windowやlayoutへ取り付ける例です。Window側はこのWidgetを生成して配置するだけで、
同じbinding一式を利用できます。

```python
widget = bool_views.BoolViewsWidget(
    data,
    "visible_by_default",
    maya_node_name=node,
    maya_attribute_name="visibility",
    parent=parent,
)
layout.addWidget(widget)
```

複数の独立したWindow管理が必要な場合は、Managerを個別に生成できます。

```python
manager = bool_views.BoolViewsWindowManager()
window = manager.show(data, "visible_by_default")
```

sampleを完全に破棄する場合です。

```python
bool_views.dispose()
```

### 1つのViewModelを複数Windowで共有するsample

`shared_bool_views`は、1つの`BoolViewModel`をWindow A / Bで共有するsampleです。
両方に全5種類のBool Viewと`Print Data Value`ボタンを配置し、片方を閉じた後の同期と
再表示まで確認できます。MayaのScript EditorのPythonタブで次を実行してください。

```python
from bd_util._sample.maya.ui.bool_sample import shared_bool_views

data = shared_bool_views.VisibilityData()
manager = shared_bool_views.SharedBoolViewsManager(
    data,
    "visible_by_default",
)
window_a, window_b = manager.show()
```

引数は既存sampleと同じく、任意のPython objectと正本にするbool attribute名です。
`VisibilityData`は`bool_sample/data.py`に置いた共通dataclassです。Managerを操作できるよう、
`manager`変数を保持してください。

責務は次のように分けています。

| class | 責務 |
| --- | --- |
| `SharedBoolViewsManager` | 1つの`MayaBoolBinding`と2つのWindow Controllerを保持する |
| `SharedBoolViewsWidget` | 外部ViewModelを受け取り、5種類のViewを接続する。正本の出力はsignalでManagerへ要求する |
| `SharedBoolViewsWindow` | Widgetと、そのWindowだけを閉じるボタンを配置する |

共通ownerとなるbindingはWindowの子にせず、ViewModelとMaya Viewの寿命を管理します。
Window自体のQt parentは、既存の`MayaWindowController`を通してMaya main windowになります。
各Widgetは渡されたViewModelのparentを変更しません。

node名からbool plugを解決する処理は、公開APIの`bd_util.maya.ui.resolve_bool_plug()`へ
委譲します。sampleの`bool_plug.py`は任意引数を組として検証する補助だけを担います。

Window A / BのいずれかのViewを操作すると、相手WindowとPython正本へ反映されます。
次の式でも、同じViewModel instanceであることを確認できます。

```python
print(
    window_a.bool_views_widget.view_model
    is window_b.bool_views_widget.view_model
    is manager.view_model
)  # True

manager.set_value(False)  # 両Windowと共通のCommandから入力する。
manager.print_data_value()  # 各WindowのPrint Data Valueボタンと同じ処理。
```

×ボタンまたは`Close Window A / B`で片方を閉じても、もう一方の操作は継続できます。
閉じたWindowは、その後のScript Editor操作で再表示できます。

```python
window_a = manager.show_a()  # Aだけ再表示する。
window_b = manager.show_b()  # Bだけ再表示する。
window_a, window_b = manager.show()  # 両方を表示する。
```

生存中のWindowは再利用し、破棄済みのWindowだけを再生成します。再生成したViewは同じ
ViewModelの現在値を初期表示します。両方のWindowを閉じた場合も、共有bindingは継続します。

Python objectのattributeをCommandを使わず直接変更した場合は、明示的に再読込します。

```python
data.visible_by_default = True
manager.refresh_from_data()
```

Maya nodeも同期する場合は、現在のManagerを終了してから任意のnode名・attribute名を
指定したManagerを作成します。次の例は確認用cubeを追加します。

```python
from maya import cmds

manager.dispose()
node = cmds.polyCube(name="bdSharedBoolViewsSample")[0]
manager = shared_bool_views.SharedBoolViewsManager(
    data,
    "visible_by_default",
    maya_node_name=node,
    maya_attribute_name="visibility",
)
window_a, window_b = manager.show()
```

生成時にはPython正本の現在値がMaya plugへ反映されます。`MayaBoolPlugView`はWindowごとに
作らず、共通ownerの下に1つだけ作成します。Attribute Editor、Maya Python、undo / redo
からの変更は、Qtへ制御が戻った後のevent loopで両Windowと正本へ反映されます。
両Windowを閉じた状態でも、Maya nodeとPython正本の同期は継続します。

```python
cmds.setAttr(f"{node}.visibility", False)
```

確認終了時は、Windowを閉じる操作とは別に、次を実行してください。

```python
manager.dispose()
```

`dispose()`はMaya callbackを即座に解除し、両Windowと共有QObjectの削除をQtへ予約します。
保留中のMaya入力も以後は反映しません。渡したPythonデータの値やMaya nodeは削除・復元しません。
終了したManagerは再利用せず、新しいManagerを生成してください。構成を変更する場合も、
古いManagerを`dispose()`してから作成します。

## 浮動小数点値のMVVMとQDoubleSpinBox

`MayaFloatPlugBinding`は既存Maya属性を正本として読み取り、`FloatSpinBox`で編集します。
単位なしのfloat/double、距離、角度に対応し、表示・入力は現在のMaya表示単位へ追従します。
Pythonからの`binding.value`／`set_value()`は既存PlugOperatorと同じcm／degree固定です。

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

# 既存transformの名前を指定する。nodeや属性は作成しない。
window = maya_plug.show("pCube1")
```

サンプルは`translateX`、`rotateX`、`scaleX`にそれぞれ独立したBindingを作ります。
`maya_plug.dispose()`またはWindowのcloseでUIとcallbackを終了します。
API、単位、丸め、対応範囲は[浮動小数点binding](float_binding.md)を参照してください。
サンプルの小数桁数はWindow生成時にChannel BoxのChange Precision設定から取得します。
桁数設定の変更は次回表示時に反映し、距離・角度の単位変更は表示中も追従します。

### 数値と単位の表示・コピー

`FloatLabel(binding, decimals=6)`は、SpinBoxと同じBindingを共有できる読み取り専用の数値ラベルです。
現在の表示単位と指定桁数で表示し、文字列の選択・コピーに対応します。表示の丸めは正本へ戻さず、
lock・接続・Pythonの読み取り専用属性でも表示を継続します。Binding終了時には最終表示を残して無効化します。
単一値サンプルの`maya_plug`・`minimal`・`maya_view`へ、SpinBoxと対になる共有ラベルを追加しています。
API、精度、寿命、確認手順は[FloatLabel](float_label.md)を参照してください。

### スライダーによる連続編集

`FloatSlider(binding, minimum=-100, maximum=100)`は、公開単位の有限範囲を操作するViewです。
ドラッグ中も正本・SpinBox・Labelへ即時反映し、Mayaへの一連の書き込みをUndo 1回にまとめます。
範囲外の正本値や表示精度は維持し、つまみの表示位置だけを範囲内へ制限します。
既存の`maya_plug`・`minimal`・`maya_view`サンプルで共有表示を確認できます。
操作範囲、入力単位、Undoと中断の仕様は[FloatSlider](float_slider.md)を参照してください。

### SliderとSpinBoxの複合View

`FloatSliderSpinBox(binding, minimum=-100, maximum=100, decimals=3)`で、横並びの編集Viewを
1つのWidgetとして配置できます。内部の`editor.slider`と`editor.spin_box`にも型補完つきでアクセスできます。
各Viewが同じ正本を共有し、スライダーの操作範囲外の数値もSpinBoxから入力できます。
既存の単一値サンプルは、この複合Viewと共有ラベルを並べる構成です。
API、範囲と入力単位、寿命の詳細は[FloatSliderSpinBox](float_slider_spin_box.md)を参照してください。

## Python属性を正本にする浮動小数点binding

`FloatBinding.from_attribute()`はPython objectやdataclassの数値属性を正本とし、
既存の`FloatSpinBox`で編集します。生成される`PythonFloatAttributeStore`は正本の具体型を
維持し、setterによる補正・拒否、有限値の検証、読み取り専用属性に対応します。
表示単位と範囲は`FloatPresentation`で明示でき、直接代入後は`binding.refresh()`で同期します。

```python
from bd_util._sample.maya.ui.float_sample import minimal

window = minimal.show()
```

サンプルは1つのPython属性を3桁と6桁のSpinBoxと数値ラベルで共有し、直接代入とrefreshも試せます。
API、単位、範囲、寿命は[Python属性の浮動小数点binding](python_float_binding.md)を参照してください。

## Python属性とMaya Viewの浮動小数点同期

`MayaFloatBinding.from_attribute()`はPython属性を正本とし、Qt WidgetとMaya属性を同期します。
初期値はPythonからMayaへ適用し、Maya側の編集はCommand経由でPythonへ渡します。
距離はcm、角度はdegreeでPythonに保持し、Qt表示はMayaの現在単位に追従します。
Maya側のlock・接続などによる同期失敗は、Python Storeの編集可否とは別に公開します。

```python
from bd_util._sample.maya.ui.float_sample import maya_view

window = maya_view.show("pCube1")
```

既存transformのtranslateX・rotateX・scaleXへサンプルのPython初期値を適用します。
API、精度、Undo/Redo、同期失敗の扱いは[Python正本とMaya View](python_float_maya_binding.md)を
参照してください。Pythonの3成分tupleとMaya compound全体は`MayaFloat3Binding`で同期できます。

## 3成分の浮動小数点値とXYZ編集

`MayaFloat3PlugBinding`と`Float3SpinBox`は、`translate`・`rotate`・`scale`を
それぞれXYZの行として編集します。各軸は既存のscalar基盤を使い、単位・桁数・精度保持の
規則を引き継ぎます。Yだけをlockした場合でもX・Zは編集できます。

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
window.widget.translate_binding.set_value((100.0, 200.0, 300.0))
```

各軸の入力はその軸だけを書き換え、他の成分の実値を保持します。
`set_value()`は全成分を事前検証し、1回のMaya Undoで戻せる一括設定を行います。
API、対応属性、Storeの構成は[3成分binding](float3_binding.md)を参照してください。

Python objectの3成分tupleは`Float3Binding.from_attribute(data, "offset", parent=...)`で
接続できます。各軸は他成分の最新値を保持してsetterへ渡し、setterによる全軸の補正も
再同期します。`FloatPresentation`は全軸共通またはXYZごとに指定できます。

```python
from bd_util._sample.maya.ui.float3_sample import minimal

window = minimal.show()
```

サンプルは3桁と6桁のXYZ Viewを共有し、一括編集、Python属性への直接代入、refreshを試せます。
対応する値の型と失敗時の扱いは[Python属性の3成分binding](python_float3_binding.md)を参照してください。

### Python正本とMayaの3成分同期

`MayaFloat3Binding.from_attribute()`はPython tupleを正本として、QtのXYZ ViewとMayaの
translate・rotate・scaleを同期します。初期値はPythonからMayaへ適用し、親属性の一括変更は
setter 1回、Mayaへの一括反映も1回のUndoで扱います。単位と表示精度は単一値版と共通です。
一部の軸がlock・入力接続で書けない場合もPython編集を続け、一括同期は部分反映せず保留します。

```python
from bd_util._sample.maya.ui.float3_sample import maya_view

window = maya_view.show("pCube1")
```

API、単位、Undo/Redo、寿命、手動確認手順は[Python正本とMaya Viewの3成分同期](python_float3_maya_binding.md)を
参照してください。

## Maya callbackのlifecycle管理

`MayaCallbackRegistry`は、`MEventMessage`、`MSceneMessage`、`MNodeMessage`などが返す
Maya callback IDを1つのQt ownerへ関連付けます。callback種別ごとの登録方法はMaya APIへ
委ね、解除とlifecycleだけを共通化します。

```python
from maya.api import OpenMaya as om

from bd_util.maya.ui import MayaCallbackRegistry
from bd_util.ui import qt


class MyWindow(qt.QDialog):
    def __init__(self, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)

        # Window instanceが所有するMaya callbackをまとめて管理する。
        self.maya_callbacks = MayaCallbackRegistry(self)
        callback_id = om.MEventMessage.addEventCallback(
            "SelectionChanged",
            self._on_selection_changed,
        )
        self.maya_callbacks.register(int(callback_id))

    def _on_selection_changed(self, *_args: object) -> None:
        print("selection changed")
```

登録済みIDは`callback_ids`で確認でき、`remove()`では1件、`dispose()`では全件を解除します。
全件解除は登録と逆順に行い、二重disposeとMaya側で解除済みのIDを許容します。破棄済みregistry
への追加と、同じIDの重複登録はerrorにします。

Qt ownerの`destroyed`と`MSceneMessage.kMayaExiting`でも自動解除します。さらに
`MayaWindowController.dispose()`と`MayaDockableWindowController.dispose()`は、Qtの遅延破棄や
workspaceControl削除を待たず、owner直下のregistryを即座に解除します。既定の
`retain=False`では`close()`も完全破棄を通るためcallbackを解除します。`retain=True`の
closeだけはWindow instanceとcallbackを維持し、同じinstanceの再表示で再登録されません。

Maya終了前にtool固有処理が必要な場合は`on_maya_exiting`を指定できます。処理が例外を送出しても
registryのcallback解除は必ず実行されます。

```python
self.maya_callbacks = MayaCallbackRegistry(
    self,
    on_maya_exiting=self.save_cached_state,
)
```

`MayaUiStateTracker`のMaya終了callbackもこのregistryで管理します。tool側でtracker用callbackを
個別に解除する必要はありません。

## Window stateの保存

`settings_path`を指定すると、windowの位置、サイズ、最大化状態をMayaのuser
preferencesへ保存します。`QMainWindow`の場合は、dockとtoolbarのstateもgeometryと
分離して保存します。

```python
controller = MayaWindowController(
    MyWindow,
    settings_path="tool_name/widget_a/func_a/my_window",
)
```

先頭segmentはtool名、それ以降はtoolのINIファイル内のgroupとして扱います。

```text
<Maya userPrefDir>/
└─ bakedanuki/
   └─ tools/
      └─ tool_name/
         └─ ui.ini
```

`ui.ini`内では次のgroupとkeyに分かれます。

```text
widget_a/func_a/my_window/geometry
widget_a/func_a/my_window/window_state
widget_a/func_a/my_window/schema_version
```

window stateはclose eventで保存されます。タイトルバーのclose、`controller.close()`、
`controller.dispose()`のいずれも同じ保存処理を通ります。`settings_path`を省略した場合は
永続化を行いません。

保存済みgeometryの復元後は、Windowのタイトル領域が現在接続されているいずれかのscreenで
操作可能か確認します。モニター切断、解像度変更、配置変更によってタイトル領域が画面外へ
移動した場合は、現在のWindowと最も広く重なるscreen、Maya親Windowのscreen、Windowへ割り当て
済みのscreen、primary screenの順に補正先を選びます。元のサイズを可能な限り維持し、screenの
available geometryを超える場合は収まる大きさへ変更して中央へ配置します。

既に操作可能なWindowは変更しません。表示中のWindowを明示的に確認する場合は、汎用Qt APIの
`ensure_window_on_screen()`を使用できます。戻り値はgeometryを補正した場合だけ`True`です。

```python
from bd_util.ui import ensure_window_on_screen

ensure_window_on_screen(window)
```

`settings_path`はplatformにかかわらず`/`で区切ります。絶対path、`.`、`..`、空segment、
Windows予約名や使用できない文字は拒否されます。

## Widget内部状態の保存

`UiStateManager`は、明示登録したWidgetの内部状態を同じtool単位の`ui.ini`へ保存します。
第一弾では次のWidgetに対応しています。

- `QSplitter`: 分割位置
- `QTabWidget`: 現在選択されているタブ

`QHeaderView`の列幅・表示順は対応対象に含めません。MayaのworkspaceControlでは終了時の
layout変更とWidget破棄の順序により、利用中のheader stateを安定して取得・復元できなかった
ためです。必要なtoolでは`UiStateManager`へ含めず、tool側の要件に合わせて個別に管理します。
`bd_util.ui.qt.QHeaderView`は通常のUI構築用Qt facadeとして引き続き利用できます。

Mayaでは`create_ui_state_manager()`から生成し、`MayaUiStateTracker`でMaya終了前の保存を
管理します。

```python
from bd_util.maya.ui import MayaUiStateTracker, create_ui_state_manager


self.ui_state = create_ui_state_manager(
    "rig_editor/windows/main",
)
self.ui_state.register_splitter(
    "main_splitter",
    self.main_splitter,
)
self.ui_state.register_tab_widget(
    "main_tabs",
    self.main_tabs,
)

# 通常Windowでは全Widgetの登録後にlifecycle連携済みtrackerを生成する。
self.ui_state_tracker = MayaUiStateTracker.for_window(
    self.ui_state,
    self,
)
```

dockable Windowでは`for_dockable()`を使用します。

```python
self.ui_state_tracker = MayaUiStateTracker.for_dockable(
    self.ui_state,
    self,
)
```

Maya終了時はQtの`closeEvent()`や`destroyed`だけでは保存処理の実行順を保証できません。
`MayaUiStateTracker`は`MSceneMessage.kMayaExiting`を受け、Widgetから終了時に再取得せず、
変更signalで退避済みの状態を保存します。ownerの破棄時にはMaya callbackを解除します。

`MayaUiStateTracker.for_dockable()`は`MayaDockableWindow`のlifecycle signalへ次の処理を
接続します。

- `dock_attached`: workspaceControl接続後、次のQt event loopで一度だけ復元
- `dock_closed`: workspaceControlのclose時に退避済み状態を保存
- `dock_about_to_dispose`: 完全破棄前に保存してMaya callbackを解除
- `destroyed`: 外部から破棄された場合も退避済み状態を保存してcallbackを解除

controllerが接続完了と完全破棄前を通知するため、tool側の`show()`、`restore()`、`dispose()`で
trackerを個別に呼び出す必要はありません。

`MayaUiStateTracker.for_window()`は通常Windowへevent filterを設定し、次の処理を接続します。

- 初回`Show`: 次のQt event loopで一度だけ復元
- `Close`: 退避済み状態を保存
- `destroyed`: `Close`を通らない外部破棄では退避済み状態を保存し、callbackを解除
- Maya終了: 退避済み状態を保存し、callbackを解除

`MayaWindowController.dispose()`は`Close`後にQt event loopへ破棄を予約します。close時点で保存済みの
Windowは、遅れて`destroyed`が届いても二重保存しません。これによりUI配置リセットでINIを削除した
後に、古いWindowの状態が復活することを防ぎます。

```python
def show():
    return controller.show()


def restore():
    return controller.restore()
```

`MayaUiStateTracker.restore()`は次のQt event loopで一度だけ復元します。通常Windowの表示または
workspaceControl接続後のlayout計算を待って内部状態を適用し、同じWindowの再表示では保存済み状態を
再適用しません。`for_window()`と`for_dockable()`を使用する場合、tool側から`restore()`や`save()`を
個別に呼び出す必要はありません。

`clear()`はWidget内部状態だけを削除し、同じgroupに保存されたgeometryや他のtool設定は変更しません。

Splitter移動とTab選択変更はsignalでmemoryへ退避し、通常closeまたはMaya終了時にまとめて
永続化します。

`save()`は生存中のWidgetから現在状態を取得してQSettingsへ書き込みます。
`MayaUiStateTracker.save()`はMaya終了処理中のlayout状態で上書きせず、変更時に退避した状態を
`save_cached()`で永続化します。C++ objectが破棄済みの場合や、有効なまま初期状態へ戻った
場合でも、利用中の最新状態を維持できます。

state keyは`main_splitter`のような固定識別子を指定します。異なるWidgetへの重複登録や、
`/`を含むkeyは拒否されます。保存時のWidget種類と登録時の種類が異なる場合や、Qtが復元
できない値は適用せず、そのWidgetの状態だけを削除します。

`save()`はそのmanagerへ登録されているkeyだけを更新します。同じsettings pathを複数の
UI componentで共有しても、別managerが保存したWidget状態は維持されます。`clear()`は
settings path配下の`ui_state`全体を削除するため、toolの「UI配置をリセット」に利用できます。

上記の例はINI内で次のように分離されます。

```text
windows/main/geometry
windows/main/ui_state/schema_version
windows/main/ui_state/widgets/main_splitter/type
windows/main/ui_state/widgets/main_splitter/state
windows/main/ui_state/widgets/main_tabs/type
windows/main/ui_state/widgets/main_tabs/state
```

### 通常Windowでのlifecycle統合確認

同梱sampleをMayaのScript Editorから表示できます。

```python
from bd_util._sample.maya.ui import simple_window

simple_window.show()
```

次の操作で、通常Windowの自動保存・復元とリセットを確認します。

1. Splitter幅と選択タブを変更する。
2. `Close`後に`simple_window.show()`を実行し、新しいWindowへ状態が復元されることを確認する。
3. 表示中に`simple_window.show()`を再実行し、同じWindowが前面へ移動することを確認する。
4. `Reset layout`でWindowが再生成され、初期geometry、Splitter幅、選択タブへ戻ることを確認する。
5. Mayaを終了・再起動して`simple_window.show()`を実行し、Splitter幅と選択タブが復元されることを確認する。

## UI配置の統合リセット

`reset_ui_layout()`は、controllerの完全破棄と保存済みUI配置の削除を正しい順序でまとめて
実行します。通常Windowとdockable Windowの両方に利用でき、reset後はWindowを閉じた状態に
します。

```python
from bd_util.maya.ui import reset_and_show_ui_layout, reset_ui_layout


def reset_layout() -> bool:
    return reset_ui_layout(
        controller,
        "tool_name/windows/main",
    )


def reset_and_show_layout():
    return reset_and_show_ui_layout(
        controller,
        "tool_name/windows/main",
    )
```

通常Windowでは`dispose()`後にgeometry、QMainWindow state、Widget内部状態を削除します。
dockable Windowでは`reset_workspace_state()`によってworkspaceControl本体とMayaの保存配置も
削除してから、同じINI stateを削除します。dispose時のclose eventやlifecycle trackerによる
最終保存より後にINIをclearするため、resetした値が直後に復活しません。

既定ではWindow stateとWidget内部状態の両方を削除します。片方を維持する場合は
`clear_window_state=False`または`clear_widget_state=False`を指定します。同じsettings pathに
保存されたtool固有設定や、別のsettings pathは削除しません。通常WindowのWindow stateを
削除する場合、settings pathは`MayaWindowController`へ指定した保存先と一致させます。

ユーザー操作からresetする場合は`reset_and_show_ui_layout()`を使うと、保存配置の削除後に
同じcontrollerから初期状態のWindowを再生成して返します。通常Windowとdockable Windowの
どちらでも具体的なWindow型が戻り値へ維持されます。QSettingsのclearが失敗した場合は、
古い配置を復元しないよう再表示せず`RuntimeError`を送出します。

## Mayaへドッキング可能なWindow

`MayaDockableWindow`と`MayaDockableWindowController`は、Mayaの`workspaceControl`を
利用して1つのdockable Widgetを管理します。通常windowとはMaya側のlifecycleが異なるため、
`MayaWindowController`とは別のcontrollerとして提供します。

```python
from bd_util.maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
)
from bd_util.ui import qt


class MyWindow(MayaDockableWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Maya tool")

        layout = qt.QVBoxLayout(self)
        layout.addWidget(qt.QLabel("Dockable content"))


controller = MayaDockableWindowController(
    MyWindow,
    control_id="myMayaTool",
    restore=DockRestoreSpec(
        module="my_tool.ui.main_window",
        function="restore",
    ),
    dock_options=DockOptions(
        area=DockArea.RIGHT,
        floating=False,
        initial_width=420,
        retain=False,
    ),
)


def show() -> MyWindow:
    return controller.show()


def restore() -> MyWindow:
    return controller.restore()
```

`control_id`はQtの`objectName`として使われ、上の例ではMaya側に
`myMayaToolWorkspaceControl`が作成されます。Mayaの保存状態と対応付けるため、release後は
同じIDを維持してください。1つのIDにつき1つのWidgetを管理します。

`DockRestoreSpec`には、Maya再起動時にもimportできるmoduleと復元関数を指定します。
controllerが生成した`uiScript`からその関数が呼ばれ、`restore()`がMayaの復元中のlayoutへ
Widgetを接続します。lambdaやlocal関数は復元先に指定できません。

`DockOptions.retain`の既定値は`False`です。タイトルバーのcloseと`controller.close()`で
workspaceControlとWidgetを削除し、Windowが所有するMaya callbackも解除します。次の
`show()`では保存済みworkspace配置へ新しいWidgetを接続します。`retain=True`ではMaya標準の
closeでworkspaceControlを非表示にし、同じWidgetとcallbackを維持します。

`controller.dispose()`は`retain`にかかわらずworkspaceControlとWidgetを完全に削除するため、
開発中のmodule reload前にも利用できます。`controller.reset_workspace_state()`は完全破棄に
加えてMayaが保存した配置も削除し、次回表示で`DockOptions`の初期値を適用します。

floating workspaceControlは`show()`と`restore()`のlayout接続後、次のQt event loopで外枠の
タイトル領域を確認します。現在接続中のscreenから外れている場合だけ、Mayaが位置管理に使う
floating最上位Widgetへ`ensure_window_on_screen()`を適用します。Maya 2025では内容Widgetの
直接の親が同名の`QWidget`になるため、その親階層から最上位Windowを取得します。docked状態、
Maya main window、内側のWidget geometryは変更しないため、Mayaのworkspace layout管理とは
競合しません。

表示後に明示的な確認が必要な場合はcontrollerから実行できます。

```python
controller.ensure_on_screen()
```

Qtが接続中と認識しているscreenは補正対象外です。モニターの電源OFF後もOS上で接続中の場合は
そのscreenの保存配置を維持します。

`DockOptions.allowed_area`は移動を許可する領域を制限し、既定値の`DockArea.ALL`では全領域を
許可します。`MayaDockableWindow.dock_closed`と`floating_changed`を使うと、Maya側で閉じた
ときとドッキング状態が変わったときをtool固有処理へ通知できます。

同梱sampleはMayaのScript Editorから開けます。

```python
from bd_util._sample.maya.ui import dockable_window

dockable_window.show()
```

sampleは`retain=False`を使用します。close後の`show()`で新しいWidgetが生成され、Splitter幅と
選択タブが復元されることを確認できます。

### 実Mayaでのlifecycle統合確認

開発用ハーネスをMayaのScript Editorから表示できます。

```python
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.show()
```

このハーネスは既定の破棄policyを検証するため`retain=False`を指定しています。

次の操作で、workspaceControlとWidget内部状態を実Maya上で確認します。

1. Splitter幅と選択タブを変更する。
2. `Close`後の`dock_lifecycle.diagnose()`でWindowとcallbackが残っていないことを確認する。
3. `dock_lifecycle.show()`を実行し、新しいWidgetへ状態が復元されることを確認する。
4. floatingとdockを切り替え、event logへ変更が記録されることを確認する。
5. Mayaを終了・再起動し、workspaceControl、Splitter幅、選択タブが復元されることを確認する。
6. `Reset`でWindowが再生成され、初期配置と初期Widget状態へ戻ることを確認する。

同じハーネスには`SelectionChanged` callbackも登録されています。次の操作でcallbackの寿命を
確認できます。

1. Maya上で選択を変更し、event logへ`selection_changed`が1行追加されることを確認する。
2. `Close`後に`dock_lifecycle.diagnose()`を実行し、`callback_ids`が空であることを確認する。
3. `dock_lifecycle.show()`で新しいWindowを生成し、選択変更ごとに1行だけ追加されることを確認する。
4. `dock_lifecycle.dispose()`後にmoduleをreloadし、古いcallbackによる二重記録がないことを確認する。

管理中の利用側callback IDは診断結果から確認できます。

```python
from pprint import pprint

pprint(dock_lifecycle.diagnose()["callback_ids"])
```

floating workspaceControlの画面外救済は、Script Editorから次の順に確認できます。

```python
from maya import cmds
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.show()
cmds.workspaceControl(
    "bdUtilDockLifecycleHarnessWorkspaceControl",
    edit=True,
    floating=True,
)
```

floating表示へ切り替わった後、test用の画面外座標へ移動します。

```python
dock_lifecycle.move_offscreen_for_test()
```

明示APIまたは通常の`show()`で現在のscreenへ戻ることを確認します。

```python
dock_lifecycle.ensure_on_screen()

# 再度画面外へ移動した場合は、show後の遅延処理でも自動補正される。
dock_lifecycle.move_offscreen_for_test()
dock_lifecycle.show()
```

同名の直下workspace widget、実際に補正するfloating外枠、Qtが認識しているscreenは次で
確認できます。

```python
from pprint import pprint

pprint(dock_lifecycle.diagnose())
```

module reloadは古いcontrollerとMaya callbackを残さないよう、完全破棄後に実行します。

```python
from importlib import reload
from bd_util._dev.maya.ui import dock_lifecycle

dock_lifecycle.dispose()
reload(dock_lifecycle)
dock_lifecycle.show()
```

### 状態保存の責務

ドッキング位置、タブ構成、ドック幅、フローティング状態はMayaのworkspaceControlへ委ねます。
内側のWidgetへ`WindowStateStore.restoreGeometry()`を適用するとMaya側の復元と競合するため、
dockable Widgetのgeometry保存には使用しません。

tool固有のSplitter幅や選択タブは`UiStateManager`でtool単位の`ui.ini`へ
保存します。Window geometryとは別の`ui_state` groupで管理するため、dockable Windowでも
同じ仕組みを利用できます。

## Maya 2025 / 2026 / 2027 UI互換性確認

Qt facade、Window lifecycle、Maya UI連携の自動テストは、対応する各Mayaの`mayapy`で
同じコマンドから実行できます。

```powershell
.\scripts\test-ui-maya2025.cmd
.\scripts\test-ui-maya2026.cmd
.\scripts\test-ui-maya2027.cmd

# 3 versionを順番に確認する。
.\scripts\test-ui-maya-all.cmd
```

各versionでは、Maya、Python、Qt bindingの実バージョンを表示した後、汎用Qt/UIテストと
Maya APIを使うUIテストを独立したmayapy processで実行します。pytestはrepository直下の
`.test`から読み込み、統一検証では`.\scripts\verify.cmd`が3 versionを実行します。
Qt/UI用processでは、root conftestのMaya初期化より先に`QApplication`を生成します。
Mayaが先に`QGuiApplication`を作り、Widgetのtestがskipされる状態を避けるためです。

2026-09-12にFloatSliderSpinBoxと複合Viewのサンプルを追加した作業ツリーでの確認結果です。

| Maya | Python | Qt binding | `tests/ui` | `tests/maya/ui` |
| --- | --- | --- | --- | --- |
| 2025 | 3.11.4 | PySide6 6.5.3 | 437 passed | 244 passed |
| 2026 | 3.11.9 | PySide6 6.5.3 | 437 passed | 244 passed |
| 2027 | 3.13.9 | PySide6 6.8.3 | 437 passed | 244 passed |

`verify.cmd`はBlack、3 versionのPyright contract、Maya 2025 full pytest、
上表の3 version UI互換性テスト、`git diff --check`を実行します。
Maya 2025 full pytestは`2758 passed, 346 skipped`です。全体実行ではMaya初期化が先になるため
Widgetを必要とするtestがskipされますが、上表のUI専用processではskipなしで確認しています。
Maya 2027には`QtTest`が同梱されていないため、入力テストは標準のQt key eventを使います。
Maya本体での手動表示・操作確認は、この自動テスト結果に含めません。

Maya 2027のPySide6 6.8では、bound methodを指定するsignal切断が`RuntimeWarning`になるため、
ownerの`destroyed`接続は`QMetaObject.Connection`を保持し、その接続オブジェクトを使って
解除します。この方法はMaya 2025 / 2026同梱のPySide6 6.5でも利用できます。

mayapyでは実際のworkspaceControl表示やMaya再起動後の復元までは確認できません。各versionの
Maya Script Editorで次を実行し、同じハーネスを表示します。

```python
from pprint import pprint

from bd_util._dev.maya.ui import dock_lifecycle

window = dock_lifecycle.show()
pprint(dock_lifecycle.diagnose())
```

各versionで、次の共通項目を確認します。

1. dockとfloatingの切り替え、`Close`後の再表示、`Dispose`後の再生成ができる。
2. Splitter幅、選択タブ、workspaceControlがMaya再起動後に復元される。
3. `SelectionChanged`が1操作につき1行だけ記録され、module reload後に重複しない。
4. `Reset`で初期配置と初期Widget状態へ戻り、新しいWindowが表示される。
5. floating時に`move_offscreen_for_test()`後の`ensure_on_screen()`で画面内へ戻る。

詳しい操作手順は前節の「実Mayaでのlifecycle統合確認」を参照してください。

## 保守時に維持する設計境界

UI基盤を変更・拡張するときは、次のcontractを維持します。

- `bd_util.ui`はMayaをimportせず、Maya固有処理は`bd_util.maya.ui`へ置く。
- Qt Bool Viewは生成時にBindingからViewModelを解決し、入力・表示はViewModelへ接続する。
  受け取ったBindingは参照保持し、Qt parentや共有Bindingの終了責任は引き取らない。
- PySideとshibokenは利用側から直接importせず、`bd_util.ui.qt`をbinding境界とする。
- bool bindingのViewModelはViewを所有・破棄せず、破棄通知からのUI操作を遅延させる。
  View生成順の制約を利用側へ戻さず、共有時は個々のWindowから独立したownerを使う。
  詳細と回帰テストの入口は[設計・保守メモ](bool_binding_design.md)を参照する。
- dockable Windowの配置はworkspaceControlへ委ね、内側のWidgetへ通常Window用geometryを
  復元しない。
- Maya終了時にWidgetから状態を再取得せず、変更signalで退避済みの状態を保存する。
- ownerの`destroyed`接続は`QMetaObject.Connection`を保持して解除し、PySideのversion差を
  bound methodの再検索へ依存させない。
- closeの既定は`retain=False`とし、WindowとMaya callbackを完全破棄する。非表示中も処理を
  継続する明確な要件があるtoolだけ`retain=True`を指定する。
- QHeaderViewの列幅・表示順は共通保存へ追加せず、必要なtoolが個別に管理する。
- Qt facade、Window lifecycle、Maya UI連携の変更中は`test-ui-maya-all.cmd`で
  切り分け、最終確認は`verify.cmd`を実行する。
  workspaceControl、再起動復元、実画面配置に関わる変更は各versionのMaya本体でも確認する。
