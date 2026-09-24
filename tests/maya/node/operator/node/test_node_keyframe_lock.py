from __future__ import annotations

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu

pytestmark = pytest.mark.maya


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def _keys(cmds, plug, *, weighted=False):
    for frame, value in ((1, 1), (2, 4), (3, 9)):
        cmds.setKeyframe(plug, time=frame, value=value)
    curve_name = cmds.listConnections(
        plug, source=True, destination=False, type="animCurve"
    )[0]
    curve = oma.MFnAnimCurve(
        om.MSelectionList().add(curve_name).getDependNode(0)
    )
    curve.setIsWeighted(weighted)
    for index in range(curve.numKeys):
        curve.setTangentsLocked(index, False)
        curve.setWeightsLocked(index, False)
    return curve_name


def _locks(node, attribute):
    data = getattr(node, attribute).keyframe.get_curve_data()
    assert data is not None
    return [(key.tangents_locked, key.weights_locked) for key in data.keys]


def test_node_tangent_locks_include_continuous_and_discrete_curves(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    _keys(maya_cmds, target + ".tx", weighted=True)
    _keys(maya_cmds, target + ".visibility", weighted=False)
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    before = (_locks(node, "tx"), _locks(node, "visibility"))

    node.keyframes.set_tangent_locks(
        2,
        None,
        tangents_locked=True,
        weights_locked=True,
    )
    manager.do_it_dg()
    after = (_locks(node, "tx"), _locks(node, "visibility"))
    assert after == (
        [(False, False), (True, True), (True, True)],
        [(False, False), (True, True), (True, True)],
    )
    assert not node.ty.keyframe.has_anim_curve()

    for _ in range(2):
        manager.undo_it()
        assert (_locks(node, "tx"), _locks(node, "visibility")) == before
        manager.redo_it()
        assert (_locks(node, "tx"), _locks(node, "visibility")) == after


def test_node_tangent_locks_use_explicit_attributes_and_layer(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    for frame, value in ((1, 1), (2, 2), (3, 3)):
        maya_cmds.setKeyframe(target + ".tx", time=frame, value=value)
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame, value in ((1, 10), (2, 20), (3, 30)):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=value,
            animLayer=layer,
            noResolve=True,
        )
    root = maya_cmds.animLayer(query=True, root=True)
    base_curve = maya_cmds.animLayer(
        root, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_curve = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    for curve_name in (base_curve, layer_curve):
        curve = oma.MFnAnimCurve(
            om.MSelectionList().add(curve_name).getDependNode(0)
        )
        for index in range(curve.numKeys):
            curve.setTangentsLocked(index, False)
            curve.setWeightsLocked(index, False)

    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.anim_layer(layer).set_tangent_locks(
        2,
        2,
        attributes=["tx"],
        tangents_locked=True,
        weights_locked=True,
    )
    manager.do_it_dg()

    layer_data = node.tx.keyframe.anim_layer(layer).get_curve_data()
    base_data = node.tx.keyframe.get_curve_data()
    assert layer_data is not None and base_data is not None
    assert [key.tangents_locked for key in layer_data.keys] == [
        False,
        True,
        False,
    ]
    assert [key.weights_locked for key in layer_data.keys] == [
        False,
        True,
        False,
    ]
    assert not any(key.tangents_locked for key in base_data.keys)
    assert not any(key.weights_locked for key in base_data.keys)


def test_nodes_tangent_locks_validate_every_target_before_edit(maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    first_curve = _keys(maya_cmds, first + ".tx")
    second_curve = _keys(maya_cmds, second + ".tx")
    maya_cmds.setAttr(second_curve + ".keyTanLocked[1]", lock=True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    first_node = nodes.existing.transform(first)
    second_node = nodes.existing.transform(second)
    before = (_locks(first_node, "tx"), _locks(second_node, "tx"))

    nodes.keyframes.set_tangent_locks(
        [first, second],
        attributes=["tx"],
        tangents_locked=True,
        weights_locked=True,
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert (_locks(first_node, "tx"), _locks(second_node, "tx")) == before
    assert not manager.can_undo
    maya_cmds.setAttr(second_curve + ".keyTanLocked[1]", lock=False)

    nodes.keyframes.set_tangent_locks(
        [first, second],
        attributes=["tx"],
        tangents_locked=True,
    )
    manager.do_it_dg()
    assert all(lock[0] for lock in _locks(first_node, "tx"))
    assert all(lock[0] for lock in _locks(second_node, "tx"))
    assert first_curve != second_curve


@pytest.mark.parametrize("nodes", [[], "target"])
def test_nodes_tangent_locks_reject_invalid_node_collections(maya_cmds, nodes):
    maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    with pytest.raises((TypeError, ValueError)):
        bdu.Nodes(modifier_manager=manager).keyframes.set_tangent_locks(
            nodes, tangents_locked=True
        )
    assert not manager.can_undo


def test_node_tangent_locks_reject_invalid_options(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.set_tangent_locks(
            include_channel_box=1,
            tangents_locked=True,
        )
    with pytest.raises(TypeError, match="weights_locked"):
        node.keyframes.set_tangent_locks(weights_locked=1)
    assert not manager.can_undo
