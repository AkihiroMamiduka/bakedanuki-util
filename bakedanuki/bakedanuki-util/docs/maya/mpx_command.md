# MPxCommand

`MPxCommandBase`は、再利用可能なPython処理をMayaのcommandとundo queueへ接続する
API 2.0専用基盤です。Maya 2025以降を対象とし、API 1.0の
`maya.OpenMayaMPx.MPxCommand`とは混在させません。

## 役割

推奨する呼び出し経路は次の通りです。

```text
型付きPython facade
    -> maya.cmdsの登録command
        -> MPxCommandBase.execute()
            -> 再利用可能なoperation関数
                -> Nodes / ModifierManager
```

各層の責務を分けます。

- operation
  - ノード作成、値設定、接続など、再利用するscene処理です。
  - 呼び出し側から`Nodes`を受け取り、同じ`ModifierManager`へ操作を積みます。
  - command名、flag、`MArgDatabase`、plug-inのロードを知りません。
- MPxCommand adapter
  - Mayaの引数を型付きparameterへ変換し、operationを組み合わせます。
  - `do_it_dg()` / `do_it_dag()`の実行境界と結果のserializeを担当します。
- 型付きPython facade
  - 必要なplug-inをロードし、動的な`maya.cmds` commandを呼びます。
  - 公開引数と戻り値に静的な型を与え、Mayaのraw結果を正規化します。
- plug-in entry
  - commandの登録と解除だけを担当します。

## 基本実装

parameterはimmutableな`dataclass`などで表し、Maya固有の引数表現をoperationへ
持ち込みません。

```python
from dataclasses import dataclass

import bd_util as bdu


@dataclass(frozen=True, slots=True)
class CreateTransformsParams:
    prefix: str = "sample"
    count: int = 2


def queue_create_transforms(
    nodes: bdu.Nodes,
    params: CreateTransformsParams,
):
    return tuple(
        nodes.create.transform(name=f"{params.prefix}{index + 1}")
        for index in range(params.count)
    )
```

operation内では新しい`ModifierManager`を作成しません。`set_direct()`、sceneを変更する
`maya.cmds`、個別に作成したmodifierの直接実行も避けます。それらはcommandが所有する
履歴から見えないため、undoと失敗時rollbackの対象になりません。

読み取り専用の照会は必要に応じて使用できますが、scene編集は共有managerを通します。

### MPxCommand adapter

```python
from maya.api import OpenMaya as om

import bd_util as bdu


class CreateTransformsCommand(
    bdu.MPxCommandBase[CreateTransformsParams]
):
    COMMAND_NAME = "sampleCreateTransforms"

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        syntax = om.MSyntax()
        syntax.addFlag("-p", "-prefix", om.MSyntax.kString)
        syntax.addFlag("-c", "-count", om.MSyntax.kLong)
        return syntax

    def parse_arguments(
        self,
        arg_database: om.MArgDatabase,
    ) -> CreateTransformsParams:
        prefix = "sample"
        if arg_database.isFlagSet("-prefix"):
            prefix = arg_database.flagArgumentString("-prefix", 0)

        count = 2
        if arg_database.isFlagSet("-count"):
            count = arg_database.flagArgumentInt("-count", 0)

        return CreateTransformsParams(prefix=prefix, count=count)

    def execute(
        self,
        params: CreateTransformsParams,
    ) -> bdu.CommandResult:
        transforms = queue_create_transforms(self.nodes, params)
        self.modifier_manager.do_it_dag()
        return [transform.name for transform in transforms]
```

`execute()`は処理本体をすべて記述する場所ではなく、commandとしてのworkflowを
組み立てる場所です。ただし、一行にする必要はありません。複数operationの順序、
中間評価、DG / DAGの実行境界、結果の組み立ては`execute()`の責務です。

基盤はpending modifierを自動実行しません。未実行操作を読む必要があるworkflowでは、
依存する処理の間に`do_it_dg()` / `do_it_dag()`を明示します。operation側で中間実行が
不可欠な場合も、渡された`nodes.modifier_manager`を使い、その事実をoperationの契約へ
記載します。

## lifecycleとrollback

`MPxCommandBase`が次を固定します。

- `doIt()`
  - `MArgDatabase`の生成、`parse_arguments()`、`execute()`、`setResult()`を順に実行します。
  - 成功後に実行済みmodifier履歴がある場合だけundoableになります。
- `undoIt()`
  - 共有`ModifierManager`の履歴を逆順にundoします。
- `redoIt()`
  - undo済み履歴を元の順序で再実行します。`execute()`は再実行しません。
- `isUndoable()`
  - 初回実行が成功し、managerに実行済み履歴がある場合だけ`True`を返します。

照会やno-op commandはmodifier履歴を作らないため、Mayaのundo queueへ入りません。

`execute()`または結果設定が例外を送出すると、基盤は`ModifierManager.rollback()`を
呼びます。rollbackは実行済みmodifierを逆順にundoし、未実行modifier、done stack、
redo stackをすべて破棄します。rollback自体でも失敗した場合は、元の例外へその情報を
noteとして追加します。

この保証は共有`ModifierManager`を通った変更だけに適用されます。operationが独自managerや
直接編集を使うとrollbackできません。

## operationを直接使う場合

operationはMPxCommandがなくても利用できます。

```python
import bd_util as bdu

mod = bdu.ModifierManager()
nodes = bdu.Nodes(modifier_manager=mod)

transforms = queue_create_transforms(
    nodes,
    CreateTransformsParams(prefix="direct", count=2),
)
mod.do_it_dag()
```

この場合、保持している`mod`から`undo_it()` / `redo_it()`はできますが、実行自体は
Mayaのグローバルundo queueへ一つのcommandとして登録されません。UI、Shelf、menuなど
利用者の操作としてCtrl+Zへ参加させる場合は、型付きfacadeからMPxCommandを呼びます。

すべてのhelperをMPxCommand化する必要はありません。利用者にとって独立したundo単位だけを
commandにし、一つのcommandから複数operationを組み合わせます。command内部から別の
custom commandを`maya.cmds`経由で呼ぶとundo単位が入れ子になるため、共通operationを
直接共有します。

## commandの登録

plug-in entryはAPI 2.0の利用を宣言し、登録だけを行います。MayaがPythonファイルを
plug-inとして直接ロードするため、entry file内ではpackageの絶対importを使用します。

```python
from maya.api import OpenMaya as om

from my_package.mpx_commands import CreateTransformsCommand
from bd_util.maya.mpx_cmd import (
    deregister_commands,
    register_commands,
)

COMMAND_TYPES = (CreateTransformsCommand,)


def maya_useNewAPI() -> None:
    return None


def initializePlugin(plugin: om.MObject) -> None:
    register_commands(plugin, COMMAND_TYPES)


def uninitializePlugin(plugin: om.MObject) -> None:
    deregister_commands(plugin, COMMAND_TYPES)
```

`register_commands()`は途中のcommand登録に失敗すると、それまでに登録したcommandを
逆順に解除します。`deregister_commands()`も逆順で全commandの解除を試み、一つの解除に
失敗しても残りを続行します。

旧`LoaderBase`とcommand class単位の登録methodは公開しません。plug-inの場所とロード時期は
配布packageごとに異なるため、型付きfacadeが自身のplug-inを遅延ロードします。plug-inの
importだけでMayaの状態を変更しないようにします。

## 型付きfacade

登録したcommandは`cmds.sampleCreateTransforms()`として実行できますが、Maya標準の
`maya.cmds` stubには存在せず、plug-inをロードするまでruntimeにも存在しません。
`maya.cmds`のglobal stubは変更せず、公開Python APIに型付きfacadeを用意します。

```python
from dataclasses import dataclass
from typing import Protocol, cast

from maya import cmds


@dataclass(frozen=True, slots=True)
class CreateTransformsResult:
    node_names: tuple[str, ...]


class _CreateTransformsCallable(Protocol):
    def __call__(
        self,
        *,
        prefix: str,
        count: int,
    ) -> object: ...


def create_transforms(
    *,
    prefix: str = "sample",
    count: int = 2,
) -> CreateTransformsResult:
    ensure_commands_plugin_loaded()

    command = cast(
        _CreateTransformsCallable,
        getattr(cmds, CreateTransformsCommand.COMMAND_NAME),
    )
    raw_result = command(prefix=prefix, count=count)
    return decode_create_transforms_result(raw_result)
```

`getattr()`と`cast()`は動的な`maya.cmds`との境界だけに閉じ込めます。利用者は型付き関数を
通じて引数補完と戻り値追跡を利用できます。facadeからoperationを直接呼ばず、登録commandを
必ず経由することでMayaのundo queueを維持します。

`MPxCommand.setResult()`で扱う公開`CommandResult`は、次のMaya command結果に限定します。

- `bool` / `int` / `float` / `str`
- `list[int]` / `list[float]` / `list[str]`

Mayaのcommand層ではrichなPython objectを直接返しません。node名などの安定したprimitiveへ
serializeし、facadeで`dataclass`などへ復元します。Maya versionや要素数によってscalarと
一要素listの表現差があり得るため、raw結果の検証と正規化もfacadeの責務です。

query / edit modeで戻り値型が異なる場合は、単純な差ならfacadeへ`overload`を定義できます。
用途と戻り値が大きく異なる場合は、別の型付き関数へ分ける方を優先します。

## sample

実装例は`python/bd_util/_sample/maya/mpx_cmd`にあります。

- `create_transforms/`
  - transformを作成するサンプルです。
- `set_transform_translation/`
  - 既存transformのlocal translationを変更するサンプルです。
- 各command packageの`operation.py`
  - parameter、result、再利用可能なoperationです。
- 各command packageの`mpx_command.py`
  - 引数解析とworkflowを担当するMPxCommand adapterです。
- 各command packageの`facade.py`
  - 動的command呼び出しと結果変換を行う型付きfacadeです。
- `_plugin.py`
  - 両方のfacadeで共有する`bdUtilSampleCommands.py`の遅延ロード処理です。
- `plug-ins/maya2025|maya2026|maya2027/bdUtilSampleCommands.py`
  - 対応Maya versionのplug-in pathに配置する薄いentryです。API 2.0宣言と
    2つのcommand登録だけを行います。

```python
from bd_util._sample.maya.mpx_cmd import create_transforms

result = create_transforms(prefix="sample", count=3)
print(result.node_names)
```

同じplug-inへ登録された2つ目のcommandも、型付きfacadeから呼び出せます。translationの
単位はcentimeterです。

```python
from bd_util._sample.maya.mpx_cmd import set_transform_translation

result = set_transform_translation(
    node_name="sample1",
    translation=(1.0, 2.0, 3.0),
)
print(result.node_name)
print(result.translation)
```

facadeは`bdUtilSampleCommands.py`をファイル名でロードするため、Maya Moduleとして
導入済みであればsource checkoutの絶対pathを渡す必要はありません。読み込まれるentryは、
実行中のMaya versionに対応する`plug-ins/maya20xx`以下のファイルです。

sampleは設計確認用です。実際の公開commandは、そのcommandを所有するpackageの
command単位package、共有plug-in loader、version別`plug-ins`へ同じ責務で配置します。
