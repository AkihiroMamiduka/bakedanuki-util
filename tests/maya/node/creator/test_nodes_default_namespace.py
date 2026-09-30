from __future__ import annotations

import pytest


def test_default_namespace_is_frozen_and_explicit_names_win(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":outer")
    maya_cmds.namespace(set=":outer")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace="group")
    cached_create = nodes.create.transform

    assert nodes.namespace == ":outer:group"
    maya_cmds.namespace(set=":")
    default = cached_create(name="default_ctrl")
    per_call = cached_create(name="override", namespace=":unique")
    qualified = cached_create(name=":explicit:qualified")
    root = cached_create(name=":root")
    maya_cmds.namespace(set=":outer")
    nodes.set_namespace("later")
    assert nodes.namespace == ":outer:later"
    maya_cmds.namespace(set=":")
    later = cached_create(name="later")

    assert not maya_cmds.namespace(exists=":outer:group")
    mod.do_it_dag()
    assert default.name == "outer:group:default_ctrl"
    assert per_call.name == "unique:override"
    assert qualified.name == "explicit:qualified"
    assert root.name == "root"
    assert later.name == "outer:later:later"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":outer:group")
    assert not maya_cmds.namespace(exists=":unique")
    assert not maya_cmds.namespace(exists=":explicit")
    assert not maya_cmds.namespace(exists=":outer:later")
    assert maya_cmds.namespace(exists=":outer")


def test_default_namespace_can_be_reset_or_forced_to_root(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":current")
    maya_cmds.namespace(set=":current")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace=":default")

    assert nodes.set_namespace(None) is nodes
    assert nodes.namespace is None
    current = nodes.create.transform(name="current_node")
    nodes.set_namespace("")
    assert nodes.namespace == ":"
    root = nodes.create.transform(name="root_node")
    nodes.set_namespace(":default")
    explicit_root = nodes.create.transform(name="explicit_root", namespace=":")

    mod.do_it_dag()
    assert current.name == "current:current_node"
    assert root.name == "root_node"
    assert explicit_root.name == "explicit_root"
    assert not maya_cmds.namespace(exists=":default")


def test_relative_per_call_namespace_ignores_nodes_default(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":outer")
    maya_cmds.namespace(set=":outer")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace=":default")
    per_call = nodes.create.multiplyDivide(name="math", namespace="other")
    qualified = nodes.create.multiplyDivide(name="other:qualified")
    maya_cmds.namespace(set=":")

    mod.do_it_dg()
    assert per_call.name == "outer:other:math"
    assert qualified.name == "outer:other:qualified"
    assert not maya_cmds.namespace(exists=":default")


def test_default_namespace_covers_shape_pair_and_anim_layer(
    new_scene, maya_cmds
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace=":assets")
    cached_mesh = nodes.create.with_transform.mesh
    nodes.set_namespace(":rig")
    transform, shape = cached_mesh(name="model")
    other_transform, other_shape = cached_mesh(
        name="other_model", namespace=":other"
    )
    explicit_transform, explicit_shape = cached_mesh(name=":explicit:model")
    layer = nodes.create.animLayer(name="Correction")

    mod.do_it_dag()
    mod.do_it_dg()
    assert transform.name == "rig:model"
    assert shape.name == "rig:modelShape"
    assert other_transform.name == "other:other_model"
    assert other_shape.name == "other:other_modelShape"
    assert explicit_transform.name == "explicit:model"
    assert explicit_shape.name == "explicit:modelShape"
    assert layer.name == "rig:Correction"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":rig")
    assert not maya_cmds.namespace(exists=":other")
    assert not maya_cmds.namespace(exists=":explicit")
    assert not maya_cmds.namespace(exists=":assets")


def test_nodes_instances_keep_separate_defaults_with_shared_modifier(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.createNode("transform", name=":existing")
    mod = bdu.ModifierManager()
    left = bdu.Nodes(modifier_manager=mod, namespace=":left")
    right = bdu.Nodes(modifier_manager=mod, namespace=":right")
    existing = left.existing.transform(":existing")
    left_node = left.create.transform(name="ctrl")
    right_node = right.create.transform(name="ctrl")

    mod.do_it_dag()
    assert existing.name == "existing"
    assert left_node.name == "left:ctrl"
    assert right_node.name == "right:ctrl"


def test_default_namespace_rejects_unnamed_and_conflicting_requests(
    new_scene, maya_cmds
):
    import bd_util as bdu

    with pytest.raises(ValueError, match="invalid name"):
        bdu.Nodes(namespace="bad;namespace")

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace=":group")
    with pytest.raises(ValueError, match="name is required"):
        nodes.create.transform()
    with pytest.raises(ValueError, match="name is required"):
        nodes.create.create("multiplyDivide")
    with pytest.raises(ValueError, match="name is required"):
        nodes.create.with_transform.mesh()
    with pytest.raises(ValueError, match="name is required"):
        nodes.create.animLayer()
    with pytest.raises(ValueError, match="cannot include a namespace"):
        nodes.create.transform(name=":explicit:ctrl", namespace=":other")
    with pytest.raises(ValueError, match="invalid name"):
        nodes.set_namespace("bad;namespace")

    assert nodes.namespace == ":group"
    assert not maya_cmds.namespace(exists=":group")
    assert not maya_cmds.namespace(exists=":explicit")
    assert not maya_cmds.namespace(exists=":other")
