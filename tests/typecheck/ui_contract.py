from typing import assert_type

from PySide6 import QtWidgets

from bd_util.maya.ui import MayaWindowController, get_main_window
from bd_util.ui import WindowController


class SampleWindow(QtWidgets.QDialog):
    pass


window_controller = WindowController(SampleWindow)
assert_type(window_controller.window, SampleWindow | None)
assert_type(window_controller.show(), SampleWindow)

maya_window_controller = MayaWindowController(SampleWindow)
assert_type(maya_window_controller.window, SampleWindow | None)
assert_type(maya_window_controller.show(), SampleWindow)
assert_type(get_main_window(), QtWidgets.QWidget | None)
