# Python正本とMaya Viewの単一float同期

`MayaFloatBinding`はPython属性を正本とし、Qtの`FloatSpinBox`とMaya属性を同期します。
Maya属性自体を正本にする[既存のMayaFloatPlugBinding](float_binding.md)とは別の入口です。
初期同期ではPythonの値をMayaへ適用します。

## 最小の組み込み

```python
from dataclasses import dataclass

import bd_util as bdu
from bd_util.maya.ui import MayaFloatBinding
from bd_util.ui import FloatSpinBox, qt


@dataclass
class Settings:
    offset_x: float = 100.0  # cm


class OffsetWidget(qt.QWidget):
    def __init__(self, data: Settings, node_name: str, parent=None):
        super().__init__(parent)
        nodes = bdu.Nodes()
        node = nodes.existing.transform(node_name)
        self.binding = MayaFloatBinding.from_attribute(
            data, "offset_x", maya_plug=node.translate.translateX, parent=self
        )
        self.spin_box = FloatSpinBox(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

`maya_plug=None`ならPython属性とQtだけで動作します。名前からplugを指定するときは
`resolve_float_plug(node_name, "translateX")`を使います。対応するMaya属性は既存scalar版と
同じfloat・double・doubleLinear・doubleAngleで、compoundのscalar子も対象です。

## APIと責務

| API | 役割 |
| --- | --- |
| `MayaFloatBinding.from_attribute(instance, attribute_name, maya_plug=..., presentation=..., parent=...)` | Python Store、ViewModel、任意のMaya Viewを所有する |
| `MayaFloatBinding(store, maya_plug=..., parent=...)` | 独自のPython側Storeを接続する |
| `MayaFloatPlugView(view_model, plug, owner)` | Store接続済みViewModelへMayaを編集・表示先として追加する |
| `binding.value` / `changed` / `set_value()` / `refresh()` | 単一float共通の操作窓口 |
| `binding.store.instance` | 元のPython objectを具体型のまま返す |
| `binding.maya_view` | Mayaとの同期状態と再同期操作の窓口。未指定時はNone |
| `maya_view.is_synchronized` | Python確定値がMayaの格納精度で同期できているか |
| `maya_view.last_sync_error` / `sync_failed` | 直近の同期例外と通知 |
| `maya_view.sync_from_view_model()` | 最後に確定したPython値をMayaへ再適用する。失敗時は例外を送出する |

1つのViewModelへ接続できるMaya Viewは1つです。複数のQt Viewでは同じBindingまたは
ViewModelを共有します。Maya Storeを正本とするViewModelへのMaya Viewの追加は拒否します。

Qt入力はCommandからPython Storeへ渡し、setter後の確定値をQtとMayaへ反映します。
Mayaからの入力はcallback中に書き戻さず、次のQt event loopでCommandへ渡します。
setterが補正・拒否した場合は、通常の入力ではPython確定値をMayaへ再表示します。

Python属性へ直接代入したときは、従来どおり`binding.refresh()`が必要です。
同値のCommandやrefreshも、先に届いていた未処理のMaya入力より優先します。
Mayaへの描画中のcallbackは抑制し、通知先でさらにPythonを編集した場合は最新値を採用します。

## 単位と精度

| 接続する属性 | Python側の値 | Qt表示 |
| --- | --- | --- |
| doubleLinear / translateX | cm | Mayaの現在の距離単位 |
| doubleAngle / rotateX | degree | Mayaの現在の角度単位 |
| float・double / scaleX | 単位なし | 単位なし |

Python属性名から単位を推測せず、接続先の型に上表の契約で合わせます。
単位変更callbackは表示情報だけを更新し、Python値や保留中のMaya入力を変更しません。
`presentation`のminimum/maximumはPython側の公開単位で指定し、その制約を維持します。
Maya Viewの接続中はscale/suffixをMayaの表示単位で上書きします。
Maya側のhard limitは同期時の制約として検証し、Pythonの編集範囲へは取り込みません。

内部では`FloatViewModel.set_presentation_adapter()`がStoreの表示情報を変換します。
この拡張点は値を変更せず、Storeのrefresh時にも適用されます。Maya Viewの接続中は
そのViewが管理します。明示dispose時に解除し、Qt ownerからViewが破棄された場合は
次のrefreshでPython側の表示情報へ戻ります。変換側はViewを弱参照で保持します。

小数桁数は各`FloatSpinBox`が管理します。表示更新や未編集のEnterでPython値を丸めません。
Mayaの32bit floatへ投影する際もPython正本は丸めず、変換後に得られる格納値との一致を
判定します。Python値とMaya値が数値として完全一致しなくても、正しい格納結果なら同期済みです。
汎用の許容誤差で小さな編集を隠す処理は行いません。

floatの範囲超過・非ゼロ値のunderflowなどはMayaへ書く前に同期エラーとし、Python値を維持します。
距離・角度の変換で生じる往復誤差も、新しいMaya入力としてPythonへ戻しません。

## lock・接続・同期失敗

対象plugやcompoundの親がlock・入力接続を持つ場合、Mayaへの書き込みを停止します。
接続から評価された値はPythonへの編集入力として扱いません。Python側のStoreが編集可能なら
QtとPythonの編集は継続し、同期できなかったことをMaya Viewの状態として公開します。

通常のlock解除・入力切断では保留していたPython値を再同期します。短時間の接続・切断も
Python正本を維持します。再び書き込み可能になった後に新しいMaya値を設定した場合は、
その新しい入力を採用します。

非同期処理の例外は`last_sync_error`と`sync_failed`へ公開します。Python Command自体が
成功した後のMaya同期失敗は、Python値を巻き戻しません。setterが値を変更してから例外を
送出した場合は可能なら正本を再読込し、元の例外を保持します。不正値やgetterの失敗で
正本を読めなくなった場合は入力を停止し、修復後の`binding.refresh()`で復帰できます。

Pythonが読み取り専用の場合、Mayaからの入力は採用せず同期失敗として残します。
`sync_from_view_model()`でPython確定値をMayaへ戻せます。初期同期の失敗はconstructorから
例外を送出し、生成途中のcallbackとMaya View接続枠を解放します。

## Undo / Redo

PythonからMayaへの値設定は`cmds.setAttr()`を使い、MayaのUndo対象になります。
MayaのUndo/Redoで復元された値はPythonのCommandへ渡します。値が受理されれば追加の
setAttrを実行しないため、Redo履歴を維持します。

通常のMaya入力に対するsetter補正の書き戻しも、独立したMaya Undoになります。
その書き戻しをUndoした値がPythonの制約と一致しない場合、補正を繰り返して履歴を上書きせず、
Python確定値とMaya復元値の不一致を同期保留として公開します。続くUndo/Redoを行うか、
PythonのCommand・refresh・明示再同期で確定値を適用できます。

Undo/Redo中の変更かどうかは、Maya callback中の`MGlobal.isUndoing()`／`isRedoing()`を
記録して判断します。[Autodesk APIリファレンス](https://help.autodesk.com/cloudhelp/2025/ENU/MAYA-API-REF/cpp_ref/class_m_global.html)

Pythonだけの変更をMayaのUndoへ登録する機能や、PythonとMayaをまとめたtransactionは
提供しません。MayaからUndoで取り戻すPython値はMayaに格納されていた実値であり、
32bit floatへの投影前のPython値の末尾精度までは復元しません。

## 寿命とサンプル

BindingのdisposeやQt ownerの破棄でcallbackを解放します。Maya Viewだけをdisposeした場合や
対象nodeが削除された場合は、Python StoreとQt編集を継続できます。予約済みのMaya入力は
終了後に適用しません。PythonデータとMaya nodeを削除・復元しません。

```python
from bd_util._sample.maya.ui.float_sample import maya_view
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData

data = TransformFloatData(translate_x=10.0, rotate_x=45.0, scale_x=1.0)
window = maya_view.show("pCube1", data)
```

既存transformのtranslateX・rotateX・scaleXへPython初期値を適用します。
dataを省略した場合はサンプル既定値を使います。nodeは作成しません。
3行の表示桁数は起動時のChannel Box設定を使い、Translate Xには6桁の共有Viewも配置します。

1. Qt・Channel Boxの双方から編集し、Pythonデータと表示が揃うことを確認する。
2. Preferencesの距離・角度単位を変更し、Python値を維持したまま表示が切り替わることを確認する。
3. `Set Python data`でPythonだけを変更し、`Refresh views`でQtとMayaへ反映する。
4. Mayaのlock中にQtで変更し、`Retry Maya sync`の結果がPendingになることを確認する。
5. lock解除後に再試行し、最新のPython値が反映されることを確認する。
6. close後に同じdataを渡してshowし、保持したPython値で再表示する。

`Last sync check`はボタン操作時点の結果です。詳細な失敗理由は各Bindingの
`maya_view.last_sync_error`から確認できます。showの再呼び出しでは前のWindowを終了して
新しいWindowを作ります。`maya_view.dispose()`でサンプル全体を終了できます。

## 検証

- `tests/maya/ui/test_float_plug_view.py`: 単位、格納精度、setter、Undo/Redo、親lock・接続、再同期。
- `tests/ui/test_python_float_maya_view.py`: 共有Widget、寿命、通知からの再入、サンプルと生成途中の解放。
- `tests/typecheck/maya_float_binding_contract.py`: 公開API、Storeの具体型、Qt View・サンプルの補完。

最終検証は`scripts/verify.cmd`で行います。Mayaを正本とする単一値・3成分版、および
Pythonだけの単一値・3成分版も回帰確認します。Pythonの3成分tupleからMayaのcompound全体へは
[MayaFloat3Binding](python_float3_maya_binding.md)で同期できます。
