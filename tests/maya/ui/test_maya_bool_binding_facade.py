# coding: utf-8
"""Maya用bool組み立てAPIと名前解決の回帰テスト。"""

from dataclasses import dataclass

import pytest
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.maya.ui import MayaBoolBinding, resolve_bool_plug
from bd_util.ui import qt


@dataclass
class _Data:
    enabled: bool = False


def _process_events() -> None:
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QtCore.QEvent.Type.DeferredDelete
    )


def test_maya_binding_syncs_and_dispose_cancels_pending_input(
    new_scene, maya_cmds
):
    name = maya_cmds.createNode("transform")
    node = Nodes().existing.transform(name)
    data = _Data()
    initial_callbacks = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    binding = MayaBoolBinding.from_attribute(
        data, "enabled", maya_plug=node.visibility
    )
    view_model = binding.view_model
    view = binding.maya_view
    assert view is not None
    try:
        assert view.parent() is binding
        assert view.is_synchronized
        assert not maya_cmds.getAttr(f"{name}.visibility")
        assert binding.set_value(True)
        assert maya_cmds.getAttr(f"{name}.visibility")
        maya_cmds.undo()
        _process_events()
        assert data.enabled is False
        maya_cmds.redo()
        _process_events()
        assert data.enabled is True
        maya_cmds.setAttr(f"{name}.visibility", False)
        _process_events()
        assert data.enabled is False
        maya_cmds.setAttr(f"{name}.visibility", True)
        binding.dispose()
        assert view.is_disposed
        assert (
            tuple(om.MMessage.nodeCallbacks(node.m_obj)) == initial_callbacks
        )
        assert not view_model.set_value_command.execute(True)
        _process_events()
        assert data.enabled is False
        assert maya_cmds.objExists(name)
    finally:
        binding.dispose()
        _process_events()


def test_maya_binding_exposes_sync_failure_and_keeps_python_editable(
    new_scene, maya_cmds
):
    name = maya_cmds.createNode("transform")
    binding = MayaBoolBinding.from_attribute(
        _Data(), "enabled", maya_plug=resolve_bool_plug(name, "visibility")
    )
    view = binding.maya_view
    assert view is not None
    try:
        maya_cmds.setAttr(f"{name}.visibility", lock=True)
        assert binding.set_value(True)
        assert binding.value
        assert not view.is_synchronized
        assert view.last_sync_error is not None
        assert binding.view_model.set_value_command.can_execute
        maya_cmds.setAttr(f"{name}.visibility", lock=False)
        view.sync_from_view_model()
        assert view.is_synchronized
        assert view.last_sync_error is None
    finally:
        binding.dispose()
        _process_events()


@pytest.mark.parametrize("fail_initial_sync", [False, True])
def test_maya_binding_releases_callbacks_on_failure_or_parent_deletion(
    new_scene, maya_cmds, fail_initial_sync
):
    name = maya_cmds.createNode("transform")
    plug = resolve_bool_plug(name, "visibility")
    callbacks = tuple(om.MMessage.nodeCallbacks(plug.node.m_obj))
    owner = qt.QObject()
    if fail_initial_sync:
        maya_cmds.setAttr(f"{name}.visibility", lock=True)
        with pytest.raises(RuntimeError, match="書き込めません"):
            MayaBoolBinding.from_attribute(
                _Data(), "enabled", maya_plug=plug, parent=owner
            )
        assert tuple(om.MMessage.nodeCallbacks(plug.node.m_obj)) == callbacks
        _process_events()
        assert not owner.children()
    else:
        binding = MayaBoolBinding.from_attribute(
            _Data(), "enabled", maya_plug=plug, parent=owner
        )
    owner.deleteLater()
    _process_events()
    assert tuple(om.MMessage.nodeCallbacks(plug.node.m_obj)) == callbacks
    if not fail_initial_sync:
        assert binding.is_disposed
        binding.dispose()


def test_resolver_accepts_standard_and_dynamic_bool_names(
    new_scene, maya_cmds
):
    name = maya_cmds.createNode("transform")
    maya_cmds.addAttr(
        name, longName="customVisibility", shortName="cv", attributeType="bool"
    )
    for long_name, short_name in (
        ("visibility", "v"),
        ("customVisibility", "cv"),
    ):
        first = resolve_bool_plug(name, long_name)
        second = resolve_bool_plug(name, short_name)
        assert first.plug == second.plug
        binding = MayaBoolBinding.from_attribute(
            _Data(True), "enabled", maya_plug=second
        )
        assert maya_cmds.getAttr(f"{name}.{long_name}")
        binding.dispose()
    _process_events()


def test_resolver_rejects_missing_non_bool_and_non_scalar_attributes(
    new_scene, maya_cmds
):
    name = maya_cmds.createNode("transform")
    maya_cmds.addAttr(
        name, longName="boolArray", attributeType="bool", multi=True
    )
    maya_cmds.addAttr(
        name,
        longName="boolGroup",
        attributeType="compound",
        numberOfChildren=1,
    )
    maya_cmds.addAttr(
        name, longName="boolChild", attributeType="bool", parent="boolGroup"
    )
    for attribute in (
        "translateX",
        "translate",
        "boolArray",
        "boolGroup",
        "boolChild",
    ):
        with pytest.raises(TypeError, match="bool"):
            resolve_bool_plug(name, attribute)
    with pytest.raises(AttributeError, match="存在しません"):
        resolve_bool_plug(name, "missing")
    for attribute in ("boolArray[0]", "boolGroup.boolChild", ""):
        with pytest.raises(ValueError):
            resolve_bool_plug(name, attribute)
    with pytest.raises(TypeError, match="str"):
        resolve_bool_plug(name, None)
