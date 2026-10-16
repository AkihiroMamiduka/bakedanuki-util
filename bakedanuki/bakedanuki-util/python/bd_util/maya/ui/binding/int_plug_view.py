# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Protocol, cast
from weakref import ReferenceType, ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import IntViewModel, qt
from ....ui.binding.int._connection import connect_queued, disconnect
from ..callback import MayaCallbackRegistry
from ._float_edit import FloatEditUndo
from ._int_plug_value import IntPlugValue
from ._plugs_store import PlugsStore
from .int_plug_resolver import MayaIntPlug, require_int_plug

_VIEW_REFERENCE = "_bd_util_maya_int_plug_view_reference"


def _require_view_model(value: object) -> IntViewModel:
    """動的な呼出し境界で整数ViewModelを検証する。"""
    if not isinstance(value, IntViewModel):
        raise TypeError("view_modelにはIntViewModelを指定してください")
    return value


def _require_owner(value: object) -> qt.QObject:
    """動的な呼出し境界でQt所有者を検証する。"""
    if not isinstance(value, qt.QObject):
        raise TypeError("ownerにはQObjectを指定してください")
    return value


class _QTimerType(Protocol):
    """Qt stub差分を遅延実行の境界へ限定する。"""

    @staticmethod
    def singleShot(milliseconds: int, callback: Callable[[], None]) -> None:
        """次のevent loopでcallbackを一度実行する。"""
        raise NotImplementedError


class _IntViewRegistry(MayaCallbackRegistry):
    """外部解除とQt破棄経路を整数Viewへ通知するRegistry。"""

    disposed = qt.Signal()

    def __init__(self, owner: qt.QObject) -> None:
        """Qt破棄中の通知を区別する状態を初期化する。"""
        self.destroying_qt_owner = False
        super().__init__(owner)

    def dispose(self, _object: qt.QObject | None = None) -> None:
        """callbackを解除し、最初の解除時だけViewへ通知する。"""
        if self.is_disposed:
            return
        super().dispose(_object)
        self.disposed.emit()

    @qt.Slot()
    def _on_owner_destroyed(self) -> None:
        """Qt所有者の破棄中にViewを同期処理へ戻さない。"""
        self.destroying_qt_owner = True
        super()._on_owner_destroyed()

    @qt.Slot()
    def dispose_from_view_destruction(self) -> None:
        """View実体の破棄時にもcallbackを即座に解除する。"""
        self.destroying_qt_owner = True
        self.dispose()


class MayaIntPlugView(qt.QObject):
    """Python正本の確定整数とMayaのbyte・short・longを双方向同期する。"""

    sync_failed = qt.Signal(object)

    def __init__(
        self,
        view_model: IntViewModel,
        plug: MayaIntPlug,
        owner: qt.QObject,
    ) -> None:
        """Python初期値を既存Maya属性へ適用し、変更を遅延監視する。

        Args:
            view_model: Python側のStoreを接続済みのViewModel。
            plug: 同期先の単一整数属性。compoundの整数子も指定できる。
            owner: callbackとViewの寿命を管理する所有者。

        Raises:
            TypeError: ViewModel・plug・ownerの型が不正な場合。
            RuntimeError: Store未接続、Maya正本、View重複、初期同期不可の場合。
            ValueError: Python初期値がMayaの型範囲やhard limitの範囲外の場合。
        """
        view_model = _require_view_model(view_model)
        owner = _require_owner(owner)
        plug = require_int_plug(plug)
        if view_model.is_disposed or view_model.store is None:
            raise RuntimeError(
                "Maya View作成前にPython Storeを接続してください"
            )
        if isinstance(view_model.store, PlugsStore):
            raise RuntimeError(
                "MayaIntPlugViewにはPython側を正本とするStoreが必要です"
            )
        reference = cast(
            ReferenceType[MayaIntPlugView] | None,
            getattr(view_model, _VIEW_REFERENCE, None),
        )
        current = reference() if reference is not None else None
        if current is not None and not current.is_disposed:
            raise RuntimeError(
                "同じViewModelへ複数のMayaIntPlugViewを接続できません"
            )
        super().__init__(owner)
        self._view_model: IntViewModel | None = view_model
        self._view_model_ref = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._codec = IntPlugValue(plug)
        self._node_handle = om.MObjectHandle(self._plug.node())
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._watched_plugs = [self._plug]
        while self._watched_plugs[-1].isChild:
            self._watched_plugs.append(self._watched_plugs[-1].parent())
        self._is_disposed = False
        self._refresh_scheduled = False
        self._is_applying_value = False
        self._is_forwarding_plug_input = False
        self._is_history_input = False
        self._is_synchronized = False
        self._pending_store_sync = False
        self._last_sync_error: Exception | None = None
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = []
        self._registry = _IntViewRegistry(owner)
        self._edit_undo = FloatEditUndo(view_model)
        self._registry.disposed.connect(self._edit_undo.dispose)
        try:
            # 破棄と外部Registry解除の双方で、遅延入力と接続を終了する
            self._connections.extend(
                (
                    self._registry.disposed.connect(
                        self._on_registry_disposed
                    ),
                    self.destroyed.connect(
                        self._registry.dispose_from_view_destruction
                    ),
                    connect_queued(owner.destroyed, self.dispose),
                    connect_queued(view_model.destroyed, self.dispose),
                    view_model.disposed.connect(self.dispose),
                    view_model.value.changed.connect(
                        self._on_store_confirmation
                    ),
                    view_model.set_value_command.executed.connect(
                        self._on_store_confirmation
                    ),
                    view_model.store_refreshed.connect(
                        self._on_store_confirmation
                    ),
                )
            )
            setattr(view_model, _VIEW_REFERENCE, ref(self))
            self._register_callbacks()
            self.sync_from_view_model()
        except Exception:
            self.dispose()
            self.deleteLater()
            raise

    @property
    def view_model(self) -> IntViewModel:
        """同期対象のViewModelを返す。Qt実体が破棄済みなら例外を送出する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のIntViewModelは終了しています")
        return view_model

    @property
    def plug_operator(self) -> MayaIntPlug:
        """同期対象の整数PlugOperatorを返す。"""
        return self._plug_operator

    @property
    def is_available(self) -> bool:
        """Maya nodeと属性の実体を安全に読み取れるか返す。"""
        return (
            not self.is_disposed
            and self._node_handle.isValid()
            and self._attribute_handle.isValid()
        )

    @property
    def is_writable(self) -> bool:
        """属性とcompound祖先がlock・入力接続を持たず書けるか返す。"""
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
        """明示終了・所有者破棄・外部callback解除済みか返す。"""
        return (
            self._is_disposed
            or self._registry.is_disposed
            or not qt.isValid(self)
        )

    @property
    def is_synchronized(self) -> bool:
        """PythonとMayaの確定整数が一致し、入力保留もないか返す。"""
        view_model = self._valid_view_model()
        return (
            self._is_synchronized
            and not self.is_disposed
            and view_model is not None
            and not view_model.is_disposed
        )

    @property
    def last_sync_error(self) -> Exception | None:
        """直近の同期失敗を返す。同期成功後は`None`。"""
        return self._last_sync_error

    def dispose(self) -> None:
        """Maya callbackと遅延入力を停止し、Python Storeは維持する。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        self._refresh_scheduled = False
        self._is_synchronized = False
        view_model = self._valid_view_model()
        if view_model is not None:
            view_model.end_edit()
        self._edit_undo.dispose()
        for connection in self._connections:
            disconnect(connection)
        self._connections.clear()
        self._registry.dispose()
        view_model = self._valid_view_model()
        if view_model is not None:
            reference = cast(
                ReferenceType[MayaIntPlugView] | None,
                getattr(view_model, _VIEW_REFERENCE, None),
            )
            if reference is not None and reference() is self:
                delattr(view_model, _VIEW_REFERENCE)
        self._view_model = None

    def sync_from_view_model(self) -> bool:
        """最後のPython確定値をMayaへ反映し、書込み有無を返す。

        Raises:
            RuntimeError: StoreやMaya属性が利用不可、書込み不可の場合。
            ValueError: Python値がMayaの型範囲やhard limitの範囲外の場合。
        """
        self._is_history_input = False
        return self._sync_from_view_model(allow_write=True)

    def _sync_from_view_model(self, *, allow_write: bool) -> bool:
        """Python値を優先し、履歴復元中は追加書込みを行わない。"""
        if self._is_applying_value:
            return False
        wrote = False
        try:
            while True:
                view_model = self.view_model
                store = view_model.store
                if (
                    not self.is_available
                    or view_model.is_disposed
                    or store is None
                    or not store.is_available
                ):
                    raise RuntimeError(
                        "同期対象のStoreまたはMaya属性は利用できません"
                    )
                value = view_model.value.value
                if self._read_plug() == value:
                    self._mark_synchronized()
                    return wrote
                if not allow_write:
                    raise RuntimeError(
                        "Undo/Redoの復元値とPython値が異なるため同期を保留します"
                    )
                if not self.is_writable:
                    raise RuntimeError(
                        "同期対象のMaya整数属性へ書き込めません"
                    )
                self._codec.validate(value)
                # Mayaからのechoを抑止し、通知先が再編集したPython値も取り込む
                self._is_applying_value = True
                try:
                    if not view_model.is_editing:
                        FloatEditUndo.finish_active()
                    with self._edit_undo.write():
                        cast(Callable[[str, int], None], cmds.setAttr)(
                            self._cmds_plug_name(), value
                        )
                    wrote = True
                finally:
                    self._is_applying_value = False
                if self.is_disposed or view_model.is_disposed:
                    return wrote
                if view_model.value.value != value:
                    continue
                if self._read_plug() != value:
                    raise RuntimeError(
                        "Maya属性へPythonの確定整数を反映できませんでした"
                    )
                self._mark_synchronized()
                return wrote
        except Exception as error:
            self._pending_store_sync = True
            self._record_sync_failure(error)
            raise

    def _refresh_from_plug(self) -> bool:
        """Maya入力をCommandへ渡し、setter後のPython確定値を再表示する。"""
        if self._is_applying_value or self.is_disposed:
            return False
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            self.dispose()
            return False
        try:
            actual = self._read_plug()
            value = view_model.value.value
            if not self.is_writable:
                if actual == value:
                    self._mark_synchronized()
                    return False
                self._pending_store_sync = True
                raise RuntimeError(
                    "Maya属性が書込み不可のためPython値を維持します"
                )
            if self._pending_store_sync:
                return self._sync_from_view_model(
                    allow_write=not self._is_history_input
                )
            if actual == value:
                self._mark_synchronized()
                return False
            if not view_model.set_value_command.can_execute:
                raise RuntimeError("Python StoreへMaya入力を反映できません")
            self._is_forwarding_plug_input = True
            try:
                changed = view_model.set_value_command.execute(actual)
            except Exception as error:
                self._restore_after_input_error(error)
                return False
            finally:
                self._is_forwarding_plug_input = False
            if self.is_disposed or view_model.is_disposed:
                return changed
            self._sync_from_view_model(allow_write=not self._is_history_input)
            return changed
        except Exception as error:
            self._record_sync_failure(error)
            return False

    def _restore_after_input_error(self, error: Exception) -> None:
        """読めるPython正本を再同期し、元のsetter例外を公開する。"""
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed or self.is_disposed:
            return
        store = view_model.store
        try:
            if store is not None:
                view_model.refresh_from_store(store)
        except Exception:
            if store is not None and not view_model.is_disposed:
                view_model.store_became_unavailable(store)
        else:
            try:
                self._sync_from_view_model(
                    allow_write=not self._is_history_input
                )
            except Exception:
                pass
        self._record_sync_failure(error)

    def _valid_view_model(self) -> IntViewModel | None:
        """Qt実体も生存しているViewModelだけを返す。"""
        view_model = self._view_model or self._view_model_ref()
        return (
            view_model
            if view_model is not None and qt.isValid(view_model)
            else None
        )

    def _read_plug(self) -> int:
        """同期先の実値を暗黙変換せず整数で読む。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya整数属性は利用できません")
        return self._codec.read()

    def _cmds_plug_name(self) -> str:
        """同名DAGやcompound子でも一意になる属性名を返す。"""
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
        """値・lock・接続・dirty・node削除を所有者のRegistryへ登録する。"""
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

    def _matches_plug(self, plug: om.MPlug) -> bool:
        """通知対象がこの属性かcompound祖先か返す。"""
        if not self.is_available:
            return False
        try:
            return any(plug == watched for watched in self._watched_plugs)
        except RuntimeError:
            return False

    def _schedule_refresh(self) -> None:
        """Maya callbackの外で一度だけ確定処理を実行する。"""
        if self.is_disposed or self._is_applying_value:
            return
        if om.MGlobal.isUndoing() or om.MGlobal.isRedoing():
            self._is_history_input = True
        self._is_synchronized = False
        if not self._refresh_scheduled:
            self._refresh_scheduled = True
            cast(_QTimerType, qt.QtCore.QTimer).singleShot(
                0, self._refresh_after_callback
            )

    def _refresh_after_callback(self) -> None:
        """所有者破棄後の予約済み入力を破棄し、現在値を同期する。"""
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
        """変更時のUndo状態と同期方向を遅延処理まで保持する。"""
        if not self._matches_plug(plug) or self._is_applying_value:
            return
        if message & (
            om.MNodeMessage.kAttributeLocked | om.MNodeMessage.kConnectionMade
        ):
            view_model = self._valid_view_model()
            if view_model is not None:
                view_model.end_edit()
        if message & om.MNodeMessage.kAttributeRemoved:
            self.dispose()
            return
        if om.MGlobal.isUndoing() or om.MGlobal.isRedoing():
            self._is_history_input = True
        elif message & (
            om.MNodeMessage.kAttributeSet
            | om.MNodeMessage.kAttributeLocked
            | om.MNodeMessage.kAttributeUnlocked
            | om.MNodeMessage.kConnectionMade
            | om.MNodeMessage.kConnectionBroken
        ):
            self._is_history_input = False
        if (
            message & om.MNodeMessage.kConnectionMade
            and message & om.MNodeMessage.kIncomingDirection
        ):
            self._pending_store_sync = True
        elif message & om.MNodeMessage.kAttributeSet and self.is_writable:
            self._pending_store_sync = False
        self._schedule_refresh()

    def _on_node_dirty_plug(
        self, _node: om.MObject, plug: om.MPlug, _client_data: object
    ) -> None:
        """同期対象のdirty通知を次のevent loopへまとめる。"""
        if self._matches_plug(plug):
            self._schedule_refresh()

    def _on_node_pre_removal(self, *_args: object) -> None:
        """削除Undo後も古い属性へ再接続しないよう終了する。"""
        self.dispose()

    @qt.Slot()
    def _on_registry_disposed(self) -> None:
        """外部解除へ追従し、Qt破棄中は遅延終了へ委ねる。"""
        if not self._registry.destroying_qt_owner:
            self.dispose()

    @qt.Slot(object)
    def _on_store_confirmation(self, _value: object) -> None:
        """同値Commandやrefreshも保留中の古いMaya入力より優先する。"""
        if self.is_disposed or self._is_forwarding_plug_input:
            return
        self._pending_store_sync = True
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def _mark_synchronized(self) -> None:
        """同期成功と直近エラーの解除を公開する。"""
        self._pending_store_sync = False
        self._is_synchronized = True
        self._last_sync_error = None

    def _record_sync_failure(self, error: Exception) -> None:
        """非同期境界の失敗を保持し、生存中だけ通知する。"""
        view_model = self._valid_view_model()
        if view_model is not None:
            view_model.end_edit()
        self._is_synchronized = False
        self._last_sync_error = error
        if not self.is_disposed:
            self.sync_failed.emit(error)
