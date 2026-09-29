# coding: utf-8
from __future__ import annotations

from typing import ClassVar, cast
from weakref import ReferenceType, ref

from maya.api import OpenMaya as om

from ....ui import StringViewModel, qt
from ....ui.binding.string._connection import disconnect_qt_connection
from ._string_plug_endpoint import StringPlugEndpoint
from .string_plug_resolver import MayaStringPlug

_VIEW_REFERENCE = "_bd_util_maya_string_plug_view_reference"


class MayaStringPlugStore(StringPlugEndpoint):
    """Mayaの単一string属性を正本として扱うStore。"""

    def __init__(
        self,
        view_model: StringViewModel,
        plug: MayaStringPlug,
        owner: qt.QObject,
    ) -> None:
        """既存plugの値を読み、変更を監視する。"""
        self._write_depth = 0
        super().__init__(view_model, plug, owner)

    def read(self) -> str:
        """未設定値を空文字として現在のMaya値を返す。"""
        return self._read_plug()

    def write(self, value: str) -> str:
        """Undo対応の書込み後に、通知先の再編集も含む実値を返す。"""
        self._write_depth += 1
        try:
            actual = self._write_plug(value)
        finally:
            self._write_depth -= 1
        self.refresh()
        return self.read() if self.is_available else actual

    def refresh(self) -> bool:
        """Maya実値と編集可否をViewModelへ反映する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self.dispose()
            return False
        if view_model.store is not self:
            return False
        if not self.is_available:
            view_model.store_became_unavailable(self)
            return False
        return view_model.refresh_from_store(self)

    def _validate_attached_view_model(
        self, view_model: StringViewModel
    ) -> None:
        """構築時に指定したViewModelだけへ接続させる。"""
        if view_model is not self.view_model:
            raise ValueError("別のStringViewModelへStoreを接続できません")

    def _callbacks_are_suppressed(self) -> bool:
        """自身の書込み通知を確定後の一回の読込みへまとめる。"""
        return self._write_depth > 0

    def _refresh_from_plug(self) -> bool:
        """Maya callbackを正本の再読込みへ変換する。"""
        return self.refresh()

    def _on_endpoint_unavailable(self) -> None:
        """対象削除や終了時はCommandを停止する。"""
        view_model = self._valid_view_model()
        if view_model is not None and view_model.store is self:
            view_model.store_became_unavailable(self)


class MayaStringPlugView(StringPlugEndpoint):
    """Python正本とMaya string属性を双方向同期するView。"""

    sync_failed = qt.Signal(object)
    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = True

    def __init__(
        self,
        view_model: StringViewModel,
        plug: MayaStringPlug,
        owner: qt.QObject,
    ) -> None:
        """Pythonの実値を初期適用し、Maya側の変更を監視する。"""
        if view_model.is_disposed or view_model.store is None:
            raise RuntimeError(
                "Maya View作成前にPython Storeを接続してください"
            )
        if isinstance(view_model.store, MayaStringPlugStore):
            raise RuntimeError("Maya正本へMaya Viewを追加できません")
        reference = cast(
            ReferenceType[MayaStringPlugView] | None,
            getattr(view_model, _VIEW_REFERENCE, None),
        )
        current = reference() if reference is not None else None
        if current is not None and not current.is_disposed:
            raise RuntimeError(
                "同じViewModelへ複数のMayaStringPlugViewを接続できません"
            )
        self._is_applying_value = False
        self._is_forwarding_plug_input = False
        self._is_history_input = False
        self._is_synchronized = False
        self._pending_store_sync = False
        self._last_sync_error: Exception | None = None
        self._connections: list[qt.QtCore.QMetaObject.Connection | None] = []
        super().__init__(view_model, plug, owner)
        try:
            setattr(view_model, _VIEW_REFERENCE, ref(self))
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
            self.dispose()
            self.deleteLater()
            raise

    @property
    def is_synchronized(self) -> bool:
        """PythonとMayaの確定値が一致するとき`True`。"""
        return self._is_synchronized and not self.is_disposed

    @property
    def last_sync_error(self) -> Exception | None:
        """直近の同期失敗を返す。成功後は`None`。"""
        return self._last_sync_error

    def sync_from_view_model(self) -> bool:
        """Pythonの確定値をMayaへ反映し、書込み有無を返す。"""
        self._is_history_input = False
        return self._sync_from_view_model(allow_write=True)

    def _sync_from_view_model(self, *, allow_write: bool) -> bool:
        """Undo/Redo中は書き戻さずに一致だけを判定する。"""
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
                        "StoreまたはMaya string plugを利用できません"
                    )
                value = view_model.value.value
                if self._read_plug() == value:
                    self._mark_synchronized()
                    return wrote
                if not allow_write:
                    raise RuntimeError(
                        "Undo/Redoの復元値とPython値が異なるため再同期を保留します"
                    )
                if not self.is_writable:
                    raise RuntimeError("Maya string plugへ書き込めません")
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
                if self._read_plug() != value:
                    raise RuntimeError(
                        "MayaへPythonの確定値を反映できませんでした"
                    )
                self._mark_synchronized()
                return wrote
        except Exception as error:
            self._pending_store_sync = True
            self._record_sync_failure(error)
            raise

    def _refresh_from_plug(self) -> bool:
        """Maya入力をPython Commandへ送り、補正後の実値を再同期する。"""
        if self._is_applying_value or self.is_disposed:
            return False
        view_model = self._valid_view_model()
        if view_model is None or view_model.is_disposed:
            self.dispose()
            return False
        try:
            if not self.is_available:
                raise RuntimeError("Maya string plugを利用できません")
            actual = self._read_plug()
            value = view_model.value.value
            if not self.is_writable:
                if actual == value:
                    self._mark_synchronized()
                    return False
                self._pending_store_sync = True
                raise RuntimeError(
                    "Maya plugが書込み不可のためPython値を維持します"
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
        """Python正本を再読込みし、元の入力失敗を公開する。"""
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

    def _callbacks_are_suppressed(self) -> bool:
        """Python値の書込み中にMaya callbackを折り返さない。"""
        return self._is_applying_value

    def _on_refresh_scheduled(self) -> None:
        """Maya入力の保留中は未同期として公開する。"""
        if om.MGlobal.isUndoing() or om.MGlobal.isRedoing():
            self._is_history_input = True
        self._is_synchronized = False

    def _history_input_received(self) -> None:
        """Undo/Redo後の入力でRedo履歴を消さないよう記録する。"""
        self._is_history_input = True

    def _on_attribute_message(self, message: int) -> None:
        """接続変更と値変更の優先方向を記録する。"""
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

    @qt.Slot(object)
    def _on_store_confirmation(self, _value: object) -> None:
        """同値CommandやrefreshもPython正本をMayaへ優先する。"""
        if self.is_disposed or self._is_forwarding_plug_input:
            return
        self._pending_store_sync = True
        try:
            self.sync_from_view_model()
        except Exception:
            pass

    def _mark_synchronized(self) -> None:
        """成功した同期状態とエラー解除を公開する。"""
        self._pending_store_sync = False
        self._is_synchronized = True
        self._last_sync_error = None

    def _record_sync_failure(self, error: Exception) -> None:
        """非同期境界で生じた失敗を状態とsignalに残す。"""
        self._is_synchronized = False
        self._last_sync_error = error
        if not self.is_disposed:
            self.sync_failed.emit(error)

    def _on_endpoint_unavailable(self) -> None:
        """Maya側だけを終了し、Python Storeの編集は継続する。"""
        self._is_synchronized = False
        for connection in self._connections:
            disconnect_qt_connection(connection)
        self._connections.clear()
        view_model = self._valid_view_model()
        if view_model is not None:
            reference = cast(
                ReferenceType[MayaStringPlugView] | None,
                getattr(view_model, _VIEW_REFERENCE, None),
            )
            if reference is not None and reference() is self:
                delattr(view_model, _VIEW_REFERENCE)
