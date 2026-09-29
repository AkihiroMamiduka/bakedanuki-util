# string MVVM binding

`bd_util.ui`の文字列基盤は、一つの確定値を`StringValue`で公開し、
`SetStringCommand`から正本の`StringValueStore`へ変更を要求します。
`StringViewModel`が実値を再読込みし、`StringBinding`が接続と寿命を管理します。
暗黙の`str()`変換は行わず、Python属性もMaya属性も`str`だけを扱います。
空文字は有効値で、Mayaの未設定string属性も空文字として公開します。

## Maya属性を正本にする

既存jointの`.otherType`を一行で編集する例です。Windowを開くだけではsceneへ書き込みません。
`.type`や`.drawLabel`は変更しないため、Maya viewportでラベルを表示したい場合は
利用側でそれぞれ`Other`と`True`へ設定してください。

```python
from bd_util.maya.ui import MayaStringPlugBinding, resolve_string_plug
from bd_util.ui import StringLabel, StringLineEdit

binding = MayaStringPlugBinding(resolve_string_plug("joint1", "otherType"), parent=window)
line_edit = StringLineEdit(binding, window)
label = StringLabel(binding, window)

# Windowの終了時やreload前に呼ぶ
binding.dispose()
```

実際にWindowを開くサンプルは次のとおりです。既存joint名を渡してください。

```python
from bd_util._sample.maya.ui.string_sample import maya_plug

window = maya_plug.show("joint1")
maya_plug.dispose()
```

`resolve_string_plug()`は既存の単一typed string属性だけを受け付けます。
配列、配列配下の子、numeric属性、存在しない属性は拒否します。
`MayaStringPlugBinding`はMaya値を正本とし、外部の属性変更、lock、入力接続、改名、
Undo / Redoを反映します。nodeまたは属性が削除された場合はcallbackを解除して入力を停止し、
Undoや同名nodeの再作成で自動再接続しません。書込みは`cmds.setAttr(..., type="string")`
によるMaya標準Undoを使用します。NUL文字はMayaへの書込み前に拒否します。

## Python属性を正本にする

```python
from bd_util.ui import StringBinding, StringLineEdit

binding = StringBinding.from_attribute(data, "name", parent=window)
line_edit = StringLineEdit(binding, window)
binding.refresh()  # callback外でPython属性を変更した後に呼ぶ
```

Python属性のgetter・setterを通して読み書きし、setterが補正した値を再読込みします。
属性の型が`str`でなければ例外にします。`StringBinding(store)`には独自の
`StringValueStore`も接続できます。Storeは`is_available`、`is_writable`、
`read() -> str`、`write(value: str) -> str`を実装してください。

Python正本とMaya属性を双方向同期する場合は`MayaStringBinding.from_attribute(
data, "name", maya_plug=resolve_string_plug(...))`を使用します。同一ViewModelへ
接続するMaya Viewは一つです。同期失敗は`maya_view.last_sync_error`、
`maya_view.sync_failed`、`maya_view.is_synchronized`で確認できます。

## 一行Viewの確定規則

`StringLineEdit`はユーザーの編集中の文字列を正本へ送らず、Enterまたは通常の
フォーカス移動で一度だけ確定します。Escapeは未確定入力を破棄します。
編集中に正本が外部変更された場合は入力欄の文字列を維持し、`hasConflict()`と
`conflict_changed`で知らせます。この状態の通常のフォーカス移動は書込みません。
Enterによる明示操作だけが新しい正本を上書きします。利用側は競合表示と
Enter / Escapeの案内を付けてください。サンプルWindowにはその表示があります。

同じBindingを複数の`StringLineEdit`と`StringLabel`へ渡せます。確定後は全Viewへ
実値が伝わります。`StringLabel`はplain textとして表示し、選択・コピーできます。
`setInputEnabled(False)`や正本のlock中も入力欄はread-onlyとなり、コピーはできます。
同じ文字列を再表示するときに`QLineEdit.setText()`を避け、編集中の選択やQtのUndo履歴を
不要に消しません。Qtの既定の32767文字制限による黙った切り詰めも避けます。

## 複数のMaya string属性を一括編集する

`MayaStringPlugsBinding`は、順序付きの単一typed string属性群を同じ一行Viewへ接続します。
最初の属性を代表として表示し、生成・`refresh()`・外部変更では書き込みません。
代表以外の値が異なる場合は`is_mixed`で確認します。混在は入力文字列へ埋め込まず、
`state_changed`を受けて別の表示へ反映してください。

```python
from bd_util.maya.ui import MayaStringPlugsBinding, resolve_string_plug
from bd_util.ui import StringLineEdit

binding = MayaStringPlugsBinding(
    [resolve_string_plug(name, "otherType") for name in joint_names],
    parent=window,
)
line_edit = StringLineEdit(binding, window)
binding.apply_representative_value()  # 代表値で編集可能な後続属性を揃える
binding.set_value("")                # 空文字を明示的に全対象へ設定する
```

`value`・`changed`は代表の確定値、`is_mixed`は利用可能な対象の値の混在を示します。
`target_count`・`writable_count`・`target_states`・`state_changed`・`edit_failed`は
既存の複数属性Bindingと同じ用途です。代表値が変わらず後続だけ変わる場合は
`changed`ではなく`state_changed`で通知します。代表値と同じ明示入力も後続の
差分へ適用でき、差分がなければ書込み・Undoを増やしません。

明示入力は編集可能な対象へ一回のMaya Undoで適用します。lock・入力接続・削除済みの
後続対象を除外し、代表が編集不可なら全体を停止します。途中失敗では今回変更した
値を逆順で復旧します。復旧にも失敗すれば両方の例外を公開します。
空文字とMaya未設定値は同一視し、文字列を暗黙変換・trimしません。NUL文字は
全対象の書込み前に拒否します。対象削除をUndoしたり同名nodeを再作成したりしても
自動再接続しません。選択対象を変えるときはBindingを作り直してください。

`StringLineEdit`は編集中に後続対象だけが外部更新された場合も競合を検出し、
通常のフォーカス移動では入力を上書きしません。代表値と同じ文字列を入力欄で
再確定する操作はQtから変更入力として届かないため、`apply_representative_value()`を
明示操作へ割り当ててください。代表が空文字の混在状態を全件空文字へする場合は
`set_value("")`を使います。編集中の文字列と外部更新後の代表値が一致した場合は
未確定状態と競合を解除します。`StringViewModel.source_changed`は代表以外も含む
属性群の状態変更を入力Viewへ通知します。

既存jointを対象にするサンプルは次のとおりです。選択中のjointを一度だけ取得し、
Window表示後の選択変更には自動追従しません。`.type`・`.drawLabel`・`.otherType`は
Windowを開くだけでは変更しません。

```python
from bd_util._sample.maya.ui.string_sample import maya_plugs

window = maya_plugs.show_selected()
# または maya_plugs.show(["joint1", "joint2"])
maya_plugs.dispose()
```

複数行編集と配列属性は現在の対象外です。
