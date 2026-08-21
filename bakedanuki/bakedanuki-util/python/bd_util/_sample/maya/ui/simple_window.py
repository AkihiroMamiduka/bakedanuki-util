# coding: utf-8
from ....ui import qt
from ....maya.ui import (
    MayaWindowController,
    reset_and_show_ui_layout,
    reset_ui_layout,
)

_SETTINGS_PATH = "bakedanuki_util/sample/simple_window"


class SampleWindow(qt.QDialog):
    """Maya main windowを親に持つsample dialog。"""

    def __init__(self, parent: qt.QWidget | None = None) -> None:
        """親widgetを受け取ってsample UIを構築する。"""
        # dialogの親とwindow固有の表示設定を初期化する。
        super().__init__(parent)
        self.setObjectName("bdUtilSampleWindow")
        self.setWindowTitle("bakedanuki-util UI sample")
        self.setMinimumWidth(320)

        # sampleの説明とwindowを閉じるbuttonを作成する。
        label = qt.QLabel("This window is parented to Maya's main window.")
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(self.close)
        reset_button = qt.QPushButton("Reset layout")
        reset_button.clicked.connect(reset_and_show)

        # 作成したwidgetを縦方向へ配置する。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(close_button)
        layout.addWidget(reset_button)


# module内で1つのwindow instanceを共有する。
_controller = MayaWindowController(
    SampleWindow,
    settings_path=_SETTINGS_PATH,
)


def show() -> SampleWindow:
    """sample windowを表示してinstanceを返す。"""
    # 既存windowがある場合はcontrollerから再表示する。
    return _controller.show()


def reset() -> bool:
    """sample windowと保存済みUI配置を初期状態へ戻す。"""
    # Windowを完全破棄してgeometryとWidget内部状態をまとめて削除する。
    return reset_ui_layout(_controller, _SETTINGS_PATH)


def reset_and_show() -> SampleWindow:
    """UI配置をリセットしてsample windowを初期状態で再表示する。"""
    # ユーザー操作向けにreset完了後の新しいWindowを返す。
    return reset_and_show_ui_layout(_controller, _SETTINGS_PATH)
