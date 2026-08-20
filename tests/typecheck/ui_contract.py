from typing import assert_type

from PySide6 import QtCore, QtGui, QtWidgets

from bd_util.maya.ui import (
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
    MayaWindowController,
    create_ui_state_manager,
    get_main_window,
)
from bd_util.ui import SettingsPath, UiStateManager, WindowController, qt


class SampleWindow(QtWidgets.QDialog):
    pass


class SampleDockableWindow(MayaDockableWindow):
    pass


class FacadeWidget(qt.QWidget):
    changed = qt.Signal()


window_controller = WindowController(SampleWindow)
assert_type(window_controller.window, SampleWindow | None)
assert_type(window_controller.show(), SampleWindow)

maya_window_controller = MayaWindowController(SampleWindow)
assert_type(maya_window_controller.window, SampleWindow | None)
assert_type(maya_window_controller.show(), SampleWindow)
assert_type(maya_window_controller.settings_path, SettingsPath | None)

persistent_maya_window_controller = MayaWindowController(
    SampleWindow,
    settings_path="sample_tool/windows/main",
)
assert_type(persistent_maya_window_controller.show(), SampleWindow)
assert_type(
    persistent_maya_window_controller.settings_path,
    SettingsPath | None,
)

settings_path = SettingsPath("sample_tool/windows/main")
assert_type(settings_path.tool_name, str)
assert_type(settings_path.group_path, str)
assert_type(get_main_window(), QtWidgets.QWidget | None)

dockable_controller = MayaDockableWindowController(
    SampleDockableWindow,
    control_id="sampleDockableWindow",
    restore=DockRestoreSpec("sample_tool.ui"),
    dock_options=DockOptions(),
)
assert_type(dockable_controller.window, SampleDockableWindow | None)
assert_type(dockable_controller.show(), SampleDockableWindow)
assert_type(dockable_controller.restore(), SampleDockableWindow)
assert_type(dockable_controller.control_id, str)
assert_type(dockable_controller.workspace_control_name, str)

ui_state_manager = create_ui_state_manager("sample_tool/windows/main")
assert_type(ui_state_manager, UiStateManager)
assert_type(ui_state_manager.settings_path, SettingsPath)
assert_type(ui_state_manager.registered_keys, tuple[str, ...])
assert_type(
    ui_state_manager.register_splitter(
        "main_splitter",
        QtWidgets.QSplitter(),
    ),
    None,
)
assert_type(
    ui_state_manager.register_header(
        "main_header",
        QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal),
    ),
    None,
)
assert_type(
    ui_state_manager.register_tab_widget(
        "main_tabs",
        QtWidgets.QTabWidget(),
    ),
    None,
)
assert_type(ui_state_manager.save(), bool)
assert_type(ui_state_manager.restore(), frozenset[str])
assert_type(ui_state_manager.clear(), bool)

facade_widget = FacadeWidget()
assert_type(facade_widget, FacadeWidget)
assert_type(qt.QLabel(), QtWidgets.QLabel)
assert_type(qt.QAction(), QtGui.QAction)
