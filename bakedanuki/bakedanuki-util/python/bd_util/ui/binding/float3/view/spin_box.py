# coding: utf-8
from typing import cast

from .... import qt
from ...float._validation import require_decimals, require_float
from ...float.view.spin_box import FloatSpinBox
from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..view_model import Float3ViewModel


def _resolve_source(
    source: object,
) -> tuple[Float3ViewModel, Float3Binding[Float3ValueStore] | None]:
    """入力元を検証し、表示対象と参照保持するBindingへ解決する。"""
    binding = None
    if isinstance(source, Float3Binding):
        binding = cast(Float3Binding[Float3ValueStore], source)
        view_model = binding.view_model
    elif isinstance(source, Float3ViewModel):
        view_model = source
    else:
        raise TypeError(
            "view_modelにはFloat3ViewModelまたはFloat3Bindingを指定してください"
        )
    if view_model.is_disposed or view_model.store is None:
        raise RuntimeError(
            "表示対象のFloat3ViewModelには有効なStore接続が必要です"
        )
    return view_model, binding


class Float3SpinBox(qt.QWidget):
    """X・Y・ZのFloatSpinBoxを横に並べる3成分用View。"""

    def __init__(
        self,
        view_model: Float3ViewModel | Float3Binding[Float3ValueStore],
        parent: qt.QWidget | None = None,
        *,
        decimals: int = 6,
        single_step: float = 0.1,
    ) -> None:
        """共有ViewModelと各軸共通の表示・入力設定で初期化する。"""
        # Widget生成前に入力元と設定を検証する。
        view_model, binding = _resolve_source(view_model)
        decimals = require_decimals(decimals)
        single_step = require_float(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model

        # 各軸の入力経路・丸め防止・編集可否は既存のscalar Viewへ委譲する。
        self.x_spin_box = FloatSpinBox(
            view_model.x, self, decimals=decimals, single_step=single_step
        )
        self.y_spin_box = FloatSpinBox(
            view_model.y, self, decimals=decimals, single_step=single_step
        )
        self.z_spin_box = FloatSpinBox(
            view_model.z, self, decimals=decimals, single_step=single_step
        )
        layout = qt.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        for label, spin_box in zip(
            ("X", "Y", "Z"),
            (self.x_spin_box, self.y_spin_box, self.z_spin_box),
        ):
            spin_box.setAccessibleName(label)
            layout.addWidget(qt.QLabel(label, self))
            layout.addWidget(spin_box, 1)

    @property
    def view_model(self) -> Float3ViewModel:
        """表示・操作対象のViewModelを返す。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のFloat3ViewModelは終了しています")
        return self._view_model
