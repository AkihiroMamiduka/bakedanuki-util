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
from bd_util.ui import Float3Label, Float3SpinBox, qt
from bd_util._sample.maya.ui.float3_sample import maya_plug, maya_view, minimal


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def texts(view):
    return tuple(
        label.text() for label in (view.x_label, view.y_label, view.z_label)
    )


def spin_texts(view):
    return tuple(
        spin.text()
        + ("" if spin.isUnitVisible() else spin.view_model.presentation.suffix)
        for spin in (view.x_spin_box, view.y_spin_box, view.z_spin_box)
    )


@pytest.fixture
def scene(qt_application, maya_standalone):
    cmds.file(new=True, force=True)
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo = cmds.undoInfo(q=True, state=True)
    precision = (
        cmds.optionVar(q="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    owner = qt.QWidget()
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield owner, node
    for sample in (maya_plug, maya_view, minimal):
        sample.dispose()
    owner.deleteLater()
    flush()
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo)
    if precision is None:
        cmds.optionVar(remove="channelsPrecision")
    else:
        cmds.optionVar(intValue=("channelsPrecision", precision))


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize(
    "attribute,values,expected",
    [
        ("translate", (100, 200, 300), ("1.000 m", "2.000 m", "3.000 m")),
        ("rotate", (90, 180, 270), ("1.571 rad", "3.142 rad", "4.712 rad")),
        ("scale", (1, 2, 3), ("1.000", "2.000", "3.000")),
    ],
)
def test_units_axis_and_compound_edits_undo_redo_and_label_has_no_writes(
    scene, source, attribute, values, expected
):
    owner, node = scene

    @dataclass
    class Data:
        value: tuple[float, float, float] = values

    path = f"{node.cmd_access_name}.{attribute}"
    cmds.setAttr(path, *values, type="double3")
    plug = resolve_float3_plug(node.cmd_access_name, attribute)
    binding = (
        MayaFloat3PlugBinding(plug, parent=owner)
        if source == "maya"
        else MayaFloat3Binding.from_attribute(
            Data(), "value", maya_plug=plug, parent=owner
        )
    )
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    label = Float3Label(binding, owner, decimals=3)
    spin = Float3SpinBox(binding, owner, decimals=3)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    assert texts(label) == spin_texts(spin) == expected
    original = binding.value
    cmds.flushUndo()
    label.setDecimals(6)
    binding.refresh()
    label.setDecimals(3)
    assert binding.value == pytest.approx(original)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    spin.y_spin_box.setValue(0.125)
    flush()
    assert texts(label) == spin_texts(spin)
    assert texts(label)[0] == expected[0]
    assert texts(label)[2] == expected[2]
    assert binding.value[0] == pytest.approx(original[0])
    assert binding.value[2] == pytest.approx(original[2])
    cmds.undo()
    flush()
    assert texts(label) == expected
    cmds.redo()
    flush()
    assert label.y_label.text().startswith("0.125")
    binding.set_value((4, 5, 6))
    assert texts(label) == spin_texts(spin)
    assert binding.value == pytest.approx((4, 5, 6))
    cmds.setAttr(path, 7, 8, 9, type="double3")
    flush()
    assert texts(label) == spin_texts(spin)
    assert label.x_label.text().startswith("7.000")


def test_parent_lock_connection_and_view_destruction_keep_labels_live(scene):
    owner, node = scene
    path = f"{node.cmd_access_name}.translate"
    binding = MayaFloat3PlugBinding(node.translate, parent=owner)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    label = Float3Label(binding, owner, decimals=3)
    other = Float3Label(binding, owner, decimals=3)
    spin = Float3SpinBox(binding, owner)
    cmds.setAttr(path, lock=True)
    flush()
    assert not spin.x_spin_box.isEnabled()
    for value in (label.x_label, label.y_label, label.z_label):
        assert value.isEnabled()
        value.setSelection(0, len(value.text()))
        assert value.selectedText() == "0.000 cm"
    cmds.setAttr(path, lock=False)
    source = cmds.createNode("transform")
    cmds.connectAttr(f"{source}.translate", path)
    cmds.setAttr(f"{source}.translate", 1, 2, 3, type="double3")
    flush()
    assert texts(label) == ("1.000 cm", "2.000 cm", "3.000 cm")
    assert not spin.y_spin_box.isEnabled()
    label.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.setAttr(f"{source}.ty", 5)
    flush()
    assert other.y_label.text() == "5.000 cm"
    assert not binding.is_disposed
    binding.dispose()
    flush()
    assert not other.y_label.isEnabled()
    assert not tuple(om.MMessage.nodeCallbacks(node.m_obj))


def test_python_authority_is_shown_during_pending_maya_sync(scene):
    owner, node = scene

    @dataclass
    class Data:
        value: tuple[float, float, float] = (1, 2, 3)

    binding = MayaFloat3Binding.from_attribute(
        Data(), "value", maya_plug=node.translate, parent=owner
    )
    label = Float3Label(binding, owner, decimals=3)
    cmds.setAttr(f"{node.cmd_access_name}.translate", lock=True)
    flush()
    binding.set_value((4.125, 5.25, 6.5))
    assert texts(label) == ("4.125 cm", "5.250 cm", "6.500 cm")
    assert not binding.maya_view.is_synchronized
    assert cmds.getAttr(f"{node.cmd_access_name}.translate")[0] == (1, 2, 3)
    cmds.setAttr(f"{node.cmd_access_name}.translate", lock=False)
    flush()
    assert binding.maya_view.is_synchronized
    assert cmds.getAttr(f"{node.cmd_access_name}.translate")[0] == (
        4.125,
        5.25,
        6.5,
    )
    binding.dispose()
    assert texts(label) == ("4.125", "5.250", "6.500")
    assert not label.z_label.isEnabled()


@pytest.mark.parametrize("sample", [maya_plug, maya_view])
@pytest.mark.parametrize("precision", [3, 15])
def test_samples_share_labels_channel_precision_and_reopen(
    scene, sample, precision
):
    _, node = scene
    cmds.optionVar(intValue=("channelsPrecision", precision))
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    window = sample.show(node.cmd_access_name)
    widget = window.widget
    for spin, label in (
        (widget.translate, widget.translate_label),
        (widget.rotate, widget.rotate_label),
        (widget.scale, widget.scale_label),
    ):
        assert label.decimals() == precision
        assert texts(label) == spin_texts(spin)
    widget.translate.y_spin_box.setValue(5.125)
    assert widget.translate_label.y_label.text() == f"{5.125:.{precision}f} cm"
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    assert texts(widget.translate_label) == spin_texts(widget.translate)
    assert texts(widget.rotate_label) == spin_texts(widget.rotate)
    if sample is maya_view:
        assert widget.linked_translate_label.decimals() == 6
        previous = texts(widget.translate_label)
        widget.set_data_button.click()
        assert texts(widget.translate_label) == previous
        widget.refresh_button.click()
        assert texts(widget.translate_label) == spin_texts(widget.translate)
        assert texts(widget.linked_translate_label) == (
            "0.100000 m",
            "0.200000 m",
            "0.300000 m",
        )
    window.close()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    assert not qt.isValid(widget.translate_label)
    replacement = sample.show(node.cmd_access_name)
    assert qt.isValid(replacement.widget.translate_label)


def test_minimal_sample_labels_follow_edits_and_explicit_refresh(scene):
    window = minimal.show()
    widget = window.widget
    assert widget.value_label.decimals() == 3
    assert widget.linked_value_label.decimals() == 6
    assert texts(widget.value_label) == spin_texts(widget.spin_box)
    widget.spin_box.x_spin_box.setValue(0.125)
    assert widget.value_label.x_label.text() == "0.125"
    assert widget.linked_value_label.x_label.text() == "0.125000"
    widget.set_value_button.click()
    assert texts(widget.value_label) == ("4.000", "5.000", "6.000")
    widget.set_data_button.click()
    assert texts(widget.value_label) == ("4.000", "5.000", "6.000")
    widget.refresh_button.click()
    assert texts(widget.value_label) == ("7.000", "8.000", "9.000")
    assert texts(widget.linked_value_label) == (
        "7.000000",
        "8.000000",
        "9.000000",
    )
