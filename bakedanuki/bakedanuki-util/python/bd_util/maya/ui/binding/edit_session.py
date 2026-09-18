# coding: utf-8
"""複数の入力先にまたがる連続編集を一つのMaya Undoへまとめる。"""

from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import ClassVar

from maya import cmds

from ....ui import qt
from ._float_edit import FloatEditUndo

__all__ = ["MayaEditSession"]


class MayaEditSession(qt.QObject):
    """実書込みまでUndoを開かず、終了要求を内側の書込み後へ延期する。"""

    finished = qt.Signal()
    _active: ClassVar[MayaEditSession | None] = None

    def __init__(
        self, parent: qt.QObject, *, chunk_name: str = "ContinuousEdit"
    ) -> None:
        """所有者の破棄時にも終了できる編集状態を保持する。"""
        super().__init__(parent)
        self._chunk_name = chunk_name
        self._editing = False
        self._opened = False
        self._write_depth = 0
        self._finish_pending = False
        self._disposed = False
        self.destroyed.connect(self.dispose)
        parent.destroyed.connect(self.dispose)

    @property
    def is_editing(self) -> bool:
        """終了要求後の追加書込みを許可しない編集状態を返す。"""
        return self._editing and not self._finish_pending

    def begin(self) -> None:
        """前の連続編集を終了し、Undoをまだ開かずに入力を開始する。"""
        if self._disposed:
            raise RuntimeError("終了済みの編集セッションです")
        if self._write_depth:
            raise RuntimeError("書込み中に編集を開始できません")
        if self.is_editing:
            return
        FloatEditUndo.finish_active()
        active = MayaEditSession._active
        if active is not None and active is not self:
            if active._write_depth:
                raise RuntimeError("別の連続編集へ書込み中です")
            active.finish()
        self._editing = True
        MayaEditSession._active = self

    @contextmanager
    def write(self) -> Generator[None, None, None]:
        """差分がある書込みだけを囲み、内側のchunkより後に終了する。"""
        if not self.is_editing or self._disposed:
            raise RuntimeError("編集セッションが開始されていません")
        if not self._opened and cmds.undoInfo(query=True, state=True):
            cmds.undoInfo(openChunk=True, chunkName=self._chunk_name)
            self._opened = True
        self._write_depth += 1
        try:
            yield
        except Exception:
            self._finish_pending = True
            raise
        finally:
            self._write_depth -= 1
            if self._finish_pending:
                self.finish()

    def finish(self) -> None:
        """操作を確定し、書込み中なら最外のwrite終了まで閉じるのを待つ。"""
        if self._write_depth:
            self._finish_pending = True
            return
        editing = self._editing
        if self._opened:
            cmds.undoInfo(closeChunk=True)
            self._opened = False
        self._editing = False
        self._finish_pending = False
        if MayaEditSession._active is self:
            MayaEditSession._active = None
        if editing and qt.isValid(self):
            self.finished.emit()

    def dispose(self) -> None:
        """所有者の終了後は再開を禁止し、開いているUndoを確定する。"""
        self._disposed = True
        self.finish()
