# coding: utf-8
from __future__ import annotations

from ......maya.node.operator.node._core import NodeOperator
from ......maya.ui import MayaBoolPlugView
from ......ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
    PythonBoolAttributeStore,
    qt,
)
from ..bool_plug import resolve_bool_plug, validate_maya_view_names


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
        # Maya Viewの指定はWidget生成前にnode名とattribute名の組で検証する。
        maya_view_names = validate_maya_view_names(
            maya_node_name,
            maya_attribute_name,
        )
        super().__init__(parent)

        # Python object内の指定attributeを値の正本としてViewModelへ接続する。
        self.data = data
        self.store = PythonBoolAttributeStore(data, data_attribute_name)
        self.view_model = BoolViewModel(parent=self)
        self.view_model.attach_store(self.store)

        # Maya指定がない場合も同じWidget APIになるよう空の同期状態を用意する。
        self.maya_node: NodeOperator | None = None
        self.maya_node_name: str | None = None
        self.maya_attribute_name: str | None = None
        self.maya_view: MayaBoolPlugView | None = None
        self._maya_node_argument: str | None = None

        # Maya指定がある場合だけplugを入力・表示用Viewとして接続する。
        if maya_view_names is not None:
            requested_node_name, requested_attribute_name = maya_view_names
            self.maya_node, plug = resolve_bool_plug(
                requested_node_name,
                requested_attribute_name,
            )
            self.maya_node_name = self.maya_node.cmd_access_name
            self.maya_attribute_name = requested_attribute_name
            self._maya_node_argument = requested_node_name
            self.maya_view = MayaBoolPlugView(
                self.view_model,
                plug,
                self,
            )

        # 入力可能なQt Viewをすべて同じViewModelへ接続する。
        self.check_box = BoolCheckBox(
            self.view_model,
            "Visible",
            self,
        )
        self.combo_box = BoolComboBox(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.push_button = BoolPushButton(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )
        self.radio_button_group = BoolRadioButtonGroup(
            self.view_model,
            false_text="Off",
            true_text="On",
            parent=self,
        )

        # 読み取り専用Viewも同じ確定値を表示する。
        self.status_label = BoolStatusLabel(
            self.view_model,
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
            if self.maya_node_name is None
            else f"{self.maya_node_name}.{self.maya_attribute_name}"
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
        return self.view_model.value.value

    def set_value(self, value: bool) -> bool:
        """UI入力と同じCommandからbool値を変更する。"""
        # Python入力も各Qt Viewと同じ値変更Commandへ集約する。
        return self.view_model.set_value_command.execute(value)

    def refresh_from_data(self) -> bool:
        """Python objectのattributeを正本としてViewへ再反映する。"""
        # 外部で直接変更されたPython attributeをStoreから読み直す。
        return self.view_model.refresh_from_store(self.store)

    def matches_configuration(
        self,
        data: object,
        data_attribute_name: str,
        maya_node_name: str | None,
        maya_attribute_name: str | None,
    ) -> bool:
        """指定内容が現在のbinding構成と同じか返す。"""
        # 比較対象のMaya指定も生成時と同じ規則で検証する。
        maya_view_names = validate_maya_view_names(
            maya_node_name,
            maya_attribute_name,
        )

        # Python正本が異なるか利用不能なら別構成として扱う。
        if (
            self.data is not data
            or self.store.attribute_name != data_attribute_name
            or not self.store.is_available
        ):
            return False

        # Maya指定がない構成ではMaya Viewを持たないことを確認する。
        if maya_view_names is None:
            return self.maya_view is None

        # Maya Viewが破棄済みなら同じ引数でもWindowを作り直す。
        if self.maya_view is None or not self.maya_view.is_available:
            return False

        # Python正本とMaya指定の両方が一致した場合だけ再利用する。
        return (
            self._maya_node_argument == maya_view_names[0]
            and self.maya_attribute_name == maya_view_names[1]
        )

    @qt.Slot(bool)
    def _print_data_value(self, _checked: bool = False) -> None:
        """現在の内部データ値をMaya Script Editorへ出力する。"""
        # 表示中のsnapshotではなくStoreから読み直した正本値を出力する。
        print(
            f"{type(self.data).__name__}.{self.store.attribute_name} = "
            f"{self.store.read()}"
        )
