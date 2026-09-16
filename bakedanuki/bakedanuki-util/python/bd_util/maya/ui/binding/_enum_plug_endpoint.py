# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Protocol, cast
from weakref import ReferenceType, ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import EnumViewModel, qt
from ....ui.binding.enum.definition import require_enum_value
from .enum_plug_resolver import MayaEnumPlug
from .enum_plug_resolver import require_enum_plug
from ._enum_plug_value import EnumPlugValue
from ..callback import MayaCallbackRegistry


class _QTimerType(Protocol):
    """PySide stub境界で使用するQTimer classの必要最小API。"""

    @staticmethod
    def singleShot(
        milliseconds: int,
        callback: Callable[[], None],
    ) -> None:
        """指定時間後にcallbackを一度だけ呼び出す。"""
        raise NotImplementedError


class _QueuedSignal(Protocol):
    """PySide stubの型と実際のqueued connectの差を吸収する。"""

    def connect(
        self,
        slot: Callable[[], None],
        connection_type: qt.Qt.ConnectionType,
    ) -> qt.QtCore.QMetaObject.Connection:
        """slotを指定した接続方式で登録する。"""
        raise NotImplementedError


def run_later(callback: Callable[[], None]) -> None:
    """次のQt event loopでcallbackを一度だけ呼び出す。"""
    timer_type = cast(_QTimerType, qt.QtCore.QTimer)
    timer_type.singleShot(0, callback)


def require_enum_view_model(value: object) -> EnumViewModel:
    """runtime値をEnumViewModelとして検証する。"""
    if not isinstance(value, EnumViewModel):
        raise TypeError(
            "view_modelにはEnumViewModelを指定してください: "
            f"{type(value).__name__}"
        )
    return value


def require_owner(value: object) -> qt.QObject:
    """runtime値をcallback ownerとして検証する。"""
    if not isinstance(value, qt.QObject):
        raise TypeError(
            "ownerにはQObjectを指定してください: " f"{type(value).__name__}"
        )
    return value


def disconnect_qt_connection(
    connection: qt.QtCore.QMetaObject.Connection | None,
) -> None:
    """保持しているQt signal接続を安全に解除する。"""
    if connection is None:
        return
    try:
        disconnect = cast(
            Callable[[qt.QtCore.QMetaObject.Connection], bool],
            getattr(qt.QtCore.QObject, "disconnect"),
        )
        disconnect(connection)
    except (RuntimeError, TypeError):
        pass


class _EnumPlugOperatorCallbackRegistry(MayaCallbackRegistry):
    """外部からのcallback解除をbindingへ通知するregistry。"""

    disposed = qt.Signal()

    def __init__(self, owner: qt.QObject) -> None:
        """callback ownerと破棄経路の状態を保持して初期化する。"""
        self._owner_is_being_destroyed = False
        self._endpoint_is_being_destroyed = False
        super().__init__(owner)

    @property
    def owner_is_being_destroyed(self) -> bool:
        """ownerのQObject破棄通知から解除中か返す。"""
        return self._owner_is_being_destroyed

    @property
    def endpoint_is_being_destroyed(self) -> bool:
        """endpointのQObject破棄通知から解除中か返す。"""
        return self._endpoint_is_being_destroyed

    def dispose(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """callbackを解除し、最初の解除時だけ通知する。"""
        if self.is_disposed:
            return
        super().dispose(_object)
        self.disposed.emit()

    @qt.Slot()
    def _on_owner_destroyed(self) -> None:
        """owner破棄中の同期通知を識別してcallbackを解除する。"""
        self._owner_is_being_destroyed = True
        super()._on_owner_destroyed()

    @qt.Slot()
    def dispose_from_endpoint_destruction(self) -> None:
        """endpoint破棄中の同期通知を識別してcallbackを解除する。"""
        self._endpoint_is_being_destroyed = True
        self.dispose()


class EnumPlugEndpoint(qt.QObject):
    """Mayaenumplugへのアクセスとcallbackの寿命を管理する。"""

    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = False

    def __init__(
        self,
        view_model: EnumViewModel,
        plug: MayaEnumPlug,
        owner: qt.QObject,
    ) -> None:
        """ViewModel、enumplug、callback ownerを保持する。"""
        view_model = require_enum_view_model(view_model)
        owner = require_owner(owner)
        plug = require_enum_plug(plug)
        super().__init__(owner)

        # Viewだけを保持するfactory構成でも同期先を存続させる。
        self._view_model: EnumViewModel | None = view_model
        self._view_model_ref: ReferenceType[EnumViewModel] = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._codec = EnumPlugValue(self._plug)
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._watched_plugs = [self._plug]
        while self._watched_plugs[-1].isChild:
            self._watched_plugs.append(self._watched_plugs[-1].parent())
        self._node_handle = om.MObjectHandle(self._plug.node())
        self._registry = _EnumPlugOperatorCallbackRegistry(owner)
        self._node_was_removed = False
        self._refresh_scheduled = False
        self._is_disposed = False

        self._registry_disposed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self._registry.disposed.connect(self._on_registry_disposed)
        self._owner_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = cast(_QueuedSignal, owner.destroyed).connect(
            self._on_owner_destroyed,
            qt.Qt.ConnectionType.QueuedConnection,
        )
        self._view_model_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = cast(_QueuedSignal, view_model.destroyed).connect(
            self._on_view_model_destroyed,
            qt.Qt.ConnectionType.QueuedConnection,
        )
        view_model.disposed.connect(self.dispose)
        self._self_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self.destroyed.connect(
            self._registry.dispose_from_endpoint_destruction
        )

        try:
            self._register_callbacks()
        except Exception:
            self._dispose_endpoint()
            raise

    @property
    def view_model(self) -> EnumViewModel:
        """同期対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のEnumViewModelは破棄されています")
        return view_model

    @property
    def plug_operator(self) -> MayaEnumPlug:
        """同期対象のenumplug operatorを返す。"""
        return self._plug_operator

    @property
    def is_available(self) -> bool:
        """Maya plugを安全に読み取れるか返す。"""
        return (
            not self.is_disposed
            and not self._node_was_removed
            and self._node_handle.isValid()
            and self._attribute_handle.isValid()
        )

    @property
    def is_writable(self) -> bool:
        """Maya標準の値設定を受け付けられるplugか返す。"""
        if not self.is_available:
            return False
        try:
            attribute = om.MFnAttribute(self._plug.attribute())
            return (
                attribute.writable
                and self._plug.isFreeToChange(True, False)
                == om.MPlug.kFreeToChange
                and not any(plug.isDestination for plug in self._watched_plugs)
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

    def dispose(self) -> None:
        """Maya callbackを解除して同期を停止する。"""
        self._dispose_endpoint()

    def _read_plug(self) -> int:
        """Maya enumplugの現在値を返す。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya enumplugは利用できません")
        return self._codec.read()

    def _write_plug(self, value: int) -> int:
        """Mayaの最新定義を検証し、Undo対応のsetAttrで確定する。"""
        value = require_enum_value(value)
        if not self.is_writable:
            raise RuntimeError("同期対象のMaya enum plugへ書き込めません")
        self._codec.definition.require_value(value)
        current = self._read_plug()
        if current != value:
            set_attr = cast(Callable[[str, int], None], cmds.setAttr)
            set_attr(self._cmds_plug_name(), value)
        return self._read_plug()

    def _dispose_endpoint(
        self,
        *,
        notify_view_model: bool = True,
    ) -> bool:
        """破棄順に依存せずcallbackと同期状態を停止する。"""
        if self._is_disposed:
            return False
        self._is_disposed = True
        self._refresh_scheduled = False
        self._disconnect_lifecycle_connections()
        self._registry.dispose()
        try:
            self._on_endpoint_unavailable(notify_view_model)
        finally:
            self._view_model = None
        return True

    def _disconnect_lifecycle_connections(self) -> None:
        """破棄済みPython slotをQt owner側へ残さない。"""
        disconnect_qt_connection(self._registry_disposed_connection)
        self._registry_disposed_connection = None
        disconnect_qt_connection(self._owner_destroyed_connection)
        self._owner_destroyed_connection = None
        disconnect_qt_connection(self._view_model_destroyed_connection)
        self._view_model_destroyed_connection = None
        disconnect_qt_connection(self._self_destroyed_connection)
        self._self_destroyed_connection = None

    def _valid_view_model(self) -> EnumViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if view_model is None:
            view_model = self._view_model_ref()
        if view_model is None or not qt.isValid(view_model):
            return None
        return view_model

    def _cmds_plug_name(self) -> str:
        """同名DAG nodeでも一意になるcmds用plug名を返す。"""
        attribute_path = cast(
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
        return f"{self._plug_operator.node.cmd_access_name}.{attribute_path}"

    def _register_callbacks(self) -> None:
        """値・評価・node削除通知をownerのregistryへ登録する。"""
        node = self._plug.node()
        self._registry.register(
            int(
                om.MNodeMessage.addAttributeChangedCallback(
                    node,
                    self._on_attribute_changed,
                )
            )
        )
        self._registry.register(
            int(
                om.MNodeMessage.addNodeDirtyPlugCallback(
                    node,
                    self._on_node_dirty_plug,
                )
            )
        )
        self._registry.register(
            int(
                om.MNodeMessage.addNodePreRemovalCallback(
                    node,
                    self._on_node_pre_removal,
                )
            )
        )

    def _matches_plug(self, plug: om.MPlug) -> bool:
        """callback対象が同期中のplug自身か返す。"""
        if not self.is_available:
            return False
        try:
            return any(plug == watched for watched in self._watched_plugs)
        except RuntimeError:
            return False

    def _schedule_refresh(self) -> None:
        """次のQt event loopで一度だけplug同期を実行する。"""
        if self._refresh_scheduled or self._callbacks_are_suppressed():
            return
        self._refresh_scheduled = True
        self._on_refresh_scheduled()
        run_later(self._refresh_after_callback)

    def _refresh_after_callback(self) -> None:
        """Maya callback完了後に確定値を同期する。"""
        self._refresh_scheduled = False
        if not self.is_disposed:
            self._refresh_from_plug()

    def _on_attribute_changed(
        self,
        _message: int,
        plug: om.MPlug,
        _other_plug: om.MPlug,
        _client_data: object,
    ) -> None:
        """直接変更、接続、lock変更を同期する。"""
        if not self._matches_plug(plug) or self._callbacks_are_suppressed():
            return
        if _message & om.MNodeMessage.kAttributeRemoved:
            self._dispose_endpoint()
            return
        self._on_attribute_message(_message)
        if self._DEFER_ATTRIBUTE_CHANGES:
            self._schedule_refresh()
        else:
            self._refresh_from_plug()

    def _callbacks_are_suppressed(self) -> bool:
        """自身の書き込み中callbackをsubclassで抑制する。"""
        return False

    def _on_refresh_scheduled(self) -> None:
        """遅延同期の予約をsubclassへ通知する。"""
        return

    def _on_attribute_message(self, _message: int) -> None:
        """同期の優先方向に必要な変更種別をsubclassへ渡す。"""
        return

    def _refresh_from_plug(self) -> bool:
        """subclass固有の方向でplugの状態を同期する。"""
        raise NotImplementedError

    def _on_endpoint_unavailable(self, notify_view_model: bool) -> None:
        """利用終了をsubclassへ通知する。"""
        raise NotImplementedError

    def _on_node_dirty_plug(
        self,
        _node: om.MObject,
        plug: om.MPlug,
        _client_data: object,
    ) -> None:
        """上流評価でdirtyになった対象plugの遅延更新を予約する。"""
        if not self._matches_plug(plug):
            return
        self._schedule_refresh()

    def _on_node_pre_removal(self, *_args: object) -> None:
        """node削除前にplugを利用不可へ変更する。"""
        if self._node_was_removed:
            return
        self._node_was_removed = True
        self._refresh_scheduled = False
        self._dispose_endpoint()

    def _on_registry_disposed(self) -> None:
        """controllerなどによるregistryの先行解除へ追従する。"""
        if (
            self._registry.owner_is_being_destroyed
            or self._registry.endpoint_is_being_destroyed
        ):
            return
        self._dispose_endpoint()

    @qt.Slot()
    def _on_owner_destroyed(self) -> None:
        """owner破棄後に残ったendpointを通知なしで停止する。"""
        self._dispose_endpoint(notify_view_model=False)

    @qt.Slot()
    def _on_view_model_destroyed(self) -> None:
        """ViewModelのQObject tree破棄後にcallbackを停止する。"""
        self._dispose_endpoint()
