# coding: utf-8
"""Python正本の3つの3成分tuple属性をQtとMayaへ同期するサンプル。"""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from .....maya.ui import (
    MayaFloat3Binding,
    MayaFloat3Plug,
    MayaWindowController,
    get_channel_box_precision,
    resolve_float3_plug,
)
from .....ui import Float3SpinBox, qt
from .data import TransformFloat3Data


class TransformFloat3Widget(qt.QWidget):
    """Pythonの各属性と、既存transformの3成分属性を共有Viewで編集する。"""

    def __init__(
        self,
        data: TransformFloat3Data,
        plugs: tuple[MayaFloat3Plug, MayaFloat3Plug, MayaFloat3Plug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """単位の異なる3つのBindingを作り、Python初期値をMayaへ反映する。"""
        super().__init__(parent)
        self.data = data
        self.translate_binding = MayaFloat3Binding.from_attribute(
            data, "translate", maya_plug=plugs[0], parent=self
        )
        self.rotate_binding = MayaFloat3Binding.from_attribute(
            data, "rotate", maya_plug=plugs[1], parent=self
        )
        self.scale_binding = MayaFloat3Binding.from_attribute(
            data, "scale", maya_plug=plugs[2], parent=self
        )
        self.bindings = (
            self.translate_binding,
            self.rotate_binding,
            self.scale_binding,
        )
        decimals = get_channel_box_precision()
        self.translate = Float3SpinBox(
            self.translate_binding, self, decimals=decimals, single_step=0.1
        )
        self.rotate = Float3SpinBox(
            self.rotate_binding, self, decimals=decimals, single_step=1.0
        )
        self.scale = Float3SpinBox(
            self.scale_binding, self, decimals=decimals, single_step=0.01
        )
        self.linked_translate = Float3SpinBox(
            self.translate_binding, self, decimals=6, single_step=0.1
        )

        # Pythonの実値と共有Viewを並べ、表示精度とデータの精度を確認する。
        form = qt.QFormLayout()
        form.addRow("Translate", self.translate)
        form.addRow("Translate (6 decimals)", self.linked_translate)
        form.addRow("Rotate", self.rotate)
        form.addRow("Scale", self.scale)
        self.data_label = qt.QLabel(self)
        self.result_label = qt.QLabel(self)
        self.set_data_button = qt.QPushButton("Set Python data", self)
        self.refresh_button = qt.QPushButton("Refresh views", self)
        self.retry_button = qt.QPushButton("Retry Maya sync", self)
        self.set_data_button.clicked.connect(self._set_data)
        self.refresh_button.clicked.connect(self._refresh_views)
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

    @qt.Slot()
    def _set_data(self) -> None:
        """Python正本だけを変更し、明示refreshとの違いを確認する。"""
        self.data.translate = (10.0, 20.0, 30.0)
        self.data.rotate = (20.0, 40.0, 60.0)
        self.data.scale = (2.0, 3.0, 4.0)
        self._update_data_label()

    @qt.Slot()
    def _refresh_views(self) -> None:
        """正本を読み直し、全Qt ViewとMaya属性へ同期する。"""
        for binding in self.bindings:
            binding.refresh()
        self._update_data_label()
        self._show_sync_result()

    @qt.Slot()
    def _retry_sync(self) -> None:
        """最後に確定したPython値を再同期し、成否を表示する。"""
        for binding in self.bindings:
            if binding.maya_view is not None:
                try:
                    binding.maya_view.sync_from_view_model()
                except Exception:
                    pass
        self._show_sync_result()

    def _show_sync_result(self) -> None:
        """明示操作した時点のMaya同期状態を表示する。"""
        states: list[str] = []
        for binding in self.bindings:
            view = binding.maya_view
            state = (
                "OK"
                if view is not None and view.is_synchronized
                else "Pending"
            )
            states.append(f"{binding.store.attribute_name}: {state}")
        self.result_label.setText("Last sync check: " + ", ".join(states))

    @qt.Slot()
    def _update_data_label(self) -> None:
        """表示用の丸めを加えず、Python値を公開単位付きで表示する。"""
        self.data_label.setText(
            f"Translate: {self.data.translate!r} cm\n"
            f"Rotate: {self.data.rotate!r} deg\nScale: {self.data.scale!r}"
        )


class TransformFloat3Window(qt.QDialog):
    """Python正本とMaya Viewの同期サンプルを所有するWindow。"""

    def __init__(
        self,
        data: TransformFloat3Data,
        plugs: tuple[MayaFloat3Plug, MayaFloat3Plug, MayaFloat3Plug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """データと既存plugを受け取り、サンプルWidgetを配置する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilPythonFloat3MayaViewSampleWindow")
        self.setWindowTitle("bakedanuki-util Python float3 / Maya")
        try:
            self.widget = TransformFloat3Widget(data, plugs, self)
        except Exception:
            # 途中の属性だけ接続できた場合も、生成済みBindingを終了する。
            find_children = cast(
                Callable[[type[qt.QObject]], list[qt.QObject]],
                getattr(self, "findChildren"),
            )
            for child in find_children(qt.QObject):
                if isinstance(child, MayaFloat3Binding):
                    child.dispose()
            self.deleteLater()
            raise
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller: MayaWindowController[TransformFloat3Window] | None = None


def show(
    node_name: str, data: TransformFloat3Data | None = None
) -> TransformFloat3Window:
    """指定transformへPython初期値を適用し、同期Windowを表示する。"""
    global _controller
    plugs = (
        resolve_float3_plug(node_name, "translate"),
        resolve_float3_plug(node_name, "rotate"),
        resolve_float3_plug(node_name, "scale"),
    )
    source = data if data is not None else TransformFloat3Data()
    dispose()

    def create_window(
        parent: qt.QWidget | None = None,
    ) -> TransformFloat3Window:
        """同じPython正本を参照するWindowを生成する。"""
        return TransformFloat3Window(source, plugs, parent)

    _controller = MayaWindowController(create_window)
    try:
        return _controller.show()
    except Exception:
        dispose()
        raise


def dispose() -> None:
    """Windowとcallbackを終了し、PythonとMayaの値は残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
