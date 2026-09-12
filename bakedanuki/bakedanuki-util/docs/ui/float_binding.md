# 浮動小数点binding

Maya属性を正本として、単一の浮動小数点値をQtの`QDoubleSpinBox`で編集します。
役割分担は[既存のMVVM](mvvm_roles.md)と同じで、Storeが実値を読み書きし、
ViewModelが確定値とCommandの実行可否を公開し、Viewが入力と表示を担当します。
Python objectを正本にする場合は[Python属性の浮動小数点binding](python_float_binding.md)を使用します。

## 最小の組み込み

```python
import bd_util as bdu
from bd_util.maya.ui import MayaFloatPlugBinding
from bd_util.ui import FloatSpinBox, qt


class TranslateXWidget(qt.QWidget):
    def __init__(self, node_name: str, parent: qt.QWidget | None = None) -> None:
        super().__init__(parent)
        nodes = bdu.Nodes()
        node = nodes.existing.transform(node_name)
        self.binding = MayaFloatPlugBinding(node.translate.translateX, parent=self)
        self.spin_box = FloatSpinBox(self.binding, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.spin_box)
```

Viewは`FloatBinding[FloatValueStore]`または`FloatViewModel`を受け取ります。
同じBindingを複数Viewに渡せます。Viewは共有Bindingの所有権を移動せず、
一時生成したBindingを受け取った場合はPython参照を保持します。

名前から取得する場合は次の入口を使用します。長い名前と短い名前に対応します。

```python
from bd_util.maya.ui import MayaFloatPlugBinding, resolve_float_plug

binding = MayaFloatPlugBinding(resolve_float_plug("pCube1", "tx"))
binding.set_value(100.0)  # cm。Mayaの表示単位には依存しない。
print(binding.value)
binding.dispose()
```

通常は最初の例のように`parent`を指定します。親なしBindingのcallbackはPythonのGCに
任せず、明示的に`dispose()`してください。node削除・対象属性削除でも同期を終了します。
削除をUndoした場合や同名属性を再作成した場合は新しいBindingを作ります。

## 公開API

| 入口 | 内容 |
| --- | --- |
| `FloatValue.value` / `changed(float)` | 最後に同期した確定値と、実値が変わったときの通知 |
| `SetFloatCommand.execute(value)` | 公開単位で変更を要求し、実値が変わったかboolで返す |
| `FloatViewModel` | Value、Command、単一Store、表示情報を仲介する |
| `FloatViewModel.disposed` | 読み取り専用Viewにも、編集可否と区別して明示終了を1回通知する |
| `FloatValueStore` | `read()`、`write()`、`is_available`、`is_writable`、`presentation`の契約 |
| `FloatBinding(store, parent=...)` | 外部Storeと専用ViewModelを組み立てる。外部Storeは所有しない |
| `FloatBinding.from_attribute(instance, attribute_name, ...)` | Python属性用StoreとBindingを生成する |
| `PythonFloatAttributeStore` | Python属性の有限値・入力範囲を検証し、setter適用後の実値を返す |
| `MayaFloatPlugBinding(plug, parent=...)` | `MayaFloatPlugStore`と専用ViewModel、callbackを所有する |
| `binding.value` / `changed` / `set_value()` / `refresh()` | bool Bindingと同じ利用窓口 |
| `FloatPresentation` | immutableな表示倍率・suffix・公開単位でのhard limit |
| `FloatSpinBox(source, parent=None, decimals=6, single_step=0.1)` | 共通のQDoubleSpinBox View |
| `FloatLabel(source, parent=None, decimals=6)` | 値と単位を表示し、選択・コピーできるQLabel View |
| `FloatSlider(source, parent=None, minimum=..., maximum=..., steps=1000)` | 公開単位の有限範囲を連続編集するQSlider View |
| `get_channel_box_precision()` | MayaのChange Precision設定を取得し、intで返す |

汎用APIは`bd_util.ui`、Maya APIは`bd_util.maya.ui`からimportします。
Storeの`write()`は成功可否ではなく、書き込み後のfloat実値を返します。
SpinBoxとラベルは同じBindingを共有できます。ラベルの仕様は[FloatLabel](float_label.md)を参照してください。
公開数値APIは有限のfloatとintを受け取り、floatへ正規化します。
bool、文字列、NaN、無限大は拒否します。`Float`という名前はPythonの数値型を表し、
Mayaの32bit floatだけを意味するものではありません。

## 単位の契約

| 属性 | Maya内部 | 公開値・Command入力 | SpinBoxの表示・入力 |
| --- | --- | --- | --- |
| `translateX` / doubleLinear | cm | cm | 現在の距離単位 |
| `rotateX` / doubleAngle | radian | degree | 現在の角度単位 |
| `scaleX` / double、float | 単位なし | 単位なし | 単位なし |

Maya Storeは`MDistance`／`MAngle`で読み取り、公開単位の値を返します。
書き込み時は現在単位へ変換して`cmds.setAttr()`を実行し、実値を読み直します。
既存PlugOperatorの`set()`はModifierManagerへ積むAPIなので、ここでの即時編集には使いません。

ViewModelの`presentation: FloatPresentation`は以下を持ちます。

- `scale`: 公開値に掛ける表示倍率。正の有限値。
- `suffix`: 数値に添える単位表記。
- `minimum` / `maximum`: 公開単位でのhard limit。`None`はその側の制限なし。
- `to_display(value)` / `from_display(value)`: 相互変換。

`linearUnitChanged`／`angularUnitChanged`はMaya adapterが監視します。
単位変更では`presentation_changed`を通知し、値・suffix・範囲を再表示します。
正本の数値は変更せず、`binding.changed`も値が変わらなければ通知しません。
変更時の未確定テキストは破棄し、確定済みの値を新しい単位で表示します。

## 入力、精度、範囲

`decimals`は各Viewの表示・入力の小数桁数です。既定は6桁、指定範囲は0〜323です。
QDoubleSpinBox自身の保持値も丸められますが、ViewModelやMayaの実値は表示更新で丸めません。
表示更新は`QSignalBlocker`で入力経路から分離し、未編集のEnterやフォーカス移動では
正本へ書き戻しません。ユーザーが編集・stepした場合は、その入力値を正本へ適用します。
小さい値や大きい値の表示精度、指数表記の編集にはQt標準Widgetの制約があります。

MayaのChannel Boxの「Edit > Settings > Change Precision」に合わせる場合は、
Widget生成時に`get_channel_box_precision()`を呼び、`decimals`へ渡します。

```python
from bd_util.maya.ui import get_channel_box_precision
from bd_util.ui import FloatSpinBox

spin_box = FloatSpinBox(binding, decimals=get_channel_box_precision())
```

この関数はMaya標準の`channelsPrecision` optionVarを読み取ります。設定値は1〜15桁、
未設定・不正な値の場合はMaya標準の3桁を返し、optionVarを書き換えません。
Channel Box自体が未生成でも取得できます。スクリプトでChannel Boxの`precision`だけを
直接変更した場合は、optionVarの設定とは一致しないことがあります。
設定の取得は呼び出し時だけで、callbackによる追従は行いません。
汎用の`FloatSpinBox`を桁数指定なしで生成した場合は、従来どおり6桁です。
`decimals`は表示と入力の両方に適用され、15桁を指定してもMaya属性自体の精度は増えません。

`single_step`は表示単位での刻み幅です。Mayaの単位変更後も数値の刻み幅は維持します。
キーボード入力はEnter／フォーカス移動で確定し、矢印・ホイールはstepごとに反映します。
Mayaへの各書き込みは標準Undo／Redo対象です。SpinBoxの各変更は個別に確定します。
[FloatSlider](float_slider.md)はViewModelの連続編集APIを使い、ドラッグ中の書き込みをUndo 1回へまとめます。

Maya属性のhard min/maxを表示単位に変換して範囲へ反映します。soft limitは入力制限に
使いません。範囲なしの側はQt doubleの有限範囲を使用します。今回のtransformの3属性には
属性のhard min/maxはなく、負のscaleや360度を超えるrotationも入力できます。
transform固有のLimit Informationを属性のmin/maxとして自動解釈する機能は含めません。
表示範囲は正本の制約から再設定されるため、継承元の`setRange()`による変更は同期時に戻ります。

float属性は32bitへの変換結果を採用し、同じ格納値への再要求ではUndoを追加しません。
格納範囲を超える値や書き込み時に0へunderflowする非ゼロ値は、シーンへ書き込む前に拒否します。
比較に汎用の許容誤差を使って小さな実値の変更を隠すことはしません。

## Maya callbackと編集可否

対象plug自身とcompoundの祖先の通知を監視します。親への値設定・接続・lockを
子のUIへ反映し、上流評価でdirtyになったときは次のQt event loopで値を読み直します。
直接編集やUndo／RedoはMaya側の確定値を読む経路で処理し、書き戻しません。

対象または祖先がlock・入力接続を持つ場合は編集を無効化し、値の表示同期は続けます。
アニメーション接続も表示専用です。Mayaが一部のanimCurve接続を変更可能と判定しても、
このUIではキーの追加・変更を暗黙に行いません。

callback解放とQObject破棄通知の扱いはbool基盤と同じです。callbackは直ちに解放し、
共有親の破棄中に兄弟Viewを同期操作しません。構築途中の失敗でもcallbackを解放します。

## サンプルと対応範囲

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

window = maya_plug.show("pCube1")
window.widget.translate_x_binding.set_value(100.0)
maya_plug.dispose()
```

3行のSpinBoxを表示します。刻み幅はTranslate Xが0.1、Rotate Xが1.0、Scale Xが0.01で、
それぞれ表示単位で指定しています。対象を検証してから前のWindowを置き換えます。
nodeや属性を自動作成せず、close・disposeでもMayaデータは残します。
3つのViewの小数桁数はWindow生成時にChannel Boxの設定から一度だけ取得します。
Windowを開いている間にChange Precisionを変更しても桁数は変わらず、次の`show()`で反映します。
距離・角度の単位変更は、引き続きWindowを開いたまま追従します。

対応対象は既存scalarのfloat/double・距離・角度と、配列配下ではないcompoundのscalar子です。
`resolve_float_plug()`は属性名のみを受け取り、属性パス、配列、配列要素、配列配下の子、
compound全体、整数、bool、time、typed dataは拒否します。
`double3`／`float3`全体の編集は[3成分binding](float3_binding.md)を使用します。
Python属性は`FloatBinding.from_attribute()`で接続できます。
Python正本をMaya Viewへ同期する場合は[MayaFloatBinding](python_float_maya_binding.md)を使用します。
共通の`FloatValueStore`を実装した独自Storeは使用できます。

## 検証

- `tests/ui/test_float_binding.py`: 入力確定、精度保持、共有View、補正・拒否・失敗、寿命。
- `tests/ui/test_float_transform_sample.py`: 3属性サンプル、起動時の桁数設定・精度保持、単位変更、親操作、再表示・破棄。
- `tests/maya/ui/test_float_plug_binding.py`: 単位、Undo／Redo、親接続、評価、float精度、callback。
- `tests/typecheck/float_binding_contract.py`: 公開APIの型・ドット補完。

開発中はtargeted pytest、最終確認は`scripts/verify.cmd`を使います。
3 versionのQt/UI確認結果は[UI README](README.md#maya-2025--2026--2027-ui互換性確認)を参照してください。
Maya本体では、Channel Boxとの双方向同期、単位変更、Undo／Redo、Windowのcloseと再表示を確認します。
