from __future__ import annotations

import pytest


@pytest.mark.parametrize("first_kind", ["dg", "dag"])
def test_create_auto_creates_shared_namespace_with_undo_redo(
    new_scene, maya_cmds, first_kind
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    dag_node = nodes.create.transform(name="new_ns:inner:ctrl")
    dg_node = nodes.create.multiplyDivide(name="new_ns:inner:math")

    assert not maya_cmds.namespace(exists=":new_ns")

    getattr(mod, f"do_it_{first_kind}")()
    getattr(mod, f"do_it_{'dag' if first_kind == 'dg' else 'dg'}")()

    assert maya_cmds.namespace(exists=":new_ns:inner")
    assert dag_node.name == "new_ns:inner:ctrl"
    assert dg_node.name == "new_ns:inner:math"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":new_ns")

    mod.redo_it()
    assert dag_node.name == "new_ns:inner:ctrl"
    assert dg_node.name == "new_ns:inner:math"
    assert maya_cmds.namespace(exists=":new_ns:inner")


def test_create_keeps_existing_namespace_on_undo(new_scene, maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add=":existing_ns")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.transform(
        name=":existing_ns:ctrl"
    )

    mod.do_it_dag()
    assert node.name == "existing_ns:ctrl"

    mod.undo_it()
    assert maya_cmds.namespace(exists=":existing_ns")
    assert not maya_cmds.objExists(":existing_ns:ctrl")


def test_undo_keeps_namespace_used_by_later_node(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.transform(
        name="created_ns:owned"
    )
    mod.do_it_dag()
    other = maya_cmds.createNode("transform", name=":created_ns:other")

    mod.undo_it()
    assert not maya_cmds.objExists(":created_ns:owned")
    assert maya_cmds.objExists(other)
    assert maya_cmds.namespace(exists=":created_ns")

    mod.redo_it()
    assert node.name == "created_ns:owned"
    mod.undo_it()
    assert maya_cmds.objExists(other)
    assert maya_cmds.namespace(exists=":created_ns")


def test_undo_handles_created_current_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=mod).create.transform(name="created_ns:node")
    mod.do_it_dag()
    maya_cmds.namespace(set=":created_ns")

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":created_ns")


def test_create_freezes_relative_namespace_at_request_time(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":outer")
    maya_cmds.namespace(set=":outer")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    relative = nodes.create.transform(name="inner:ctrl")
    absolute = nodes.create.transform(name="root_ctrl", namespace=":root_ns")

    assert relative._requested_name_hint == "outer:inner:ctrl"
    assert absolute._requested_name_hint == "root_ns:root_ctrl"
    maya_cmds.namespace(set=":")

    mod.do_it_dag()
    assert relative.name == "outer:inner:ctrl"
    assert absolute.name == "root_ns:root_ctrl"


def test_pending_namespaced_node_rename_keeps_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.transform(
        name="created_ns:original"
    )
    node.rename(new_name="renamed")

    mod.do_it_dag()
    mod.do_it_dg()
    assert node.name == "created_ns:renamed"


def test_existing_namespaced_node_rename_keeps_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add=":existing_ns")
    maya_cmds.createNode("transform", name=":existing_ns:original")
    maya_cmds.namespace(add=":other_ns")
    maya_cmds.namespace(set=":other_ns")

    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(
        ":existing_ns:original"
    )
    node.rename(new_name="renamed")
    mod.do_it_dg()

    assert node.name == "existing_ns:renamed"


def test_create_rejects_conflicting_or_invalid_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    nodes = bdu.Nodes()
    with pytest.raises(ValueError, match="cannot include a namespace"):
        nodes.create.transform(name="first:ctrl", namespace="second")
    with pytest.raises(ValueError, match="invalid name"):
        nodes.create.transform(name="ctrl", namespace="bad;name")
    with pytest.raises(ValueError, match="name is required"):
        nodes.create.transform(namespace="new_ns")

    assert not maya_cmds.namespace(exists=":first")
    assert not maya_cmds.namespace(exists=":second")
    assert not maya_cmds.namespace(exists=":new_ns")


def test_shape_pair_uses_same_new_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    transform, mesh = nodes.create.with_transform.mesh(
        name="model", namespace="assets"
    )

    mod.do_it_dag()
    assert transform.name == "assets:model"
    assert mesh.name == "assets:modelShape"
    assert mesh.full_path == "|assets:model|assets:modelShape"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":assets")


def test_anim_layer_uses_new_namespace(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    layer = bdu.Nodes(modifier_manager=mod).create.animLayer(
        name="Correction", namespace="layers"
    )

    mod.do_it_dg()
    assert layer.name == "layers:Correction"
    assert maya_cmds.namespace(exists=":layers")

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":layers")
