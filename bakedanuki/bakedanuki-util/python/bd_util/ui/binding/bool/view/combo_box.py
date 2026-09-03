# coding: utf-8
from __future__ import annotations

from .... import qt
from ..view_model import BoolViewModel
from ._connection import disconnect_qt_connection


class BoolComboBox(qt.QComboBox):
    """BoolViewModelをOff／On項目で表示・操作するコンボボックス。"""

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
        self.addItem(false_text, False)
        self.addItem(true_text, True)
        self._update_current_value(view_model.value.value)
        self.setEnabled(view_model.set_value_command.can_execute)

        self._current_index_connection: (
            qt.QtCore.QMetaObject.Connection | None
        ) = self.currentIndexChanged.connect(self._request_index)
        view_model.value.changed.connect(self._update_current_value)
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

    def _request_index(self, index: int) -> None:
        """選択項目のbool dataをCommandへ渡し、拒否時は実値へ戻す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._disable_binding()
            return

        value = self.itemData(index)
        if not isinstance(value, bool):
            self._update_current_value(view_model.value.value)
            raise RuntimeError("BoolComboBoxの選択項目にはbool dataが必要です")

        try:
            changed = view_model.set_value_command.execute(value)
        except Exception:
            self._update_current_value(view_model.value.value)
            raise
        if not changed:
            self._update_current_value(view_model.value.value)

    def _update_current_value(self, value: bool) -> None:
        """Commandを再実行せずViewModelの実値を表示する。"""
        index = self.findData(value)
        if index < 0:
            raise RuntimeError("BoolComboBoxに表示対象のbool dataがありません")

        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setCurrentIndex(index)
        finally:
            del blocker

    def _valid_view_model(self) -> BoolViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if not qt.isValid(view_model):
            return None
        return view_model

    def _disable_binding(self) -> None:
        """入力接続を解除してコンボボックスを無効にする。"""
        disconnect_qt_connection(self._current_index_connection)
        self._current_index_connection = None
        if qt.isValid(self):
            self.setEnabled(False)

    def _on_view_model_destroyed(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """ViewModel破棄後のUI入力を安全に停止する。"""
        self._disable_binding()
