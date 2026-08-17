from typing import assert_type

from PySide6 import QtWidgets

from bd_util.maya.ui import (
    DockOptions,
    DockRestoreSpec,
    MayaDockableWindow,
    MayaDockableWindowController,
    MayaWindowController,
    get_main_window,
)
from bd_util.ui import SettingsPath, WindowController


class SampleWindow(QtWidgets.QDialog):
    pass


class SampleDockableWindow(MayaDockableWindow):
    pass


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
