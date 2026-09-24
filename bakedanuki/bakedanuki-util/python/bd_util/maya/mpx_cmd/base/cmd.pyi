from __future__ import annotations

from abc import abstractmethod
from typing import ClassVar, Generic, Self, TypeAlias, TypeVar

from maya.api import OpenMaya as om

from ...node.modifier import ModifierManager
from ...node.nodes import Nodes

ParamsT = TypeVar("ParamsT")

CommandResult: TypeAlias = (
    bool | int | float | str | list[int] | list[float] | list[str]
)

class MPxCommandBase(om.MPxCommand, Generic[ParamsT]):
    """Maya API 2.0 コマンドの undo 対応基底クラス。

    ``parse_arguments()`` と ``execute()`` を実装する。シーン変更には
    ``modifier_manager`` を使う。
    """

    COMMAND_NAME: ClassVar[str]

    def __new__(cls) -> Self: ...
    def __init__(self) -> None: ...
    @property
    def modifier_manager(self) -> ModifierManager:
        """このコマンドの変更履歴を管理する ``ModifierManager``。"""
        ...

    @property
    def nodes(self) -> Nodes:
        """同じ ``ModifierManager`` を共有するノード操作入口。"""
        ...

    @classmethod
    def creator(cls) -> Self:
        """登録時に使う新しいコマンドインスタンスを作る。"""
        ...

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """Maya コマンドの引数構文を作る。既定では空の構文を返す。"""
        ...

    @abstractmethod
    def parse_arguments(self, arg_database: om.MArgDatabase) -> ParamsT:
        """Maya の引数を ``execute()`` 用のパラメータに変換する。

        Args:
            arg_database: Maya が渡した引数の解析結果。

        Returns:
            ``execute()`` に渡すパラメータ。
        """
        ...

    @abstractmethod
    def execute(self, params: ParamsT) -> CommandResult | None:
        """初回処理を実行する。保留中の変更は自動実行されない。

        Args:
            params: ``parse_arguments()`` が返したパラメータ。

        Returns:
            Maya のコマンド結果。結果が不要なら ``None``。
        """
        ...

    def doIt(self, args: om.MArgList) -> None:
        """初回処理を実行し、失敗時は変更履歴を巻き戻す。"""
        ...

    def undoIt(self) -> None:
        """実行済みの変更履歴を取り消す。"""
        ...

    def redoIt(self) -> None:
        """取り消した変更履歴を再実行する。"""
        ...

    def isUndoable(self) -> bool:
        """実行済みの変更履歴が undo 可能かを返す。"""
        ...
