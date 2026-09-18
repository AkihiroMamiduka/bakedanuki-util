# coding: utf-8
"""任意参加のボタン操作で、マウス経路と中断処理を共有する。"""

from __future__ import annotations

from . import qt


def _entry_fraction(
    start: qt.QPoint, end: qt.QPoint, rect: qt.QtCore.QRect
) -> float | None:
    """線分が矩形へ入る位置を返し、速い移動でも途中のボタンを拾う。"""
    first, last = 0.0, 1.0
    for origin, delta, low, high in (
        (start.x(), end.x() - start.x(), rect.left(), rect.right()),
        (start.y(), end.y() - start.y(), rect.top(), rect.bottom()),
    ):
        if delta == 0:
            if not low <= origin <= high:
                return None
            continue
        near, far = sorted(((low - origin) / delta, (high - origin) / delta))
        first, last = max(first, near), min(last, far)
        if first > last:
            return None
    return first


class ButtonSweep(qt.QObject):
    """通常クリックを保ち、左ドラッグ中だけ派生先の操作を適用する。"""

    started = qt.Signal()
    finished = qt.Signal()

    def __init__(self, scope: qt.QWidget) -> None:
        """存続する操作領域を所有者にし、登録されたボタンだけを監視する。"""
        super().__init__(scope)
        self._scope = scope
        self._buttons: list[qt.QtWidgets.QAbstractButton] = []
        self._origin: qt.QtWidgets.QAbstractButton | None = None
        self._cancelled_origin: qt.QtWidgets.QAbstractButton | None = None
        self._position = qt.QPoint()
        self._dragging = False
        self._disposed = False
        scope.destroyed.connect(self.dispose)

    @property
    def is_active(self) -> bool:
        """通常の押下待ちを除き、なぞり選択中か返す。"""
        return self._dragging

    def _add_button(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """表示範囲の子ボタンへ任意参加のドラッグ操作を追加する。"""
        if self._disposed:
            raise RuntimeError("終了済みのなぞり操作です")
        if not self._scope.isAncestorOf(button):
            raise ValueError("表示範囲内のボタンを指定してください")
        if button not in self._buttons:
            self._buttons.append(button)
            button.installEventFilter(self)

    def clear(self) -> None:
        """行を差し替える前に操作を終了し、ボタンの登録を解除する。"""
        self.finish()
        for button in self._buttons:
            if qt.isValid(button):
                button.removeEventFilter(self)
        self._buttons.clear()

    def finish(self) -> None:
        """終了・中断時は現在の選択を保持し、押下状態と監視を解除する。"""
        self._reset(clear_down=True)

    def _reset(self, *, clear_down: bool) -> None:
        """状態を先に解放し、終了通知からの再入を無害にする。"""
        origin, self._origin = self._origin, None
        dragging, self._dragging = self._dragging, False
        application = qt.QApplication.instance()
        if application is not None and qt.isValid(self):
            application.removeEventFilter(self)
        if clear_down and origin is not None and qt.isValid(origin):
            origin.setDown(False)
            self._cancelled_origin = origin
        if dragging and qt.isValid(self):
            self.finished.emit()

    def dispose(self) -> None:
        """所有者の終了時にアプリケーション監視も確実に解除する。"""
        self._disposed = True
        self.clear()

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """押下開始だけを個別監視し、操作中の移動と中断を追跡する。"""
        if self._disposed:
            return False
        kind = event.type()
        if isinstance(event, qt.QtGui.QMouseEvent):
            if kind == qt.QEvent.Type.MouseButtonPress:
                self.finish()
                self._cancelled_origin = None
                if (
                    isinstance(watched, qt.QtWidgets.QAbstractButton)
                    and watched in self._buttons
                    and watched.isEnabled()
                    and event.button() == qt.Qt.MouseButton.LeftButton
                    and watched.hitButton(event.position().toPoint())
                ):
                    self._origin = watched
                    self._position = event.globalPosition().toPoint()
                    self._prepare(watched)
                    application = qt.QApplication.instance()
                    if application is not None:
                        application.installEventFilter(self)
                return False
            if watched is self._cancelled_origin and kind in (
                qt.QEvent.Type.MouseMove,
                qt.QEvent.Type.MouseButtonRelease,
            ):
                if kind == qt.QEvent.Type.MouseButtonRelease:
                    self._cancelled_origin = None
                return True
            if self._origin is not None:
                if kind == qt.QEvent.Type.MouseMove:
                    return self._move(event)
                if (
                    kind == qt.QEvent.Type.MouseButtonRelease
                    and event.button() == qt.Qt.MouseButton.LeftButton
                ):
                    dragging = self._dragging
                    if dragging:
                        self._visit(event.globalPosition().toPoint())
                    # 単発クリックのreleaseは標準Widgetへ渡す
                    self._reset(clear_down=dragging)
                    return dragging
        if self._origin is None:
            return False
        if kind == qt.QEvent.Type.KeyPress:
            self.finish()
            return (
                isinstance(event, qt.QtGui.QKeyEvent)
                and event.key() == qt.Qt.Key.Key_Escape
            )
        if kind == qt.QEvent.Type.Wheel and self._dragging:
            return True
        if kind == qt.QEvent.Type.ApplicationDeactivate:
            self.finish()
        elif isinstance(watched, qt.QWidget) and (
            watched is self._origin
            or watched is self._scope
            or watched.isAncestorOf(self._scope)
            or watched.isAncestorOf(self._origin)
        ):
            if (
                kind
                in (
                    qt.QEvent.Type.Hide,
                    qt.QEvent.Type.Close,
                    qt.QEvent.Type.WindowDeactivate,
                    qt.QEvent.Type.UngrabMouse,
                    qt.QEvent.Type.DeferredDelete,
                )
                or (
                    kind == qt.QEvent.Type.EnabledChange
                    and not watched.isEnabled()
                )
                or (
                    kind == qt.QEvent.Type.FocusOut and watched is self._origin
                )
            ):
                self.finish()
        return False

    def _move(self, event: qt.QtGui.QMouseEvent) -> bool:
        """小さな手ぶれでは標準クリックを維持し、移動開始後だけ選択する。"""
        if not event.buttons() & qt.Qt.MouseButton.LeftButton:
            self.finish()
            return False
        position = event.globalPosition().toPoint()
        if not self._dragging:
            if (
                position - self._position
            ).manhattanLength() < qt.QApplication.startDragDistance():
                return False
            self._dragging = True
            if self._origin is not None:
                self._origin.setDown(False)
            self.started.emit()
        if self._dragging:
            self._visit(position)
        return True

    def _visit(self, position: qt.QPoint) -> None:
        """表示範囲内で経路に触れた有効なボタンだけを、通過順に選択する。"""
        # host側で差し替えられるviewportのwrapperは保持しない
        viewport = (
            self._scope.viewport()
            if isinstance(self._scope, qt.QtWidgets.QAbstractScrollArea)
            else self._scope
        )
        clip = viewport.rect().translated(viewport.mapToGlobal(qt.QPoint()))
        candidates: list[tuple[float, qt.QtWidgets.QAbstractButton]] = []
        for button in self._buttons:
            if not qt.isValid(button) or not button.isVisible():
                continue
            if not button.isEnabled():
                continue
            rect = self._click_rect(button)
            rect = rect.translated(button.mapToGlobal(qt.QPoint()))
            rect = rect.intersected(clip)
            if rect.isEmpty():
                continue
            fraction = _entry_fraction(self._position, position, rect)
            if fraction is not None:
                candidates.append((fraction, button))
        self._position = position
        for _fraction, button in sorted(candidates, key=lambda item: item[0]):
            if not self._dragging:
                break
            if qt.isValid(button) and button.isEnabled():
                self._apply(button)

    def _prepare(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """押下時に派生先の操作状態を準備し、既定では何も変更しない。"""

    def _click_rect(
        self, button: qt.QtWidgets.QAbstractButton
    ) -> qt.QtCore.QRect:
        """派生先のボタン種別に対応したクリック領域を返す。"""
        raise NotImplementedError

    def _apply(self, button: qt.QtWidgets.QAbstractButton) -> None:
        """経路上のボタンへ派生先の状態変更を適用する。"""
        raise NotImplementedError
