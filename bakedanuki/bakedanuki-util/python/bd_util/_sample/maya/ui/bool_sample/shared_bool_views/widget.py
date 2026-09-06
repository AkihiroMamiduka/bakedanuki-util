# coding: utf-8
from __future__ import annotations

from ......ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
    qt,
)


class SharedBoolViewsWidget(qt.QWidget):
    """外部で所有する1つのBoolViewModelを表示・操作するsample Widget。"""

    print_value_requested = qt.Signal()

    def __init__(
        self,
        view_model: BoolViewModel,
        *,
        data_description: str = "Shared Data Store",
        maya_description: str = "None",
        parent: qt.QWidget | None = None,
    ) -> None:
        """共有ViewModelと対象の説明を受け取り、5種類のViewを配置する。"""
        super().__init__(parent)

        # ViewModelのparentを変更せず、外部Managerの共有instanceを参照する。
        self.view_model = view_model

        # 4種類の入力Viewを同じViewModelのCommandへ接続する。
        self.check_box = BoolCheckBox(view_model, "Visible", self)
        self.combo_box = BoolComboBox(
            view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.push_button = BoolPushButton(
            view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.radio_button_group = BoolRadioButtonGroup(
            view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )

        # 読み取り専用Viewも同じ確定値を表示する。
        self.status_label = BoolStatusLabel(
            view_model,
            false_text="Status: Off",
            true_text="Status: On",
            parent=self,
        )

        # 正本の出力はdataを所有するManagerへ要求する。
        self.print_value_button = qt.QPushButton("Print Data Value", self)
        self.print_value_button.clicked.connect(self._request_print_value)

        # 各bool Viewを役割名と対にして縦に並べる。
        form_layout = qt.QFormLayout()
        form_layout.addRow("BoolCheckBox", self.check_box)
        form_layout.addRow("BoolComboBox", self.combo_box)
        form_layout.addRow("BoolPushButton", self.push_button)
        form_layout.addRow("BoolRadioButtonGroup", self.radio_button_group)
        form_layout.addRow("BoolStatusLabel", self.status_label)

        # 対象情報と共有中であることを両Windowへ同じように表示する。
        description = qt.QLabel(
            "Window A / Bは同じViewModelを共有しています。\n"
            "このWindowを閉じても、共有データと同期は継続します。"
        )
        description.setWordWrap(True)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(qt.QLabel(f"Data: {data_description}"))
        layout.addWidget(qt.QLabel(f"Maya View: {maya_description}"))
        layout.addLayout(form_layout)
        layout.addWidget(description)
        layout.addWidget(self.print_value_button)

    @qt.Slot(bool)
    def _request_print_value(self, _checked: bool = False) -> None:
        """確認ボタンから正本値の出力を要求する。"""
        self.print_value_requested.emit()
