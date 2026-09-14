# coding: utf-8
from collections.abc import Callable, Sequence
from typing import Generic, TypeVar

from .... import qt
from ...float._validation import require_float, require_slider_range
from ...float.view.slider_spin_box import FloatSliderSpinBox
from ...float.view_model import FloatViewModel
from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..value import Float3, require_float3
from ..view_model import Float3ViewModel
from ._source import resolve_float3_view_source

_EditorT = TypeVar("_EditorT", bound=FloatSliderSpinBox)


def _require_axis_values(value: object, name: str) -> Float3:
    """共通の数値またはXYZの3成分を、有限なfloatのtupleへ揃える。"""
    if isinstance(value, (int, float)):
        scalar = require_float(value, name)
        return scalar, scalar, scalar
    return require_float3(value)


class Float3SliderSpinBoxBase(qt.QWidget, Generic[_EditorT]):
    """具体型を維持した3つの編集欄の配置と寿命を共有する内部基盤。"""

    def __init__(
        self,
        view_model: Float3ViewModel | Float3Binding[Float3ValueStore],
        parent: qt.QWidget | None,
        *,
        minimum: float | Sequence[float],
        maximum: float | Sequence[float],
        create_editor: Callable[
            [FloatViewModel, qt.QWidget, float, float], _EditorT
        ],
    ) -> None:
        """入力元と全軸の範囲を検証し、既存のscalar Viewを組み立てる。"""
        # 子Widget生成前に全軸の設定を検証し、途中までの生成を避ける。
        view_model, binding = resolve_float3_view_source(view_model)
        minima = _require_axis_values(minimum, "minimum")
        maxima = _require_axis_values(maximum, "maximum")
        ranges = tuple(
            require_slider_range(lower, upper)
            for lower, upper in zip(minima, maxima)
        )
        self._ready = False
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model

        # 各成分の同期・単位変換・連続編集は既存のscalar Viewへ委譲する。
        try:
            self.x_editor = create_editor(view_model.x, self, *ranges[0])
            self.y_editor = create_editor(view_model.y, self, *ranges[1])
            self.z_editor = create_editor(view_model.z, self, *ranges[2])
            self._editors = (self.x_editor, self.y_editor, self.z_editor)
            self.x_spin_box = self.x_editor.spin_box
            self.y_spin_box = self.y_editor.spin_box
            self.z_spin_box = self.z_editor.spin_box

            # 行ごとに軸名を付け、Tab順もXYZの表示順へ揃える。
            layout = qt.QFormLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setFieldGrowthPolicy(
                qt.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow
            )
            previous: qt.QWidget | None = None
            for axis, editor in zip(("X", "Y", "Z"), self._editors):
                editor.slider.setAccessibleName(f"{axis} slider")
                editor.spin_box.setAccessibleName(axis)
                layout.addRow(axis, editor)
                for widget in self._tab_widgets(editor):
                    if previous is not None:
                        qt.QWidget.setTabOrder(previous, widget)
                    previous = widget
            self.setSizePolicy(
                qt.QSizePolicy.Policy.Expanding, qt.QSizePolicy.Policy.Fixed
            )
            self.setFocusPolicy(qt.Qt.FocusPolicy.StrongFocus)
            self.setFocusProxy(self.x_editor.focusProxy())
            self._ready = True
        except Exception:
            # 部分生成に失敗しても、共有Bindingを残して自身と子だけを片付ける。
            self.setParent(None)
            self.deleteLater()
            raise

    def _tab_widgets(self, editor: _EditorT) -> tuple[qt.QWidget, ...]:
        """各行のフォーカス移動順を返す。"""
        return editor.slider, editor.spin_box

    @property
    def view_model(self) -> Float3ViewModel:
        """共有ViewModelを返し、明示終了・Qt破棄後は例外を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("編集対象のFloat3ViewModelは終了しています")
        return self._view_model

    def event(self, event: qt.QEvent) -> bool:
        """子へhide通知が届かない場合も、このViewの連続編集を終了する。"""
        if (
            self._ready
            and event.type()
            in (
                qt.QEvent.Type.Close,
                qt.QEvent.Type.Hide,
                qt.QEvent.Type.HideToParent,
                qt.QEvent.Type.WindowDeactivate,
            )
            and not self._view_model.is_disposed
        ):
            for component, editor in zip(
                (self._view_model.x, self._view_model.y, self._view_model.z),
                self._editors,
            ):
                component.end_edit(editor.slider)
        return super().event(event)
