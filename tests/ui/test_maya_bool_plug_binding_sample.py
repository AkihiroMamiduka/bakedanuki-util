# coding: utf-8
import gc
from weakref import ref

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util._sample.maya.ui.bool_sample import maya_plug
from bd_util.maya.ui import MayaBoolPlugBinding
from bd_util.ui import (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    qt,
)


def _flush(application):
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )
    application.processEvents()
    application.processEvents()


@pytest.mark.parametrize(
    "view_type",
    [
        BoolCheckBox,
        BoolComboBox,
        BoolPushButton,
        BoolRadioButtonGroup,
        BoolStatusLabel,
    ],
)
def test_plug_binding_supports_all_views_and_common_parent_destruction(
    qt_application, maya_standalone, view_type
):
    name = cmds.createNode("transform")
    node = Nodes().existing.transform(name)
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QWidget()
    binding = MayaBoolPlugBinding(node.visibility, parent=owner)
    view = view_type(binding, parent=owner)
    assert view.view_model is binding.view_model
    binding.set_value(False)
    assert not view.view_model.value.value
    owner.deleteLater()
    _flush(qt_application)
    assert binding.is_disposed
    assert not qt.isValid(view)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
    cmds.delete(name)


def test_shared_plug_binding_outlives_both_windows(
    qt_application, maya_standalone
):
    name = cmds.createNode("transform")
    node = Nodes().existing.transform(name)
    binding = MayaBoolPlugBinding(node.visibility)
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    first_window = qt.QWidget()
    second_window = qt.QWidget()
    first = BoolCheckBox(binding, parent=first_window)
    second = BoolCheckBox(binding, parent=second_window)
    try:
        first.click()
        assert not second.isChecked()
        first_window.deleteLater()
        _flush(qt_application)
        assert not binding.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
        cmds.setAttr(f"{name}.visibility", True)
        _flush(qt_application)
        assert second.isChecked()
        cmds.setAttr(f"{name}.visibility", lock=True)
        _flush(qt_application)
        assert not second.isEnabled()
        cmds.setAttr(f"{name}.visibility", lock=False)
        _flush(qt_application)
        assert second.isEnabled()
        second_window.deleteLater()
        _flush(qt_application)
        assert binding.set_value(False)
        assert not cmds.getAttr(f"{name}.visibility")
    finally:
        binding.dispose()
        for window in (first_window, second_window):
            if qt.isValid(window):
                window.deleteLater()
        _flush(qt_application)
        cmds.delete(name)


def test_temporary_plug_binding_ends_with_its_explicit_owner(
    qt_application, maya_standalone
):
    name = cmds.createNode("transform")
    node = Nodes().existing.transform(name)
    callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    owner = qt.QObject()

    def create_view():
        binding = MayaBoolPlugBinding(node.visibility, parent=owner)
        return BoolCheckBox(binding), ref(binding)

    view, binding_ref = create_view()
    try:
        gc.collect()
        view.click()
        assert not cmds.getAttr(f"{name}.visibility")
        assert binding_ref() is not None
        view.deleteLater()
        _flush(qt_application)
        del view
        gc.collect()
        _flush(qt_application)
        binding = binding_ref()
        assert binding is not None
        assert not binding.is_disposed
        # Maya callbackの終了責任はViewではなく、明示したownerにある。
        owner.deleteLater()
        _flush(qt_application)
        assert binding.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == callbacks
    finally:
        remaining_binding = binding_ref()
        if remaining_binding is not None:
            remaining_binding.dispose()
        if qt.isValid(owner):
            owner.deleteLater()
        _flush(qt_application)
        cmds.delete(name)


def test_maya_plug_sample_preserves_scene_and_replaces_window(
    qt_application, maya_standalone
):
    first_name = cmds.createNode("transform")
    second_name = cmds.createNode("transform")
    first_node = Nodes().existing.transform(first_name)
    callbacks = tuple(om.MMessage.nodeCallbacks(first_node.m_obj))
    cmds.setAttr(f"{first_name}.visibility", False)
    try:
        first = maya_plug.show(first_name)
        binding = first.widget.binding
        assert not first.widget.check_box.isChecked()
        assert first.widget.status_label.text() == "Off"
        first.widget.check_box.click()
        assert cmds.getAttr(f"{first_name}.visibility")
        assert first.widget.status_label.text() == "On"
        with pytest.raises(AttributeError):
            maya_plug.show(first_name, "missingBool")
        assert not binding.is_disposed
        second = maya_plug.show(second_name)
        _flush(qt_application)
        assert second is not first
        assert binding.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(first_node.m_obj)) == callbacks
        second_binding = second.widget.binding
        second.close()
        _flush(qt_application)
        assert second_binding.is_disposed
        reopened = maya_plug.show(first_name)
        assert reopened.widget.check_box.isChecked()
        maya_plug.dispose()
        _flush(qt_application)
        assert cmds.objExists(first_name)
        assert cmds.objExists(second_name)
    finally:
        maya_plug.dispose()
        _flush(qt_application)
        cmds.delete(first_name, second_name)
