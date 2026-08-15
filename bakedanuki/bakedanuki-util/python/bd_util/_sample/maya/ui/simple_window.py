# coding: utf-8
from PySide6 import QtWidgets

from ....maya.ui import MayaWindowController


class SampleWindow(QtWidgets.QDialog):
    """Maya main windowを親に持つsample dialog。"""

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        """親widgetを受け取ってsample UIを構築する。"""
        # dialogの親とwindow固有の表示設定を初期化する。
        super().__init__(parent)
        self.setObjectName("bdUtilSampleWindow")
        self.setWindowTitle("bakedanuki-util UI sample")
        self.setMinimumWidth(320)

        # sampleの説明とwindowを閉じるbuttonを作成する。
        label = QtWidgets.QLabel(
            "This window is parented to Maya's main window."
        )
        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.close)

        # 作成したwidgetを縦方向へ配置する。
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(close_button)


# module内で1つのwindow instanceを共有する。
_controller = MayaWindowController(SampleWindow)


def show() -> SampleWindow:
    """sample windowを表示してinstanceを返す。"""
    # 既存windowがある場合はcontrollerから再表示する。
    return _controller.show()
