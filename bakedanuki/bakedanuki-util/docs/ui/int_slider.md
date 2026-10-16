# 整数Sliderと連続編集

`IntSlider`は`IntBinding`または`IntViewModel`を共有する整数用の`QSlider` Viewです。
Python正本、Maya正本、Python正本とMaya同期の三経路で使用できます。
ドラッグ中も正本・数値欄・ラベルへ即時反映し、Mayaへの変更を一操作一回のUndoにまとめます。

```python
from bd_util.ui import IntSlider

slider = IntSlider(binding, minimum=-100, maximum=100)
```

## 公開API

| API | 内容 |
| --- | --- |
| `IntSlider(source, parent=None, *, minimum, maximum, steps=1000, orientation=qt.Qt.Orientation.Horizontal)` | 指定範囲の整数Sliderを生成 |
| `slider.view_model` | 生存中の入力元。終了後は例外 |
| `slider.intRange()` / `setIntRange(minimum, maximum)` | View固有の操作範囲を取得・変更 |
| `slider.effectiveIntRange()` | 操作範囲と正本の制限の共通部分。操作不能なら`None` |
| `slider.intRangeChanged(int, int)` | 設定範囲の実変更時に通知 |
| `slider.value()` / `setValue(position)` | Qt内部の整数位置を取得・変更 |
| `slider.finish_edit()` | 最後の確定値で操作を終了し、残りの古い入力を停止 |
| `slider.editStarted` / `editFinished` | Viewの操作開始・終了通知 |
| `slider.setValueRequestHandler(handler)` | 公開整数を外側で処理したら`True`を返す入力先を指定 |

`bd_util.ui`、`bd_util.ui.binding`、`bd_util.ui.binding.int`、
`bd_util.ui.binding.int.view`からimportできます。
正本の値は`binding.value`／`binding.set_value(value)`で操作します。
Qtの`setRange()`・`setMinimum()`・`setMaximum()`は内部位置用です。
公開整数の範囲変更には`setIntRange()`を使用します。
独自handlerが`None`または`False`を返した場合はViewModelのCommandへ委譲します。
`True`を返して外側で処理する場合、連続Undoも外側が管理します。
`editStarted`／`editFinished`を`MayaEditSession`などの操作境界へ接続してください。

## 整数の精度と範囲

公開値と両端は`-2147483648～2147483647`の厳密な`int`です。
`bool`・小数・文字列・範囲外の整数を暗黙変換せず拒否します。
操作範囲は`minimum < maximum`、分割数は`1～2147483647`です。

実効範囲の整数幅を`span`とすると、Qt内部位置は`0～min(steps, span)`です。
`0～10`なら11個の整数全てを1刻みで操作でき、大きい範囲は最大`steps`分割です。
全32-bit範囲の幅4294967295もPython整数で計算し、変換にfloatを使用しません。
値・位置の丸めは最寄りの整数を選び、同点では大きい整数側へ丸めます。
数値欄ではSliderの分割にかかわらず各整数を正確に入力できます。

外部値が操作範囲外でも、実値と数値欄は維持し、つまみだけ端へ寄せます。
表示、生成、範囲変更、正本からの同期では値を書き戻しません。
setterが補正・拒否した場合も、正本の確定整数を再表示します。
実効範囲に操作できる幅がなければSliderだけを無効化し、数値欄は独立して使用できます。

操作範囲はViewごとに保持し、同じBindingの別Viewへ強制反映しません。
Mayaの型範囲・hard limitは変更しません。soft limitの自動取得は行いません。
既存のStep設定は数値欄の上下操作の刻み幅で、Sliderの分割数とは独立です。
Qtの`singleStep`・`pageStep`は内部位置単位で、それぞれ既定1・分割数の約1/10です。

## 連続編集・Undo・中断

`IntViewModel`に次のAPIを追加しています。

| API | 内容 |
| --- | --- |
| `begin_edit(owner)` | 生存中のQObjectが操作を所有。開始できれば`True` |
| `end_edit(owner=None)` | 指定owner、または現在の操作を確定終了 |
| `is_editing` | 連続操作が進行中か |
| `edit_started` / `edit_finished` | 開始・終了通知 |

同じViewModelを異なるownerが同時編集する要求は拒否します。
owner破棄・入力不可・Binding終了時も操作を終了します。

| 入力 | 一操作の単位 |
| --- | --- |
| つまみ・溝 | マウス押下から解放まで。溝のリピートを含む |
| 矢印・Page・Home・End | 実際のキー押下から解放まで。キーリピートを含む |
| ホイール | フォーカス中の一イベント |
| Pythonからの`setValue()` | 通常は一呼出し。`setSliderDown(True)`中なら同じ操作 |

ドラッグ中も値を更新する`tracking=True`を使用します。
Mayaの最初の実変更でUndoを開始し、操作終了時に閉じます。無変更では履歴を増やしません。
Undoが無効ならその設定を維持します。Pythonのみの正本に独自Undo履歴は作りません。
Python正本とMaya同期では、MayaのUndo／RedoをPython正本へ反映します。
Maya同期失敗ではPython値を維持し、既存の同期保留と再同期の規則に従います。

floatと整数は同じMaya連続Undo管理を使用します。別Bindingの操作・通常入力へ
切り替える際は先行操作を終了し、chunkを入れ子のまま残しません。
時間カーブはAuto Key、SDKは一時値、short／longのLayerはMayaの編集先選択に従います。
複数対象は各更新の全件を事前検証し、途中の不正入力はその更新を拒否して操作を終了します。
既に成功した更新は最後の確定値として維持し、Undo一回で操作前へ戻せます。

Esc、フォーカス喪失、非表示、無効化、範囲変更では最後の確定値で終了します。
Escで開始値へロールバックしません。Maya時刻の移動も操作を終了し、
同時刻の再評価では継続します。時刻変更command自体のUndoはMaya標準の履歴です。
終了後の古いマウス移動・キーリピートを新しい時刻へ持ち越しません。
書込み中の終了要求は、そのcommandが戻ってからUndoを閉じます。

Slider自身はMayaをimportせず、Maya callbackも追加しません。
Maya連携側が操作中だけ時刻を監視し、終了・監視解除・Qt破棄時に解除します。
Viewだけの破棄では共有Bindingを終了しません。

## 操作サンプル

Maya Script EditorのPythonタブで実行します。

```python
import bd_tools
bd_tools.reload_package(reload_util=True)

from bd_util._sample.maya.ui.int_sample import slider
window = slider.show_demo()
```

`show_demo()`は現在のsceneへ二つの検証用transformと整数属性を追加します。
既存sceneは消去しません。Windowを閉じても検証用ノードは残ります。
`show()`はPython正本だけのWindowを開き、sceneを変更しません。
`show_maya(first, second)`は既存ノードを使います。整数の`byteValue`・`shortValue`・
両ノードの`longValue`に加え、第一ノードの同期用`pythonValue`が必要です。
Python同期行は生成時にPython初期値42をMayaへ適用します。

- 上の3行は同じPython値を共有し、操作範囲が異なります。
- `Maya long`行は二ノードを一括編集します。
- `Python → Maya long`行はPython正本とMaya属性を同期します。
- `Maya float`行は整数との操作切替とUndoの比較用です。

1. 狭い範囲を矢印で1刻み、広い範囲をドラッグし、値・ラベルの整数表示を確認します。
2. 値欄にSliderの範囲外の整数を入力し、実値と他Viewの表示が保たれることを確認します。
3. Maya行をドラッグし、Undo／Redo各一回で開始値と終了値へ戻ることを確認します。
4. 整数行とfloat行を順に操作し、それぞれのUndoが分かれることを確認します。
5. ドラッグ途中の時刻移動、ロック、Esc、closeで操作が終了することを確認します。
6. Windowの最小幅と拡大時の全Slider・値欄・ラベルの表示を確認します。

`tests/ui/test_int_slider.py`は整数写像と入力・寿命、
`tests/ui/test_int_slider_maya.py`はMaya同期・Undo・接続属性・サンプルを検証します。
公開型は`tests/typecheck/int_slider_contract.py`、最終検証は`scripts/verify.cmd`を使用します。

## 後続段階

今回の第一段階は`IntSlider`単体と連続編集、操作サンプルまでです。
第二段階で`IntSliderSpinBox`・`IntRangeSliderSpinBox`と設定保存、
第三段階でbdChannelBoxへのSlider組込みを行います。整数2／3成分MVVMは計画対象外です。

## Maya本体の確認（2026-10-15）

Maya 2025本体の専用一時設定でサンプルを起動し、自然幅と最小幅の画像を確認しました。
マウスの押下・移動・解放による整数入力、二ノードへのライブ同期、Undo／Redo各一回、
Python正本とMaya同期、32-bit両端、時刻移動による終了とclose時の解放が成功しました。
結果は`%TEMP%/bd-int-slider-maya2025-idatf4ds/result.json`の`success: true`です。
同じ場所に`initial-window.png`・`minimum-window.png`・`edited-window.png`を保存しました。

検証runnerは終了code 0でした。結果保存後のMaya終了待ちは完了せず、
runnerが専用processを終了したためMaya processの終了codeは1です。
Mayaの正常終了は未確認です。Maya 2026／2027本体の画面操作も未実施です。
第一段階の利用者による操作確認はこれからです。

## 自動検証

`scripts/verify.cmd`が終了code 0で完了しました。

| 確認対象 | 結果 |
| --- | --- |
| Black・3 versionのPyright型契約 | 成功。新しい公開APIとサンプルの補完を含む |
| 新規実装とサンプルの明示パス指定Pyright | Maya 2027で型エラー・警告0件 |
| Maya 2025 full pytest | 成功 |
| Maya 2025／2026／2027 Qt UI | 各1053件成功。整数Sliderの新規70件を含む |
| Maya 2025／2026／2027 Maya UI | 各804件成功 |

full pytestでQt applicationがないため省略するWidgetテストは、続くQt UIで検証しています。
toolsのBlack・Pyrightとunit test 37件も成功しました。
共通Undo管理の利用側回帰として、toolsのMaya 2025／2026／2027の
全runtime testを順に実行し、各394件が成功しました。
