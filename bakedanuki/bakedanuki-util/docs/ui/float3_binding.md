# 3成分の浮動小数点binding

Mayaの`translate`・`rotate`・`scale`などの3成分属性を正本として、XYZのSpinBoxで編集します。
[scalarの浮動小数点binding](float_binding.md)を各軸で再利用し、3成分の確定値と一括変更を
`Float3ViewModel`でまとめます。Maya固有処理は`bd_util.maya.ui`に置きます。

## 最小の組み込み

```python
import bd_util as bdu
from bd_util.maya.ui import MayaFloat3PlugBinding, get_channel_box_precision
from bd_util.ui import Float3SpinBox, qt


class TranslateWidget(qt.QWidget):
    def __init__(self, node_name: str, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        nodes = bdu.Nodes()
        node = nodes.existing.transform(node_name)
        self.binding = MayaFloat3PlugBinding(node.translate, parent=self)
        self.spin_box = Float3SpinBox(
            self.binding, self, decimals=get_channel_box_precision()
        )
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

名前から解決する場合は`resolve_float3_plug()`を使います。属性の長い名前と短い名前に対応します。

```python
from bd_util.maya.ui import MayaFloat3PlugBinding, resolve_float3_plug

binding = MayaFloat3PlugBinding(resolve_float3_plug("pCube1", "t"))
binding.set_value((100.0, 200.0, 300.0))  # cmでXYZを一括変更する。
binding.view_model.x.set_value_command.execute(25.0)  # Xだけを変更する。
print(binding.value)  # (25.0, 200.0, 300.0)
binding.dispose()
```

通常は最初の例のように`parent`を指定します。親なしBindingは明示的に`dispose()`してください。
nodeや属性を自動作成せず、終了時にもMayaデータを削除・復元しません。

## 公開API

| 入口 | 内容 |
| --- | --- |
| `Float3` | `tuple[float, float, float]`の型alias |
| `Float3Value.value` / `changed(object)` | 読み取り専用の確定値と、3成分tupleの変更通知 |
| `SetFloat3Command.execute(values)` | 3成分の変更を要求し、実値が変わったかboolで返す |
| `Float3ViewModel.x` / `y` / `z` | 各軸を担当する既存の`FloatViewModel` |
| `Float3ViewModel.value` / `set_value_command` | 全体の確定値と一括Command |
| `Float3ValueStore` | 各軸のStore、一括`read()`／`write()`、利用・編集可否の契約 |
| `Float3Binding(store, parent=...)` | 外部Storeと専用ViewModelを組み立てる |
| `MayaFloat3PlugBinding(plug, parent=...)` | Maya Store、専用ViewModel、callbackを所有する |
| `binding.value` / `changed` / `set_value()` / `refresh()` | scalar Bindingと同じ利用窓口 |
| `Float3SpinBox(source, parent=None, decimals=6, single_step=0.1)` | XYZラベルと3つの`FloatSpinBox`を横に並べるView |
| `view.x_spin_box` / `y_spin_box` / `z_spin_box` | 各軸の`FloatSpinBox` |

ViewはStore接続済みの`Float3ViewModel`または`Float3Binding`を受け取ります。
同じBindingを複数Viewへ渡せるほか、`FloatSpinBox(binding.view_model.x)`で1軸だけを
別の場所へ表示できます。Widgetの`x()`／`y()`はQtの座標取得APIとして維持します。

入力は要素数3のSequenceで、各要素は有限のfloatまたはintです。
tupleやlistに加え、既存の`Double3`・`DoubleLinear3`・`DoubleAngle3`なども渡せます。
確定値はimmutableなtupleへ正規化し、要素数の不一致、bool、文字列、NaN、無限大を拒否します。
回転の正規化や行列・Quaternionへの変換は行いません。

型付きPlugOperatorを渡すと`binding.store.plug_operator`にも具体型を維持します。
名前解決の戻り値は`MayaFloat3Plug` Protocolで、`node`とOpenMayaの`plug`を公開します。

## 各軸の編集と一括変更

SpinBoxからの編集は、その軸のscalar Commandで処理します。Xを編集しても、表示用に
丸められたY・Zの値を親属性へ書き戻すことはありません。他の軸のMaya実値を保持します。

`binding.set_value((x, y, z))`は全軸の編集可否、hard min/max、float32の格納範囲、
単位変換を先に検証します。成功時は親属性へ1回だけ`cmds.setAttr(..., type="double3")`
または`type="float3"`を実行し、書き込み後の実値を読み直します。
不正な成分があれば書き込み前に拒否し、一部だけを変更しません。
Mayaでは親属性へのsetAttrが子のhard limitを適用しないため、Store側で事前に確認します。

各軸の編集は1回のUndo、一括設定も3成分まとめて1回のUndoです。
通常の一括設定では、中間tupleを公開せず`binding.changed`へ確定後のtupleを1回通知します。
通知先がさらに編集した場合は、その結果も読み直して同期します。
同じ格納値への再設定では変更通知やUndoを増やしません。float属性はfloat32への丸め結果で
同値を判定します。連続stepを1回のUndoへまとめる機能は含めません。

一括変更は[AutodeskのsetAttr仕様](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html)
に従い、既存PlugOperatorのModifierManagerへ積む`set()`とは独立した即時編集として扱います。

## 単位・桁数・編集可否

| 属性 | 公開値・Command入力 | 各SpinBoxの表示・入力 |
| --- | --- | --- |
| `translate` | XYZともcm | Mayaの現在の距離単位 |
| `rotate` | XYZともdegree | Mayaの現在の角度単位 |
| `scale`、通常のdouble3／float3 | 単位なし | 単位なし |

単位変更は各軸のMaya Storeが既存の`linearUnitChanged`／`angularUnitChanged` callbackで
検知します。公開値を変えず、表示値・suffix・範囲を更新します。
桁数・刻み幅・精度保持・入力確定の規則はscalarの`FloatSpinBox`と共通です。

`decimals`と`single_step`は生成時に全3軸へ同じ値を指定します。
汎用Viewの既定は6桁で、Maya用サンプルはChannel BoxのChange Precisionを起動時に一度だけ
読み取ります。未編集のEnterやフォーカス移動ではMayaの精度を変更しません。

Yだけがlock・入力接続を持つ場合はYの入力だけを無効にし、X・Zは編集できます。
親属性のlock・接続では全軸を無効にします。値の表示同期は継続します。
一括Commandは全3軸が編集可能な場合だけ実行できます。アニメーション接続を編集して
キーを暗黙に追加・変更する機能はありません。

## Store・callback・寿命

Maya Storeは既存の`MayaFloatPlugStore`を3つ所有します。各軸の値変化、親属性の変更、
上流のdirty評価、Undo／Redo、lock・接続、単位変更への対応を共通化しています。
一括書き込み中の自身のcallbackを抑止し、完了後に全体と各軸を同期します。

Windowのclose、Bindingの`dispose()`、Qt ownerの破棄でcallbackを解放します。
構築途中の失敗でも生成済みのcallbackを残しません。
対象node・属性の削除でも同期を終了し、削除をUndoしても自動再接続しません。
再度編集する場合は新しいBindingを作ります。

Viewは共有Bindingの所有権を移さず、渡されたBindingのPython参照を保持します。
個々のViewだけを破棄してもBindingは終了しません。複数Windowで共有する場合は、
Windowから独立したownerを指定し、そのownerが終了を管理します。

独自Storeは`Float3ValueStore`を実装できます。`components`は3つの`FloatValueStore`で、
全体と各軸は同じ正本を参照し、`write()`は書き込み後の実値を返します。
外部変更は`binding.refresh()`で読み直します。外部Storeの所有権はBindingへ移しません。
3成分のPython属性用Storeの便利APIや、Python正本をMaya Viewへ同期する構成は後続対応です。
単一値は[Python属性の浮動小数点binding](python_float_binding.md)を使用できます。

## サンプルと対応範囲

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
window.widget.translate_binding.set_value((100.0, 200.0, 300.0))
window.widget.rotate_binding.set_value((45.0, 90.0, 450.0))
window.widget.scale_binding.set_value((1.0, 2.0, -1.0))
maya_plug.dispose()
```

Translate・Rotate・Scaleの3行に、各XYZのSpinBoxを表示します。
刻み幅は順に0.1、1.0、0.01で、各表示単位を使います。
対象3属性を検証してから既存Windowを置き換えるため、無効なnode名で現在のWindowを閉じません。

対応対象はnumeric attributeの`double3`／`float3`です。3つの子はすべて浮動小数点scalarで、
単位種別が揃っている必要があります。transformの距離3成分・角度3成分にも対応します。
配列、配列要素、配列配下、任意のcompound、整数3成分、異なる単位種別の混在は拒否します。
`resolve_float3_plug()`は属性名を受け取り、属性パス・配列記法を拒否します。

## 検証

- `tests/ui/test_float3_binding.py`: 独自Store、共有View、精度保持、再入、失敗復旧、サンプルと寿命。
- `tests/maya/ui/test_float3_plug_binding.py`: 単位、各軸・一括変更、Undo／Redo、lock・接続、float32、callback。
- `tests/typecheck/float3_binding_contract.py`: 公開API、各軸、具体PlugOperator、サンプルの型・ドット補完。

最終確認は`scripts/verify.cmd`を使用します。
[UI README](README.md#maya-2025--2026--2027-ui互換性確認)に3 versionの確認結果を記載します。
Maya本体では、Channel Boxとの双方向同期、単位変更、Undo／Redo、部分lock、closeと再表示を確認します。
