# Mayaノード名を正本にするstring binding

`MayaNodeNameBinding`は既存ノード一つの名前を正本とし、既存の`StringLineEdit`や
`StringLabel`へ接続します。属性の`MPlug`を介さず、名前の読み書きとMaya callbackを
`MayaNodeNameStore`が担当します。確定値・Command・入力中の文字列は既存string基盤と共通です。

## 最小構成

```python
import bd_util as bdu
from bd_util.maya.ui import MayaNodeNameBinding
from bd_util.ui import StringLabel, StringLineEdit

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
node = nodes.existing("existing_node")

binding = MayaNodeNameBinding(node, parent=window)
line_edit = StringLineEdit(binding, window)
label = StringLabel(binding, window)

binding.set_value("new_name")  # Maya標準Undoに載る名前変更
binding.refresh()              # 現在名と編集可否の再読込み
binding.dispose()              # Window終了時やreload前に呼ぶ
```

`node`には`NodeOperator`を渡します。文字列からの解決は`nodes.existing()`で明示し、
同名DAGの場合は一意なパスを指定してください。構築時は現在名を読むだけで、ノード作成や
sceneへの書込みは行いません。Bindingは受け取った実体を固定し、選択変更には追従しません。
選択監視、代表ノードの決定、別ノードへの切替えは利用側で行い、切替え時は古いBindingを
`dispose()`して作り直します。

## 表示と名前変更

`binding.value`と`binding.changed`は、namespaceを含みDAGパスを含まない確定名を扱います。
たとえば`|group|character:control`の表示は`character:control`です。

| 入力 | 対象が`character:control`の場合 |
| --- | --- |
| `hand` | 同じnamespace内の`character:hand`へ変更要求 |
| `character:hand` | 同じnamespace内の`character:hand`へ変更要求 |
| `other:hand` | 別namespaceへの移動になるため拒否 |

namespaceの変更は別操作として行ってください。現在のMaya namespaceに依存して別の
namespaceへ移動しないよう、名前変更の対象を解決します。

既存名との衝突はMayaへ委ね、自動採番などを適用した実際の名前を読み直して全Viewへ
表示します。同じ確定名への変更要求は書込みもUndo履歴も増やしません。名前変更は
`cmds.rename()`によるMaya標準Undoを使用し、`NodeOperator`の`ModifierManager`へは
予約しません。そのため上の`set_value()`後に`mod.do_it_dg()`を呼ぶ必要はありません。

Transformに付随するShape名は、既定ではMaya標準の名前変更に従います。
`MayaNodeNameBinding(node, rename_shapes=False, parent=window)`とすると、
その名前変更からのShape名の追従を抑止します。

## 入力と失敗

`StringLineEdit`の未確定入力はEnterまたは通常のフォーカス移動で確定し、Escapeで
破棄します。通常EnterとテンキーEnterは入力欄内で処理し、親WindowやMaya側へ
確定キーを伝播させません。入力欄へフォーカスした時と確定直前にも正本を読み直します。
マウスでフォーカスした最初の左クリック後は、既定で確定名を全選択します。
クリック位置から入力したい場合は`select_all_on_mouse_focus=False`を指定できます。

編集中の外部リネームでは、既定で入力文字列を保ち`hasConflict()`と`conflict_changed`で
競合を知らせます。競合中の通常フォーカス移動では書き込まず、Enterで明示した場合だけ
下書きを変更要求として扱います。`follow_source_during_edit=True`を指定したViewでは、
外部の確定名を優先して下書きを破棄します。詳しい共通規則は
[string binding](string_binding.md#一行viewの確定規則)を参照してください。

UIからの失敗は`StringLineEdit.edit_failed`がエラーメッセージを通知し、入力欄を
正本の確定名へ戻します。利用側はsignalをステータス表示などへ接続してください。
`binding.set_value()`を直接呼んだ場合の失敗は例外として返り、呼出元で対処します。
編集不可のためCommandが実行されなかった場合や、確定名が変わらなかった場合の戻り値は
`False`です。不正な入力や、実行したMayaコマンドが拒否した変更は例外になります。

## 外部変更・編集可否・寿命

通常の名前変更とUndo／Redoを監視し、現在の名前をViewへ反映します。
namespace自体の名前変更、およびnode lock・name lockの変更については定期pollを行わず、
入力欄へのフォーカス・確定前・明示的な`binding.refresh()`で再確認します。
参照ノード、node lock、name lockでは編集を停止し、表示とコピーを維持します。
それ以外の制約でMayaが変更を拒否した場合は、入力失敗として通知します。
lock解除後すぐに表示状態を更新したい場合は`refresh()`を呼んでください。

対象ノードが削除されるとcallbackを解除し、入力を停止します。最後の確定名は残ります。
削除のUndoや同名ノードの再作成でも自動接続しません。再び編集するには新しいBindingを
作成してください。`dispose()`、Qt ownerの破棄、Maya終了でも監視を終了します。
WindowやmanagerがBindingを保持し、reload前には明示的に`dispose()`してください。

## 操作サンプル

既存ノード名を明示して、二つの入力欄と確定名ラベルを開きます。

```python
from bd_util._sample.maya.ui.string_sample import node_name

window = node_name.show("existing_node")
node_name.dispose()  # 終了時やbd_utilのreload前に呼ぶ
```

importやWindowの表示ではsceneに書き込みません。Windowを開いた後の選択変更でも
対象は変わりません。状態・競合・エラー表示とRefreshボタンを備えています。

Maya本体では次を確認します。

1. 通常EnterとテンキーEnterで確定し、同じ確定名が共有入力欄とラベルに表示される。
2. 先にOutlinerを操作した場合も、確定後にOutlinerが名前編集へ入らない。
3. 他ノードと同じ名前を要求すると、Mayaが採番した確定名を表示する。
4. 外部リネームとUndo／Redoに追従し、編集中は競合の案内を表示する。
5. name lockを変更してRefreshすると読み取り専用表示が切り替わる。
6. 別namespaceを指定した入力はエラー表示となり、確定名へ戻る。
7. Windowを閉じるか`dispose()`した後はcallbackが残らず、対象ノードは残る。

自動テストは`tests/maya/ui/test_node_name_binding.py`と
`tests/ui/test_node_name_sample.py`でMaya連携とサンプルの寿命を確認します。
共通Viewの入力規則は`tests/ui/test_string_binding.py`で確認し、最終検証は
リポジトリ直下の`.\scripts\verify.cmd`を使用します。
