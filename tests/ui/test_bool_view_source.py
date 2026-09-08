# coding: utf-8
from dataclasses import dataclass
import gc
from weakref import ref

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import MayaBoolBinding, resolve_bool_plug
from bd_util.ui import (
    BoolBinding,
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
    qt,
)

_VIEW_TYPES = (
    BoolCheckBox,
    BoolComboBox,
    BoolPushButton,
    BoolRadioButtonGroup,
    BoolStatusLabel,
)


@dataclass
class _Data:
    enabled: bool = True


def _flush(application):
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )
    application.processEvents()
    application.processEvents()


def _assert_value(view, value):
    if isinstance(view, (BoolCheckBox, BoolPushButton)):
        assert view.isChecked() is value
    elif isinstance(view, BoolComboBox):
        assert view.currentData() is value
    elif isinstance(view, BoolRadioButtonGroup):
        assert view.true_button.isChecked() is value
        assert view.false_button.isChecked() is not value
    else:
        assert view.text() == ("On" if value else "Off")


@pytest.mark.parametrize("view_type", _VIEW_TYPES)
def test_binding_and_view_model_inputs_share_state(qt_application, view_type):
    owner = qt.QWidget()
    data = _Data()
    binding = BoolBinding.from_attribute(data, "enabled", parent=owner)
    first = view_type(binding, parent=owner)
    second = view_type(view_model=binding.view_model, parent=owner)
    try:
        assert first.view_model is second.view_model is binding.view_model
        assert binding.parent() is owner
        assert binding.view_model.parent() is binding
        binding.set_value(False)
        assert data.enabled is False
        _assert_value(first, False)
        _assert_value(second, False)
        data.enabled = True
        binding.refresh()
        _assert_value(first, True)
        _assert_value(second, True)
    finally:
        owner.deleteLater()
        _flush(qt_application)


@pytest.mark.parametrize("view_type", _VIEW_TYPES)
def test_view_retains_temporary_binding(qt_application, view_type):
    data = _Data()

    def create_view():
        binding = BoolBinding.from_attribute(data, "enabled")
        return view_type(binding), ref(binding)

    view, binding_ref = create_view()
    gc.collect()
    _flush(qt_application)
    binding = binding_ref()
    try:
        assert binding is not None
        assert not binding.is_disposed
        assert binding.parent() is None
        assert view.view_model is binding.view_model
        view.view_model.set_value_command.execute(False)
        assert data.enabled is False
        _assert_value(view, False)
    finally:
        view.deleteLater()
        _flush(qt_application)
    del view, binding
    gc.collect()
    _flush(qt_application)
    remaining_binding = binding_ref()
    try:
        assert remaining_binding is None
    finally:
        if remaining_binding is not None:
            remaining_binding.dispose()
            _flush(qt_application)


@pytest.mark.parametrize("view_type", _VIEW_TYPES)
@pytest.mark.parametrize("termination", ["dispose", "parent"])
def test_binding_termination_disables_surviving_view(
    qt_application, view_type, termination
):
    owner = qt.QObject()
    binding = BoolBinding.from_attribute(_Data(), "enabled", parent=owner)
    view = view_type(binding)
    if termination == "dispose":
        binding.dispose()
        assert not view.view_model.set_value_command.can_execute
    else:
        owner.deleteLater()
    _flush(qt_application)
    try:
        assert binding.is_disposed
        assert not view.isEnabled()
        with pytest.raises(RuntimeError, match="破棄"):
            _ = view.view_model
    finally:
        if qt.isValid(owner):
            owner.deleteLater()
        view.deleteLater()
        _flush(qt_application)


@pytest.mark.parametrize("view_type", _VIEW_TYPES)
def test_invalid_and_finished_sources_fail_before_widget_creation(
    qt_application, view_type
):
    parent = qt.QWidget()
    binding = BoolBinding.from_attribute(_Data(), "enabled")
    view_model = binding.view_model
    try:
        for source in (None, True, object()):
            with pytest.raises(
                TypeError, match="BoolViewModelまたはBoolBinding"
            ):
                view_type(source, parent=parent)
        binding.dispose()
        with pytest.raises(RuntimeError, match="終了しています"):
            view_type(binding, parent=parent)
        _flush(qt_application)
        with pytest.raises(RuntimeError, match="終了しています"):
            view_type(binding, parent=parent)
        with pytest.raises(RuntimeError, match="破棄"):
            view_type(view_model, parent=parent)
        assert not parent.children()
    finally:
        binding.dispose()
        parent.deleteLater()
        _flush(qt_application)


def test_maya_binding_survives_both_views_closing(
    qt_application, maya_standalone
):
    cmds.file(new=True, force=True)
    name = cmds.createNode("transform")
    plug = resolve_bool_plug(name, "visibility")
    initial_callbacks = tuple(om.MMessage.nodeCallbacks(plug.node.m_obj))
    data = _Data()
    binding = MayaBoolBinding.from_attribute(data, "enabled", maya_plug=plug)
    first_window = qt.QWidget()
    second_window = qt.QWidget()
    first = BoolCheckBox(binding, parent=first_window)
    second = BoolCheckBox(binding, parent=second_window)
    callbacks = tuple(om.MMessage.nodeCallbacks(plug.node.m_obj))
    try:
        assert callbacks != initial_callbacks
        assert binding.parent() is None
        first.click()
        assert not second.isChecked()
        assert not cmds.getAttr(f"{name}.visibility")
        first_window.deleteLater()
        _flush(qt_application)
        assert not binding.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(plug.node.m_obj)) == callbacks
        cmds.setAttr(f"{name}.visibility", True)
        _flush(qt_application)
        assert second.isChecked()
        assert data.enabled
        second_window.deleteLater()
        _flush(qt_application)
        assert not binding.is_disposed
        assert tuple(om.MMessage.nodeCallbacks(plug.node.m_obj)) == callbacks
        assert binding.set_value(False)
        assert not cmds.getAttr(f"{name}.visibility")
        binding.dispose()
        assert (
            tuple(om.MMessage.nodeCallbacks(plug.node.m_obj))
            == initial_callbacks
        )
    finally:
        binding.dispose()
        for window in (first_window, second_window):
            if qt.isValid(window):
                window.deleteLater()
        _flush(qt_application)
        cmds.file(new=True, force=True)
