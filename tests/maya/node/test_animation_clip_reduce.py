from __future__ import annotations

import math
from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.animation_clip import NodeAnimationData
from bd_util.maya.node.operator.attr import (
    _keyframe_move,
    _keyframe_reduce,
    _keyframe_snapshot,
)
from test_animation_clip import _layer, _node, _values

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


@pytest.fixture(autouse=True)
def units(maya_cmds):
    maya_cmds.currentUnit(time="film", linear="cm", angle="deg")
    yield
    maya_cmds.currentUnit(time="film", linear="cm", angle="deg")


def _clip(cmds, *, mode="flatten", values=None, frames=None, attr="tx"):
    values = list(range(11)) if values is None else values
    frames = list(range(len(values))) if frames is None else frames
    source = _node(cmds, "source", zip(frames, values), attr=attr)
    return bdu.AnimationClip.capture(
        [source], attributes=[attr], layer_mode=mode
    )


def _frames(clip):
    return [key.frame for key in clip.nodes[0].channels[0].curve.keys]


def _restore(cmds, clip, name="target"):
    target = cmds.createNode("transform", name=name)
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all")
    mod.do_it_dg()
    return target, mod


def _state(cmds):
    return (
        sorted(cmds.ls()),
        cmds.file(query=True, modified=True),
        cmds.currentTime(query=True),
        cmds.ls(selection=True),
        cmds.undoInfo(query=True, undoName=True),
        cmds.undoInfo(query=True, redoName=True),
    )


@pytest.mark.parametrize("mode", ["flatten", "preserve"])
@pytest.mark.parametrize("attr", ["tx", "rx", "sx"])
def test_reduced_copy_json_and_restore_history(maya_cmds, mode, attr):
    clip = _clip(maya_cmds, mode=mode, attr=attr)
    before = clip.to_dict()
    reduced = clip.reduce_keys(tolerance=1e-8)
    assert reduced is not clip
    assert _frames(reduced) == [0, 10]
    assert clip.to_dict() == before
    assert replace(reduced, nodes=clip.nodes) == clip
    reduced = bdu.AnimationClip.from_json(reduced.to_json())
    target, mod = _restore(maya_cmds, reduced)
    frames = [i / 10 for i in range(101)]
    assert _values(maya_cmds, target + "." + attr, frames) == pytest.approx(
        frames
    )
    assert len(maya_cmds.keyframe(target + "." + attr, query=True)) == 2
    for _ in range(2):
        mod.undo_it()
        assert not maya_cmds.keyframe(target + "." + attr, query=True)
        mod.redo_it()
        assert _values(
            maya_cmds, target + "." + attr, frames
        ) == pytest.approx(frames)
    reduced.nodes[0].channels[0].curve.keys[0].value = 99
    assert clip.to_dict() == before


@pytest.mark.parametrize("mode", ["flatten", "preserve"])
@pytest.mark.parametrize(
    "bounds,expected",
    [
        ((2, 7), [0, 1, 2, 7, 8, 9, 10]),
        ((2.5, 7.5), [0, 1, 2, 3, 7, 8, 9, 10]),
        ((None, 7), [0, 7, 8, 9, 10]),
        ((2, None), [0, 1, 2, 10]),
        ((2, 2), list(range(11))),
        ((20, 30), list(range(11))),
        ((2.2, 2.8), list(range(11))),
    ],
)
def test_range_preserves_ends_outside_shape_and_clip_extent(
    maya_cmds, mode, bounds, expected
):
    clip = _clip(maya_cmds, mode=mode)
    reduced = clip.reduce_keys(*bounds, tolerance=0)
    assert _frames(reduced) == expected
    assert (reduced.start_frame, reduced.end_frame) == (0, 10)
    target, _ = _restore(maya_cmds, reduced)
    frames = [i / 10 for i in range(101)]
    assert _values(maya_cmds, target + ".tx", frames) == pytest.approx(frames)


@pytest.mark.parametrize("kind", ["tx", "rx", "sx"])
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "linear", "auto", "spline", "clamped", "plateau"]
)
def test_matches_live_reduction_and_preserves_curve_metadata(
    maya_cmds, kind, weighted, tangent
):
    source = _node(
        maya_cmds,
        "source",
        enumerate([0, 0.08, 0.12, 0.16, 0.20, 0.12, 0.06, 0]),
        attr=kind,
    )
    mod = bdu.ModifierManager()
    keys = bdu.Nodes(modifier_manager=mod).existing(source)[kind].keyframe
    curve = oma.MFnAnimCurve(keys.find_anim_curves()[0].m_obj)
    curve.setIsWeighted(weighted)
    if tangent == "fixed":
        maya_cmds.keyTangent(
            source + "." + kind,
            edit=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    maya_cmds.keyTangent(
        source + "." + kind,
        edit=True,
        inTangentType=tangent,
        outTangentType=tangent,
    )
    curve.setPreInfinityType(curve.kLinear)
    curve.setPostInfinityType(curve.kCycleRelative)
    curve.setIsBreakdown(3, True)
    clip = bdu.AnimationClip.capture(
        [source], attributes=[kind], layer_mode="preserve"
    )
    before = clip.to_dict()
    original_data = clip.nodes[0].channels[0].curve
    reduced = clip.reduce_keys(tolerance=0.06)
    keys.reduce_keys(tolerance=0.06)
    mod.do_it_dg()
    assert _frames(reduced) == pytest.approx(keys.frames())
    assert clip.to_dict() == before
    data = reduced.nodes[0].channels[0].curve
    assert (data.weighted, data.pre_infinity, data.post_infinity) == (
        weighted,
        "linear",
        "cycleRelative",
    )
    originals = {key.frame: key for key in original_data.keys}
    for key in data.keys:
        original = originals[key.frame]
        assert (
            key.value,
            key.in_tangent_type,
            key.out_tangent_type,
            key.tangents_locked,
            key.weights_locked,
            key.breakdown,
        ) == (
            original.value,
            original.in_tangent_type,
            original.out_tangent_type,
            original.tangents_locked,
            original.weights_locked,
            original.breakdown,
        )
        if tangent == "fixed":
            for field in ("in_tangent_xy", "out_tangent_xy"):
                a, b = getattr(key, field), getattr(original, field)
                if weighted:
                    assert a == pytest.approx(b, abs=1e-10)
                else:
                    assert math.atan2(a[1], a[0]) == pytest.approx(
                        math.atan2(b[1], b[0]), abs=1e-10
                    )
    target, _ = _restore(maya_cmds, reduced)
    frames = [i / 50 for i in range(-50, 401)]
    assert _values(maya_cmds, target + "." + kind, frames) == pytest.approx(
        _values(maya_cmds, source + "." + kind, frames), abs=1e-7
    )


@pytest.mark.parametrize("preserve", [False, True])
def test_breakdowns_and_discrete_transitions(maya_cmds, preserve):
    clip = _clip(maya_cmds, mode="preserve")
    clip.nodes[0].channels[0].curve.keys[5].breakdown = True
    reduced = clip.reduce_keys(tolerance=0, preserve_breakdowns=preserve)
    assert _frames(reduced) == ([0, 5, 10] if preserve else [0, 10])
    source = _node(
        maya_cmds,
        "discrete",
        enumerate([0, 0, 0, 1, 1, 1, 1]),
        attr="visibility",
    )
    maya_cmds.keyTangent(
        source + ".visibility", edit=True, outTangentType="step"
    )
    clip = bdu.AnimationClip.capture([source], attributes=["visibility"])
    reduced = clip.reduce_keys(tolerance=100)
    assert _frames(reduced) == [0, 2, 3, 6]
    target, _ = _restore(maya_cmds, reduced)
    frames = [i / 10 for i in range(61)]
    assert _values(maya_cmds, target + ".visibility", frames) == _values(
        maya_cmds, source + ".visibility", frames
    )


@pytest.mark.parametrize("attr", ["tx", "rx", "sx"])
@pytest.mark.parametrize("tolerance,count", [(0.01, 3), (0.03, 2)])
def test_error_uses_public_value_units(maya_cmds, attr, tolerance, count):
    clip = _clip(maya_cmds, values=[0, 0.02, 0], attr=attr)
    maya_cmds.currentUnit(angle="rad", linear="m")
    reduced = clip.reduce_keys(tolerance=tolerance)
    assert len(_frames(reduced)) == count


@pytest.mark.parametrize("rate", [1 / 24, 1 / 29.97, 0.123456789])
def test_saved_frame_units_and_exact_subframes_survive_fps_changes(
    maya_cmds, rate
):
    clip = _clip(
        maya_cmds, mode="preserve", frames=[-2.75, -1.5, -0.25, 1, 2.25]
    )
    curve = replace(clip.nodes[0].channels[0].curve, seconds_per_frame=rate)
    channel = replace(clip.nodes[0].channels[0], curve=curve)
    clip = replace(
        clip,
        seconds_per_frame=rate,
        nodes=(replace(clip.nodes[0], channels=(channel,)),),
    )
    maya_cmds.currentUnit(time="ntsc")
    reduced = clip.reduce_keys(-1.5, 2.25, tolerance=1e-5)
    assert _frames(reduced) == [-2.75, -1.5, 2.25]
    assert reduced.seconds_per_frame == rate
    assert reduced.nodes[0].channels[0].curve.seconds_per_frame == rate
    assert (reduced.start_frame, reduced.end_frame, reduced.sample_by) == (
        clip.start_frame,
        clip.end_frame,
        clip.sample_by,
    )


@pytest.mark.parametrize("values", [[2], [2, 2], [2] * 11])
def test_constant_single_and_two_key_channels_stay_independent(
    maya_cmds, values
):
    clip = _clip(maya_cmds, values=values)
    before = clip.to_dict()
    reduced = clip.reduce_keys(tolerance=0)
    assert _frames(reduced) == (
        [0] if len(values) == 1 else [0, len(values) - 1]
    )
    reduced.nodes[0].channels[0].curve.keys[0].value = 99
    assert clip.to_dict() == before


@pytest.mark.parametrize("dirty", [False, True])
@pytest.mark.parametrize("fail", [False, True])
def test_scene_history_pending_edits_and_input_survive_success_or_late_failure(
    maya_cmds, monkeypatch, dirty, fail
):
    clip = _clip(maya_cmds)
    clip = replace(
        clip,
        nodes=(clip.nodes[0], replace(clip.nodes[0], name="deleted_source")),
    )
    before = clip.to_dict()
    maya_cmds.delete(clip.nodes[0].name)
    maya_cmds.createNode("transform", name="selected")
    maya_cmds.currentTime(19)
    maya_cmds.setAttr("selected.ty", 8)
    maya_cmds.undo()
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    nodes.create.multiplyDivide(name="pending")
    nodes.existing("selected").tx.keyframe.set_key(99, frame=7)
    maya_cmds.file(modified=dirty)
    scene = _state(maya_cmds)
    original = _keyframe_reduce.reduce_curve
    calls = 0

    def reduce_curve(*args):
        nonlocal calls
        calls += 1
        original(*args)
        if fail and calls == 2:
            raise RuntimeError("late reduction failure")

    monkeypatch.setattr(_keyframe_reduce, "reduce_curve", reduce_curve)
    if fail:
        with pytest.raises(RuntimeError, match="late reduction failure"):
            clip.reduce_keys(tolerance=0)
    else:
        assert all(
            len(n.channels[0].curve.keys) == 2
            for n in clip.reduce_keys(tolerance=0).nodes
        )
    assert clip.to_dict() == before
    assert _state(maya_cmds) == scene
    assert not maya_cmds.objExists("pending")
    assert not maya_cmds.keyframe("selected.tx", query=True)
    mod.do_it_dg()
    assert maya_cmds.objExists("pending")
    assert _values(maya_cmds, "selected.tx", [7]) == [99]


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"tolerance": -1}, ValueError),
        ({"tolerance": float("nan")}, ValueError),
        ({"tolerance": float("inf")}, ValueError),
        ({"tolerance": True}, TypeError),
        ({"tolerance": "0.1"}, TypeError),
        ({"tolerance": 0, "preserve_breakdowns": 1}, TypeError),
        ({"tolerance": 0, "start_frame": float("inf")}, ValueError),
        ({"tolerance": 0, "end_frame": "5"}, TypeError),
        ({"tolerance": 0, "start_frame": True}, TypeError),
        ({"tolerance": 0, "start_frame": 8, "end_frame": 2}, ValueError),
        ({"tolerance": 0, "start_frame": 1e30}, ValueError),
    ],
)
def test_invalid_arguments_do_not_change_clip_or_scene(
    maya_cmds, kwargs, error
):
    clip = _clip(maya_cmds)
    before = clip.to_dict()
    maya_cmds.file(modified=False)
    scene = _state(maya_cmds)
    with pytest.raises(error):
        clip.reduce_keys(**kwargs)
    assert clip.to_dict() == before
    assert _state(maya_cmds) == scene


@pytest.mark.parametrize(
    "field,value",
    [
        ("value", float("nan")),
        ("in_tangent_type", "unknown"),
        ("frame", 1e30),
        ("frame", 1e-20),
    ],
)
def test_mutated_key_data_is_revalidated(maya_cmds, field, value):
    clip = _clip(maya_cmds)
    setattr(clip.nodes[0].channels[0].curve.keys[1], field, value)
    with pytest.raises((TypeError, ValueError)):
        clip.reduce_keys(tolerance=0)


def test_empty_nodes_and_curves_keep_target_mapping(maya_cmds):
    clip = _clip(maya_cmds)
    node = clip.nodes[0]
    empty = replace(
        node.channels[0],
        attribute="translateY",
        curve=replace(node.channels[0].curve, keys=()),
    )
    clip = replace(
        clip,
        nodes=(
            NodeAnimationData("empty", ()),
            replace(node, channels=(*node.channels, empty)),
        ),
    )
    reduced = clip.reduce_keys(tolerance=0)
    assert [n.name for n in reduced.nodes] == ["empty", node.name]
    assert reduced.nodes[0].channels == ()
    assert reduced.nodes[1].channels[1] == empty
    assert len(reduced.nodes[1].channels[0].curve.keys) == 2


@pytest.mark.parametrize("override", [False, True])
def test_layer_channels_reduce_but_root_and_layer_settings_do_not(
    maya_cmds, override
):
    source = _clip(maya_cmds).nodes[0].name
    layer = _layer(maya_cmds, source, override=override)
    root = maya_cmds.animLayer(query=True, root=True)
    for setting in (layer + ".weight", root + ".weight"):
        for frame in range(11):
            maya_cmds.setKeyframe(
                setting,
                time=frame,
                value=0.5,
                inTangentType="linear",
                outTangentType="linear",
            )
    for frame in range(11):
        maya_cmds.setKeyframe(
            source + ".tx",
            animLayer=layer,
            time=frame,
            value=3,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    clip = bdu.AnimationClip.capture(
        [source],
        attributes=["tx", "ty"],
        layer_mode="preserve",
        include_static=True,
    )
    before = clip.to_dict()
    reduced = clip.reduce_keys(tolerance=0)
    assert reduced.layers == clip.layers
    assert reduced.root_settings == clip.root_settings
    assert reduced.nodes[0].name == clip.nodes[0].name
    assert all(len(ch.curve.keys) == 2 for ch in reduced.nodes[0].channels)
    target, _ = _restore(maya_cmds, reduced)
    assert _values(maya_cmds, target + ".tx") == pytest.approx(
        _values(maya_cmds, source + ".tx")
    )
    weight = next(s for s in reduced.layers[0].settings if s.name == "weight")
    weight.curve.keys[0].value = 0.9
    assert clip.to_dict() == before


def test_flatten_error_is_not_destination_layer_composition_error(maya_cmds):
    clip = _clip(maya_cmds, values=[5, 5, 5])
    reduced = clip.reduce_keys(tolerance=0)
    assert _frames(reduced) == [0, 2]
    target = _node(maya_cmds, "target", ())
    layer = _layer(maya_cmds, target)
    layer_curve = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )
    maya_cmds.cutKey(layer_curve, clear=True)
    for frame, value in ((0, 0), (1, 10), (2, 0)):
        maya_cmds.setKeyframe(
            target + ".tx",
            animLayer=layer,
            time=frame,
            value=value,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    mod = bdu.ModifierManager()
    clip.restore(mod, targets=[target], mode="replace_all", tolerance=0)
    mod.do_it_dg()
    assert _values(maya_cmds, target + ".tx", [0, 1, 2]) == [5, 5, 5]
    reduced.restore(mod, targets=[target], mode="replace_all", tolerance=0)
    mod.do_it_dg()
    assert _values(maya_cmds, target + ".tx", [0, 1, 2]) == [5, 15, 5]


def test_reduced_clip_restore_rollback_and_queued_copy(maya_cmds):
    reduced = _clip(maya_cmds).reduce_keys(tolerance=0)
    target = _node(maya_cmds, "target", ((0, 20), (10, 20)))
    mod = bdu.ModifierManager()
    reduced.restore(mod, targets=[target], mode="replace_all")

    def fail(modifier):
        raise RuntimeError("restore failure")

    mod.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError, match="restore failure"):
        mod.do_it_dg()
    assert _values(maya_cmds, target + ".tx") == [20, 20, 20]
    reduced.restore(mod, targets=[target], mode="replace_all")
    reduced.nodes[0].channels[0].curve.keys[0].value = 100
    mod.do_it_dg()
    assert _values(maya_cmds, target + ".tx", [0, 5, 10]) == [0, 5, 10]


@pytest.mark.parametrize("weighted", [False, True])
def test_between_key_excursions_are_not_lost(maya_cmds, weighted):
    clip = _clip(maya_cmds, mode="preserve", values=[0] * 6)
    node = clip.nodes[0]
    channel = node.channels[0]
    curve = replace(channel.curve, weighted=weighted)
    for key in curve.keys:
        key.in_tangent_type = key.out_tangent_type = "fixed"
        key.in_tangent_xy = (0.01, 0.02)
        key.out_tangent_xy = (0.01, -0.02)
        key.tangents_locked = False
    clip = replace(
        clip, nodes=(replace(node, channels=(replace(channel, curve=curve),)),)
    )
    assert clip.reduce_keys(tolerance=1e-6) == clip


@pytest.mark.parametrize("locked", [False, True])
def test_short_weighted_fixed_tangents_survive_data_reduction(
    maya_cmds, locked
):
    clip = _clip(maya_cmds, mode="preserve", values=[2] * 6)
    node = clip.nodes[0]
    channel = node.channels[0]
    curve = replace(channel.curve, weighted=True)
    for key in curve.keys:
        key.in_tangent_type = key.out_tangent_type = "fixed"
        key.in_tangent_xy = (1e-8, 0)
        key.out_tangent_xy = (1e-8 if locked else 2e-8, 0)
        key.tangents_locked = key.weights_locked = locked
    clip = replace(
        clip, nodes=(replace(node, channels=(replace(channel, curve=curve),)),)
    )
    reduced = clip.reduce_keys(tolerance=0)
    assert _frames(reduced) == [0, 5]
    for actual, expected in zip(
        reduced.nodes[0].channels[0].curve.keys,
        (curve.keys[0], curve.keys[-1]),
    ):
        assert actual.in_tangent_xy == pytest.approx(
            expected.in_tangent_xy, abs=1e-16
        )
        assert actual.out_tangent_xy == pytest.approx(
            expected.out_tangent_xy, abs=1e-16
        )
        assert actual.tangents_locked == actual.weights_locked == locked


@pytest.mark.parametrize("stage", ["restore", "capture"])
@pytest.mark.parametrize("dirty", [False, True])
def test_work_curve_failure_restores_scene_state(
    maya_cmds, monkeypatch, stage, dirty
):
    clip = _clip(maya_cmds)
    original = clip.to_dict()
    maya_cmds.file(modified=dirty)
    scene = _state(maya_cmds)
    module, name = (
        (_keyframe_move, "restore_keys")
        if stage == "restore"
        else (_keyframe_snapshot, "_capture_curve")
    )
    implementation = getattr(module, name)

    def fail(*args, **kwargs):
        implementation(*args, **kwargs)
        raise RuntimeError("working curve failure")

    monkeypatch.setattr(module, name, fail)
    with pytest.raises(RuntimeError, match="working curve failure"):
        clip.reduce_keys(tolerance=0)
    assert clip.to_dict() == original
    assert _state(maya_cmds) == scene
