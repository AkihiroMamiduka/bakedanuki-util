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


def test_set_namespace_moves_existing_node_with_undo_redo(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.createNode("transform", name=":source:ctrl")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(":source:ctrl")

    assert node.set_namespace(":target:inner") is node
    assert not maya_cmds.namespace(exists=":target")
    mod.do_it_dg()
    assert node.name == "target:inner:ctrl"
    assert maya_cmds.namespace(exists=":source")

    mod.undo_it()
    assert node.name == "source:ctrl"
    assert maya_cmds.namespace(exists=":source")
    assert not maya_cmds.namespace(exists=":target")

    mod.redo_it()
    assert node.name == "target:inner:ctrl"
    assert maya_cmds.namespace(exists=":target:inner")


@pytest.mark.parametrize(
    "node_type,creation_kind", [("transform", "dag"), ("multiplyDivide", "dg")]
)
def test_set_namespace_moves_pending_named_node(
    new_scene, maya_cmds, node_type, creation_kind
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    node = getattr(bdu.Nodes(modifier_manager=mod).create, node_type)(
        name="source:node"
    )
    node.set_namespace(":target")

    if creation_kind == "dag":
        mod.do_it_dag()
        assert node.name == "source:node"
    mod.do_it_dg()
    assert node.name == "target:node"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":source")
    assert not maya_cmds.namespace(exists=":target")

    mod.redo_it()
    assert node.name == "target:node"


@pytest.mark.parametrize("order", ["rename_then_move", "move_then_rename"])
def test_rename_and_set_namespace_share_pending_name(
    new_scene, maya_cmds, order
):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.createNode("transform", name=":source:old")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(":source:old")

    if order == "rename_then_move":
        node.rename(new_name="new")
        node.set_namespace(":target")
    else:
        node.set_namespace(":target")
        node.rename(new_name="new")

    assert node._requested_name_hint == "target:new"
    mod.do_it_dg()
    assert node.name == "target:new"


def test_set_namespace_uses_live_name_after_previous_batch(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.createNode("transform", name=":source:old")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(":source:old")

    node.rename(new_name="reserved")
    mod.do_it_dg()
    maya_cmds.rename(":source:reserved", ":source:external")
    node.set_namespace(":target")
    mod.do_it_dg()

    assert node.name == "target:external"


def test_set_namespace_resolves_relative_target_at_reservation(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.createNode("transform", name=":ctrl")
    maya_cmds.namespace(add=":outer")
    maya_cmds.namespace(set=":outer")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(":ctrl")
    node.set_namespace("inner")
    maya_cmds.namespace(set=":")

    mod.do_it_dg()
    assert node.name == "outer:inner:ctrl"

    node.set_namespace(":")
    mod.do_it_dg()
    assert node.name == "ctrl"


@pytest.mark.parametrize(
    "kwargs",
    [
        {"new_name": "other:renamed"},
        {"search": "original", "replace": "other:renamed"},
        {"prefix": "other:"},
        {"suffix": ":other"},
    ],
)
def test_rename_rejects_namespace_in_local_name(new_scene, maya_cmds, kwargs):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.createNode("transform", name=":source:original")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(
        ":source:original"
    )

    with pytest.raises(ValueError, match="local node name"):
        node.rename(**kwargs)

    assert node._requested_name_hint is None
    mod.do_it_dg()
    assert node.name == "source:original"


def test_set_namespace_rejects_invalid_or_unnamed_pending_node(
    new_scene, maya_cmds
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    unnamed = nodes.create.transform()
    with pytest.raises(ValueError, match="must have a name"):
        unnamed.set_namespace("target")

    named = nodes.create.transform(name="named")
    with pytest.raises(ValueError, match="invalid name"):
        named.set_namespace("bad;name")
    with pytest.raises(TypeError, match="must be a string"):
        named.set_namespace(None)

    assert not maya_cmds.namespace(exists=":target")
    mod.do_it_dag()
    assert not maya_cmds.namespace(exists=":target")
