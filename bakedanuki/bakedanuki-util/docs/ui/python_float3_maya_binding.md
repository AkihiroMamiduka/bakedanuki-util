# Python正本とMaya Viewの3成分同期

`MayaFloat3Binding`はPython属性のXYZ tupleを正本として、`Float3SpinBox`とMayaの
`translate`・`rotate`・`scale`を同期します。初期同期ではPython値をMayaへ適用します。
Maya属性を正本にする場合は[既存のMayaFloat3PlugBinding](float3_binding.md)を使います。

## 最小の組み込み

```python
from dataclasses import dataclass

import bd_util as bdu
from bd_util.maya.ui import MayaFloat3Binding
from bd_util.ui import Float3SpinBox, qt


@dataclass
class Settings:
    offset: tuple[float, float, float] = (10.0, 20.0, 30.0)  # cm


class OffsetWidget(qt.QWidget):
    def __init__(self, data: Settings, node_name: str, parent=None):
        super().__init__(parent)
        nodes = bdu.Nodes()
        node = nodes.existing.transform(node_name)
        self.binding = MayaFloat3Binding.from_attribute(
            data, "offset", maya_plug=node.translate, parent=self
        )
        self.spin_box = Float3SpinBox(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

`maya_plug=None`ならPythonとQtだけで動作します。名前から解決する場合は
`resolve_float3_plug(node_name, "translate")`を使います。対応する属性は既存3成分版と同じ
numericのdouble3／float3で、距離・角度の3成分にも対応します。配列・配列要素、任意の
compound、整数3成分、単位種別の混在は対象外です。

## APIと責務

| API | 役割 |
| --- | --- |
| `MayaFloat3Binding.from_attribute(instance, attribute_name, maya_plug=..., presentation=..., parent=...)` | Python Store、ViewModel、任意のMaya Viewを所有する |
| `MayaFloat3Binding(store, maya_plug=..., parent=...)` | 独自のPython側3成分Storeを接続する |
| `MayaFloat3PlugView(view_model, plug, owner)` | Store接続済みViewModelへMayaの3成分Viewを追加する |
| `binding.value` / `changed` / `set_value()` / `refresh()` | 3成分共通の操作窓口 |
| `binding.view_model.x` / `y` / `z` | 各軸のViewModelとCommand |
| `binding.store.instance` | Python正本を具体型のまま返す |
| `binding.maya_view` | 同期状態と明示再同期の窓口。未指定時はNone |
| `maya_view.is_synchronized` | 全軸がPython確定値の格納結果と一致しているか |
| `maya_view.is_writable` | Mayaの親属性へ一括で書き込めるか |
| `maya_view.last_sync_error` / `sync_failed` | 直近の同期例外と通知 |
| `maya_view.sync_from_view_model()` | 最後に確定したPython tupleを再適用し、失敗時は例外を送出する |

1つのViewModelへ接続するMaya Viewは1つです。親ViewModelとXYZすべての接続枠を共有管理し、
同じ軸への単一値Maya Viewとの重複も拒否します。Maya Storeを正本とするViewModelへは
追加できません。複数のQt Viewは同じBindingまたはViewModelを共有します。

Python Store・tupleの検証・setterの契約は[Python属性の3成分binding](python_float3_binding.md)と
共通です。Maya ViewはPython Storeを書き換えず、入力を既存Commandへ渡します。
各軸のMayaアクセス・単位変換・callbackの寿命管理は単一値版と共用します。

## 各軸と一括変更

```python
binding.set_value((10.0, 20.0, 30.0))
binding.view_model.x.set_value_command.execute(5.0)
data.offset = (7.0, 8.0, 9.0)
binding.refresh()
```

各軸の編集はPython正本の最新tupleから対象軸だけを差し替え、setterを1回呼びます。
未編集軸の表示丸めや古い値は書き戻しません。setterが他軸だけを補正した場合も、
全軸の確定値をQtとMayaへ反映します。単独軸の入力範囲だけを検証する規則も維持します。

Pythonの一括Commandは全成分を検証してsetterを1回呼びます。Maya親属性の変更通知は
次のQt event loopへ集約して全軸を読み、変更対象を1つのtupleとしてCommandへ渡します。
通常の親変更ではsetterと`binding.changed`はそれぞれ1回で、中間tupleを公開しません。

Mayaへの反映は差分が1軸なら子属性へ、複数軸なら親属性へ1回の`setAttr()`で行います。
書き込む全成分の編集可否・Maya hard limit・格納精度を事前検証します。
自分の書き込みによるcallbackは入力として扱いません。

Pythonへ直接代入した場合は`binding.refresh()`が必要です。同値の軸Command・一括Command・
refreshも、先に届いた未処理のMaya入力より優先します。通知先がさらにPythonを編集した場合は
最新の確定tupleを採用します。

## 単位と精度

| 接続先 | Python tupleの単位 | Qt表示 |
| --- | --- | --- |
| translateなどの距離3成分 | cm | Mayaの現在の距離単位 |
| rotateなどの角度3成分 | degree | Mayaの現在の角度単位 |
| scale・通常のdouble3／float3 | 単位なし | 単位なし |

各成分の表示はMayaの単位変更callbackに追従し、Python値と保留中のMaya入力は維持します。
`presentation`には全軸共通の`FloatPresentation`またはXYZごとのtupleを指定できます。
各軸のminimum/maximumはPython公開単位のまま維持し、scale/suffixだけMayaの単位で上書きします。
Mayaのhard limitは同期時だけ検証し、Python側の入力範囲へ取り込みません。

小数桁数・刻み幅は`Float3SpinBox`へ指定します。表示更新や未編集のEnterで正本を丸めず、
float32への格納や単位変換の往復誤差もPythonへ戻しません。同期済み判定は公開値の完全一致、
確認済みの格納値との対応、または変換後の格納結果の一致を使い、汎用の許容誤差は使いません。
非ゼロ値のunderflow、float32の範囲超過などはMayaへの書き込み前にエラーとします。

## 一部の軸のlock・接続・同期失敗

Python Storeが編集可能なら、Maya側にlock・入力接続があってもQtとPythonの編集は継続します。
接続による評価値はPythonへの編集入力にしません。

- 複数軸の反映が必要なら、親属性へ全軸を書けることを確認します。1軸でも書けなければ、
  全体を保留してMayaへ部分反映しません。
- 差分がXだけでYが既に同期済みなら、YがlockされていてもXだけ反映できます。
- 未同期のYが残った状態でXも変えた場合は、XYZを揃えられるまで全体を保留します。

通常のlock解除・接続解除では最新のPython確定値を再同期します。1tick内の接続・切断も
Python値を維持します。`sync_from_view_model()`で明示的に再試行することもできます。

同期失敗は`last_sync_error`と`sync_failed`で公開し、成功済みのPython変更を巻き戻しません。
setterの補正・拒否は実値を採用します。setterが例外を送出した場合は可能なら正本を読み直して
Mayaへ復旧し、元の例外を保持します。getter失敗・不正tupleで正本が読めない場合は全軸の入力を
停止し、修復後の`binding.refresh()`で復帰します。読み取り専用のPython正本はMaya入力を
受け付けず、明示再同期でPython確定値をMayaへ戻せます。

初期同期が失敗した場合はconstructorから例外を送出し、生成途中のcallbackと接続枠を解放します。
PythonとMayaをまとめたtransactionや、任意のsetterの副作用を巻き戻す機能は提供しません。

## Undo / Redoと寿命

Pythonからの単独軸変更も一括変更も、Mayaへ書き込む場合は1回のUndo対象です。
MayaのUndo/Redoで復元された値をPythonのCommandへ渡し、受理されれば追加書き込みを行いません。
Mayaから復元する値は格納されていた実値で、float32投影前のPython末尾精度は復元しません。
Pythonだけの変更はMayaのUndoへ登録しません。

通常のMaya入力へのsetter補正は、独立した1回のUndo対象です。その補正をUndoした値が
Pythonの制約と合わない場合は、再補正の書き戻しでRedoを消さず同期保留にします。
続くUndo/Redoか、PythonのCommand・refresh・明示再同期で解消できます。

Bindingのdispose・owner破棄で全軸のcallbackを解放します。Maya Viewだけのdisposeやnode削除では
PythonとQtの編集を継続できます。明示disposeは表示変換を解除し、Qt owner破棄では次のrefreshで
Python側の表示情報に戻ります。終了後に予約済みのMaya入力を適用せず、PythonデータとMaya nodeの
削除・復元も行いません。

## サンプルと検証

```python
from bd_util._sample.maya.ui.float3_sample import maya_view
from bd_util._sample.maya.ui.float3_sample.data import TransformFloat3Data

data = TransformFloat3Data(
    translate=(10.0, 20.0, 30.0),
    rotate=(0.0, 45.0, 0.0),
    scale=(1.0, 1.0, 1.0),
)
window = maya_view.show("pCube1", data)
```

既存transformへPython初期値を適用します。data省略時はサンプル既定値を使い、nodeは作成しません。
Translate・Rotate・ScaleのXYZ行は起動時のChannel Box桁数を使い、Translateには6桁の共有行も表示します。

1. QtとChannel Boxから各軸・親属性を編集し、Python tupleと共有Viewの同期を確認する。
2. Preferencesの距離・角度単位を変更し、Python値を維持したまま表示単位が変わることを確認する。
3. `Set Python data`で直接代入し、`Refresh views`でQtとMayaへ反映する。
4. Yをlockして一括変更し、`Retry Maya sync`でPendingになることと、Mayaが部分変更されないことを確認する。
5. lock解除後に再試行して全軸の同期を確認し、Undo/Redoも操作する。
6. close後に同じdataを渡してshowし、保持した値で再表示する。

`Last sync check`はボタン操作時点の結果です。詳細は各Bindingの`maya_view.last_sync_error`を
参照します。`maya_view.dispose()`でWindowとcallbackを終了できます。

- `tests/maya/ui/test_float3_plug_view.py`: 各軸・一括入力、単位、精度、補正、Undo/Redo、lock・接続、寿命。
- `tests/ui/test_python_float3_maya_view.py`: 共有Widget、owner破棄、再入、表示桁数、サンプルと再表示。
- `tests/typecheck/maya_float3_binding_contract.py`: 公開API、正本・plugの具体型、Qt View・サンプルの補完。

最終検証は`scripts/verify.cmd`を使用します。既存の単一値版、Maya正本版、Pythonのみの3成分版も
回帰確認し、3 versionの結果を[UI README](README.md#maya-2025--2026--2027-ui互換性確認)へ記載します。
