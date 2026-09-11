# coding: utf-8
from __future__ import annotations

from typing import ClassVar
from weakref import ref

from maya.api import OpenMaya as om

from ....ui import FloatPresentation, FloatViewModel, qt
from .float_plug_resolver import MayaFloatPlug
from ._float_view_attachment import (
    claim_view_slot,
    release_view_slot,
    require_view_slot,
)
from ._float_plug_endpoint import (
    FloatPlugEndpoint,
    disconnect_qt_connection,
    require_float_view_model,
)


class MayaFloatPlugStore(FloatPlugEndpoint):
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


class MayaFloatPlugView(FloatPlugEndpoint):
    """Python正本の確定値とMaya浮動小数点plugを双方向同期するView。"""

    sync_failed = qt.Signal(object)
    _DEFER_ATTRIBUTE_CHANGES: ClassVar[bool] = True

    def __init__(
        self,
        view_model: FloatViewModel,
        plug: MayaFloatPlug,
        owner: qt.QObject,
    ) -> None:
        """Python値を初期同期し、Maya入力と表示単位のcallbackを接続する。"""
        view_model = require_float_view_model(view_model)
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
            disconnect_qt_connection(connection)
        self._connections.clear()
        view_model = self._valid_view_model()
        if view_model is not None and self._release_view_model(view_model):
            view_model.set_presentation_adapter(None, notify=notify_view_model)

    @classmethod
    def _require_no_other_view(cls, view_model: FloatViewModel) -> None:
        """1つのViewModelへ複数のMaya Viewを接続しない。"""
        require_view_slot(view_model, "MayaFloatPlugView")

    def _claim_view_model(self, view_model: FloatViewModel) -> None:
        """ViewModelへこのMaya Viewの弱参照を登録する。"""
        claim_view_slot(view_model, self)

    def _release_view_model(self, view_model: FloatViewModel) -> bool:
        """自身が保持する接続枠だけを解放する。"""
        return release_view_slot(view_model, self)
