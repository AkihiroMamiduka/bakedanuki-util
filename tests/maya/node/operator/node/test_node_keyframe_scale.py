from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_scale

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
    ("timing", "first", "second"),
    [
        ({"scale": 2}, [10, 30], [14, 34]),
        ({"duration": 24}, [10, 30], [14, 34]),
        ({"to_start": 100, "to_end": 124}, [100, 120], [104, 124]),
        ({"scale": 2, "to_start": 100}, [100, 120], [104, 124]),
        ({"scale": 2, "to_end": 124}, [100, 120], [104, 124]),
        ({"scale": 2, "pivot": 20}, [0, 20], [4, 24]),
    ],
)
def test_nodes_use_one_source_interval_and_multiplier(
    maya_cmds, timing, first, second
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [
        _curve(maya_cmds, names[0] + ".tx", (10, 20)),
        _curve(maya_cmds, names[1] + ".tx", (12, 22)),
    ]
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    assert (
        nodes.keyframes.scale_frames(names, attributes=["tx"], **timing)
        is None
    )
    manager.do_it_dg()
    assert _frames(curves[0]) == first
    assert _frames(curves[1]) == second
    for _ in range(2):
        manager.undo_it()
        assert _frames(curves[0]) == [10, 20]
        assert _frames(curves[1]) == [12, 22]
        manager.redo_it()
        assert _frames(curves[0]) == first
        assert _frames(curves[1]) == second


def test_duration_uses_group_span_when_each_curve_has_one_key(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    curves = [
        _curve(maya_cmds, names[0] + ".tx", (10,)),
        _curve(maya_cmds, names[1] + ".tx", (12,)),
    ]
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        names, attributes=["tx"], duration=4
    )
    manager.do_it_dg()
    assert _frames(curves[0]) == [10]
    assert _frames(curves[1]) == [14]


def test_node_inclusive_range_preserves_values_breakdown_and_history(
    maya_cmds,
):
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (0, 10, 20, 40))
    curve.setIsBreakdown(1, True)
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    before = node.tx.keyframe.get_curve_data()
    node.keyframes.scale_frames(10, 20, attributes=["tx"], scale=2)
    manager.do_it_dg()
    assert _frames(curve) == [0, 10, 30, 40]
    assert [curve.value(i) for i in range(curve.numKeys)] == [0, 10, 20, 40]
    assert curve.isBreakdown(curve.find(om.MTime(10, om.MTime.kFilm)))
    manager.undo_it()
    assert node.tx.keyframe.get_curve_data() == before


def test_explicit_bounds_and_attribute_union_accept_mixed_nodes(maya_cmds):
    first = maya_cmds.createNode("transform")
    second = maya_cmds.createNode("transform")
    maya_cmds.addAttr(
        first, longName="custom", attributeType="double", keyable=True
    )
    curve = _curve(maya_cmds, first + ".custom", (10, 20))
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    first_object = om.MSelectionList().add(first).getDependNode(0)
    second_node = nodes.existing.transform(second)
    nodes.keyframes.scale_frames(
        [first_object, second_node],
        5,
        25,
        attributes=["custom"],
        scale=2,
        to_start=30,
    )
    manager.do_it_dg()
    assert _frames(curve) == [40, 60]


@pytest.mark.parametrize(
    ("mode", "expected"),
    [
        ("replace_range", [0, 20, 40]),
        ("merge", [0, 20, 30, 40]),
    ],
)
def test_missing_boundaries_and_replacement_on_each_curve(
    maya_cmds, mode, expected
):
    name = maya_cmds.createNode("transform")
    curves = [
        _curve(maya_cmds, name + ".tx", (0, 30)),
        _curve(maya_cmds, name + ".ty", (0, 30)),
    ]
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.scale_frames(
        10,
        20,
        attributes=["tx", "ty", "tz"],
        scale=2,
        to_start=20,
        mode=mode,
        insert_missing=True,
    )
    manager.do_it_dg()
    assert all(_frames(curve) == expected for curve in curves)
    assert not node.tz.keyframe.has_anim_curve()
    manager.undo_it()
    assert all(_frames(curve) == [0, 30] for curve in curves)


def test_global_source_moves_fade_only_curve_but_missing_source_is_noop(
    maya_cmds,
):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    core = _curve(maya_cmds, names[0] + ".tx", (10, 20))
    fade = _curve(maya_cmds, names[1] + ".tx", (25, 30))
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.scale_frames(
        names,
        None,
        20,
        attributes=["tx"],
        scale=1.5,
        interpolate_end=30,
        interpolation="linear",
    )
    manager.do_it_dg()
    assert _frames(core) == [10, 25]
    assert _frames(fade) == pytest.approx([28.75, 30])

    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        [names[1]],
        None,
        20,
        attributes=["tx"],
        scale=2,
        interpolate_end=30,
    )
    manager.do_it_dg()
    assert _frames(fade) == pytest.approx([28.75, 30])


def test_channel_box_upstream_and_discrete_attribute(maya_cmds):
    name = maya_cmds.createNode("transform")
    maya_cmds.addAttr(name, longName="custom", attributeType="double")
    maya_cmds.setAttr(name + ".custom", channelBox=True)
    custom = _curve(maya_cmds, name + ".custom", (0, 10))
    conversion = maya_cmds.createNode("unitConversion")
    maya_cmds.disconnectAttr(custom.name() + ".output", name + ".custom")
    maya_cmds.connectAttr(custom.name() + ".output", conversion + ".input")
    maya_cmds.connectAttr(conversion + ".output", name + ".custom")
    for frame, value in ((0, 0), (10, 1)):
        maya_cmds.setKeyframe(name + ".visibility", time=frame, value=value)
    visibility_name = maya_cmds.listConnections(
        name + ".visibility", source=True, destination=False, type="animCurve"
    )[0]
    visibility = oma.MFnAnimCurve(
        om.MSelectionList().add(visibility_name).getDependNode(0)
    )
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).existing.transform(
        name
    ).keyframes.scale_frames(scale=2, include_channel_box=True)
    manager.do_it_dg()
    assert _frames(custom) == [0, 20]
    assert _frames(visibility) == [0, 20]
    assert [visibility.value(i) for i in range(visibility.numKeys)] == [0, 1]


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
    ).keyframes.anim_layer(layer).scale_frames(attributes=["tx"], scale=2)
    manager.do_it_dg()
    assert _frames(base) == [0, 10]
    assert _frames(layer_curve) == [0, 20]

    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).existing.transform(
        name
    ).keyframes.scale_frames(attributes=["tx"], scale=2)
    manager.do_it_dg()
    assert _frames(base) == [0, 20]
    assert _frames(layer_curve) == [0, 20]


def test_shared_upstream_curve_is_scaled_once(maya_cmds):
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
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        [first, second], attributes=["tx"], scale=2
    )
    manager.do_it_dg()
    assert _frames(curve) == [0, 20]
    manager.undo_it()
    assert _frames(curve) == [0, 10]


def test_scale_follows_queued_bake_and_clip_restore(maya_cmds):
    baked = maya_cmds.createNode("transform")
    restored = maya_cmds.createNode("transform")
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
    nodes.keyframes.scale_frames(
        [baked_node, restored_node], attributes=["tx"], scale=2
    )
    assert not baked_node.tx.keyframe.has_anim_curve()
    manager.do_it_dg()
    assert baked_node.tx.keyframe.frames() == [0, 2, 4]
    assert restored_node.tx.keyframe.frames() == [0, 20]
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
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        names, attributes=["tx"], scale=2
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 10, 20] for curve in curves)
    assert not manager.can_undo


def test_later_curve_collision_is_rejected_before_any_edit(maya_cmds):
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    first = _curve(maya_cmds, names[0] + ".tx", (10, 20))
    second = _curve(maya_cmds, names[1] + ".tx", (10, 20, 30))
    manager = bdu.ModifierManager()
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        names,
        10,
        20,
        attributes=["tx"],
        scale=2,
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
    bdu.Nodes(modifier_manager=manager).keyframes.scale_frames(
        names, attributes=["tx"], scale=2
    )
    if fail_during_apply:
        original = _keyframe_scale._apply_scale
        calls = 0

        def fail_second(*args):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise RuntimeError("intentional later failure")
            return original(*args)

        monkeypatch.setattr(_keyframe_scale, "_apply_scale", fail_second)
    else:

        def fail(_change):
            raise RuntimeError("intentional later failure")

        manager.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="intentional later failure"):
        manager.do_it_dg()
    assert all(_frames(curve) == [0, 10, 20] for curve in curves)
    assert not manager.can_undo


def test_implicit_zero_width_and_booking_units(maya_cmds):
    maya_cmds.currentUnit(time="film")
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (24,))
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.scale_frames(attributes=["tx"], duration=24)
    with pytest.raises(ValueError, match="zero-width"):
        manager.do_it_dg()
    assert _frames(curve) == [24]

    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.scale_frames(24, 24, attributes=["tx"], scale=2, offset=24)
    maya_cmds.currentUnit(time="ntsc")
    manager.do_it_dg()
    assert [
        curve.input(index).asUnits(om.MTime.kSeconds)
        for index in range(curve.numKeys)
    ] == pytest.approx([2])


def test_invalid_inputs_and_no_curve_noop(maya_cmds):
    name = maya_cmds.createNode("transform")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    node = nodes.existing.transform(name)
    with pytest.raises(ValueError, match="exactly one"):
        node.keyframes.scale_frames(attributes=["tx"])
    with pytest.raises(ValueError, match="exactly one"):
        node.keyframes.scale_frames(scale=2, duration=10)
    with pytest.raises(ValueError, match="positive"):
        node.keyframes.scale_frames(scale=0)
    with pytest.raises(ValueError, match="finite"):
        node.keyframes.scale_frames(scale=math.inf)
    with pytest.raises(ValueError, match="offset"):
        node.keyframes.scale_frames(scale=2, offset=1, to_start=2)
    with pytest.raises(ValueError, match="pivot"):
        node.keyframes.scale_frames(scale=2, pivot=1, to_end=2)
    with pytest.raises(TypeError, match="include_channel_box"):
        node.keyframes.scale_frames(scale=2, include_channel_box=1)
    with pytest.raises(TypeError, match="attributes"):
        node.keyframes.scale_frames(scale=2, attributes="tx")
    with pytest.raises(ValueError, match="at least one"):
        nodes.keyframes.scale_frames([], scale=2)
    with pytest.raises(TypeError, match="iterable"):
        nodes.keyframes.scale_frames(name, scale=2)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.scale_frames([name, node], scale=2)

    empty = _curve(maya_cmds, name + ".ty", (0, 10))
    for index in reversed(range(empty.numKeys)):
        empty.remove(index)
    node.keyframes.scale_frames(attributes=["tx"], scale=2)
    node.keyframes.scale_frames(
        2, 8, attributes=["tx"], scale=2, insert_missing=True
    )
    node.keyframes.scale_frames(
        2, 8, attributes=["ty"], scale=2, insert_missing=True
    )
    manager.do_it_dg()
    assert not node.tx.keyframe.has_anim_curve()
    assert empty.numKeys == 0


def test_identity_does_not_insert_or_flush_query(maya_cmds):
    name = maya_cmds.createNode("transform")
    curve = _curve(maya_cmds, name + ".tx", (0, 30))
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.keyframes.scale_frames(
        10, 20, attributes=["tx"], scale=1, insert_missing=True
    )
    assert _frames(curve) == [0, 30]
    assert node.tx.keyframe.frames() == [0, 30]
    manager.do_it_dg()
    assert _frames(curve) == [0, 30]
