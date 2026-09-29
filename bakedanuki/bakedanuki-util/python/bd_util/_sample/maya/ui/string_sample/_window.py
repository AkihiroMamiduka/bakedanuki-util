# coding: utf-8
from collections.abc import Callable

from .....ui import (
    StringBinding,
    StringLabel,
    StringLineEdit,
    StringValueStore,
    qt,
)


class StringSampleWindow(qt.QDialog):
    """同じ文字列正本を二つの入力欄とラベルへ表示する。"""

    def __init__(
        self,
        create_binding: Callable[
            [qt.QObject], StringBinding[StringValueStore]
        ],
        title: str,
        parent: qt.QWidget | None = None,
    ) -> None:
        """正本とViewをWindowの寿命へ結び付ける。"""
        super().__init__(parent)
        self.setObjectName("bdUtilStringSampleWindow")
        self.setWindowTitle(title)
        try:
            self.binding = create_binding(self)
        except Exception:
            self.deleteLater()
            raise
        self.line_edit = StringLineEdit(self.binding, self)
        self.linked_line_edit = StringLineEdit(self.binding, self)
        self.label = StringLabel(self.binding, self)
        self.conflict_label = qt.QLabel(self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.line_edit.conflict_changed.connect(self._render_conflict)
        self.linked_line_edit.conflict_changed.connect(self._render_conflict)
        self.refresh_button.clicked.connect(self._refresh)
        layout = qt.QFormLayout(self)
        layout.addRow("otherType", self.line_edit)
        layout.addRow("共有View", self.linked_line_edit)
        layout.addRow("確定値", self.label)
        layout.addRow("競合", self.conflict_label)
        layout.addRow(self.refresh_button)
        self._render_conflict()

    def _render_conflict(self, *_args: object) -> None:
        """未確定入力が外部変更と競合しているか表示する。"""
        conflicted = (
            self.line_edit.hasConflict() or self.linked_line_edit.hasConflict()
        )
        self.conflict_label.setText(
            "外部変更あり: Enterで上書き / Escで破棄" if conflicted else "なし"
        )

    @qt.Slot()
    def _refresh(self) -> None:
        """Pythonなどcallback外から変更された値を読み直す。"""
        self.binding.refresh()
