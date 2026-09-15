# 複数のMaya属性を一つの入力で編集する

`MayaBoolPlugsBinding`と`MayaFloatPlugsBinding`は、順序付きの属性群を既存の
`BoolComboBox`、`FloatSpinBox`、`FloatSliderSpinBox`などへ接続します。
先頭属性を代表として表示し、ユーザーの入力時だけ編集可能な対象へ同じ値を適用します。

```python
from bd_util.maya.ui import MayaFloatPlugsBinding, resolve_float_plug
from bd_util.ui import FloatSpinBox, qt

owner = qt.QWidget()
binding = MayaFloatPlugsBinding(
    [resolve_float_plug(name, "tx") for name in ("pCube1", "pCube2")],
    parent=owner,
)
editor = FloatSpinBox(binding, owner)
binding.set_value(10.0)  # 全対象のtranslateXを10cmへ設定する
```

属性の列挙、表示条件、選択順、同名属性の組み合わせは利用側が決めます。
Bindingは空の属性群、重複する実体、非対応型を拒否します。
floatの数値・距離・角度の単位種別は全対象で一致させてください。
異なるnodeや長名・短名から解決した属性も、同じ単位種別なら扱えます。

## 公開する状態と操作

| API | 内容 |
| --- | --- |
| `value` / `changed` / `view_model` | 代表の確定値と、既存Viewへの接続先 |
| `set_value(value)` | 編集可能な対象へ絶対値を適用し、変更があればboolで返す |
| `apply_representative_value()` | 代表の現在の未丸め実値を他の編集可能な対象へ揃える |
| `is_mixed` | 利用可能な対象の値が代表と異なるか |
| `target_count` / `writable_count` | 登録した対象数と、個別に書込み可能な対象数 |
| `target_states` | 対象順の`tuple[MayaPlugTargetState, ...]` |
| `state_changed` | 対象値、混在、編集可否の変更を引数なしで通知するsignal |
| `edit_failed` | 入力拒否や実行失敗の説明をstrで通知するsignal |
| `refresh()` / `dispose()` | 全対象の再同期とcallbackの明示終了 |

`MayaPlugTargetState`はimmutableな`name`、`is_available`、`is_writable`、
`reason`を持ちます。`name`は同名DAGを区別する属性名です。
後続の削除・lock・入力接続はその属性だけを入力対象から除外します。
代表が書込み不可の場合は全体の入力を止めます。この場合も`writable_count`は
個別に書込み可能な対象数を示すため、0になるとは限りません。
アニメーション接続を含む入力接続は、キーを暗黙に変更せず読取り専用です。

`changed`は代表値の変更通知です。代表値を変えず後続だけが変わる入力では、
`state_changed`を用いて混在表示や件数を更新してください。
readonlyの後続に異なる値が残る場合、入力後も`is_mixed`はTrueです。
既存のComboBoxやSpinBoxは未変更の入力をCommandにしません。
表示と同じ値へ揃える操作は、明示的なボタンなどから
`apply_representative_value()`を呼び出してください。

## 表示と入力の分離

構築、`refresh()`、単位変更、外部操作、Undo／Redo、混在状態の更新では
Maya属性へ書き戻しません。`changed`を別属性の書込みへ接続して同期させる構成は
不要です。選択変更で対象を変える場合は古いBindingを`dispose()`し、作り直します。

floatの公開単位は単一属性Bindingと同じで、距離はcm、角度はdegreeです。
表示の単位・hard min/maxは先頭属性の`FloatPresentation`を保ちます。
後続の範囲に合わせて表示をクランプせず、代表の実値をそのまま確認できます。

入力時は編集可能な全対象のhard min/max、有限値、float32の格納範囲を
**書込み前に**検証します。後続の範囲に違反する入力は`edit_failed`で説明し、
例外を送出します。silent clampや一部の対象だけへの範囲内適用は行いません。
Sliderに代表の範囲を使った場合もこの検証は同じです。
soft limitは入力制限に使いません。

## Undo、失敗復旧、終了

boolの確定・数値の確定は対象群をまとめてUndo一回になります。
floatのドラッグは、各位置を全対象へ即時反映し、全ドラッグをUndo一回にまとめます。
全てが同じ格納値になる要求では書込みやUndoを追加しません。
代表と同値でも後続に差分がある場合は、一括入力を実行します。

適用途中で失敗した場合、今回の入力で変更した対象を同じUndo chunk内で
元へ戻します。ドラッグでは直前の成功した位置を維持し、ドラッグを終了します。
復旧処理も失敗する外部変更があった場合は、元の失敗と復旧失敗を
`ExceptionGroup`として通知します。復旧に成功した失敗操作は、値を変えない
Undo項目として残る場合があります。既存のUndo履歴を削除して隠しません。

callbackはnodeごとにまとめ、dirty通知を次のQt event loopで集約します。
対象削除は無効状態として保持し、削除Undoや同名再作成へ自動再接続しません。
明示終了・Qt ownerの破棄・Maya終了でcallbackと開いているUndoを解除します。
選択変更やWindow closeを所有するcontrollerは、Viewを破棄する前にBindingを終了させてください。

## 検証

- `tests/maya/ui/test_plugs_binding.py`: 無書込み初期表示、混在、同値揃え、範囲、
  単位、lock・接続、単発・連続Undo、部分失敗の復旧、削除とcallback解放。
- `tests/ui/test_plugs_binding_views.py`: 既存ComboBox・SpinBox・Sliderとの接続。
- `tests/typecheck/maya_plugs_binding_contract.py`: 状態APIと既存Viewへの受け渡し型。

開発中はtargeted pytest、最終確認は`scripts/verify.cmd`を使用します。
