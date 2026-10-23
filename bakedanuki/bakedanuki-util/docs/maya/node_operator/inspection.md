# 選択nodeとscalar属性の調査

`bd_util.maya.node.inspection`は、sceneのnode、値、選択、Undo履歴を変更せずに
値編集UI向けの情報を取得します。

```python
from bd_util.maya.node.inspection import (
    inspect_scalar_attributes,
    node_display_name,
    selected_node_names,
)

for node_name in selected_node_names():
    print(node_display_name(node_name))
    for info in inspect_scalar_attributes(node_name):
        if info.keyable or info.channel_box:
            print(info.path, info.nice_name, info.kind)
```

`selected_node_names()`は現在のMaya active selection listの順を保ちます。
DAGはフルpath、DGはnode名を返し、componentとplugの選択は除外します。
同じnodeの複数DAG instanceは最初のpathだけを返します。選択順trackingの設定は
変更しないため、クリックした履歴の順とは限りません。
`selected_node_names(limit=50)`のように上限を指定すると、対象ノードをその数だけ
見つけた時点で走査を終えます。componentとplugは数えず、DAG instanceは同じnodeとして
まとめます。省略時は選択全体を返します。

`node_display_name(node_name)`は一意に解決できる既存ノードのUI表示名を返します。
DAGでは名前とパスが一意ならnamespaceを含む短名、同名ノードがある場合と
インスタンスで複数パスを持つ場合は指定したフルパスを返します。DGではノード名を
返します。表示名は操作対象の識別子として使わず、元の`node_name`を保持してください。
同名・インスタンスの状態は呼び出し時点で再判定します。

`inspect_scalar_attributes()`はMayaの属性定義順に`ScalarAttributeInfo`のtupleを
返します。bool、byte・short・long、float/double、距離、角度、enum、typed stringのscalarを
扱い、compoundの子も含めます。配列自身と配列配下、time、matrix等は含めません。

`ScalarAttributeInfo`は変更不能で、`name`（長名）、`path`（長名の完全な相対属性
path）、`nice_name`、`kind`、`keyable`、`channel_box`を持ちます。`kind`は
`bool`、`byte`、`short`、`long`、`number`、`distance`、`angle`、`enum`、`string`のいずれかです。表示フラグによる除外、表示順の
並べ替え、複数nodeの同名対応は利用側が決めます。

`inspect_scalar_attributes_by_type(node_type)`は、ノードを作成せずに登録済みノード型の
標準属性を調べ、同じ`ScalarAttributeInfo`のtupleを返します。抽象型も指定できます。
対応値種別と配列配下の除外は既存ノードの調査と共通です。keyableとchannel_boxは
型の既定フラグであり、個別ノードの変更や追加属性を含みません。返却順は型の属性定義順です。
未登録型と空文字列は`ValueError`、文字列以外は`TypeError`になります。

MayaのChannel Boxに対応する表示条件は`keyable or channel_box`です。親compoundが
非表示でも子はkeyableにできるため、親のフラグで子を除外しません。

`resolve_bool_plug()`と`resolve_float_plug()`は`info.path`を受け取れます。
enumには`resolve_enum_plug()`を使用します。`bd_util.maya.ui.read_enum_definition(plug)`で
callbackを作らず実定義を取得し、`EnumDefinition.matches()`で整数値と項目名の対応を
比較できます。表示順だけの違いは一致とみなします。
従来の長名・短名も使えますが、同じleaf名が複数ある場合は`ValueError`となるため、
完全な相対pathを渡してください。boolのcompound子は親のlock、入力接続、削除へ
追従し、書き込みできない状態ではCommandを無効にします。

非一意な最上位属性の`path`は`.envelope`のように先頭がdotとなり、`kitA.envelope`
のような同名の子属性と区別します。このpathもそのままresolverへ渡せます。

名前が一意な属性はMaya APIから直接取得し、長名・短名と指定された親pathを検証します。
非一意な属性など直接確定できない場合は全属性を検索し、曖昧なleaf名を拒否します。
aliasは受理しません。検索結果をキャッシュしないため、属性の追加・削除・改名後も
呼出し時点の構成を読み取ります。
