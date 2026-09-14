# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.ui import FloatLabel, FloatSliderSpinBox, qt
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal


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


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["tx", "rx", "sx"])
def test_composite_shares_units_history_and_out_of_range_input(
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
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    editor = FloatSliderSpinBox(binding, owner, minimum=-100, maximum=100)
    label = FloatLabel(binding, owner)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    cmds.flushUndo()
    editor.slider.setSliderDown(True)
    for position in (600, 800, 900):
        editor.slider.setValue(position)
        assert binding.value == pytest.approx(plug.get())
        assert editor.spin_box.text() == label.text()
        if source == "python":
            assert data.value == binding.value
    editor.slider.setSliderDown(False)
    assert binding.value == pytest.approx(80)
    editor.spin_box.setValue(binding.view_model.presentation.to_display(140))
    assert editor.slider.value() == 1000
    assert binding.value > 100
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(80)
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(10)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == pytest.approx(80)
    cmds.redo()
    flush()
    assert binding.value > 100
    assert cmds.undoInfo(q=True, redoQueueEmpty=True)


def test_composite_close_finishes_only_its_own_drag(scene):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    first = FloatSliderSpinBox(binding, owner, minimum=0, maximum=100)
    second = FloatSliderSpinBox(binding, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    first.slider.setSliderDown(True)
    first.slider.setValue(300)
    second.close()
    assert binding.view_model.is_editing
    first.close()
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    cmds.setAttr(f"{node.cmd_access_name}.ty", 10)
    cmds.undo()
    assert binding.value == 30
    cmds.undo()
    assert binding.value == 0


def test_maya_lock_keeps_label_copyable_and_dispose_releases_only_editor(
    scene,
):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    editor = FloatSliderSpinBox(binding, owner, minimum=0, maximum=100)
    label = FloatLabel(binding, owner)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
    flush()
    assert not editor.slider.isEnabled()
    assert not editor.spin_box.isEnabled()
    assert label.isEnabled()
    editor.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.setAttr(f"{node.cmd_access_name}.tx", lock=False)
    binding.set_value(3.25)
    assert label.text() == "3.250000 cm"


@pytest.mark.parametrize("sample", ["maya", "python_maya", "python"])
def test_samples_expose_composite_children_and_reopen(scene, sample):
    _, node = scene
    module = {"maya": maya_plug, "python_maya": maya_view, "python": minimal}[
        sample
    ]
    precision = (
        cmds.optionVar(q="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.optionVar(intValue=("channelsPrecision", 4))
    try:
        window = (
            module.show()
            if sample == "python"
            else module.show(node.cmd_access_name)
        )
        widget = window.widget
        editor = (
            widget.editor if sample == "python" else widget.translate_x_editor
        )
        spin = widget.spin_box if sample == "python" else widget.translate_x
        slider = (
            widget.slider if sample == "python" else widget.translate_x_slider
        )
        assert isinstance(editor, FloatSliderSpinBox)
        assert editor.spin_box is spin
        assert editor.slider is slider
        assert spin.decimals() == (3 if sample == "python" else 4)
        editor.slider.setSliderDown(True)
        editor.slider.setValue(750)
        window.close()
        flush()
        assert not qt.isValid(editor)
        assert FloatEditUndo._active is None
        replacement = (
            module.show()
            if sample == "python"
            else module.show(node.cmd_access_name)
        )
        assert replacement is not window
    finally:
        module.dispose()
        if precision is None:
            cmds.optionVar(remove="channelsPrecision")
        else:
            cmds.optionVar(intValue=("channelsPrecision", precision))
        flush()
