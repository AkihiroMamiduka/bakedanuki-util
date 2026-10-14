# coding: utf-8
"""Mayaのbyte・short・long属性を編集する整数MVVMサンプル。"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeAlias, cast

from maya import cmds

from .....maya.ui import (
    MayaIntPlug,
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    MayaWindowController,
    resolve_int_plug,
)
from .....ui import IntLabel, IntSpinBox, qt

_SamplePlugs: TypeAlias = tuple[
    MayaIntPlug, MayaIntPlug, MayaIntPlug, MayaIntPlug
]


class MayaIntWidget(qt.QWidget):
    """単一byte・shortと二つのlongの一括編集を表示する。"""

    def __init__(
        self,
        plugs: _SamplePlugs,
        parent: qt.QWidget | None = None,
    ) -> None:
        """既存Maya属性の現在値を読み、Window所有のBindingを作る。"""
        super().__init__(parent)
        self.byte_binding = MayaIntPlugBinding(plugs[0], parent=self)
        self.short_binding = MayaIntPlugBinding(plugs[1], parent=self)
        self.long_binding = MayaIntPlugsBinding(plugs[2:], parent=self)
        self.byte_spin_box = IntSpinBox(self.byte_binding, self)
        self.short_spin_box = IntSpinBox(self.short_binding, self)
        self.long_spin_box = IntSpinBox(self.long_binding, self)
        self.byte_label = IntLabel(self.byte_binding, self)
        self.short_label = IntLabel(self.short_binding, self)
        self.long_label = IntLabel(self.long_binding, self)
        self.group_state_label = qt.QLabel(self)
        self.align_button = qt.QPushButton("代表値に揃える", self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.align_button.clicked.connect(self._align_to_representative)
        self.refresh_button.clicked.connect(self._refresh)
        self.long_binding.state_changed.connect(self._update_group_state)

        # 編集欄と確定値ラベルを共有し、混在状態も別に表示する。
        form = qt.QFormLayout()
        for title, spin_box, label in (
            ("byte (0～255)", self.byte_spin_box, self.byte_label),
            ("short", self.short_spin_box, self.short_label),
            ("long (2 nodes)", self.long_spin_box, self.long_label),
        ):
            row = qt.QHBoxLayout()
            row.addWidget(spin_box)
            row.addWidget(label)
            form.addRow(title, row)
        buttons = qt.QHBoxLayout()
        buttons.addWidget(self.align_button)
        buttons.addWidget(self.refresh_button)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.group_state_label)
        layout.addLayout(buttons)
        self._update_group_state()

    @qt.Slot()
    def _align_to_representative(self) -> None:
        """二つのlong属性を代表の現在値へ揃える。"""
        self.long_binding.apply_representative_value()

    @qt.Slot()
    def _refresh(self) -> None:
        """Maya側の外部変更を各Bindingへ読み直す。"""
        self.byte_binding.refresh()
        self.short_binding.refresh()
        self.long_binding.refresh()

    @qt.Slot()
    def _update_group_state(self) -> None:
        """long属性群の混在状態と編集可能数を表示する。"""
        binding = self.long_binding
        mixed = "はい" if binding.is_mixed else "いいえ"
        self.group_state_label.setText(
            f"long値の混在: {mixed} / 編集可能: "
            f"{binding.writable_count}/{binding.target_count}"
        )


class MayaIntWindow(qt.QDialog):
    """Maya整数属性の編集Widgetを通常Windowへ配置する。"""

    def __init__(
        self,
        plugs: _SamplePlugs,
        node_names: tuple[str, str],
        parent: qt.QWidget | None = None,
    ) -> None:
        """既存二ノードのplugをWidgetへ渡す。"""
        super().__init__(parent)
        self.setObjectName("bdUtilMayaIntSampleWindow")
        self.setWindowTitle("bakedanuki-util Maya int")
        self.node_names = node_names
        self.widget = MayaIntWidget(plugs, self)
        description = qt.QLabel(
            f"代表: {node_names[0]} / もう一つ: {node_names[1]}", self
        )
        layout = qt.QVBoxLayout(self)
        layout.addWidget(description)
        layout.addWidget(self.widget)


_controller: MayaWindowController[MayaIntWindow] | None = None


def show(node_name: str, other_node_name: str) -> MayaIntWindow:
    """既存二ノードの整数属性を監視するサンプルWindowを開く。

    両ノードにlongValue、第一ノードにbyteValueとshortValueが必要。
    """
    global _controller
    plugs: _SamplePlugs = (
        resolve_int_plug(node_name, "byteValue"),
        resolve_int_plug(node_name, "shortValue"),
        resolve_int_plug(node_name, "longValue"),
        resolve_int_plug(other_node_name, "longValue"),
    )
    dispose()

    def create_window(parent: qt.QWidget | None = None) -> MayaIntWindow:
        """解決済みplugを使い、新しいWindowを生成する。"""
        return MayaIntWindow(plugs, (node_name, other_node_name), parent)

    controller = MayaWindowController(create_window)
    _controller = controller
    try:
        return controller.show()
    except Exception:
        dispose()
        raise


def create_demo_nodes() -> tuple[str, str]:
    """サンプル専用の二ノードと整数属性を現在のMayaシーンに作る。"""
    set_attr = cast(Callable[[str, int], None], cmds.setAttr)
    first = cmds.createNode("transform", name="bdIntSample")
    second = cmds.createNode("transform", name="bdIntSampleOther")
    cmds.addAttr(
        first, longName="byteValue", attributeType="byte", keyable=True
    )
    cmds.addAttr(
        first,
        longName="shortValue",
        attributeType="short",
        minValue=-20,
        maxValue=20,
        keyable=True,
    )
    for node, value in ((first, 3), (second, 4)):
        cmds.addAttr(
            node, longName="longValue", attributeType="long", keyable=True
        )
        set_attr(node + ".longValue", value)
    set_attr(first + ".byteValue", 128)
    set_attr(first + ".shortValue", 5)
    return first, second


def show_demo() -> MayaIntWindow:
    """現在のMayaシーンに検証ノードを作り、サンプルを開く。"""
    return show(*create_demo_nodes())


def dispose() -> None:
    """Windowとcallbackを終了する。Maya nodeや属性は残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
