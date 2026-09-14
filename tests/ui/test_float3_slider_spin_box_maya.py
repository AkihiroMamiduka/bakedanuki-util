# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaFloat3Binding,
    MayaFloat3PlugBinding,
    resolve_float3_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.maya.ui.binding._float_plug_value import FloatPlugValue
from bd_util.ui import (
    Float3Label,
    Float3SliderSpinBox,
    Float3RangeSliderSpinBox,
    SettingsPath,
    UiStateManager,
    qt,
)
from bd_util._sample.maya.ui.float3_sample import maya_plug, maya_view, minimal


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
    undo_enabled = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    owner = qt.QWidget()
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield owner, node
    for sample in (maya_plug, maya_view, minimal):
        sample.dispose()
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


def make_binding(owner, node, source, attribute="translate"):
    @dataclass
    class Data:
        value: tuple[float, float, float] = (
            1.23456789,
            2.34567891,
            3.45678912,
        )

    cmds.setAttr(
        f"{node.cmd_access_name}.{attribute}", *Data().value, type="double3"
    )
    plug = resolve_float3_plug(node.cmd_access_name, attribute)
    if source == "maya":
        return MayaFloat3PlugBinding(plug, parent=owner)
    return MayaFloat3Binding.from_attribute(
        Data(), "value", maya_plug=plug, parent=owner
    )


@pytest.fixture(params=[Float3SliderSpinBox, Float3RangeSliderSpinBox])
def view_factory(request):
    def create(binding, parent, **kwargs):
        if request.param is Float3RangeSliderSpinBox:
            kwargs["value_show_unit"] = True
        return request.param(binding, parent, **kwargs)

    return create


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["translate", "rotate", "scale"])
def test_each_axis_drag_is_one_undo_and_tracks_units_and_other_views(
    scene, source, attribute, view_factory
):
    owner, node = scene
    binding = make_binding(owner, node, source, attribute)
    original = binding.value
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    view = view_factory(binding, owner, minimum=-100, maximum=100, decimals=3)
    linked = view_factory(
        binding.view_model, owner, minimum=-100, maximum=100, decimals=3
    )
    label = Float3Label(binding, owner, decimals=3)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    assert binding.value == pytest.approx(original)
    cmds.flushUndo()
    confirmed = list(original)
    refreshed = []
    binding.view_model.store_refreshed.connect(refreshed.append)
    for index, editor, other, value_label in zip(
        range(3),
        (view.x_editor, view.y_editor, view.z_editor),
        (linked.x_editor, linked.y_editor, linked.z_editor),
        (label.x_label, label.y_label, label.z_label),
    ):
        editor.slider.setSliderDown(True)
        for position in (600, 700, 800):
            refreshed.clear()
            editor.slider.setValue(position)
            confirmed[index] = (position / 1000) * 200 - 100
            assert binding.value == pytest.approx(confirmed)
            assert len(refreshed) == 1
            assert refreshed[0] == pytest.approx(confirmed)
            assert other.slider.value() == position
            assert (
                editor.spin_box.text()
                == other.spin_box.text()
                == value_label.text()
            )
            assert editor.spin_box.value() == pytest.approx(
                round(
                    editor.view_model.presentation.to_display(
                        confirmed[index]
                    ),
                    3,
                )
            )
            if source == "python":
                assert binding.store.instance.value == pytest.approx(confirmed)
        editor.slider.setSliderDown(False)
    view.x_spin_box.setValue(view.view_model.x.presentation.to_display(140))
    assert binding.value[0] > 100
    assert view.x_editor.slider.value() == 1000
    cmds.undo()
    flush()
    assert binding.value == pytest.approx((60, 60, 60))
    for index in (2, 1, 0):
        cmds.undo()
        flush()
        confirmed[index] = original[index]
        assert binding.value == pytest.approx(confirmed)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    for index in (0, 1, 2):
        cmds.redo()
        flush()
        confirmed[index] = 60
        assert binding.value == pytest.approx(confirmed)
    cmds.redo()
    flush()
    assert binding.value[0] > 100
    assert cmds.undoInfo(q=True, redoQueueEmpty=True)


def test_drag_limits_maya_rereads_per_position_without_delaying_other_axes(
    scene, monkeypatch, view_factory, tmp_path
):
    owner, node = scene
    binding = make_binding(owner, node, "maya")
    original = binding.value
    view = view_factory(binding, owner, minimum=0, maximum=100)
    if isinstance(view, Float3RangeSliderSpinBox):
        settings = qt.QtCore.QSettings(
            str(tmp_path / "drag.ini"), qt.QtCore.QSettings.Format.IniFormat
        )
        manager = UiStateManager(
            settings, SettingsPath("tool/editor_settings/main")
        )
        manager.register_float3_range_slider_spin_box("axes", view)

        def reject_capture(*args):
            pytest.fail("現在値のドラッグでは設定を再取得しない")

        monkeypatch.setattr(
            type(manager._adapters["axes_x"]), "save_state", reject_capture
        )
    read = FloatPlugValue.read
    reads = 0

    def counted_read(codec):
        nonlocal reads
        reads += 1
        return read(codec)

    monkeypatch.setattr(FloatPlugValue, "read", counted_read)
    view.x_editor.slider.setSliderDown(True)
    for position in (300, 400, 500):
        reads = 0
        view.x_editor.slider.setValue(position)
        assert binding.value == pytest.approx(
            (position / 10, original[1], original[2])
        )
        # 時間の揺らぎに依存せず、従来の41回への増加を検知する。
        assert reads <= 20
    view.x_editor.slider.setSliderDown(False)


@pytest.mark.parametrize("source", ["maya", "python"])
def test_switching_axis_ends_previous_edit_and_closing_other_view_does_not(
    scene, source, view_factory
):
    owner, node = scene
    binding = make_binding(owner, node, source)
    original = binding.value
    view = view_factory(binding, owner, minimum=0, maximum=100)
    other = view_factory(binding, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    view.x_editor.slider.setSliderDown(True)
    view.x_editor.slider.setValue(300)
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(500)
    assert not binding.view_model.x.is_editing
    assert binding.view_model.y.is_editing
    assert not view.x_editor.slider.isSliderDown()
    other.close()
    assert binding.view_model.y.is_editing
    view.hide()
    assert not binding.view_model.y.is_editing
    assert FloatEditUndo._active is None
    cmds.setAttr(f"{node.cmd_access_name}.tz", 10)
    cmds.undo()
    flush()
    assert binding.value == pytest.approx((30, 50, original[2]))
    cmds.undo()
    flush()
    assert binding.value == pytest.approx((30, original[1], original[2]))
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(original)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_axis_and_parent_lock_connection_and_callback_release(
    scene, view_factory
):
    owner, node = scene
    path = f"{node.cmd_access_name}.translate"
    baseline = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = make_binding(owner, node, "maya")
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    view = view_factory(binding, owner, minimum=0, maximum=100)
    label = Float3Label(binding, owner)
    view.y_editor.slider.setSliderDown(True)
    view.y_editor.slider.setValue(300)
    cmds.setAttr(f"{node.cmd_access_name}.ty", lock=True)
    flush()
    assert not binding.view_model.y.is_editing
    assert not view.y_editor.slider.isEnabled()
    assert not view.y_spin_box.isEnabled()
    assert view.x_editor.slider.isEnabled()
    assert view.z_editor.slider.isEnabled()
    cmds.setAttr(f"{node.cmd_access_name}.ty", lock=False)
    cmds.setAttr(path, lock=True)
    flush()
    assert all(
        not editor.slider.isEnabled()
        for editor in (view.x_editor, view.y_editor, view.z_editor)
    )
    cmds.setAttr(path, lock=False)
    source = cmds.createNode("transform")
    cmds.connectAttr(f"{source}.translate", path)
    cmds.setAttr(f"{source}.translate", 20, 40, 60, type="double3")
    flush()
    assert (
        view.x_editor.slider.value(),
        view.y_editor.slider.value(),
        view.z_editor.slider.value(),
    ) == (200, 400, 600)
    assert not view.x_spin_box.isEnabled()
    if isinstance(view, Float3RangeSliderSpinBox):
        assert view.x_editor.minimum_spin_box.isEnabled()
        assert view.y_editor.maximum_spin_box.isEnabled()
        assert view.z_editor.step_spin_box.isEnabled()
    assert label.x_label.text() == "20.000000 cm"
    view.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.setAttr(f"{source}.ty", 50)
    flush()
    assert label.y_label.text() == "50.000000 cm"
    binding.dispose()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == baseline


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["translate", "rotate", "scale"])
def test_range_and_step_edits_remain_local_across_units_and_undo(
    scene, source, attribute
):
    owner, node = scene
    binding = make_binding(owner, node, source, attribute)
    original = binding.value
    view = Float3RangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=100,
        minimum_decimals=6,
        maximum_decimals=6,
        single_step=15,
        step_mode="multiplicative",
        minimum_show_unit=True,
        step_show_unit=True,
    )
    linked = Float3RangeSliderSpinBox(binding, owner, minimum=-10, maximum=10)
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    cmds.flushUndo()
    presentation = view.view_model.y.presentation
    editor = view.y_editor
    assert (
        editor.minimum_spin_box.suffix()
        == editor.step_spin_box.suffix()
        == presentation.suffix
    )
    assert editor.maximum_spin_box.suffix() == editor.spin_box.suffix() == ""
    assert editor.minimum_spin_box.value() == pytest.approx(
        presentation.to_display(-100), abs=1e-6
    )
    editor.minimum_spin_box.setValue(presentation.to_display(-200))
    editor.step_spin_box.stepDown()
    assert editor.singleStep() == 1.5
    low, high = editor.floatRange()
    assert low == pytest.approx(-200, abs=1e-4)
    assert high == 100
    assert (
        view.x_editor.floatRange() == view.z_editor.floatRange() == (-100, 100)
    )
    assert linked.y_editor.floatRange() == (-10, 10)
    assert linked.y_editor.singleStep() == 0.1
    assert binding.value == pytest.approx(original)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    editor.slider.setSliderDown(True)
    editor.slider.setValue(600)
    editor.slider.setValue(800)
    editor.slider.setSliderDown(False)
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(original)
    assert editor.floatRange() == (low, high)
    assert editor.singleStep() == 1.5
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.currentUnit(linear="cm", angle="deg")
    flush()
    assert editor.floatRange() == (low, high)
    assert editor.singleStep() == 1.5


@pytest.mark.parametrize("sample", ["maya", "python_maya", "python"])
def test_samples_close_during_drag_release_callbacks_and_reopen(scene, sample):
    _, node = scene
    module = {"maya": maya_plug, "python_maya": maya_view, "python": minimal}[
        sample
    ]
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    window = (
        module.show()
        if sample == "python"
        else module.show(node.cmd_access_name)
    )
    editor = (
        window.widget.spin_box
        if sample == "python"
        else window.widget.translate
    )
    assert isinstance(editor, Float3RangeSliderSpinBox)
    assert editor.x_editor.spin_box is editor.x_spin_box
    editor.z_editor.slider.setSliderDown(True)
    editor.z_editor.slider.setValue(750)
    window.close()
    flush()
    assert not qt.isValid(editor)
    assert FloatEditUndo._active is None
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    replacement = (
        module.show()
        if sample == "python"
        else module.show(node.cmd_access_name)
    )
    assert replacement is not window
