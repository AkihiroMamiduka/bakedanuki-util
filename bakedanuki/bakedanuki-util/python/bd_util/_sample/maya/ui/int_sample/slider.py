# coding: utf-8
"""整数Sliderの共有、広い範囲、Maya同期と連続Undoを確認する。"""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from maya import cmds

from .....maya.ui import (
    MayaFloatPlugBinding,
    MayaIntBinding,
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    MayaWindowController,
    resolve_float_plug,
    resolve_int_plug,
)
from .....ui import (
    FloatSlider,
    FloatSpinBox,
    IntBinding,
    IntLabel,
    IntSlider,
    IntSpinBox,
    IntValueStore,
    qt,
)
from .data import IntSampleData
from .maya_plug import create_demo_nodes


class IntSliderSampleRow(qt.QWidget):
    """同じ整数BindingをSlider・値欄・確定値ラベルで共有する行。"""

    def __init__(
        self,
        binding: IntBinding[IntValueStore],
        parent: qt.QWidget,
        *,
        minimum: int,
        maximum: int,
    ) -> None:
        """サンプル用の操作範囲と、精度を維持する値欄を並べる。"""
        super().__init__(parent)
        self.slider = IntSlider(
            binding, self, minimum=minimum, maximum=maximum
        )
        self.slider.setMinimumWidth(200)
        self.spin_box = IntSpinBox(
            binding, self, select_all_on_mouse_focus=True
        )
        self.spin_box.setFixedWidth(140)
        self.value_label = IntLabel(binding, self)
        self.value_label.setMinimumWidth(100)
        layout = qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider, 1)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.value_label)


class IntSliderWidget(qt.QWidget):
    """Python共有Viewと、任意のMaya連携Viewを表示する。"""

    def __init__(
        self,
        node_names: tuple[str, str] | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """Pythonのみ、またはMayaの三つの同期経路を構築する。"""
        super().__init__(parent)
        self.data = IntSampleData()
        self.python_binding = IntBinding.from_attribute(
            self.data, "signed_value", parent=self
        )
        self.python_row = IntSliderSampleRow(
            self.python_binding, self, minimum=0, maximum=100
        )
        self.linked_row = IntSliderSampleRow(
            self.python_binding, self, minimum=-10, maximum=10
        )
        self.wide_row = IntSliderSampleRow(
            self.python_binding, self, minimum=-(2**31), maximum=2**31 - 1
        )
        form = qt.QFormLayout()
        form.addRow("Python 0～100", self.python_row)
        form.addRow("共有 -10～10", self.linked_row)
        form.addRow("共有 int32 全域", self.wide_row)
        self.maya_binding: MayaIntPlugsBinding | None = None
        self.maya_row: IntSliderSampleRow | None = None
        self.sync_row: IntSliderSampleRow | None = None
        if node_names is not None:
            first = node_names[0]
            byte_binding = MayaIntPlugBinding(
                resolve_int_plug(first, "byteValue"),
                parent=self,
                edit_connected=True,
            )
            short_binding = MayaIntPlugBinding(
                resolve_int_plug(first, "shortValue"),
                parent=self,
                edit_connected=True,
            )
            self.maya_binding = MayaIntPlugsBinding(
                tuple(resolve_int_plug(n, "longValue") for n in node_names),
                parent=self,
                edit_connected=True,
            )
            self.maya_row = IntSliderSampleRow(
                self.maya_binding, self, minimum=-100, maximum=100
            )
            self.sync_data = IntSampleData()
            self.sync_binding = MayaIntBinding.from_attribute(
                self.sync_data,
                "signed_value",
                parent=self,
                maya_plug=resolve_int_plug(first, "pythonValue"),
            )
            self.sync_row = IntSliderSampleRow(
                self.sync_binding, self, minimum=0, maximum=100
            )
            form.addRow(
                "Maya byte 0～255",
                IntSliderSampleRow(byte_binding, self, minimum=0, maximum=255),
            )
            form.addRow(
                "Maya short -20～20",
                IntSliderSampleRow(
                    short_binding, self, minimum=-20, maximum=20
                ),
            )
            form.addRow("Maya long（二ノード）", self.maya_row)
            form.addRow("Python → Maya long", self.sync_row)
            self.float_binding = MayaFloatPlugBinding(
                resolve_float_plug(first, "translateX"), parent=self
            )
            self.float_slider = FloatSlider(
                self.float_binding, self, minimum=0, maximum=100
            )
            self.float_spin_box = FloatSpinBox(self.float_binding, self)
            float_row = qt.QHBoxLayout()
            float_row.addWidget(self.float_slider, 1)
            float_row.addWidget(self.float_spin_box)
            form.addRow("Maya float（Undo比較）", float_row)
        description = qt.QLabel(
            "上の3行は同じPython値を共有します。範囲外の値も数値欄とラベルに保持します。\n"
            "Maya行のドラッグはUndo／Redo各1回で戻せます。時刻移動・Escは最後の値で操作を終了します。",
            self,
        )
        description.setWordWrap(True)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(description)


class IntSliderWindow(qt.QDialog):
    """整数Sliderの各同期経路を試す通常Window。"""

    def __init__(
        self,
        node_names: tuple[str, str] | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """既存Maya属性を使う場合は二ノード名を渡す。"""
        super().__init__(parent)
        self.setObjectName("bdUtilIntSliderSampleWindow")
        self.setWindowTitle("bakedanuki-util int Slider")
        self.node_names = node_names
        try:
            self.widget = IntSliderWidget(node_names, self)
        except Exception:
            # 途中まで構築したBindingも、Qtの遅延破棄より先に終了する
            find_children = cast(
                Callable[[type[qt.QObject]], list[qt.QObject]],
                getattr(self, "findChildren"),
            )
            for child in find_children(qt.QObject):
                if isinstance(child, (IntBinding, MayaFloatPlugBinding)):
                    child.dispose()
            self.deleteLater()
            raise
        layout = qt.QVBoxLayout(self)
        if node_names is not None:
            label = qt.QLabel(
                f"代表: {node_names[0]} / 後続: {node_names[1]}", self
            )
            label.setWordWrap(True)
            layout.addWidget(label)
        layout.addWidget(self.widget)
        self.resize(820, self.sizeHint().height())


_controller: MayaWindowController[IntSliderWindow] | None = None


def _show(node_names: tuple[str, str] | None) -> IntSliderWindow:
    """既存Windowを終了し、指定した正本のサンプルを一つだけ開く。"""
    global _controller
    dispose()

    def create_window(parent: qt.QWidget | None = None) -> IntSliderWindow:
        """今回の同期先を使ってWindowを生成する。"""
        return IntSliderWindow(node_names, parent)

    _controller = MayaWindowController(create_window)
    try:
        return _controller.show()
    except Exception:
        dispose()
        raise


def show() -> IntSliderWindow:
    """sceneを変更せず、Python正本の共有Sliderを開く。"""
    return _show(None)


def show_maya(node_name: str, other_node_name: str) -> IntSliderWindow:
    """既存二ノードの整数属性とPython同期用`pythonValue`を表示する。"""
    return _show((node_name, other_node_name))


def show_demo() -> IntSliderWindow:
    """現在のsceneへ検証用ノードと属性を追加してサンプルを開く。"""
    first, second = create_demo_nodes()
    cmds.addAttr(
        first, longName="pythonValue", attributeType="long", keyable=True
    )
    return show_maya(first, second)


def dispose() -> None:
    """Window・Binding・callbackを終了する。検証用Mayaノードは残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
