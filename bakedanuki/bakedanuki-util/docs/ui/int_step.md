# 整数Stepの入力と保存

`IntStepSpinBox`は正の整数Stepを編集し、`IntValueStepSpinBox`は`[値][Step]`を横に並べます。
Python正本・Maya正本・複数Maya属性の整数Bindingで共通に使用できます。

```python
from bd_util.ui import IntValueStepSpinBox

editor = IntValueStepSpinBox(
    binding,
    single_step=1,
    step_mode="multiplicative",
    value_select_all_on_mouse_focus=True,
    step_select_all_on_mouse_focus=True,
)
editor.setSingleStep(15)
```

## 整数演算と入力

Stepの範囲は1～2147483647です。APIは`bool`・小数・文字列を暗黙変換しません。
任意の正整数を直接入力できます。未確定文字はEnter・通常のフォーカス移動で確定します。
不正な文字入力は確定値へ戻し、0や小数を正本へ渡しません。

| 操作方式 | 上下操作 |
| --- | --- |
| `additive`（utilの既定） | 正の`step_increment`を加減算。既定は1 |
| `multiplicative`（bdChannelBoxの既定） | 上は10倍、下は10で整数除算し下限1 |

10倍方式は`1→10→100`、任意入力からは`3→30→300`になります。
下方向は`150→15→1`で、`1`からは減少しません。
増加結果が上限を超える場合は現在値を維持し、その方向の矢印を無効にします。
上限へ切り詰めて10倍の列を変えることはありません。演算は整数で行います。
加算方式では増減結果が範囲外なら現在値を維持します。

値欄の上下操作は現在のStepを値に加減算します。Stepを10倍にする操作とは独立です。
値の型範囲、hard limit、複数対象、Undoは接続したBindingと利用側へ委譲します。

## 複合ViewのAPIと寿命

| API | 内容 |
| --- | --- |
| `single_step=1` | 値欄の初期刻み幅 |
| `step_mode="additive"` / `step_increment=1` | Step欄自身の操作方式と加算幅 |
| `value_wheel_requires_focus=False` / `step_wheel_requires_focus=True` | 各欄のホイール方針 |
| `value_select_all_on_mouse_focus=False` / `step_select_all_on_mouse_focus=False` | 初回文字クリックの全選択 |
| `value_width=None` / `step_width=68` | 値欄の自動幅または固定幅と、Step欄の固定幅 |
| `spin_box` / `step_spin_box` / `view_model` | 子Viewと共有する入力元 |
| `singleStep()` / `setSingleStep(value)` | 両欄のStepの取得・変更 |
| `settingsChanged` | 実際にStepが変わったときだけ通知 |

`IntStepSpinBox`単体は`value=1`と同じStep操作引数を受け取ります。
`stepMode()`で生成時の方式を取得できます。`setSingleStep()`は加算方式の増減幅です。
両欄はEnterを親へ伝播せず、任意指定の初回全選択と再クリック・ドラッグ選択を両立します。
ホイールと全選択の設定は各欄の既存getter／setterでも変更できます。

StepはView固有の設定です。変更しても正本や同じBindingの別Viewへ伝播しません。
正本が読み取り専用・lock中でもStep設定は変更できます。Binding終了・Qt破棄後は両欄を停止します。
Viewは入力元を保持し、Viewだけの削除では共有Bindingを終了しません。
幅や矢印ボタンなどの表示は公開した子Widgetから調整できます。
値欄が自動幅の場合もStep欄の固定幅を先に確保し、残りの幅を値欄へ割り当てます。

## 汎用Profileと永続化

`IntStepSetting(key, single_step)`と`IntStepProfile`はMayaに依存しません。
空でない識別子ごとにStepを保持し、`single_step(key)`、`set_single_step(key, value)`、
`replace_entries(entries)`、`remove(key)`、`clear()`を公開します。
未登録値は`None`、変更操作は実変更時に`True`を返して`changed`を通知します。
一括置換は全項目を検証してから反映し、同じ識別子は後の項目を優先します。

```python
from bd_util.ui import IntStepProfile

profile = IntStepProfile(parent)
ui_state.register_int_step_profile("integer_steps", profile)
profile.set_single_step("count", 15)
```

View単体は設定ファイルを作りません。利用側が`settingsChanged`とProfileを接続します。
Profileの保存形式は`int_step_profile`、内部JSONのversionは1で、整数のまま保存します。
形式・version不正なら復元を拒否し、個別項目だけが不正ならその項目を除いて復元します。
不正な保存値をfloatから整数へ変換しません。他の設定の復元は継続します。

## bdChannelBox

明示された両側hard limitが`Min < Max`を満たす整数行は`[値][Slider]`、
それ以外は`[値][Step]`を表示します。Step欄の既定は1・10倍方式です。
byteの型既定の全範囲0～255だけではSliderへ切り替えません。0～31などの狭い範囲は対象です。
範囲の選別は[整数binding](int_binding.md#開発完了と拡張時の確認)を参照してください。
選択中のStep欄を持つ行へ同じ数値を設定し、各行の方式は維持します。
未選択行からの操作はその行だけが対象です。Step欄がない行は対象外理由を表示します。

floatと整数を混在選択した場合は、連携境界だけで整数相当のfloatを検証して整数へ変換します。
`5.0`は整数行に`5`として共有できますが、`0.5`や整数上限超過では全体を拒否します。
対象を全て検証する前に保存や他行のStepを変更せず、操作元も以前の設定へ戻します。
Step変更はsceneとMaya Undoを変更しません。値欄の上下は現在の一括入力規則に従います。

整数の保存先は`bd_channel_box/preferences/main`の`integer_attribute_steps`です。
識別子は`long:count`のように属性型と正式な相対属性pathを組み合わせます。
node名・node型・namespace・sceneを含めず、同じpathでもbyte・short・longで設定を分けます。
既定値1と同じ設定は保存せず、既存floatの`attribute_steps`の形式を維持します。
close・再表示・reload・Maya再起動後に復元し、配置リセットでは保持します。
Slider表示中も保存済みStepを保持し、Step表示へ戻ると復元します。
既存の「Step設定」の選択属性リセットはStep欄のある整数行も対象にします。
全属性リセットには、画面外やSlider表示中の保存値も含めます。

## 操作サンプル

Maya Script EditorのPythonタブで実行します。sceneやMaya属性は変更しません。

```python
import bd_tools
bd_tools.reload_package(reload_util=True)

from bd_util._sample.maya.ui.int_sample import step
window = step.show()
```

上段のStepで`1→10→100`と、手入力`15`から下へ`1`になることを確認します。
下段は加算方式です。Stepだけを変えても共有する値は変わりません。
値欄を操作すると両Viewとラベルが更新されます。close後に再表示すると両Stepが復元されます。
リセットボタンで保存値を削除し初期値1へ戻せます。
bdChannelBoxでは整数とfloatの混在選択、範囲違反、選択リセットと全リセットも確認できます。

## 検証記録

`scripts/verify.cmd`が成功しました。Black、3 versionの型契約、Maya 2025 full pytest、
Maya 2025／2026／2027それぞれのQt UI 983件・Maya UI 804件を通過しています。
新規の`tests/ui/test_int_step.py`29件は、各versionで全て成功しました。
利用側toolsのBlack・Pyright・unit test 37件と、Maya 2025／2026／2027の
runtime test各394件も成功し、整数の一括Step・保存・リセットと既存操作を確認しました。
新しい実装とサンプルはMaya 2027の明示パス指定Pyrightでもエラー・警告0件です。

Maya 2025本体でも、10倍操作・任意整数入力・混在選択の拒否・値Undoと欄幅、
close後の復元を確認しました。別processへの再起動後も整数Step 15とfloat Step 2.5が復元され、
選択属性／全属性のリセットが成功しました。再起動検証runnerの終了codeは0です。
初回runnerは操作結果の保存後にMaya終了待ちが120秒でタイムアウトし、終了codeは1でした。
その検証用processはrunnerが終了しました。操作結果の成功とprocess終了の結果は区別します。

資料は`%TEMP%/bd-int-step-maya2025-hilbw8sy`の`initial-result.json`・`restart-result.json`と
`initial-window.png`・`restart-window.png`です。両JSONは`success: true`で、画像も確認しました。
Maya 2026／2027本体の画面操作は実施していません。
利用者のサンプル初回操作でStep欄が見えない報告を受け、下記の配置不具合を修正しました。
修正後に利用者がStep欄の表示と操作を確認し、commit・pushが完了しました。
確認したMaya versionは未申告です。

### 自動幅でのStep欄の表示修正（2026-10-15）

Step欄の横方向のsize policyが`Ignored`のため、値欄が自動幅だとStep用の幅が
確保されず、Step欄全体が親Viewの右外へ配置されていました。
整数とfloatの複合Viewを`Fixed`へ変更し、Step欄の固定幅を確保しました。
`tests/ui/test_value_step_layout.py`は両型の自動幅・固定幅を4件で検証します。
修正前は自動幅の2件が失敗し、修正後は4件とも成功しました。
サンプルの既存testにもStep欄の表示領域と可視性の検証を追加しました。

Maya 2025本体で初期表示、拡大・縮小、上キーによる10倍操作、値欄の連動、
Step設定のclose・再表示後の復元を確認し、画像でも両Step欄の表示を確認しました。
資料は`%TEMP%/bd-int-step-sample-maya2025-jhmoveac`の`result.json`と
`initial-window.png`・`edited-window.png`・`reopened-window.png`です。
JSONは`success: true`、検証runnerの終了codeは0です。
操作後にMayaの終了待ちが完了しなかったためrunnerが専用processを終了し、
Maya processの終了codeは1でした。Mayaの正常終了は未確認です。
起動中に遅延生成された既定IK solver 4個はJSONへ記録しています。
scene非変更は`tests/ui/test_int_step.py`の独立したテストで検証します。

toolsのStep・欄幅の関連runtime testはMaya 2025／2026／2027で各27件が成功しました。
修正後も`scripts/verify.cmd`が終了code 0で完了しました。
Black、3 versionの型契約、Maya 2025 full pytest（8241成功・870 skip）、
3 versionそれぞれのQt UI 983件・Maya UI 804件、差分の空白検証が成功しています。
full pytestでQt applicationがないためskipしたWidgetテストは、続くQt UI実行で検証しました。
