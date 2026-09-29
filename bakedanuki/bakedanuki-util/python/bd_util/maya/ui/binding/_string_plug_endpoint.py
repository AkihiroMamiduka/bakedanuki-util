# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Protocol, cast
from weakref import ReferenceType, ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import StringViewModel, qt
from ....ui.binding.string._connection import (
    connect_queued_qt_signal,
    disconnect_qt_connection,
)
from ....ui.binding.string._validation import require_string
from ..callback import MayaCallbackRegistry
from .string_plug_resolver import MayaStringPlug, require_string_plug


class _SetStringAttr(Protocol):
    """Maya command stubの可変引数をstring書込みに限定する。"""

    def __call__(self, name: str, value: str, *, type: str) -> None:
        """string型の属性へ書き込む。"""
        raise NotImplementedError


class _QTimerType(Protocol):
    """PySide stub差分を越えて遅延実行する型境界。"""

    @staticmethod
    def singleShot(milliseconds: int, callback: Callable[[], None]) -> None:
        """次のevent loopでcallbackを実行する。"""
        raise NotImplementedError


def _run_later(callback: Callable[[], None]) -> None:
    """Maya callbackの外で値を確定する。"""
    cast(_QTimerType, qt.QtCore.QTimer).singleShot(0, callback)


class StringPlugEndpoint(qt.QObject):
    """単一string plugのアクセス・監視・寿命をStoreとViewへ提供する。"""

    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = False

    def __init__(
        self,
        view_model: StringViewModel,
        plug: MayaStringPlug,
        owner: qt.QObject,
    ) -> None:
        """既存plugとViewModelを接続し、Maya callbackを登録する。"""
        plug = require_string_plug(plug)
        super().__init__(owner)
        self._view_model: StringViewModel | None = view_model
        self._view_model_ref: ReferenceType[StringViewModel] = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._node_handle = om.MObjectHandle(self._plug.node())
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._watched_plugs = [self._plug]
        while self._watched_plugs[-1].isChild:
            self._watched_plugs.append(self._watched_plugs[-1].parent())
        self._node_was_removed = False
        self._refresh_scheduled = False
        self._is_disposed = False
        self._registry = MayaCallbackRegistry(
            owner, on_maya_exiting=self.dispose
        )
        self._view_model_disposed_connection = view_model.disposed.connect(
            self.dispose
        )
        self._view_model_destroyed_connection = connect_queued_qt_signal(
            view_model.destroyed, self.dispose
        )
        try:
            self._register_callbacks()
        except Exception:
            self.dispose()
            raise

    @property
    def view_model(self) -> StringViewModel:
        """同期中のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のStringViewModelは終了しています")
        return view_model

    @property
    def plug_operator(self) -> MayaStringPlug:
        """対象の型付きPlugOperatorを返す。"""
        return self._plug_operator

    @property
    def is_available(self) -> bool:
        """nodeと属性の実体が利用可能なら`True`。"""
        return (
            not self.is_disposed
            and not self._node_was_removed
            and self._node_handle.isValid()
            and self._attribute_handle.isValid()
        )

    @property
    def is_writable(self) -> bool:
        """Maya標準の書込みを受け付ける場合は`True`。"""
        if not self.is_available:
            return False
        try:
            return (
                om.MFnAttribute(self._plug.attribute()).writable
                and not any(plug.isLocked for plug in self._watched_plugs)
                and not any(plug.isDestination for plug in self._watched_plugs)
                and self._plug.isFreeToChange(True, False)
                == om.MPlug.kFreeToChange
            )
        except RuntimeError:
            return False

    @property
    def is_disposed(self) -> bool:
        """callbackを解除済みか返す。"""
        return (
            self._is_disposed
            or self._registry.is_disposed
            or not qt.isValid(self)
        )

    def dispose(self, *_args: object) -> None:
        """callbackを即座に解除し、ViewModelとの接続を終了する。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        self._refresh_scheduled = False
        disconnect_qt_connection(self._view_model_disposed_connection)
        disconnect_qt_connection(self._view_model_destroyed_connection)
        self._registry.dispose()
        try:
            self._on_endpoint_unavailable()
        finally:
            self._view_model = None

    def _valid_view_model(self) -> StringViewModel | None:
        """Python参照とQt実体の両方が生存するViewModelを返す。"""
        view_model = self._view_model or self._view_model_ref()
        if view_model is None or not qt.isValid(view_model):
            return None
        return view_model

    def _read_plug(self) -> str:
        """未設定値を空文字としてMaya実値を読む。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya string plugは利用できません")
        return cast(str, self._plug.asString())

    def _write_plug(self, value: str) -> str:
        """Maya Undoに載るsetAttrで文字列を確定する。"""
        value = require_string(value)
        if "\x00" in value:
            raise ValueError("Maya string属性へNUL文字は書き込めません")
        if not self.is_writable:
            raise RuntimeError("同期対象のMaya string plugへ書き込めません")
        if self._read_plug() != value:
            cast(_SetStringAttr, cmds.setAttr)(
                self._cmds_plug_name(), value, type="string"
            )
        return self._read_plug()

    def _cmds_plug_name(self) -> str:
        """同名DAGでも一意になる完全な属性名を返す。"""
        path = cast(
            str,
            self._plug.partialName(
                includeNodeName=False,
                includeNonMandatoryIndices=True,
                includeInstancedIndices=True,
                useAlias=False,
                useFullAttributePath=True,
                useLongNames=True,
            ),
        )
        return f"{self._plug_operator.node.cmd_access_name}.{path}"

    def _register_callbacks(self) -> None:
        """対象nodeの値・dirty・削除とUndo/Redoを監視する。"""
        node = self._plug.node()
        self._registry.register(
            int(
                om.MNodeMessage.addAttributeChangedCallback(
                    node, self._on_attribute_changed
                )
            )
        )
        self._registry.register(
            int(
                om.MNodeMessage.addNodeDirtyPlugCallback(
                    node, self._on_node_dirty_plug
                )
            )
        )
        self._registry.register(
            int(
                om.MNodeMessage.addNodePreRemovalCallback(
                    node, self._on_node_pre_removal
                )
            )
        )
        for event in ("Undo", "Redo"):
            self._registry.register(
                int(
                    om.MEventMessage.addEventCallback(
                        event, self._on_history_event
                    )
                )
            )

    def _matches_plug(self, plug: om.MPlug) -> bool:
        """通知対象がこの属性またはcompound祖先か返す。"""
        if not self.is_available:
            return False
        try:
            return any(plug == watched for watched in self._watched_plugs)
        except RuntimeError:
            return False

    def _schedule_refresh(self) -> None:
        """dirty通知を次のQt event loopの読込みへまとめる。"""
        if (
            self.is_disposed
            or self._refresh_scheduled
            or self._callbacks_are_suppressed()
        ):
            return
        self._refresh_scheduled = True
        self._on_refresh_scheduled()
        _run_later(self._refresh_after_callback)

    def _refresh_after_callback(self) -> None:
        """Maya callback完了後に現在値を再読込みする。"""
        self._refresh_scheduled = False
        if not self.is_disposed:
            self._refresh_from_plug()

    def _on_attribute_changed(
        self,
        message: int,
        plug: om.MPlug,
        _other_plug: om.MPlug,
        _client_data: object,
    ) -> None:
        """対象属性の変更・lock・接続・削除を反映する。"""
        if not self._matches_plug(plug) or self._callbacks_are_suppressed():
            return
        if message & om.MNodeMessage.kAttributeRemoved:
            self._node_was_removed = True
            self.dispose()
            return
        self._on_attribute_message(message)
        if self._DEFER_ATTRIBUTE_CHANGES:
            self._schedule_refresh()
        else:
            self._refresh_from_plug()

    def _on_node_dirty_plug(
        self, _node: om.MObject, plug: om.MPlug, _client_data: object
    ) -> None:
        """関係するdirty通知だけを遅延再読込みへ送る。"""
        if self._matches_plug(plug):
            self._schedule_refresh()

    def _on_node_pre_removal(self, *_args: object) -> None:
        """削除Undoで自動再接続しないよう対象を終了する。"""
        self._node_was_removed = True
        self.dispose()

    def _on_history_event(self, *_args: object) -> None:
        """Undo/Redo後の実値を読み直す。"""
        self._history_input_received()
        self._schedule_refresh()

    def _callbacks_are_suppressed(self) -> bool:
        """自身の書込み中なら派生クラスがcallbackを抑止する。"""
        return False

    def _on_refresh_scheduled(self) -> None:
        """遅延読込みの予約を派生クラスへ知らせる。"""
        return

    def _on_attribute_message(self, _message: int) -> None:
        """値・接続の変更種別を派生クラスへ知らせる。"""
        return

    def _history_input_received(self) -> None:
        """Undo/Redo通知を派生クラスへ知らせる。"""
        return

    def _refresh_from_plug(self) -> bool:
        """正本の方向に従って再同期する。"""
        raise NotImplementedError

    def _on_endpoint_unavailable(self) -> None:
        """派生クラスに終了を知らせる。"""
        raise NotImplementedError
