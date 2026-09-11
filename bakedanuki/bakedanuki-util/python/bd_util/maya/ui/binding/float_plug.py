# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Protocol, cast
from weakref import ReferenceType, ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import FloatPresentation, FloatViewModel, qt
from ....ui.binding.float._validation import require_float
from .float_plug_resolver import MayaFloatPlug, require_float_plug
from ._float_plug_value import FloatPlugValue
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


def _run_later(callback: Callable[[], None]) -> None:
    """次のQt event loopでcallbackを一度だけ呼び出す。"""
    timer_type = cast(_QTimerType, qt.QtCore.QTimer)
    timer_type.singleShot(0, callback)


def _require_view_model(value: object) -> FloatViewModel:
    """runtime値をFloatViewModelとして検証する。"""
    if not isinstance(value, FloatViewModel):
        raise TypeError(
            "view_modelにはFloatViewModelを指定してください: "
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


class _MayaFloatPlugCallbackRegistry(MayaCallbackRegistry):
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


class _MayaFloatPlugEndpoint(qt.QObject):
    """Maya浮動小数点plugへのアクセスとcallbackの寿命を管理する。"""

    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = False

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        owner: qt.QObject,
    ) -> None:
        """ViewModel、浮動小数点plug、callback ownerを保持する。"""
        view_model = _require_view_model(view_model)
        owner = _require_owner(owner)
        plug = require_float_plug(plug)
        super().__init__(owner)

        # Viewだけを保持するfactory構成でも同期先を存続させる。
        self._view_model: FloatViewModel | None = view_model
        self._view_model_ref: ReferenceType[FloatViewModel] = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._codec = FloatPlugValue(self._plug)
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._watched_plugs = [self._plug]
        while self._watched_plugs[-1].isChild:
            self._watched_plugs.append(self._watched_plugs[-1].parent())
        self._node_handle = om.MObjectHandle(self._plug.node())
        self._registry = _MayaFloatPlugCallbackRegistry(owner)
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
    def view_model(self) -> FloatViewModel:
        """同期対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のFloatViewModelは破棄されています")
        return view_model

    @property
    def plug_operator(self) -> MayaFloatPlug:
        """同期対象の浮動小数点plug operatorを返す。"""
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

    def _read_plug(self) -> float:
        """Maya 浮動小数点plugの現在値を返す。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya 浮動小数点plugは利用できません")
        return self._codec.read()

    def _write_plug(self, value: float) -> float:
        """Maya undo対応のsetAttrで値を設定し、確定値を返す。"""
        value = require_float(value)
        if not self.is_writable:
            raise RuntimeError("同期対象のMaya 浮動小数点plugへ書き込めません")

        ui_value = self._codec.to_ui(value)
        current_value = self._read_plug()
        if self._codec.to_ui(current_value) == ui_value:
            return current_value
        set_attr = cast(Callable[[str, float], None], cmds.setAttr)
        set_attr(self._cmds_plug_name(), ui_value)
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
        _disconnect_qt_connection(self._registry_disposed_connection)
        self._registry_disposed_connection = None
        _disconnect_qt_connection(self._owner_destroyed_connection)
        self._owner_destroyed_connection = None
        _disconnect_qt_connection(self._view_model_destroyed_connection)
        self._view_model_destroyed_connection = None
        _disconnect_qt_connection(self._self_destroyed_connection)
        self._self_destroyed_connection = None

    def _valid_view_model(self) -> FloatViewModel | None:
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
        unit_event = {
            "distance": "linearUnitChanged",
            "angle": "angularUnitChanged",
        }.get(self._codec.kind)
        if unit_event is not None:
            self._registry.register(
                int(
                    om.MEventMessage.addEventCallback(
                        unit_event, self._on_unit_changed
                    )
                )
            )
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

    def _on_unit_changed(self, *_args: object) -> None:
        """単位変更に合わせて値と表示情報を読み直す。"""
        if not self.is_disposed:
            self._refresh_from_plug()

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
        _run_later(self._refresh_after_callback)

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


class MayaFloatPlugStore(_MayaFloatPlugEndpoint):
    """Mayaの単一浮動小数点属性を正本として読み書きするStore。"""

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        owner: qt.QObject,
    ) -> None:
        """自身の書き込み通知をまとめるStoreを初期化する。"""
        self._write_depth = 0
        super().__init__(view_model, plug, owner)

    @property
    def presentation(self) -> FloatPresentation:
        """現在のMaya表示単位と公開単位のhard limitを返す。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya plugは利用できません")
        return self._codec.presentation

    def read(self) -> float:
        """Maya 浮動小数点plugの現在値を返す。"""
        return self._read_plug()

    def write(self, value: float) -> float:
        """Maya undo対応のsetAttrで値を設定し、確定値を返す。"""
        # changed slotが終了しても、書き込み後の確定値は先に取得しておく。
        self._write_depth += 1
        try:
            actual_value = self._write_plug(value)
        finally:
            self._write_depth -= 1
        self.refresh()
        # slotから別の値を設定した場合は、その最新値を優先する。
        return self._read_plug() if self.is_available else actual_value

    def _callbacks_are_suppressed(self) -> bool:
        """自身の書き込み通知は確定値の取得後にまとめて反映する。"""
        return self._write_depth > 0

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
        view_model: FloatViewModel,
    ) -> None:
        """callback先とStore接続先が同じViewModelか検証する。"""
        if view_model is not self.view_model:
            raise ValueError(
                "MayaFloatPlugStoreは構築時に指定したFloatViewModelへ"
                "接続してください"
            )

    def _refresh_from_plug(self) -> bool:
        """Maya callbackを接続済みViewModelへ反映する。"""
        return self.refresh()

    def _on_endpoint_unavailable(self, notify_view_model: bool) -> None:
        """このStoreが正本の場合だけCommandを無効化する。"""
        if not notify_view_model:
            return
        view_model = self._valid_view_model()
        if view_model is not None and view_model.store is self:
            view_model.store_became_unavailable(self)


class MayaFloatPlugView(_MayaFloatPlugEndpoint):
    """Python正本の確定値とMaya浮動小数点plugを双方向同期するView。"""

    sync_failed = qt.Signal(object)
    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = True
    _VIEW_REFERENCE_ATTRIBUTE: ClassVar[str] = (
        "_bd_util_maya_float_plug_view_reference"
    )

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        owner: qt.QObject,
    ) -> None:
        """Python値を初期同期し、Maya入力と表示単位のcallbackを接続する。"""
        view_model = _require_view_model(view_model)
        if view_model.is_disposed or view_model.store is None:
            raise RuntimeError(
                "MayaFloatPlugViewの作成前に有効なFloatViewModelへStoreを接続してください"
            )
        if isinstance(view_model.store, MayaFloatPlugStore):
            raise RuntimeError(
                "MayaFloatPlugViewにはPython側を正本とするStoreを接続してください"
            )
        self._require_no_other_view(view_model)
        self._is_applying_value = False
        self._is_forwarding_plug_input = False
        self._is_history_input = False
        self._is_synchronized = False
        self._pending_store_sync = False
        self._last_sync_error: Exception | None = None
        self._last_store_value: float | None = None
        self._last_plug_value: float | None = None
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = []
        super().__init__(view_model, plug, owner)

        view_reference = ref(self)

        def present_store(
            presentation: FloatPresentation,
        ) -> FloatPresentation:
            """Qt破棄済みのViewを保持せず、終了後はStoreの表示情報へ戻す。"""
            view = view_reference()
            if view is None or view.is_disposed:
                return presentation
            return view._present_store(presentation)

        self._presentation_adapter = present_store

        # 正本の値と入力範囲を維持し、接続中だけMayaの表示単位を使用する。
        try:
            self._claim_view_model(view_model)
            view_model.set_presentation_adapter(self._presentation_adapter)
            self._connections.extend(
                (
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
            self.sync_from_view_model()
        except Exception:
            self._dispose_endpoint()
            self.deleteLater()
            raise

    @property
    def is_synchronized(self) -> bool:
        """Python確定値がMayaの格納精度で同期済みか返す。"""
        view_model = self._valid_view_model()
        return (
            self._is_synchronized
            and not self.is_disposed
            and view_model is not None
            and not view_model.is_disposed
        )

    @property
    def last_sync_error(self) -> Exception | None:
        """直近の同期失敗を返す。成功時はNoneへ戻す。"""
        return self._last_sync_error

    def sync_from_view_model(self) -> bool:
        """Pythonの確定値をMayaへ反映し、失敗を公開して呼び出し元へ返す。"""
        self._is_history_input = False
        return self._sync_from_view_model(allow_write=True)

    def _sync_from_view_model(self, *, allow_write: bool) -> bool:
        """Undo/Redoの復元確認では追加書き込みをせずに同期状態を判定する。"""
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
                        "同期対象のStoreまたはMaya plugは利用できません"
                    )
                value = view_model.value.value
                if self._matches_value(value):
                    self._mark_synchronized(value)
                    return wrote
                if not allow_write:
                    raise RuntimeError(
                        "Undo/Redoの復元値とPython確定値が異なるためMayaへの再同期を保留します"
                    )
                if not self.is_writable:
                    raise RuntimeError(
                        "同期対象のMaya float plugへ書き込めません"
                    )
                self._require_plug_range(value)

                # setAttrのechoは抑制し、通知slotによる後続のPython値も取り込む。
                self._is_applying_value = True
                try:
                    self._write_plug(value)
                    wrote = True
                finally:
                    self._is_applying_value = False
                if self.is_disposed or view_model.is_disposed:
                    return wrote
                if view_model.value.value != value:
                    continue
                if not self._codec.matches(value):
                    raise RuntimeError(
                        "Maya float plugへStoreの確定値を反映できませんでした"
                    )
                self._mark_synchronized(value)
                return wrote
        except Exception as error:
            self._pending_store_sync = True
            self._record_sync_failure(error)
            raise

    def _matches_value(self, value: float) -> bool:
        """確認済みの格納値または今回の変換結果と一致するか返す。"""
        actual = self._read_plug()
        # 単位変更による再変換誤差でPythonの精度やUndo履歴を変更しない。
        if value == self._last_store_value and actual == self._last_plug_value:
            return True
        return self._codec.matches(value)

    def _require_plug_range(self, value: float) -> None:
        """Maya固有のhard limitを同期時に検証し、Python値は変更しない。"""
        presentation = self._codec.presentation
        if presentation.minimum is not None and value < presentation.minimum:
            raise ValueError("Python値はMaya属性の下限未満です")
        if presentation.maximum is not None and value > presentation.maximum:
            raise ValueError("Python値はMaya属性の上限を超えています")

    def _refresh_from_plug(self) -> bool:
        """callback完了後にMaya入力をCommandへ渡し、Python確定値を再表示する。"""
        if self._is_applying_value or self.is_disposed:
            return False
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            self._dispose_endpoint()
            return False
        try:
            if not self.is_available:
                raise RuntimeError("同期対象のMaya float plugは利用できません")
            actual = self._read_plug()
            value = view_model.value.value
            if not self.is_writable:
                if self._matches_value(value):
                    self._mark_synchronized(value)
                    return False
                self._pending_store_sync = True
                raise RuntimeError(
                    "Maya plugが書き込み不可のためPython値を維持します"
                )
            if self._pending_store_sync:
                return self._sync_from_view_model(
                    allow_write=not self._is_history_input
                )
            if self._matches_value(value):
                self._mark_synchronized(value)
                return False
            if not view_model.set_value_command.can_execute:
                raise RuntimeError(
                    "Storeが書き込み不可のためMaya入力を反映できません"
                )

            # setter補正や拒否を含め、確定後に一度だけMayaへ描画する。
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
        """読める正本だけを再同期し、復旧の成否によらず元の例外を公開する。"""
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
            # Maya側の同期失敗ではPython Storeの編集可否を変更しない。
            try:
                self._sync_from_view_model(
                    allow_write=not self._is_history_input
                )
            except Exception:
                pass
        self._record_sync_failure(error)

    def _present_store(
        self, presentation: FloatPresentation
    ) -> FloatPresentation:
        """Python側の入力範囲を残し、単位表示をMayaの現在単位へ置き換える。"""
        maya_presentation = self._codec.presentation
        return FloatPresentation(
            scale=maya_presentation.scale,
            suffix=maya_presentation.suffix,
            minimum=presentation.minimum,
            maximum=presentation.maximum,
        )

    def _on_unit_changed(self, *_args: object) -> None:
        """単位変更では表示だけを更新し、保留中のMaya入力を上書きしない。"""
        if self.is_disposed:
            return
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            return
        try:
            view_model.set_presentation_adapter(self._presentation_adapter)
        except Exception as error:
            self._record_sync_failure(error)

    def _callbacks_are_suppressed(self) -> bool:
        """Python値をMayaへ反映している間のcallbackを抑制する。"""
        return self._is_applying_value

    def _on_refresh_scheduled(self) -> None:
        """Maya入力の確定処理まで未同期として報告する。"""
        if om.MGlobal.isUndoing() or om.MGlobal.isRedoing():
            self._is_history_input = True
        self._is_synchronized = False

    def _on_attribute_message(self, message: int) -> None:
        """短時間の接続変更でもPython正本を優先する理由を保持する。"""
        # 遅延処理時にはUndo/Redoが終了しているため、callback中の状態を残す。
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

    @qt.Slot(float)
    def _on_store_confirmation(self, _value: float) -> None:
        """同値のCommand・refreshも、先に届いたMaya入力より優先する。"""
        if self.is_disposed or self._is_forwarding_plug_input:
            return
        self._pending_store_sync = True
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def _mark_synchronized(self, value: float) -> None:
        """Python値と確認済み格納値の組を保持し、同期エラーを解除する。"""
        self._last_plug_value = self._read_plug()
        self._last_store_value = value
        self._pending_store_sync = False
        self._is_synchronized = True
        self._last_sync_error = None

    def _record_sync_failure(self, error: Exception) -> None:
        """非同期境界の失敗を状態とsignalで公開する。"""
        self._is_synchronized = False
        self._last_sync_error = error
        if not self.is_disposed:
            self.sync_failed.emit(error)

    def _on_endpoint_unavailable(self, notify_view_model: bool) -> None:
        """Maya同期と単位変換を解除し、Python Storeの編集は継続する。"""
        self._is_synchronized = False
        for connection in self._connections:
            _disconnect_qt_connection(connection)
        self._connections.clear()
        view_model = self._valid_view_model()
        if view_model is not None and self._release_view_model(view_model):
            view_model.set_presentation_adapter(None, notify=notify_view_model)

    @classmethod
    def _require_no_other_view(cls, view_model: FloatViewModel) -> None:
        """1つのViewModelへ複数のMaya Viewを接続しない。"""
        current_reference = cast(
            ReferenceType[MayaFloatPlugView] | None,
            getattr(view_model, cls._VIEW_REFERENCE_ATTRIBUTE, None),
        )
        current = (
            current_reference() if current_reference is not None else None
        )
        if current is not None and not current.is_disposed:
            raise RuntimeError(
                "1つのFloatViewModelへ複数のMayaFloatPlugViewを接続できません"
            )

    def _claim_view_model(self, view_model: FloatViewModel) -> None:
        """ViewModelへこのMaya Viewの弱参照を登録する。"""
        setattr(view_model, self._VIEW_REFERENCE_ATTRIBUTE, ref(self))

    def _release_view_model(self, view_model: FloatViewModel) -> bool:
        """自身が保持する接続枠だけを解放する。"""
        current_reference = cast(
            ReferenceType[MayaFloatPlugView] | None,
            getattr(view_model, self._VIEW_REFERENCE_ATTRIBUTE, None),
        )
        if current_reference is not None and current_reference() is self:
            delattr(view_model, self._VIEW_REFERENCE_ATTRIBUTE)
            return True
        return False
