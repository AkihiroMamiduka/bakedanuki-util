# coding: utf-8
from __future__ import annotations

from sys import float_info

from .... import qt
from .._validation import require_decimals, require_float
from ..binding import FloatBinding
from ..store import FloatValueStore
from ..view_model import FloatViewModel
from ._connection import connect_queued_qt_signal, disconnect_qt_connection
from ._source import resolve_float_view_source


class FloatSpinBox(qt.QDoubleSpinBox):
    """公開値を表示単位に変換して編集するQDoubleSpinBox。

    decimalsは表示・入力の小数桁数、single_stepは表示単位での刻み幅。
    表示の丸めや単位変更を正本へ書き戻さない。
    """

    def __init__(
        self,
        view_model: FloatViewModel | FloatBinding[FloatValueStore],
        parent: qt.QWidget | None = None,
        *,
        decimals: int = 6,
        single_step: float = 0.1,
    ) -> None:
        """ViewModelまたはBindingと、表示桁数・刻み幅で初期化する。"""
        # 入力元を解決し、Widget生成前に表示・入力設定を検証する。
        view_model, binding = resolve_float_view_source(view_model)
        decimals = require_decimals(decimals)
        single_step = require_float(single_step, "single_step")
        if single_step <= 0:
            raise ValueError("single_stepには正の値を指定してください")

        # Viewだけを保持する構成でもBindingとViewModelを存続させる。
        super().__init__(parent)
        self._binding = binding
        self._view_model = view_model
        self._input_enabled = True

        # 表示桁数・刻み幅を設定し、入力途中の逐次確定と値の循環を止める。
        self.setDecimals(decimals)
        self.setSingleStep(single_step)
        self.setKeyboardTracking(False)
        self.setWrapping(False)

        # 入力通知を接続する前に、確定値と編集可否を初期表示する。
        self._render()
        self._update_enabled()

        # ユーザー入力とViewModel側の値・表示情報・編集可否を接続する。
        self._input_connection: qt.QtCore.QMetaObject.Connection | None = (
            self.valueChanged.connect(self._request_value)
        )
        view_model.value.changed.connect(self._update_value)
        view_model.presentation_changed.connect(self._update_presentation)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )

        # QObjectの破棄が完了してから、次のevent loopで入力を停止する。
        connect_queued_qt_signal(
            view_model.destroyed, self._on_view_model_destroyed
        )

    @property
    def view_model(self) -> FloatViewModel:
        """表示・操作対象のViewModelを返し、破棄済みなら例外を送出する。"""
        view_model = self._valid_view_model()
        if view_model is None:
            raise RuntimeError("表示対象のFloatViewModelは破棄されています")
        return view_model

    def isInputEnabled(self) -> bool:
        """正本の編集可否とは独立した、この入力欄の操作設定を返す。"""
        return self._input_enabled

    def setInputEnabled(self, enabled: bool) -> None:
        """表示更新を継続しながら、この入力欄からの値変更を許可・禁止する。"""
        if type(enabled) is not bool:
            raise TypeError("enabledにはboolを指定してください")
        self._input_enabled = enabled
        self._update_enabled()

    @qt.Slot()
    def _update_enabled(self) -> None:
        """View固有の操作設定と正本の編集可否を組み合わせる。"""
        view_model = self._valid_view_model()
        self.setEnabled(
            self._input_enabled
            and view_model is not None
            and not view_model.is_disposed
            and view_model.set_value_command.can_execute
        )

    def _request_value(self, value: float) -> None:
        """表示単位の入力をCommandへ渡し、実行後の確定値を再表示する。"""
        # 入力元が破棄済みなら、Commandを実行せず接続を終了する。
        view_model = self._valid_view_model()
        if view_model is None:
            self._disable_binding()
            return
        # 明示的に無効化した入力は、setValueによる通知も正本へ渡さない。
        if not self._input_enabled:
            self._render()
            return

        # 公開単位へ変換して値の変更を要求する。
        try:
            view_model.set_value_command.execute(
                view_model.presentation.from_display(value)
            )
        finally:
            # 入力の補正・拒否・失敗時も、正本の確定値へ表示を戻す。
            if qt.isValid(self) and self._valid_view_model() is not None:
                self._render()

    def _render(self) -> None:
        """入力通知を抑止し、確定値・単位表記・範囲を表示へ反映する。"""
        # 確定値を現在の表示単位へ変換する。
        view_model = self.view_model
        presentation = view_model.presentation
        value = presentation.to_display(view_model.value.value)

        # 上下限を表示単位へ変換し、制限のない側にはdoubleの有限範囲を使う。
        minimum = (
            -float_info.max
            if presentation.minimum is None
            else presentation.to_display(presentation.minimum)
        )
        maximum = (
            float_info.max
            if presentation.maximum is None
            else presentation.to_display(presentation.maximum)
        )

        # 表示の丸めや範囲更新によるvalueChangedを正本へ書き戻さない。
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.setSuffix(presentation.suffix)
            self.setRange(minimum, maximum)
            self.setValue(value)
        finally:
            del blocker

    def _update_value(self, _value: float) -> None:
        """値の変更通知を受け、ViewModelの最新の確定値を表示する。"""
        self._render()

    def _update_presentation(self, _presentation: object) -> None:
        """表示情報の変更通知を受け、値・単位表記・範囲を更新する。"""
        # 単位変更前の未確定テキストは破棄し、正本から再表示する。
        self._render()

    def _valid_view_model(self) -> FloatViewModel | None:
        """C++ objectも生存しているViewModelだけを返す。"""
        return self._view_model if qt.isValid(self._view_model) else None

    def _disable_binding(self) -> None:
        """入力接続を解除し、SpinBoxが生存していれば編集を無効にする。"""
        # 再度呼ばれた場合も入力接続の解除を安全に処理する。
        disconnect_qt_connection(self._input_connection)
        self._input_connection = None

        # 親と同時に破棄される場合は、破棄済みWidgetへアクセスしない。
        if qt.isValid(self):
            self.setEnabled(False)

    @qt.Slot()
    def _on_view_model_destroyed(self) -> None:
        """ViewModelの破棄通知を受け、UIからの入力を停止する。"""
        self._disable_binding()
