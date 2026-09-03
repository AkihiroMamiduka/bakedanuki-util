# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Protocol, cast
from weakref import ReferenceType, ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import BoolViewModel, qt
from ...node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
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


def _run_later(callback: Callable[[], None]) -> None:
    """次のQt event loopでcallbackを一度だけ呼び出す。"""
    timer_type = cast(_QTimerType, qt.QtCore.QTimer)
    timer_type.singleShot(0, callback)


def _require_view_model(value: object) -> BoolViewModel:
    """runtime値をBoolViewModelとして検証する。"""
    if not isinstance(value, BoolViewModel):
        raise TypeError(
            "view_modelにはBoolViewModelを指定してください: "
            f"{type(value).__name__}"
        )
    return value


def _require_owner(value: object) -> qt.QObject:
    """runtime値をcallback ownerとして検証する。"""
    if not isinstance(value, qt.QObject):
        raise TypeError(
            "ownerにはQObjectを指定してください: " f"{type(value).__name__}"
        )
    return value


def _require_bool_plug(value: object) -> BoolPlugOperator:
    """runtime値をBoolPlugOperatorとして検証する。"""
    if not isinstance(value, BoolPlugOperator):
        raise TypeError(
            "plugにはBoolPlugOperatorを指定してください: "
            f"{type(value).__name__}"
        )
    return value


def _require_bool(value: object) -> bool:
    """runtime値をboolとして検証する。"""
    if not isinstance(value, bool):
        raise TypeError(
            "valueにはboolを指定してください: " f"{type(value).__name__}"
        )
    return value


def _disconnect_qt_connection(
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


class _MayaBoolPlugCallbackRegistry(MayaCallbackRegistry):
    """外部からのcallback解除をbindingへ通知するregistry。"""

    disposed = qt.Signal()

    def dispose(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """callbackを解除し、最初の解除時だけ通知する。"""
        if self.is_disposed:
            return
        super().dispose(_object)
        self.disposed.emit()


class _MayaBoolPlugEndpoint(qt.QObject):
    """Maya bool plugのcallbackとlifecycleを共有する内部基底。"""

    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = False

    def __init__(
        self,
        view_model: BoolViewModel,
        plug: BoolPlugOperator,
        owner: qt.QObject,
    ) -> None:
        """ViewModel、bool plug、callback ownerを保持する。"""
        view_model = _require_view_model(view_model)
        owner = _require_owner(owner)
        plug = _require_bool_plug(plug)
        super().__init__(owner)

        # Viewだけを保持するfactory構成でも同期先を存続させる。
        self._view_model: BoolViewModel | None = view_model
        self._view_model_ref: ReferenceType[BoolViewModel] = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._node_handle = om.MObjectHandle(self._plug.node())
        self._registry = _MayaBoolPlugCallbackRegistry(owner)
        self._node_was_removed = False
        self._refresh_scheduled = False
        self._is_disposed = False

        self._registry_disposed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self._registry.disposed.connect(self._on_registry_disposed)
        self._owner_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = owner.destroyed.connect(self._on_owner_destroyed)
        self._view_model_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = view_model.destroyed.connect(self._on_view_model_destroyed)
        self._self_destroyed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self.destroyed.connect(self._registry.dispose)

        try:
            self._register_callbacks()
        except Exception:
            self._dispose_endpoint()
            raise

    @property
    def view_model(self) -> BoolViewModel:
        """同期対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のBoolViewModelは破棄されています")
        return view_model

    @property
    def plug_operator(self) -> BoolPlugOperator:
        """同期対象のbool plug operatorを返す。"""
        return self._plug_operator

    @property
    def is_available(self) -> bool:
        """Maya plugを安全に読み取れるか返す。"""
        return (
            not self.is_disposed
            and not self._node_was_removed
            and self._node_handle.isValid()
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
                and not self._plug.isLocked
                and not self._plug.isDestination
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

    def _read_plug(self) -> bool:
        """Maya bool plugの現在値を返す。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya bool plugは利用できません")
        return self._plug.asBool()

    def _write_plug(self, value: bool) -> bool:
        """Maya undo対応のsetAttrで値を設定し、確定値を返す。"""
        value = _require_bool(value)
        if not self.is_writable:
            raise RuntimeError("同期対象のMaya bool plugへ書き込めません")

        set_attr = cast(Callable[[str, bool], None], cmds.setAttr)
        set_attr(self._cmds_plug_name(), value)
        return self._read_plug()

    def _dispose_endpoint(self) -> bool:
        """破棄順に依存せずcallbackと同期状態を停止する。"""
        if self._is_disposed:
            return False
        self._is_disposed = True
        self._refresh_scheduled = False
        self._disconnect_lifecycle_connections()
        self._registry.dispose()
        try:
            self._on_endpoint_unavailable()
        finally:
            self._view_model = None
        return True

    def _disconnect_lifecycle_connections(self) -> None:
        """破棄済みPython slotをQt owner側へ残さない。"""
        _disconnect_qt_connection(self._registry_disposed_connection)
        self._registry_disposed_connection = None
        _disconnect_qt_connection(self._owner_destroyed_connection)
        self._owner_destroyed_connection = None
        _disconnect_qt_connection(self._view_model_destroyed_connection)
        self._view_model_destroyed_connection = None
        _disconnect_qt_connection(self._self_destroyed_connection)
        self._self_destroyed_connection = None

    def _valid_view_model(self) -> BoolViewModel | None:
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
            return plug == self._plug
        except RuntimeError:
            return False

    def _schedule_refresh(self) -> None:
        """次のQt event loopで一度だけplug同期を実行する。"""
        if self._refresh_scheduled or self._callbacks_are_suppressed():
            return
        self._refresh_scheduled = True
        self._on_refresh_scheduled()
        _run_later(self._refresh_after_callback)

    def _refresh_after_callback(self) -> None:
        """Maya callback完了後に確定値を同期する。"""
        self._refresh_scheduled = False
        if not self.is_disposed:
            self._refresh_from_plug()

    def _callbacks_are_suppressed(self) -> bool:
        """subclassが自身の書き込み中callbackを抑制する入口。"""
        return False

    def _on_refresh_scheduled(self) -> None:
        """subclassへ遅延同期の予約を通知する。"""
        return

    def _on_attribute_message(self, _message: int) -> None:
        """subclassへattribute変更種別を同期的に通知する。"""
        return

    def _refresh_from_plug(self) -> bool:
        """subclass固有の方向でplugの状態を同期する。"""
        raise NotImplementedError

    def _on_endpoint_unavailable(self) -> None:
        """subclassへnodeまたはbindingの利用終了を通知する。"""
        raise NotImplementedError

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
        self._on_attribute_message(_message)
        if self._DEFER_ATTRIBUTE_CHANGES:
            self._schedule_refresh()
        else:
            self._refresh_from_plug()

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
        self._dispose_endpoint()

    def _on_owner_destroyed(self, *_args: object) -> None:
        """owner破棄時に同期を安全に停止する。"""
        self._dispose_endpoint()

    def _on_view_model_destroyed(self, *_args: object) -> None:
        """ViewModel破棄時にcallbackを安全に停止する。"""
        self._dispose_endpoint()


class MayaBoolPlugStore(_MayaBoolPlugEndpoint):
    """Maya bool plugをbool値の正本として扱うStore。"""

    def read(self) -> bool:
        """Maya bool plugの現在値を返す。"""
        return self._read_plug()

    def write(self, value: bool) -> bool:
        """Maya undo対応のsetAttrで値を設定し、確定値を返す。"""
        return self._write_plug(value)

    def refresh(self) -> bool:
        """Maya plugの実値と書き込み可否をViewModelへ同期する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._dispose_endpoint()
            return False
        if view_model.store is not self:
            return False
        if not self.is_available:
            view_model.store_became_unavailable(self)
            return False
        return view_model.refresh_from_store(self)

    def _validate_attached_view_model(
        self,
        view_model: BoolViewModel,
    ) -> None:
        """callback先とStore接続先が同じViewModelか検証する。"""
        if view_model is not self.view_model:
            raise ValueError(
                "MayaBoolPlugStoreは構築時に指定したBoolViewModelへ"
                "接続してください"
            )

    def _refresh_from_plug(self) -> bool:
        """Maya callbackを接続済みViewModelへ反映する。"""
        return self.refresh()

    def _on_endpoint_unavailable(self) -> None:
        """このStoreが正本の場合だけCommandを無効化する。"""
        view_model = self._valid_view_model()
        if view_model is not None and view_model.store is self:
            view_model.store_became_unavailable(self)


class MayaBoolPlugView(_MayaBoolPlugEndpoint):
    """Store正本のbool値とMaya bool plugを同期するView。"""

    sync_failed = qt.Signal(object)
    _DEFER_ATTRIBUTE_CHANGES = True
    _VIEW_REFERENCE_ATTRIBUTE: ClassVar[str] = (
        "_bd_util_maya_bool_plug_view_reference"
    )

    def __init__(
        self,
        view_model: BoolViewModel,
        plug: BoolPlugOperator,
        owner: qt.QObject,
    ) -> None:
        """Store接続済みViewModelとMaya plugを双方向同期する。"""
        view_model = _require_view_model(view_model)
        store = view_model.store
        if store is None:
            raise RuntimeError(
                "MayaBoolPlugViewの作成前にBoolViewModelへStoreを接続してください"
            )
        if isinstance(store, MayaBoolPlugStore):
            raise RuntimeError(
                "MayaBoolPlugViewにはPython側を正本とするStoreを接続してください"
            )
        self._require_no_other_view(view_model)

        self._is_applying_value = False
        self._is_forwarding_plug_input = False
        self._is_synchronized = False
        self._last_sync_error: Exception | None = None
        self._pending_store_sync = False
        self._value_changed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None
        self._command_executed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None
        self._store_refreshed_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = None
        super().__init__(view_model, plug, owner)

        self._claim_view_model(view_model)
        self._value_changed_connection = view_model.value.changed.connect(
            self._on_view_model_value_changed
        )
        self._command_executed_connection = (
            view_model.set_value_command.executed.connect(
                self._on_command_executed
            )
        )
        self._store_refreshed_connection = view_model.store_refreshed.connect(
            self._on_store_refreshed
        )
        try:
            self.sync_from_view_model()
        except Exception:
            self._dispose_endpoint()
            raise

    @property
    def is_synchronized(self) -> bool:
        """Storeの公開値とMaya plugが同期済みか返す。"""
        return self._is_synchronized and not self.is_disposed

    @property
    def last_sync_error(self) -> Exception | None:
        """直近の非同期同期処理で発生した例外を返す。"""
        return self._last_sync_error

    def sync_from_view_model(self) -> bool:
        """Storeの公開値をMaya plugへ反映する。"""
        try:
            view_model = self.view_model
            if not self.is_available:
                raise RuntimeError("同期対象のMaya bool plugは利用できません")

            value = view_model.value.value
            if self._read_plug() == value:
                self._pending_store_sync = False
                self._mark_synchronized()
                return False
            if not self.is_writable:
                raise RuntimeError("同期対象のMaya bool plugへ書き込めません")

            self._is_applying_value = True
            try:
                actual_value = self._write_plug(value)
            finally:
                self._is_applying_value = False
            if actual_value != value:
                raise RuntimeError(
                    "Maya bool plugへStoreの確定値を反映できませんでした"
                )

            self._pending_store_sync = False
            self._mark_synchronized()
            return True
        except Exception as error:
            self._pending_store_sync = True
            self._record_sync_failure(error)
            raise

    def _refresh_from_plug(self) -> bool:
        """Maya入力をCommand経由でStoreへ反映する。"""
        if self._is_applying_value or self.is_disposed:
            return False

        view_model = self._valid_view_model()
        if view_model is None:
            self._dispose_endpoint()
            return False
        if not self.is_available:
            self._record_sync_failure(
                RuntimeError("同期対象のMaya bool plugは利用できません")
            )
            return False

        actual_value = self._read_plug()
        store_value = view_model.value.value
        if not self.is_writable:
            if actual_value == store_value:
                self._pending_store_sync = False
                self._mark_synchronized()
                return False
            self._pending_store_sync = True
            self._record_sync_failure(
                RuntimeError(
                    "Maya bool plugが書き込み不可のためStore値を維持します"
                )
            )
            return False

        if self._pending_store_sync:
            try:
                return self.sync_from_view_model()
            except Exception:
                return False

        if actual_value == store_value:
            self._mark_synchronized()
            return False
        if not view_model.set_value_command.can_execute:
            self._record_sync_failure(
                RuntimeError(
                    "Storeが書き込み不可のためMaya入力を反映できません"
                )
            )
            return False

        self._is_forwarding_plug_input = True
        try:
            try:
                changed = view_model.set_value_command.execute(actual_value)
            except Exception as error:
                self._record_sync_failure(error)
                return False
        finally:
            self._is_forwarding_plug_input = False

        if view_model.value.value != actual_value:
            self._record_sync_failure(
                RuntimeError(
                    "Maya入力はStoreの確定値として採用されませんでした"
                )
            )
            return False

        self._mark_synchronized()
        return changed

    def _callbacks_are_suppressed(self) -> bool:
        """Store値をplugへ描画している間のecho callbackを抑制する。"""
        return self._is_applying_value

    def _on_refresh_scheduled(self) -> None:
        """確定値を再読込するまでは同期中と報告しない。"""
        self._is_synchronized = False

    def _on_attribute_message(self, message: int) -> None:
        """coalesce後もStoreを優先すべき変更理由を保持する。"""
        connection_made = bool(
            message & om.MNodeMessage.kConnectionMade
            and message & om.MNodeMessage.kIncomingDirection
        )
        if connection_made:
            self._pending_store_sync = True
            return
        if message & om.MNodeMessage.kAttributeSet and self.is_writable:
            # 書き込み可能へ戻った後の新しいMaya入力は後勝ちとする。
            self._pending_store_sync = False

    def _on_view_model_value_changed(self, _value: bool) -> None:
        """Storeの確定値をMaya Viewへ描画する。"""
        if self.is_disposed:
            return
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def _on_command_executed(self, _value: bool) -> None:
        """同値Commandも遅延中の古いMaya入力より優先する。"""
        self._sync_after_store_confirmation()

    def _on_store_refreshed(self, _value: bool) -> None:
        """同値refreshも遅延中の古いMaya入力より優先する。"""
        self._sync_after_store_confirmation()

    def _sync_after_store_confirmation(self) -> None:
        """Store側で後から確定した値をMaya Viewへ適用する。"""
        if self.is_disposed or self._is_forwarding_plug_input:
            return
        self._pending_store_sync = True
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def _mark_synchronized(self) -> None:
        """直近の同期失敗を消去して同期済みにする。"""
        self._is_synchronized = True
        self._last_sync_error = None

    def _record_sync_failure(self, error: Exception) -> None:
        """非同期境界の失敗を状態とsignalで公開する。"""
        self._is_synchronized = False
        self._last_sync_error = error
        self.sync_failed.emit(error)

    def _on_endpoint_unavailable(self) -> None:
        """Viewだけを停止し、StoreとCommandには影響させない。"""
        self._is_synchronized = False
        _disconnect_qt_connection(self._value_changed_connection)
        self._value_changed_connection = None
        _disconnect_qt_connection(self._command_executed_connection)
        self._command_executed_connection = None
        _disconnect_qt_connection(self._store_refreshed_connection)
        self._store_refreshed_connection = None
        self._release_view_model()

    @classmethod
    def _require_no_other_view(cls, view_model: BoolViewModel) -> None:
        """1つのViewModelへ複数Maya Viewを接続しない。"""
        current_reference = cast(
            ReferenceType[MayaBoolPlugView] | None,
            getattr(view_model, cls._VIEW_REFERENCE_ATTRIBUTE, None),
        )
        if current_reference is None:
            return
        current_view = current_reference()
        if current_view is not None and not current_view.is_disposed:
            raise RuntimeError(
                "1つのBoolViewModelへ複数のMayaBoolPlugViewを接続できません"
            )

    def _claim_view_model(self, view_model: BoolViewModel) -> None:
        """ViewModelへこのMaya Viewの弱参照を登録する。"""
        setattr(
            view_model,
            self._VIEW_REFERENCE_ATTRIBUTE,
            ref(self),
        )

    def _release_view_model(self) -> None:
        """このMaya Viewが保持していた接続枠だけを解放する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            return
        current_reference = cast(
            ReferenceType[MayaBoolPlugView] | None,
            getattr(view_model, self._VIEW_REFERENCE_ATTRIBUTE, None),
        )
        if current_reference is not None and current_reference() is self:
            delattr(view_model, self._VIEW_REFERENCE_ATTRIBUTE)
