# coding: utf-8
"""操作元の入力方法から、一時画面を開く起点を求める。"""

from __future__ import annotations

from typing import cast

from . import qt

__all__ = ["DialogAnchorTracker"]


class DialogAnchorTracker(qt.QObject):
    """所有Widget内の入力を追跡し、マウスまたはキーボードの起点を返す。

    マウス操作では呼出し時のカーソル位置、キーボード操作では操作元Widgetの
    中心を使用します。連続するダイアログへ同じ起点を渡す場合は、呼出し元で
    `position()`の戻り値を保持してください。
    """

    def __init__(self, source: qt.QWidget) -> None:
        """`source`を所有者にし、その子や所有popupの入力を監視する。"""
        super().__init__(source)
        application = qt.QApplication.instance()
        if not isinstance(application, qt.QApplication):
            raise RuntimeError("QApplicationを初期化してください")
        self._source = source
        self._application = application
        self._keyboard = False
        self._key_source: qt.QWidget | None = None
        self._key_event: qt.QEvent | None = None
        self._disposed = False
        application.installEventFilter(self)
        source.destroyed.connect(self.dispose)

    def position(self, source: qt.QWidget | None = None) -> qt.QPoint:
        """現在の入力方法に応じたグローバル座標を返す。

        Args:
            source: キーボード操作時、focusと最後の入力元が無効な場合に使う
                Widget。`None`の場合は所有Widgetを使用します。

        Returns:
            マウス操作では現在のカーソル位置のコピー。キーボード操作では
            所有範囲のfocus、最後の入力元、`source`、所有Widgetの順に
            有効なWidgetの中心を返します。終了後はカーソル位置を返します。
        """
        if not self._disposed and self._keyboard:
            focus = qt.QApplication.focusWidget()
            if self._belongs_to_source(focus):
                return self._center(focus)
            if self._belongs_to_source(self._key_source):
                return self._center(self._key_source)
            if source is not None and qt.isValid(source):
                return self._center(source)
            if qt.isValid(self._source):
                return self._center(self._source)
        return qt.QPoint(qt.QCursor.pos())

    def dispose(self) -> None:
        """入力監視を解除し、所有Widgetの破棄時や繰返し呼出しも安全に扱う。"""
        if self._disposed:
            return
        self._disposed = True
        self._key_source = None
        self._key_event = None
        if qt.isValid(self._application) and qt.isValid(self):
            self._application.removeEventFilter(self)

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """所有範囲の入力方法だけを記録し、eventを通常どおり処理する。"""
        if self._disposed:
            return False
        kind = event.type()
        if kind not in (
            qt.QEvent.Type.KeyPress,
            qt.QEvent.Type.MouseButtonPress,
            qt.QEvent.Type.MouseButtonRelease,
            qt.QEvent.Type.MouseButtonDblClick,
        ):
            return False
        if not isinstance(watched, qt.QWidget) or not self._belongs_to_source(
            watched
        ):
            return False

        # 未処理キーが親へ伝播しても、最初の受信Widgetを保持する
        if kind == qt.QEvent.Type.KeyPress and event is self._key_event:
            return False

        # popupも所有階層で識別し、他ツールの操作では入力方法を変えない
        self._keyboard = kind == qt.QEvent.Type.KeyPress
        self._key_source = watched if self._keyboard else None
        self._key_event = event if self._keyboard else None
        return False

    def _belongs_to_source(self, widget: qt.QWidget | None) -> bool:
        """破棄済みwrapperを避け、popupを含むQObject所有階層を確認する。"""
        if widget is None or not qt.isValid(self._source):
            return False
        current: qt.QObject | None = widget
        while current is not None and qt.isValid(current):
            if current is self._source:
                return True
            current = cast(qt.QObject | None, current.parent())
        return False

    @staticmethod
    def _center(widget: qt.QWidget | None) -> qt.QPoint:
        """有効性を確認済みのWidgetの中心をグローバル座標へ変換する。"""
        if widget is None:
            raise ValueError("起点のWidgetを指定してください")
        return widget.mapToGlobal(widget.rect().center())
