from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_snap

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _curve(cmds, plug, keys=((0, 0), (0.75, 10), (2, 0))):
    for frame, value in keys:
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


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def test_node_snaps_selected_existing_curves_in_one_undo_unit(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    translate = _curve(maya_cmds, target + ".tx")
    rotate = _curve(maya_cmds, target + ".rx")
    manager = bdu.ModifierManager()
    node = _node(target, manager)

    assert (
        node.keyframes.snap_subframe_keys(
            attributes=["translate", "rotate", "scale"]
        )
        is None
    )
    assert _frames(translate) == _frames(rotate) == [0, 0.75, 2]
    manager.do_it_dg()

    assert _frames(translate) == _frames(rotate) == [0, 1, 2]
    assert not node.sy.keyframe.has_anim_curve()
    for _ in range(2):
        manager.undo_it()
        assert _frames(translate) == _frames(rotate) == [0, 0.75, 2]
        manager.redo_it()
        assert _frames(translate) == _frames(rotate) == [0, 1, 2]


def test_nodes_accept_mixed_targets_and_attribute_union(maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    third = maya_cmds.createNode("transform", name="third")
    maya_cmds.addAttr(
        first, longName="custom", attributeType="double", keyable=True
    )
    custom = _curve(maya_cmds, first + ".custom")
    translate = _curve(maya_cmds, second + ".tx")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    third_object = om.MSelectionList().add(third).getDependNode(0)

    assert (
        nodes.keyframes.snap_subframe_keys(
            [first, nodes.existing.transform(second), third_object],
            attributes=["custom", "tx"],
        )
        is None
    )
    manager.do_it_dg()
    assert _frames(custom) == _frames(translate) == [0, 1, 2]


def test_channel_box_upstream_and_discrete_curve_are_selected(maya_cmds):
    target = maya_cmds.createNode("transform")
    maya_cmds.addAttr(target, longName="custom", attributeType="double")
    maya_cmds.setAttr(target + ".custom", channelBox=True)
    custom = _curve(maya_cmds, target + ".custom")
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom.name() + ".output", target + ".custom")
    maya_cmds.connectAttr(custom.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", target + ".custom")
    visibility = _curve(
        maya_cmds, target + ".visibility", ((0, 0), (0.75, 1), (2, 0))
    )
    visibility.setOutTangentType(0, visibility.kTangentStep)
    visibility.setOutTangentType(1, visibility.kTangentStep)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.snap_subframe_keys(
        include_channel_box=True
    )
    manager.do_it_dg()
    assert _frames(custom) == _frames(visibility) == [0, 1, 2]
    assert visibility.outTangentType(0) == visibility.kTangentStep


def test_explicit_layer_selection_does_not_change_base(maya_cmds):
    target = maya_cmds.createNode("transform")
    base = _curve(maya_cmds, target + ".tx")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame, value in ((0, 0), (0.75, 5), (2, 0)):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=value,
            animLayer=layer,
            noResolve=True,
        )
    layer_name = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(layer_name).getDependNode(0)
    )
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).snap_subframe_keys(
        attributes=["tx"]
    )
    manager.do_it_dg()
    assert _frames(base) == [0, 0.75, 2]
    assert _frames(layer_curve) == [0, 1, 2]


def test_shared_upstream_curve_is_edited_once(maya_cmds):
    source = maya_cmds.createNode("transform")
    first = maya_cmds.createNode("transform")
    second = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, source + ".tx")
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(curve.name() + ".output", source + ".tx")
    maya_cmds.connectAttr(curve.name() + ".output", conversion + ".input")
    for target in (first, second):
        maya_cmds.connectAttr(conversion + ".output", target + ".tx")
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.snap_subframe_keys(
        [first, second], attributes=["tx"]
    )
    manager.do_it_dg()
    assert _frames(curve) == [0, 1, 2]
    manager.undo_it()
    assert _frames(curve) == [0, 0.75, 2]


def test_later_locked_curve_leaves_earlier_curve_untouched(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    maya_cmds.setAttr(curves[1].name() + ".ktv", lock=True)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.snap_subframe_keys(
        names, attributes=["tx"]
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 0.75, 2] for curve in curves)
    assert not manager.can_undo


@pytest.mark.parametrize("failure", ["collision", "deviation"])
def test_later_plan_failure_leaves_all_curves_untouched(maya_cmds, failure):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    first = _curve(maya_cmds, names[0] + ".tx", ((0, 0), (0.75, 0), (2, 0)))
    second_keys = (
        ((0, 0), (1, 1), (1.25, 10), (2, 0))
        if failure == "collision"
        else ((0, 0), (0.75, 10), (2, 0))
    )
    second = _curve(maya_cmds, names[1] + ".tx", second_keys)
    before = [_frames(first), _frames(second)]
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.snap_subframe_keys(
        names,
        attributes=["tx"],
        max_deviation=0 if failure == "deviation" else None,
    )
    with pytest.raises(ValueError):
        manager.do_it_dg()
    assert [_frames(first), _frames(second)] == before
    assert not manager.can_undo


def test_later_callback_failure_rolls_back_all_curves(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.snap_subframe_keys(
        names, attributes=["tx"]
    )

    def fail(_change):
        raise RuntimeError("later failure")

    manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="later failure"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 0.75, 2] for curve in curves)
    assert not manager.can_undo


def test_failure_while_applying_second_curve_rolls_back_first(
    maya_cmds, monkeypatch
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    original = _keyframe_snap._apply_plan
    calls = 0

    def fail_second(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("later apply failure")
        return original(*args)

    monkeypatch.setattr(_keyframe_snap, "_apply_plan", fail_second)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.snap_subframe_keys(
        names, attributes=["tx"]
    )
    with pytest.raises(RuntimeError, match="later apply failure"):
        manager.do_it_dg()
    assert calls == 2
    assert all(_frames(curve) == [0, 0.75, 2] for curve in curves)
    assert not manager.can_undo


def test_node_resolves_curve_created_by_earlier_queued_bake(maya_cmds):
    target = maya_cmds.createNode("transform")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.bake(0, 5, attributes=["tx"], sample_by=1.25)
    node.keyframes.snap_subframe_keys(attributes=["tx"])
    assert not node.tx.keyframe.has_anim_curve()
    manager.do_it_dg()
    assert node.tx.keyframe.frames() == [0, 1, 3, 4, 5]
    manager.undo_it()
    assert not node.tx.keyframe.has_anim_curve()


def test_no_curve_and_integer_only_curve_are_noops(maya_cmds):
    target = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, target + ".tx", ((0, 0), (1, 1), (2, 0)))
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.snap_subframe_keys(attributes=["tx", "ty"])
    maya_cmds.file(modified=False)
    manager.do_it_dg()
    assert _frames(curve) == [0, 1, 2]
    assert not node.ty.keyframe.has_anim_curve()
    assert not maya_cmds.file(query=True, modified=True)


def test_node_and_nodes_reject_invalid_arguments(maya_cmds):
    target = maya_cmds.createNode("transform")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    node = nodes.existing.transform(target)
    with pytest.raises(ValueError):
        node.keyframes.snap_subframe_keys(2, 1)
    with pytest.raises(TypeError):
        node.keyframes.snap_subframe_keys(preserve_breakdowns=1)
    with pytest.raises(ValueError):
        node.keyframes.snap_subframe_keys(max_deviation=math.inf)
    with pytest.raises(TypeError):
        node.keyframes.snap_subframe_keys(include_channel_box=1)
    with pytest.raises(TypeError):
        node.keyframes.snap_subframe_keys(attributes="tx")
    with pytest.raises(ValueError):
        nodes.keyframes.snap_subframe_keys([])
    with pytest.raises(TypeError):
        nodes.keyframes.snap_subframe_keys(target)
    with pytest.raises(ValueError):
        nodes.keyframes.snap_subframe_keys([target, node])
    assert not manager.can_undo
