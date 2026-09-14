# 浮動小数点MVVMの到達点と今後の拡張

2026-09-14時点で、単一値・3成分のMVVM基盤と、ラベル・スライダー・範囲／step編集付きViewまでの
予定した機能実装は完了しています。`Float3RangeSliderSpinBox`もユーザーからMaya上での動作確認報告を受けています。
この文書は次回の開発時に、現在の仕様と未実装の拡張候補を確認するための入口です。

## 完了した範囲

| 項目 | 単一値 | 3成分 |
| --- | --- | --- |
| Maya属性が正本 | `MayaFloatPlugBinding` | `MayaFloat3PlugBinding` |
| Python属性が正本 | `FloatBinding.from_attribute()` | `Float3Binding.from_attribute()` |
| Python正本とMayaの同期 | `MayaFloatBinding.from_attribute()` | `MayaFloat3Binding.from_attribute()` |
| 数値入力 | `FloatSpinBox` | `Float3SpinBox` |
| 数値表示・選択コピー | `FloatLabel` | `Float3Label` |
| スライダー＋数値入力 | `FloatSliderSpinBox` | `Float3SliderSpinBox` |
| 範囲・step編集付きスライダー | `FloatRangeSliderSpinBox` | `Float3RangeSliderSpinBox` |

単一値のスライダーは`FloatSlider`として単独でも使用できます。
各構成で共有View、単位追従、表示精度、編集可否、寿命管理を扱い、Maya連携ではUndo／Redoにも対応します。
対象属性と同期の詳細は[単一値binding](float_binding.md)、[3成分binding](float3_binding.md)、
[PythonとMayaの単一値同期](python_float_maya_binding.md)、[PythonとMayaの3成分同期](python_float3_maya_binding.md)を参照してください。

## Min／Max・stepの保存と復元（実装済み）

単一値・3成分Viewを`UiStateManager`へ明示登録できるようになりました。
公開単位の範囲と表示単位のstepを、tool・Window・View・軸ごとに独立して保存します。
既存の6サンプルは保存を有効にしており、Window再生成時に復元します。

配置とは別のsettings_pathを使用し、**UI配置リセットではMin／Max・stepを保持**します。
正本・hard limit・Undo履歴は変更しません。確定設定の変更時に退避し、close・破棄・Maya終了時に保存します。
形式version・単位種別・数値を検証してから行へ適用し、不正な行は現在の設定を維持します。
API、単位の扱い、保存形式、寿命と検証の詳細は[Min／Max・stepの保存と復元](float_view_settings.md)を参照してください。

stepモード、幅、表示桁数、単位文字の表示可否は保存対象に含めず、生成時引数を使います。

## 今後の任意拡張

次のリセット操作は未実装の候補です。公開API名・UI配置は実装着手時に決めます。

### 範囲・stepを初期設定へ戻す操作

生成時に指定した範囲とstepへ戻す操作です。初期設定は公開単位の範囲と表示単位のstep数値として保持する案です。
Maya属性のdefault値へのリセットとは別の操作で、正本の現在値やUndo履歴を変更しません。

- 単一値ではその行、3成分では軸単位を基本とし、必要なら全軸をまとめる操作を検討する。
- 他の共有Viewの設定を保持し、リセット後も現在の単位とhard limitを使って表示する。
- 操作中の軸の範囲を戻す場合は、既存の`setFloatRange()`と同様にその軸のドラッグを確定終了する。
- 保存機能と併用する場合は、対象キーの削除または初期設定の保存まで扱い、Window再作成時に古い設定が復活しないようにする。

配置はコンテキストメニューや任意表示のボタンなどを比較し、省スペースな既存レイアウトを保つ方針です。
Window配置リセットでは数値設定を保持する方針です。範囲だけ・stepだけを戻せるかは着手時に決めます。

## 拡張時に維持する仕様

- Maya属性の実値を表示桁数へ丸め直さない。3成分の1軸編集では他2軸の未丸めの値を保持する。
- 範囲とstepはView・軸ごとに独立させ、Mayaのhard limit、正本、他View、Undo履歴へ変更を波及させない。
- 距離・角度の表示単位へ追従する。単位文字が非表示でも数値の単位変換を有効にする。
- Min／Maxの表示桁数の既定は0、各数値欄の単位文字の既定は非表示とし、stepの精度は現在値の表示桁数から独立させる。
- stepの加算モードと10倍／1/10倍モードを維持する。後者で15を直接入力した場合も150／1.5へ操作できるようにする。
- 各ドラッグ位置を正本と他Viewへ即時反映し、Maya連携では1軸のドラッグをUndo 1回にまとめる。
- Maya正本のlock・入力接続による値の編集停止と、View設定である範囲・stepの編集可否を区別する。Python正本では既存の同期保留仕様を使う。
- Viewの破棄で共有Bindingを終了しない。Binding・ViewModelの終了では入力を停止し、Maya callbackを解放する。
- 子Widgetの具体型までIDE補完を維持し、3成分Viewには単一値Viewの処理を再利用する。

## 軽量化と検証の引き継ぎ

3成分の軸編集では`Float3ViewModel`が全体再同期を1回の軸Command完了時へ集約します。
詳細な計測条件は[Float3SliderSpinBox](float3_slider_spin_box.md#軸編集時の再同期と処理時間)を参照してください。
setterによる他軸の補正、同値入力時の他軸変更、失敗時の実値復旧、通知先からの再編集も維持します。

`tests/ui/test_float3_slider_spin_box_maya.py`では、両方の3成分スライダーを対象に、
通常の位置変更ごとの全体通知1回とMaya実値の読込20回以下を検証しています。
この回数はテスト条件での回帰基準で、任意のシーンや再入処理の回数を制限するものではありません。
時間だけを基準にせず、即時同期・通知回数・読込回数とMaya本体での操作感を合わせて確認します。

保存・復元の拡張やリセットの実装時は、単一値／3成分、共有View、cm／m・deg／rad変更、
表示0桁・高精度、範囲外の現在値、lock・接続、ドラッグ中、Window再作成・Maya再起動を確認します。
不正な保存データ、他View・他軸との独立性、復元時の正本不変、Undo履歴不変も検証対象です。
既存テストの入口は[単一値範囲View](float_range_slider_spin_box.md#サンプルと確認)と
[3成分範囲View](float3_range_slider_spin_box.md#サンプルと確認)に記載しています。
最終検証には`scripts/verify.cmd`を使用し、各Maya versionの結果を[UI README](README.md#maya-2025--2026--2027-ui互換性確認)へ記録します。
