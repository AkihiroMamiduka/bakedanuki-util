# coding: utf-8
import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util._sample.maya.ui.float_sample import maya_plug as sample
from bd_util.maya.ui import MayaFloatPlugBinding, get_channel_box_precision
from bd_util.ui import FloatSpinBox, qt


def press_key(widget, key, text=""):
    event = qt.QtGui.QKeyEvent(
        qt.QEvent.Type.KeyPress, key, qt.Qt.KeyboardModifier.NoModifier, text
    )
    qt.QApplication.sendEvent(widget, event)


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    precision = (
        cmds.optionVar(query="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.optionVar(intValue=("channelsPrecision", 6))
    units = cmds.currentUnit(query=True, linear=True), cmds.currentUnit(
        query=True, angle=True
    )
    cmds.currentUnit(linear="cm", angle="deg")
    name = cmds.createNode("transform")
    yield name
    sample.dispose()
    if cmds.objExists(name):
        cmds.delete(name)
    cmds.currentUnit(linear=units[0], angle=units[1])
    if precision is None:
        cmds.optionVar(remove="channelsPrecision")
    else:
        cmds.optionVar(intValue=("channelsPrecision", precision))
    flush()


def test_sample_precision_units_parent_edit_and_window_lifetime(scene):
    cmds.setAttr(scene + ".tx", 100.123456789)
    cmds.setAttr(scene + ".rx", 450.123456789)
    cmds.setAttr(scene + ".sx", -2.123456789)
    node = Nodes().existing.transform(scene)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    window = sample.show(scene)
    widget = window.widget
    assert widget.translate_x_binding.value == pytest.approx(
        100.123456789, rel=1e-14
    )
    assert widget.scale_x.value() == -2.123457
    for view in [widget.translate_x, widget.rotate_x, widget.scale_x]:
        press_key(view, qt.Qt.Key.Key_Return)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.currentUnit(linear="m", angle="rad")
    assert widget.translate_x.suffix() == ""
    assert widget.rotate_x.suffix() == ""
    assert widget.translate_x_editor.minimum_spin_box.suffix() == ""
    assert widget.rotate_x_editor.maximum_spin_box.suffix() == ""
    assert widget.scale_x.suffix() == ""
    assert widget.translate_x.value() == 1.001235
    assert widget.rotate_x.value() == round(
        om.MAngle(450.123456789, om.MAngle.kDegrees).asRadians(), 6
    )
    assert cmds.getAttr(scene + ".sx") == -2.123456789
    widget.translate_x.setValue(2)
    widget.rotate_x.setValue(1)
    assert node.translate.translateX.get() == 200
    assert node.rotate.rotateX.get() == pytest.approx(
        om.MAngle(1, om.MAngle.kRadians).asDegrees()
    )
    cmds.setAttr(scene + ".translate", 3, 4, 5, type="double3")
    flush()
    assert widget.translate_x.value() == 3
    cmds.setAttr(scene + ".translate", lock=True)
    assert not widget.translate_x.isEnabled()
    replacement = sample.show(scene)
    flush()
    assert not qt.isValid(window)
    assert replacement.widget.translate_x.value() == 3
    sample.dispose()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    assert cmds.objExists(scene)


def test_invalid_target_keeps_existing_sample(scene):
    window = sample.show(scene)
    with pytest.raises(Exception):
        sample.show("missingFloatSampleTransform")
    assert qt.isValid(window)
    assert not window.widget.scale_x_binding.is_disposed


@pytest.mark.parametrize("precision", [None, 1, 3, 6, 15])
def test_channel_box_precision_is_read_on_open_without_rounding_scene(
    scene, precision
):
    if precision is None:
        cmds.optionVar(remove="channelsPrecision")
    else:
        cmds.optionVar(intValue=("channelsPrecision", precision))
    decimals = 3 if precision is None else precision
    attributes = [scene + suffix for suffix in (".tx", ".rx", ".sx")]
    for attribute, value in zip(
        attributes, (100.1234567890123, 450.1234567890123, -2.1234567890123)
    ):
        cmds.setAttr(attribute, value)
    before = [cmds.getAttr(attribute) for attribute in attributes]
    cmds.undoInfo(state=True)
    cmds.flushUndo()

    window = sample.show(scene)
    views = [
        window.widget.translate_x,
        window.widget.rotate_x,
        window.widget.scale_x,
    ]
    for view, value in zip(views, before):
        assert view.decimals() == decimals
        assert view.value() == pytest.approx(round(value, decimals), rel=1e-14)
        press_key(view, qt.Qt.Key.Key_Return)
    assert [cmds.getAttr(attribute) for attribute in attributes] == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert bool(cmds.optionVar(exists="channelsPrecision")) == (
        precision is not None
    )

    next_precision = 3 if decimals == 15 else 15
    cmds.optionVar(intValue=("channelsPrecision", next_precision))
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    assert all(view.decimals() == decimals for view in views)
    assert views[0].suffix() == views[1].suffix() == ""

    replacement = sample.show(scene)
    flush()
    assert not qt.isValid(window)
    assert all(
        view.decimals() == next_precision
        for view in (
            replacement.widget.translate_x,
            replacement.widget.rotate_x,
            replacement.widget.scale_x,
        )
    )
    cmds.currentUnit(linear="cm", angle="deg")
    assert [cmds.getAttr(attribute) for attribute in attributes] == before


@pytest.mark.parametrize(
    "flag, value", [("intValue", 0), ("intValue", 16), ("stringValue", "15")]
)
def test_invalid_channel_box_precision_uses_default_without_changing_setting(
    scene, flag, value
):
    cmds.optionVar(**{flag: ("channelsPrecision", value)})
    assert get_channel_box_precision() == 3
    assert cmds.optionVar(query="channelsPrecision") == value


def test_shared_views_and_common_parent_destruction(scene):
    node = Nodes().existing.transform(scene)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QWidget()
    binding = MayaFloatPlugBinding(node.rotate.rotateX, parent=owner)
    first = FloatSpinBox(binding, owner)
    second = FloatSpinBox(binding, owner)
    first.setValue(45)
    assert second.value() == 45
    first.deleteLater()
    flush()
    cmds.currentUnit(angle="rad")
    assert second.value() == round(
        om.MAngle(45, om.MAngle.kDegrees).asRadians(), 6
    )
    owner.deleteLater()
    flush()
    assert binding.is_disposed
    assert not qt.isValid(second)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
