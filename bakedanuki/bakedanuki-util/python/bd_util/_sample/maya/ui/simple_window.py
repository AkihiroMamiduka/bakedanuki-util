# coding: utf-8
from ....ui import qt
from ....maya.ui import (
    MayaUiStateTracker,
    MayaWindowController,
    create_ui_state_manager,
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
        self.resize(520, 320)

        # 通常Windowで保存されるWidget内部状態を操作できるようにする。
        label = qt.QLabel("Splitter sizes and the selected tab are saved.")
        self.item_list = qt.QListWidget()
        self.item_list.addItems(["root", "body_ctrl", "settings"])
        self.main_tabs = qt.QTabWidget()
        self.main_tabs.addTab(qt.QTextEdit("Settings page"), "Settings")
        self.main_tabs.addTab(qt.QTextEdit("Log page"), "Log")
        self.main_splitter = qt.QSplitter()
        self.main_splitter.addWidget(self.item_list)
        self.main_splitter.addWidget(self.main_tabs)
        self.main_splitter.setSizes([180, 320])

        # lifecycle操作を確認するbuttonを作成する。
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(self.close)
        reset_button = qt.QPushButton("Reset layout")
        reset_button.clicked.connect(reset_and_show)

        # 作成したwidgetを縦方向へ配置する。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.main_splitter)
        layout.addWidget(close_button)
        layout.addWidget(reset_button)

        # tool単位のui.iniへ保存するWidgetを固定keyで明示登録する。
        self.ui_state = create_ui_state_manager(_SETTINGS_PATH)
        self.ui_state.register_splitter("main_splitter", self.main_splitter)
        self.ui_state.register_tab_widget("main_tabs", self.main_tabs)

        # Show、Close、完全破棄とMaya終了へ自動連携するtrackerを作成する。
        self.ui_state_tracker = MayaUiStateTracker.for_window(
            self.ui_state,
            self,
        )


# module内で1つのwindow instanceを共有する。
_controller = MayaWindowController(
    SampleWindow,
    settings_path=_SETTINGS_PATH,
)


def show() -> SampleWindow:
    """sample windowを表示してinstanceを返す。"""
    # 既存windowがある場合はcontrollerから再表示する。
    return _controller.show()


def dispose() -> None:
    """sample windowを完全に破棄する。"""
    # close時に状態を保存し、次のshowで新しいWindowを生成できるようにする。
    _controller.dispose()


def reset() -> bool:
    """sample windowと保存済みUI配置を初期状態へ戻す。"""
    # Windowを完全破棄してgeometryとWidget内部状態をまとめて削除する。
    return reset_ui_layout(_controller, _SETTINGS_PATH)


def reset_and_show() -> SampleWindow:
    """UI配置をリセットしてsample windowを初期状態で再表示する。"""
    # ユーザー操作向けにreset完了後の新しいWindowを返す。
    return reset_and_show_ui_layout(_controller, _SETTINGS_PATH)
