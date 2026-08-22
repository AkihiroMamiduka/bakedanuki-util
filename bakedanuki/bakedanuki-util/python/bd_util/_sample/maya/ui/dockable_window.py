# coding: utf-8
from ....ui import qt
from ....maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
    MayaUiStateTracker,
    create_ui_state_manager,
)


class SampleDockableWindow(MayaDockableWindow):
    """Mayaへドッキングできるsample window。"""

    def __init__(self) -> None:
        """ドッキング動作を確認するsample UIを構築する。"""
        # Mayaのdockable mixinを含む基底Widgetを初期化する。
        super().__init__()
        self.setWindowTitle("bakedanuki-util dockable UI sample")

        # sampleの用途と保存対象を説明するlabelを作成する。
        label = qt.QLabel("Splitter sizes and the selected tab are saved.")
        label.setWordWrap(True)

        # Splitterの左側へ表示するNode一覧を作成する。
        self.node_tree = qt.QTreeWidget()
        self.node_tree.setColumnCount(3)
        self.node_tree.setHeaderLabels(["Name", "Type", "Status"])
        self.node_tree.addTopLevelItem(
            qt.QTreeWidgetItem(["root", "joint", "Ready"])
        )
        self.node_tree.addTopLevelItem(
            qt.QTreeWidgetItem(["body_ctrl", "transform", "Ready"])
        )

        # 選択タブを変更できる右側の編集領域を作成する。
        self.main_tabs = qt.QTabWidget()
        self.main_tabs.addTab(qt.QTextEdit("Settings page"), "Settings")
        self.main_tabs.addTab(qt.QTextEdit("Log page"), "Log")

        # TreeとTabをリサイズ可能なSplitterへ格納する。
        self.main_splitter = qt.QSplitter()
        self.main_splitter.addWidget(self.node_tree)
        self.main_splitter.addWidget(self.main_tabs)
        self.main_splitter.setSizes([180, 260])

        # workspaceControlを閉じる操作を確認するbuttonを作成する。
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(_controller.close)

        # 作成したWidgetを余白付きの縦方向へ配置する。
        layout = qt.QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.main_splitter)
        layout.addWidget(close_button)

        # tool単位のui.iniへ保存するWidgetを固定keyで明示登録する。
        self.ui_state = create_ui_state_manager(
            "bakedanuki_util/sample/dockable_window"
        )
        self.ui_state.register_splitter("main_splitter", self.main_splitter)
        self.ui_state.register_tab_widget("main_tabs", self.main_tabs)

        # dock接続、close、完全破棄とMaya終了へ連携するtrackerを作成する。
        self.ui_state_tracker = MayaUiStateTracker.for_dockable(
            self.ui_state,
            self,
        )


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
        retain=False,
    ),
)


def show() -> SampleDockableWindow:
    """sample windowを表示してinstanceを返す。"""
    # 表示中は同じWidgetを返し、close後は新しく生成する。
    return _controller.show()


def restore() -> SampleDockableWindow:
    """Mayaが復元したworkspaceControlへsample windowを接続する。"""
    # uiScript実行中のcurrent parentへWidgetを追加してlifecycleを通知する。
    return _controller.restore()


def dispose() -> None:
    """sample windowとworkspaceControlを完全に破棄する。"""
    # controllerの破棄通知で状態保存とcallback解除を行ってからMaya UIを削除する。
    _controller.dispose()
