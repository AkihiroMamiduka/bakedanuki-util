# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import ClassVar, Generic, Protocol, TypeVar, cast
from weakref import ref

from maya import cmds
from maya.api import OpenMaya as om

from ....ui import (
    Float3,
    Float3ViewModel,
    FloatPresentation,
    FloatViewModel,
    qt,
)
from ....ui.binding.float3.value import require_float3
from ._float_plug_endpoint import (
    FloatPlugEndpoint,
    disconnect_qt_connection,
    require_owner,
    run_later,
)
from ._float_view_attachment import (
    claim_view_slot,
    release_view_slot,
    require_view_slot,
)
from .float_plug import MayaFloatPlugStore
from .float_plug_resolver import MayaFloatPlug, resolve_float_plug
from .float3_plug import MayaFloat3PlugStore
from .float3_plug_resolver import MayaFloat3Plug, require_float3_plug

_PlugT = TypeVar("_PlugT", bound=MayaFloat3Plug, covariant=True)


class _SetFloat3Attr(Protocol):
    """親setAttrの可変長引数を3成分の型境界へ限定する。"""

    def __call__(
        self, name: str, x: float, y: float, z: float, *, type: str
    ) -> None:
        """Maya親属性へ3成分を1回で設定する。"""
        raise NotImplementedError


class _ComponentPlugView(FloatPlugEndpoint):
    """各軸のMaya通知を3成分Viewへ集約する内部endpoint。"""

    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = True

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        group: MayaFloat3PlugView[MayaFloat3Plug],
        index: int,
    ) -> None:
        """単一値版の単位変換・callback・寿命管理を再利用する。"""
        self._group = group
        self._index = index
        super().__init__(view_model, plug, group)

    def read(self) -> float:
        """この軸のMaya実値を公開単位で返す。"""
        return self._read_plug()

    def matches(self, value: float) -> bool:
        """Python値の格納結果とこの軸の実値が一致するか返す。"""
        return self._codec.matches(value)

    def prepare(self, value: float) -> float:
        """Mayaの範囲と格納精度を事前検証し、現在単位の入力値を返す。"""
        presentation = self._codec.presentation
        if presentation.minimum is not None and value < presentation.minimum:
            raise ValueError("Python値はMaya属性の下限未満です")
        if presentation.maximum is not None and value > presentation.maximum:
            raise ValueError("Python値はMaya属性の上限を超えています")
        return self._codec.to_ui(value)

    def write(self, value: float) -> float:
        """事前検証済みの単独成分をMayaへ反映する。"""
        return self._write_plug(value)

    def present(self, presentation: FloatPresentation) -> FloatPresentation:
        """Python範囲を維持してMayaの表示単位を適用する。"""
        maya_presentation = self._codec.presentation
        return FloatPresentation(
            maya_presentation.scale,
            maya_presentation.suffix,
            presentation.minimum,
            presentation.maximum,
        )

    def _callbacks_are_suppressed(self) -> bool:
        """親による一括描画のechoを抑制する。"""
        return self._group.is_applying_value or self._group.is_disposed

    def _schedule_refresh(self) -> None:
        """各軸で別々のsetterを呼ばず、親の遅延同期へまとめる。"""
        if not self._callbacks_are_suppressed():
            self._group.schedule_refresh(self._index)

    def _refresh_from_plug(self) -> bool:
        """この軸の入力を親の同期対象へ追加する。"""
        self._schedule_refresh()
        return False

    def _on_attribute_message(self, _message: int) -> None:
        """接続・lock・Undoによる優先方向を親へ渡す。"""
        self._group.attribute_changed(self._index, _message)

    def _on_unit_changed(self, *_args: object) -> None:
        """単位変更ではPython値や保留入力を変更しない。"""
        self._group.on_unit_changed()

    def _on_endpoint_unavailable(self, notify_view_model: bool) -> None:
        """1成分の終了で親全体のcallbackを停止する。"""
        self._group.dispose_endpoint(notify_view_model=notify_view_model)


class MayaFloat3PlugView(qt.QObject, Generic[_PlugT]):
    """Pythonの3成分tupleを正本としてMaya compoundと双方向同期する。"""

    sync_failed = qt.Signal(object)

    def __init__(
        self, view_model: Float3ViewModel, plug: _PlugT, owner: qt.QObject
    ) -> None:
        """全成分を検証して接続し、Python初期値をMayaへまとめて適用する。"""
        view_model = _require_view_model(view_model)
        require_float3_plug(plug)
        owner = require_owner(owner)
        store = view_model.store
        if view_model.is_disposed or store is None:
            raise RuntimeError(
                "有効なFloat3ViewModelへStoreを接続してください"
            )
        if isinstance(store, MayaFloat3PlugStore) or any(
            isinstance(component, MayaFloatPlugStore)
            for component in store.components
        ):
            raise RuntimeError(
                "MayaFloat3PlugViewにはPython側を正本とするStoreを接続してください"
            )
        for target in (view_model, view_model.x, view_model.y, view_model.z):
            require_view_slot(target, "MayaFloat3PlugView")
        super().__init__(owner)
        self._view_model: Float3ViewModel | None = view_model
        self._view_model_ref = ref(view_model)
        self._plug_operator = plug
        self._plug = plug.plug
        self._attribute_handle = om.MObjectHandle(self._plug.attribute())
        self._is_disposed = False
        self._is_applying_value = False
        self._is_forwarding_input = False
        self._is_synchronized = False
        self._is_history_input = False
        self._refresh_scheduled = False
        self._pending_python: set[int] = {0, 1, 2}
        self._input_axes: set[int] = set()
        self._last_sync_error: Exception | None = None
        self._last_python: Float3 | None = None
        self._last_maya: Float3 | None = None
        self._observed: Float3 = (0.0, 0.0, 0.0)
        self._components: list[_ComponentPlugView] = []
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = []
        self._data_type = (
            "float3"
            if om.MFnNumericAttribute(self._plug.attribute()).numericType()
            == om.MFnNumericData.k3Float
            else "double3"
        )

        # 3軸のcallbackは監視専用とし、入力と描画はこの親Viewだけが実行する。
        try:
            for index, component in enumerate(
                (view_model.x, view_model.y, view_model.z)
            ):
                name = cast(
                    str,
                    om.MFnAttribute(self._plug.child(index).attribute()).name,
                )
                child = resolve_float_plug(plug.node.cmd_access_name, name)
                self._components.append(
                    _ComponentPlugView(component, child, self, index)
                )
            for target in (
                view_model,
                view_model.x,
                view_model.y,
                view_model.z,
            ):
                claim_view_slot(target, self)
            self._observed = self._read_actual()
            self.refresh_presentation()
            self._connections.extend(
                (
                    view_model.value.changed.connect(
                        self._on_store_confirmation
                    ),
                    view_model.store_refreshed.connect(
                        self._on_store_confirmation
                    ),
                    view_model.set_value_command.executed.connect(
                        self._on_store_confirmation
                    ),
                )
            )
            self.sync_from_view_model()
        except Exception:
            self.dispose()
            self.deleteLater()
            raise

    @property
    def view_model(self) -> Float3ViewModel:
        """生存中の同期先ViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("同期対象のFloat3ViewModelは破棄されています")
        return view_model

    @property
    def plug_operator(self) -> _PlugT:
        """接続先の親plugを具体型のまま返す。"""
        return self._plug_operator

    @property
    def is_disposed(self) -> bool:
        """明示終了またはQt ownerの破棄によって終了したか返す。"""
        return self._is_disposed or not qt.isValid(self)

    @property
    def is_available(self) -> bool:
        """親と全成分のMaya属性が利用可能か返す。"""
        return (
            not self.is_disposed
            and self._attribute_handle.isValid()
            and len(self._components) == 3
            and all(component.is_available for component in self._components)
        )

    @property
    def is_writable(self) -> bool:
        """親属性への一括描画が可能か返す。"""
        return (
            self.is_available
            and bool(om.MFnAttribute(self._plug.attribute()).writable)
            and all(component.is_writable for component in self._components)
        )

    @property
    def is_applying_value(self) -> bool:
        """各軸のechoを抑止する描画中の状態を返す。"""
        return self._is_applying_value

    @property
    def is_synchronized(self) -> bool:
        """3成分すべてがPython確定値の格納結果と一致しているか返す。"""
        view_model = self._valid_view_model()
        return (
            self._is_synchronized
            and self.is_available
            and view_model is not None
            and not view_model.is_disposed
        )

    @property
    def last_sync_error(self) -> Exception | None:
        """直近の同期失敗を返し、成功後はNoneとする。"""
        return self._last_sync_error

    def _valid_view_model(self) -> Float3ViewModel | None:
        """C++ objectが生存するViewModelだけを返す。"""
        view_model = self._view_model or self._view_model_ref()
        return (
            view_model
            if view_model is not None and qt.isValid(view_model)
            else None
        )

    def _read_actual(self) -> Float3:
        """全軸のMaya実値を公開単位で読み取る。"""
        if not self.is_available:
            raise RuntimeError("同期対象のMaya 3成分plugは利用できません")
        return require_float3(
            tuple(component.read() for component in self._components)
        )

    def _matches(self, index: int, value: float, actual: float) -> bool:
        """確認済みの投影または今回の格納結果と一致するか判定する。"""
        # Mayaから受け入れた公開値を再変換して角度の丸め誤差を作らない。
        if value == actual:
            return True
        if (
            self._last_python is not None
            and self._last_maya is not None
            and value == self._last_python[index]
            and actual == self._last_maya[index]
        ):
            return True
        return self._components[index].matches(value)

    def sync_from_view_model(self) -> bool:
        """最後に確定したPython tupleを明示再同期し、失敗時は例外を返す。"""
        self._is_history_input = False
        self._input_axes.clear()
        self._pending_python.update(range(3))
        return self._sync_from_view_model(allow_write=True)

    def _sync_from_view_model(self, *, allow_write: bool) -> bool:
        """変更軸を事前検証して描画し、途中だけMayaへ反映しない。"""
        if self._is_applying_value:
            return False
        wrote = False
        try:
            while True:
                view_model = self.view_model
                store = view_model.store
                if (
                    view_model.is_disposed
                    or store is None
                    or not store.is_available
                ):
                    raise RuntimeError(
                        "同期対象のPython Storeは利用できません"
                    )
                value = view_model.value.value
                actual = self._read_actual()
                changed = [
                    index
                    for index in range(3)
                    if not self._matches(index, value[index], actual[index])
                ]
                if not changed:
                    self._mark_synchronized(value, actual)
                    return wrote
                if not allow_write:
                    raise RuntimeError(
                        "Undo/Redoの復元値とPython確定値が異なるため再同期を保留します"
                    )

                # 単独成分は子へ、複数成分は親へ1回で書き込み、Undoをまとめる。
                if len(changed) == 1:
                    index = changed[0]
                    if not self._components[index].is_writable:
                        raise RuntimeError(
                            "同期対象のMaya成分へ書き込めません"
                        )
                    self._components[index].prepare(value[index])
                    ui_values = None
                else:
                    if not self.is_writable:
                        raise RuntimeError(
                            "同期対象のMaya 3成分plugへ一括で書き込めません"
                        )
                    ui_values = tuple(
                        component.prepare(item)
                        for component, item in zip(self._components, value)
                    )
                self._is_applying_value = True
                try:
                    if ui_values is None:
                        self._components[changed[0]].write(value[changed[0]])
                    else:
                        set_attr = cast(_SetFloat3Attr, cmds.setAttr)
                        path = self._plug.partialName(
                            useFullAttributePath=True, useLongNames=True
                        )
                        set_attr(
                            f"{self._plug_operator.node.cmd_access_name}.{path}",
                            *ui_values,
                            type=self._data_type,
                        )
                    wrote = True
                finally:
                    self._is_applying_value = False
                if self.is_disposed or view_model.is_disposed:
                    return wrote
                if view_model.value.value != value:
                    continue
                actual = self._read_actual()
                if not all(
                    self._matches(i, value[i], actual[i]) for i in range(3)
                ):
                    raise RuntimeError(
                        "Maya 3成分plugへPython確定値を反映できませんでした"
                    )
                self._mark_synchronized(value, actual)
                return wrote
        except Exception as error:
            self._pending_python.update(range(3))
            self._record_sync_failure(error)
            raise

    def schedule_refresh(self, index: int) -> None:
        """同じtick内の各軸通知をまとめ、親変更を1つのPython入力にする。"""
        if self.is_disposed or self._is_applying_value:
            return
        self._input_axes.add(index)
        if om.MGlobal.isUndoing() or om.MGlobal.isRedoing():
            self._is_history_input = True
        self._is_synchronized = False
        if not self._refresh_scheduled:
            self._refresh_scheduled = True
            run_later(self._refresh_after_callback)

    def attribute_changed(self, index: int, message: int) -> None:
        """接続評価を入力とせず、後から来た編集とUndoの順序を保持する。"""
        if index >= len(self._components) or self.is_disposed:
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
            self._pending_python.add(index)
        elif (
            message & om.MNodeMessage.kAttributeSet
            and self._components[index].is_writable
        ):
            self._pending_python.discard(index)

    def _refresh_after_callback(self) -> None:
        """Mayaの確定値を読み、変更された編集可能な軸だけをPythonへ渡す。"""
        self._refresh_scheduled = False
        if self.is_disposed:
            return
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            self.dispose()
            return
        axes, self._input_axes = self._input_axes, set()
        try:
            actual = self._read_actual()
            previous, self._observed = self._observed, actual
            store = view_model.store
            if store is None or not store.is_available:
                view_model.refresh()
                raise RuntimeError("同期対象のPython Storeは利用できません")
            try:
                current = require_float3(store.read())
            except Exception:
                view_model.refresh()
                raise
            incoming = [
                i
                for i in axes
                if actual[i] != previous[i]
                and i not in self._pending_python
                and self._components[i].is_writable
                and not self._matches(i, current[i], actual[i])
            ]
            if incoming:
                if not view_model.set_value_command.can_execute:
                    raise RuntimeError(
                        "Python Storeが書き込み不可のためMaya入力を反映できません"
                    )
                self._is_forwarding_input = True
                try:
                    if len(incoming) == 1:
                        index = incoming[0]
                        (view_model.x, view_model.y, view_model.z)[
                            index
                        ].set_value_command.execute(actual[index])
                    else:
                        values = require_float3(
                            tuple(
                                actual[i] if i in incoming else current[i]
                                for i in range(3)
                            )
                        )
                        view_model.set_value_command.execute(values)
                except Exception as error:
                    self._restore_after_input_error(error)
                    return
                finally:
                    self._is_forwarding_input = False
            if not self.is_disposed and not view_model.is_disposed:
                self._sync_from_view_model(
                    allow_write=not self._is_history_input
                )
        except Exception as error:
            self._record_sync_failure(error)

    def _restore_after_input_error(self, error: Exception) -> None:
        """正本が読める場合だけ復旧し、元のsetter例外を保持する。"""
        view_model = self._valid_view_model()
        if self.is_disposed or view_model is None or view_model.is_disposed:
            return
        try:
            view_model.refresh()
            self._sync_from_view_model(allow_write=not self._is_history_input)
        except Exception:
            pass
        self._record_sync_failure(error)

    @qt.Slot(object)
    def _on_store_confirmation(self, _value: object) -> None:
        """同値の確定も未処理のMaya入力より優先し、全体を再同期する。"""
        if self.is_disposed or self._is_forwarding_input:
            return
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def refresh_presentation(self) -> None:
        """各軸の範囲を維持したまま、Mayaの表示単位だけを更新する。"""
        if not self.is_available:
            return
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            return
        view_reference = ref(self)

        def make_adapter(
            index: int,
        ) -> Callable[[FloatPresentation], FloatPresentation]:
            """Qt破棄後のViewを保持しない成分別の表示変換を生成する。"""

            def present(presentation: FloatPresentation) -> FloatPresentation:
                """終了後は元のPython側表示情報を使用する。"""
                view = view_reference()
                if view is None or not view.is_available:
                    return presentation
                return view._components[index].present(presentation)

            return present

        for index, component in enumerate(
            (view_model.x, view_model.y, view_model.z)
        ):
            component.set_presentation_adapter(make_adapter(index))

    def on_unit_changed(self) -> None:
        """Mayaの単位callback境界で表示更新の例外を保持する。"""
        try:
            self.refresh_presentation()
        except Exception as error:
            self._record_sync_failure(error)

    def _mark_synchronized(self, value: Float3, actual: Float3) -> None:
        """確認済みのPython値とMaya格納値を保持し、保留状態を解除する。"""
        self._last_python, self._last_maya = value, actual
        self._observed = actual
        self._pending_python.clear()
        self._is_synchronized = True
        self._last_sync_error = None

    def _record_sync_failure(self, error: Exception) -> None:
        """非同期境界の失敗を公開し、Pythonの編集可否は変更しない。"""
        self._is_synchronized = False
        self._last_sync_error = error
        if not self.is_disposed:
            self.sync_failed.emit(error)

    def dispose(self) -> None:
        """Maya同期を終了し、Python正本とQt編集は継続する。"""
        self.dispose_endpoint()

    def dispose_endpoint(self, *, notify_view_model: bool = True) -> None:
        """各軸のcallbackを即座に解除し、共有親の破棄中はQtへ再入しない。"""
        if self._is_disposed:
            return
        self._is_disposed = True
        self._refresh_scheduled = False
        self._input_axes.clear()
        self._is_synchronized = False
        for connection in self._connections:
            disconnect_qt_connection(connection)
        self._connections.clear()
        for component in self._components:
            if qt.isValid(component):
                component.dispose()
        view_model = self._valid_view_model()
        if view_model is not None:
            release_view_slot(view_model, self)
            for component in (view_model.x, view_model.y, view_model.z):
                if release_view_slot(component, self) and qt.isValid(
                    component
                ):
                    component.set_presentation_adapter(
                        None, notify=notify_view_model
                    )
        self._view_model = None


def _require_view_model(value: object) -> Float3ViewModel:
    """runtime値を3成分ViewModelとして検証する。"""
    if not isinstance(value, Float3ViewModel):
        raise TypeError("view_modelにはFloat3ViewModelを指定してください")
    return value
