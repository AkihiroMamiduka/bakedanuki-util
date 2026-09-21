# Maya scalar値のクリップボード搬送

`bd_util`は、tool固有の行選択やメニューから独立した2層のAPIを提供します。

- `bd_util.ui.JsonClipboard`はMayaをimportせず、任意のJSON互換documentを
  custom MIMEとmarker付き`text/plain`へ保存します。
- `bd_util.maya.ui`のscalar value transferは、Mayaのbool・number・distance・angle・enumを
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
`inspect_scalar_attributes()`で扱えるbool・number・distance・angle・enumです。

取得はsceneとUndo履歴を変更しません。distanceはcm、angleはdegree、通常数値は単位なしの
公開単位で保存するため、コピー元と貼り付け先のMayaで表示単位が異なっても同じ実値を運べます。
表示文字列へ丸めず、boolとenumも数値へ暗黙変換しません。

enumは整数値、項目名、表示順を保存します。貼り付け先では整数値と項目名の対応を比較し、
表示順だけの違いを許容します。コピーした整数値が定義にないdataは読込時に拒否します。

## 貼り付け規則

`apply_scalar_value_transfer()`は行位置や表示名を使いません。各対象nodeを列挙し、
正式な相対属性pathと`ScalarAttributeKind`が一致する属性だけを候補にします。

`apply_scalar_value_transfer_to_paths()`は、複数値を含むtransferから明示した正式pathとの
共通部分だけを選び、全target nodeの同じpathへ適用します。指定pathがtransferにない場合は
`excluded`へ「コピーされた値なし」として返し、別pathの値へ暗黙に対応させません。

`apply_scalar_value_to_paths()`は、一つのコピー元nodeに一つの属性値だけを持つtransferと、
貼り付け先の正式pathを受け取ります。コピー元pathの代わりに指定pathへ同じ値を展開し、
全target nodeへ適用します。number・distance・angle・boolは同じkind同士、enumは整数値と
項目名の定義が一致する場合だけ候補にします。空・重複pathや複数の搬送値は書込み前に拒否します。

- 属性なし、型・単位違い、enum定義違い、lock・入力接続などのreadonly属性は
  `MayaScalarPasteResult.excluded`へ理由を返します。
- 候補は既存の`apply_plugs_values()`へまとめ、hard limitを含む全件検証後に一回のUndoで
  書き込みます。途中で失敗した場合は変更済みの値を復旧します。
- 全候補が同値なら`changed`は`False`となり、Undo項目を作りません。
- 現在の適用APIは一つのコピー元nodeを受け付けます。transfer形式は将来の複数source拡張に
  備えて`nodes`をtupleで保持しますが、複数sourceを暗黙に順番対応させません。

## OSクリップボード形式

`MayaScalarValueClipboard`は次の識別子を使用します。

- custom MIME: `application/vnd.bakedanuki.maya-scalar-values+json`
- text marker: `BAKEDANUKI_MAYA_SCALAR_VALUES/1\n`
- document format: `bd_util.maya.scalar_values`
- schema version: `1`

custom MIMEとmarker付きtextには同じUTF-8 JSONを保存します。custom MIMEを維持するQt process間は
その値を優先し、OSやアプリケーションがcustom MIMEを落としてもtextから復元できます。
読込時は1 MiBの上限、UTF-8、標準JSON、重複key、有限数、未知key、件数・文字列長、
path形式、kindと値の対応を検証します。未対応versionを現在versionとして解釈しません。

`JsonClipboard`を別用途で使う場合は、利用側ごとに固有の`application/...` MIMEと、改行で終わる
markerを指定してください。schemaの内容とversion判定は利用側が所有します。
