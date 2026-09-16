# enum MVVMの到達点と今後の拡張

2026-09-17時点で、enum基盤、ラジオボタンView、複数Mayaプラグの一括編集まで、
今回合意した実装は完了しています。各段階でユーザーから動作確認・push完了の報告を受けています。
合意範囲に未完了の実装はありません。

この文書は開発再開時の入口です。利用方法は[enum binding](enum_binding.md)、
一括編集の詳細は[複数プラグ基盤](plugs_binding.md#enum属性群)を参照してください。

## 完了した範囲

| 正本・構成 | 公開Binding | 初期動作 |
| --- | --- | --- |
| Pythonオブジェクトの整数属性 | `EnumBinding.from_attribute()` | Python値と指定した定義を読む |
| 単一のMaya enum属性 | `MayaEnumPlugBinding` | Mayaの実値・実定義を読み、書き戻さない |
| Python正本と単一Maya属性の双方向同期 | `MayaEnumBinding.from_attribute()` | Python値をMayaへ反映する |
| 同じ定義を持つ複数Maya属性 | `MayaEnumPlugsBinding` | 先頭を代表として読み、他対象へ書き戻さない |

全構成で`EnumComboBox`、`EnumRadioButtonGroup`、`EnumLabel`を共有できます。
RadioButtonGroupは横並び・縦並びに対応します。負数・飛び番・未定義の現在値、
定義変更、編集可否、共有Viewとcallbackの寿命を扱います。
Maya正本の入力はUndo／Redoに対応し、一括編集では対象群を一回のUndoにまとめます。

サンプルは`bd_util._sample.maya.ui.enum_sample`の`minimal`、`maya_plug`、
`maya_view`、`maya_plugs`です。Mayaを使うサンプルは既存ノードを指定し、
ノードの作成・削除は行いません。`maya_view`はPython値を初期適用します。

## 採用した設計と実装の分担

値の保持には`int`を採用しました。一方、選択肢・項目名・未定義値を扱う責務があるため、
同期APIは`EnumViewModel`とし、汎用の整数入力から分離しています。
利用者にPythonの`Enum`／`IntEnum` classの作成を要求しません。
今後汎用int基盤を追加しても、enumの選択肢管理まで整数入力Viewへ移す必要はありません。

| 実装の入口 | 主な責務 |
| --- | --- |
| [ui/binding/enum](../../python/bd_util/ui/binding/enum/__init__.py) | 不変な`EnumItem`／`EnumDefinition`、Value・Command・ViewModel、Python Store、Qt View |
| [enum_plug_resolver.py](../../python/bd_util/maya/ui/binding/enum_plug_resolver.py) | 対象の実体・scalar enum型・配列祖先の検証 |
| [_enum_plug_value.py](../../python/bd_util/maya/ui/binding/_enum_plug_value.py) | Mayaの実値と実定義の取得。生成classの項目表を正本にしない |
| [_enum_plug_endpoint.py](../../python/bd_util/maya/ui/binding/_enum_plug_endpoint.py)・[enum_plug.py](../../python/bd_util/maya/ui/binding/enum_plug.py) | 単一プラグのcallback、書込み、Python正本との同期・終了 |
| [plugs_binding.py](../../python/bd_util/maya/ui/binding/plugs_binding.py) | enum属性群の定義一致、代表値、同値入力と集約状態 |
| [_plugs_store.py](../../python/bd_util/maya/ui/binding/_plugs_store.py) | bool／float／enum共通の監視、入力前検証、Undo、失敗時の復旧 |

Maya固有の処理は`bd_util.maya.ui`へ置き、Qt ViewにMayaアクセスを持たせません。
`_plugs_store.py`を変更する場合はenumだけでなく既存bool／floatの回帰も確認してください。

## 拡張時に維持する仕様

- **整数値と表示位置を分離する。** ComboBoxのindexやRadioButtonのIDをenum値とみなさない。
  Qtの固定幅整数へPython値を狭めず、Mayaのshort値の扱いはadapter内に留める。
- **未定義値を勝手に修正しない。** 読取りでは保持し、通常入力は定義内の整数に限定する。
  失敗復旧では元の未定義整数へ戻せる必要があるため、通常入力と復旧の検証を混同しない。
- **値と定義を一緒に確定してから通知する。** 定義通知中に再編集・再読込みされても最新状態を公開する。
  表示の再構築は入力ではなく、CommandやMaya書込みへ折り返さない。
- **同値の要求と値の変更通知を区別する。** Python正本の同値Commandも同期の確認になる。
  複数プラグでは代表と同値でも後続だけを変更できるため、単一値ViewModelの同値省略を流用しない。
  混在・対象の状態は`state_changed`、代表値は`changed`、代表の定義は`definition_changed`で通知する。
- **定義の同一性と表示順を区別する。** `EnumDefinition.matches()`は整数値と項目名の対応を比較する。
  定義の順序変更もViewには反映するが、PythonとMayaの同期や一括編集の一致条件には順序を含めない。
- **実定義の変更を検出し続ける。** 定義文字列が同じ間だけ解析結果を再利用する。
  一括編集では入力直前の検証も残し、書込みcallbackによる途中の定義変更を見逃さない。
- **正本に応じた入力可否を保つ。** Python正本ではMaya側の不一致・lockでPython編集まで停止しない。
  Maya属性群では定義不一致か代表の書込み不可で全体を停止し、後続のlock・接続は個別に除外する。
- **Maya正本の読込みでUndo履歴を増やさない。** Maya正本の外部変更・Undo／Redo・refreshは読取りとして扱う。
  Python正本のrefreshにはPython確定値のMaya同期も含まれる。Undo／Redoの復元時は、
  setter補正によるMaya再書込みでRedo履歴を消さないよう、既存の保留処理を維持する。
- **共有Viewと同期先の寿命を分離する。** Viewを閉じても共有Bindingを終了しない。
  Binding・ViewModelの終了と構築途中の失敗ではcallbackを解放する。削除Undoで対象へ自動再接続しない。
  Qtの遅延破棄とqueued通知を検証するテストでは、DeferredDelete後のevent loopも処理する。

一括編集の`writable_count`は対象ごとの件数で、全体の入力可否とは異なります。
代表lockや定義不一致による停止中も0とは限らないため、入力Viewは
`view_model.set_value_command.can_execute`へ接続します。
`EnumComboBox`は同じindexの選択ではCommandを発行しません。
同値揃えは`apply_representative_value()`か、選択済みRadioButtonのクリックで行います。

## 今後の候補と現在の対象外

今後の候補として挙がった汎用int／stringのMVVM基盤は、今回のenum実装とは独立した機能です。
実装順・公開API・対応Viewは未確定で、次のツールで必要になる値型に合わせて決めます。

現在は配列と配列配下の属性、異なるenum定義間の値・名前変換、Maya定義の自動書換え、
Python正本と複数Maya属性の双方向同期を提供していません。
これらは今回の残作業ではなく、必要になった場合に責務・同期方向・失敗時の挙動を検討する別の拡張です。
対象選択の追従は利用側が担当し、対象を変更するときはBindingを作り直します。

## 検証記録と再開時の確認

2026-09-17の複数プラグ実装完了時に、`QT_QPA_PLATFORM=offscreen`を指定した
`scripts/verify.cmd`が成功しています。以下はその時点の記録で、将来の固定件数ではありません。

| 検証 | 結果 |
| --- | --- |
| Black / git diff --check | 成功 |
| Maya 2025／2026／2027 Pyright contract | 各versionでエラー・警告なし |
| Maya 2025 full pytest | 4,171 passed / 690 skipped |
| Maya 2025／2026／2027 Qt/UI専用pytest | 各versionで790 passed、skipなし |
| Maya 2025／2026／2027 Maya UI専用pytest | 各versionで305 passed、skipなし |

full pytestではMaya初期化が先に行われるため、QWidgetを必要とするテストがskipされます。
QApplicationを先に作成するQt/UI専用processでこれらも検証しています。
一括編集で追加したテストはMaya側25件、View・サンプル側4件です。
テストファイルの入口は[enum binding](enum_binding.md#サンプルと検証)と
[複数プラグ基盤](plugs_binding.md#検証)にまとめています。

ユーザーの動作確認・push報告は自動テストとは別の確認記録です。
使用したMaya versionと個別操作条件の指定はないため、全対応versionのMaya本体で
同じ手動操作を実施済みとは扱いません。

次回変更時は、定義の追加・削除・名前／順序変更、未定義値、同値入力、lock・接続、
再入通知、途中失敗・復旧失敗、Undo／Redo、共有Windowとcallbackの終了を確認します。
公開Bindingだけでなく、`store`・子Widgetの具体型までIDE補完を維持してください。
最終検証は引き続き`scripts/verify.cmd`を使用します。
