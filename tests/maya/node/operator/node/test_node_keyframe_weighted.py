from __future__ import annotations

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def _curve(cmds, plug, *, weighted=False):
    for frame, value in ((1, 0), (2, 2), (3, 1)):
        cmds.setKeyframe(
            plug,
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    name = cmds.listConnections(
        plug, source=True, destination=False, type="animCurve"
    )[0]
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    curve.setIsWeighted(weighted)
    return name, curve


def _tangents(curve):
    return tuple(
        component
        for index in range(curve.numKeys)
        for is_in in (True, False)
        for component in curve.getTangentXY(index, is_in)
    )


def test_node_weighted_changes_existing_continuous_and_discrete_curves(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    _, continuous = _curve(maya_cmds, target + ".tx", weighted=True)
    _, discrete = _curve(maya_cmds, target + ".visibility")
    continuous.setTangent(1, 0.03, 0.2, True, convertUnits=False)
    continuous.setTangent(1, 0.09, -0.1, False, convertUnits=False)
    before_tangents = _tangents(continuous)
    before_types = tuple(
        (
            continuous.inTangentType(index),
            continuous.outTangentType(index),
        )
        for index in range(continuous.numKeys)
    )
    manager = bdu.ModifierManager()
    node = _node(target, manager)

    assert node.keyframes.set_weighted(False) is None
    manager.do_it_dg()
    assert continuous.isWeighted is False
    assert discrete.isWeighted is False
    assert not node.ty.keyframe.has_anim_curve()
    assert (
        tuple(
            (
                continuous.inTangentType(index),
                continuous.outTangentType(index),
            )
            for index in range(continuous.numKeys)
        )
        == before_types
    )

    for _ in range(2):
        manager.undo_it()
        assert continuous.isWeighted is True
        assert discrete.isWeighted is False
        assert _tangents(continuous) == pytest.approx(before_tangents)
        manager.redo_it()
        assert continuous.isWeighted is False
        assert discrete.isWeighted is False

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.set_weighted(True)
    manager.do_it_dg()
    assert continuous.isWeighted is True
    assert discrete.isWeighted is True


def test_node_weighted_uses_existing_curves_and_follows_queued_creation(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.set_weighted(True, attributes=["sx"])
    manager.do_it_dg()
    assert not node.sx.keyframe.has_anim_curve()

    empty_name = maya_cmds.createNode("animCurveTU", name="empty_curve")
    maya_cmds.connectAttr(empty_name + ".output", target + ".sy")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.set_weighted(True, attributes=["sy"])
    manager.do_it_dg()
    empty = oma.MFnAnimCurve(
        om.MSelectionList().add(empty_name).getDependNode(0)
    )
    assert empty.numKeys == 0
    assert empty.isWeighted is True

    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.tx.keyframe.set_keys([(1, 0), (2, 1)])
    node.keyframes.set_weighted(True, attributes=["tx"])
    manager.do_it_dg()
    assert node.tx.keyframe.get_weighted() is True

    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.set_weighted(True, attributes=["missing"])
    with pytest.raises(ValueError, match="does not exist"):
        manager.do_it_dg()
    assert not manager.can_undo


def test_node_weighted_supports_channel_box_upstream_and_explicit_layer(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.addAttr(target, longName="custom", attributeType="double")
    maya_cmds.setAttr(target + ".custom", channelBox=True)
    custom_name, custom = _curve(maya_cmds, target + ".custom")
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom_name + ".output", target + ".custom")
    maya_cmds.connectAttr(custom_name + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", target + ".custom")

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.set_weighted(
        True, include_channel_box=True
    )
    manager.do_it_dg()
    assert custom.isWeighted is True

    _curve(maya_cmds, target + ".tx")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame, value in ((1, 3), (2, 6), (3, 9)):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=value,
            animLayer=layer,
            noResolve=True,
        )
    root = maya_cmds.animLayer(query=True, root=True)
    base_name = maya_cmds.animLayer(
        root, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_name = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    base = oma.MFnAnimCurve(
        om.MSelectionList().add(base_name).getDependNode(0)
    )
    layer_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(layer_name).getDependNode(0)
    )

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).set_weighted(
        True, attributes=["tx"]
    )
    manager.do_it_dg()
    assert layer_curve.isWeighted is True
    assert base.isWeighted is False


def test_nodes_weighted_apply_attribute_union_and_prevalidate_all_curves(
    maya_cmds,
):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    maya_cmds.addAttr(first, longName="custom", attributeType="double")
    _, custom = _curve(maya_cmds, first + ".custom")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.set_weighted([first, second], True, attributes=["custom"])
    manager.do_it_dg()
    assert custom.isWeighted is True
    manager.undo_it()
    assert custom.isWeighted is False

    _, first_curve = _curve(maya_cmds, first + ".tx")
    second_name, second_curve = _curve(maya_cmds, second + ".tx")
    maya_cmds.setAttr(second_name + ".weightedTangents", lock=True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.set_weighted([first, second], True, attributes=["tx"])
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert first_curve.isWeighted is False
    assert second_curve.isWeighted is False
    assert not manager.can_undo


def test_node_weighted_rolls_back_after_later_failure(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    _, curve = _curve(maya_cmds, target + ".tx")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.set_weighted(True, attributes=["tx"])

    def fail(_change):
        raise RuntimeError("later failure")

    manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="later failure"):
        manager.do_it_dg()
    assert curve.isWeighted is False
    assert not manager.can_undo


def test_node_weighted_rejects_invalid_arguments(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    with pytest.raises(TypeError, match="weighted"):
        node.keyframes.set_weighted(1)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.set_weighted(True, include_channel_box=1)
    with pytest.raises(TypeError, match="attributes"):
        node.keyframes.set_weighted(True, attributes="tx")

    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.set_weighted([], True)
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.set_weighted(target, True)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.set_weighted([target, node], True)
    assert not manager.can_undo
