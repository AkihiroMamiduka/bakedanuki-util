from __future__ import annotations

import pytest

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def test_pending_creation_keeps_explicit_name_hint(maya_cmds):
    import bd_util as bdu

    bd_nodes = bdu.Nodes()
    dg_node = bd_nodes.create.multiplyDivide(name="pendingDG")
    dag_node = bd_nodes.create.transform(name="pendingDAG")

    assert dg_node.name == ""
    assert dag_node.name == ""
    assert dag_node.full_path == ""
    assert dg_node._requested_name_hint == "pendingDG"
    assert dag_node._requested_name_hint == "pendingDAG"
    assert dg_node._was_pending_creation
    assert dag_node._was_pending_creation
    assert not maya_cmds.objExists("pendingDG")
    assert not maya_cmds.objExists("pendingDAG")

    bd_nodes.modifier_manager.do_it_dag()
    bd_nodes.modifier_manager.do_it_dg()

    assert dg_node.name == "pendingDG"
    assert dag_node.name == "pendingDAG"
    assert dg_node._requested_name_hint == "pendingDG"
    assert dag_node._requested_name_hint == "pendingDAG"
    assert dg_node._was_pending_creation
    assert dag_node._was_pending_creation


def test_existing_node_has_no_name_hint_until_rename(maya_cmds):
    import bd_util as bdu

    name = maya_cmds.createNode("transform", name="original")
    bd_nodes = bdu.Nodes()
    node = bd_nodes.existing.transform(name)

    assert node._requested_name_hint is None
    assert not node._was_pending_creation

    node.rename(new_name="first")
    node.rename(new_name="final")

    assert node.name == "original"
    assert node._requested_name_hint == "final"
    assert not node._was_pending_creation

    bd_nodes.modifier_manager.do_it_dg()

    assert node.name == "final"
    assert node._requested_name_hint == "final"
    assert not node._was_pending_creation


def test_pending_creation_rename_updates_final_name_hint(maya_cmds):
    import bd_util as bdu

    bd_nodes = bdu.Nodes()
    node = bd_nodes.create.transform(name="created")

    node.rename(new_name="renamed")

    assert node.name == ""
    assert node._requested_name_hint == "renamed"
    assert node._was_pending_creation

    bd_nodes.modifier_manager.do_it_dag()
    assert node.name == "created"
    assert node._requested_name_hint == "renamed"

    bd_nodes.modifier_manager.do_it_dg()
    assert node.name == "renamed"
    assert node._requested_name_hint == "renamed"


def test_requested_name_hint_resolves_namespace_at_request_time(maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add="ns")
    maya_cmds.namespace(add="other")
    maya_cmds.namespace(add="ns:other")
    maya_cmds.namespace(set="ns")
    bd_nodes = bdu.Nodes()

    relative = bd_nodes.create.transform(name="ctrl")
    absolute = bd_nodes.create.transform(name=":rootCtrl")
    nested_relative = bd_nodes.create.transform(name="other:nestedCtrl")
    nested_absolute = bd_nodes.create.transform(name=":other:nestedCtrl")

    assert relative._requested_name_hint == "ns:ctrl"
    assert absolute._requested_name_hint == "rootCtrl"
    assert nested_relative._requested_name_hint == "ns:other:nestedCtrl"
    assert nested_absolute._requested_name_hint == "other:nestedCtrl"

    maya_cmds.namespace(set=":")
    assert relative._requested_name_hint == "ns:ctrl"
    assert absolute._requested_name_hint == "rootCtrl"
    assert nested_relative._requested_name_hint == "ns:other:nestedCtrl"
    assert nested_absolute._requested_name_hint == "other:nestedCtrl"
