# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from functools import partial
from typing import Protocol, cast

from .... import qt
from ..._view_source import ViewSourceConnections
from ..binding import EnumBinding
from ..definition import EnumItem
from ..store import EnumValueStore
from ..view_model import EnumViewModel
from ._source import resolve_enum_view_source


class _QTimerType(Protocol):
    """PySide版ごとのsingleShotの型差を局所化する。"""

    @staticmethod
    def singleShot(milliseconds: int, callback: Callable[[], None]) -> None:
        """指定した遅延時間後に処理を一回だけ呼び出す。"""
        raise NotImplementedError


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
        self._source_connections = ViewSourceConnections(self)
        self._input_enabled = True
        self.set_wheel_requires_focus(wheel_requires_focus)
        self._value_request_handler: Callable[[int], bool] | None = None
        self._index_change_pending = False
        self.set_source(binding if binding is not None else view_model)
        self.currentIndexChanged.connect(self._index_changed)
        self.activated.connect(self._activate_index)

    def set_source(
        self, source: EnumViewModel | EnumBinding[EnumValueStore]
    ) -> None:
        """候補popupを閉じ、値と選択肢を書き込まずに表示先を交換する。

        入力handlerとView固有の設定を維持し、旧Bindingは破棄しない。

        Args:
            source: 生存中のViewModelまたはBinding。
        """
        view_model, binding = resolve_enum_view_source(source)
        generation = self._source_connections.generation
        blocker = qt.QtCore.QSignalBlocker(self)
        try:
            self.hidePopup()
            if (
                generation != self._source_connections.generation
                or not qt.isValid(self)
            ):
                return
            # popup終了の外部通知で候補が失効しても、旧接続は変更しない
            if not qt.isValid(view_model) or view_model.is_disposed:
                raise RuntimeError("接続先のEnumViewModelが終了しました")
            self._source_connections.clear()
            self._index_change_pending = False
            self._view_model = view_model
            self._binding = binding
            self._source_connections.connect(
                view_model.value.changed, self._render
            )
            self._source_connections.connect(
                view_model.definition_changed, self._render
            )
            self._source_connections.connect(
                view_model.set_value_command.can_execute_changed,
                self._update_enabled,
            )
            self._source_connections.connect(
                view_model.disposed, self._disable_binding
            )
            self._source_connections.connect(
                view_model.destroyed,
                self._disable_binding,
                queued=True,
                discard_args=True,
            )
            self._render()
        finally:
            del blocker

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
        """選択時に整数値を受け取る入力 `handler` を設定する。

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

    def _index_changed(self, index: int) -> None:
        """値の変化を即時反映し、同じ操作のactivatedとの重複を防ぐ。"""
        self._index_change_pending = True
        cast(_QTimerType, qt.QTimer).singleShot(
            0,
            partial(
                self._clear_index_change, self._source_connections.generation
            ),
        )
        self._request_index(index)

    def _clear_index_change(self, generation: int) -> None:
        """次のイベントでは同じ項目の明示選択も入力として受け付ける。"""
        if generation == self._source_connections.generation:
            self._index_change_pending = False

    def _activate_index(self, index: int) -> None:
        """同じ項目の再選択を入力handlerへ一回だけ伝える。"""
        if self._index_change_pending:
            self._index_change_pending = False
            return
        self._request_index(index)

    def _request_index(self, index: int) -> None:
        """選択した項目の整数値を明示入力として処理する。"""
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
        generation = self._source_connections.generation
        try:
            handler = self._value_request_handler
            handled = handler is not None and handler(item.value)
            if generation != self._source_connections.generation:
                return
            if not handled:
                vm.set_value_command.execute(item.value)
        finally:
            if qt.isValid(self):
                self._render()

    def wheelEvent(self, e: qt.QtGui.QWheelEvent) -> None:
        """設定に応じて、非フォーカス時のホイールを親へ渡す。"""
        if self._wheel_requires_focus and not self.hasFocus():
            e.ignore()
            return
        super().wheelEvent(e)

    @qt.Slot()
    def _disable_binding(self) -> None:
        if qt.isValid(self):
            self.setEnabled(False)
