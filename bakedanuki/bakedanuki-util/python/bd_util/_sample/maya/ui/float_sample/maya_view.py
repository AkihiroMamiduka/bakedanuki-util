# coding: utf-8
"""Python正本の3つの単一float属性をQtとMayaへ同期するサンプル。"""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from .....maya.ui import (
    MayaFloatBinding,
    MayaFloatPlug,
    MayaWindowController,
    get_channel_box_precision,
    resolve_float_plug,
)
from .....ui import FloatLabel, FloatSlider, FloatSpinBox, qt
from .data import TransformFloatData


class TransformFloatWidget(qt.QWidget):
    """Pythonの各属性と、既存transformのX属性を共有Viewで編集する。"""

    def __init__(
        self,
        data: TransformFloatData,
        plugs: tuple[MayaFloatPlug, MayaFloatPlug, MayaFloatPlug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """単位の異なる3つのBindingを作り、Python初期値をMayaへ反映する。"""
        super().__init__(parent)
        self.data = data
        self.translate_x_binding = MayaFloatBinding.from_attribute(
            data, "translate_x", maya_plug=plugs[0], parent=self
        )
        self.rotate_x_binding = MayaFloatBinding.from_attribute(
            data, "rotate_x", maya_plug=plugs[1], parent=self
        )
        self.scale_x_binding = MayaFloatBinding.from_attribute(
            data, "scale_x", maya_plug=plugs[2], parent=self
        )
        self.bindings = (
            self.translate_x_binding,
            self.rotate_x_binding,
            self.scale_x_binding,
        )
        decimals = get_channel_box_precision()
        self.translate_x = FloatSpinBox(
            self.translate_x_binding, self, decimals=decimals, single_step=0.1
        )
        self.rotate_x = FloatSpinBox(
            self.rotate_x_binding, self, decimals=decimals, single_step=1.0
        )
        self.scale_x = FloatSpinBox(
            self.scale_x_binding, self, decimals=decimals, single_step=0.01
        )
        self.linked_translate_x = FloatSpinBox(
            self.translate_x_binding, self, decimals=6, single_step=0.1
        )
        self.translate_x_label = FloatLabel(
            self.translate_x_binding, self, decimals=decimals
        )
        self.linked_translate_x_label = FloatLabel(
            self.translate_x_binding, self, decimals=6
        )
        self.rotate_x_label = FloatLabel(
            self.rotate_x_binding, self, decimals=decimals
        )
        self.scale_x_label = FloatLabel(
            self.scale_x_binding, self, decimals=decimals
        )
        # Pythonの公開値に対する操作範囲を、各Viewから共有する。
        self.translate_x_slider = FloatSlider(
            self.translate_x_binding,
            self,
            minimum=-100,
            maximum=100,
            steps=2000,
        )
        self.linked_translate_x_slider = FloatSlider(
            self.translate_x_binding,
            self,
            minimum=-100,
            maximum=100,
            steps=2000,
        )
        self.rotate_x_slider = FloatSlider(
            self.rotate_x_binding, self, minimum=-180, maximum=180, steps=3600
        )
        self.scale_x_slider = FloatSlider(
            self.scale_x_binding, self, minimum=0, maximum=3, steps=3000
        )

        # Pythonの実値と共有Viewを並べ、表示精度とデータの精度を確認する。
        form = qt.QFormLayout()
        for title, spin_box, label, slider in (
            (
                "Translate X",
                self.translate_x,
                self.translate_x_label,
                self.translate_x_slider,
            ),
            (
                "Translate X (6 decimals)",
                self.linked_translate_x,
                self.linked_translate_x_label,
                self.linked_translate_x_slider,
            ),
            (
                "Rotate X",
                self.rotate_x,
                self.rotate_x_label,
                self.rotate_x_slider,
            ),
            ("Scale X", self.scale_x, self.scale_x_label, self.scale_x_slider),
        ):
            row = qt.QHBoxLayout()
            slider.setMinimumWidth(160)
            row.addWidget(slider, 1)
            row.addWidget(spin_box)
            row.addWidget(label, 1)
            form.addRow(title, row)
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
        self.data.translate_x = 10.0
        self.data.rotate_x = 20.0
        self.data.scale_x = 2.0
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
            f"Python: {self.data.translate_x!r} cm / "
            f"{self.data.rotate_x!r} deg / {self.data.scale_x!r}"
        )


class TransformFloatWindow(qt.QDialog):
    """Python正本とMaya Viewの同期サンプルを所有するWindow。"""

    def __init__(
        self,
        data: TransformFloatData,
        plugs: tuple[MayaFloatPlug, MayaFloatPlug, MayaFloatPlug],
        parent: qt.QWidget | None = None,
    ) -> None:
        """データと既存plugを受け取り、サンプルWidgetを配置する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilPythonFloatMayaViewSampleWindow")
        self.setWindowTitle("bakedanuki-util Python float / Maya")
        try:
            self.widget = TransformFloatWidget(data, plugs, self)
        except Exception:
            # 途中の属性だけ接続できた場合も、生成済みBindingを終了する。
            find_children = cast(
                Callable[[type[qt.QObject]], list[qt.QObject]],
                getattr(self, "findChildren"),
            )
            for child in find_children(qt.QObject):
                if isinstance(child, MayaFloatBinding):
                    child.dispose()
            self.deleteLater()
            raise
        layout = qt.QVBoxLayout(self)
        layout.addWidget(self.widget)


_controller: MayaWindowController[TransformFloatWindow] | None = None


def show(
    node_name: str, data: TransformFloatData | None = None
) -> TransformFloatWindow:
    """指定transformへPython初期値を適用し、同期Windowを表示する。"""
    global _controller
    plugs = (
        resolve_float_plug(node_name, "translateX"),
        resolve_float_plug(node_name, "rotateX"),
        resolve_float_plug(node_name, "scaleX"),
    )
    source = data if data is not None else TransformFloatData()
    dispose()

    def create_window(
        parent: qt.QWidget | None = None,
    ) -> TransformFloatWindow:
        """同じPython正本を参照するWindowを生成する。"""
        return TransformFloatWindow(source, plugs, parent)

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
