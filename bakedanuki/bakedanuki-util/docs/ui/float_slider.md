# 浮動小数点値を連続編集するFloatSlider

`FloatSlider`は、`FloatBinding`または`FloatViewModel`を共有する`QSlider` Viewです。
ドラッグ中も正本とSpinBox・Labelへ即時反映し、Mayaへの一連の書き込みをUndo 1回にまとめます。
Maya正本・Python正本・Python正本とMaya同期に同じViewを使用します。

## 最小の組み込み

```python
from bd_util.ui import FloatBinding, FloatLabel, FloatSlider, FloatSpinBox, qt


class WeightWidget(qt.QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.binding = FloatBinding.from_attribute(data, "weight", parent=self)
        self.slider = FloatSlider(self.binding, self, minimum=0, maximum=1)
        self.spin_box = FloatSpinBox(self.binding, self, decimals=3)
        self.label = FloatLabel(self.binding, self, decimals=6)
        layout = qt.QHBoxLayout(self)
        layout.addWidget(self.slider)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.label)
```

Maya属性が正本なら`MayaFloatPlugBinding`、Python正本とMaya同期なら`MayaFloatBinding`を
同じ引数へ渡します。これらのBindingが既存のMaya callbackとUndo管理を担当します。
SliderからMayaはimportしません。

## 公開APIと操作範囲

| API | 内容 |
| --- | --- |
| `FloatSlider(source, parent=None, *, minimum, maximum, steps=1000, orientation=qt.Qt.Orientation.Horizontal)` | 有限範囲の編集Viewを生成する |
| `slider.view_model` | 生存中のViewModelを返す。終了後は例外を送出する |
| `slider.floatRange()` | 指定した公開単位の操作範囲を返す |
| `slider.setFloatRange(minimum, maximum)` | 値を書き換えずに操作範囲を変更する |
| `slider.effectiveFloatRange()` | hard limitとの共通範囲。操作できる幅がなければ`None` |
| `slider.value()` / `setValue(position)` | Qt標準の**整数位置**を取得・設定する |
| `binding.value` / `binding.set_value(value)` | 正本の浮動小数点値を取得・変更する |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float`からimportできます。

`minimum`と`maximum`は公開値の単位で指定し、`minimum < maximum`が必要です。
Mayaの距離はcm、角度はdegree、数値型は単位なしです。表示単位をmやradへ変更しても
操作対象の物理的な範囲は変わりません。値と単位の表示には共有するSpinBox・Labelを使います。

操作範囲と正本のhard min/maxの共通範囲を`0～steps`へ等分して対応付けます。
`steps`は1～2147483647の整数です。範囲・位置への丸めは表示だけに適用し、外部から受け取った
正本の値が範囲外でも書き戻しません。ユーザーが位置を動かした時だけ正本へ入力します。
setterが入力を補正・拒否した場合も、表示は正本の確定値へ戻します。

Qtの`setRange()`・`setMinimum()`・`setMaximum()`は内部の整数範囲用です。FloatSliderでは
`0～steps`を維持し、浮動小数点の操作範囲変更には`setFloatRange()`を使ってください。
Qtの`singleStep`は1位置、`pageStep`は分割数の約1/10です。これらのQt APIは整数位置単位で使えます。
今回のViewは線形スライダーです。soft limitの自動取得、対数目盛り、自動範囲拡張は追加していません。

## 連続編集とUndo

| 入力 | 1操作の単位 |
| --- | --- |
| つまみのドラッグ | マウス押下から解放まで |
| 溝のクリック・押し続け | マウス押下から解放まで。Qtのリピートを含む |
| 矢印・PageUp/Down・Home/End | キー押下から実際の解放まで。キーリピートを含む |
| ホイール | フォーカス中の1イベントごと |
| Pythonからの`setValue()` / `binding.set_value()` | 通常は1呼び出しごと |

`tracking=True`でドラッグ中も値を確定します。標準の入力タイミングは
[Qt QAbstractSlider](https://doc.qt.io/qt-6/qabstractslider.html#tracking-prop)に従います。
`setTracking(False)`による解放時だけの更新は、このViewの運用対象に含めません。

Maya adapterは、最初にMayaの実値を変更する時点で
[undoInfoのchunk](https://help.autodesk.com/cloudhelp/ENU/MayaCRE-Tech-Docs/CommandsPython/undoInfo.html)を
開始し、操作終了時に閉じます。つまみを押して離しただけの場合や、float32の格納結果が同じ場合は
新しい履歴を追加しません。MayaでUndoが無効なら、その設定を維持します。

MayaのUndo chunkはグローバルです。操作中に別の処理が発行したUndo可能なcommandも同じまとまりへ
含まれます。独自Viewで連続編集APIを使う場合は、ユーザー操作の境界に合わせて確実に終了してください。
別Bindingのスライダーが編集を開始して書き込む場合は、先行するスライダーの操作を確定終了します。
同一ViewModelを複数ownerで同時に編集しようとする要求は拒否します。

Pythonだけを正本とする構成にPython用Undo履歴は追加しません。Python正本とMaya同期の構成では、
MayaのUndo/Redoによる復元値を既存のMaya ViewがPythonへ反映します。Mayaがlockなどで同期保留中なら、
Pythonの編集は継続しますが、Mayaへ書き込まれなかった変更はMayaのUndo対象になりません。

## 中断と寿命

Esc、フォーカス喪失、Window非アクティブ化、非表示、無効化、操作範囲や表示単位の変更では、
最後に確定した値を維持して連続編集を終了します。Escは開始値へのロールバックではありません。
ViewModelの明示終了、View・ownerの破棄、Maya node削除、callback解除、書き込み失敗でもchunkを閉じます。
書き込み途中の通知で終了要求が届いた場合は、Maya commandが戻ってから閉じます。

Sliderを破棄しても共有Bindingは終了しません。Binding・ViewModelはSliderが参照保持します。
Python属性への直接代入後は、既存仕様どおり`binding.refresh()`で同期します。

独自の編集View向けに、FloatViewModelへ次のAPIを追加しています。

| API | 内容 |
| --- | --- |
| `view_model.begin_edit(owner)` | ownerの連続編集を開始する。入力不可・終了済みなら`False` |
| `view_model.end_edit(owner=None)` | 連続編集を確定終了する。owner指定時はそのownerの操作だけを終了する |
| `view_model.is_editing` | 連続編集中か返す |
| `view_model.edit_started` / `edit_finished` | 開始・終了時の引数なしsignal |

ownerは生存中のQObjectです。owner破棄時にも終了します。明示的に利用する場合は、
`begin_edit()`の後の処理を`try/finally`で囲み、`finally`で`end_edit(owner)`を呼びます。
従来のSpinBoxはこの連続編集APIを自動では使用せず、従来どおり各変更を確定します。

## サンプルと確認

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

window = maya_plug.show("pCube1")
```

既存のtransformのtranslateX・rotateX・scaleXについて、Slider・SpinBox・Labelを並べて表示します。
各スライダーの操作範囲は順に-100～100 cm、-180～180 degree、0～3です。
これらはサンプルの操作範囲で、正本やSpinBoxの入力範囲を制限しません。

Pythonだけのサンプルは`minimal.show()`、Python正本とMaya同期は`maya_view.show("pCube1")`です。
後者は従来どおりPython初期値をMayaへ適用します。

1. スライダーをドラッグし、途中でもSpinBox・Label・Mayaが更新されることを確認する。
2. マウスを離してUndoし、ドラッグ開始前へ戻ること、Redoで終了値へ戻ることを確認する。
3. Channel BoxやSpinBoxから操作範囲外の値を入力し、値を維持してつまみだけが端に寄ることを確認する。
4. Mayaの単位を変更し、同じ物理量の範囲を操作できることを確認する。
5. lock・接続時の操作不可と、Windowを閉じて再表示した後の同期を確認する。

`tests/ui/test_float_slider.py`は写像・共有・入力・寿命、`test_float_slider_maya.py`はMaya同期・Undo・
中断・サンプル、`tests/typecheck/float_slider_contract.py`は公開APIの型補完を検証します。
最終検証は`scripts/verify.cmd`を使い、結果は[UI README](README.md#maya-2025--2026--2027-ui互換性確認)へ記載します。
