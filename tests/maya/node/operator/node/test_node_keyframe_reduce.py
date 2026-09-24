from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_reduce

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def _curve(cmds, plug, *, values=None):
    values = list(range(11)) if values is None else values
    for frame, value in enumerate(values):
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
    return oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))


def _frames(curve):
    return [
        curve.input(index).asUnits(om.MTime.kFilm)
        for index in range(curve.numKeys)
    ]


def test_node_reduces_existing_curves_and_preserves_breakdowns(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.addAttr(
        target, longName="custom", attributeType="double", keyable=True
    )
    translate = _curve(maya_cmds, target + ".tx")
    rotate = _curve(maya_cmds, target + ".rx")
    custom = _curve(maya_cmds, target + ".custom")
    translate.setIsBreakdown(5, True)
    manager = bdu.ModifierManager()

    assert _node(target, manager).keyframes.reduce_keys(tolerance=0) is None
    manager.do_it_dg()

    assert _frames(translate) == [0, 5, 10]
    assert _frames(rotate) == [0, 10]
    assert _frames(custom) == [0, 10]
    assert not _node(target, manager).ty.keyframe.has_anim_curve()

    for _ in range(2):
        manager.undo_it()
        assert translate.numKeys == rotate.numKeys == custom.numKeys == 11
        manager.redo_it()
        assert _frames(translate) == [0, 5, 10]
        assert _frames(rotate) == _frames(custom) == [0, 10]

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.reduce_keys(
        attributes=["tx"], tolerance=0, preserve_breakdowns=False
    )
    manager.do_it_dg()
    assert _frames(translate) == [0, 10]
    manager.undo_it()
    assert _frames(translate) == [0, 5, 10]


def test_node_range_does_not_create_boundaries_or_curves(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    curve = _curve(maya_cmds, target + ".tx")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.reduce_keys(2.5, 7.5, tolerance=0, attributes=["tx"])
    node.keyframes.reduce_keys(tolerance=0, attributes=["sy"])
    manager.do_it_dg()

    assert _frames(curve) == [0, 1, 2, 3, 7, 8, 9, 10]
    assert not node.sy.keyframe.has_anim_curve()


def test_node_noop_does_not_create_curves_or_dirty_scene(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    maya_cmds.file(modified=False)
    node.keyframes.reduce_keys(attributes=["tx"], tolerance=0)
    manager.do_it_dg()
    assert not node.tx.keyframe.has_anim_curve()
    assert not maya_cmds.file(query=True, modified=True)


def test_node_reduction_follows_queued_bake(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.bake(
        0,
        10,
        attributes=["tx"],
        sample_by=1,
        tangent_type="linear",
    )
    node.keyframes.reduce_keys(0, 10, attributes=["tx"], tolerance=0)
    assert not node.tx.keyframe.has_anim_curve()

    manager.do_it_dg()
    assert node.tx.keyframe.frames() == [0, 10]
    manager.undo_it()
    assert not node.tx.keyframe.has_anim_curve()
    manager.redo_it()
    assert node.tx.keyframe.frames() == [0, 10]


def test_node_reduction_supports_channel_box_upstream_and_layer(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.addAttr(target, longName="custom", attributeType="double")
    maya_cmds.setAttr(target + ".custom", channelBox=True)
    custom = _curve(maya_cmds, target + ".custom")
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom.name() + ".output", target + ".custom")
    maya_cmds.connectAttr(custom.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", target + ".custom")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.reduce_keys(
        include_channel_box=True, tolerance=0
    )
    manager.do_it_dg()
    assert _frames(custom) == [0, 10]

    base = _curve(maya_cmds, target + ".tx")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame in range(11):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=frame,
            animLayer=layer,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    layer_name = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(layer_name).getDependNode(0)
    )
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).reduce_keys(
        attributes=["tx"], tolerance=0
    )
    manager.do_it_dg()
    assert base.numKeys == 11
    assert _frames(layer_curve) == [0, 10]


def test_nodes_apply_attribute_union_and_prevalidate_locked_curves(maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    maya_cmds.addAttr(
        first, longName="custom", attributeType="double", keyable=True
    )
    custom = _curve(maya_cmds, first + ".custom")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.reduce_keys(
        [first, second], attributes=["custom"], tolerance=0
    )
    manager.do_it_dg()
    assert _frames(custom) == [0, 10]
    manager.undo_it()
    assert custom.numKeys == 11

    first_curve = _curve(maya_cmds, first + ".tx")
    second_curve = _curve(maya_cmds, second + ".tx")
    maya_cmds.setAttr(second_curve.name() + ".ktv", lock=True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.reduce_keys(
        [first, second], attributes=["tx"], tolerance=0
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert first_curve.numKeys == second_curve.numKeys == 11
    assert not manager.can_undo


def test_nodes_plan_every_curve_before_editing(maya_cmds, monkeypatch):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    original = _keyframe_reduce._plan
    calls = 0

    def fail_second(*args, **kwargs):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("intentional planning failure")
        return original(*args, **kwargs)

    monkeypatch.setattr(_keyframe_reduce, "_plan", fail_second)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.reduce_keys(
        names, attributes=["tx"], tolerance=0
    )
    with pytest.raises(RuntimeError, match="intentional planning failure"):
        manager.do_it_dg()
    assert calls == 2
    assert all(curve.numKeys == 11 for curve in curves)
    assert not manager.can_undo


def test_node_reduction_rolls_back_after_later_failure(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    curve = _curve(maya_cmds, target + ".tx")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.reduce_keys(
        attributes=["tx"], tolerance=0
    )

    def fail(_change):
        raise RuntimeError("later failure")

    manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="later failure"):
        manager.do_it_dg()
    assert curve.numKeys == 11
    assert not manager.can_undo


def test_node_reduction_rejects_invalid_arguments(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    with pytest.raises(TypeError, match="tolerance"):
        node.keyframes.reduce_keys(tolerance="0")
    with pytest.raises(ValueError, match="nonnegative"):
        node.keyframes.reduce_keys(tolerance=-1)
    with pytest.raises(ValueError, match="finite"):
        node.keyframes.reduce_keys(tolerance=math.inf)
    with pytest.raises(TypeError, match="preserve_breakdowns"):
        node.keyframes.reduce_keys(tolerance=0, preserve_breakdowns=1)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.reduce_keys(tolerance=0, include_channel_box=1)
    with pytest.raises(TypeError, match="attributes"):
        node.keyframes.reduce_keys(tolerance=0, attributes="tx")

    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.reduce_keys([], tolerance=0)
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.reduce_keys(target, tolerance=0)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.reduce_keys([target, node], tolerance=0)
    assert not manager.can_undo
