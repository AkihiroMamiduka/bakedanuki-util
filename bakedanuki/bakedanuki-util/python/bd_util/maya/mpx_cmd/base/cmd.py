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
    """Base class for undoable API 2.0 Maya commands.

    Subclasses parse Maya command arguments into a typed parameter object and
    implement ``execute()`` as the command workflow. Scene edits must be queued
    and executed through this instance's ``modifier_manager`` so the base can
    provide undo, redo, and failure rollback.
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
        return self._modifier_manager

    @property
    def nodes(self) -> Nodes:
        return self._nodes

    @classmethod
    def creator(cls) -> MPxCommandBase[ParamsT]:
        """Return an API 2.0 command instance for ``registerCommand``."""
        return cls()

    @classmethod
    def create_syntax(cls) -> om.MSyntax:
        """Create the Maya command syntax.

        Commands without arguments can use the default empty syntax.
        """
        return om.MSyntax()

    @abstractmethod
    def parse_arguments(self, arg_database: om.MArgDatabase) -> ParamsT:
        """Convert Maya arguments into the command's typed parameters."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, params: ParamsT) -> CommandResult | None:
        """Execute the initial command workflow and optionally return a result.

        Implementations explicitly choose their ``do_it_dg()`` and
        ``do_it_dag()`` boundaries. The base does not auto-execute pending
        modifiers because workflows may require intermediate Maya evaluation.
        """
        raise NotImplementedError

    def doIt(self, args: om.MArgList) -> None:
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
        if not self._is_undoable:
            raise RuntimeError(
                "This command has no executed modifier history."
            )
        self._modifier_manager.undo_it()

    def redoIt(self) -> None:
        if not self._is_undoable:
            raise RuntimeError(
                "This command has no executed modifier history."
            )
        self._modifier_manager.redo_it()

    def isUndoable(self) -> bool:
        return self._is_undoable
