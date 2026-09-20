# FloatValueStepSpinBox

値の入力欄 `FloatSpinBox` と、刻み幅の入力欄 `FloatStepSpinBox` を横に並べる
汎用Viewです。Maya固有の属性判定を持たず、既存の `FloatBinding` または
`FloatViewModel` を受け取ります。単一属性・複数属性Bindingのどちらでも使用できます。

```python
from bd_util.ui import FloatValueStepSpinBox

editor = FloatValueStepSpinBox(
    binding,
    parent,
    decimals=3,
    single_step=15,
    step_mode="additive",
    step_increment=15,
)
```

## 設定と公開API

| API | 内容 |
| --- | --- |
| `decimals=6` | 値欄の表示・入力小数桁数 |
| `single_step=0.1` | 値欄の初期刻み幅。正の有限値 |
| `step_mode="additive"` | step欄の上下操作。`additive` または `multiplicative` |
| `step_increment=1.0` | additiveでstep欄自身を増減する幅 |
| `step_show_unit=False` | step欄に現在の表示単位を付けるか |
| `value_wheel_requires_focus=False` | 値欄のホイール操作にフォーカスを必須とするか |
| `step_wheel_requires_focus=True` | step欄のホイール操作にフォーカスを必須とするか |
| `value_width=None` | 値欄の固定幅。未指定なら残り幅に合わせて伸縮 |
| `step_width=68` | 上下ボタンを含め、4桁を表示できるstep欄の固定幅 |
| `.spin_box` | 値欄の `FloatSpinBox` |
| `.step_spin_box` | 刻み幅欄の `FloatStepSpinBox` |
| `.view_model` | 共有するViewModel。終了後は例外 |
| `.singleStep()` / `.setSingleStep(value)` | 刻み幅の取得・両欄の同期 |
| `.settingsChanged` | 刻み幅が変わったときの引数なし通知 |

multiplicativeはstep欄を10倍・1/10倍にします。値欄の上下操作は、その時点の
stepを加減算します。additiveで15刻みにする場合は、初期値と増減幅の両方に15を指定します。
step欄には正の有限値を直接入力することもできます。

値欄は従来どおりマウスオーバー中のホイールを受け付け、step欄は一覧スクロール中の
誤変更を避けるため、既定ではフォーカス中だけ受け付けます。生成時の2引数で個別に変更でき、
生成後も各欄の`wheel_requires_focus()`／`set_wheel_requires_focus()`を利用できます。
非フォーカス時に受け付けないホイールイベントは親Widgetへ渡します。

子Widgetを公開しているため、幅・prefix・ボタン表示などは利用側で指定できます。
値欄・step欄の単位文字は既定で非表示です。値欄は
`editor.spin_box.setUnitVisible(True)`、step欄は生成時の`step_show_unit=True`で表示できます。
単位文字を省略しても、現在の表示単位での入力・換算は継続します。
値の刻み幅は複合Viewの `setSingleStep()` で変更すると、両欄の表示と変更通知が揃います。

```python
editor = FloatValueStepSpinBox(binding, value_width=90, step_width=80)
editor.step_spin_box.setPrefix("step ")
editor.step_spin_box.set_wheel_requires_focus(False)
editor.setSingleStep(0.1)
```

## 値、単位、寿命

- 初期表示、step変更、単位変更では正本へ書き込みません。
- stepはこのView固有の設定です。同じBindingを使う別Viewのstepへ伝播しません。
- `single_step` と `step_increment` は表示単位です。単位変更時も数値を維持し、
  単位文字の表示が有効ならsuffixも更新します。例: 1 cmから表示単位をmへ変えるとstepは1 mです。
- 単位変更時はstep欄の古い未確定入力を捨てます。stepの小数精度は値欄と独立です。
- step欄は初期値を設定してから正の下限を適用し、生成途中の不要な極小値表示を省きます。
  初期化後の精度と`1e-323`から有限float最大値までの入力範囲は維持します。
- 値のhard limit、型・単位変換、複数対象への適用、Undoは既存のViewとBindingへ委譲します。
- 値が読取り専用でもstep設定は変更できます。入力元が終了・Qt破棄された場合は両欄を停止します。
- Viewだけを削除しても共有Bindingを終了しません。Viewは入力元を保持するため、
  利用側がViewだけを保持する構成にも対応します。

属性による初期値の選択、設定の保存先・共有範囲は利用側の責務です。
このViewは設定ファイルを自動作成しません。`settingsChanged` と `singleStep()` を使い、
必要な範囲で設定を保持できます。

検証は `tests/ui/test_float_value_step_spin_box.py`、公開型契約は
`tests/typecheck/float_value_step_spin_box_contract.py` に配置しています。
