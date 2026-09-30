from __future__ import annotations

import pytest


def test_mixed_targets_move_with_one_history(new_scene, maya_cmds):
    import bd_util as bdu
    from maya.api import OpenMaya as om

    maya_cmds.namespace(add=":source")
    for name in ("first", "second", "third", "fourth"):
        maya_cmds.createNode("transform", name=f":source:{name}")

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod, namespace=":creation_default")
    first = nodes.existing.transform(":source:first")
    second = nodes.existing.transform(":source:second")
    selection = om.MSelectionList()
    selection.add(":source:fourth")
    fourth = selection.getDependNode(0)

    nodes.move_to_namespace(
        [first, second, ":source:third", fourth], namespace=":target:inner"
    )
    assert nodes.namespace == ":creation_default"
    assert not maya_cmds.namespace(exists=":target")

    mod.do_it_dg()
    assert first.name == "target:inner:first"
    assert second.name == "target:inner:second"
    assert maya_cmds.objExists(":target:inner:third")
    assert om.MFnDependencyNode(fourth).name() == "target:inner:fourth"

    mod.undo_it()
    assert first.name == "source:first"
    assert second.name == "source:second"
    assert maya_cmds.objExists(":source:third")
    assert om.MFnDependencyNode(fourth).name() == "source:fourth"
    assert not maya_cmds.namespace(exists=":target")

    mod.redo_it()
    assert first.name == "target:inner:first"
    assert maya_cmds.objExists(":target:inner:third")


def test_relative_target_and_parent_child_are_moved_together(
    new_scene, maya_cmds
):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.namespace(add=":outer")
    maya_cmds.createNode("transform", name=":source:parent")
    maya_cmds.createNode(
        "transform", name=":source:child", parent=":source:parent"
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.existing.transform(":source:parent")
    child = nodes.existing.transform("|source:parent|source:child")

    maya_cmds.namespace(set=":outer")
    nodes.move_to_namespace([parent, child], namespace="inner")
    maya_cmds.namespace(set=":")
    mod.do_it_dg()

    assert parent.name == "outer:inner:parent"
    assert child.name == "outer:inner:child"
    assert child.full_path == "|outer:inner:parent|outer:inner:child"

    mod.undo_it()
    assert parent.name == "source:parent"
    assert child.name == "source:child"
    assert not maya_cmds.namespace(exists=":outer:inner")


def test_named_pending_nodes_move_after_creation(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    dag = nodes.create.transform(name="source:dag")
    dg = nodes.create.multiplyDivide(name="source:dg")

    nodes.move_to_namespace([dag, dg], namespace=":target")
    mod.do_it_dag()
    assert dag.name == "source:dag"
    mod.do_it_dg()
    assert dag.name == "target:dag"
    assert dg.name == "target:dg"

    mod.undo_it()
    assert not maya_cmds.namespace(exists=":source")
    assert not maya_cmds.namespace(exists=":target")


def test_invalid_batch_does_not_reserve_earlier_moves(new_scene, maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.createNode("transform", name=":source:first")
    maya_cmds.createNode("transform", name=":source:second")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    first = nodes.existing.transform(":source:first")
    second = nodes.existing.transform(":source:second")
    foreign = bdu.Nodes().existing.transform(":source:second")

    with pytest.raises(TypeError, match="iterable"):
        nodes.move_to_namespace(first, namespace=":target")
    with pytest.raises(ValueError, match="at least one"):
        nodes.move_to_namespace([], namespace=":target")
    with pytest.raises(TypeError, match="must be a string"):
        nodes.move_to_namespace([first], namespace=None)
    with pytest.raises(ValueError, match="invalid name"):
        nodes.move_to_namespace([first], namespace="bad;name")
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.move_to_namespace([first, first.m_obj], namespace=":target")
    with pytest.raises(ValueError, match="Node not found"):
        nodes.move_to_namespace(
            [first, ":source:missing"], namespace=":target"
        )
    with pytest.raises(ValueError, match="modifier_manager"):
        nodes.move_to_namespace([first, foreign], namespace=":target")
    with pytest.raises(TypeError, match="Expected a NodeOperator"):
        nodes.move_to_namespace([first, object()], namespace=":target")

    mod.do_it_dg()
    assert first.name == "source:first"
    assert second.name == "source:second"
    assert not maya_cmds.namespace(exists=":target")


def test_pending_mobject_and_unnamed_node_are_rejected(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    named = nodes.create.transform(name="source:named")
    unnamed = nodes.create.transform()

    with pytest.raises(ValueError, match="existing node"):
        nodes.move_to_namespace([named.m_obj], namespace=":target")
    with pytest.raises(ValueError, match="must have a name"):
        nodes.move_to_namespace([named, unnamed], namespace=":target")

    mod.do_it_dag()
    mod.do_it_dg()
    assert named.name == "source:named"
    assert not maya_cmds.namespace(exists=":target")


def test_name_collision_matches_single_node_move(new_scene, maya_cmds):
    import bd_util as bdu

    maya_cmds.namespace(add=":source")
    maya_cmds.namespace(add=":target")
    maya_cmds.createNode("transform", name=":source:duplicate")
    maya_cmds.createNode("transform", name=":target:duplicate")
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = nodes.existing.transform(":source:duplicate")

    nodes.move_to_namespace([node], namespace=":target")
    mod.do_it_dg()
    assert node.name == "target:duplicate1"

    mod.undo_it()
    assert node.name == "source:duplicate"
