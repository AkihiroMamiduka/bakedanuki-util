# coding: utf-8
"""登録したチェックボックスを、押下元で決めた状態へなぞって揃える。"""

from collections.abc import Callable
from typing import cast

from . import qt
from ._button_sweep import ButtonSweep

__all__ = ["CheckBoxSweep"]


class CheckBoxSweep(ButtonSweep):
    """Checkedからは解除、それ以外からはチェックへ揃える。"""

    def __init__(self, scope: qt.QWidget) -> None:
        """操作領域と、各ボタンの明示入力先を保持する。"""
        super().__init__(scope)
        self._writers: dict[qt.QCheckBox, Callable[[bool], None]] = {}
        self._visited: set[qt.QtWidgets.QAbstractButton] = set()
        self._checked = True

    def add_button(
        self,
        button: qt.QCheckBox,
        *,
        on_change: Callable[[bool], None] | None = None,
    ) -> None:
        """対象を登録し、入力先の指定時は表示同期もその入力先へ委ねる。"""
        self._add_button(button)
        if on_change is None:
            self._writers.pop(button, None)
        else:
            self._writers[button] = on_change

    def clear(self) -> None:
        """操作を終了し、古い行や入力先への参照も解放する。"""
        super().clear()
        self._writers.clear()
        self._visited.clear()

    def _prepare(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """押下時の三状態から入力値を固定し、前の通過記録を捨てる。"""
        self._checked = (
            cast(qt.QCheckBox, button).checkState() != qt.Qt.CheckState.Checked
        )
        self._visited.clear()

    def _click_rect(
        self, button: qt.QtWidgets.QAbstractButton
    ) -> qt.QtCore.QRect:
        """登録されたチェックボックスの標準クリック領域を返す。"""
        check_box = cast(qt.QCheckBox, button)
        option = qt.QtWidgets.QStyleOptionButton()
        check_box.initStyleOption(option)
        return check_box.style().subElementRect(
            qt.QtWidgets.QStyle.SubElement.SE_CheckBoxClickRect,
            option,
            check_box,
        )

    def _apply(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """同じ行は一度だけ処理し、混在を含む異なる状態だけを揃える。"""
        if button in self._visited:
            return
        self._visited.add(button)
        check_box = cast(qt.QCheckBox, button)
        state = (
            qt.Qt.CheckState.Checked
            if self._checked
            else qt.Qt.CheckState.Unchecked
        )
        if check_box.checkState() == state:
            return
        writer = self._writers.get(check_box)
        if writer is None:
            check_box.setCheckState(state)
        else:
            try:
                writer(self._checked)
            except Exception:
                self.finish()
                raise
