# coding: utf-8
from collections.abc import Callable

from .....maya.ui import MayaStringPlugsBinding
from .....ui import StringLabel, StringLineEdit, qt


class StringPlugsSampleWindow(qt.QDialog):
    """複数jointのotherTypeを共有Viewで一括編集するWindow。"""

    def __init__(
        self,
        create_binding: Callable[[qt.QObject], MayaStringPlugsBinding],
        parent: qt.QWidget | None = None,
    ) -> None:
        """既存jointの正本とViewをWindowの寿命へ結び付ける。"""
        super().__init__(parent)
        self.setObjectName("bdUtilStringPlugsSampleWindow")
        self.setWindowTitle("bakedanuki-util string / joint.otherType group")
        try:
            self.binding = create_binding(self)
        except Exception:
            self.deleteLater()
            raise
        self.line_edit = StringLineEdit(self.binding, self)
        self.linked_line_edit = StringLineEdit(self.binding, self)
        self.label = StringLabel(self.binding, self)
        self.state_label = qt.QLabel(self)
        self.conflict_label = qt.QLabel(self)
        self.error_label = qt.QLabel(self)
        self.align_button = qt.QPushButton("代表値へ揃える", self)
        self.clear_button = qt.QPushButton("空文字へ設定", self)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.binding.state_changed.connect(self._render_state)
        self.binding.edit_failed.connect(self.error_label.setText)
        self.binding.view_model.set_value_command.can_execute_changed.connect(
            self._render_state
        )
        self.line_edit.conflict_changed.connect(self._render_conflict)
        self.linked_line_edit.conflict_changed.connect(self._render_conflict)
        self.align_button.clicked.connect(self._align)
        self.clear_button.clicked.connect(self._clear)
        self.refresh_button.clicked.connect(self._refresh)
        layout = qt.QFormLayout(self)
        layout.addRow("代表 otherType", self.line_edit)
        layout.addRow("共有View", self.linked_line_edit)
        layout.addRow("代表確定値", self.label)
        layout.addRow("対象", self.state_label)
        layout.addRow("競合", self.conflict_label)
        layout.addRow(self.align_button)
        layout.addRow(self.clear_button)
        layout.addRow(self.refresh_button)
        layout.addRow("エラー", self.error_label)
        self._render_state()
        self._render_conflict()

    def _render_state(self, *_args: object) -> None:
        """代表以外の混在と除外対象を入力文字列とは別に表示する。"""
        binding = self.binding
        state = "混在" if binding.is_mixed else "一致"
        self.state_label.setText(
            f"{state} / {binding.target_count}件中{binding.writable_count}件を書込み可能"
        )
        excluded = [
            f"{target.name}: {target.reason}"
            for target in binding.target_states
            if not target.is_writable and target.reason is not None
        ]
        self.state_label.setToolTip("\n".join(excluded))
        editable = binding.view_model.set_value_command.can_execute
        self.align_button.setEnabled(editable)
        self.clear_button.setEnabled(editable)

    def _render_conflict(self, *_args: object) -> None:
        """編集中の外部変更と確定方法を表示する。"""
        conflicted = (
            self.line_edit.hasConflict() or self.linked_line_edit.hasConflict()
        )
        self.conflict_label.setText(
            "外部変更あり: Enterで上書き / Escで破棄" if conflicted else "なし"
        )

    @qt.Slot()
    def _align(self) -> None:
        """代表と同じ値を編集可能な後続jointへ適用する。"""
        self.binding.apply_representative_value()

    @qt.Slot()
    def _clear(self) -> None:
        """代表が空文字でも全対象へ明示的に空文字を適用する。"""
        self.binding.set_value("")

    @qt.Slot()
    def _refresh(self) -> None:
        """全jointの現在値と編集可否を読み直す。"""
        self.binding.refresh()
