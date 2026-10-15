# Python正本とMaya Viewの整数同期

`MayaIntBinding`はPython整数属性を正本とし、Qtの`IntSpinBox`・`IntLabel`と
Mayaの整数属性を同期します。**生成時はPython初期値をMayaへ適用します。**
Maya属性を正本にする場合は[整数binding](int_binding.md)の`MayaIntPlugBinding`を使用します。

## 最小の組み込み

```python
from dataclasses import dataclass

from bd_util.maya.ui import MayaIntBinding, resolve_int_plug
from bd_util.ui import IntLabel, IntSpinBox, qt


@dataclass
class Settings:
    count: int = 128


class CountWidget(qt.QWidget):
    def __init__(self, data: Settings, node_name: str, parent=None):
        super().__init__(parent)
        self.binding = MayaIntBinding.from_attribute(
            data,
            "count",
            maya_plug=resolve_int_plug(node_name, "count"),
            parent=self,
        )
        self.spin_box = IntSpinBox(self.binding, self)
        self.value_label = IntLabel(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.value_label)
```

既存nodeにbyte・short・longの`count`属性が必要です。属性は自動追加しません。
compoundの整数子も扱えます。compound親、配列配下、int64、bool、enum、time、
float属性は対象外です。`maya_plug=None`ならQtとPythonだけで動作します。

## APIと同期方向

| API | 役割 |
| --- | --- |
| `MayaIntBinding.from_attribute(instance, attribute_name, maya_plug=..., presentation=..., parent=...)` | Python属性のStoreと任意のMaya Viewを所有する |
| `MayaIntBinding(store, maya_plug=..., parent=...)` | 独自のPython側整数Storeを接続する |
| `MayaIntPlugView(view_model, plug, owner)` | Python Store接続済みのViewModelへMaya Viewを追加する |
| `binding.value` / `changed` / `set_value()` / `refresh()` | 単一整数の共通操作 |
| `binding.store.instance` | 元のPython objectを具体型のまま返す |
| `binding.maya_view` | 同期状態と再同期操作の窓口。同期先未指定なら`None` |
| `maya_view.is_synchronized` | PythonとMayaが一致し、保留入力もないか |
| `maya_view.last_sync_error` / `sync_failed` | 直近の同期例外と通知 |
| `maya_view.sync_from_view_model()` | Python確定値をMayaへ明示再適用する。書込み時は`True`、同値なら`False`、失敗時は例外 |
| `maya_view.plug_operator` / `view_model` | 接続した整数plugとViewModel |

1つのViewModelにつきMaya Viewは1つです。Qt Viewは同じBindingやViewModelを共有できます。
Maya属性を正本とする`MayaIntPlugBinding`／`MayaIntPlugsBinding`のViewModelへ、
このMaya Viewを追加することは拒否します。

Qt入力はCommandからPython Storeへ渡し、setter後の確定値を各Viewへ反映します。
Channel Boxや`cmds.setAttr()`の入力も、Maya callback完了後のQt event loopで同じCommandへ
渡します。setterの補正・拒否後はPython確定値をMayaへ再表示します。
Mayaへの描画中のecho通知は折り返さず、通知先でさらにPythonを再編集した場合は最新値を採用します。

Python属性へ直接代入した場合は`binding.refresh()`で同期します。
同値のCommandやrefreshも、それ以前の未処理Maya入力より優先します。

## 整数型と範囲

公開値は`-2147483648`～`2147483647`の整数です。`bool`・小数・文字列を暗黙変換せず、
範囲を超えるPython整数も拒否します。Mayaへの同期でも小数化・丸め・clampは行いません。

| Maya型 | 同期できる型範囲 |
| --- | --- |
| byte | 0～255 |
| short | -32768～32767 |
| long | -2147483648～2147483647 |

`IntPresentation`はPython側の入力制約です。Mayaの型範囲とhard limitは同期時の追加制約として
検証し、Python側の編集範囲に取り込みません。例えばbyteへ同期中のPython値が`300`なら、
PythonとQtは`300`を保持し、Mayaへの書込みだけを保留して`ValueError`を公開します。
Maya属性のhard limitは、同期のたびに現在の制約で検証します。

## lock・入力接続・同期失敗

同期先やcompound祖先がlock・入力接続を持つ間はMayaへの書込みを停止します。
接続の評価値はPythonへの編集入力として扱いません。Python Storeが編集可能ならQtの編集は
継続でき、通常のlock解除・入力切断後は保留していたPython値を再同期します。
再び書込み可能になった後で新しいMaya入力が届けば、その入力を採用します。

これはPython正本用の同期方針です。アニメーション・SDK・Layerへの値入力は、
Maya正本の`MayaIntPlugBinding(..., edit_connected=True)`を使用します。
`MayaIntPlugView`に接続編集フラグはありません。

初期同期の失敗はconstructorから例外を送出し、生成途中のcallbackと接続枠を解放します。
運用中の非同期エラーは`last_sync_error`と`sync_failed`で公開し、成功時にエラーを解除します。
Python Command成功後のMaya同期失敗ではPython値を巻き戻しません。
setterが一部更新後に例外を送出した場合は可能なら正本を再読込し、元の例外を保持します。
不正値やgetter失敗で正本を読めなくなった場合は入力を停止し、修復後のrefreshで復帰できます。

読み取り専用のPython属性ではMaya入力を採用せず、同期失敗を保持します。
明示的な`sync_from_view_model()`でPython確定値をMayaへ戻せます。

## Undo／Redoと寿命

Mayaへの値設定は標準`cmds.setAttr()`を使い、Undo／Redo対象になります。
履歴で復元された値はPythonのCommandへ渡します。受理された場合は追加書込みせず、
Redo履歴を維持します。通常入力のsetter補正は独立したMaya Undoになります。
補正をUndoした復元値がPythonの制約と一致しない場合は、再補正の書込みを保留して履歴を維持します。
続くUndo／Redo、PythonのCommand・refresh、明示再同期で状態を更新できます。
Pythonだけの変更をMaya Undoへ登録する機能や、両者をまとめたtransactionは提供しません。

Bindingのdispose、ViewModel終了、Qt owner破棄、node・対象属性削除でcallbackを解除します。
Maya Viewだけをdisposeした場合や対象削除後も、PythonとQtの編集を継続できます。
終了後の予約済み入力は適用せず、削除Undoや同名再作成で自動再接続しません。
PythonデータとMaya nodeは削除しません。reload前はWindow／Bindingをdisposeします。

## 操作確認用サンプル

Maya Script EditorのPythonタブで実行します。現在のsceneを消去せず、
検証用transformを一つ追加します。short属性だけhard limitを-20～20にしています。

```python
import bd_tools
bd_tools.reload_package(reload_util=True)

from bd_util._sample.maya.ui.int_sample import maya_view

window = maya_view.show_demo()
data = window.widget.data
node_name = window.node_name
```

1. QtとChannel Boxの双方から変更し、Python値・共有入力欄・ラベルが揃うことを確認する。
2. 「Python値を直接変更」後はMaya値が変わらず、「Refresh」で反映されることを確認する。
3. byte欄に`300`、short欄に`30`を入力し、「Maya同期を再試行」でPendingと理由を確認する。
   Python値は維持され、Maya値は変わらない。有効範囲へ戻すと同期が復帰する。
4. Channel Boxでlong属性をlockし、Qtで値を変え、lock解除後に再同期されることを確認する。
5. MayaのUndo／RedoでPython値・Qt表示も追従することを確認する。
6. Windowを閉じて`maya_view.show(node_name, data)`を実行し、同じデータで再表示する。

結果欄はボタン操作時点の同期状態です。`show()`の再呼出しは前のWindowを終了します。
`maya_view.dispose()`でサンプルを終了できます。utilだけを使用する環境では、
サンプルをdisposeした後に`bd_util.reload_package()`を使用してください。

## 検証

- `tests/maya/ui/test_int_plug_view.py`: 三種類の整数、setter、型範囲、hard limit、接続、Undo、削除。
- `tests/ui/test_python_int_maya_view.py`: 共有View、所有者破棄、再入通知、サンプルと途中失敗。
- `tests/typecheck/python_int_maya_binding_contract.py`: 公開API、Python正本の具体型、Viewとサンプルの補完。

最終検証は`scripts/verify.cmd`で実施します。Maya 2025／2026／2027のUI互換性を含みます。

今回の実装では`verify.cmd`が成功しました。

| 確認対象 | 結果 |
| --- | --- |
| Black・3 versionのPyright契約 | 成功。型エラー・警告は0件 |
| 新しい実装とサンプルの個別Pyright | Maya 2025／2027で成功。型エラー・警告は0件 |
| Maya 2025 full pytest | 8,241件成功、837件は既定の条件でskip |
| Maya 2025／2026／2027 Qt UI | 各950件成功。新規の共有View・サンプル9件を含む |
| Maya 2025／2026／2027 Maya UI | 各804件成功。新規の整数同期55件を含む |

full pytestで省略するQtテストは、続く専用のUI互換性テストで実行しています。
今回追加したPython正本とMaya整数同期の利用者によるMaya本体確認はこれからです。
