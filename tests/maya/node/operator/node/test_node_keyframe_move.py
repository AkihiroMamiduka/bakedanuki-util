from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_move

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


def _curve(cmds, plug, frames=(0, 10, 20)):
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


@pytest.mark.parametrize(
    ("placement", "expected_first", "expected_second"),
    [
        ("to_start", [30, 40], [32, 42]),
        ("to_end", [38, 48], [40, 50]),
    ],
)
def test_nodes_use_one_absolute_anchor_and_preserve_channel_offsets(
    maya_cmds, placement, expected_first, expected_second
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [
        _curve(maya_cmds, names[0] + ".tx", (10, 20)),
        _curve(maya_cmds, names[1] + ".tx", (12, 22)),
    ]
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    destination = 30 if placement == "to_start" else 50
    assert (
        nodes.keyframes.move_frames(
            names, attributes=["tx"], **{placement: destination}
        )
        is None
    )
    manager.do_it_dg()
    assert _frames(curves[0]) == expected_first
    assert _frames(curves[1]) == expected_second
    for _ in range(2):
        manager.undo_it()
        assert _frames(curves[0]) == [10, 20]
        assert _frames(curves[1]) == [12, 22]
        manager.redo_it()
        assert _frames(curves[0]) == expected_first
        assert _frames(curves[1]) == expected_second


def test_node_moves_inclusive_range_and_preserves_key_data(maya_cmds):
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (0, 10, 20, 30))
    curve.setIsBreakdown(1, True)
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    before = node.tx.keyframe.get_curve_data()
    node.keyframes.move_frames(10, 20, attributes=["tx"], offset=5)
    manager.do_it_dg()
    assert _frames(curve) == [0, 15, 25, 30]
    assert curve.isBreakdown(curve.find(om.MTime(15, om.MTime.kFilm)))
    manager.undo_it()
    assert node.tx.keyframe.get_curve_data() == before


def test_explicit_boundary_and_union_of_mixed_nodes(maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    maya_cmds.addAttr(
        first, longName="custom", attributeType="double", keyable=True
    )
    curve = _curve(maya_cmds, first + ".custom", (10, 20))
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    second_node = nodes.existing.transform(second)
    first_object = om.MSelectionList().add(first).getDependNode(0)
    nodes.keyframes.move_frames(
        [first_object, second_node],
        5,
        25,
        attributes=["custom"],
        to_start=30,
    )
    manager.do_it_dg()
    assert _frames(curve) == [35, 45]


def test_missing_boundaries_are_inserted_on_each_existing_curve(maya_cmds):
    name = maya_cmds.createNode("transform")
    tx = _curve(maya_cmds, name + ".tx", (0, 30))
    ty = _curve(maya_cmds, name + ".ty", (0, 30))
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.move_frames(
        10, 20, attributes=["tx", "ty", "tz"], offset=5, insert_missing=True
    )
    manager.do_it_dg()
    assert _frames(tx) == [0, 15, 25, 30]
    assert _frames(ty) == [0, 15, 25, 30]
    assert not node.tz.keyframe.has_anim_curve()
    manager.undo_it()
    assert _frames(tx) == _frames(ty) == [0, 30]


def test_inserted_main_boundary_can_be_the_shared_implicit_anchor(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [
        _curve(maya_cmds, names[0] + ".tx", (30, 50)),
        _curve(maya_cmds, names[1] + ".tx", (35, 55)),
    ]
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        names, None, 20, attributes=["tx"], to_start=40, insert_missing=True
    )
    manager.do_it_dg()
    assert _frames(curves[0]) == [30, 40, 50]
    assert _frames(curves[1]) == [35, 40, 55]


def test_global_anchor_moves_fade_only_curve_but_empty_core_is_noop(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    core = _curve(maya_cmds, names[0] + ".tx", (10, 20))
    fade = _curve(maya_cmds, names[1] + ".tx", (25, 30))
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.move_frames(
        names,
        None,
        20,
        attributes=["tx"],
        to_start=15,
        interpolate_end=30,
        interpolation="linear",
    )
    manager.do_it_dg()
    assert _frames(core) == [15, 25]
    assert _frames(fade) == [27.5, 30]

    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        [names[1]],
        None,
        20,
        attributes=["tx"],
        to_start=40,
        interpolate_end=30,
    )
    manager.do_it_dg()
    assert _frames(fade) == [27.5, 30]


def test_channel_box_upstream_and_discrete_attribute(maya_cmds):
    name = maya_cmds.createNode("transform")
    maya_cmds.addAttr(name, longName="custom", attributeType="double")
    maya_cmds.setAttr(name + ".custom", channelBox=True)
    custom = _curve(maya_cmds, name + ".custom", (0, 10))
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom.name() + ".output", name + ".custom")
    maya_cmds.connectAttr(custom.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", name + ".custom")
    visibility = _curve(maya_cmds, name + ".visibility", (0, 10))
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).existing.transform(
        name
    ).keyframes.move_frames(offset=5, include_channel_box=True)
    manager.do_it_dg()
    assert _frames(custom) == [5, 15]
    assert _frames(visibility) == [5, 15]


def test_layer_selection_keeps_base_curve(maya_cmds):
    name = maya_cmds.createNode("transform")
    base = _curve(maya_cmds, name + ".tx", (0, 10))
    layer = maya_cmds.animLayer("Correction", attribute=name + ".tx")
    for frame in (0, 10):
        maya_cmds.setKeyframe(
            name + ".tx",
            time=frame,
            value=frame,
            animLayer=layer,
            noResolve=True,
        )
    layer_name = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=name + ".tx"
    )[0]
    layer_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(layer_name).getDependNode(0)
    )
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).existing.transform(
        name
    ).keyframes.anim_layer(layer).move_frames(attributes=["tx"], offset=5)
    manager.do_it_dg()
    assert _frames(base) == [0, 10]
    assert _frames(layer_curve) == [5, 15]

    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).existing.transform(
        name
    ).keyframes.move_frames(attributes=["tx"], offset=2)
    manager.do_it_dg()
    assert _frames(base) == [2, 12]
    assert _frames(layer_curve) == [5, 15]


def test_curve_reached_through_two_channels_is_moved_once(maya_cmds):
    source = maya_cmds.createNode("transform")
    first = maya_cmds.createNode("transform")
    second = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, source + ".tx", (0, 10))
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(curve.name() + ".output", source + ".tx")
    maya_cmds.connectAttr(curve.name() + ".output", conversion + ".input")
    for name in (first, second):
        maya_cmds.connectAttr(conversion + ".output", name + ".tx")
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        [first, second], attributes=["tx"], offset=5
    )
    manager.do_it_dg()
    assert _frames(curve) == [5, 15]
    manager.undo_it()
    assert _frames(curve) == [0, 10]


def test_move_follows_queued_bake_and_clip_restore(maya_cmds):
    baked = maya_cmds.createNode("transform", name="baked")
    restored = maya_cmds.createNode("transform", name="restored")
    _curve(maya_cmds, restored + ".tx", (0, 10))
    clip = bdu.AnimationClip.capture(
        [restored], attributes=["tx"], layer_mode="preserve"
    )
    maya_cmds.cutKey(restored + ".tx", clear=True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    baked_node = nodes.existing.transform(baked)
    restored_node = nodes.existing.transform(restored)
    baked_node.keyframes.bake(0, 2, attributes=["tx"], sample_by=1)
    clip.restore(manager, targets=[restored_node], mode="replace_all")
    nodes.keyframes.move_frames(
        [baked_node, restored_node], attributes=["tx"], offset=5
    )
    assert not baked_node.tx.keyframe.has_anim_curve()
    manager.do_it_dg()
    assert baked_node.tx.keyframe.frames() == [5, 6, 7]
    assert restored_node.tx.keyframe.frames() == [5, 15]
    manager.undo_it()
    assert not baked_node.tx.keyframe.has_anim_curve()
    assert restored_node.tx.keyframe.frames() == []


@pytest.mark.parametrize("lock", ["plug", "curve"])
def test_later_locked_target_leaves_all_curves_untouched(maya_cmds, lock):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    if lock == "plug":
        maya_cmds.setAttr(names[1] + ".tx", lock=True)
    else:
        maya_cmds.setAttr(curves[1].name() + ".ktv", lock=True)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        names, attributes=["tx"], offset=5
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 10, 20] for curve in curves)
    assert not manager.can_undo


def test_later_plan_failure_leaves_all_curves_untouched(
    maya_cmds, monkeypatch
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    original = _keyframe_move._plan_move
    calls = 0

    def fail_second(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("intentional planning failure")
        return original(*args)

    monkeypatch.setattr(_keyframe_move, "_plan_move", fail_second)
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        names, attributes=["tx"], offset=5
    )
    with pytest.raises(RuntimeError, match="intentional planning failure"):
        manager.do_it_dg()
    assert calls == 2
    assert all(_frames(curve) == [0, 10, 20] for curve in curves)


def test_later_curve_order_reversal_is_rejected_before_any_edit(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    first = _curve(maya_cmds, names[0] + ".tx", (10, 20))
    second = _curve(maya_cmds, names[1] + ".tx", (10, 20, 30))
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        names,
        10,
        20,
        attributes=["tx"],
        offset=20,
        interpolate_end=30,
        interpolation="linear",
    )
    with pytest.raises(ValueError, match="coincide or change order"):
        manager.do_it_dg()
    assert _frames(first) == [10, 20]
    assert _frames(second) == [10, 20, 30]


@pytest.mark.parametrize("fail_during_apply", [False, True])
def test_apply_and_later_failures_roll_back_all_curves(
    maya_cmds, monkeypatch, fail_during_apply
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [_curve(maya_cmds, name + ".tx") for name in names]
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.move_frames(
        names, attributes=["tx"], offset=5
    )
    if fail_during_apply:
        original = _keyframe_move._apply_move
        calls = 0

        def fail_second(*args):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise RuntimeError("intentional later failure")
            return original(*args)

        monkeypatch.setattr(_keyframe_move, "_apply_move", fail_second)
    else:

        def fail(_change):
            raise RuntimeError("intentional later failure")

        manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="intentional later failure"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 10, 20] for curve in curves)
    assert not manager.can_undo


def test_arguments_and_ui_time_unit_are_captured_at_booking(maya_cmds):
    maya_cmds.currentUnit(time="film")
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (0, 24))
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.move_frames(24, 24, attributes=["tx"], offset=24)
    maya_cmds.currentUnit(time="ntsc")
    manager.do_it_dg()
    assert [
        curve.input(index).asUnits(om.MTime.kSeconds)
        for index in range(curve.numKeys)
    ] == pytest.approx([0, 2])


def test_invalid_inputs_and_missing_targets(maya_cmds):
    name = maya_cmds.createNode("transform")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    node = nodes.existing.transform(name)
    with pytest.raises(ValueError, match="exactly one"):
        node.keyframes.move_frames(attributes=["tx"])
    with pytest.raises(ValueError, match="exactly one"):
        node.keyframes.move_frames(offset=1, to_start=2)
    with pytest.raises(ValueError, match="less than or equal"):
        node.keyframes.move_frames(2, 1, offset=1)
    with pytest.raises(ValueError, match="finite"):
        node.keyframes.move_frames(offset=math.inf)
    with pytest.raises(TypeError, match="insert_missing"):
        node.keyframes.move_frames(offset=1, insert_missing=1)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.move_frames(offset=1, include_channel_box=1)
    with pytest.raises(TypeError, match="attributes"):
        node.keyframes.move_frames(offset=1, attributes="tx")
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.move_frames([], offset=1)
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.move_frames(name, offset=1)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.move_frames([name, node], offset=1)

    empty = _curve(maya_cmds, name + ".ty", (0, 10))
    for index in reversed(range(empty.numKeys)):
        empty.remove(index)
    node.keyframes.move_frames(attributes=["tx"], to_start=10)
    node.keyframes.move_frames(
        attributes=["tx"], offset=10, insert_missing=True
    )
    node.keyframes.move_frames(
        attributes=["ty"], offset=10, insert_missing=True
    )
    manager.do_it_dg()
    assert not node.tx.keyframe.has_anim_curve()
    assert empty.numKeys == 0


def test_zero_move_does_not_insert_boundaries_or_flush_query(maya_cmds):
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (0, 30))
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.move_frames(
        10, 20, attributes=["tx"], offset=0, insert_missing=True
    )
    assert _frames(curve) == [0, 30]
    assert node.tx.keyframe.frames() == [0, 30]
    manager.do_it_dg()
    assert _frames(curve) == [0, 30]
