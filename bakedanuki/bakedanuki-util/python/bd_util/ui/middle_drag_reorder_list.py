# coding: utf-8
"""左ボタンの標準選択を保ち、中ドラッグだけで一覧の移動を要求する。"""

from dataclasses import dataclass
from typing import cast

from . import qt

__all__ = ["ListReorderRequest", "MiddleDragReorderListWidget"]


@dataclass(frozen=True, slots=True)
class ListReorderRequest:
    """移動前の行番号と、移動前の一覧にある挿入先の行間を保持する。

    Attributes:
        rows: 元の表示順で昇順に並べた移動行。
        before_row: 削除前の一覧で、直後の行番号。末尾は元の行数。
    """

    rows: tuple[int, ...]
    before_row: int


class MiddleDragReorderListWidget(qt.QListWidget):
    """縦一覧の中ドラッグを通知し、項目の変更は利用側へ委ねる。

    `reorder_requested` は有効な移動の解放時に一回だけ
    `ListReorderRequest` を渡す。項目を自動では移動しないため、利用側は
    データを更新して表示と選択を復元する。左ボタンの選択とキー操作は
    `QListWidget` の標準動作を使う。外部とのドラッグ転送は行わない。
    """

    reorder_requested = qt.Signal(object)

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """複数選択の縦一覧と、中ドラッグ中だけ使う監視を準備する。"""
        super().__init__(parent)
        self._press_position: qt.QPoint | None = None
        self._last_position = qt.QPoint()
        self._drag_rows: tuple[int, ...] = ()
        self._dragging = False
        self._before_row: int | None = None
        self._indicator_y: int | None = None
        self._previous_cursor: qt.QCursor | None = None
        self._had_cursor = False
        self._scroll_direction = 0
        self._scroll_timer = qt.QTimer(self)
        self._scroll_timer.setInterval(50)
        self._scroll_timer.timeout.connect(self._auto_scroll)

        # 左ドラッグをQtの範囲選択へ残し、並び順は利用側のモデルで管理する
        self.setSelectionMode(
            qt.QAbstractItemView.SelectionMode.ExtendedSelection
        )
        self.setDragEnabled(False)
        self.setAcceptDrops(False)
        self.setSortingEnabled(False)
        self.setFlow(qt.QListView.Flow.TopToBottom)
        self.setWrapping(False)
        self.setSpacing(0)

        # 行番号や対象集合が変化したら、古い移動要求を確定させない
        model = self.model()
        model.rowsAboutToBeInserted.connect(self.cancel_reorder)
        model.rowsAboutToBeRemoved.connect(self.cancel_reorder)
        model.rowsAboutToBeMoved.connect(self.cancel_reorder)
        model.modelAboutToBeReset.connect(self.cancel_reorder)
        model.layoutAboutToBeChanged.connect(self.cancel_reorder)
        model.dataChanged.connect(self.cancel_reorder)
        self.itemSelectionChanged.connect(self.cancel_reorder)
        self.verticalScrollBar().valueChanged.connect(self._refresh_target)

    def cancel_reorder(self) -> None:
        """保留中の中ドラッグを破棄し、監視・線・カーソルを戻す。"""
        application = qt.QApplication.instance()
        if application is not None:
            application.removeEventFilter(self)
        self._scroll_timer.stop()
        self._scroll_direction = 0
        self._press_position = None
        self._drag_rows = ()
        self._dragging = False
        self._before_row = None
        self._indicator_y = None
        if self._previous_cursor is not None:
            if self._had_cursor:
                self.viewport().setCursor(self._previous_cursor)
            else:
                self.viewport().unsetCursor()
            self._previous_cursor = None
        self.viewport().update()

    def mousePressEvent(self, event: qt.QtGui.QMouseEvent) -> None:
        """中押下だけを移動準備に使い、選択内では複数選択を維持する。"""
        if event.button() != qt.Qt.MouseButton.MiddleButton:
            super().mousePressEvent(event)
            return
        self.cancel_reorder()
        position = event.position().toPoint()
        item = cast(qt.QListWidgetItem | None, self.itemAt(position))
        if item is None or not (
            item.flags() & qt.Qt.ItemFlag.ItemIsEnabled
            and item.flags() & qt.Qt.ItemFlag.ItemIsSelectable
        ):
            event.accept()
            return

        # 選択変更のsignalが監視を解除してから、新しい対象を記録する
        self.setCurrentItem(
            item,
            (
                qt.QItemSelectionModel.SelectionFlag.NoUpdate
                if item.isSelected()
                else qt.QItemSelectionModel.SelectionFlag.ClearAndSelect
            ),
        )
        self.setFocus(qt.Qt.FocusReason.MouseFocusReason)
        self._drag_rows = tuple(
            sorted(self.row(selected) for selected in self.selectedItems())
        )
        self._press_position = position
        self._last_position = position
        application = qt.QApplication.instance()
        if application is not None:
            application.installEventFilter(self)
        event.accept()

    def eventFilter(self, object: qt.QObject, event: qt.QEvent) -> bool:
        """中ドラッグ中の入力だけを追跡し、中断時は要求を破棄する。"""
        if self._press_position is None:
            return super().eventFilter(object, event)
        kind = event.type()
        if isinstance(event, qt.QtGui.QMouseEvent):
            if kind == qt.QEvent.Type.MouseMove:
                if not event.buttons() & qt.Qt.MouseButton.MiddleButton:
                    self.cancel_reorder()
                    return False
                self._move_reorder(event)
                event.accept()
                return True
            if (
                kind == qt.QEvent.Type.MouseButtonRelease
                and event.button() == qt.Qt.MouseButton.MiddleButton
            ):
                self._release_reorder(event)
                event.accept()
                return True
            if kind == qt.QEvent.Type.MouseButtonPress:
                self.cancel_reorder()
        elif isinstance(event, qt.QtGui.QKeyEvent):
            if kind == qt.QEvent.Type.KeyPress:
                self.cancel_reorder()
                if event.key() == qt.Qt.Key.Key_Escape:
                    event.accept()
                    return True
        elif kind == qt.QEvent.Type.ApplicationDeactivate or (
            object in (self, self.viewport(), self.window())
            and kind
            in (
                qt.QEvent.Type.Hide,
                qt.QEvent.Type.WindowDeactivate,
                qt.QEvent.Type.UngrabMouse,
                qt.QEvent.Type.EnabledChange,
            )
        ):
            self.cancel_reorder()
        return super().eventFilter(object, event)

    def _move_reorder(self, event: qt.QtGui.QMouseEvent) -> None:
        """一定距離を超えてから移動表示と行間の追跡を開始する。"""
        pressed = self._press_position
        if pressed is None:
            return
        self._last_position = self.viewport().mapFromGlobal(
            event.globalPosition().toPoint()
        )
        if not self._dragging:
            if (
                self._last_position - pressed
            ).manhattanLength() < qt.QApplication.startDragDistance():
                return
            self._dragging = True
            self._had_cursor = self.viewport().testAttribute(
                qt.Qt.WidgetAttribute.WA_SetCursor
            )
            self._previous_cursor = qt.QCursor(self.viewport().cursor())
        self._refresh_target()

    def _refresh_target(self) -> None:
        """現在位置の行間と端スクロールを更新し、範囲外を無効にする。"""
        if not self._dragging:
            return
        viewport = self.viewport()
        position = self._last_position
        if not viewport.rect().contains(position):
            self._before_row = None
            self._indicator_y = None
            self._scroll_direction = 0
            self._scroll_timer.stop()
            viewport.setCursor(qt.Qt.CursorShape.ForbiddenCursor)
            viewport.update()
            return

        viewport.setCursor(qt.Qt.CursorShape.ClosedHandCursor)
        item = cast(
            qt.QListWidgetItem | None,
            self.itemAt(qt.QPoint(viewport.width() // 2, position.y())),
        )
        if item is not None:
            rect = self.visualItemRect(item)
            after = position.y() > rect.center().y()
            self._before_row = self.row(item) + int(after)
            line_y = rect.bottom() + 1 if after else rect.top()
        else:
            self._before_row = self.count()
            last = self.item(self.count() - 1) if self.count() else None
            line_y = (
                self.visualItemRect(last).bottom() + 1
                if last is not None
                else 0
            )
        self._indicator_y = max(1, min(viewport.height() - 2, line_y))

        # 端に留まる操作でも、現在の行間を更新しながら一段ずつ送る
        margin = min(24, max(1, viewport.height() // 3))
        scroll = self.verticalScrollBar()
        if position.y() < margin and scroll.value() > scroll.minimum():
            self._scroll_direction = -1
        elif (
            position.y() >= viewport.height() - margin
            and scroll.value() < scroll.maximum()
        ):
            self._scroll_direction = 1
        else:
            self._scroll_direction = 0
        if self._scroll_direction:
            if not self._scroll_timer.isActive():
                self._scroll_timer.start()
        else:
            self._scroll_timer.stop()
        viewport.update()

    def _auto_scroll(self) -> None:
        """端の現在方向へ送り、スクロール後の挿入先を再計算する。"""
        if not self._dragging or not self._scroll_direction:
            self._scroll_timer.stop()
            return
        scroll = self.verticalScrollBar()
        scroll.setValue(
            scroll.value()
            + self._scroll_direction * max(1, scroll.singleStep())
        )
        self._refresh_target()

    def _release_reorder(self, event: qt.QtGui.QMouseEvent) -> None:
        """一覧内の有効な移動だけを一回通知し、通知前に監視を解除する。"""
        self._last_position = self.viewport().mapFromGlobal(
            event.globalPosition().toPoint()
        )
        self._refresh_target()
        before = self._before_row
        request: ListReorderRequest | None = None
        if (
            self._dragging
            and before is not None
            and self._changes_order(before)
        ):
            request = ListReorderRequest(self._drag_rows, before)
        self.cancel_reorder()
        if request is not None:
            self.reorder_requested.emit(request)

    def _changes_order(self, before: int) -> bool:
        """元の行番号で挿入を試算し、順序を変えない解放を除外する。"""
        rows = self._drag_rows
        selected = set(rows)
        remaining = [row for row in range(self.count()) if row not in selected]
        target = before - sum(row < before for row in rows)
        reordered = remaining[:target] + list(rows) + remaining[target:]
        return reordered != list(range(self.count()))

    def paintEvent(self, e: qt.QtGui.QPaintEvent) -> None:
        """Qt標準の行描画を保ち、移動先の行間だけに線を重ねる。"""
        super().paintEvent(e)
        line_y = self._indicator_y
        if line_y is None:
            return
        painter = qt.QPainter(self.viewport())
        painter.setPen(
            qt.QtGui.QPen(
                self.palette().color(qt.QPalette.ColorRole.Highlight), 2
            )
        )
        painter.drawLine(2, line_y, self.viewport().width() - 3, line_y)
        painter.end()
