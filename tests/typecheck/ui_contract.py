from dataclasses import dataclass
from typing import assert_type

from PySide6 import QtGui, QtWidgets

from bd_util import Nodes
from bd_util._sample.maya.ui.bool_views import (
    BoolViewsWidget,
    BoolViewsWindow,
    BoolViewsWindowManager,
    VisibilityData,
)
from bd_util.maya.ui import (
    DockOptions,
    DockRestoreSpec,
    MayaCallbackRegistry,
    MayaBoolPlugStore,
    MayaBoolPlugView,
    MayaDockableWindow,
    MayaDockableWindowController,
    MayaUiStateTracker,
    MayaWindowController,
    create_ui_state_manager,
    get_main_window,
    reset_and_show_ui_layout,
    reset_ui_layout,
)
from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    BoolValue,
    BoolValueStore,
    BoolViewModel,
    PythonBoolAttributeStore,
    SettingsPath,
    SetBoolCommand,
    UiStateManager,
    WindowController,
    ensure_window_on_screen,
    qt,
)


class SampleWindow(QtWidgets.QDialog):
    pass


@dataclass
class SampleBoolData:
    visible: bool = True


class SampleDockableWindow(MayaDockableWindow):
    pass


class FacadeWidget(qt.QWidget):
    changed = qt.Signal()


window_controller = WindowController(SampleWindow)
assert_type(window_controller.window, SampleWindow | None)
assert_type(window_controller.show(), SampleWindow)
assert_type(window_controller.retain, bool)
assert_type(ensure_window_on_screen(SampleWindow()), bool)

maya_window_controller = MayaWindowController(SampleWindow)
assert_type(maya_window_controller.window, SampleWindow | None)
assert_type(maya_window_controller.show(), SampleWindow)
assert_type(maya_window_controller.settings_path, SettingsPath | None)
assert_type(maya_window_controller.retain, bool)

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
assert_type(dockable_controller.ensure_on_screen(), bool)
assert_type(dockable_controller.control_id, str)
assert_type(dockable_controller.workspace_control_name, str)
assert_type(dockable_controller.dock_options.retain, bool)

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
    ui_state_manager.register_tab_widget(
        "main_tabs",
        QtWidgets.QTabWidget(),
    ),
    None,
)
assert_type(ui_state_manager.save(), bool)
assert_type(ui_state_manager.save_cached(), bool)
assert_type(ui_state_manager.restore(), frozenset[str])
assert_type(ui_state_manager.clear(), bool)

ui_state_tracker = MayaUiStateTracker(
    ui_state_manager,
    SampleDockableWindow(),
)
assert_type(ui_state_tracker.manager, UiStateManager)
assert_type(ui_state_tracker.restore(), None)
assert_type(ui_state_tracker.save(), bool)
assert_type(ui_state_tracker.dispose(), None)

callback_owner = SampleWindow()
callback_registry = MayaCallbackRegistry(callback_owner)
assert_type(callback_registry.callback_ids, tuple[int, ...])
assert_type(callback_registry.is_disposed, bool)
assert_type(callback_registry.register(42), int)
assert_type(callback_registry.remove(42), bool)
assert_type(callback_registry.dispose(), None)

dockable_ui_state_tracker = MayaUiStateTracker.for_dockable(
    ui_state_manager,
    SampleDockableWindow(),
)
assert_type(dockable_ui_state_tracker, MayaUiStateTracker)
normal_ui_state_tracker = MayaUiStateTracker.for_window(
    ui_state_manager,
    SampleWindow(),
)
assert_type(normal_ui_state_tracker, MayaUiStateTracker)
assert_type(
    reset_ui_layout(
        dockable_controller,
        "sample_tool/windows/main",
    ),
    bool,
)
assert_type(
    reset_ui_layout(
        maya_window_controller,
        "sample_tool/windows/main",
        clear_widget_state=False,
    ),
    bool,
)
assert_type(
    reset_and_show_ui_layout(
        dockable_controller,
        "sample_tool/windows/main",
    ),
    SampleDockableWindow,
)
assert_type(
    reset_and_show_ui_layout(
        maya_window_controller,
        "sample_tool/windows/main",
    ),
    SampleWindow,
)

facade_widget = FacadeWidget()
assert_type(facade_widget, FacadeWidget)
assert_type(qt.QLabel(), QtWidgets.QLabel)
assert_type(qt.QAction(), QtGui.QAction)

bool_view_model = BoolViewModel(False)
assert_type(bool_view_model.value, BoolValue)
assert_type(bool_view_model.value.value, bool)
assert_type(bool_view_model.set_value_command, SetBoolCommand)
assert_type(bool_view_model.set_value_command.can_execute, bool)
assert_type(bool_view_model.set_value_command.execute(True), bool)
assert_type(bool_view_model.store, BoolValueStore | None)

sample_bool_data = SampleBoolData()
python_bool_store = PythonBoolAttributeStore(sample_bool_data, "visible")
assert_type(
    python_bool_store,
    PythonBoolAttributeStore[SampleBoolData],
)
assert_type(python_bool_store.instance, SampleBoolData)
assert_type(python_bool_store.attribute_name, str)
assert_type(python_bool_store.is_available, bool)
assert_type(python_bool_store.is_writable, bool)
assert_type(python_bool_store.read(), bool)
assert_type(python_bool_store.write(False), bool)
assert_type(bool_view_model.attach_store(python_bool_store), None)

# sampleのFeature WidgetとWindow管理APIが具体型を維持することを確認する。
sample_visibility_data = VisibilityData()
bool_views_widget = BoolViewsWidget(
    sample_visibility_data,
    "visible_by_default",
)
assert_type(bool_views_widget, BoolViewsWidget)
assert_type(bool_views_widget.value, bool)
assert_type(bool_views_widget.maya_view, MayaBoolPlugView | None)
assert_type(bool_views_widget.set_value(False), bool)
assert_type(bool_views_widget.refresh_from_data(), bool)

bool_views_window = BoolViewsWindow(
    sample_visibility_data,
    "visible_by_default",
)
assert_type(bool_views_window, BoolViewsWindow)
assert_type(bool_views_window.bool_views_widget, BoolViewsWidget)

bool_views_window_manager = BoolViewsWindowManager()
assert_type(bool_views_window_manager.window, BoolViewsWindow | None)
assert_type(
    bool_views_window_manager.show(
        sample_visibility_data,
        "visible_by_default",
    ),
    BoolViewsWindow,
)
assert_type(bool_views_window_manager.set_value(False), bool)
assert_type(bool_views_window_manager.refresh_from_data(), bool)
assert_type(bool_views_window_manager.dispose(), None)

bool_checkbox = BoolCheckBox(
    bool_view_model,
    "Visibility",
)
assert_type(bool_checkbox, BoolCheckBox)
assert_type(bool_checkbox.view_model, BoolViewModel)

bool_combo_box = BoolComboBox(
    bool_view_model,
    false_text="Off",
    true_text="On",
)
assert_type(bool_combo_box, BoolComboBox)
assert_type(bool_combo_box.view_model, BoolViewModel)

bool_push_button = BoolPushButton(
    bool_view_model,
    false_text="Off",
    true_text="On",
)
assert_type(bool_push_button, BoolPushButton)
assert_type(bool_push_button.view_model, BoolViewModel)

bool_radio_button_group = BoolRadioButtonGroup(
    bool_view_model,
    false_text="Off",
    true_text="On",
)
assert_type(bool_radio_button_group, BoolRadioButtonGroup)
assert_type(bool_radio_button_group.view_model, BoolViewModel)
assert_type(bool_radio_button_group.false_button, QtWidgets.QRadioButton)
assert_type(bool_radio_button_group.true_button, QtWidgets.QRadioButton)

bool_status_label = BoolStatusLabel(
    bool_view_model,
    false_text="Status: Off",
    true_text="Status: On",
)
assert_type(bool_status_label, BoolStatusLabel)
assert_type(bool_status_label.view_model, BoolViewModel)

transform = Nodes().existing.transform("sampleTransform")
maya_store_view_model = BoolViewModel()
maya_bool_store = MayaBoolPlugStore(
    maya_store_view_model,
    transform.visibility,
    SampleWindow(),
)
assert_type(maya_store_view_model.attach_store(maya_bool_store), None)
assert_type(maya_bool_store, MayaBoolPlugStore)
assert_type(maya_bool_store.view_model, BoolViewModel)
assert_type(maya_bool_store.is_available, bool)
assert_type(maya_bool_store.is_writable, bool)
assert_type(maya_bool_store.is_disposed, bool)
assert_type(maya_bool_store.read(), bool)
assert_type(maya_bool_store.write(False), bool)
assert_type(maya_bool_store.refresh(), bool)
assert_type(maya_bool_store.dispose(), None)

maya_bool_view = MayaBoolPlugView(
    bool_view_model,
    transform.visibility,
    SampleWindow(),
)
assert_type(maya_bool_view, MayaBoolPlugView)
assert_type(maya_bool_view.view_model, BoolViewModel)
assert_type(maya_bool_view.is_available, bool)
assert_type(maya_bool_view.is_writable, bool)
assert_type(maya_bool_view.is_synchronized, bool)
assert_type(maya_bool_view.last_sync_error, Exception | None)
assert_type(maya_bool_view.is_disposed, bool)
assert_type(maya_bool_view.sync_from_view_model(), bool)
assert_type(maya_bool_view.dispose(), None)
