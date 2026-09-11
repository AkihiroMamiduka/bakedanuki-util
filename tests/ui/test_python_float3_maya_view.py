# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaFloat3Binding, MayaFloat3PlugView
from bd_util.ui import Float3Binding, Float3SpinBox, FloatPresentation, qt
from bd_util._sample.maya.ui.float3_sample import maya_view
from bd_util._sample.maya.ui.float3_sample.data import TransformFloat3Data


@dataclass
class Data:
    value: tuple = (1.23456789123, 2.3456789123, 3.456789123)


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


def test_shared_widgets_units_pending_input_and_unedited_enter_preserve_precision(
    node,
):
    data = Data()
    initial = data.value
    binding = MayaFloat3Binding.from_attribute(
        data,
        "value",
        maya_plug=node.translate,
        presentation=FloatPresentation(minimum=-500, maximum=500),
    )
    first = Float3SpinBox(binding, decimals=3)
    second = Float3SpinBox(binding.view_model, decimals=6)
    try:
        assert first.x_spin_box.value() == 1.235
        assert second.x_spin_box.value() == 1.234568
        qt.QApplication.sendEvent(
            first.x_spin_box,
            qt.QtGui.QKeyEvent(
                qt.QEvent.Type.KeyPress,
                qt.Qt.Key.Key_Return,
                qt.Qt.KeyboardModifier.NoModifier,
            ),
        )
        assert data.value == initial
        cmds.currentUnit(linear="m")
        assert first.x_spin_box.suffix() == second.z_spin_box.suffix() == " m"
        assert first.y_spin_box.minimum() == -5
        assert first.z_spin_box.maximum() == 5
        assert data.value == initial
        first.x_spin_box.setValue(2.5)
        assert data.value == (250, initial[1], initial[2])
        assert second.x_spin_box.value() == 2.5
        assert tuple(node.translate.get()) == data.value
        # 単位変更は直前のMaya入力を消さず、Pythonはcmのまま保持する。
        cmds.setAttr(
            f"{node.cmd_access_name}.translate",
            1.25,
            2.5,
            3.75,
            type="double3",
        )
        cmds.currentUnit(linear="cm")
        flush()
        assert data.value == (125, 250, 375)
        assert second.z_spin_box.value() == 375
        first.deleteLater()
        flush()
        assert not binding.is_disposed
        assert binding.set_value((10, 20, 30))
        assert second.y_spin_box.value() == 20
    finally:
        if qt.isValid(first):
            first.deleteLater()
        second.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("failure", [False, True])
def test_constructor_failure_or_owner_destruction_releases_all_callbacks(
    node, failure
):
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QWidget()
    if failure:
        cmds.setAttr(f"{node.cmd_access_name}.ty", lock=True)
        with pytest.raises(RuntimeError):
            MayaFloat3Binding.from_attribute(
                Data(), "value", maya_plug=node.translate, parent=owner
            )
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        assert tuple(node.translate.get()) == (0, 0, 0)
        flush()
        assert not owner.children()
    else:
        data = Data()
        binding = MayaFloat3Binding.from_attribute(
            data, "value", maya_plug=node.translate, parent=owner
        )
        child = Float3SpinBox(binding, owner)
        survivor = Float3SpinBox(binding)
        cmds.setAttr(
            f"{node.cmd_access_name}.translate", 50, 60, 70, type="double3"
        )
    owner.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    if not failure:
        assert binding.is_disposed
        assert data.value == Data().value
        assert not qt.isValid(child)
        assert not survivor.x_spin_box.isEnabled()
        survivor.deleteLater()
        binding.dispose()
        flush()


def test_separate_view_owner_destruction_keeps_python_editable_and_allows_replacement(
    node,
):
    source = Float3Binding.from_attribute(
        Data(),
        "value",
        presentation=FloatPresentation(scale=2, suffix=" units"),
    )
    owner = qt.QObject()
    view = MayaFloat3PlugView(source.view_model, node.translate, owner)
    spin = Float3SpinBox(source)
    before = tuple(node.translate.get())
    try:
        assert spin.y_spin_box.suffix() == " cm"
        owner.deleteLater()
        flush()
        assert view.is_disposed
        source.refresh()
        assert spin.y_spin_box.suffix() == " units"
        assert spin.y_spin_box.isEnabled()
        assert source.set_value((10, 20, 30))
        assert tuple(node.translate.get()) == before
        assert spin.z_spin_box.value() == 60
        replacement = MayaFloat3PlugView(
            source.view_model, node.translate, source
        )
        assert replacement.is_synchronized
        assert tuple(node.translate.get()) == (10, 20, 30)
    finally:
        spin.deleteLater()
        source.dispose()
        flush()


@pytest.mark.parametrize("dispose_from", ["changed", "sync_failed"])
def test_user_signal_may_dispose_binding_during_sync(node, dispose_from):
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    data = Data()
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    spin = Float3SpinBox(binding)
    if dispose_from == "sync_failed":
        binding.maya_view.sync_failed.connect(lambda _error: binding.dispose())
        cmds.setAttr(f"{node.cmd_access_name}.ty", lock=True)
    else:
        binding.changed.connect(lambda _value: binding.dispose())
    try:
        binding.set_value((10, 20, 30))
        assert binding.is_disposed
        assert data.value == (10, 20, 30)
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        assert not spin.x_spin_box.isEnabled()
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_reentrant_python_command_during_maya_input_uses_latest_tuple(node):
    data = Data()
    binding = MayaFloat3Binding.from_attribute(
        data, "value", maya_plug=node.translate
    )
    spin = Float3SpinBox(binding)

    def replace(value):
        if value == (10, 20, 30):
            binding.set_value((40, 50, 60))

    binding.changed.connect(replace)
    try:
        cmds.setAttr(
            f"{node.cmd_access_name}.translate", 10, 20, 30, type="double3"
        )
        flush()
        assert (
            data.value
            == binding.value
            == tuple(node.translate.get())
            == (40, 50, 60)
        )
        assert spin.x_spin_box.value() == 40
        assert binding.maya_view.is_synchronized
    finally:
        spin.deleteLater()
        binding.dispose()
        flush()


def test_sample_initial_values_precision_refresh_retry_close_and_reopen(node):
    data = TransformFloat3Data()
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
        assert widget.translate_binding.store.instance is data
        assert widget.translate.x_spin_box.decimals() == 4
        assert widget.rotate.y_spin_box.decimals() == 4
        assert widget.scale.z_spin_box.decimals() == 4
        assert widget.linked_translate.x_spin_box.decimals() == 6
        assert tuple(node.translate.get()) == data.translate
        widget.translate.x_spin_box.setValue(7.125)
        assert (
            data.translate[0]
            == widget.linked_translate.x_spin_box.value()
            == 7.125
        )
        widget.set_data_button.click()
        assert data.translate == (10, 20, 30)
        assert node.translate.translateX.get() == 7.125
        widget.refresh_button.click()
        assert tuple(node.translate.get()) == (10, 20, 30)
        assert tuple(node.rotate.get()) == pytest.approx((20, 40, 60))
        assert tuple(node.scale.get()) == (2, 3, 4)
        cmds.currentUnit(linear="m", angle="rad")
        assert widget.translate.x_spin_box.suffix() == " m"
        assert widget.rotate.y_spin_box.suffix() == " rad"
        cmds.setAttr(f"{node.cmd_access_name}.ty", lock=True)
        widget.translate_binding.set_value((50, 60, 70))
        widget.retry_button.click()
        assert "Pending" in widget.result_label.text()
        assert tuple(node.translate.get()) == (10, 20, 30)
        cmds.setAttr(f"{node.cmd_access_name}.ty", lock=False)
        widget.retry_button.click()
        assert "Pending" not in widget.result_label.text()
        window.close()
        flush()
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
        assert data.translate == (50, 60, 70)
        assert cmds.objExists(node.cmd_access_name)
        replacement = maya_view.show(node.cmd_access_name, data)
        assert replacement.widget.data is data
        assert replacement.widget.translate_binding.value == (50, 60, 70)
    finally:
        maya_view.dispose()
        if old_precision is None:
            cmds.optionVar(remove="channelsPrecision")
        else:
            cmds.optionVar(intValue=("channelsPrecision", old_precision))
        flush()


def test_sample_partial_constructor_failure_releases_completed_bindings(node):
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    cmds.setAttr(f"{node.cmd_access_name}.ry", lock=True)
    with pytest.raises(RuntimeError):
        maya_view.show(node.cmd_access_name)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    flush()
