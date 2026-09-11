# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaFloatBinding, MayaFloatPlugView
from bd_util.ui import FloatBinding, FloatPresentation, FloatSpinBox, qt
from bd_util._sample.maya.ui.float_sample import maya_view
from bd_util._sample.maya.ui.float_sample.data import TransformFloatData


@dataclass
class Data:
    value: float = 1.23456789123


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
    maya_view.dispose()
    cmds.currentUnit(linear=units[0], angle=units[1])
    flush()


def test_shared_widgets_units_and_unedited_enter_preserve_python_precision(
    node,
):
    data = Data()
    binding = MayaFloatBinding.from_attribute(
        data,
        "value",
        maya_plug=node.translate.translateX,
        presentation=FloatPresentation(minimum=-500, maximum=500),
    )
    first = FloatSpinBox(binding, decimals=3)
    second = FloatSpinBox(binding.view_model, decimals=6)
    try:
        assert first.value() == 1.235
        assert second.value() == 1.234568
        for view in (first, second):
            qt.QApplication.sendEvent(
                view,
                qt.QtGui.QKeyEvent(
                    qt.QEvent.Type.KeyPress,
                    qt.Qt.Key.Key_Return,
                    qt.Qt.KeyboardModifier.NoModifier,
                ),
            )
        assert data.value == 1.23456789123
        cmds.currentUnit(linear="m")
        assert first.suffix() == second.suffix() == " m"
        assert first.minimum() == -5
        assert first.maximum() == 5
        assert data.value == 1.23456789123
        first.setValue(2.5)
        assert data.value == 250
        assert second.value() == 2.5
        assert node.translate.translateX.get() == 250
        first.deleteLater()
        flush()
        assert not binding.is_disposed
        cmds.setAttr(f"{node.cmd_access_name}.tx", 1.25)
        flush()
        assert data.value == 125
        assert second.value() == 1.25
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("failure", [False, True])
def test_constructor_failure_or_owner_destruction_releases_callbacks(
    node, failure
):
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QWidget()
    if failure:
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
        with pytest.raises(RuntimeError):
            MayaFloatBinding.from_attribute(
                Data(),
                "value",
                maya_plug=node.translate.translateX,
                parent=owner,
            )
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        flush()
        assert not owner.children()
    else:
        data = Data()
        binding = MayaFloatBinding.from_attribute(
            data, "value", maya_plug=node.translate.translateX, parent=owner
        )
        child = FloatSpinBox(binding, owner)
        survivor = FloatSpinBox(binding)
        cmds.setAttr(f"{node.cmd_access_name}.tx", 50)
    owner.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    if not failure:
        assert binding.is_disposed
        assert data.value == 1.23456789123
        assert not qt.isValid(child)
        assert not survivor.isEnabled()
        survivor.deleteLater()
        binding.dispose()
        flush()


def test_separate_maya_view_owner_restores_python_units_without_disabling_input(
    node,
):
    binding = FloatBinding.from_attribute(
        Data(),
        "value",
        presentation=FloatPresentation(scale=2, suffix=" units"),
    )
    owner = qt.QObject()
    view = MayaFloatPlugView(
        binding.view_model, node.translate.translateX, owner
    )
    spin = FloatSpinBox(binding)
    try:
        assert spin.suffix() == " cm"
        owner.deleteLater()
        flush()
        assert view.is_disposed
        assert spin.isEnabled()
        # 次の明示refreshでPython側の表示情報も再評価する。
        binding.refresh()
        assert spin.suffix() == " units"
        assert binding.set_value(10)
        assert spin.value() == 20
        assert node.translate.translateX.get() == 1.23456789123
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("dispose_from", ["changed", "sync_failed"])
def test_user_notification_can_dispose_binding(node, dispose_from):
    data = Data()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.translate.translateX
    )
    spin = FloatSpinBox(binding)
    before = len(tuple(om.MMessage.nodeCallbacks(node.m_obj)))
    if dispose_from == "sync_failed":
        binding.maya_view.sync_failed.connect(lambda _error: binding.dispose())
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
    else:
        binding.changed.connect(lambda _value: binding.dispose())
    try:
        binding.set_value(10)
        assert binding.is_disposed
        assert len(tuple(om.MMessage.nodeCallbacks(node.m_obj))) < before
        assert data.value == 10
        assert not spin.isEnabled()
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_reentrant_python_command_during_maya_input_keeps_latest_value(node):
    data = Data()
    binding = MayaFloatBinding.from_attribute(
        data, "value", maya_plug=node.scale.scaleX
    )
    spin = FloatSpinBox(binding)

    def replace(value):
        if value == 10:
            binding.set_value(20)

    binding.changed.connect(replace)
    try:
        cmds.setAttr(f"{node.cmd_access_name}.sx", 10)
        flush()
        assert binding.value == data.value == node.scale.scaleX.get() == 20
        assert spin.value() == 20
        assert binding.maya_view.is_synchronized
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_sample_python_initial_value_shared_views_refresh_retry_and_reopen(
    node,
):
    data = TransformFloatData()
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    old_precision = (
        cmds.optionVar(q="channelsPrecision")
        if cmds.optionVar(exists="channelsPrecision")
        else None
    )
    cmds.optionVar(intValue=("channelsPrecision", 4))
    try:
        window = maya_view.show(node.cmd_access_name, data)
        widget = window.widget
        assert widget.translate_x_binding.store.instance is data
        assert widget.translate_x.decimals() == 4
        assert widget.rotate_x.decimals() == 4
        assert widget.scale_x.decimals() == 4
        assert widget.linked_translate_x.decimals() == 6
        assert node.translate.translateX.get() == data.translate_x
        widget.translate_x.setValue(7.125)
        assert data.translate_x == widget.linked_translate_x.value() == 7.125
        widget.set_data_button.click()
        assert data.translate_x == 10
        assert node.translate.translateX.get() == 7.125
        widget.refresh_button.click()
        assert node.translate.translateX.get() == 10
        assert node.rotate.rotateX.get() == 20
        assert node.scale.scaleX.get() == 2
        cmds.currentUnit(linear="m", angle="rad")
        assert widget.translate_x.suffix() == " m"
        assert widget.rotate_x.suffix() == " rad"
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=True)
        widget.translate_x_binding.set_value(50)
        widget.retry_button.click()
        assert "Pending" in widget.result_label.text()
        cmds.setAttr(f"{node.cmd_access_name}.tx", lock=False)
        widget.retry_button.click()
        assert "Pending" not in widget.result_label.text()
        window.close()
        flush()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        assert data.translate_x == 50
        assert cmds.objExists(node.cmd_access_name)
        replacement = maya_view.show(node.cmd_access_name, data)
        assert replacement.widget.data is data
        assert replacement.widget.translate_x_binding.value == 50
    finally:
        maya_view.dispose()
        if old_precision is None:
            cmds.optionVar(remove="channelsPrecision")
        else:
            cmds.optionVar(intValue=("channelsPrecision", old_precision))
        flush()


def test_sample_partial_initialization_releases_completed_bindings(node):
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    cmds.setAttr(f"{node.cmd_access_name}.rx", lock=True)
    with pytest.raises(RuntimeError):
        maya_view.show(node.cmd_access_name)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    flush()
