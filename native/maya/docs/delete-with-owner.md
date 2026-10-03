# `bdDeleteWithOwner`

`bdDeleteWithOwner` は、所有元ノードの削除時に、明示的に登録した DG ノードを
同じ削除操作で片付けるためのノードです。自身を直接削除した場合も登録対象を削除します。
計算用の出力は持ちません。

## 接続

```text
null1.message           -> cleanup.owner
multiplyDivide1.message -> cleanup.deleteTarget[0]
```

`owner` は単一の message 入力です。`deleteTarget` は sparse な message 配列入力で、
各要素の接続元ノードを削除対象にします。接続先からたどる任意の DG ノードや、
シーン内の同型ノードを推測して削除することはありません。

`bd_util` からは次のように接続できます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)
owner = nodes.existing("null1")
target = nodes.existing("multiplyDivide1")
cleanup = nodes.create.bdDeleteWithOwner(name="cleanup")

owner.message.connect(cleanup.owner)
target.message.connect(cleanup.deleteTarget[next])
mod.do_it_dg()
```

`owner` の削除時は管理ノードを削除し、管理ノードの削除時は `deleteTarget` に
登録したノードを削除します。これらの削除は Maya が渡す同じ `MDGModifier` に
積まれるため、Undo / Redo で接続を含めて復元・再削除されます。

`deleteTarget` の接続を外しただけでは接続元を削除しません。対象ノードを個別に
削除しても `owner` や管理ノードは残ります。`owner` の接続を外した場合も
管理ノードは残り、別の `owner` を接続できます。

## 初期版の制約

- `deleteTarget` には編集可能な非 DAG ノードだけを登録します。DAG 階層の削除は
  Maya 標準の階層削除に任せます。
- 同じ対象を複数の `deleteTarget` 要素や複数の管理ノードへ登録しません。
  Maya 2025 の検証では重複削除が Redo を壊したため、接続時に拒否します。
- 参照ノード、ロックされたノード、Maya の既定ノードは登録対象にできません。
  登録後に保護状態が変わった場合、削除時はその対象を残して警告します。
- 同じノードを `owner` と `deleteTarget` の両方に接続することはできません。
- `owner` と対象ノードの接続は、どちらも標準の `.message` 属性から行います。

シーンを開き直した場合も `owner` の接続から削除通知を再登録します。
プラグインが未ロードの状態では、この追加削除動作は利用できません。
