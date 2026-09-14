# coding: utf-8
from .... import qt
from ...float._validation import require_decimals
from ...float.view.label import FloatLabel
from ..binding import Float3Binding
from ..store import Float3ValueStore
from ..view_model import Float3ViewModel
from ._source import resolve_float3_view_source


class Float3Label(qt.QWidget):
    """X・Y・ZのFloatLabelを横に並べる、各軸をコピー可能な読み取り専用View。"""

    def __init__(
        self,
        view_model: Float3ViewModel | Float3Binding[Float3ValueStore],
        parent: qt.QWidget | None = None,
        *,
        decimals: int = 6,
    ) -> None:
        """同じ正本を参照する3成分ラベルを、全軸共通の桁数で生成する。"""
        view_model, binding = resolve_float3_view_source(view_model)
        decimals = require_decimals(decimals)
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._decimals = decimals
        try:
            # 各軸の表示・コピー・単位追従・終了処理は単一値ラベルへ委譲する。
            self.x_label = FloatLabel(view_model.x, self, decimals=decimals)
            self.y_label = FloatLabel(view_model.y, self, decimals=decimals)
            self.z_label = FloatLabel(view_model.z, self, decimals=decimals)
            self._labels = (self.x_label, self.y_label, self.z_label)
            layout = qt.QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            for axis, label in zip(("X", "Y", "Z"), self._labels):
                label.setAccessibleName(axis)
                label.setToolTip(
                    f"{axis}; select the displayed value to copy."
                )
                layout.addWidget(qt.QLabel(axis, self))
                layout.addWidget(label, 1)
            self.setFocusProxy(self.x_label)
            qt.QWidget.setTabOrder(self.x_label, self.y_label)
            qt.QWidget.setTabOrder(self.y_label, self.z_label)
        except Exception:
            # 部分的な生成失敗でも、共有Bindingを終了せず子Widgetだけを片付ける。
            self.setParent(None)
            self.deleteLater()
            raise

    @property
    def view_model(self) -> Float3ViewModel:
        """表示対象のViewModelを返し、終了後は例外を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のFloat3ViewModelは終了しています")
        return self._view_model

    def decimals(self) -> int:
        """全軸共通として指定した表示桁数を返す。"""
        return self._decimals

    def setDecimals(self, decimals: int) -> None:
        """全軸の表示桁数を揃え、正本の値と精度を保持する。"""
        decimals = require_decimals(decimals)
        self._decimals = decimals
        for label in self._labels:
            label.setDecimals(decimals)
