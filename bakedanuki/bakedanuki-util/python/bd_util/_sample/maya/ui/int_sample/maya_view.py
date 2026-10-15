# coding: utf-8
"""Python整数を正本としてQtとMayaのbyte・short・longへ同期するサンプル。"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import cast

from maya import cmds

from .....maya.ui import (
    MayaIntBinding,
    MayaIntPlug,
    MayaWindowController,
    resolve_int_plug,
)
from .....ui import IntLabel, IntSpinBox, qt


@dataclass
class MayaIntSampleData:
    """Maya同期先とは独立したPython側の整数データ。"""

    byte_value: int = 128
    short_value: int = 5
    long_value: int = 3


class PythonMayaIntWidget(qt.QWidget):
    """Python正本と三種類のMaya整数属性を共有Viewで編集する。"""

    def __init__(
        self,
        data: MayaIntSampleData,
        plugs: tuple[MayaIntPlug, MayaIntPlug, MayaIntPlug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """Python初期値をMayaへ反映し、直接変更と再同期の操作を配置する。"""
        super().__init__(parent)
        self.data = data
        self.byte_binding = MayaIntBinding.from_attribute(
            data, "byte_value", maya_plug=plugs[0], parent=self
        )
        self.short_binding = MayaIntBinding.from_attribute(
            data, "short_value", maya_plug=plugs[1], parent=self
        )
        self.long_binding = MayaIntBinding.from_attribute(
            data, "long_value", maya_plug=plugs[2], parent=self
        )
        self.bindings = (
            self.byte_binding,
            self.short_binding,
            self.long_binding,
        )
        self.byte_spin_box = IntSpinBox(
            self.byte_binding, self, select_all_on_mouse_focus=True
        )
        self.short_spin_box = IntSpinBox(
            self.short_binding, self, select_all_on_mouse_focus=True
        )
        self.long_spin_box = IntSpinBox(
            self.long_binding, self, select_all_on_mouse_focus=True
        )
        self.linked_long_spin_box = IntSpinBox(
            self.long_binding,
            self,
            single_step=10,
            select_all_on_mouse_focus=True,
        )
        self.byte_label = IntLabel(self.byte_binding, self)
        self.short_label = IntLabel(self.short_binding, self)
        self.long_label = IntLabel(self.long_binding, self)
        form = qt.QFormLayout()
        for title, spin_box, label in (
            ("byte → Maya 0～255", self.byte_spin_box, self.byte_label),
            (
                "short → Maya 型範囲・hard limit",
                self.short_spin_box,
                self.short_label,
            ),
            ("long → Maya int32", self.long_spin_box, self.long_label),
        ):
            row = qt.QHBoxLayout()
            row.addWidget(spin_box)
            row.addWidget(label)
            form.addRow(title, row)
        form.addRow("long 共有View（step 10）", self.linked_long_spin_box)
        self.data_label = qt.QLabel(self)
        self.result_label = qt.QLabel(self)
        self.set_data_button = qt.QPushButton("Python値を直接変更", self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.retry_button = qt.QPushButton("Maya同期を再試行", self)
        self.set_data_button.clicked.connect(self._set_data)
        self.refresh_button.clicked.connect(self._refresh)
        self.retry_button.clicked.connect(self._retry_sync)
        for binding in self.bindings:
            binding.changed.connect(self._update_data_label)
        buttons = qt.QHBoxLayout()
        buttons.addWidget(self.set_data_button)
        buttons.addWidget(self.refresh_button)
        buttons.addWidget(self.retry_button)
        layout = qt.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.data_label)
        layout.addLayout(buttons)
        layout.addWidget(self.result_label)
        self._update_data_label()
        self._show_sync_result()

    @qt.Slot()
    def _set_data(self) -> None:
        """Python正本だけを変更し、明示Refreshとの違いを確認する。"""
        self.data.byte_value = 200
        self.data.short_value = -10
        self.data.long_value = 100
        self._update_data_label()

    @qt.Slot()
    def _refresh(self) -> None:
        """Python正本を読み直してQtとMayaへ反映する。"""
        for binding in self.bindings:
            binding.refresh()
        self._update_data_label()
        self._show_sync_result()

    @qt.Slot()
    def _retry_sync(self) -> None:
        """Mayaへ確定値を再適用し、失敗理由を表示する。"""
        for binding in self.bindings:
            if binding.maya_view is not None:
                try:
                    binding.maya_view.sync_from_view_model()
                except Exception:
                    pass
        self._show_sync_result()

    def _show_sync_result(self) -> None:
        """ボタン操作時点の同期状態と保留理由を表示する。"""
        results: list[str] = []
        for binding in self.bindings:
            view = binding.maya_view
            state = (
                "OK"
                if view is not None and view.is_synchronized
                else "Pending"
            )
            error = view.last_sync_error if view is not None else None
            results.append(
                f"{binding.store.attribute_name}: {state}"
                + (f" ({error})" if error else "")
            )
        self.result_label.setText("最終同期確認:\n" + "\n".join(results))
        self.result_label.setWordWrap(True)

    @qt.Slot()
    def _update_data_label(self) -> None:
        """Mayaの範囲へ切り詰めずにPythonの確定整数を表示する。"""
        self.data_label.setText(
            f"Python: byte={self.data.byte_value}, "
            f"short={self.data.short_value}, long={self.data.long_value}"
        )


class PythonMayaIntWindow(qt.QDialog):
    """Python整数正本とMaya同期の確認Window。"""

    def __init__(
        self,
        data: MayaIntSampleData,
        node_name: str,
        plugs: tuple[MayaIntPlug, MayaIntPlug, MayaIntPlug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """サンプルを配置し、途中の初期同期失敗では生成済みBindingを解放する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilPythonIntMayaViewSampleWindow")
        self.setWindowTitle("bakedanuki-util Python int / Maya")
        self.node_name = node_name
        try:
            self.widget = PythonMayaIntWidget(data, plugs, self)
        except Exception:
            find_children = cast(
                Callable[[type[qt.QObject]], list[qt.QObject]],
                getattr(self, "findChildren"),
            )
            for child in find_children(qt.QObject):
                if isinstance(child, MayaIntBinding):
                    child.dispose()
            self.deleteLater()
            raise
        layout = qt.QVBoxLayout(self)
        layout.addWidget(qt.QLabel(f"同期先: {node_name}", self))
        layout.addWidget(
            qt.QLabel(
                "Pythonが正本です。Mayaの範囲外の値は同期保留になります。",
                self,
            )
        )
        layout.addWidget(self.widget)


_controller: MayaWindowController[PythonMayaIntWindow] | None = None


def show(
    node_name: str, data: MayaIntSampleData | None = None
) -> PythonMayaIntWindow:
    """既存属性へPython初期値を適用し、同期Windowを開く。

    `node_name`には`byteValue`・`shortValue`・`longValue`が必要。
    `data`省略時は新しいサンプルデータを使用する。
    """
    global _controller
    plugs = (
        resolve_int_plug(node_name, "byteValue"),
        resolve_int_plug(node_name, "shortValue"),
        resolve_int_plug(node_name, "longValue"),
    )
    source = data if data is not None else MayaIntSampleData()
    dispose()

    def create_window(parent: qt.QWidget | None = None) -> PythonMayaIntWindow:
        """同じPython正本を持つWindowを生成する。"""
        return PythonMayaIntWindow(source, node_name, plugs, parent)

    _controller = MayaWindowController(create_window)
    try:
        return _controller.show()
    except Exception:
        dispose()
        raise


def show_demo(data: MayaIntSampleData | None = None) -> PythonMayaIntWindow:
    """現在のsceneに検証ノードを一つ追加し、Python正本でWindowを開く。"""
    node_name = cmds.createNode("transform", name="bdPythonIntSample")
    for name, kind in (
        ("byteValue", "byte"),
        ("shortValue", "short"),
        ("longValue", "long"),
    ):
        if kind == "short":
            cmds.addAttr(
                node_name,
                longName=name,
                attributeType=kind,
                keyable=True,
                minValue=-20,
                maxValue=20,
            )
        else:
            cmds.addAttr(
                node_name, longName=name, attributeType=kind, keyable=True
            )
    return show(node_name, data)


def dispose() -> None:
    """Windowとcallbackを終了し、PythonデータとMayaノードを残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
