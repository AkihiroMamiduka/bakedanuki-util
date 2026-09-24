from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _plug(name):
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getPlug(0)


def _source(name):
    sources = _plug(name).connectedTo(True, False)
    return None if not sources else sources[0].name()


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing(name)


def _keys(cmds, plug):
    for frame, value in ((1, 0), (2, 1), (3, 0)):
        cmds.setKeyframe(
            plug,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )


def _tangents(cmds, plug, incoming):
    return cmds.keyTangent(
        plug,
        query=True,
        **{"inTangentType" if incoming else "outTangentType": True},
    )


def test_node_tangents_separate_continuous_and_discrete_channels(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    _keys(cmds, target + ".tx")
    _keys(cmds, target + ".visibility")
    original_values = cmds.keyframe(
        target + ".tx", query=True, valueChange=True
    )
    original_discrete_in = _tangents(cmds, target + ".visibility", True)
    original_discrete_out = _tangents(cmds, target + ".visibility", False)
    manager = bdu.ModifierManager()

    assert (
        _node(target, manager).keyframes.set_tangents(
            1,
            3,
            tangent_type="flat",
            out_tangent_type="linear",
            discrete_tangent_type="step",
        )
        is None
    )
    manager.do_it_dg()

    assert _tangents(cmds, target + ".tx", True) == ["flat"] * 3
    assert _tangents(cmds, target + ".tx", False) == ["linear"] * 3
    assert _tangents(cmds, target + ".visibility", True) == ["step"] * 3
    assert _tangents(cmds, target + ".visibility", False) == ["step"] * 3
    assert (
        cmds.keyframe(target + ".tx", query=True, valueChange=True)
        == original_values
    )

    manager.undo_it()
    assert _tangents(cmds, target + ".tx", True) == ["linear"] * 3
    assert (
        _tangents(cmds, target + ".visibility", True) == original_discrete_in
    )
    assert (
        _tangents(cmds, target + ".visibility", False) == original_discrete_out
    )
    manager.redo_it()
    assert _tangents(cmds, target + ".visibility", False) == ["step"] * 3


def test_general_node_tangent_options_leave_discrete_channels_unchanged(
    maya_cmds,
):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    _keys(cmds, target + ".tx")
    _keys(cmds, target + ".visibility")
    original_discrete_in = _tangents(cmds, target + ".visibility", True)
    original_discrete_out = _tangents(cmds, target + ".visibility", False)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.set_tangents(tangent_type="auto")
    manager.do_it_dg()

    assert _tangents(cmds, target + ".tx", True) == ["auto"] * 3
    assert (
        _tangents(cmds, target + ".visibility", True) == original_discrete_in
    )
    assert (
        _tangents(cmds, target + ".visibility", False) == original_discrete_out
    )


def test_node_tangents_do_not_create_curves_and_validate_explicit_targets(
    maya_cmds,
):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.set_tangents(attributes=["sx"], tangent_type="flat")
    manager.do_it_dg()
    assert _source(target + ".sx") is None

    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.set_tangents(attributes=["missing"], tangent_type="flat")
    with pytest.raises(ValueError, match="does not exist"):
        manager.do_it_dg()


def test_node_tangents_follow_earlier_queued_keys(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.tx.keyframe.set_keys([(1, 0), (2, 1), (3, 0)], tangent_type="linear")
    node.keyframes.set_tangents(
        2, None, attributes=["tx"], tangent_type="flat"
    )
    manager.do_it_dg()

    assert _tangents(cmds, target + ".tx", True) == [
        "linear",
        "flat",
        "flat",
    ]


def test_node_tangents_support_channel_box_and_explicit_layer(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    cmds.addAttr(target, longName="custom", attributeType="double")
    cmds.setAttr(target + ".custom", channelBox=True)
    _keys(cmds, target + ".custom")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.set_tangents(
        include_channel_box=True, tangent_type="flat"
    )
    manager.do_it_dg()
    assert _tangents(cmds, target + ".custom", True) == ["flat"] * 3

    _keys(cmds, target + ".tx")
    layer = cmds.animLayer("Correction")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    for frame, value in ((1, 2), (2, 4), (3, 6)):
        cmds.setKeyframe(
            target + ".tx",
            animLayer=layer,
            time=frame,
            value=value,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    root = cmds.animLayer(query=True, root=True)
    base_curve = cmds.animLayer(
        root, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_curve = cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).set_tangents(
        attributes=["tx"], tangent_type="auto"
    )
    manager.do_it_dg()

    assert _tangents(cmds, layer_curve, True) == ["auto"] * 3
    assert _tangents(cmds, base_curve, True) == ["linear"] * 3


def test_nodes_tangents_apply_attribute_union_and_rollback_together(
    maya_cmds,
):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.addAttr(first, longName="custom", attributeType="double")
    _keys(cmds, first + ".custom")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.set_tangents(
        [first, second],
        attributes=["custom"],
        tangent_type="flat",
    )
    manager.do_it_dg()
    assert _tangents(cmds, first + ".custom", True) == ["flat"] * 3
    manager.undo_it()
    assert _tangents(cmds, first + ".custom", True) == ["linear"] * 3

    _keys(cmds, first + ".tx")
    _keys(cmds, second + ".tx")
    second_curve = _source(second + ".tx").split(".")[0]
    cmds.lockNode(second_curve, lock=True)
    first_before = _tangents(cmds, first + ".tx", True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.set_tangents(
        [first, second], attributes=["tx"], tangent_type="auto"
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert _tangents(cmds, first + ".tx", True) == first_before
    assert not manager.can_undo


def test_nodes_tangents_reject_attributes_missing_from_every_node(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.set_tangents(
        [first, second], attributes=["missing"], tangent_type="flat"
    )
    with pytest.raises(ValueError, match="missing"):
        manager.do_it_dg()
    assert not manager.can_undo


@pytest.mark.parametrize("nodes", [[], "target"])
def test_nodes_tangents_reject_invalid_node_collections(maya_cmds, nodes):
    maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    with pytest.raises((TypeError, ValueError)):
        bdu.Nodes(modifier_manager=manager).keyframes.set_tangents(
            nodes, tangent_type="flat"
        )
    assert not manager.can_undo


def test_nodes_tangents_reject_duplicate_nodes(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.set_tangents(
            [target, nodes.existing(target)], tangent_type="flat"
        )
    assert not manager.can_undo
