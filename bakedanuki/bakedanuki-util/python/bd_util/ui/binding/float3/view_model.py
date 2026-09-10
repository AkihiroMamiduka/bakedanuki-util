# coding: utf-8
from __future__ import annotations

from ... import qt
from ..float.view_model import FloatViewModel
from ..float.view._connection import connect_queued_qt_signal
from .command import SetFloat3Command
from .store import Float3ValueStore
from .value import Float3, Float3Value, require_float3


class _MutableFloat3Value(Float3Value):
    """ViewModel専用の値更新を提供する。"""

    def replace(self, value: Float3) -> bool:
        """変更された場合だけ確定値を置き換えて通知する。"""
        if value == self._value:
            return False
        self._value = value
        self.changed.emit(value)
        return True


class _MutableSetFloat3Command(SetFloat3Command):
    """ViewModel専用の実行可否更新を提供する。"""

    def set_can_execute(self, value: bool) -> None:
        """実行可否が変わった場合だけ通知する。"""
        if value != self._can_execute:
            self._can_execute = value
            self.can_execute_changed.emit(value)


class Float3ViewModel(qt.QObject):
    """各軸のFloatViewModelと3成分の確定値・一括Commandをまとめる。"""

    def __init__(self, parent: qt.QObject | None = None) -> None:
        """各軸のViewModelを所有し、単一のStoreの接続を待つ。"""
        super().__init__(parent)
        self._is_disposed = False
        self._refreshing = False
        self._attaching = False
        self._write_depth = 0
        self._store: Float3ValueStore | None = None
        self._value = _MutableFloat3Value(self)
        self._command = _MutableSetFloat3Command(self._request_value, self)
        self._components = tuple(FloatViewModel(parent=self) for _ in range(3))

        # scalar側の確定・編集可否通知から全体の状態を同期する。
        for component in self._components:
            component.value.changed.connect(self._on_component_refreshed)
            component.store_refreshed.connect(self._on_component_refreshed)
            component.set_value_command.can_execute_changed.connect(
                self._on_component_state_changed
            )
            connect_queued_qt_signal(
                component.destroyed, self._on_component_destroyed
            )

    @property
    def x(self) -> FloatViewModel:
        """X成分のViewModelを返す。"""
        return self._components[0]

    @property
    def y(self) -> FloatViewModel:
        """Y成分のViewModelを返す。"""
        return self._components[1]

    @property
    def z(self) -> FloatViewModel:
        """Z成分のViewModelを返す。"""
        return self._components[2]

    @property
    def value(self) -> Float3Value:
        """読み取り専用の3成分値を返す。"""
        return self._value

    @property
    def set_value_command(self) -> SetFloat3Command:
        """3成分を一括設定するCommandを返す。"""
        return self._command

    @property
    def store(self) -> Float3ValueStore | None:
        """接続中の3成分Storeを返す。"""
        return self._store

    @property
    def is_disposed(self) -> bool:
        """入力・同期を終了したか返す。"""
        return self._is_disposed or not qt.isValid(self)

    def attach_store(self, store: Float3ValueStore) -> None:
        """各軸のStoreを接続し、正本から初期表示を同期する。"""
        if self.is_disposed or self._store is not None:
            raise RuntimeError("Float3ViewModelへStoreを追加接続できません")
        self._store = store
        self._attaching = True
        try:
            if len(store.components) != 3:
                raise ValueError("Storeには3成分が必要です")
            for component, source in zip(self._components, store.components):
                component.attach_store(source)
            if isinstance(store, qt.QObject):
                connect_queued_qt_signal(
                    store.destroyed, self._on_store_destroyed
                )
        except Exception:
            self.dispose()
            raise
        finally:
            self._attaching = False
        self.refresh()

    def refresh(self) -> bool:
        """各軸の表示情報と編集可否を揃え、最新の3成分値を通知する。"""
        if (
            self.is_disposed
            or self._attaching
            or self._refreshing
            or self._write_depth > 0
        ):
            return False
        store = self._store
        if store is None:
            return False
        changed = False
        self._refreshing = True
        try:
            while not self.is_disposed:
                if not store.is_available:
                    self._disable_commands()
                    return changed
                before = require_float3(store.read())
                for component, source in zip(
                    self._components, store.components
                ):
                    if self.is_disposed:
                        return changed
                    component.refresh_from_store(source)
                if self.is_disposed:
                    return changed
                if not store.is_available:
                    self._disable_commands()
                    return changed
                actual = require_float3(store.read())
                # 通知slotが正本を変更した場合は、各軸を最新値へ揃え直す。
                if actual != before:
                    continue
                self._command.set_can_execute(store.is_writable)
                if self.is_disposed:
                    return changed
                changed = self._value.replace(actual) or changed
                if self.is_disposed or not store.is_available:
                    return changed
                if require_float3(store.read()) == actual:
                    return changed
            return changed
        finally:
            self._refreshing = False

    def _request_value(self, value: Float3) -> bool:
        """一括書き込み中の全体通知をまとめ、処理後に正本を読み直す。"""
        store = self._store
        if self.is_disposed or store is None or not store.is_available:
            return False
        if not store.is_writable:
            self.refresh()
            return False
        before = require_float3(store.read())
        if value == before:
            self.refresh()
            return False
        self._write_depth += 1
        try:
            try:
                actual = require_float3(store.write(value))
            finally:
                self._write_depth -= 1
        except Exception:
            # 書き込み後の失敗でも実値へ復旧し、復旧失敗で元の例外を隠さない。
            try:
                self.refresh()
            except Exception:
                self._disable_commands()
            raise
        self.refresh()
        return actual != before

    def _disable_commands(self) -> None:
        """正本が利用できなくなった場合に全成分の入力を停止する。"""
        self._command.set_can_execute(False)
        for component in self._components:
            if self.is_disposed:
                return
            if qt.isValid(component) and component.store is not None:
                component.store_became_unavailable(component.store)

    def dispose(self) -> None:
        """所有する各軸の入力と同期を終了する。"""
        if self.is_disposed:
            return
        self._is_disposed = True
        self._command.set_can_execute(False)
        for component in self._components:
            if qt.isValid(component):
                component.dispose()

    @qt.Slot(float)
    def _on_component_refreshed(self, _value: float) -> None:
        """各軸の確定通知を全体の再同期へ渡す。"""
        self.refresh()

    @qt.Slot(bool)
    def _on_component_state_changed(self, _enabled: bool) -> None:
        """各軸の値確定へ再入せず、一括Commandの実行可否を更新する。"""
        if self.is_disposed or self._attaching or self._refreshing:
            return
        store = self._store
        if store is not None:
            self._command.set_can_execute(
                store.is_available
                and store.is_writable
                and all(
                    component.set_value_command.can_execute
                    for component in self._components
                )
            )

    @qt.Slot()
    def _on_store_destroyed(self) -> None:
        """StoreのQObject破棄後に残った入力経路を停止する。"""
        self.dispose()

    @qt.Slot()
    def _on_component_destroyed(self) -> None:
        """所有する成分が外部から破棄された場合に全体を停止する。"""
        self.dispose()
