# coding: utf-8
from PySide6 import QtWidgets

from ....maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
)


class SampleDockableWindow(MayaDockableWindow):
    """Mayaへドッキングできるsample window。"""

    def __init__(self) -> None:
        """ドッキング動作を確認するsample UIを構築する。"""
        # Mayaのdockable mixinを含む基底Widgetを初期化する。
        super().__init__()
        self.setWindowTitle("bakedanuki-util dockable UI sample")

        # sampleの用途と現在の表示形態を説明するlabelを作成する。
        label = QtWidgets.QLabel(
            "This window can be docked into Maya's main window."
        )
        label.setWordWrap(True)

        # workspaceControlを閉じる操作を確認するbuttonを作成する。
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(_controller.close)

        # 作成したWidgetを余白付きの縦方向へ配置する。
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(close_button)


# Maya再起動時にimport可能な復元関数と固定control IDを登録する。
_controller = MayaDockableWindowController(
    SampleDockableWindow,
    control_id="bdUtilSampleDockableWindow",
    restore=DockRestoreSpec(
        module="bd_util._sample.maya.ui.dockable_window",
        function="restore",
    ),
    dock_options=DockOptions(
        area=DockArea.RIGHT,
        floating=False,
        initial_width=320,
        initial_height=420,
        retain=True,
    ),
)


def show() -> SampleDockableWindow:
    """sample windowを表示してinstanceを返す。"""
    # 初回は生成し、2回目以降は同じworkspaceControlを再表示する。
    return _controller.show()


def restore() -> SampleDockableWindow:
    """Mayaが復元したworkspaceControlへsample windowを接続する。"""
    # uiScript実行中のcurrent parentへWidgetを追加する。
    return _controller.restore()


def dispose() -> None:
    """sample windowとworkspaceControlを完全に破棄する。"""
    # 開発中のmodule reload前に残っているMaya UIを削除する。
    _controller.dispose()
