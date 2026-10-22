# coding: utf-8
"""登録したラジオボタンだけになぞり選択を追加する。"""

from collections.abc import Callable
from typing import cast

from . import qt
from ._button_sweep import ButtonSweep

__all__ = ["RadioButtonSweep"]


class RadioButtonSweep(ButtonSweep):
    """通常クリックを保ち、左ドラッグ中だけ通過したボタンを選択する。"""

    def __init__(self, scope: qt.QWidget) -> None:
        """操作領域と、明示入力先・同値要求の設定を保持する。"""
        super().__init__(scope)
        self._writers: dict[qt.QRadioButton, Callable[[], None]] = {}
        self._apply_unchanged: set[qt.QRadioButton] = set()
        self._visited: set[qt.QtWidgets.QAbstractButton] = set()

    def add_button(
        self,
        button: qt.QRadioButton,
        *,
        on_change: Callable[[], None] | None = None,
        apply_unchanged: bool = False,
        group: object | None = None,
    ) -> None:
        """対象と、なぞり中だけ使う明示入力先を登録する。

        Args:
            button: 表示範囲内のラジオボタン。
            on_change: 指定時は `click()` の代わりに呼び、表示同期も委ねる。
            apply_unchanged: Trueなら選択済みでも入力する。実際のboolに限る。
            group: 開始時に指定があれば、等しいgroupのボタンだけを通過する。
                Noneから開始した場合は全登録を対象にする。

        `on_change` または `apply_unchanged` の指定時は、同じボタンへの
        要求を一ドラッグ一回に限る。通常クリックとキー操作は変更しない。
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
        """操作を終了し、古い行と入力先への参照を解放する。"""
        super().clear()
        self._writers.clear()
        self._apply_unchanged.clear()
        self._visited.clear()

    def _prepare(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """新しい押下では、明示要求したボタンの記録を捨てる。"""
        self._visited.clear()

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
        """既定のクリックか明示入力を、一回制限と同値設定に従って行う。"""
        radio = cast(qt.QRadioButton, button)
        writer = self._writers.get(radio)
        apply_unchanged = radio in self._apply_unchanged
        if writer is not None or apply_unchanged:
            if radio in self._visited:
                return
            self._visited.add(radio)
        if radio.isChecked() and not apply_unchanged:
            return
        try:
            if writer is None:
                radio.click()
            else:
                writer()
        except Exception:
            self.finish()
            raise
