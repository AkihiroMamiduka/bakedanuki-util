# coding: utf-8
"""整数の複合Slider Viewと、ViewごとのMin／Max／Step保存を確認する。"""

from __future__ import annotations

from collections.abc import Callable
from typing import cast

from maya import cmds

from .....maya.ui import (
    MayaIntBinding,
    MayaIntPlugsBinding,
    MayaUiStateTracker,
    MayaWindowController,
    create_ui_state_manager,
    resolve_int_plug,
)
from .....ui import (
    IntBinding,
    IntLabel,
    IntRangeSliderSpinBox,
    IntSliderSpinBox,
    IntValueStore,
    PythonIntAttributeStore,
    qt,
)
from .data import IntSampleData
from .maya_plug import create_demo_nodes

__all__ = ["IntRangeSliderWindow", "show", "show_maya", "show_demo", "dispose"]


class IntRangeSliderWindow(qt.QDialog):
    """整数の範囲編集・Step方式・再表示時の設定復元を試すWindow。"""

    def __init__(
        self,
        node_names: tuple[str, str] | None = None,
        parent: qt.QWidget | None = None,
    ) -> None:
        """Python正本と、任意のMaya正本・Python同期行を構築する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilIntRangeSliderSampleWindow")
        self.setWindowTitle("bakedanuki-util int Range Slider")
        self.node_names = node_names
        self.editor_settings = create_ui_state_manager(
            "int_sample/editor_settings/range_slider"
        )
        self.editors: dict[str, IntRangeSliderSpinBox] = {}
        self.data = IntSampleData()
        self.python_binding = IntBinding.from_attribute(
            self.data, "signed_value", parent=self
        )
        self.maya_binding: MayaIntPlugsBinding | None = None
        self.sync_binding: (
            MayaIntBinding[PythonIntAttributeStore[IntSampleData]] | None
        ) = None
        layout = qt.QVBoxLayout(self)
        form = qt.QFormLayout()
        layout.addLayout(form)
        try:
            # 値は共有し、Min／Max／Stepは各行の独立した設定として保持する
            self.simple_editor = IntSliderSpinBox(
                self.python_binding,
                self,
                minimum=0,
                maximum=100,
                layout_order="value_slider",
                value_select_all_on_mouse_focus=True,
            )
            self.simple_editor.spin_box.setFixedWidth(140)
            form.addRow("基本 [値][Slider]", self.simple_editor)
            self.python_editor = self._add_editor(
                form, "python", "Python 加算Step", self.python_binding, 0, 100
            )
            self.linked_editor = self._add_editor(
                form,
                "linked",
                "共有 10倍Step",
                self.python_binding,
                -10,
                10,
                multiplicative=True,
            )
            form.addRow("Python 確定値", IntLabel(self.python_binding, self))
            if node_names is not None:
                self.maya_binding = MayaIntPlugsBinding(
                    tuple(
                        resolve_int_plug(n, "longValue") for n in node_names
                    ),
                    parent=self,
                    edit_connected=True,
                )
                self._add_editor(
                    form,
                    "maya",
                    "Maya long（二ノード）",
                    self.maya_binding,
                    -100,
                    100,
                    multiplicative=True,
                )
                self.sync_data = IntSampleData()
                self.sync_binding = MayaIntBinding.from_attribute(
                    self.sync_data,
                    "signed_value",
                    parent=self,
                    maya_plug=resolve_int_plug(node_names[0], "pythonValue"),
                )
                self._add_editor(
                    form,
                    "sync",
                    "Python → Maya long",
                    self.sync_binding,
                    0,
                    100,
                    multiplicative=True,
                )
            description = qt.QLabel(
                "範囲編集行は [Min][Slider][Max][値][Step] です。\n"
                "Min／Max／Stepは各行で独立し、閉じて再表示すると復元されます。\n"
                "Min／Maxの上下操作は1刻み、Stepは値欄だけに適用します。\n"
                "範囲外の確定値は保持されます。Maya行のドラッグは一回Undoで戻せます。",
                self,
            )
            description.setWordWrap(True)
            layout.addWidget(description)
            self.reset_button = qt.QPushButton(
                "操作範囲とStepを初期値へ戻す", self
            )
            self.reset_button.clicked.connect(self.reset_settings)
            layout.addWidget(self.reset_button)
            self.editor_settings_tracker = MayaUiStateTracker.for_window(
                self.editor_settings, self
            )
            self.resize(1060, self.sizeHint().height())
        except Exception:
            # 途中でMaya属性解決に失敗しても、生成済みの同期を確実に終了する
            find_children = cast(
                Callable[[type[qt.QObject]], list[qt.QObject]],
                getattr(self, "findChildren"),
            )
            for child in find_children(qt.QObject):
                if isinstance(child, IntBinding):
                    child.dispose()
            self.deleteLater()
            raise

    def _add_editor(
        self,
        form: qt.QFormLayout,
        key: str,
        title: str,
        binding: IntBinding[IntValueStore],
        minimum: int,
        maximum: int,
        *,
        multiplicative: bool = False,
    ) -> IntRangeSliderSpinBox:
        """表示と保存キーを対応させ、設定だけを保存する行を追加する。"""
        editor = IntRangeSliderSpinBox(
            binding,
            self,
            minimum=minimum,
            maximum=maximum,
            step_mode="multiplicative" if multiplicative else "additive",
            minimum_width=140,
            maximum_width=140,
            value_width=140,
            step_width=110,
            value_select_all_on_mouse_focus=True,
        )
        editor.slider.setMinimumWidth(150)
        form.addRow(title, editor)
        self.editors[key] = editor
        self.editor_settings.register_int_range_slider_spin_box(key, editor)
        return editor

    def reset_settings(self) -> None:
        """正本の値を維持し、全行の操作設定だけを初期値へ戻す。"""
        defaults = {
            "python": (0, 100),
            "linked": (-10, 10),
            "maya": (-100, 100),
            "sync": (0, 100),
        }
        for key, editor in self.editors.items():
            editor.setIntRange(*defaults[key])
            editor.setSingleStep(1)


_controller: MayaWindowController[IntRangeSliderWindow] | None = None


def _show(node_names: tuple[str, str] | None) -> IntRangeSliderWindow:
    """前のWindowを終了して今回の同期対象を一つのWindowに表示する。"""
    global _controller
    dispose()

    def create_window(
        parent: qt.QWidget | None = None,
    ) -> IntRangeSliderWindow:
        """今回のノード指定を保持したWindowを生成する。"""
        return IntRangeSliderWindow(node_names, parent)

    _controller = MayaWindowController(create_window)
    try:
        return _controller.show()
    except Exception:
        dispose()
        raise


def show() -> IntRangeSliderWindow:
    """sceneを変更せずPython正本のサンプルを表示する。"""
    return _show(None)


def show_maya(node_name: str, other_node_name: str) -> IntRangeSliderWindow:
    """既存二ノードの`longValue`と第一ノードの`pythonValue`を編集する。"""
    return _show((node_name, other_node_name))


def show_demo() -> IntRangeSliderWindow:
    """現在のsceneへ二ノードを追加し、Maya連携サンプルを表示する。"""
    first, second = create_demo_nodes()
    cmds.addAttr(
        first, longName="pythonValue", attributeType="long", keyable=True
    )
    return show_maya(first, second)


def dispose() -> None:
    """Window・Binding・callbackを終了する。検証用ノードは残す。"""
    global _controller
    if _controller is not None:
        _controller.dispose()
        _controller = None
