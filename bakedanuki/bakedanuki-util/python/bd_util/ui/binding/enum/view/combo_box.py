# coding: utf-8
from __future__ import annotations

from collections.abc import Callable

from .... import qt
from .._connection import connect_queued_qt_signal
from ..binding import EnumBinding
from ..definition import EnumItem
from ..store import EnumValueStore
from ..view_model import EnumViewModel
from ._source import resolve_enum_view_source


def _require_enabled(value: object) -> bool:
    if not isinstance(value, bool):
        raise TypeError("enabledにはboolを指定してください")
    return value


class EnumComboBox(qt.QComboBox):
    """enumの整数値を項目dataとして扱うコンボボックス。"""

    def __init__(
        self,
        view_model: EnumViewModel | EnumBinding[EnumValueStore],
        parent: qt.QWidget | None = None,
        *,
        wheel_requires_focus: bool = False,
    ) -> None:
        """enum の選択肢と確定値を表示する。

        Args:
            view_model: 表示する ViewModel またはその Binding。
            parent: Qt の親 Widget。
            wheel_requires_focus: ``True`` なら非フォーカス時のホイール入力を親へ渡す。
        """
        if type(wheel_requires_focus) is not bool:
            raise TypeError("wheel_requires_focusにはboolを指定してください")
        view_model, binding = resolve_enum_view_source(view_model)
        super().__init__(parent)
        self._view_model = view_model
        self._binding = binding
        self._input_enabled = True
        self.set_wheel_requires_focus(wheel_requires_focus)
        self._value_request_handler: Callable[[int], bool] | None = None
        self._render()
        self.currentIndexChanged.connect(self._request_index)
        view_model.value.changed.connect(self._render)
        view_model.definition_changed.connect(self._render)
        view_model.set_value_command.can_execute_changed.connect(
            self._update_enabled
        )
        view_model.disposed.connect(self._disable_binding)
        connect_queued_qt_signal(view_model.destroyed, self._disable_binding)

    @property
    def view_model(self) -> EnumViewModel:
        """表示対象を返す。終了済みの場合は ``RuntimeError`` を送出する。"""
        if self._view_model.is_disposed:
            raise RuntimeError("表示対象のEnumViewModelは終了しています")
        return self._view_model

    def isInputEnabled(self) -> bool:
        """この View 固有の入力許可設定を返す。"""
        return self._input_enabled

    def setInputEnabled(self, enabled: bool) -> None:
        """この View からの入力を許可または停止する。

        Args:
            enabled: 入力を許可する場合は ``True``。

        Raises:
            TypeError: ``enabled`` が ``bool`` でない場合。
        """
        self._input_enabled = _require_enabled(enabled)
        self._update_enabled()

    def wheel_requires_focus(self) -> bool:
        """ホイール操作にフォーカスを必須とする設定を返す。"""
        return self._wheel_requires_focus

    def set_wheel_requires_focus(self, required: bool) -> None:
        """フォーカス必須時は、ホイールによる自動フォーカス移動も止める。"""
        if type(required) is not bool:
            raise TypeError("requiredにはboolを指定してください")
        self._wheel_requires_focus = required
        self.setFocusPolicy(
            qt.Qt.FocusPolicy.StrongFocus
            if required
            else qt.Qt.FocusPolicy.WheelFocus
        )

    def setValueRequestHandler(
        self, handler: Callable[[int], bool] | None
    ) -> None:
        """選択時に整数値を受け取る入力 handler を設定する。

        Args:
            handler: 入力を処理したら ``True`` を返す関数。``False`` または
                ``None`` の場合は ViewModel の Command が値を設定する。

        Raises:
            TypeError: ``handler`` が呼び出し可能でも ``None`` でもない場合。
        """
        if handler is not None and not callable(handler):
            raise TypeError(
                "handlerには呼出し可能な関数またはNoneを指定してください"
            )
        self._value_request_handler = handler

    def _update_enabled(self, *_args: object) -> None:
        self.setEnabled(
            self._input_enabled
            and not self._view_model.is_disposed
            and self._view_model.set_value_command.can_execute
        )

    def _render(self, *_args: object) -> None:
        if self._view_model.is_disposed:
            self._disable_binding()
            return
        vm = self._view_model
        # 選択肢を再構築しても入力イベントとして扱わず、未定義値はプレースホルダーに残す。
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.clear()
            selected = -1
            for index, item in enumerate(vm.definition.items):
                self.addItem(item.name, item)
                if item.value == vm.value.value:
                    selected = index
            self.setPlaceholderText(f"未定義 ({vm.value.value})")
            self.setCurrentIndex(selected)
            self._update_enabled()
        finally:
            del blocker

    def _request_index(self, index: int) -> None:
        vm = self._view_model
        if vm.is_disposed:
            self._disable_binding()
            return
        if not self._input_enabled:
            self._render()
            return
        # QVariantの整数変換を避け、Python objectとして値を保持する。
        item = self.itemData(index)
        if not isinstance(item, EnumItem):
            self._render()
            return
        try:
            handler = self._value_request_handler
            if handler is None or not handler(item.value):
                vm.set_value_command.execute(item.value)
        finally:
            if qt.isValid(self):
                self._render()

    def wheelEvent(self, event: qt.QtGui.QWheelEvent) -> None:
        """設定に応じて、非フォーカス時のホイールを親へ渡す。"""
        if self._wheel_requires_focus and not self.hasFocus():
            event.ignore()
            return
        super().wheelEvent(event)

    @qt.Slot()
    def _disable_binding(self) -> None:
        if qt.isValid(self):
            self.setEnabled(False)
