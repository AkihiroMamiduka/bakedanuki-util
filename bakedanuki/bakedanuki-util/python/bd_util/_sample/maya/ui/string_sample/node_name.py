# coding: utf-8
"""既存ノード一つの名前を共有Viewで編集するサンプル。"""

from .....maya.node import Nodes
from .....maya.node.operator.node._core import NodeOperator
from .....maya.ui import MayaNodeNameBinding, MayaWindowController
from .....ui import StringLabel, StringLineEdit, qt

__all__ = ("NodeNameSampleWindow", "show", "dispose")


class NodeNameSampleWindow(qt.QDialog):
    """固定したノード名と入力・同期状態を表示するWindow。"""

    def __init__(
        self, node: NodeOperator, parent: qt.QWidget | None = None
    ) -> None:
        """同じ名前Bindingを二つの入力欄とラベルへ接続する。"""
        super().__init__(parent)
        self.setObjectName("bdUtilNodeNameSampleWindow")
        self.setWindowTitle("bakedanuki-util Node Name")
        try:
            self.binding = MayaNodeNameBinding(node, parent=self)
        except Exception:
            self.deleteLater()
            raise

        # 下書きと確定値を並べ、外部リネーム時の競合を確認できるようにする
        self.line_edit = StringLineEdit(self.binding, self)
        self.linked_line_edit = StringLineEdit(self.binding, self)
        self.label = StringLabel(self.binding, self)
        self.status_label = qt.QLabel(self)
        self.conflict_label = qt.QLabel(self)
        self.error_label = qt.QLabel(self)
        for label in (
            self.status_label,
            self.conflict_label,
            self.error_label,
        ):
            label.setTextFormat(qt.Qt.TextFormat.PlainText)
            label.setWordWrap(True)
        self.refresh_button = qt.QPushButton("Refresh", self)
        self.refresh_button.setAutoDefault(False)
        for line_edit in (self.line_edit, self.linked_line_edit):
            line_edit.conflict_changed.connect(self._render_conflict)
            line_edit.edit_failed.connect(self._show_error)
            line_edit.textEdited.connect(self._clear_error)
        view_model = self.binding.view_model
        view_model.set_value_command.can_execute_changed.connect(
            self._render_status
        )
        view_model.store_refreshed.connect(self._render_status)
        self.binding.changed.connect(self._clear_error)
        self.refresh_button.clicked.connect(self._refresh)

        layout = qt.QFormLayout(self)
        layout.addRow("ノード名", self.line_edit)
        layout.addRow("共有View", self.linked_line_edit)
        layout.addRow("確定名", self.label)
        layout.addRow("状態", self.status_label)
        layout.addRow("競合", self.conflict_label)
        layout.addRow("エラー", self.error_label)
        layout.addRow(self.refresh_button)
        self._render_status()
        self._render_conflict()

    def _render_status(self, *_args: object) -> None:
        """現在の実体と名前の編集可否を表示する。"""
        store = self.binding.store
        if not store.is_available:
            text = "対象ノードは利用できません。接続を終了しました。"
        elif not store.is_writable:
            text = "読み取り専用です。解除後は Refresh で確認できます。"
        else:
            text = "編集可能: Enter で確定 / Esc で未確定入力を破棄"
        self.status_label.setText(text)

    def _render_conflict(self, *_args: object) -> None:
        """外部変更と未確定入力の競合を案内する。"""
        conflicted = (
            self.line_edit.hasConflict() or self.linked_line_edit.hasConflict()
        )
        self.conflict_label.setText(
            "外部変更あり: Enter で上書き / Esc で破棄"
            if conflicted
            else "なし"
        )

    def _show_error(self, message: str) -> None:
        """入力失敗をモーダル表示せず、確定名と並べて知らせる。"""
        self.error_label.setText(message)
        self._render_status()

    def _clear_error(self, *_args: object) -> None:
        """次の入力または正本の変更時に前回のエラーを消す。"""
        self.error_label.clear()

    @qt.Slot()
    def _refresh(self) -> None:
        """名前と編集可否を読み直し、失敗時はその内容を表示する。"""
        self._clear_error()
        try:
            self.binding.refresh()
        except Exception as error:
            self._show_error(str(error))
        self._render_status()

    def closeEvent(self, arg__1: qt.QtGui.QCloseEvent) -> None:
        """Window終了時に名前の監視を即座に解除する。"""
        self.binding.dispose()
        super().closeEvent(arg__1)


_controller: MayaWindowController[NodeNameSampleWindow] | None = None


def show(node_name: str) -> NodeNameSampleWindow:
    """指定した既存ノードを固定して表示し、sceneには書き込まない。

    Args:
        node_name: 既存ノード名。同名DAGの場合は一意なパスを指定する。

    Returns:
        選択変更に追従しない名前編集Window。
    """
    global _controller
    nodes = Nodes()
    node = nodes.existing(node_name)
    dispose()
    controller = MayaWindowController(
        lambda parent: NodeNameSampleWindow(node, parent)
    )
    _controller = controller
    try:
        return controller.show()
    except Exception:
        dispose()
        raise


def dispose() -> None:
    """Windowとcallbackを終了し、ノードと名前はそのまま残す。"""
    global _controller
    if _controller is not None:
        window = _controller.window
        if window is not None and qt.isValid(window):
            window.binding.dispose()
        _controller.dispose()
        _controller = None
