from __future__ import annotations

import pytest

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def test_pending_creation_keeps_explicit_name_hint(maya_cmds):
    import bd_util as bdu

    nodes = bdu.Nodes()
    dg_node = nodes.create.multiplyDivide(name="pendingDG")
    dag_node = nodes.create.transform(name="pendingDAG")

    assert dg_node.name == ""
    assert dag_node.name == ""
    assert dag_node.full_path == ""
    assert dg_node._requested_name_hint == "pendingDG"
    assert dag_node._requested_name_hint == "pendingDAG"
    assert dg_node._was_pending_creation
    assert dag_node._was_pending_creation
    assert not maya_cmds.objExists("pendingDG")
    assert not maya_cmds.objExists("pendingDAG")

    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()

    assert dg_node.name == "pendingDG"
    assert dag_node.name == "pendingDAG"
    assert dg_node._requested_name_hint == "pendingDG"
    assert dag_node._requested_name_hint == "pendingDAG"
    assert dg_node._was_pending_creation
    assert dag_node._was_pending_creation


def test_existing_node_has_no_name_hint_until_rename(maya_cmds):
    import bd_util as bdu

    name = maya_cmds.createNode("transform", name="original")
    nodes = bdu.Nodes()
    node = nodes.existing.transform(name)

    assert node._requested_name_hint is None
    assert not node._was_pending_creation

    node.rename(new_name="first")
    node.rename(new_name="final")

    assert node.name == "original"
    assert node._requested_name_hint == "final"
    assert not node._was_pending_creation

    nodes.modifier_manager.do_it_dg()

    assert node.name == "final"
    assert node._requested_name_hint == "final"
    assert not node._was_pending_creation


def test_pending_creation_rename_updates_final_name_hint(maya_cmds):
    import bd_util as bdu

    nodes = bdu.Nodes()
    node = nodes.create.transform(name="created")

    node.rename(new_name="renamed")

    assert node.name == ""
    assert node._requested_name_hint == "renamed"
    assert node._was_pending_creation

    nodes.modifier_manager.do_it_dag()
    assert node.name == "created"
    assert node._requested_name_hint == "renamed"

    nodes.modifier_manager.do_it_dg()
    assert node.name == "renamed"
    assert node._requested_name_hint == "renamed"


def test_requested_name_hint_resolves_namespace_at_request_time(maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add="ns")
    maya_cmds.namespace(add="other")
    maya_cmds.namespace(add="ns:other")
    maya_cmds.namespace(set="ns")
    nodes = bdu.Nodes()

    relative = nodes.create.transform(name="ctrl")
    absolute = nodes.create.transform(name=":rootCtrl")
    nested_relative = nodes.create.transform(name="other:nestedCtrl")
    nested_absolute = nodes.create.transform(name=":other:nestedCtrl")

    assert relative._requested_name_hint == "ns:ctrl"
    assert absolute._requested_name_hint == "rootCtrl"
    assert nested_relative._requested_name_hint == "ns:other:nestedCtrl"
    assert nested_absolute._requested_name_hint == "other:nestedCtrl"

    maya_cmds.namespace(set=":")
    assert relative._requested_name_hint == "ns:ctrl"
    assert absolute._requested_name_hint == "rootCtrl"
    assert nested_relative._requested_name_hint == "ns:other:nestedCtrl"
    assert nested_absolute._requested_name_hint == "other:nestedCtrl"
