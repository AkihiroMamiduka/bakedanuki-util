# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import cast

from .... import qt
from .._validation import require_decimals
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._connection import connect_queued_qt_signal
from ._source import resolve_float_view_source


class FloatLabel(qt.QLabel):
    """確定値を表示単位と指定桁数で表示する、コピー可能な数値ラベル。"""

    def __init__(
        self,
        view_model: FloatViewModel | FloatBinding[FloatValueStore],
        parent: qt.QWidget | None = None,
        *,
        decimals: int = 6,
    ) -> None:
        """BindingまたはViewModelを共有し、正本への書き込みなしで表示する。"""
        view_model, binding = resolve_float_view_source(view_model)
        decimals = require_decimals(decimals)
        if view_model.is_disposed:
            raise RuntimeError("表示対象のFloatViewModelは終了しています")

        # Viewだけを保持する構成でも、共有するBindingとViewModelを存続させる。
        self._ready = False
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._decimals = decimals
        self.setTextFormat(qt.Qt.TextFormat.PlainText)
        self.setTextInteractionFlags(
            qt.Qt.TextInteractionFlag.TextSelectableByMouse
            | qt.Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        self.setAlignment(
            qt.Qt.AlignmentFlag.AlignRight | qt.Qt.AlignmentFlag.AlignVCenter
        )
        self._ready = True
        self._render()

        # 書き込み可否に依存せず、値・単位・明示終了だけを監視する。
        view_model.value.changed.connect(self._update_value)
        view_model.presentation_changed.connect(self._update_presentation)
        view_model.disposed.connect(self._on_view_model_disposed)
        connect_queued_qt_signal(
            view_model.destroyed, self._on_view_model_disposed
        )

    @property
    def view_model(self) -> FloatViewModel:
        """生存中のViewModelを返し、終了後は例外を送出する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のFloatViewModelは終了しています")
        return view_model

    def decimals(self) -> int:
        """表示する小数桁数を返す。"""
        return self._decimals

    def setDecimals(self, decimals: int) -> None:
        """表示桁数だけを変更し、正本の精度を維持する。"""
        decimals = require_decimals(decimals)
        if decimals != self._decimals:
            self._decimals = decimals
            self._render()

    def _render(self) -> None:
        """確定値を範囲制限なしで表示し、選択中の同値テキストは維持する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            self._on_view_model_disposed()
            return
        presentation = view_model.presentation
        try:
            value = presentation.to_display(view_model.value.value)
        except ValueError:
            # 表示単位への変換がoverflowしても、正本と他のViewへ影響させない。
            text = "—" + presentation.suffix
        else:
            locale = self.locale()
            locale.setNumberOptions(
                locale.numberOptions()
                | qt.QtCore.QLocale.NumberOption.OmitGroupSeparator
            )
            # Qt 6.5 stubのchar引数を、実行時に受け付けるstrへ限定する。
            format_number = cast(
                Callable[[float, str, int], str], locale.toString
            )
            number = format_number(value, "f", self._decimals)
            # 表示上の負のゼロだけを除き、SpinBoxと同じゼロ表記にする。
            if value < 0:
                rounded, valid = locale.toDouble(number)
                if valid and rounded == 0.0:
                    number = format_number(0.0, "f", self._decimals)
            text = number + presentation.suffix
        if text != self.text():
            self.setText(text)

    @qt.Slot(float)
    def _update_value(self, _value: float) -> None:
        """通知先から再編集された場合も、最新の確定値を表示する。"""
        self._render()

    @qt.Slot(object)
    def _update_presentation(self, _presentation: object) -> None:
        """表示単位の変更を読み直し、正本へ書き戻さず表示する。"""
        self._render()

    def changeEvent(self, arg__1: qt.QEvent) -> None:
        """Widgetのlocale変更に合わせ、小数点表記を更新する。"""
        super().changeEvent(arg__1)
        if self._ready and arg__1.type() == qt.QEvent.Type.LocaleChange:
            self._render()

    def _valid_view_model(self) -> FloatViewModel | None:
        """明示終了とQObject破棄の両方を確認する。"""
        view_model = self._view_model
        return view_model if not view_model.is_disposed else None

    @qt.Slot()
    def _on_view_model_disposed(self) -> None:
        """終了後は最後のテキストを残し、破棄済みWidgetには触れない。"""
        if qt.isValid(self):
            self.setEnabled(False)
