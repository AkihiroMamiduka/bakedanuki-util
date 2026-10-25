# coding: utf-8
"""指定位置を基準に、Qtのモーダル画面を画面内へ配置する。"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import cast

from . import qt

__all__ = [
    "exec_dialog_near",
    "warning_near",
    "get_open_file_names_near",
    "get_existing_directory_near",
    "get_save_file_name_near",
]


def _available_geometry(dialog: qt.QDialog, anchor: qt.QPoint) -> qt.QRect:
    """起点の画面を優先し、親画面・主画面の利用可能領域へ補完する。"""
    screen = cast(
        qt.QtGui.QScreen | None, qt.QtGui.QGuiApplication.screenAt(anchor)
    )
    if screen is None:
        screen = cast(qt.QtGui.QScreen | None, dialog.screen())
    if screen is None:
        screen = cast(
            qt.QtGui.QScreen | None,
            qt.QtGui.QGuiApplication.primaryScreen(),
        )
    return screen.availableGeometry() if screen is not None else qt.QRect()


class _DialogPlacement(qt.QObject):
    """表示直後に確定する外枠も含めて、一度だけ配置を補正する。"""

    def __init__(self, dialog: qt.QDialog, anchor: qt.QPoint) -> None:
        """画面と起点を保持し、表示通知と所有タイマーを接続する。"""
        super().__init__(dialog)
        self.dialog = dialog
        self.anchor = qt.QPoint(anchor)
        self._minimum = dialog.minimumSize()
        self._layout = cast(
            Callable[[], qt.QtWidgets.QLayout | None],
            getattr(dialog, "layout"),
        )()
        self._constraint = (
            self._layout.sizeConstraint() if self._layout is not None else None
        )
        self._timer = qt.QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._place)
        dialog.installEventFilter(self)

    def prepare(self) -> None:
        """自然な寸法を確定し、表示前にも起点付近へ配置する。"""
        self.dialog.ensurePolished()
        if not self.dialog.testAttribute(qt.Qt.WidgetAttribute.WA_Resized):
            self.dialog.adjustSize()
        self._place()

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """表示時の外枠確定後に同じ起点で補正し、他の通知は通常処理へ渡す。"""
        if watched is self.dialog and event.type() == qt.QEvent.Type.Show:
            self.correct_after_show()
        return super().eventFilter(watched, event)

    def correct_after_show(self) -> None:
        """表示通知中と次のイベントループで、確定した外枠へ補正する。"""
        self._place()
        self._timer.start(0)

    def _place(self) -> None:
        """画面より大きい場合だけ縮小し、起点を中心に外枠を収める。"""
        dialog = self.dialog
        available = _available_geometry(dialog, self.anchor)
        if available.isEmpty():
            return
        frame = dialog.frameGeometry().size()
        maximum = qt.QSize(
            max(1, available.width() - max(0, frame.width() - dialog.width())),
            max(
                1,
                available.height() - max(0, frame.height() - dialog.height()),
            ),
        )
        # 小さい画面では内容の最小寸法よりも作業領域を優先する
        if self._layout is not None:
            minimum = self._layout.totalMinimumSize()
            if (
                minimum.width() > maximum.width()
                or minimum.height() > maximum.height()
            ):
                self._layout.setSizeConstraint(
                    qt.QtWidgets.QLayout.SizeConstraint.SetNoConstraint
                )
        dialog.setMinimumSize(self._minimum.boundedTo(maximum))
        dialog.resize(dialog.size().boundedTo(maximum))
        frame = dialog.frameGeometry().size()
        dialog.move(
            max(
                available.left(),
                min(
                    self.anchor.x() - frame.width() // 2,
                    available.right() - frame.width() + 1,
                ),
            ),
            max(
                available.top(),
                min(
                    self.anchor.y() - frame.height() // 2,
                    available.bottom() - frame.height() + 1,
                ),
            ),
        )

    def dispose(self) -> None:
        """タイマーと監視を解除し、呼出し元の最小寸法とlayout制約を戻す。"""
        self._timer.stop()
        if qt.isValid(self.dialog):
            self.dialog.removeEventFilter(self)
            if self._layout is not None and self._constraint is not None:
                self._layout.setSizeConstraint(self._constraint)
            self.dialog.setMinimumSize(self._minimum)
        self.deleteLater()


class _ChildMessageBoxPlacement(qt.QObject):
    """実行中のダイアログ配下に現れる標準確認だけを同じ起点へ配置する。"""

    def __init__(self, dialog: qt.QDialog, anchor: qt.QPoint) -> None:
        """対象の親階層と起点を保持し、実行中だけ表示通知を監視する。"""
        super().__init__(dialog)
        self._dialog = dialog
        self._anchor = qt.QPoint(anchor)
        self._placements: list[_DialogPlacement] = []
        self._application = qt.QApplication.instance()
        if self._application is not None:
            self._application.installEventFilter(self)

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """親ダイアログに属する確認だけを捕捉し、内容と標準動作は維持する。"""
        if (
            event.type() == qt.QEvent.Type.Show
            and isinstance(watched, qt.QMessageBox)
            and watched is not self._dialog
            and self._owns_message(watched)
            and not any(
                qt.isValid(placement) and placement.dialog is watched
                for placement in self._placements
            )
        ):
            placement = _DialogPlacement(watched, self._anchor)
            self._placements.append(placement)
            placement.prepare()
            placement.correct_after_show()
        return super().eventFilter(watched, event)

    def _owns_message(self, message: qt.QMessageBox) -> bool:
        """Window境界で途切れる祖先判定を避け、実際の親Widget階層を辿る。"""
        parent = cast(qt.QWidget | None, message.parentWidget())
        while parent is not None:
            if parent is self._dialog:
                return True
            parent = cast(qt.QWidget | None, parent.parentWidget())
        return False

    def dispose(self) -> None:
        """共有イベント監視と、存命の標準確認に付けた補正を解除する。"""
        if self._application is not None:
            self._application.removeEventFilter(self)
        for placement in self._placements:
            if qt.isValid(placement):
                placement.dispose()
        self._placements.clear()
        self.deleteLater()


def exec_dialog_near(dialog: qt.QDialog, anchor: qt.QPoint) -> int:
    """`anchor`を中心に、外枠まで画面内へ収めてモーダル実行する。

    通常のQtダイアログ用です。ネイティブのファイルダイアログは対象外です。
    実行中に`dialog`配下へ表示されるQt標準の確認も同じ起点へ配置します。
    表示直後に一度補正し、その後の利用者による移動は追跡しません。

    Args:
        dialog: 呼出し元が所有する未表示のダイアログ。
        anchor: 操作開始時に記録したグローバル座標。

    Returns:
        `QDialog.exec()`の結果。ダイアログ自体は削除しません。
    """
    placement = _DialogPlacement(dialog, anchor)
    messages = _ChildMessageBoxPlacement(dialog, anchor)
    try:
        placement.prepare()
        return int(dialog.exec())
    finally:
        if qt.isValid(messages):
            messages.dispose()
        if qt.isValid(placement):
            placement.dispose()


def warning_near(
    parent: qt.QWidget | None,
    title: str,
    text: str,
    anchor: qt.QPoint,
    buttons: qt.QMessageBox.StandardButton = qt.QMessageBox.StandardButton.Ok,
    default_button: qt.QMessageBox.StandardButton = (
        qt.QMessageBox.StandardButton.NoButton
    ),
) -> qt.QMessageBox.StandardButton:
    """警告を操作位置へ表示し、選択したQt標準ボタンを返す。

    Args:
        parent: 所有Widget。`None`の場合は親を指定しません。
        title: ダイアログのタイトル。
        text: 警告の本文。
        anchor: 操作開始時に記録したグローバル座標。
        buttons: 表示する標準ボタンの組合せ。既定は`Ok`です。
        default_button: 初期選択。`NoButton`ではQtの標準選択を使用します。

    Returns:
        選択した標準ボタン。閉じる操作の扱いはQtの標準動作に従います。
    """
    dialog = qt.QMessageBox(parent)
    dialog.setWindowTitle(title)
    dialog.setIcon(qt.QMessageBox.Icon.Warning)
    dialog.setText(text)
    dialog.setStandardButtons(buttons)
    if default_button != qt.QMessageBox.StandardButton.NoButton:
        dialog.setDefaultButton(default_button)
    try:
        return qt.QMessageBox.StandardButton(exec_dialog_near(dialog, anchor))
    finally:
        dialog.deleteLater()


def get_open_file_names_near(
    parent: qt.QWidget | None,
    caption: str,
    directory: str,
    name_filter: str,
    anchor: qt.QPoint,
) -> tuple[list[str], str]:
    """Qt版の複数ファイル選択を操作位置へ表示する。

    Args:
        parent: 所有Widget。`None`の場合は親を指定しません。
        caption: ダイアログのタイトル。
        directory: 初期フォルダー、または初期ファイル名を含むパス。
        name_filter: Qt形式のファイル名filter。
        anchor: 操作開始時に記録したグローバル座標。

    Returns:
        選択したファイル名の一覧とfilter。取消時は空の一覧と空文字です。
    """
    dialog = qt.QFileDialog(parent)
    dialog.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
    dialog.setWindowTitle(caption)
    dialog.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
    dialog.setFileMode(qt.QFileDialog.FileMode.ExistingFiles)
    dialog.setNameFilter(name_filter)
    initial = Path(directory).expanduser()
    if initial.is_dir():
        dialog.setDirectory(str(initial))
    else:
        dialog.setDirectory(str(initial.parent))
        dialog.selectFile(initial.name)
    try:
        if exec_dialog_near(dialog, anchor) != qt.QDialog.DialogCode.Accepted:
            return [], ""
        return dialog.selectedFiles(), dialog.selectedNameFilter()
    finally:
        dialog.deleteLater()


def get_existing_directory_near(
    parent: qt.QWidget | None,
    caption: str,
    directory: str,
    anchor: qt.QPoint,
) -> str:
    """Qt版の既存フォルダー選択を操作位置へ表示する。

    フォルダー間の移動と確定にはQt標準の動作を使用します。
    この関数は選択だけを行い、フォルダーやファイルを作成しません。

    Args:
        parent: 所有Widget。`None`の場合は親を指定しません。
        caption: ダイアログのタイトル。
        directory: 初期フォルダー。
        anchor: 操作開始時に記録したグローバル座標。

    Returns:
        選択した既存フォルダーのパス。取消時は空文字です。
    """
    dialog = qt.QFileDialog(parent)
    # Qt版で配置と既存フォルダーのみの選択を制御する
    dialog.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
    dialog.setWindowTitle(caption)
    dialog.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptOpen)
    dialog.setFileMode(qt.QFileDialog.FileMode.Directory)
    dialog.setOption(qt.QFileDialog.Option.ShowDirsOnly, True)
    dialog.setDirectory(str(Path(directory).expanduser()))
    try:
        if exec_dialog_near(dialog, anchor) != qt.QDialog.DialogCode.Accepted:
            return ""
        paths = dialog.selectedFiles()
        return paths[0] if paths and Path(paths[0]).is_dir() else ""
    finally:
        dialog.deleteLater()


def get_save_file_name_near(
    parent: qt.QWidget | None,
    caption: str,
    directory: str,
    name_filter: str,
    anchor: qt.QPoint,
    default_suffix: str = "",
) -> tuple[str, str]:
    """Qt版の保存先選択を起点付近へ表示し、ファイル名と選択filterを返す。

    既存ファイルの上書き確認はQtの標準動作を使用します。
    この関数は保存先を選択するだけで、ファイルへ書き込みません。

    Args:
        parent: 所有Widget。`None`の場合は親を指定しません。
        caption: ダイアログのタイトル。
        directory: 初期フォルダー、または初期ファイル名を含むパス。
        name_filter: Qt形式のファイル名filter。
        anchor: 操作開始時に記録したグローバル座標。
        default_suffix: 拡張子省略時に補う文字列。既定の空文字では補いません。

    Returns:
        選択したファイル名とfilter。取消時は二つとも空文字です。
    """
    dialog = qt.QFileDialog(parent)
    # 他の設定より先にQt版を選び、配置可能なWidgetを使用する
    dialog.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
    dialog.setWindowTitle(caption)
    dialog.setAcceptMode(qt.QFileDialog.AcceptMode.AcceptSave)
    dialog.setFileMode(qt.QFileDialog.FileMode.AnyFile)
    dialog.setNameFilter(name_filter)
    dialog.setDefaultSuffix(default_suffix)
    initial = Path(directory).expanduser()
    if initial.is_dir():
        dialog.setDirectory(str(initial))
    else:
        dialog.setDirectory(str(initial.parent))
        dialog.selectFile(initial.name)
    try:
        if exec_dialog_near(dialog, anchor) != qt.QDialog.DialogCode.Accepted:
            return "", ""
        paths = dialog.selectedFiles()
        return (paths[0], dialog.selectedNameFilter()) if paths else ("", "")
    finally:
        dialog.deleteLater()
