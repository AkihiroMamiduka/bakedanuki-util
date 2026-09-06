# coding: utf-8
from __future__ import annotations

from ......maya.ui import MayaBoolBinding
from ......ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    qt,
)
from ..bool_plug import resolve_optional_bool_plug


class BoolViewsWidget(qt.QWidget):
    """Python objectのbool attributeを複数Viewで編集するFeature Widget。"""

    def __init__(
        self,
        data: object,
        data_attribute_name: str,
        *,
        maya_node_name: str | None = None,
        maya_attribute_name: str | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """値の正本と任意のMaya同期先を受け取って初期化する。"""
        plug = resolve_optional_bool_plug(
            maya_node_name,
            maya_attribute_name,
        )
        super().__init__(parent)

        self.binding = MayaBoolBinding.from_attribute(
            data, data_attribute_name, maya_plug=plug, parent=self
        )
        self.data = self.binding.store.instance
        self.store = self.binding.store
        self.view_model = self.binding.view_model
        self.maya_view = self.binding.maya_view

        # 入力可能なQt Viewへ同じBindingを渡す。
        self.check_box = BoolCheckBox(
            self.binding,
            "Visible",
            self,
        )
        self.combo_box = BoolComboBox(
            self.binding,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.push_button = BoolPushButton(
            self.binding,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.radio_button_group = BoolRadioButtonGroup(
            self.binding,
            false_text="Off",
            true_text="On",
            parent=self,
        )

        # 読み取り専用Viewも同じ確定値を表示する。
        self.status_label = BoolStatusLabel(
            self.binding,
            false_text="Status: Off",
            true_text="Status: On",
            parent=self,
        )

        # 現在のData Storeと任意のMaya Viewを画面上へ明示する。
        data_label = qt.QLabel(
            f"Data: {type(data).__name__}.{self.store.attribute_name}"
        )
        maya_view_name = (
            "None"
            if plug is None
            else f"{plug.node.cmd_access_name}.{maya_attribute_name}"
        )
        maya_label = qt.QLabel(f"Maya View: {maya_view_name}")

        # Maya Viewの有無に合わせて利用できる同期経路を説明する。
        description_text = "Data Store、すべてのQt View、Pythonを同期します。"
        if self.maya_view is not None:
            description_text = (
                "Data Store、すべてのQt View、Python、Attribute Editor、"
                "undo / redoを同期します。"
            )
        description = qt.QLabel(description_text)

        # 正本の現在値をScript Editorへ出力する確認操作を用意する。
        self.print_value_button = qt.QPushButton(
            "Print Data Value",
            self,
        )
        self.print_value_button.clicked.connect(self._print_data_value)

        # 各bool Viewを役割名と対にして縦に並べる。
        form_layout = qt.QFormLayout()
        form_layout.addRow("BoolCheckBox", self.check_box)
        form_layout.addRow("BoolComboBox", self.combo_box)
        form_layout.addRow("BoolPushButton", self.push_button)
        form_layout.addRow("BoolRadioButtonGroup", self.radio_button_group)
        form_layout.addRow("BoolStatusLabel", self.status_label)

        # 対象情報、bool Views、説明、確認操作を1つのWidgetへまとめる。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(data_label)
        layout.addWidget(maya_label)
        layout.addLayout(form_layout)
        layout.addWidget(description)
        layout.addWidget(self.print_value_button)

    @property
    def value(self) -> bool:
        """ViewModelが現在公開している確定値を返す。"""
        return self.binding.value

    def set_value(self, value: bool) -> bool:
        """UI入力と同じCommandからbool値を変更する。"""
        # Python入力も各Qt Viewと同じ値変更Commandへ集約する。
        return self.binding.set_value(value)

    def refresh_from_data(self) -> bool:
        """Python objectのattributeを正本としてViewへ再反映する。"""
        # 外部で直接変更されたPython attributeをStoreから読み直す。
        return self.binding.refresh()

    @qt.Slot(bool)
    def _print_data_value(self, _checked: bool = False) -> None:
        """現在の内部データ値をMaya Script Editorへ出力する。"""
        # 表示中のsnapshotではなくStoreから読み直した正本値を出力する。
        print(
            f"{type(self.data).__name__}.{self.store.attribute_name} = "
            f"{self.store.read()}"
        )
