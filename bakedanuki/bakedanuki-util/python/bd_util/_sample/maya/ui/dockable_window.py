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

        # Maya終了前の保存とdock接続後の復元を管理するtrackerを作成する。
        self.ui_state_tracker = MayaUiStateTracker(self.ui_state, self)

        # 通常のdock closeでもMaya終了時と同じ保存処理を実行する。
        self.dock_closed.connect(self.ui_state_tracker.save)


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
    window = _controller.show()

    # workspaceControl接続後のlayout確定を待ってUI内部状態を復元する。
    window.ui_state_tracker.restore()
    return window


def restore() -> SampleDockableWindow:
    """Mayaが復元したworkspaceControlへsample windowを接続する。"""
    # uiScript実行中のcurrent parentへWidgetを追加する。
    window = _controller.restore()

    # Maya起動時もworkspaceControlへの接続完了後に復元を予約する。
    window.ui_state_tracker.restore()
    return window


def dispose() -> None:
    """sample windowとworkspaceControlを完全に破棄する。"""
    # dock closeを経由しない完全破棄でも現在のWidget状態を保存する。
    window = _controller.window
    if window is not None:
        window.ui_state_tracker.save()
        window.ui_state_tracker.dispose()

    # 開発中のmodule reload前に残っているMaya UIを削除する。
    _controller.dispose()
