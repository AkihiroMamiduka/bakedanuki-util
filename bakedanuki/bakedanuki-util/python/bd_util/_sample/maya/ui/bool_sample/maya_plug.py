# coding: utf-8
"""既存Maya bool plugを正本として編集するサンプル。"""

from __future__ import annotations

from .....maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from .....maya.ui import (
    MayaBoolPlugBinding,
    MayaWindowController,
    resolve_bool_plug,
)
from .....ui import BoolCheckBox, BoolStatusLabel, qt


class MayaPlugBoolWidget(qt.QWidget):
    """1つのMaya plugを入力用Viewと読み取り専用Viewへ接続する。"""

    def __init__(
        self, plug: BoolPlugOperator, parent: qt.QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.binding = MayaBoolPlugBinding(plug, parent=self)
        self.check_box = BoolCheckBox(self.binding, "Value", self)
        self.status_label = BoolStatusLabel(self.binding, parent=self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.check_box)
        layout.addWidget(self.status_label)


class MayaPlugBoolWindow(qt.QDialog):
    """既存plugの編集WidgetをMayaのWindowへ配置する。"""

    def __init__(
        self, plug: BoolPlugOperator, parent: qt.QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.setObjectName("bdUtilMayaPlugBoolSampleWindow")
        self.setWindowTitle("bakedanuki-util Maya bool")
        self.widget = MayaPlugBoolWidget(plug, self)
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller: MayaWindowController[MayaPlugBoolWindow] | None = None


def show(
    node_name: str, attribute_name: str = "visibility"
) -> MayaPlugBoolWindow:
    """既存plugを解決し、前のサンプルWindowを置き換えて表示する。"""
    global _controller
    plug = resolve_bool_plug(node_name, attribute_name)
    dispose()

    def create_window(parent: qt.QWidget | None = None) -> MayaPlugBoolWindow:
        return MayaPlugBoolWindow(plug, parent)

    controller = MayaWindowController(create_window)
    _controller = controller
    try:
        return controller.show()
    except Exception:
        dispose()
        raise


def dispose() -> None:
    """WindowとBindingを終了する。シーンのnodeや属性は残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
