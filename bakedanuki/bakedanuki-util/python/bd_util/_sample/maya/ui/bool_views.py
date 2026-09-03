# coding: utf-8
from dataclasses import dataclass

from .... import Nodes
from ....maya.ui import MayaBoolPlugView, MayaWindowController
from ....ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolViewModel,
    PythonBoolAttributeStore,
    qt,
)


@dataclass
class VisibilityData:
    """sampleで値の正本として扱うPython data。"""

    visible_by_default: bool = True


def _require_node_name(value: object) -> str:
    """runtime値を空でないtransform名として検証する。"""
    if not isinstance(value, str):
        raise TypeError(
            "nodeにはtransform名を指定してください: " f"{type(value).__name__}"
        )
    if not value:
        raise ValueError("nodeには空でないtransform名を指定してください")
    return value


class BoolViewsWindow(qt.QDialog):
    """複数のbool Viewとtransform.visibilityの同期を確認するsample Window。"""

    def __init__(
        self,
        node_name: str,
        parent: qt.QWidget | None = None,
    ) -> None:
        """同期対象のtransform名とMaya親Windowを受け取る。"""
        super().__init__(parent)
        self.setObjectName("bdUtilBoolViewsSampleWindow")
        self.setWindowTitle("bakedanuki-util bool views")
        self.resize(460, 300)

        # 既存transformを型付きNodeOperatorとして取得する。
        nodes = Nodes()
        self.node = nodes.existing.transform(node_name)
        self.node_name = self.node.cmd_access_name

        # dataclass fieldを値の正本としてViewModelへ明示接続する。
        self.data = VisibilityData()
        self.store = PythonBoolAttributeStore(
            self.data,
            "visible_by_default",
        )
        self.view_model = BoolViewModel(parent=self)
        self.view_model.attach_store(self.store)

        # Maya plugは正本を表示し、Attribute Editorからの入力も受けるView。
        self.maya_view = MayaBoolPlugView(
            self.view_model,
            self.node.visibility,
            self,
        )

        # すべてのQt Viewは同じViewModelだけを参照する。
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
        self.status_label = BoolStatusLabel(
            self.view_model,
            false_text="Status: Off",
            true_text="Status: On",
            parent=self,
        )

        node_label = qt.QLabel(f"Target: {self.node_name}")
        description = qt.QLabel(
            "Data Store、すべてのView、Python、Attribute Editor、"
            "undo / redoを同期します。"
        )
        self.print_value_button = qt.QPushButton(
            "Print Data Value",
            self,
        )
        self.print_value_button.clicked.connect(self._print_data_value)
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(self.close)

        form_layout = qt.QFormLayout()
        form_layout.addRow("BoolCheckBox", self.check_box)
        form_layout.addRow("BoolComboBox", self.combo_box)
        form_layout.addRow("BoolPushButton", self.push_button)
        form_layout.addRow("BoolRadioButtonGroup", self.radio_button_group)
        form_layout.addRow("BoolStatusLabel", self.status_label)

        layout = qt.QVBoxLayout(self)
        layout.addWidget(node_label)
        layout.addLayout(form_layout)
        layout.addWidget(description)
        layout.addWidget(self.print_value_button)
        layout.addWidget(close_button)

    def set_value(self, value: bool) -> bool:
        """sample Windowと同じCommandからbool値を変更する。"""
        return self.view_model.set_value_command.execute(value)

    @qt.Slot(bool)
    def _print_data_value(self, _checked: bool = False) -> None:
        """現在の内部データ値をMaya Script Editorへ出力する。"""
        print(
            "VisibilityData.visible_by_default = "
            f"{self.data.visible_by_default}"
        )


_target_node_name: str | None = None


def _create_window(parent: qt.QWidget | None) -> BoolViewsWindow:
    """現在指定されているtransform用のsample Windowを生成する。"""
    if _target_node_name is None:
        raise RuntimeError("同期対象のtransformが指定されていません")
    return BoolViewsWindow(_target_node_name, parent)


_controller = MayaWindowController(_create_window)


def show(node: str) -> BoolViewsWindow:
    """指定transformと同期するsample Windowを表示する。"""
    node = _require_node_name(node)

    # short name表記ではなくMObject identityで表示中targetと比較する。
    requested_node = Nodes().existing.transform(node)
    global _target_node_name
    current_window = _controller.window
    if current_window is not None:
        same_target = (
            current_window.maya_view.is_available
            and current_window.node.m_obj == requested_node.m_obj
        )
        if not same_target:
            _controller.dispose()
    _target_node_name = requested_node.cmd_access_name
    return _controller.show()


def set_value(value: bool) -> bool:
    """表示中sampleのCommandをPythonから実行する。"""
    window = _controller.window
    if window is None:
        raise RuntimeError("bool views sampleは表示されていません")
    return window.set_value(value)


def dispose() -> None:
    """sample WindowとMaya callbackを完全に破棄する。"""
    _controller.dispose()
