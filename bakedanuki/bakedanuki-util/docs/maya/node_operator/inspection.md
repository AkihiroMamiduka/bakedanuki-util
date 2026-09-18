# 選択nodeとscalar属性の調査

`bd_util.maya.node.inspection`は、sceneのnode、値、選択、Undo履歴を変更せずに
値編集UI向けの情報を取得します。

```python
from bd_util.maya.node.inspection import (
    inspect_scalar_attributes,
    selected_node_names,
)

for node_name in selected_node_names():
    for info in inspect_scalar_attributes(node_name):
        if info.keyable or info.channel_box:
            print(info.path, info.nice_name, info.kind)
```

`selected_node_names()`は現在のMaya active selection listの順を保ちます。
DAGはフルpath、DGはnode名を返し、componentとplugの選択は除外します。
同じnodeの複数DAG instanceは最初のpathだけを返します。選択順trackingの設定は
変更しないため、クリックした履歴の順とは限りません。

`inspect_scalar_attributes()`はMayaの属性定義順に`ScalarAttributeInfo`のtupleを
返します。bool、float/double、距離、角度、enumのscalarを扱い、compoundの子も
含めます。配列自身と配列配下、整数、time、文字列等は含めません。

`ScalarAttributeInfo`は変更不能で、`name`（長名）、`path`（長名の完全な相対属性
path）、`nice_name`、`kind`、`keyable`、`channel_box`を持ちます。`kind`は
`bool`、`number`、`distance`、`angle`、`enum`のいずれかです。表示フラグによる除外、表示順の
並べ替え、複数nodeの同名対応は利用側が決めます。

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
