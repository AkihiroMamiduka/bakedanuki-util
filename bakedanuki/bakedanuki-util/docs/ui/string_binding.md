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

本段階は単一属性と一行入力を対象とします。複数属性の混在表示と複数行編集は
別の仕様として検討します。
