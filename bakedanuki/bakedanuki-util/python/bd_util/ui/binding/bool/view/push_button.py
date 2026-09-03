# coding: utf-8
from __future__ import annotations

from .... import qt
from ..view_model import BoolViewModel
from ._connection import disconnect_qt_connection


class BoolPushButton(qt.QPushButton):
    """BoolViewModelを押下状態とOff／On文字列で表示・操作するボタン。"""

    def __init__(
        self,
        view_model: BoolViewModel,
        false_text: str = "Off",
        true_text: str = "On",
        parent: qt.QWidget | None = None,
    ) -> None:
        """ViewModel、False／Trueの表示文字列、任意の親Widgetで初期化する。"""
        super().__init__(parent)
        # Viewだけを保持するfactory構成でもbinding先を存続させる。
        self._view_model = view_model
        self._false_text = false_text
        self._true_text = true_text
        self.setCheckable(True)
        self._update_button(view_model.value.value)
        self.setEnabled(view_model.set_value_command.can_execute)

        self._toggled_connection: qt.QtCore.QMetaObject.Connection | None = (
            self.toggled.connect(self._request_value)
        )
        view_model.value.changed.connect(self._update_button)
        view_model.set_value_command.can_execute_changed.connect(
            self.setEnabled
        )
        view_model.destroyed.connect(self._on_view_model_destroyed)

    @property
    def view_model(self) -> BoolViewModel:
        """表示・操作対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のBoolViewModelは破棄されています")
        return view_model

    def _request_value(self, value: bool) -> None:
        """ユーザー入力をCommandへ渡し、拒否時は実値へ戻す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._disable_binding()
            return
        try:
            changed = view_model.set_value_command.execute(value)
        except Exception:
            self._update_button(view_model.value.value)
            raise
        if not changed:
            self._update_button(view_model.value.value)

    def _update_button(self, value: bool) -> None:
        """Commandを再実行せず押下状態と表示文字列を更新する。"""
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setChecked(value)
            self.setText(self._true_text if value else self._false_text)
        finally:
            del blocker

    def _valid_view_model(self) -> BoolViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if not qt.isValid(view_model):
            return None
        return view_model

    def _disable_binding(self) -> None:
        """入力接続を解除してボタンを無効にする。"""
        disconnect_qt_connection(self._toggled_connection)
        self._toggled_connection = None
        if qt.isValid(self):
            self.setEnabled(False)

    def _on_view_model_destroyed(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """ViewModel破棄後のUI入力を安全に停止する。"""
        self._disable_binding()
