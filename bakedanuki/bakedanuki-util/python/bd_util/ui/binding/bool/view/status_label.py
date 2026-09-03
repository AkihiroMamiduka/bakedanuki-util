# coding: utf-8
from __future__ import annotations

from .... import qt
from ..view_model import BoolViewModel


class BoolStatusLabel(qt.QLabel):
    """BoolViewModelをOff／On文字列で表示する読み取り専用View。"""

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
        self._update_text(view_model.value.value)

        view_model.value.changed.connect(self._update_text)
        view_model.destroyed.connect(self._on_view_model_destroyed)

    @property
    def view_model(self) -> BoolViewModel:
        """表示対象のViewModelを返す。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のBoolViewModelは破棄されています")
        return view_model

    def _update_text(self, value: bool) -> None:
        """ViewModelの実値に対応する表示文字列へ更新する。"""
        self.setText(self._true_text if value else self._false_text)

    def _valid_view_model(self) -> BoolViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        view_model = self._view_model
        if not qt.isValid(view_model):
            return None
        return view_model

    def _on_view_model_destroyed(
        self,
        _object: qt.QObject | None = None,
    ) -> None:
        """ViewModel破棄後は最終表示を残して無効状態にする。"""
        if qt.isValid(self):
            self.setEnabled(False)
