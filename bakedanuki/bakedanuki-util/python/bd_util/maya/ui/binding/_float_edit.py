# coding: utf-8
from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from typing import Callable, ClassVar, cast
from weakref import ref

from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ....ui import FloatViewModel, IntViewModel, qt


class FloatEditUndo:
    """float・整数のMaya連続編集を共通の遅延開始Undoで管理する。"""

    _active: ClassVar[FloatEditUndo | None] = None

    def __init__(self, view_model: FloatViewModel | IntViewModel) -> None:
        """Qt objectの破棄中でも終了できるPython状態を保持する。"""
        self._view_model = ref(view_model)
        self._chunk_name = (
            "IntSlider"
            if isinstance(view_model, IntViewModel)
            else "FloatSlider"
        )
        self._opened = False
        self._write_depth = 0
        self._finish_pending = False
        self._time_callback: int | None = None
        self._edit_time: om.MTime | None = None
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = [
            view_model.edit_started.connect(self._begin_edit),
            view_model.edit_finished.connect(self.finish),
            view_model.destroyed.connect(self.dispose),
        ]

    def _begin_edit(self) -> None:
        """Maya連携の操作中だけ、開始時刻からの移動を監視する。"""
        if self._time_callback is None:
            self._edit_time = oma.MAnimControl.currentTime()
            self._time_callback = int(
                om.MEventMessage.addEventCallback(
                    "timeChanged", self._on_time_changed
                )
            )

    def _on_time_changed(self, *_args: object) -> None:
        """時刻移動で旧操作を終了し、同時刻の再評価では継続する。"""
        if self._edit_time == oma.MAnimControl.currentTime():
            return
        view_model = self._view_model()
        if view_model is not None and not view_model.is_disposed:
            view_model.end_edit()
        else:
            self.finish()

    @contextmanager
    def write(self) -> Generator[None, None, None]:
        """最初の実書き込みで開始し、書き込み途中の終了要求は遅延する。"""
        view_model = self._view_model()
        if view_model is None or not view_model.is_editing:
            FloatEditUndo.finish_active()
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
                cmds.undoInfo(openChunk=True, chunkName=self._chunk_name)
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
        if self._time_callback is not None:
            om.MMessage.removeCallback(self._time_callback)
            self._time_callback = None
            self._edit_time = None
        if self._opened:
            cmds.undoInfo(closeChunk=True)
            self._opened = False
        if FloatEditUndo._active is self:
            FloatEditUndo._active = None

    @classmethod
    def finish_active(cls) -> None:
        """別の一括入力を既存のドラッグ履歴へ混入させず終了する。"""
        active = cls._active
        if active is None:
            return
        if active._write_depth:
            raise RuntimeError("連続編集中のMaya書き込みへ再入できません")
        active.finish()
        view_model = active._view_model()
        if view_model is not None and not view_model.is_disposed:
            view_model.end_edit()

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
