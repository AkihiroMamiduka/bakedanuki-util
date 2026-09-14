# XYZを編集するFloat3SliderSpinBox

`Float3SliderSpinBox`は、各軸の`FloatSliderSpinBox`を縦3行に並べる複合Viewです。
`Float3SpinBox`・`Float3Label`と同じBindingを共有し、ドラッグ中も正本と他のViewを更新します。
各成分の単位・精度・編集可否・Undoは既存のscalar基盤へ委譲し、View自体はMaya callbackを追加しません。

```text
X  ─────●─────  [ 1.235 cm ↕ ]
Y  ──────●────  [ 2.346 cm ↕ ]
Z  ───────●───  [ 3.457 cm ↕ ]
```

## 最小の組み込み

```python
import bd_util as bdu
from bd_util.maya.ui import MayaFloat3PlugBinding, get_channel_box_precision
from bd_util.ui import Float3Label, Float3SliderSpinBox, qt

window = qt.QWidget()
nodes = bdu.Nodes()
node = nodes.existing.transform("pCube1")
binding = MayaFloat3PlugBinding(node.translate, parent=window)
editor = Float3SliderSpinBox(
    binding, window,
    minimum=-100, maximum=100,
    steps=2000, decimals=get_channel_box_precision(), single_step=0.1,
)
label = Float3Label(binding, window, decimals=3)
layout = qt.QVBoxLayout(window)
layout.addWidget(editor)
layout.addWidget(label)
window.resize(520, window.sizeHint().height())
window.show()
```

この例はQApplicationが存在するMaya上で実行します。対象nodeをあらかじめ用意してください。
Python属性だけなら`Float3Binding.from_attribute()`、Python正本とMaya同期には
`MayaFloat3Binding.from_attribute()`を同じViewへ渡します。Store接続済みの`Float3ViewModel`も受け取ります。

## 生成時の設定

| 引数 | 既定値 | 内容 |
| --- | --- | --- |
| `view_model` | 必須 | `Float3Binding`または接続済みの`Float3ViewModel` |
| `parent` | `None` | Qtの親Widget |
| `minimum` / `maximum` | 必須 | 公開単位によるスライダーの操作範囲。共通の数値、またはXYZの3成分Sequence |
| `steps` | `1000` | 各軸のスライダーの分割数。正の整数 |
| `decimals` | `6` | 全軸のSpinBoxの表示桁数。0～323の整数 |
| `single_step` | `0.1` | 全軸のSpinBoxのボタン・ホイール操作の刻み幅。表示単位による正の数値 |

`parent`より後ろの引数はキーワード専用です。範囲の数値は有限のint／floatを受け取り、
bool・NaN・無限大や長さが3ではないSequenceを拒否します。
全軸で`minimum < maximum`が必要です。設定は全軸分を子Widgetの生成前に検証します。

```python
editor = Float3SliderSpinBox(
    binding, window,
    minimum=(-100, -50, -10),
    maximum=(100, 50, 10),
)
```

公開単位はtranslateならcm、rotateならdegree、scaleなら単位なしです。
Preferencesの表示単位をm・radへ変更しても、スライダーの物理的な操作範囲は維持します。
SpinBoxの値・単位文字・入力範囲は現在の表示単位へ追従します。
`steps`は分割数、`single_step`は数値入力の刻み幅で、それぞれ独立した設定です。

## 子Widgetへのアクセス

| API | 内容 |
| --- | --- |
| `editor.view_model` | 共有する`Float3ViewModel`。終了後は例外を送出する |
| `editor.x_editor` / `y_editor` / `z_editor` | 各軸の`FloatSliderSpinBox` |
| `editor.x_editor.slider` | Xの`FloatSlider` |
| `editor.x_editor.spin_box` | Xの`FloatSpinBox` |
| `editor.x_spin_box` / `y_spin_box` / `z_spin_box` | 各軸の数値入力への短いアクセス。同じ子Widgetを参照する |

軸ごとの設定を変える場合は、具体型が追える子Widgetの既存APIを使います。

```python
editor.y_editor.slider.setFloatRange(-20, 20)
editor.z_spin_box.setSingleStep(0.25)
editor.z_spin_box.setDecimals(3)
```

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float3`、`bd_util.ui.binding.float3.view`からimportできます。
外側余白は0で、横方向は配置先の幅へ伸びます。全体へフォーカスを移すとXの数値入力へ入り、
Tab順は各行のスライダー・数値入力から次の軸へ進みます。

## 同期・入力範囲・Undo

- スライダーの操作範囲は正本のhard limitとの共通範囲を使います。共通範囲がなければ、その軸のスライダーだけを無効にします。
- 数値入力は正本のhard limitを使います。スライダーの操作範囲外の値も入力でき、その場合はつまみを端に表示します。
- 表示やスライダーの分割数へ正本を丸め直しません。1軸の編集では、他2軸の未丸めの実値を保持します。
- Pythonのsetterが他の軸を補正した場合も、全軸を読み直して全Viewを更新します。直接代入後は`binding.refresh()`を呼びます。
- Maya連携時は1軸のドラッグをUndo 1回にまとめます。別の軸の編集開始で前の連続編集を終了し、軸ごとにUndoできます。
- 数値入力は従来どおり確定ごとにUndoします。SpinBoxの連続stepをまとめる機能は含みません。
- Mayaを接続しないPython属性BindingにはUndo履歴を追加しません。

スライダーのキー・ホイール・フォーカス移動時の挙動は[FloatSlider](float_slider.md)、
入力確定や精度保持は[FloatSliderSpinBox](float_slider_spin_box.md)と共通です。
Maya正本では軸単独のlock・接続はその軸を、親属性のlock・接続は全軸を無効にします。
Python正本とMaya同期では、Pythonの編集可否を優先し、Mayaへ書けない変更は既存仕様どおり同期保留になります。

### 軸編集時の再同期と処理時間

`Float3ViewModel`は、軸の値確定・Store再読込・書き込み完了から届く全体再同期を、
1回の軸Commandの完了時にまとめます。ドラッグの各位置変更で即時同期し、
同値入力時の他軸変更、setter補正、失敗時の実値復旧も確認します。
通知先から再編集された場合は、確定値が揃うまで必要な再同期を継続します。

2026-09-14にMaya 2025の`mayapy`で、Float3SliderSpinBoxを使っていた時点の`maya_plug`サンプルのtranslateXを計測した結果です。

| 位置変更1回あたり | 集約前 | 集約後 |
| --- | --- | --- |
| XYZ全体の再同期 | 3回 | 1回 |
| Maya実値の読込（全軸合計） | 41回 | 17回 |
| 単位・入力範囲の取得（全軸合計） | 10回 | 4回 |
| Mayaへの書き込み | 1回 | 1回 |
| 処理時間の中央値 | 約1.09 ms | 約0.92 ms |

処理時間は`QT_QPA_PLATFORM=offscreen`で表示したサンプルに対し、3桁表示・分割数2000で、
1回の連続編集につき400回の位置変更とQt event処理を3セット実行して計測しました。
回数は時間計測と分離したprofileで確認しています。描画環境や実行時の負荷で時間は変動し、
Maya本体のビューポートを含む体感速度はこの計測に含みません。
回帰テストでは処理時間の閾値ではなく、即時同期・全体通知の回数・Maya実値の読込回数を検証します。

## 寿命

ViewはBindingとViewModelを参照保持します。Viewだけを閉じる・隠す・無効にする・破棄する場合は、
そのViewが開始した連続編集を終了します。別の共有Viewが開始したドラッグは終了しません。
Bindingを終了する責務は既存のownerにあり、Viewだけを破棄しても共有BindingやMaya callbackは残ります。
Bindingの終了・ViewModelやcomponentのQt破棄時は、全軸の編集を停止します。
構築途中で失敗した場合も、自身と作成途中の子Widgetだけを片付け、共有Bindingを維持します。

## サンプルと検証

```python
from bd_util._sample.maya.ui.float3_sample import maya_plug

window = maya_plug.show("pCube1")
```

`maya_plug`はMaya正本、`maya_view`はPython正本とMaya同期、`minimal`はPython属性のみのサンプルです。
現在のサンプルの編集欄は、Min／Max・step編集を備える[Float3RangeSliderSpinBox](float3_range_slider_spin_box.md)です。
属性ごとのグループに縦3行の編集欄を配置し、その下に共有する`Float3Label`を表示します。

| サンプルの編集欄 | スライダーの範囲 | 分割数 |
| --- | --- | --- |
| `translate` | -100～100 cm | 2000 |
| `rotate` | -180～180 degree | 3600 |
| `scale` | 0～3 | 3000 |
| `maya_view`の`linked_translate` | -10～10 cm | 2000 |
| `minimal`の`spin_box` / `linked_spin_box` | -10～10 / -100～100 | 1000 |

表示桁数は起動時のChannel Box設定、共有translateは6桁、minimalは3桁と6桁です。
範囲はViewごとの操作設定で、同じ値を異なる範囲・表示桁数のViewで共有できます。

1. XYZそれぞれをドラッグし、Mayaと数値入力・ラベルが途中から同期することを確認する。
2. X、Yの順にドラッグし、Undoを2回実行して軸ごとに戻ることを確認する。
3. 単位を変更し、スライダーの範囲を保ったまま数値の表示・入力単位が変わることを確認する。
4. スライダーの範囲外の値を数値入力し、実値を保ってつまみが端に表示されることを確認する。
5. 軸のlock・接続、Windowのcloseと再表示、Pythonへの直接代入後のrefreshを確認する。

`tests/ui/test_float3_slider_spin_box.py`は精度・範囲・共有・補正・寿命、
`tests/ui/test_float3_slider_spin_box_maya.py`は単位・Undo・lock・接続・callback・サンプル、
`tests/typecheck/float3_slider_spin_box_contract.py`は公開APIの型補完を検証します。
最終検証は`scripts/verify.cmd`を使用し、[UI README](README.md)へ結果を記載します。

操作範囲をUI上から変更するMin／Max欄とstep編集欄は、`Float3RangeSliderSpinBox`が提供します。
