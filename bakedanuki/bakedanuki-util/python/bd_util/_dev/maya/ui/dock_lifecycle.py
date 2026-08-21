# coding: utf-8
from ....maya.ui import (
    DockArea,
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
    MayaUiStateTracker,
    create_ui_state_manager,
    reset_and_show_ui_layout,
    reset_ui_layout,
)
from ....ui import qt

_SETTINGS_PATH = "bakedanuki_util/dev/dock_lifecycle"
_EVENT_HISTORY: list[str] = []


class DockLifecycleHarness(MayaDockableWindow):
    """dockable Windowのlifecycleを実Mayaで確認する開発用UI。"""

    def __init__(self) -> None:
        """状態保存対象とlifecycle event表示を持つUIを構築する。"""
        # MayaのworkspaceControlへ接続できるWidgetを初期化する。
        super().__init__()
        self.setWindowTitle("bakedanuki-util dock lifecycle harness")

        # 手動確認する操作と期待する状態をWindow内へ表示する。
        instructions = qt.QLabel(
            "Move the splitter and select another tab, then use Close, "
            "Dispose, or Reset. Lifecycle events are recorded below."
        )
        instructions.setWordWrap(True)

        # 保存対象となるSplitterとTabを構築する。
        left_editor = qt.QTextEdit("Resize this pane to test QSplitter state.")
        self.main_tabs = qt.QTabWidget()
        self.main_tabs.addTab(qt.QTextEdit("First tab"), "First")
        self.main_tabs.addTab(qt.QTextEdit("Second tab"), "Second")

        self.main_splitter = qt.QSplitter()
        self.main_splitter.addWidget(left_editor)
        self.main_splitter.addWidget(self.main_tabs)
        self.main_splitter.setSizes([220, 320])

        # controllerの操作を実行するbuttonをまとめる。
        close_button = qt.QPushButton("Close")
        close_button.clicked.connect(close)
        dispose_button = qt.QPushButton("Dispose")
        dispose_button.clicked.connect(dispose)
        reset_button = qt.QPushButton("Reset")
        reset_button.clicked.connect(reset_and_show)

        button_layout = qt.QHBoxLayout()
        button_layout.addWidget(close_button)
        button_layout.addWidget(dispose_button)
        button_layout.addWidget(reset_button)

        # controllerとMaya mixinから届くlifecycle eventの表示欄を作成する。
        self.event_log = qt.QPlainTextEdit()
        self.event_log.setReadOnly(True)
        self.event_log.setMaximumBlockCount(100)
        self.event_log.setPlainText("\n".join(_EVENT_HISTORY))

        layout = qt.QVBoxLayout(self)
        layout.addWidget(instructions)
        layout.addWidget(self.main_splitter)
        layout.addLayout(button_layout)
        layout.addWidget(self.event_log)

        # trackerより先に接続して、完全破棄直前のeventも画面へ記録する。
        self.dock_attached.connect(self._on_dock_attached)
        self.dock_closed.connect(self._on_dock_closed)
        self.dock_about_to_dispose.connect(self._on_dock_about_to_dispose)
        self.floating_changed.connect(self._on_floating_changed)

        # tool単位のINIへSplitterと選択タブを保存する。
        self.ui_state = create_ui_state_manager(_SETTINGS_PATH)
        self.ui_state.register_splitter("main_splitter", self.main_splitter)
        self.ui_state.register_tab_widget("main_tabs", self.main_tabs)

        # dock lifecycleとMaya終了処理へ状態管理を一括接続する。
        self.ui_state_tracker = MayaUiStateTracker.for_dockable(
            self.ui_state,
            self,
        )
        self._append_event("window_created")

    def _append_event(self, name: str) -> None:
        """現在時刻とlifecycle event名を表示欄へ追加する。"""
        # 複数回のshowやcloseを目視で追える時刻付き文字列へ整形する。
        current_time = qt.QtCore.QTime.currentTime().toString("HH:mm:ss.zzz")
        event = f"{current_time}  {name}"

        # 完全破棄後に生成した次のWindowからも直前のeventを確認できるよう保持する。
        _EVENT_HISTORY.append(event)
        del _EVENT_HISTORY[:-100]
        self.event_log.appendPlainText(event)

    def _on_dock_attached(self) -> None:
        """workspaceControlへの接続完了を記録する。"""
        self._append_event("dock_attached")

    def _on_dock_closed(self) -> None:
        """workspaceControlの通常closeを記録する。"""
        self._append_event("dock_closed")

    def _on_dock_about_to_dispose(self) -> None:
        """workspaceControlの完全破棄直前を記録する。"""
        self._append_event("dock_about_to_dispose")

    def _on_floating_changed(self, floating: bool) -> None:
        """workspaceControlのfloating変更を記録する。"""
        self._append_event(f"floating_changed: {floating}")


# Maya再起動時にもimportできる固定復元先でcontrollerを構築する。
_controller = MayaDockableWindowController(
    DockLifecycleHarness,
    control_id="bdUtilDockLifecycleHarness",
    restore=DockRestoreSpec(
        module="bd_util._dev.maya.ui.dock_lifecycle",
        function="restore",
    ),
    dock_options=DockOptions(
        area=DockArea.RIGHT,
        floating=False,
        initial_width=560,
        initial_height=560,
        retain=True,
    ),
)


def show() -> DockLifecycleHarness:
    """lifecycle確認Windowを表示する。"""
    # 初回生成または保持済みworkspaceControlの再表示を実行する。
    return _controller.show()


def restore() -> DockLifecycleHarness:
    """Mayaが復元したworkspaceControlへ確認Windowを接続する。"""
    # uiScript実行中のcurrent parentへ新しいWidgetを接続する。
    return _controller.restore()


def close() -> None:
    """Widgetを保持したままworkspaceControlを閉じる。"""
    # retain設定を使う通常close経路を実行する。
    _controller.close()


def dispose() -> None:
    """状態保存後にworkspaceControlとWidgetを完全破棄する。"""
    # lifecycle通知による保存とcallback解除を経由して削除する。
    _controller.dispose()


def reset() -> bool:
    """workspaceControl配置とWidget内部状態を初期値へ戻す。"""
    # 完全破棄後にMayaとINIへ保存されたUI配置をまとめて削除する。
    return reset_ui_layout(_controller, _SETTINGS_PATH)


def reset_and_show() -> DockLifecycleHarness:
    """UI配置をリセットして確認Windowを初期状態で再表示する。"""
    # Reset buttonから初期配置のworkspaceControlをすぐに確認できるよう再生成する。
    return reset_and_show_ui_layout(_controller, _SETTINGS_PATH)
