# ModifierManager

`ModifierManager` は `MDGModifier` と `MDagModifier` をまとめて扱うための管理クラスです。

目的は、複数の DG / DAG 操作を 1 つの作業単位として undo / redo できるようにすることです。

## 基本方針

`MDGModifier` / `MDagModifier` は操作を溜めて `doIt()` で確定する command buffer として扱います。

一度 `doIt()` した modifier は閉じた履歴として保存し、次の操作には新しい modifier を使います。

`ModifierManager` 全体では、それら複数の modifier をまとめて 1 つのコマンド履歴として扱います。

## lifecycle

```mermaid
sequenceDiagram
    participant User
    participant Manager as ModifierManager
    participant Current as Current Modifier
    participant History as Done Stack

    User->>Current: 操作を追加
    User->>Manager: do_it_dg() / do_it_dag()
    Manager->>Current: doIt()
    Manager->>History: executed modifier を保存
    Manager->>Manager: current modifier を新規作成
```

## public API

```python
modifier_manager.dg_mod
modifier_manager.dag_mod
modifier_manager.do_it_dg()
modifier_manager.do_it_dag()
modifier_manager.undo_it()
modifier_manager.redo_it()
modifier_manager.clear()
```

## 使用例

```python
from bd_util.maya.node.modifier import ModifierManager
from bd_util.maya.node.operator.node.dg.plus_minus_average import PlusMinusAverage

modifier_manager = ModifierManager()

node = PlusMinusAverage.create(modifier_manager, name="test_pma")
node.input1D[0].set(1.0)
node.input1D[1].set(2.0)

modifier_manager.do_it_dg()

modifier_manager.undo_it()
modifier_manager.redo_it()
```

## DG / DAG の混在

DG と DAG の操作は 1 つの `ModifierManager` に混在できます。

ただし `MDGModifier` に溜まった操作は `do_it_dg()`、`MDagModifier` に溜まった操作は `do_it_dag()` で確定します。

undo 時は実行済み modifier を逆順に `undoIt()` します。

redo 時は undo 済み modifier を順番に `doIt()` します。

## 未実行の DAG 親関係

DAG `NodeOperator` 経由の作成・親変更では、現在の `MDagModifier` に積まれた
未実行の直接親を `ModifierManager` が内部的に記録します。
現在のシーン階層とこの記録を組み合わせることで、未作成ノードを含む循環した
親変更を `do_it_dag()` より前に拒否します。

この記録は `do_it_dag()` の成功後、または `clear()` で破棄します。

## redo の扱い

`undo_it()` 後、`redo_it()` を呼ぶと履歴を再実行します。

新しい `do_it_dg()` / `do_it_dag()` が実行されると redo stack は破棄されます。

これは一般的な undo / redo と同じ扱いです。

## clear

`clear()` は現在の modifier、done stack、redo stack をすべて初期化します。

テストや一時的な作業単位を破棄したい場合に使います。

## MPxCommand との関係

将来的には MPxCommand の `doIt()` / `undoIt()` / `redoIt()` 内で `ModifierManager` を保持し、各 command が必要な Maya 操作を manager に積む形を想定します。

このとき command 側の `undoIt()` では `modifier_manager.undo_it()`、`redoIt()` では `modifier_manager.redo_it()` を呼ぶだけに近づけるのが狙いです。

## 注意点

- `set_direct()` は `ModifierManager` に積まれません。
- `maya.cmds` や OpenMaya の直接 `doIt()` など、manager 外の操作は manager の undo / redo 対象外です。
- 1 つの command / 1 つの作業単位につき 1 つの `ModifierManager` を使うのが基本です。
