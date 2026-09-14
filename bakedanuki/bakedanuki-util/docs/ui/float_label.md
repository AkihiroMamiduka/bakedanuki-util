# 浮動小数点値を表示・コピーするFloatLabel

`FloatLabel`は、既存の`FloatBinding`または`FloatViewModel`を共有する読み取り専用の
`QLabel`です。正本への変更Commandを呼ばず、確定値と表示単位だけを受け取ります。
Maya正本・Python正本・Python正本とMaya同期のいずれでも同じViewを使えます。

## 最小の組み込み

```python
from bd_util.ui import FloatBinding, FloatLabel, FloatSpinBox, qt


class WeightWidget(qt.QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.binding = FloatBinding.from_attribute(data, "weight", parent=self)
        self.spin_box = FloatSpinBox(self.binding, self, decimals=3)
        self.value_label = FloatLabel(self.binding, self, decimals=6)
        layout = qt.QHBoxLayout(self)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.value_label)
```

Maya属性が正本なら`MayaFloatPlugBinding`、Python正本とMaya同期なら`MayaFloatBinding`を
同じ引数へ渡します。3成分Bindingの1軸は`FloatLabel(binding.view_model.x)`で表示できます。
XYZ全体をまとめる専用ラベルは、この段階では追加していません。

## 公開API

| API | 内容 |
| --- | --- |
| `FloatLabel(view_model, parent=None, *, decimals=6)` | BindingまたはViewModelを共有する表示Viewを生成する |
| `label.view_model` | 生存中のViewModelを返す。明示終了・Qt破棄後は例外を送出する |
| `label.decimals()` / `setDecimals(n)` | 表示小数桁数を取得・変更する。0～323を受け付ける |
| `label.text()` | 現在の表示単位で整形した数値とsuffixを返す |
| `label.setLocale(locale)` | Qt標準のlocaleを指定し、小数点などの表記を更新する |
| `label.setSelection(start, length)` / `selectedText()` | Qt標準の文字列選択と取得を行う |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.float`からimportできます。
元の公開値は`label.view_model.value.value`または`binding.value`から取得します。

## 表示と精度

`FloatPresentation.to_display()`で公開値を表示単位へ変換し、固定小数桁数で表示します。
QDoubleSpinBoxと同様に桁区切りを省略し、表示上の負のゼロは通常のゼロ表記にします。
小数点はWidgetのlocaleに従い、suffixはそのまま末尾へ付加します。

表示の丸め・桁数変更・locale変更・単位変更は、正本への書き込みやUndoを発生させません。
`minimum`／`maximum`で表示値をclampせず、正本が範囲外でも確定値をそのまま表示します。
表示単位への変換結果が有限数にならない場合は`—`とsuffixを表示し、正本は維持します。
表示可能な倍率へ戻れば、その後の表示情報更新で再表示します。

Mayaの距離・角度単位に対する追従は、既存のMaya Store／Viewが持つcallbackを使用します。
ラベル自身はMayaをimportせず、Maya callbackを追加しません。
小数桁数はViewの設定です。MayaのChannel Box設定を使う場合は、生成時に
`get_channel_box_precision()`の結果を渡します。

## コピーと読み取り専用の扱い

マウスまたはキーボードで表示文字列を選択し、Ctrl+CやQt標準のコンテキストメニューから
コピーできます。コピー対象は現在の表示文字列で、選択範囲に含まれる単位もコピーします。
全精度のPython値を取得する場合は`binding.value`を使用します。

テキストはPlainTextで扱い、suffixに`<`などが含まれていても装飾として解釈しません。
表示文字列が同じ場合は再設定せず、未変更のテキストの選択状態を維持します。

Mayaのlock・入力接続やPythonの読み取り専用属性によってCommandが無効でも、ラベルは
値の表示とコピーを継続します。接続の評価値も既存のStoreから同期されます。
Python正本とMayaが未同期の場合、ラベルはPythonの確定値を表示します。
Storeが利用不能になって値更新が止まった場合は、最後に同期した値を保持します。

## 共有と寿命

同じBindingをSpinBox・複数のラベルで共有できます。ラベルの破棄でBindingを終了せず、
BindingとViewModelは参照保持します。Python属性への直接代入後は既存仕様どおり
`binding.refresh()`が必要です。

ViewModelに`disposed` signalを追加し、編集可否とは別に明示終了を通知します。
`FloatViewModel.dispose()`の最初の呼び出しで1回だけ発火し、ラベルは直ちに無効化します。
Qt ownerによるQObject破棄は、既存のqueued接続で破棄完了後に扱います。
いずれも終了時のテキストを残し、その後の桁数・locale変更で終了前のデータを再描画しません。

`MayaFloatBinding.dispose()`はMaya Viewの表示変換を先に解除します。この場合、ラベルは
Python側の単位へ戻った後の表示を残して終了します。

## サンプルと検証

既存の単一値サンプルへ共有ラベルを追加しています。

```python
from bd_util._sample.maya.ui.float_sample import maya_plug

window = maya_plug.show("pCube1")
```

Maya正本のtranslateX・rotateX・scaleXを、SpinBoxとラベルで並べて表示します。
既存nodeの値から開始し、小数桁数は起動時のChannel Box設定に従います。

Pythonだけの場合は`minimal.show()`、Python正本とMaya同期は`maya_view.show("pCube1")`です。
後者は既存仕様どおりPython初期値をMayaへ適用します。

1. SpinBoxとChannel Boxで編集し、ラベルの値と単位が揃うことを確認する。
2. ラベルの文字列を選択してCtrl+Cでコピーする。
3. Preferencesの距離・角度単位を変更し、正本の公開値を維持して表示が変わることを確認する。
4. Maya正本の属性をlock・接続し、SpinBoxが編集不可でもラベルを選択できることを確認する。
5. Python正本のサンプルで直接代入後にrefreshし、ラベルも更新されることを確認する。
6. Windowを閉じて再表示し、古いViewやcallbackが残らないことを確認する。

- `tests/ui/test_float_label.py`: 表示精度、locale、コピー、共有、読み取り専用、setter、寿命。
- `tests/ui/test_float_label_maya.py`: 単位、Undo/Redo、lock・接続、同期保留、3種類のサンプル。
- `tests/typecheck/float_label_contract.py`: 公開API、Bindingの互換性、各軸とサンプルの型補完。

最終検証は`scripts/verify.cmd`を使用し、結果を[UI README](README.md#maya-2025--2026--2027-ui互換性確認)へ記載します。
