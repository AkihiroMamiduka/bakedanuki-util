from typing import assert_type

from bd_util._sample.maya.ui.bool_sample import shared_bool_views
from bd_util._sample.maya.ui.bool_sample.shared_bool_views import (
    SharedBoolViewsManager,
    SharedBoolViewsWidget,
    SharedBoolViewsWindow,
)
from bd_util.maya.ui import MayaBoolPlugView
from bd_util.ui import BoolViewModel, PythonBoolAttributeStore, qt

# sampleの公開入口からManager、Window、Widgetまで型と補完を追えることを確認する。
data = shared_bool_views.VisibilityData()
manager = SharedBoolViewsManager(
    data,
    "visible_by_default",
    maya_node_name="sampleTransform",
    maya_attribute_name="visibility",
)
assert_type(manager.data, object)
assert_type(manager.store, PythonBoolAttributeStore[object])
assert_type(manager.view_model, BoolViewModel)
assert_type(manager.maya_view, MayaBoolPlugView | None)
assert_type(manager.value, bool)
assert_type(manager.is_disposed, bool)
assert_type(manager.window_a, SharedBoolViewsWindow | None)
assert_type(manager.window_b, SharedBoolViewsWindow | None)
assert_type(
    manager.show(), tuple[SharedBoolViewsWindow, SharedBoolViewsWindow]
)
assert_type(manager.show_a(), SharedBoolViewsWindow)
assert_type(manager.show_b(), SharedBoolViewsWindow)
assert_type(manager.set_value(False), bool)
assert_type(manager.refresh_from_data(), bool)
assert_type(manager.print_data_value(), None)

window_a, window_b = manager.show()
assert_type(window_a.bool_views_widget, SharedBoolViewsWidget)
assert_type(window_b.bool_views_widget.view_model, BoolViewModel)
assert_type(window_a.bool_views_widget.print_value_button, qt.QPushButton)
assert_type(manager.dispose(), None)
