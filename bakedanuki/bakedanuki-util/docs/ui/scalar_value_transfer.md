# Maya scalar値のクリップボード搬送

`bd_util`は、tool固有の行選択やメニューから独立した2層のAPIを提供します。

- `bd_util.ui.JsonClipboard`はMayaをimportせず、任意のJSON互換documentを
  custom MIMEとmarker付き`text/plain`へ保存します。
- `bd_util.maya.ui`のscalar value transferは、Mayaのbool・number・distance・angle・enum・stringを
  型付きsnapshotへ取得し、別nodeの同じ正式属性pathまたは明示した複数pathへ適用します。

## 基本的な使用方法

```python
from bd_util.maya.node.inspection import inspect_scalar_attributes
from bd_util.maya.ui import (
    MayaScalarValueClipboard,
    MayaScalarValueTransfer,
    apply_scalar_value_transfer,
    apply_scalar_value_transfer_to_paths,
    capture_all_scalar_node_values,
    capture_scalar_node_values,
)

attributes = tuple(
    attribute
    for attribute in inspect_scalar_attributes("source")
    if attribute.path in {"translate.translateX", "visibility"}
)
transfer = MayaScalarValueTransfer(
    (capture_scalar_node_values("source", attributes),)
)

clipboard = MayaScalarValueClipboard()
clipboard.write(transfer)

result = apply_scalar_value_transfer(
    ("targetA", "targetB"),
    clipboard.read(),
)
print(result.changed, result.eligible_count, result.excluded)
```

node全体をコピーする場合は、表示状態やtool側の行選択に依存しない
`capture_all_scalar_node_values("source")`を使用します。このAPIが対象にする「全属性」は、
`inspect_scalar_attributes()`で扱えるbool・number・distance・angle・enum・stringです。

取得はsceneとUndo履歴を変更しません。distanceはcm、angleはdegree、通常数値は単位なしの
公開単位で保存するため、コピー元と貼り付け先のMayaで表示単位が異なっても同じ実値を運べます。
表示文字列へ丸めず、boolとenumも数値へ暗黙変換しません。

enumは整数値、項目名、表示順を保存します。貼り付け先では整数値と項目名の対応を比較し、
表示順だけの違いを許容します。コピーした整数値が定義にないdataは読込時に拒否します。
stringは単一のtyped string属性だけを対象とし、空文字・Unicode・前後の空白を
そのまま保存します。NULを含む値は読込時に拒否します。

## 貼り付け規則

`apply_scalar_value_transfer()`は行位置や表示名を使いません。各対象nodeを列挙し、
正式な相対属性pathと`ScalarAttributeKind`が一致する属性だけを候補にします。

`apply_scalar_value_transfer_to_paths()`は、複数値を含むtransferから明示した正式pathとの
共通部分だけを選び、全target nodeの同じpathへ適用します。指定pathがtransferにない場合は
`excluded`へ「コピーされた値なし」として返し、別pathの値へ暗黙に対応させません。

`apply_scalar_value_to_paths()`は、一つのコピー元nodeに一つの属性値だけを持つtransferと、
貼り付け先の正式pathを受け取ります。コピー元pathの代わりに指定pathへ同じ値を展開し、
全target nodeへ適用します。number・distance・angle・bool・stringは同じkind同士、enumは整数値と
項目名の定義が一致する場合だけ候補にします。空・重複pathや複数の搬送値は書込み前に拒否します。

三つの貼り付けAPIには`key_animated=True`を指定できます。通常の時間駆動カーブへ
直接接続された数値・bool・enum属性では、変更時にAuto KeyのON／OFFにかかわらず
現在時刻のキーを追加または更新します。
接続のない属性は従来どおり値を書き込みます。既定の`False`ではキー付き属性は
読取り専用です。Layer・Driven Key・その他の入力接続は対象外として理由を返します。
同値ならキーを追加せず、複数対象の変更は一回のUndoへまとめます。

Maya標準の値入力へ合わせる場合は、代わりに`edit_connected=True`を指定します。
通常の時間カーブとAnimation LayerはAuto Keyに連動し、OFFでは一時値を変更、
ONでは現在時刻のキーを追加・更新します。SDKも一時値を変更できますが、
SDKのキーは更新しません。未接続属性へAuto Keyで新しいカーブを作ることはありません。
constraintを含む駆動、pairBlend、unitConversion、mute、Time Editor、expressionや
その他の接続は対象外です。stringは従来どおり入力接続を許可しません。
Layerの編集先・合成後の出力はMayaの選択状態、ロック、ウェイト等に従います。
詳細は[接続属性への入力](plugs_binding.md#maya標準に合わせた接続属性への入力)を参照してください。

`edit_connected`の既定値は`False`で、既存の貼り付け規則は維持します。
`key_animated`との同時`True`は、貼り付け先に対応属性がない場合も`ValueError`です。
`bdChannelBox`のPasteは`edit_connected=True`を使用し、通常入力と規則を揃えます。
既存APIをこの動作へ移す場合は`key_animated=True`を`edit_connected=True`へ置き換えます。
clipboard schema、scene、保存設定の移行は不要です。

表示状態で正式pathを絞り込む場合は、`bd_util.maya.node`の
`filter_scalar_attribute_paths()`を使用します。`all`、`visible`、`keyable`、
`channel_box`、`hidden`を受け取り、Keyableを優先する共通分類で入力順のpathを返します。
この処理はclipboardを変更しないため、Copyした同じtransferをPaste時の条件ごとに再利用できます。

- 属性なし、型・単位違い、enum定義違い、lock・入力接続などのreadonly属性は
  `MayaScalarPasteResult.excluded`へ理由を返します。
- 候補は既存の`apply_plugs_values()`へまとめ、hard limitを含む全件検証後に一回のUndoで
  書き込みます。途中で失敗した場合は変更済みの値とAuto Keyのキー変更を復旧します。
- 全候補が同値なら`changed`は`False`となり、Undo項目を作りません。
- 適用APIは一つのコピー元nodeを受け付け、複数sourceを拒否します。transfer形式の`nodes`は
  tupleですが、複数sourceを順番や表示位置で暗黙に対応させません。

`tests/maya/ui/test_connected_value_transfer.py`では、三つのAPIから通常値・時間キー・
SDK・Animation Layerへ同時に貼り付け、Auto Key ON／OFFでのキー内容と一回Undoを
検証します。constraint・一般接続・unitConversionの除外と、stringや空path経路での
入力方針の競合も検証します。既存の型・単位・schema・対象照合は
`tests/maya/ui/test_scalar_value_transfer.py`、公開型は
`tests/typecheck/scalar_value_transfer_contract.py`で検証します。

## OSクリップボード形式

`MayaScalarValueClipboard`は次の識別子を使用します。

- custom MIME: `application/vnd.bakedanuki.maya-scalar-values+json`
- text marker: `BAKEDANUKI_MAYA_SCALAR_VALUES/1\n`
- document format: `bd_util.maya.scalar_values`
- schema version: 書込みは`2`、読込みは`1`と`2`

custom MIMEとmarker付きtextには同じUTF-8 JSONを保存します。custom MIMEを維持するQt process間は
その値を優先し、OSやアプリケーションがcustom MIMEを落としてもtextから復元できます。
読込時は1 MiBの上限、UTF-8、標準JSON、重複key、有限数、未知key、件数・文字列長、
path形式、kindと値の対応を検証します。未対応versionを現在versionとして解釈しません。
version 1の既存データは従来の型だけを受け付け、stringはversion 2で搬送します。

`JsonClipboard`を別用途で使う場合は、利用側ごとに固有の`application/...` MIMEと、改行で終わる
markerを指定してください。schemaの内容とversion判定は利用側が所有します。
