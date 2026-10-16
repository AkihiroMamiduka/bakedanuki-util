# 整数Slider複合Viewと設定保存

`IntSliderSpinBox`と`IntRangeSliderSpinBox`は同じ`IntBinding`または`IntViewModel`を
複数の入力欄で共有します。Python正本、Maya正本、Python正本からMaya同期の三経路で使用します。
整数Slider拡張の第二段階です。第一段階の利用者確認・pushは完了しています。
bdChannelBoxへのSlider組込みは第三段階に予定しています。

## 基本のSliderと値欄

```python
from bd_util.ui import IntSliderSpinBox

editor = IntSliderSpinBox(
    binding,
    minimum=-100,
    maximum=100,
    single_step=1,
    layout_order="slider_value",
    value_select_all_on_mouse_focus=True,
)
```

`layout_order="slider_value"`は`[Slider][値]`、`"value_slider"`は`[値][Slider]`です。
既定は前者です。`editor.slider`は`IntSlider`、`editor.spin_box`は`IntSpinBox`、
`editor.view_model`は共有ViewModelです。`layoutOrder()`で並び順を取得します。
`steps=1000`はSliderの最大分割数、`single_step=1`は値欄だけの整数刻み幅です。
Sliderの範囲変更は`editor.slider.setIntRange(minimum, maximum)`を使います。

## Min／Max／Step付きのView

```python
from bd_util.ui import IntRangeSliderSpinBox

editor = IntRangeSliderSpinBox(
    binding,
    minimum=-100,
    maximum=100,
    single_step=1,
    step_mode="multiplicative",
    minimum_width=140,
    maximum_width=140,
    value_width=140,
    step_width=110,
)
```

並びは`[Min][Slider][Max][値][Step]`です。各部品は順に`minimum_spin_box`、`slider`、
`maximum_spin_box`、`spin_box`、`step_spin_box`で参照できます。
Min／Max／StepはこのViewだけの設定で、同じBindingの別Viewへ共有しません。

| API・引数 | 仕様 |
| --- | --- |
| `intRange()` / `setIntRange(minimum, maximum)` | 要求範囲を取得・変更。両端は32-bit整数、Min < Max |
| `effectiveIntRange()` | 要求範囲と正本の制限の共通部分。操作可能な幅がなければ`None` |
| `singleStep()` / `setSingleStep(step)` | 値欄の刻み幅を取得・変更。1～2147483647の整数 |
| `step_mode="additive"` | Step欄自身は`step_increment=1`ずつ増減。utilの既定 |
| `step_mode="multiplicative"` | Step欄自身は10倍／整数除算。1が下限、上限超過は現在値維持 |
| `steps=1000` | Sliderの最大分割数。Stepとは独立 |
| `slider_width` / `minimum_width` / `maximum_width` / `value_width` / `step_width` | 正の固定幅。未指定の`None`は伸縮 |
| `minimum_enabled` / `maximum_enabled` / `value_enabled` / `step_enabled` | 各欄固有の編集可否。既定`True` |
| `minimum_show_buttons` / `maximum_show_buttons` / `value_show_buttons` / `step_show_buttons` | 各欄の上下ボタン。既定`True` |
| `value_select_all_on_mouse_focus=False` | 値欄の初回文字クリックで全選択するか |
| `rangeEditRejected(str)` | 不正なMin／Max入力の理由を通知 |
| `settingsChanged()` | 範囲またはStepの実変更時に通知 |

Min／Max欄自身の上下操作は常に1刻みです。Stepは値欄だけへ適用します。
任意の正整数Stepも入力でき、10倍方式では15→150→15→1と変化します。
子の値欄を直接変更せず、複合Viewの`setSingleStep()`で設定を更新してください。

## 正本・制限・連続編集

値と範囲は`-2147483648～2147483647`の整数です。APIは`bool`・小数・文字列を
暗黙変換しません。不正なAPI設定は例外を送出し、変更前の設定を維持します。
UIでMin以下のMaxやMax以上のMinを確定した場合は直前の範囲へ戻し、下部に理由を表示します。

要求範囲と正本の型範囲・hard limitを交差させ、実効範囲が異なる場合は下部へ表示します。
操作可能な幅がなければSliderだけを無効化します。範囲外の実値は値欄に正確に残し、
Sliderのつまみだけ端へ寄せます。範囲・Stepの編集、生成、表示同期、保存復元は
正本・scene・属性のhard limitを変更せず、MayaのUndo履歴を増やしません。
readonly・ロック中も、Bindingが生存していれば範囲とStepは編集できます。

Sliderの連続編集と中断・Undoは[整数Sliderと連続編集](int_slider.md)と共通です。
範囲変更は自身のドラッグを最後の確定値で終了します。Escも確定終了で、開始値へ戻しません。
Viewのclose・非表示・破棄は操作を終了します。Viewだけの破棄では共有Bindingを終了しません。
Bindingの終了後は範囲・Stepの欄も停止します。

## 保存と復元

明示登録したViewだけを既存の`UiStateManager`で保存します。

```python
from bd_util.maya.ui import create_ui_state_manager, MayaUiStateTracker

window.editor_settings = create_ui_state_manager("my_tool/editor_settings/main")
window.editor_settings.register_int_range_slider_spin_box("count", editor)
window.editor_settings_tracker = MayaUiStateTracker.for_window(
    window.editor_settings, window
)
```

Window配置とは別の`settings_path`を使い、managerとtrackerはWindowへ保持します。
keyは固定のASCII Python識別子です。同じBindingを共有するViewにも別keyを使います。
Mayaのversion別preferencesのtool別`ui.ini`へ保存します。
初回表示後に復元し、close・完全破棄・Maya終了時に最後の確定設定を保存します。
独自の寿命管理では`restore()`、`save()`、`save_cached()`を使えます。

型識別子は`int_range_slider_spin_box`、JSONは`version=1`、`minimum`、`maximum`、
`single_step`を持ち、数値は全てJSON整数です。全32-bit範囲もfloatへ変換しません。
全項目を検証してから一行へ適用し、通知は最後に一回だけ発火します。
不正な一行は一部も適用せず、その保存値を削除します。他行は独立して復元します。
復元で要求範囲が変わる場合は、進行中のSlider操作を確定終了します。

現在値、hard limit、幅、入力可否、ボタン、Step方式と増減量、Slider分割数は保存しません。
動的な属性行のStepだけを保存する既存の`IntStepProfile`も維持します。
既存のfloat設定・整数Step設定と保存型を分けており、移行は不要です。
保存の寿命・pathの詳細は[操作設定の保存](float_view_settings.md)も参照してください。

## 操作サンプル

Maya Script EditorのPythonタブで実行します。

```python
import bd_tools
bd_tools.reload_package(reload_util=True)

from bd_util._sample.maya.ui.int_sample import range_slider
window = range_slider.show_demo()
```

`show_demo()`は現在のsceneに検証用transformを二つ追加します。閉じてもノードは残ります。
`range_slider.show()`はPython正本だけで、sceneを変更しません。
`show_maya(first, second)`は既存二ノードの`longValue`と第一ノードの`pythonValue`を使います。
Python同期行は生成時にPython初期値42をMayaへ適用します。
保存先は`int_sample/editor_settings/range_slider`です。
「操作範囲とStepを初期値へ戻す」で値を保ったまま設定を戻します。

1. Min／Maxを編集し、確定値42が範囲外でも値欄に保持されることを確認します。
2. Min < Maxを満たさない入力が戻り、理由が表示されることを確認します。
3. 加算Step行と10倍Step行を操作し、値欄の増減量と他行の設定を確認します。
4. Maya行をドラッグし、一回Undo／Redoで二ノードの値が戻ることを確認します。
5. 範囲とStepを変更し、close後に同じ起動スクリプトを再実行して各行の設定復元を確認します。
6. Windowの最小幅と拡大時にMin／Slider／Max／値／Stepが全て見えることを確認します。

## 検証（2026-10-16）

新規Qt・Maya連携テスト39件がMaya 2025で成功しました。
新規実装・サンプル・公開型契約の明示パス指定PyrightはMaya 2027でエラー・警告0件です。
最終検証の`scripts/verify.cmd`は終了code 0で完了しました。

| 確認対象 | 結果 |
| --- | --- |
| Black・Maya 2025／2026／2027の公開型契約 | 成功 |
| Maya 2025 full pytest | 8241件成功、Qt applicationがない979件は省略 |
| Maya 2025／2026／2027 Qt UI | 各1092件成功。新規39件を含む |
| Maya 2025／2026／2027 Maya UI | 各804件成功 |
| util・toolsの差分空白検査 | 成功 |

full pytestで省略するWidgetテストは、続く各versionのQt UIで検証しています。
今回のtools変更は完了記録とロードマップだけで、製品コードの変更はありません。

Maya 2025本体の専用一時設定で、自然幅・最小幅の全欄表示、Min欄のEnter確定、
不正範囲の復元、整数Step、Maya二ノードのUndo、close後の設定復元とリセットを確認しました。
結果は`%TEMP%/bd-int-slider-maya2025-305bf648/result.json`の`success: true`です。
`initial-window.png`・`minimum-window.png`・`reopened-window.png`を保存し、画像も確認しました。
検証runnerは終了code 0でした。結果保存後は終了待ちが完了せず、runnerが専用processを
終了したためMaya processの終了codeは1です。Mayaの正常終了と2026／2027本体の画面操作は未確認です。
第二段階の利用者による操作確認はこれからです。
