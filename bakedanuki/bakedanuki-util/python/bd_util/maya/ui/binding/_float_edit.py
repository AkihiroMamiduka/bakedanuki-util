# coding: utf-8
from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import Callable, ClassVar, cast
from weakref import ref

from maya import cmds

from ....ui import FloatViewModel, qt


class FloatEditUndo:
    """連続編集中のMaya書き込みを、遅延開始するUndo chunkへまとめる。"""

    _active: ClassVar[FloatEditUndo | None] = None

    def __init__(self, view_model: FloatViewModel) -> None:
        """Qt objectの破棄中でも終了できるPython状態を保持する。"""
        self._view_model = ref(view_model)
        self._opened = False
        self._write_depth = 0
        self._finish_pending = False
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = [
            view_model.edit_finished.connect(self.finish),
            view_model.destroyed.connect(self.dispose),
        ]

    @contextmanager
    def write(self) -> Generator[None, None, None]:
        """最初の実書き込みで開始し、書き込み途中の終了要求は遅延する。"""
        view_model = self._view_model()
        if (
            view_model is not None
            and view_model.is_editing
            and not self._opened
        ):
            active = FloatEditUndo._active
            if active is not None and active is not self:
                if active._write_depth:
                    raise RuntimeError("別の連続編集のMaya書き込み中です")
                active.finish()
                previous = active._view_model()
                if previous is not None and not previous.is_disposed:
                    previous.end_edit()
            # Maya側でUndoが無効な場合は、設定を変更せず通常の書き込みを行う。
            if cmds.undoInfo(query=True, state=True):
                cmds.undoInfo(openChunk=True, chunkName="FloatSlider")
                self._opened = True
                FloatEditUndo._active = self
        self._write_depth += 1
        try:
            yield
        except Exception:
            self._finish_pending = True
            if view_model is not None and not view_model.is_disposed:
                view_model.end_edit()
            raise
        finally:
            self._write_depth -= 1
            if self._finish_pending:
                self.finish()

    def finish(self) -> None:
        """開いたchunkだけを1回閉じ、無変更の操作では履歴を作らない。"""
        if self._write_depth:
            self._finish_pending = True
            return
        self._finish_pending = False
        if self._opened:
            cmds.undoInfo(closeChunk=True)
            self._opened = False
        if FloatEditUndo._active is self:
            FloatEditUndo._active = None

    def dispose(self) -> None:
        """Maya endpointの終了時に、UndoとViewModelへの接続を解放する。"""
        self.finish()
        disconnect = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QObject, "disconnect"),
        )
        for connection in self._connections:
            if connection is None:
                continue
            try:
                disconnect(connection)
            except (RuntimeError, TypeError):
                pass
        self._connections.clear()
