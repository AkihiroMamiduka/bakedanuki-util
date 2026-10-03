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

## 対象と制約

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

## 実装と保守

実装は [BdDeleteWithOwnerNode.cpp](../plugins/bdUtilNodes/src/nodes/BdDeleteWithOwnerNode.cpp)
にあります。`postConstructor()` で自身の `MNodeMessage::addNodeAboutToDeleteCallback()`
を登録し、`owner` の `connectionMade()` / `connectionBroken()` で所有元の削除通知を
登録・解除します。
デストラクタは登録済みの callback ID を解除します。シーンへ保存するのは message
接続であり、callback はシーンの再読込時に接続から再登録されます。

所有元の削除通知では管理ノードの削除を、管理ノードの削除通知では登録対象の削除を、
それぞれ通知に渡された `MDGModifier` へ積みます。この modifier を使うことが
連動削除を同じ Undo / Redo に含める前提です。デストラクタは削除処理に使いません。

`deleteTarget` は logical index が連続するとは限りません。接続中の要素は
`numConnectedElements()` と `connectionByPhysicalIndex()` で列挙します。未評価の
message 配列では `numElements()` だけを頼りにすると接続を見落とす場合があります。
削除直前にも対象の重複と保護状態を確認します。接続先要素の同一性はノード・属性・
logical index をそれぞれ比較します。

回帰テストは [test_bd_delete_with_owner.py](../../../tests/maya/node/operator/node/dg/test_bd_delete_with_owner.py)
にあります。所有元・管理ノードの削除、Undo / Redo、疎な配列、無効な対象、
接続の張り直し、シーンの再読込を確認します。このノードには `compute()` と
計算出力がないため、削除と接続のライフサイクルを検証します。

```powershell
.\scripts\test-pytest-maya2025.cmd tests\maya\node\operator\node\dg\test_bd_delete_with_owner.py
.\scripts\verify.cmd -IncludeNative
```
