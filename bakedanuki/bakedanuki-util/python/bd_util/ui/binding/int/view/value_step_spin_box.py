# coding: utf-8
from __future__ import annotations

from .... import qt
from .._connection import connect_queued
from .._validation import require_step
from ..binding import IntBinding
from ..store import IntValueStore
from ..view_model import IntViewModel
from ._source import resolve_int_view_source
from .spin_box import IntSpinBox
from .step_spin_box import IntStepMode, IntStepSpinBox, require_step_mode


def _require_width(value: object, name: str) -> int | None:
    """自動幅のNoneまたはQtが扱える正の固定幅を検証する。"""
    if value is None:
        return None
    if type(value) is not int:
        raise TypeError(f"{name}にはintまたはNoneを指定してください")
    if not 1 <= value <= 16777215:
        raise ValueError(f"{name}は1～16777215にしてください")
    return value


class IntValueStepSpinBox(qt.QWidget):
    """整数値とView固有のStepを横に並べ、Stepを正本へ書かないView。"""

    settingsChanged = qt.Signal()

    def __init__(
        self,
        view_model: IntViewModel | IntBinding[IntValueStore],
        parent: qt.QWidget | None = None,
        *,
        single_step: int = 1,
        step_mode: IntStepMode = "additive",
        step_increment: int = 1,
        value_wheel_requires_focus: bool = False,
        step_wheel_requires_focus: bool = True,
        value_select_all_on_mouse_focus: bool = False,
        step_select_all_on_mouse_focus: bool = False,
        value_width: int | None = None,
        step_width: int = 68,
    ) -> None:
        """整数BindingまたはViewModelと、両欄の操作設定を指定する。"""
        view_model, binding = resolve_int_view_source(view_model)
        if view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        single_step = require_step(single_step)
        step_mode = require_step_mode(step_mode)
        step_increment = require_step(step_increment, "step_increment")
        for name, option in (
            ("value_wheel_requires_focus", value_wheel_requires_focus),
            ("step_wheel_requires_focus", step_wheel_requires_focus),
            (
                "value_select_all_on_mouse_focus",
                value_select_all_on_mouse_focus,
            ),
            ("step_select_all_on_mouse_focus", step_select_all_on_mouse_focus),
        ):
            if type(option) is not bool:
                raise TypeError(f"{name}にはboolを指定してください")
        value_width = _require_width(value_width, "value_width")
        checked_step_width = _require_width(step_width, "step_width")
        if checked_step_width is None:
            raise TypeError("step_widthにはintを指定してください")
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._last_step = single_step
        try:
            self.spin_box = IntSpinBox(
                view_model,
                self,
                single_step=single_step,
                wheel_requires_focus=value_wheel_requires_focus,
                select_all_on_mouse_focus=value_select_all_on_mouse_focus,
            )
            self.step_spin_box = IntStepSpinBox(
                self,
                value=single_step,
                step_mode=step_mode,
                step_increment=step_increment,
                wheel_requires_focus=step_wheel_requires_focus,
                select_all_on_mouse_focus=step_select_all_on_mouse_focus,
            )
            # 値欄を自動伸縮する場合もStep欄の固定幅を先に確保する
            self.step_spin_box.setSizePolicy(
                qt.QSizePolicy.Policy.Fixed, qt.QSizePolicy.Policy.Fixed
            )
            self.step_spin_box.setFixedWidth(checked_step_width)
            if value_width is not None:
                self.spin_box.setFixedWidth(value_width)
            layout = qt.QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.spin_box, 1 if value_width is None else 0)
            layout.addWidget(self.step_spin_box)
            if value_width is not None:
                layout.addStretch(1)
            self.setFocusProxy(self.spin_box)
            self.step_spin_box.valueChanged.connect(self._request_step)
            view_model.disposed.connect(self._stop_editing)
            connect_queued(view_model.destroyed, self._stop_editing)
        except Exception:
            self.setParent(None)
            self.deleteLater()
            raise

    @property
    def view_model(self) -> IntViewModel:
        """生存中の入力元を返す。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        return self._view_model

    def singleStep(self) -> int:
        """現在の値欄の刻み幅を整数で返す。"""
        return self.spin_box.singleStep()

    def setSingleStep(self, single_step: int) -> None:
        """正本を変更せず両欄のStepを揃え、実変更時だけ通知する。"""
        single_step = require_step(single_step)
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のIntViewModelは終了しています")
        self.spin_box.setSingleStep(single_step)
        blocker = qt.QtCore.QSignalBlocker(self.step_spin_box)
        try:
            self.step_spin_box.setValue(single_step)
        finally:
            del blocker
        if single_step != self._last_step:
            self._last_step = single_step
            self.settingsChanged.emit()

    @qt.Slot(int)
    def _request_step(self, value: int) -> None:
        """Step欄からの変更を受け、終了後の入力は破棄する。"""
        if self._view_model.is_disposed:
            self._stop_editing()
            return
        self.setSingleStep(value)

    @qt.Slot()
    def _stop_editing(self) -> None:
        """入力元の終了時に未確定Stepを捨て、両欄を停止する。"""
        if not qt.isValid(self):
            return
        blocker = qt.QtCore.QSignalBlocker(self.step_spin_box)
        try:
            self.step_spin_box.setValue(self.singleStep())
            self.step_spin_box.setEnabled(False)
            self.spin_box.setInputEnabled(False)
        finally:
            del blocker
