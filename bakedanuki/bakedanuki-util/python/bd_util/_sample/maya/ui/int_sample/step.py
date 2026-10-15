# coding: utf-8
"""整数Stepの加算・10倍方式と設定保存を確認するサンプル。"""

from __future__ import annotations

from .....maya.ui import (
    MayaWindowController,
    MayaUiStateTracker,
    create_ui_state_manager,
)
from .....ui import (
    IntBinding,
    IntLabel,
    IntStepProfile,
    IntValueStepSpinBox,
    qt,
)
from .data import IntSampleData


class IntStepWidget(qt.QWidget):
    """同じ整数正本を異なるStep操作で編集する。"""

    def __init__(
        self, profile: IntStepProfile, parent: qt.QWidget | None = None
    ) -> None:
        """Viewごとに独立したStepをProfileへ接続する。"""
        super().__init__(parent)
        self.profile = profile
        self.binding = IntBinding.from_attribute(
            IntSampleData(), "signed_value", parent=self
        )
        self._changing_steps = False
        self.multiplicative_editor = IntValueStepSpinBox(
            self.binding,
            self,
            step_mode="multiplicative",
            value_select_all_on_mouse_focus=True,
            step_select_all_on_mouse_focus=True,
        )
        self.additive_editor = IntValueStepSpinBox(
            self.binding,
            self,
            step_mode="additive",
            value_select_all_on_mouse_focus=True,
            step_select_all_on_mouse_focus=True,
        )
        self.value_label = IntLabel(self.binding, self)
        self.reset_button = qt.QPushButton("Stepを初期値1へ戻す", self)
        self.reset_button.clicked.connect(self._reset_steps)
        self.multiplicative_editor.settingsChanged.connect(
            self._save_multiplicative
        )
        self.additive_editor.settingsChanged.connect(self._save_additive)
        profile.changed.connect(self._restore_steps)
        form = qt.QFormLayout()
        form.addRow("10倍方式 [値][Step]", self.multiplicative_editor)
        form.addRow("加算方式 [値][Step]", self.additive_editor)
        form.addRow("共有する確定値", self.value_label)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(
            qt.QLabel(
                "Stepは各欄で独立しています。15から下へは、10倍方式で1、加算方式で14になります。",
                self,
            )
        )
        layout.addWidget(self.reset_button)

    @qt.Slot()
    def _save_multiplicative(self) -> None:
        """10倍方式のStepだけを保存する。"""
        self._save_step("multiplicative", self.multiplicative_editor)

    @qt.Slot()
    def _save_additive(self) -> None:
        """加算方式のStepだけを保存する。"""
        self._save_step("additive", self.additive_editor)

    def _save_step(self, key: str, editor: IntValueStepSpinBox) -> None:
        """既定値は削除し、正本には触れず設定を更新する。"""
        if self._changing_steps:
            return
        if editor.singleStep() == 1:
            self.profile.remove(key)
        else:
            self.profile.set_single_step(key, editor.singleStep())

    @qt.Slot()
    def _restore_steps(self) -> None:
        """復元・リセットを各Viewへ通知の循環なしで反映する。"""
        self._changing_steps = True
        try:
            for key, editor in (
                ("multiplicative", self.multiplicative_editor),
                ("additive", self.additive_editor),
            ):
                editor.setSingleStep(self.profile.single_step(key) or 1)
        finally:
            self._changing_steps = False

    @qt.Slot()
    def _reset_steps(self) -> None:
        """保存済みの両Stepを削除する。"""
        self.profile.clear()


class IntStepWindow(qt.QDialog):
    """整数Stepの設定だけを再表示後へ保存するWindow。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """独立した保存先と、同じ正本を共有する二つの編集欄を作る。"""
        super().__init__(parent)
        self.setObjectName("bdUtilIntStepSampleWindow")
        self.setWindowTitle("bakedanuki-util int Step")
        self.profile = IntStepProfile(self)
        self.settings = create_ui_state_manager(
            "int_sample/editor_settings/step"
        )
        self.settings.register_int_step_profile("steps", self.profile)
        self.widget = IntStepWidget(self.profile, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)
        self.settings_tracker = MayaUiStateTracker.for_window(
            self.settings, self
        )


_controller = MayaWindowController(IntStepWindow)


def show() -> IntStepWindow:
    """既存sceneを変更せずStep確認用Windowを表示する。"""
    return _controller.show()


def dispose() -> None:
    """WindowとBindingを終了する。保存済みStepは保持する。"""
    _controller.dispose()
