# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.ui import FloatLabel, FloatSlider, FloatSpinBox, qt


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
    if qt.isValid(owner):
        owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["tx", "rx", "sx"])
def test_drag_updates_all_views_live_and_undo_redo_once(
    scene, source, attribute
):
    owner, node = scene

    @dataclass
    class Data:
        value: float = 10

    data = Data()
    path = f"{node.cmd_access_name}.{attribute}"
    cmds.setAttr(path, 10)
    plug = resolve_float_plug(node.cmd_access_name, attribute)
    binding = (
        MayaFloatPlugBinding(plug, parent=owner)
        if source == "maya"
        else MayaFloatBinding.from_attribute(
            data, "value", maya_plug=plug, parent=owner
        )
    )
    slider = FloatSlider(binding, owner, minimum=-100, maximum=100)
    spin = FloatSpinBox(binding, owner)
    label = FloatLabel(binding, owner)
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    cmds.flushUndo()
    slider.setSliderDown(True)
    for position in (600, 700, 800):
        slider.setValue(position)
        assert binding.value == pytest.approx((position / 1000) * 200 - 100)
        assert binding.value == pytest.approx(plug.get())
        assert label.text() == spin.text()
        if source == "python":
            assert data.value == binding.value
        flush()
    slider.setSliderDown(False)
    assert cmds.undoInfo(q=True, undoName=True) == "FloatSlider"
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(10)
    assert slider.value() == 550
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == pytest.approx(60)
    assert slider.value() == 800
    assert cmds.undoInfo(q=True, redoQueueEmpty=True)


@pytest.mark.parametrize(
    "finish",
    [
        "release",
        "hide",
        "disable",
        "range",
        "unit",
        "dispose",
        "delete_slider",
        "delete_owner",
    ],
)
def test_interruptions_close_chunk_before_next_unrelated_command(
    scene, finish
):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    slider = FloatSlider(binding, owner, minimum=0, maximum=100)
    slider.show()
    flush()
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(200)
    slider.setValue(600)
    assert FloatEditUndo._active is not None
    if finish == "release":
        slider.setSliderDown(False)
    elif finish == "hide":
        slider.hide()
    elif finish == "disable":
        slider.setEnabled(False)
    elif finish == "range":
        slider.setFloatRange(0, 200)
    elif finish == "unit":
        cmds.currentUnit(linear="m")
    elif finish == "dispose":
        binding.dispose()
    elif finish == "delete_slider":
        slider.deleteLater()
    else:
        owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.setAttr(f"{node.cmd_access_name}.ty", 5)
    cmds.undo()
    flush()
    assert node.translate.translateY.get() == 0
    assert node.translate.translateX.get() == 60
    # 単位変更自身の履歴はMayaの標準挙動に従う。
    if finish != "unit":
        cmds.undo()
        flush()
        assert node.translate.translateX.get() == 0


def test_no_move_same_float32_value_and_disabled_undo_add_no_history(scene):
    owner, node = scene
    path = f"{node.cmd_access_name}.weight"
    cmds.addAttr(
        node.cmd_access_name,
        longName="weight",
        attributeType="float",
        defaultValue=1,
    )
    binding = MayaFloatPlugBinding(
        resolve_float_plug(node.cmd_access_name, "weight"), parent=owner
    )
    slider = FloatSlider(binding, owner, minimum=1, maximum=1.000000001)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setSliderDown(False)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    slider.setSliderDown(True)
    slider.setValue(500)
    slider.setSliderDown(False)
    assert cmds.getAttr(path) == 1
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    slider.setFloatRange(0, 2)
    cmds.undoInfo(state=False)
    slider.setSliderDown(True)
    slider.setValue(750)
    slider.setSliderDown(False)
    assert binding.value == 1.5
    assert not cmds.undoInfo(q=True, state=True)
    assert FloatEditUndo._active is None


def test_two_bindings_do_not_leave_nested_chunks(scene):
    owner, node = scene
    first = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    second = MayaFloatPlugBinding(node.translate.translateY, parent=owner)
    x = FloatSlider(first, owner, minimum=0, maximum=100)
    y = FloatSlider(second, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    x.setSliderDown(True)
    x.setValue(500)
    y.setSliderDown(True)
    y.setValue(700)
    assert not first.view_model.is_editing
    y.setSliderDown(False)
    cmds.undo()
    assert first.value == 50
    assert second.value == 0
    cmds.undo()
    assert first.value == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_lock_connection_and_node_deletion_stop_edit(scene):
    owner, node = scene
    path = f"{node.cmd_access_name}.tx"
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    slider = FloatSlider(binding, owner, minimum=0, maximum=100)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    slider.setSliderDown(True)
    slider.setValue(500)
    cmds.setAttr(path, lock=True)
    flush()
    assert not slider.isEnabled()
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    cmds.setAttr(path, lock=False)
    flush()
    slider.setSliderDown(True)
    slider.setValue(600)
    cmds.connectAttr(f"{node.cmd_access_name}.ty", path)
    flush()
    assert not slider.isEnabled()
    assert FloatEditUndo._active is None
    cmds.disconnectAttr(f"{node.cmd_access_name}.ty", path)
    flush()
    slider.setSliderDown(True)
    slider.setValue(700)
    cmds.delete(node.cmd_access_name)
    flush()
    assert not slider.isEnabled()
    assert FloatEditUndo._active is None


def test_write_failure_closes_previous_successful_edits(scene, monkeypatch):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    slider = FloatSlider(binding, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(300)
    original = cmds.setAttr

    def fail(*args, **kwargs):
        raise RuntimeError("write failed")

    monkeypatch.setattr(cmds, "setAttr", fail)
    with pytest.raises(RuntimeError, match="write failed"):
        slider._request_value(800)
    monkeypatch.setattr(cmds, "setAttr", original)
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    assert slider.value() == 300
    cmds.undo()
    flush()
    assert binding.value == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)


def test_dispose_during_setattr_closes_after_command_returns(
    scene, monkeypatch
):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    slider = FloatSlider(binding, owner, minimum=0, maximum=100)
    original = cmds.setAttr

    def write_and_dispose(*args, **kwargs):
        original(*args, **kwargs)
        binding.dispose()

    monkeypatch.setattr(cmds, "setAttr", write_and_dispose)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(400)
    assert FloatEditUndo._active is None
    monkeypatch.setattr(cmds, "setAttr", original)
    cmds.setAttr(f"{node.cmd_access_name}.ty", 10)
    cmds.undo()
    assert node.translate.translateX.get() == 40
    cmds.undo()
    assert node.translate.translateX.get() == 0


@pytest.mark.parametrize("sample_name", ["maya_plug", "maya_view", "minimal"])
def test_samples_share_sliders_and_release_callbacks_on_close(
    scene, sample_name
):
    from bd_util._sample.maya.ui.float_sample import (
        maya_plug,
        maya_view,
        minimal,
    )

    _, node = scene
    sample = {
        "maya_plug": maya_plug,
        "maya_view": maya_view,
        "minimal": minimal,
    }[sample_name]
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    window = (
        sample.show()
        if sample_name == "minimal"
        else sample.show(node.cmd_access_name)
    )
    try:
        widget = window.widget
        slider = (
            widget.slider
            if sample_name == "minimal"
            else widget.translate_x_slider
        )
        label = (
            widget.value_label
            if sample_name == "minimal"
            else widget.translate_x_label
        )
        spin = (
            widget.spin_box if sample_name == "minimal" else widget.translate_x
        )
        slider.setSliderDown(True)
        slider.setValue(750)
        assert label.text() == spin.text()
        if sample_name == "minimal":
            assert widget.linked_slider.value() == 750
        elif sample_name == "maya_view":
            assert widget.linked_translate_x_slider.value() == 750
        window.close()
        flush()
        assert FloatEditUndo._active is None
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    finally:
        sample.dispose()
        flush()
