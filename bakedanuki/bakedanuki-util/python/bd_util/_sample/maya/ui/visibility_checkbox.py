# coding: utf-8
from dataclasses import dataclass

from .... import Nodes
from ....maya.ui import MayaBoolPlugView, MayaWindowController
from ....ui import (
    BoolCheckBox,
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


class VisibilityCheckBoxWindow(qt.QDialog):
    """transform.visibilityとの同期を確認するsample Window。"""

    def __init__(
        self,
        node_name: str,
        parent: qt.QWidget | None = None,
    ) -> None:
        """同期対象のtransform名とMaya親Windowを受け取る。"""
        super().__init__(parent)
        self.setObjectName("bdUtilVisibilityCheckBoxSampleWindow")
        self.setWindowTitle("bakedanuki-util visibility binding")
        self.resize(420, 180)

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

        # ViewはViewModelだけを参照し、Maya固有処理を持たない。
        node_label = qt.QLabel(f"Target: {self.node_name}")
        self.visibility_checkbox = BoolCheckBox(
            self.view_model,
            "Visibility",
            self,
        )
        description = qt.QLabel(
            "Data Store、Checkbox、Python、Attribute Editor、"
            "undo / redoを同期します。"
        )
        self.print_value_button = qt.QPushButton(
            "Print Data Value",
            self,
        )
        self.print_value_button.clicked.connect(self._print_data_value)
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = qt.QVBoxLayout(self)
        layout.addWidget(node_label)
        layout.addWidget(self.visibility_checkbox)
        layout.addWidget(description)
        layout.addWidget(self.print_value_button)
        layout.addWidget(close_button)

    def set_visibility(self, value: bool) -> bool:
        """sample Windowと同じCommandからvisibilityを変更する。"""
        return self.view_model.set_value_command.execute(value)

    @qt.Slot(bool)
    def _print_data_value(self, _checked: bool = False) -> None:
        """現在の内部データ値をMaya Script Editorへ出力する。"""
        print(
            "VisibilityData.visible_by_default = "
            f"{self.data.visible_by_default}"
        )


_target_node_name: str | None = None


def _create_window(
    parent: qt.QWidget | None,
) -> VisibilityCheckBoxWindow:
    """現在指定されているtransform用のsample Windowを生成する。"""
    if _target_node_name is None:
        raise RuntimeError("同期対象のtransformが指定されていません")
    return VisibilityCheckBoxWindow(_target_node_name, parent)


_controller = MayaWindowController(_create_window)


def show(node: str) -> VisibilityCheckBoxWindow:
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


def set_visibility(value: bool) -> bool:
    """表示中sampleのCommandをPythonから実行する。"""
    window = _controller.window
    if window is None:
        raise RuntimeError("visibility checkbox sampleは表示されていません")
    return window.set_visibility(value)


def dispose() -> None:
    """sample WindowとMaya callbackを完全に破棄する。"""
    _controller.dispose()
