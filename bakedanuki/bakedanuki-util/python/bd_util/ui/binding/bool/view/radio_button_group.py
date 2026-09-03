# coding: utf-8
from __future__ import annotations

from .... import qt
from ..view_model import BoolViewModel
from ._connection import disconnect_qt_connection


class BoolRadioButtonGroup(qt.QWidget):
    """BoolViewModelをFalse／Trueの排他的なRadioButtonで操作するView。"""

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
        self.false_button = qt.QRadioButton(false_text, self)
        self.true_button = qt.QRadioButton(true_text, self)
        self._button_group = qt.QtWidgets.QButtonGroup(self)
        self._button_group.setExclusive(True)
        self._button_group.addButton(self.false_button)
        self._button_group.addButton(self.true_button)

        layout = qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.false_button)
        layout.addWidget(self.true_button)
        layout.addStretch()

        self._update_buttons(view_model.value.value)
        self.setEnabled(view_model.set_value_command.can_execute)

        self._false_clicked_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self.false_button.clicked.connect(self._request_false)
        self._true_clicked_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self.true_button.clicked.connect(self._request_true)
        view_model.value.changed.connect(self._update_buttons)
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

    def _request_false(self, _checked: bool = False) -> None:
        """False側RadioButtonのユーザー入力をCommandへ渡す。"""
        self._request_value(False)

    def _request_true(self, _checked: bool = False) -> None:
        """True側RadioButtonのユーザー入力をCommandへ渡す。"""
        self._request_value(True)

    def _request_value(self, value: bool) -> None:
        """ユーザー入力をCommandへ渡し、拒否時は実値へ戻す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._disable_binding()
            return
        try:
            changed = view_model.set_value_command.execute(value)
        except Exception:
            self._update_buttons(view_model.value.value)
            raise
        if not changed:
            self._update_buttons(view_model.value.value)

    def _update_buttons(self, value: bool) -> None:
        """Commandを再実行せずViewModelの実値を選択状態へ反映する。"""
        false_blocker = qt.QtCore.QSignalBlocker(self.false_button)
        true_blocker = qt.QtCore.QSignalBlocker(self.true_button)
        try:
            button = self.true_button if value else self.false_button
            button.setChecked(True)
        finally:
            del true_blocker
            del false_blocker

    def _valid_view_model(self) -> BoolViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if not qt.isValid(view_model):
            return None
        return view_model

    def _disable_binding(self) -> None:
        """入力接続を解除してRadioButtonを無効にする。"""
        disconnect_qt_connection(self._false_clicked_connection)
        disconnect_qt_connection(self._true_clicked_connection)
        self._false_clicked_connection = None
        self._true_clicked_connection = None
        if qt.isValid(self):
            self.setEnabled(False)

    def _on_view_model_destroyed(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """ViewModel破棄後のUI入力を安全に停止する。"""
        self._disable_binding()
