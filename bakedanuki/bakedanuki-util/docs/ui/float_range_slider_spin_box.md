# 操作範囲を編集するFloatRangeSliderSpinBox

`FloatRangeSliderSpinBox`は、スライダーの左右に最小値／最大値、現在値の右側にstep入力欄を備えた単一値の複合Viewです。
`FloatSliderSpinBox`を継承し、現在値の同期・単位変換・連続編集・Undo・寿命の処理を共有します。
各入力欄は既定で数値のみを表示し、単位文字の表示を個別に指定できます。
最小値／最大値／stepの役割はツールチップとアクセシビリティ用の名前で補います。

```text
[最小値] ─── Slider ─── [最大値] [現在値] [step]
```

## 最小の組み込み

```python
from dataclasses import dataclass

from bd_util.ui import FloatBinding, FloatRangeSliderSpinBox, qt


@dataclass
class Data:
    value: float = 0.123456789


window = qt.QWidget()
data = Data()
binding = FloatBinding.from_attribute(data, "value", parent=window)
editor = FloatRangeSliderSpinBox(
    binding, window, minimum=-1, maximum=1, decimals=3,
    minimum_decimals=2, maximum_decimals=2, single_step=0.01
)
layout = qt.QVBoxLayout(window)
layout.addWidget(editor)
window.show()

# APIは公開単位で範囲を指定する。data.valueは変更しない。
editor.setFloatRange(-0.5, 0.5)
```

この例はQApplicationが存在するMaya上で実行します。
Maya正本なら`MayaFloatPlugBinding`、Python正本とMaya同期なら`MayaFloatBinding`を渡します。
`FloatViewModel`も直接渡せます。

## 公開API

| API | 内容 |
| --- | --- |
| `FloatRangeSliderSpinBox(source, parent=None, *, minimum, maximum, steps=1000, decimals=6, single_step=0.1)` | 範囲入力と現在値入力を備えたViewを生成する |
| `editor.view_model` | 値編集で共有するViewModel |
| `editor.slider` / `editor.spin_box` | `FloatSlider` / `FloatSpinBox` |
| `editor.minimum_spin_box` / `editor.maximum_spin_box` | 表示単位で範囲を入力する`QDoubleSpinBox` |
| `editor.step_spin_box` | 現在値の刻み幅を編集する`FloatStepSpinBox` |
| `editor.floatRange()` / `setFloatRange(minimum, maximum)` | 公開単位での操作範囲を取得・変更する |
| `editor.effectiveFloatRange()` | hard limitとの共通範囲。操作幅がなければ`None` |
| `editor.decimals()` / `setDecimals(decimals)` | 現在値だけの表示・入力桁数を取得・変更する |
| `editor.minimumDecimals()` / `setMinimumDecimals(decimals)` | Minだけの表示・入力桁数を取得・変更する |
| `editor.maximumDecimals()` / `setMaximumDecimals(decimals)` | Maxだけの表示・入力桁数を取得・変更する |
| `editor.singleStep()` / `setSingleStep(single_step)` | 現在値だけの刻み幅を取得・変更し、step欄にも反映する |
| `editor.spin_box.isInputEnabled()` / `setInputEnabled(enabled)` | 現在値欄の操作設定を取得・変更する。Mayaの編集制限は維持する |
| `editor.spin_box.isUnitVisible()` / `setUnitVisible(visible)` | 現在値欄の単位文字の表示設定を取得・変更する。値の単位変換は維持する |
| `editor.range_status_label` | 入力拒否や実際の操作範囲を表示する`QLabel` |
| `editor.rangeEditRejected(str)` | 不正な範囲入力を復元した後、理由を通知するsignal |
| `editor.slider.floatRangeChanged(float, float)` | 設定した公開単位範囲が変更された後のsignal |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float`、`bd_util.ui.binding.float.view`からimportできます。

## 幅・操作可否・表示設定

コンストラクタでは、次のkeyword引数も指定できます。

| 引数 | 型 | 既定値 | 内容 |
| --- | --- | --- | --- |
| `slider_width` | `int \| None` | `None` | スライダーの幅 |
| `minimum_width` | `int \| None` | `None` | 最小値欄の幅 |
| `maximum_width` | `int \| None` | `None` | 最大値欄の幅 |
| `value_width` | `int \| None` | `None` | 現在値欄の幅 |
| `step_width` | `int \| None` | `None` | step欄の幅 |
| `minimum_enabled` | `bool` | `True` | 最小値欄からの範囲変更を許可する |
| `maximum_enabled` | `bool` | `True` | 最大値欄からの範囲変更を許可する |
| `value_enabled` | `bool` | `True` | 現在値欄からの値変更を許可する |
| `step_enabled` | `bool` | `True` | step欄からの刻み幅変更を許可する |
| `minimum_show_buttons` | `bool` | `True` | Minの増減ボタンを表示する |
| `maximum_show_buttons` | `bool` | `True` | Maxの増減ボタンを表示する |
| `value_show_buttons` | `bool` | `True` | 現在値の増減ボタンを表示する |
| `step_show_buttons` | `bool` | `True` | stepの増減ボタンを表示する |
| `minimum_decimals` | `int` | `0` | Minの表示・入力の小数桁数 |
| `maximum_decimals` | `int` | `0` | Maxの表示・入力の小数桁数 |
| `minimum_show_unit` | `bool` | `False` | Min欄にcm・degなどの単位文字を表示する |
| `maximum_show_unit` | `bool` | `False` | Max欄にcm・degなどの単位文字を表示する |
| `value_show_unit` | `bool` | `False` | 現在値欄にcm・degなどの単位文字を表示する |
| `step_show_unit` | `bool` | `False` | step欄にcm・degなどの単位文字を表示する |
| `step_mode` | `FloatStepMode` | `"additive"` | step欄の増減方式。`"additive"`または`"multiplicative"` |
| `step_increment` | `float` | `1.0` | 加算モードでstep欄を増減する量 |

共通の`show_buttons`引数は廃止し、欄ごとの個別引数へ置き換えています。
既存の`decimals`引数と`setDecimals()`は現在値専用です。Min／Maxの桁数には影響しません。

幅に正の整数を指定すると、そのWidgetをQtの論理ピクセル単位で固定します。
Qtの上限に合わせて1～16777215を受け付け、`0`・負数・`bool`・小数などは拒否します。
`None`のWidgetは同じストレッチ比率で横方向へ伸縮します。各Widgetの最小必要幅を満たしたうえで
領域を配分するため、自然な初期サイズで5つの幅が常に同じになるとは限りません。
全て固定幅の場合は左詰めに配置し、余白を行末へ残します。

固定幅は範囲・単位・小数桁数の変更後も維持します。長い数値や単位が指定幅に収まらない場合は
一部が隠れますが、保持する値と範囲の精度は変わりません。

`minimum_enabled=False`／`maximum_enabled=False`にした欄は無効表示となり、単位・桁数・範囲を
更新しても無効設定を維持します。現在値の編集には影響せず、`setFloatRange()`による範囲変更も可能です。
無効にした欄への`setValue()`は範囲変更として受け付けず、確定済みの範囲へ表示を戻します。
Binding終了や表示変換のoverflowによる無効化は、`True`の設定より優先します。

`value_enabled=False`では現在値欄を無効表示にします。スライダーと他Viewからの編集、
MayaやPython正本からの表示更新は継続します。lock解除・接続解除でも無効設定を維持し、
`True`でもMaya側のlock・接続・正本の終了による編集制限を解除しません。
無効にした現在値欄への`setValue()`は正本へ書き戻さず、確定値の表示へ戻します。

各`*_show_buttons=False`は、対象のSpinBoxへQtの`NoButtons`を設定します。
有効な入力欄では文字の直接入力や上下キーによる増減を引き続き使用できます。
幅・操作可否・ボタン表示・桁数の設定自体では、現在値やMayaのUndoを変更しません。

`minimum_show_unit`・`maximum_show_unit`・`value_show_unit`・`step_show_unit`は、各欄の末尾の単位文字を個別に設定します。
全て既定値は`False`で、`True`にした欄だけ単位文字を表示します。
非表示でもMayaの現在の表示単位への追従、入力時の単位変換、hard limitの換算は維持します。
例えば100cmは表示単位がmなら`1.000000`となり、そこで`2`を入力すると正本へ200cmを設定します。
Min／Max欄も現在の表示単位で範囲を編集し、例えばm表示でMaxに`2`を入力すれば操作範囲の上限を200cmにします。
範囲の編集では正本の値を変更しません。単位・桁数・値・範囲の更新後も表示設定を維持し、
共有ラベル・他Viewの単位表示や、有効範囲の案内に付ける単位文字は変更しません。
`double`など単位のない属性は、`True`でも単位文字を追加しません。

生成後は`editor.spin_box.setUnitVisible(True)`で単位文字を表示できます。
切替時は未確定入力を破棄して確定値を再表示し、正本やUndoを変更しません。
この複合Viewに含まれない通常の`FloatSpinBox`は、従来どおり単位文字を表示します。

```python
# 数値欄を固定幅にし、スライダーが残りの幅を使う構成。
editor = FloatRangeSliderSpinBox(
    binding,
    minimum=-100,
    maximum=100,
    slider_width=None,
    minimum_width=80,
    maximum_width=80,
    value_width=100,
    step_width=80,
    minimum_enabled=False,
    maximum_enabled=False,
    value_enabled=False,
    minimum_show_buttons=False,
    maximum_show_buttons=False,
    value_show_buttons=True,
    minimum_decimals=0,
    maximum_decimals=2,
    minimum_show_unit=False,
    maximum_show_unit=True,
    value_show_unit=False,
)
```

## 範囲・単位・精度

- 範囲は各Viewの`FloatSlider`が保持します。同じBindingを使っても別Viewの範囲には伝播しません。
- Min／Max欄は**現在の表示単位**で入力します。Mayaの単位を変更すると入力欄も追従し、物理的な範囲を維持します。
- コンストラクタと`setFloatRange()`は**公開単位**です。Mayaの距離はcm、角度はdegree、数値型は単位なしです。
- `steps`はスライダーの分割数です。範囲を狭くすると同じ分割数で細かく操作できます。
- 桁数は`setDecimals()`・`setMinimumDecimals()`・`setMaximumDecimals()`で個別に変更してください。
- 表示の丸めや単位変更で現在値・操作範囲を変更しません。片側を編集しても、反対側の未丸めの範囲を維持します。
- `editor.slider.setFloatRange()`からの変更もMin／Max欄へ反映します。

桁数は0～323の整数で指定します。Min／Maxの既定は0桁なので、表示単位で整数を入力します。
例えば実際の範囲が`-0.1～0.1`なら両端が0と表示される場合もありますが、保持する範囲は変わりません。
小さい範囲やm・radで細かく編集する場合は、必要なMin／Maxの桁数を指定してください。
桁数を減らしてから増やした場合も、保持している実値から再表示します。

`single_step`は現在値とstep欄の初期刻み幅を指定します。
Min／Maxの刻み幅は各欄の桁数が0なら表示単位で常に1、それ以外なら
`max(生成時のsingle_step, 10 ** -decimals)`です。桁数の変更後も、0桁の上下操作が
小数の刻み幅によって動かなくなることを防ぎます。
`setSingleStep()`やstep欄からの変更は現在値だけへ反映し、その後のMin／Max桁数変更でも
Min／Maxの刻み幅に伝播しません。従来の`setSingleStep()`によるMin／Maxの同時変更は廃止しています。

Min／Maxの文字入力はEnterまたはフォーカス移動で確定します。矢印ボタン・上下キーなどによる
数値変更はその操作時に反映します。有限値かつ`Min < Max`を必要とし、不正な範囲は最後の有効な範囲へ
戻して理由を表示します。APIでの不正な指定は例外を送出します。片側ずつ確定するため、例えば
`0～1`から`10～20`へ変更するときはMaxを先に20へ変更します。APIでは両端を一括変更できます。

単位変更時は未確定テキストを破棄し、確定済みの範囲を新しい単位で表示します。
表示単位への変換でoverflowする極端な範囲は、元の範囲を保持して両端の入力を無効化します。
表示可能な範囲を`setFloatRange()`で設定するか単位を戻すと、入力が復帰します。

## 現在値の刻み幅をUIで変更する

step欄で設定した数値は、このViewの現在値欄に対する矢印ボタン・上下キー・ホイール操作の刻み幅になります。
スライダーの分割数`steps`、Min／Maxの刻み幅、他Viewの刻み幅は変更しません。
step欄の変更自体では正本への書き込みやMayaのUndo追加を行わず、進行中のスライダー編集も終了しません。
モードは生成時に選び、モード選択用のUIは追加していません。

```python
# 角度用。現在値を15刻みで操作し、step欄も15ずつ増減する。
angle_editor = FloatRangeSliderSpinBox(
    angle_binding, minimum=-180, maximum=180,
    single_step=15, step_mode="additive", step_increment=15,
    step_width=80,
)

# 桁変更用。step欄を上へ操作すると10倍、下へ操作すると1/10倍になる。
linear_editor = FloatRangeSliderSpinBox(
    linear_binding, minimum=-100, maximum=100,
    single_step=0.1, step_mode="multiplicative", step_width=80,
)
linear_editor.setSingleStep(15)  # step欄も15になり、次の上下操作は150／1.5になる。
```

`"additive"`は現在のstepへ`step_increment`を加減します。0以下になる減算は直前の正の値を維持します。
`"multiplicative"`は現在のstepを10倍／1/10倍にし、15→1.5→0.15のように仮数を維持します。
複数段の操作はその回数分を適用します。Qt標準のPageUp／PageDownやCtrl併用による10段操作では、
加算量が10倍、桁変更は10桁になります。通常の上下キー・1ノッチのホイールは1段です。
step欄のホイールはフォーカス中だけ受け付け、親のスクロール操作による誤変更を防ぎます。

文字入力はEnterまたはフォーカス移動で確定します。不正な文字・0・負数・非有限値は直前の確定値へ戻します。
正の有限値をQtが保持できる範囲（`1e-323`～`sys.float_info.max`）で扱い、桁変更の上下限はその端で停止します。
APIへの不正な値は例外で拒否します。端付近ではfloat自体の表現精度による丸めがあり得ます。
step欄は現在値の`decimals`から独立して精度を保持し、不要な末尾の0を省いて表示します。
例えば現在値の表示が0桁でも、stepの`0.001`を0へ丸めません。現在値の変化を小数まで見たい場合は
現在値側の`decimals`も増やしてください。

刻み幅の数値は**現在の表示単位**で解釈します。Mayaの単位変更時も数値を維持し、物理量としての換算はしません。
例えばstepが15のとき、deg→radへ変更すると15rad刻みになります。これは従来の`single_step`と同じ扱いです。
`step_show_unit=True`なら単位文字だけを新しい単位へ更新し、未確定の古い入力は破棄します。

`step_enabled=False`ではstep欄を無効にし、欄への`setValue()`も確定値へ戻します。
設定APIの`editor.setSingleStep()`は使用できます。Maya属性のlock・接続や`value_enabled=False`は
View設定であるstep欄を無効にしません。正本の終了時はstep欄も無効化します。
Windowを作り直すと、生成時の刻み幅へ戻ります。

`FloatStepSpinBox(parent=None, *, value=0.1, step_mode="additive", step_increment=1.0)`は単独でも使用できます。
`stepMode()`でモード、`value()`で編集中の刻み幅、`singleStep()`で加算量を取得し、`valueChanged(float)`で確定を通知します。
複合Viewの刻み幅をコードから変更するときは、現在値欄との同期を行う`editor.setSingleStep()`を使用してください。

## 属性の制限とUndo

設定範囲はMaya属性のhard min/maxを変更しません。実際のスライダー操作には、設定範囲と
hard limitの共通範囲を使用します。両者が異なる場合は入力行の下に`Usable range`を表示します。
操作できる幅がない場合はSliderだけを無効化し、有効なMin／Max欄または`setFloatRange()`で範囲を変更して復帰できます。

現在値が設定範囲外でも正本を変更せず、つまみだけを端へ寄せます。現在値のSpinBoxは属性のhard limit内で
独立して入力できます。Min／Maxの変更はMayaへの書き込みを伴わず、MayaのUndoへ追加しません。
自身のSliderでドラッグ中に範囲を変更すると、そのドラッグを確定終了してから新しい範囲へ切り替えます。
他のViewが開始したドラッグには干渉しません。

属性がlock・接続中・読み取り専用でも、`minimum_enabled`／`maximum_enabled`が`True`の範囲入力は編集できます。
Bindingの明示終了・ViewModelのQt破棄時には、範囲・step入力も無効化します。
Viewの破棄で共有Bindingは終了しません。Maya callbackもこのViewには追加しません。
範囲のファイル保存・復元は行わず、Windowを作り直すと生成時の範囲へ戻ります。

## サンプルと確認

既存の`maya_plug.py`・`maya_view.py`・`minimal.py`で、このViewを使用します。

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

window = maya_plug.show("pCube1")
editor = window.widget.translate_x_editor
editor.setFloatRange(-10, 10)  # cm
```

`translate_x_editor`・`rotate_x_editor`・`scale_x_editor`から各Viewを取得できます。
`maya_view`の`linked_translate_x_editor`、`minimal`の`editor`／`linked_editor`では、同じ値に
異なる範囲を設定できます。Maya連携サンプルは現在値と数値ラベルにWindow生成時の
Channel Box桁数を使用し、Min／Maxは既定の0桁を使用します。

`maya_plug`では既存の40／40／130の固定幅・Min／Max入力無効・ボタンなし設定を使用します。
`enabled_value`変数で現在値の操作可否、`show_minimum_unit`・`show_maximum_unit`・`show_value_unit`で
各欄の単位文字の表示を指定できます。step欄は`width_step`（既定80）と`show_step_unit`で設定します。
全欄の単位文字は既定で非表示とし、共有ラベルでは単位を確認できます。
`maya_view`は80／80／100の固定幅・ボタンなしで、`linked_translate_x_editor`の数値欄は全て無効です。
共有ViewもSliderからは編集できます。
`minimal.editor`は80／80／100の固定幅・ボタンなしでMin／Maxが2桁、
`minimal.linked_editor`は全Widgetを伸縮させ、Minが1桁・Maxが3桁・現在値が6桁です。
共有Viewの数値欄はstep欄も含めて全て無効にし、Maxの増減ボタンだけを表示して設定の違いを比較できます。
Maya連携サンプルのtranslate／scaleと`minimal.editor`は桁変更モード、rotateは初期値15・増減量15の加算モードです。
操作できるstep欄には増減ボタンを表示します。
サンプルでは、伸縮するSliderに初期表示の操作用として最小幅160を設定しています。
コンストラクタで`slider_width`を指定した場合は、その固定幅を優先します。

1. Min／Maxを編集し、Maya属性と現在値が変わらず操作範囲だけが変わることを確認する。
2. 同値・逆転する入力を確定し、復元と理由表示を確認する。
3. Mayaの距離・角度単位を変更し、全入力欄の単位が揃い物理的な範囲が維持されることを確認する。
4. Sliderをドラッグし、他Viewへの即時反映とUndo／Redo各1回での復元を確認する。
5. `minimal`で属性の0～1制限を超える範囲を設定し、実際の操作範囲の表示を確認する。
6. Windowを閉じて再表示し、初期範囲への復帰とcallbackの解放を確認する。
7. Windowの幅を変え、固定幅の欄と未指定のWidgetの伸縮を確認する。
8. 数値欄を無効にした共有Viewで、単位変更やlock解除後も無効表示を維持し、Slider操作で表示が更新されることを確認する。
9. Min／Maxの桁数を別々に変更し、実際の範囲と現在値が保たれ、0桁の上下操作が1刻みになることを確認する。
10. 3つの`*_show_unit`を個別に指定し、Mayaの表示単位変更後も数値・範囲の換算と入力が正しく行われることを確認する。
11. step欄を変更してから現在値の上下操作を行い、指定した刻み幅でMayaと共有Viewが更新されることを確認する。
12. rotateのstep欄は15ずつ、translateのstep欄は15を入力すると150／1.5へ増減することを確認する。
13. step変更だけではUndoが増えず、値のUndo／Redo後もstepが維持されることを確認する。

`tests/ui/test_float_range_slider_spin_box.py`は範囲・入力・精度・寿命、
`tests/ui/test_float_step_spin_box.py`はstepの入力・増減・精度・View間の独立性、
`tests/ui/test_float_range_slider_spin_box_maya.py`はMayaとの単位同期・Undo・callback・サンプル、
`tests/typecheck/float_range_slider_spin_box_contract.py`は公開APIの型補完を検証します。
最終検証は`scripts/verify.cmd`を使用します。
