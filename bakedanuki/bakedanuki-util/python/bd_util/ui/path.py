# coding: utf-8
"""フルパスのコピーと、共通規則のExplorer操作をUIへ追加する。"""

from __future__ import annotations

import os
from collections.abc import Callable
from pathlib import Path
from typing import cast

from ..py.path import open_path_in_explorer
from . import qt
from .dialog import warning_near

__all__ = ["add_path_actions", "PathLineEdit"]


def add_path_actions(
    menu: qt.QMenu, path: str | Path, anchor: qt.QPoint
) -> None:
    """既存メニューの末尾に「パス」見出しと、開く・全文コピーを追加する。

    `menu`の所有者がメニューを実行・破棄します。パスが存在しなくてもコピー可能です。
    開く操作では実行直前にも存在確認し、失敗を`anchor`付近へ通知します。

    Args:
        menu: 呼出し元が所有するメニュー。標準項目は削除しません。
        path: メニューを開いた時点の対象。絶対パスを通常テキストとしてコピーします。
        anchor: 右クリックしたグローバル座標。
    """
    target = Path(os.path.abspath(Path(path).expanduser()))
    position = qt.QPoint(anchor)
    # Mayaのstyleでもラベルが省略されない、操作不能な見出しを使う
    section = qt.QtWidgets.QWidgetAction(menu)
    section.setText("パス")
    section.setObjectName("pathSection")
    section.setEnabled(False)
    header = qt.QWidget(menu)
    cast(Callable[[qt.QFont], None], getattr(header, "setFont"))(menu.font())
    layout = qt.QHBoxLayout(header)
    layout.setContentsMargins(8, 3, 8, 3)
    layout.setSpacing(6)
    label = qt.QLabel("パス", header)
    palette = label.palette()
    palette.setColor(
        qt.QtGui.QPalette.ColorGroup.Disabled,
        qt.QtGui.QPalette.ColorRole.WindowText,
        menu.palette().color(
            qt.QtGui.QPalette.ColorGroup.Active,
            qt.QtGui.QPalette.ColorRole.Text,
        ),
    )
    label.setPalette(palette)
    layout.addWidget(label)
    line = qt.QtWidgets.QFrame(header)
    line.setFrameShape(qt.QtWidgets.QFrame.Shape.HLine)
    layout.addWidget(line, 1)
    section.setDefaultWidget(header)
    cast(Callable[[qt.QAction], None], getattr(menu, "addAction"))(section)
    add_action = cast(Callable[[str], qt.QAction], getattr(menu, "addAction"))
    open_action = add_action("エクスプローラで開く")
    open_action.setObjectName("openPathInExplorerAction")
    copy_action = add_action("パスをコピーする")
    copy_action.setObjectName("copyFullPathAction")
    open_action.setEnabled(target.is_file() or target.is_dir())
    if not open_action.isEnabled():
        open_action.setToolTip("対象のファイルまたはフォルダーがありません")
        menu.setToolTipsVisible(True)

    def open_target() -> None:
        """メニュー表示後に対象が消えた場合も、起点に失敗を通知する。"""
        try:
            open_path_in_explorer(target)
        except (OSError, ValueError, NotImplementedError) as error:
            warning_near(
                menu.parentWidget(), "パスを開けません", str(error), position
            )

    def copy_target() -> None:
        """選択部分によらず、対象のフルパスだけを通常テキストでコピーする。"""
        qt.QApplication.clipboard().setText(str(target))

    open_action.triggered.connect(open_target)
    copy_action.triggered.connect(copy_target)


class PathLineEdit(qt.QLineEdit):
    """文字選択と標準メニューを保持する、読み取り専用のフルパス欄。"""

    def __init__(
        self, path: str | Path, parent: qt.QWidget | None = None
    ) -> None:
        """フルパスを表示し、ユーザーの編集を禁止してコピーを許可する。"""
        super().__init__(os.path.abspath(Path(path).expanduser()), parent)
        self.setReadOnly(True)
        self.setToolTip(self.text())

    def contextMenuEvent(self, arg__1: qt.QtGui.QContextMenuEvent) -> None:
        """標準のコピー・全選択を残し、同じパス操作を末尾へ加える。"""
        event = arg__1
        menu = self.createStandardContextMenu()
        try:
            add_path_actions(menu, self.text(), event.globalPos())
            execute = cast(
                Callable[[qt.QPoint], qt.QAction | None], getattr(menu, "exec")
            )
            execute(event.globalPos())
        finally:
            menu.deleteLater()
        event.accept()
