# coding: utf-8
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Generic, TypeVar

from maya.api import OpenMaya as om

from ...node.modifier import ModifierManager
from ...node.nodes import Nodes

ParamsT = TypeVar("ParamsT")

CommandResult = bool | int | float | str | list[int] | list[float] | list[str]


class MPxCommandBase(om.MPxCommand, Generic[ParamsT], ABC):
    """Maya API 2.0 コマンドの undo 対応基底クラス。

    サブクラスは引数を ``parse_arguments()`` で解析し、``execute()`` で処理する。
    シーン変更を ``modifier_manager`` 経由で実行すると、undo・redo と失敗時の
    巻き戻しを利用できる。

    Attributes:
        COMMAND_NAME: Maya に登録するコマンド名。サブクラスで設定する。
    """

    COMMAND_NAME: ClassVar[str] = ""

    def __init__(self) -> None:
        super().__init__()

        self._modifier_manager = ModifierManager()
        self._nodes = Nodes(modifier_manager=self._modifier_manager)
        self._is_undoable = False
        self._has_executed = False

    @property
    def modifier_manager(self) -> ModifierManager:
        """このコマンドの変更履歴を管理する ``ModifierManager``。"""
        return self._modifier_manager

    @property
    def nodes(self) -> Nodes:
        """同じ ``ModifierManager`` を共有するノード操作入口。"""
        return self._nodes

    @classmethod
    def creator(cls) -> MPxCommandBase[ParamsT]:
        """``registerCommand`` に渡す新しいコマンドインスタンスを作る。"""
        return cls()

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """Maya コマンドの引数構文を作る。

        引数がないコマンドでは、空の構文を返す既定実装を使える。
        """
        return om.MSyntax()

    @abstractmethod
    def parse_arguments(self, arg_database: om.MArgDatabase) -> ParamsT:
        """Maya の引数をコマンド固有のパラメータに変換する。

        Args:
            arg_database: Maya が渡した引数の解析結果。

        Returns:
            ``execute()`` に渡すパラメータ。
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self, params: ParamsT) -> CommandResult | None:
        """コマンドの初回処理を実行する。

        ``do_it_dg()`` / ``do_it_dag()`` の実行位置はサブクラスで決める。
        基底クラスは保留中の変更を自動実行しない。

        Args:
            params: ``parse_arguments()`` が返したパラメータ。

        Returns:
            Maya のコマンド結果。結果が不要なら ``None``。
        """
        raise NotImplementedError

    def doIt(self, args: om.MArgList) -> None:
        """引数解析と初回処理を実行し、失敗時は変更履歴を巻き戻す。"""
        if self._has_executed:
            raise RuntimeError("A command instance cannot execute twice.")

        try:
            arg_database = om.MArgDatabase(self.syntax(), args)
            params = self.parse_arguments(arg_database)
            result = self.execute(params)
            if result is not None:
                self.setResult(result)
        except Exception as error:
            try:
                self._modifier_manager.rollback()
            except Exception as rollback_error:
                error.add_note(
                    f"MPxCommand rollback also failed: {rollback_error!r}"
                )
            raise

        self._is_undoable = self._modifier_manager.can_undo
        self._has_executed = True

    def undoIt(self) -> None:
        """実行済みの変更履歴を取り消す。"""
        if not self._is_undoable:
            raise RuntimeError(
                "This command has no executed modifier history."
            )
        self._modifier_manager.undo_it()

    def redoIt(self) -> None:
        """取り消した変更履歴を再実行する。"""
        if not self._is_undoable:
            raise RuntimeError(
                "This command has no executed modifier history."
            )
        self._modifier_manager.redo_it()

    def isUndoable(self) -> bool:
        """実行済みの変更履歴が undo 可能かを返す。"""
        return self._is_undoable
