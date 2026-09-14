# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.ui import (
    Float3RangeSliderSpinBox,
    FloatPresentation,
    SettingsPath,
    UiStateManager,
    qt,
)
from bd_util.maya.ui import (
    MayaFloat3Binding,
    MayaFloat3PlugBinding,
    MayaUiStateTracker,
    MayaDockableWindow,
    create_ui_state_manager,
    reset_and_show_ui_layout,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util._sample.maya.ui.float_sample import (
    maya_plug as scalar_maya,
    maya_view as scalar_python,
    minimal as scalar_minimal,
)
from bd_util._sample.maya.ui.float3_sample import (
    maya_plug as triple_maya,
    maya_view as triple_python,
    minimal as triple_minimal,
)

SAMPLES = (
    scalar_maya,
    scalar_python,
    scalar_minimal,
    triple_maya,
    triple_python,
    triple_minimal,
)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    cmds.file(new=True, force=True)
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    owner = qt.QWidget()
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield owner, node
    for sample in SAMPLES:
        sample.dispose()
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo)


def sample_editor(window, sample):
    if sample is scalar_minimal:
        return window.widget.editor
    if sample is triple_minimal:
        return window.widget.spin_box.y_editor
    if sample in (triple_maya, triple_python):
        return window.widget.translate.y_editor
    return window.widget.translate_x_editor


def show_sample(sample, node):
    return (
        sample.show()
        if sample in (scalar_minimal, triple_minimal)
        else sample.show(node.cmd_access_name)
    )


@pytest.mark.parametrize("sample", SAMPLES)
@pytest.mark.parametrize("termination", ["close", "dispose"])
def test_samples_restore_range_step_after_recreation_and_keep_new_source(
    scene, sample, termination
):
    _, node = scene
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    window = show_sample(sample, node)
    flush()
    editor = sample_editor(window, sample)
    value = editor.view_model.value.value
    mode = editor.step_spin_box.stepMode()
    cmds.flushUndo()
    editor.setFloatRange(-250.123456789, 250.987654321)
    editor.setSingleStep(7.5)
    assert editor.view_model.value.value == value
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    if termination == "close":
        window.close()
    else:
        sample.dispose()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    replacement = show_sample(sample, node)
    flush()
    restored = sample_editor(replacement, sample)
    assert restored.floatRange() == (-250.123456789, 250.987654321)
    assert restored.singleStep() == restored.step_spin_box.value() == 7.5
    assert restored.step_spin_box.stepMode() == mode
    assert restored.view_model.value.value == pytest.approx(value)


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize(
    "attribute,kind",
    [("translate", "distance"), ("rotate", "angle"), ("scale", "number")],
)
def test_unit_metadata_and_restore_preserve_physical_range_step_number_and_undo(
    scene, tmp_path, source, attribute, kind
):
    owner, node = scene

    @dataclass
    class Data:
        value: tuple[float, float, float] = (
            1.23456789,
            2.34567891,
            3.45678912,
        )

    plug = getattr(node, attribute)
    if source == "maya":
        cmds.setAttr(
            f"{node.cmd_access_name}.{attribute}",
            *Data().value,
            type="double3",
        )
        binding = MayaFloat3PlugBinding(plug, parent=owner)
    else:
        binding = MayaFloat3Binding.from_attribute(
            Data(), "value", maya_plug=plug, parent=owner
        )
    settings = qt.QtCore.QSettings(
        str(tmp_path / "units.ini"), qt.QtCore.QSettings.Format.IniFormat
    )
    first = Float3RangeSliderSpinBox(binding, owner, minimum=-100, maximum=100)
    manager = UiStateManager(
        settings, SettingsPath("tool/editor_settings/main")
    )
    manager.register_float3_range_slider_spin_box("axes", first)
    first.x_editor.setFloatRange(-200, 200)
    first.x_editor.setSingleStep(15)
    manager.save_cached()
    original = binding.value
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    restored = Float3RangeSliderSpinBox(
        binding, owner, minimum=-10, maximum=10, minimum_decimals=6
    )
    second = UiStateManager(
        settings, SettingsPath("tool/editor_settings/main")
    )
    second.register_float3_range_slider_spin_box("axes", restored)
    cmds.flushUndo()
    assert second.restore() == frozenset({"axes_x", "axes_y", "axes_z"})
    assert restored.view_model.x.presentation.unit_kind == kind
    assert restored.x_editor.floatRange() == (-200, 200)
    assert restored.x_editor.minimum_spin_box.value() == pytest.approx(
        restored.view_model.x.presentation.to_display(-200), abs=1e-6
    )
    assert restored.x_editor.singleStep() == 15
    assert binding.value == pytest.approx(original)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    restored.x_editor.slider.setSliderDown(True)
    restored.x_editor.slider.setValue(600)
    restored.x_editor.slider.setValue(700)
    restored.x_editor.slider.setSliderDown(False)
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(original)
    assert restored.x_editor.singleStep() == 15
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_layout_reset_keeps_editor_settings_and_same_window_show_does_not_restore_again(
    scene,
):
    _, node = scene
    window = scalar_maya.show(node.cmd_access_name)
    flush()
    window.widget.translate_x_editor.setFloatRange(-30, 70)
    window.widget.translate_x_editor.setSingleStep(2.5)
    restored = reset_and_show_ui_layout(
        scalar_maya._controller, "float_sample/windows/maya_plug"
    )
    flush()
    assert restored is not window
    assert restored.widget.translate_x_editor.floatRange() == (-30, 70)
    assert restored.widget.translate_x_editor.singleStep() == 2.5
    restored.widget.translate_x_editor.setSingleStep(3.5)
    restored.hide()
    restored.show()
    flush()
    assert restored.widget.translate_x_editor.singleStep() == 3.5


def test_maya_exit_saves_cached_settings_after_binding_disposal(scene):
    _, node = scene
    window = triple_maya.show(node.cmd_access_name)
    flush()
    editor = window.widget.rotate.z_editor
    editor.setFloatRange(-45, 45)
    editor.setSingleStep(7.5)
    window.widget.rotate_binding.dispose()
    # Maya終了callbackの入口を呼び、実際のMaya processは終了しない。
    window.editor_settings_tracker._on_maya_exiting()
    probe = create_ui_state_manager("float3_sample/editor_settings/maya_plug")
    other = Float3RangeSliderSpinBox(
        window.widget.translate_binding, window, minimum=0, maximum=1
    )
    probe.register_float3_range_slider_spin_box("translate", other)
    assert probe.restore() == frozenset(
        {"translate_x", "translate_y", "translate_z"}
    )
    assert window.editor_settings_tracker._owner is None
    window.close()
    flush()
    replacement = triple_maya.show(node.cmd_access_name)
    flush()
    assert replacement.widget.rotate.z_editor.floatRange() == (-45, 45)
    assert replacement.widget.rotate.z_editor.singleStep() == 7.5


def test_dock_lifecycle_restores_once_and_saves_after_binding_disposal(
    scene, tmp_path
):
    owner, node = scene
    settings = qt.QtCore.QSettings(
        str(tmp_path / "dock.ini"), qt.QtCore.QSettings.Format.IniFormat
    )
    path = SettingsPath("tool/editor_settings/dock")
    first = UiStateManager(settings, path)
    binding = MayaFloat3PlugBinding(node.translate, parent=owner)
    editor = Float3RangeSliderSpinBox(binding, owner, minimum=-1, maximum=1)
    first.register_float3_range_slider_spin_box("axes", editor)
    editor.y_editor.setFloatRange(-50, 50)
    editor.y_editor.setSingleStep(5)
    assert first.save_cached()

    dock = MayaDockableWindow()
    dock.setParent(owner)
    restored = Float3RangeSliderSpinBox(binding, dock, minimum=-2, maximum=2)
    manager = UiStateManager(settings, path)
    manager.register_float3_range_slider_spin_box("axes", restored)
    tracker = MayaUiStateTracker.for_dockable(manager, dock)
    # workspaceControl本体の生成を避け、controllerが発行する接続通知を再現する。
    dock.dock_attached.emit()
    flush()
    assert restored.y_editor.floatRange() == (-50, 50)
    assert restored.y_editor.singleStep() == 5
    restored.y_editor.setSingleStep(7.5)
    dock.dock_attached.emit()
    flush()
    assert restored.y_editor.singleStep() == 7.5
    binding.dispose()
    dock.dock_about_to_dispose.emit()
    assert tracker._owner is None
    replacement_binding = MayaFloat3PlugBinding(node.translate, parent=owner)
    replacement = Float3RangeSliderSpinBox(
        replacement_binding, owner, minimum=-1, maximum=1
    )
    probe = UiStateManager(settings, path)
    probe.register_float3_range_slider_spin_box("axes", replacement)
    assert probe.restore() == frozenset({"axes_x", "axes_y", "axes_z"})
    assert replacement.y_editor.singleStep() == 7.5
