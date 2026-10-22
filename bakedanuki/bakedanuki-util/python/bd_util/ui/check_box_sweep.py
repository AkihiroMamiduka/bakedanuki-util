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
        self._apply_unchanged: set[qt.QCheckBox] = set()
        self._visited: set[qt.QtWidgets.QAbstractButton] = set()
        self._checked = True

    def add_button(
        self,
        button: qt.QCheckBox,
        *,
        on_change: Callable[[bool], None] | None = None,
        apply_unchanged: bool = False,
        group: object | None = None,
    ) -> None:
        """対象を登録し、入力先の指定時は表示同期もその入力先へ委ねる。

        Args:
            button: 表示範囲内のチェックボックス。
            on_change: なぞり時だけ呼ぶ入力先。通常クリックは変更しない。
            apply_unchanged: Trueなら表示が同じでも `on_change` を呼ぶ。
                実際のboolに限り、入力先未指定なら表示同期だけを行う。
            group: 開始時に指定があれば、等しいgroupのボタンだけを通過する。
                Noneから開始した場合は全登録を対象にする。
        """
        if type(apply_unchanged) is not bool:
            raise TypeError("apply_unchangedにはboolを指定してください")
        self._add_button(button, group=group)
        if on_change is None:
            self._writers.pop(button, None)
        else:
            self._writers[button] = on_change
        if apply_unchanged:
            self._apply_unchanged.add(button)
        else:
            self._apply_unchanged.discard(button)

    def clear(self) -> None:
        """操作を終了し、古い行や入力先への参照も解放する。"""
        super().clear()
        self._writers.clear()
        self._apply_unchanged.clear()
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
        """同じ行は一度だけ処理し、明示設定時は同値でも入力を要求する。"""
        if button in self._visited:
            return
        self._visited.add(button)
        check_box = cast(qt.QCheckBox, button)
        state = (
            qt.Qt.CheckState.Checked
            if self._checked
            else qt.Qt.CheckState.Unchecked
        )
        if (
            check_box.checkState() == state
            and check_box not in self._apply_unchanged
        ):
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
