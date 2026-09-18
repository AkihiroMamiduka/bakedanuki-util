# coding: utf-8
"""登録したラジオボタンだけになぞり選択を追加する。"""

from typing import cast

from . import qt
from ._button_sweep import ButtonSweep

__all__ = ["RadioButtonSweep"]


class RadioButtonSweep(ButtonSweep):
    """通常クリックを保ち、左ドラッグ中だけ通過したボタンを選択する。"""

    def add_button(self, button: qt.QRadioButton) -> None:
        """表示範囲の子ボタンへ任意参加のドラッグ操作を追加する。"""
        self._add_button(button)

    def _click_rect(
        self, button: qt.QtWidgets.QAbstractButton
    ) -> qt.QtCore.QRect:
        """登録されたラジオボタンの標準クリック領域を返す。"""
        radio = cast(qt.QRadioButton, button)
        option = qt.QtWidgets.QStyleOptionButton()
        radio.initStyleOption(option)
        return radio.style().subElementRect(
            qt.QtWidgets.QStyle.SubElement.SE_RadioButtonClickRect,
            option,
            radio,
        )

    def _apply(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """選択済みへの再入力を避け、通常のクリック経路で選択する。"""
        if not button.isChecked():
            button.click()
