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
from bd_util.ui import FloatLabel, FloatSpinBox, qt
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def node(qt_application, maya_standalone):
    cmds.file(new=True, force=True)
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    cmds.currentUnit(linear="cm", angle="deg")
    yield Nodes().existing.transform(cmds.createNode("transform"))
    for sample in (maya_plug, maya_view, minimal):
        sample.dispose()
    cmds.currentUnit(linear=units[0], angle=units[1])
    flush()


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize(
    "attribute,expected",
    [("tx", "1.000 m"), ("rx", "1.745 rad"), ("sx", "100.000")],
)
def test_units_external_input_and_history_are_shared_without_label_writes(
    node, source, attribute, expected
):
    @dataclass
    class Data:
        value: float = 100

    path = f"{node.cmd_access_name}.{attribute}"
    cmds.setAttr(path, 100)
    data = Data()
    plug = resolve_float_plug(node.cmd_access_name, attribute)
    binding = (
        MayaFloatPlugBinding(plug)
        if source == "maya"
        else MayaFloatBinding.from_attribute(data, "value", maya_plug=plug)
    )
    label = FloatLabel(binding, decimals=3)
    spin = FloatSpinBox(binding, decimals=3)
    try:
        cmds.undoInfo(state=True)
        cmds.currentUnit(linear="m", angle="rad")
        flush()
        assert label.text() == spin.text() == expected
        cmds.flushUndo()
        label.setDecimals(6)
        binding.refresh()
        flush()
        assert cmds.undoInfo(q=True, undoQueueEmpty=True)
        assert binding.value == pytest.approx(100)
        assert data.value == 100
        label.setDecimals(3)
        cmds.setAttr(path, 2.5)
        flush()
        assert label.text() == spin.text()
        assert label.text().startswith("2.500")
        cmds.undo()
        flush()
        assert label.text() == expected
        assert not cmds.undoInfo(q=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert label.text().startswith("2.500")
    finally:
        label.deleteLater()
        spin.deleteLater()
        binding.dispose()
        flush()


def test_maya_locked_and_connected_values_remain_selectable_and_current(node):
    path = f"{node.cmd_access_name}.tx"
    binding = MayaFloatPlugBinding(node.translate.translateX)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    label = FloatLabel(binding, decimals=3)
    spin = FloatSpinBox(binding)
    try:
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        cmds.setAttr(path, lock=True)
        flush()
        assert not spin.isEnabled()
        assert label.isEnabled()
        label.setSelection(0, len(label.text()))
        assert label.selectedText() == "0.000 cm"
        cmds.setAttr(path, lock=False)
        source = cmds.createNode("transform")
        cmds.setAttr(f"{source}.tx", 12.25)
        cmds.connectAttr(f"{source}.tx", path)
        flush()
        assert not spin.isEnabled()
        assert label.isEnabled()
        assert label.text() == "12.250 cm"
        cmds.setAttr(f"{source}.tx", 25.5)
        flush()
        assert label.text() == "25.500 cm"
        label.deleteLater()
        flush()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    finally:
        if qt.isValid(label):
            label.deleteLater()
        spin.deleteLater()
        binding.dispose()
        flush()


def test_python_label_shows_authoritative_value_while_maya_sync_is_pending(
    node,
):
    @dataclass
    class Data:
        value: float = 1

    data = Data()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.translate.translateX
    )
    label = FloatLabel(binding, decimals=3)
    try:
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
        flush()
        binding.set_value(5.125)
        assert not binding.maya_view.is_synchronized
        assert label.text() == "5.125 cm"
        assert node.translate.translateX.get() == 1
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=False)
        flush()
        assert node.translate.translateX.get() == 5.125
        assert binding.maya_view.is_synchronized
        binding.dispose()
        # Maya Viewの解除でPython側の単位へ戻ってから、Bindingが終了する。
        assert label.text() == "5.125"
        assert not label.isEnabled()
    finally:
        label.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("source", ["maya", "python"])
def test_transform_samples_share_labels_channel_precision_and_reopen(
    node, source
):
    old_precision = (
        cmds.optionVar(q="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.optionVar(intValue=("channelsPrecision", 4))
    data = TransformFloatData()
    sample = maya_plug if source == "maya" else maya_view
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    try:
        window = (
            maya_plug.show(node.cmd_access_name)
            if source == "maya"
            else maya_view.show(node.cmd_access_name, data)
        )
        widget = window.widget
        for spin, label in (
            (widget.translate_x, widget.translate_x_label),
            (widget.rotate_x, widget.rotate_x_label),
            (widget.scale_x, widget.scale_x_label),
        ):
            assert label.decimals() == 4
            assert spin.suffix() == ""
            assert (
                label.text()
                == spin.text() + spin.view_model.presentation.suffix
            )
        widget.translate_x.setValue(5.125)
        assert widget.translate_x_label.text() == "5.1250 cm"
        cmds.currentUnit(linear="m", angle="rad")
        assert widget.translate_x_label.text() == "0.0513 m"
        assert widget.rotate_x_label.text() == widget.rotate_x.text() + " rad"
        if source == "python":
            assert widget.linked_translate_x_label.decimals() == 6
            widget.set_data_button.click()
            assert widget.translate_x_label.text() == "0.0513 m"
            widget.refresh_button.click()
            assert widget.translate_x_label.text() == "0.1000 m"
        window.close()
        flush()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        assert not qt.isValid(widget.translate_x_label)
        replacement = sample.show(node.cmd_access_name)
        assert qt.isValid(replacement.widget.translate_x_label)
    finally:
        sample.dispose()
        if old_precision is None:
            cmds.optionVar(remove="channelsPrecision")
        else:
            cmds.optionVar(intValue=("channelsPrecision", old_precision))
        flush()


def test_python_sample_labels_follow_edits_and_explicit_refresh(node):
    window = minimal.show()
    widget = window.widget
    try:
        assert widget.value_label.text() == "0.123"
        assert widget.linked_value_label.text() == "0.123457"
        widget.spin_box.setValue(0.75)
        assert widget.value_label.text() == "0.750"
        assert widget.linked_value_label.text() == "0.750000"
        widget.set_data_button.click()
        assert widget.value_label.text() == "0.750"
        widget.refresh_button.click()
        assert widget.value_label.text() == "0.250"
        assert widget.linked_value_label.text() == "0.250000"
    finally:
        minimal.dispose()
        flush()
