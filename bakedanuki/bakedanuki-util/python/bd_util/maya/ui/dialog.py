# coding: utf-8
"""Maya標準のフォルダー選択へ、Qtの初期サイズと起点配置を適用する。"""

from __future__ import annotations

from collections.abc import Callable
from contextlib import ExitStack
from pathlib import Path
from typing import cast

from maya import cmds

from ...ui import place_dialog_near, qt

__all__ = ["get_existing_directory_near"]


class _MayaDirectoryPlacement(qt.QObject):
    """今回のコマンドが開く画面だけを捕捉し、監視期間を所有する。"""

    def __init__(
        self,
        parent: qt.QWidget | None,
        application: qt.QApplication,
        caption: str,
        anchor: qt.QPoint,
        initial_size: qt.QSize,
    ) -> None:
        """既存画面を除外し、Mayaが新しく表示する同じタイトルの画面を待つ。"""
        super().__init__(parent)
        self.application = application
        self.caption = caption
        self.anchor = qt.QPoint(anchor)
        self.initial_size = qt.QSize(initial_size)
        self.dialog: qt.QFileDialog | None = None
        self.error: Exception | None = None
        self._existing = tuple(qt.QApplication.topLevelWidgets())
        self._placements = ExitStack()
        application.installEventFilter(self)

    def eventFilter(self, watched: qt.QObject, event: qt.QEvent) -> bool:
        """表示通知の実体をQt公開型で取得し、一度だけ配置を適用する。"""
        if (
            self.dialog is None
            and event.type() == qt.QEvent.Type.Show
            and isinstance(watched, qt.QFileDialog)
            and watched not in self._existing
            and watched.windowTitle() == self.caption
        ):
            self.dialog = watched
            try:
                watched.resize(self.initial_size)
                self._placements.enter_context(
                    place_dialog_near(watched, self.anchor)
                )
            except Exception as error:
                # Qtの通知境界で例外を失わず、コマンド終了後に呼出し元へ返す
                self.error = error
                watched.reject()
        return super().eventFilter(watched, event)

    def dispose(self) -> None:
        """コマンドの成功・取消・例外にかかわらず、全監視を解除する。"""
        self.application.removeEventFilter(self)
        try:
            self._placements.close()
        finally:
            self.deleteLater()


def get_existing_directory_near(
    parent: qt.QWidget | None,
    caption: str,
    directory: str,
    anchor: qt.QPoint,
    *,
    initial_size: qt.QSize,
) -> str:
    """編集可能なアドレス欄を持つMaya標準画面で、既存フォルダーを選択する。

    `fileDialog2(dialogStyle=2, fileMode=3)`を使用します。表示されたQt画面を
    今回の呼出し中だけ捕捉し、`initial_size`と`anchor`を適用します。
    大きすぎる画面はモニター内へ収めます。表示後の手動リサイズや移動、
    アドレス欄による移動・コピーはMaya標準の動作を使用します。

    Args:
        parent: 一時的な監視を所有するWidget。`None`なら親なしです。
        caption: 今回開く画面の空でないタイトル。
        directory: 初期フォルダー。
        anchor: 操作開始時に記録したグローバル座標。
        initial_size: 初期クライアント寸法。Qtの論理ピクセルで幅・高さを指定します。

    Returns:
        選択した既存フォルダー。取消時は空文字です。ファイルは作成しません。

    Raises:
        ValueError: タイトルが空、または寸法が正でない場合。
        RuntimeError: Qt applicationがないか、Maya画面の実行・配置に失敗した場合。
    """
    if not caption or initial_size.width() <= 0 or initial_size.height() <= 0:
        raise ValueError("タイトルと正の初期幅・高さを指定してください")
    application = qt.QApplication.instance()
    if not isinstance(application, qt.QApplication):
        raise RuntimeError("MayaのQt applicationが必要です")

    placement = _MayaDirectoryPlacement(
        parent, application, caption, anchor, initial_size
    )
    choose = cast(Callable[..., list[str] | None], cmds.fileDialog2)
    try:
        # Mayaの内部Widget名には依存せず、表示された公開Qt型へ初期配置を適用する
        selected = choose(
            caption=caption,
            startingDirectory=str(Path(directory).expanduser()),
            dialogStyle=2,
            fileMode=3,
            okCaption="選択",
            cancelCaption="キャンセル",
        )
        if placement.error is not None:
            raise RuntimeError("Mayaのフォルダー選択を配置できません") from (
                placement.error
            )
        if placement.dialog is None:
            raise RuntimeError("Mayaのフォルダー選択画面を取得できません")
        return selected[0] if selected and Path(selected[0]).is_dir() else ""
    finally:
        placement.dispose()
