from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_delete

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing.transform(name)


def _curve(cmds, plug, frames=(-2.5, 0, 1.5, 5, 10)):
    for frame in frames:
        cmds.setKeyframe(plug, time=frame, value=frame)
    name = cmds.listConnections(
        plug, source=True, destination=False, type="animCurve"
    )[0]
    return oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))


def _frames(curve):
    return [
        curve.input(index).asUnits(om.MTime.kFilm)
        for index in range(curve.numKeys)
    ]


def test_node_deletes_inclusive_range_from_existing_curves(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    translate = _curve(maya_cmds, target + ".tx")
    rotate = _curve(maya_cmds, target + ".rx")
    manager = bdu.ModifierManager()
    node = _node(target, manager)

    assert (
        node.keyframes.delete_keys(0, 5, attributes=["translate", "rotate"])
        is None
    )
    manager.do_it_dg()

    assert _frames(translate) == [-2.5, 10]
    assert _frames(rotate) == [-2.5, 10]
    assert not node.ty.keyframe.has_anim_curve()
    for _ in range(2):
        manager.undo_it()
        assert (
            _frames(translate)
            == _frames(rotate)
            == [
                -2.5,
                0,
                1.5,
                5,
                10,
            ]
        )
        manager.redo_it()
        assert _frames(translate) == _frames(rotate) == [-2.5, 10]


def test_node_supports_one_sided_single_and_all_key_ranges(maya_cmds):
    targets = [maya_cmds.createNode("transform") for _ in range(4)]
    curves = [_curve(maya_cmds, target + ".tx") for target in targets]
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.existing.transform(targets[0]).keyframes.delete_keys(
        end_frame=0, attributes=["tx"]
    )
    nodes.existing.transform(targets[1]).keyframes.delete_keys(
        start_frame=5, attributes=["tx"]
    )
    nodes.existing.transform(targets[2]).keyframes.delete_keys(
        1.5, 1.5, attributes=["tx"]
    )
    nodes.existing.transform(targets[3]).keyframes.delete_keys(
        attributes=["tx"]
    )
    manager.do_it_dg()

    assert _frames(curves[0]) == [1.5, 5, 10]
    assert _frames(curves[1]) == [-2.5, 0, 1.5]
    assert _frames(curves[2]) == [-2.5, 0, 5, 10]
    assert curves[3].numKeys == 0
    assert maya_cmds.objExists(curves[3].name())


def test_node_delete_does_not_create_boundaries_or_curves(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    curve = _curve(maya_cmds, target + ".tx")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.delete_keys(2, 4, attributes=["tx"])
    node.keyframes.delete_keys(attributes=["sy"])
    manager.do_it_dg()

    assert _frames(curve) == [-2.5, 0, 1.5, 5, 10]
    assert not node.sy.keyframe.has_anim_curve()


def test_node_delete_captures_ui_time_unit(maya_cmds):
    maya_cmds.currentUnit(time="film")
    target = maya_cmds.createNode("transform", name="target")
    curve = _curve(maya_cmds, target + ".tx", frames=(0, 24, 48))
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.delete_keys(24, 24, attributes=["tx"])
    maya_cmds.currentUnit(time="ntsc")
    manager.do_it_dg()

    assert [
        curve.input(index).asUnits(om.MTime.kSeconds)
        for index in range(curve.numKeys)
    ] == [0, 2]


def test_node_delete_follows_queued_bake(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    node.keyframes.bake(0, 4, attributes=["tx"], sample_by=1)
    node.keyframes.delete_keys(1, 3, attributes=["tx"])
    assert not node.tx.keyframe.has_anim_curve()

    manager.do_it_dg()
    assert node.tx.keyframe.frames() == [0, 4]
    manager.undo_it()
    assert not node.tx.keyframe.has_anim_curve()
    manager.redo_it()
    assert node.tx.keyframe.frames() == [0, 4]


def test_node_delete_follows_queued_clip_restore(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    _curve(maya_cmds, target + ".tx")
    clip = bdu.AnimationClip.capture(
        [target], attributes=["tx"], layer_mode="preserve"
    )
    maya_cmds.cutKey(target + ".tx", clear=True)
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    clip.restore(manager, targets=[node], mode="replace_all")
    node.keyframes.delete_keys(0, 5, attributes=["tx"])

    manager.do_it_dg()
    assert node.tx.keyframe.frames() == [-2.5, 10]
    manager.undo_it()
    assert node.tx.keyframe.frames() == []
    manager.redo_it()
    assert node.tx.keyframe.frames() == [-2.5, 10]


def test_node_delete_supports_channel_box_upstream_and_layer(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.addAttr(target, longName="custom", attributeType="double")
    maya_cmds.setAttr(target + ".custom", channelBox=True)
    custom = _curve(maya_cmds, target + ".custom")
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom.name() + ".output", target + ".custom")
    maya_cmds.connectAttr(custom.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", target + ".custom")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.delete_keys(
        0, 5, include_channel_box=True
    )
    manager.do_it_dg()
    assert _frames(custom) == [-2.5, 10]

    base = _curve(maya_cmds, target + ".tx")
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame in (-2.5, 0, 1.5, 5, 10):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=frame,
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
    _node(target, manager).keyframes.anim_layer(layer).delete_keys(
        0, 5, attributes=["tx"]
    )
    manager.do_it_dg()
    assert base.numKeys == 5
    assert _frames(layer_curve) == [-2.5, 10]


def test_nodes_accept_mixed_nodes_and_apply_attribute_union(maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    third = maya_cmds.createNode("transform", name="third")
    maya_cmds.addAttr(
        first, longName="custom", attributeType="double", keyable=True
    )
    custom = _curve(maya_cmds, first + ".custom")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    second_node = nodes.existing.transform(second)
    third_object = om.MSelectionList().add(third).getDependNode(0)

    nodes.keyframes.delete_keys(
        [first, second_node, third_object],
        0,
        5,
        attributes=["custom"],
    )
    manager.do_it_dg()
    assert _frames(custom) == [-2.5, 10]


@pytest.mark.parametrize("lock", ["plug", "curve"])
def test_nodes_prevalidate_every_curve_before_deleting(maya_cmds, lock):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    if lock == "plug":
        maya_cmds.setAttr(names[1] + ".tx", lock=True)
    else:
        maya_cmds.setAttr(curves[1].name() + ".ktv", lock=True)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.delete_keys(
        names, attributes=["tx"]
    )

    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert all(curve.numKeys == 5 for curve in curves)
    assert not manager.can_undo


def test_nodes_plan_every_curve_before_deleting(maya_cmds, monkeypatch):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    original = _keyframe_delete._indices
    calls = 0

    def fail_second(*args, **kwargs):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("intentional planning failure")
        return original(*args, **kwargs)

    monkeypatch.setattr(_keyframe_delete, "_indices", fail_second)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.delete_keys(
        names, attributes=["tx"]
    )
    with pytest.raises(RuntimeError, match="intentional planning failure"):
        manager.do_it_dg()
    assert calls == 2
    assert all(curve.numKeys == 5 for curve in curves)
    assert not manager.can_undo


def test_node_delete_rolls_back_after_later_failure(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    curve = _curve(maya_cmds, target + ".tx")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.delete_keys(0, 5, attributes=["tx"])

    def fail(_change):
        raise RuntimeError("later failure")

    manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="later failure"):
        manager.do_it_dg()
    assert _frames(curve) == [-2.5, 0, 1.5, 5, 10]
    assert not manager.can_undo


def test_node_delete_rejects_invalid_arguments(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    node = _node(target, manager)
    with pytest.raises(ValueError, match="less than or equal"):
        node.keyframes.delete_keys(2, 1)
    with pytest.raises(ValueError, match="finite"):
        node.keyframes.delete_keys(math.inf)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.delete_keys(include_channel_box=1)
    with pytest.raises(TypeError, match="attributes"):
        node.keyframes.delete_keys(attributes="tx")

    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.delete_keys([])
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.delete_keys(target)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.delete_keys([target, node])
    nodes.keyframes.delete_keys([target], attributes=["missing"])
    with pytest.raises(ValueError, match="do not exist"):
        manager.do_it_dg()
    assert not manager.can_undo
