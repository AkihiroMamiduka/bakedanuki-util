from __future__ import annotations

import math
import random

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
)
from bd_util.maya.node.operator.attr import _keyframe_reduce
from test_keyframe_move import _assert_state, _history
from test_keyframe_set_equivalence import (
    _curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _time(frame):
    return om.MTime(frame, om.MTime.kFilm)


def _make(
    cmds,
    values=None,
    *,
    kind="animCurveTL",
    weighted=False,
    tangent="linear",
    frames=None,
):
    values = list(range(11)) if values is None else values
    frames = list(range(len(values))) if frames is None else frames
    name = cmds.createNode(kind)
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    scale = math.pi / 180 if kind == "animCurveTA" else 1.0
    for frame, value in zip(frames, values):
        curve.addKey(
            _time(frame),
            value * scale,
            curve.kTangentLinear,
            curve.kTangentLinear,
        )
    curve.setIsWeighted(weighted)
    tangent_type = getattr(
        curve,
        "kTangent"
        + {
            "stepnext": "StepNext",
            "spline": "Smooth",
            "autoease": "AutoEase",
            "automix": "AutoMix",
        }.get(tangent, tangent.capitalize()),
    )
    for i in range(curve.numKeys):
        curve.setInTangentType(
            i,
            (
                tangent_type
                if tangent not in ("step", "stepnext")
                else curve.kTangentFlat
            ),
        )
        curve.setOutTangentType(i, tangent_type)
    mod = bdu.ModifierManager()
    return (
        CurveKeyframeManager(curve.object(), modifier_manager=mod),
        mod,
        curve,
    )


def _sample(curve, frames):
    scale = 180 / math.pi if curve.animCurveType == curve.kAnimCurveTA else 1
    return [curve.evaluate(_time(frame)) * scale for frame in frames]


@pytest.mark.parametrize("kind", ["animCurveTA", "animCurveTL", "animCurveTU"])
@pytest.mark.parametrize("weighted", [False, True])
def test_straight_curve_reduction_is_deferred_and_undoable(
    maya_cmds, kind, weighted
):
    keyframe, mod, curve = _make(maya_cmds, kind=kind, weighted=weighted)
    before = _curve_state(curve)
    frames = [i / 10 for i in range(-20, 121)]
    expected = _sample(curve, frames)
    assert keyframe.reduce_keys(tolerance=1e-6) is None
    assert _curve_state(curve) == before
    assert keyframe.key_count() == 11
    mod.do_it_dg()
    assert keyframe.frames() == [0, 10]
    assert _sample(curve, frames) == pytest.approx(expected, abs=1e-6)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "args,expected",
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
def test_range_contains_ends_without_inserting_keys(maya_cmds, args, expected):
    keyframe, mod, _ = _make(maya_cmds)
    keyframe.reduce_keys(*args, tolerance=0)
    mod.do_it_dg()
    assert keyframe.frames() == expected


@pytest.mark.parametrize("preserve", [True, False])
def test_breakdown_protection_can_be_explicitly_disabled(maya_cmds, preserve):
    keyframe, mod, curve = _make(maya_cmds)
    curve.setIsBreakdown(5, True)
    before = _curve_state(curve)
    keyframe.reduce_keys(tolerance=0, preserve_breakdowns=preserve)
    mod.do_it_dg()
    assert keyframe.frames() == ([0, 5, 10] if preserve else [0, 10])
    if preserve:
        assert curve.isBreakdown(1)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent",
    ["auto", "spline", "clamped", "plateau", "autoease", "automix", "linear"],
)
def test_recomputed_tangents_are_compared_to_original(
    maya_cmds, weighted, tangent
):
    values = [0, 0.08, 0.12, 0.16, 0.20, 0.12, 0.06, 0]
    keyframe, mod, curve = _make(
        maya_cmds, values, weighted=weighted, tangent=tangent
    )
    frames = [i / 100 for i in range(701)]
    before = _curve_state(curve)
    expected = _sample(curve, frames)
    keyframe.reduce_keys(tolerance=0.06)
    mod.do_it_dg()
    assert curve.numKeys < len(values)
    assert (
        max(abs(a - b) for a, b in zip(expected, _sample(curve, frames)))
        <= 0.06 + 1e-10
    )
    for key in _curve_state(curve)["keys"]:
        original = next(
            k for k in before["keys"] if k["numeric"][0] == key["numeric"][0]
        )
        assert original["flags"] == key["flags"]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("locked", [False, True])
def test_fixed_tangents_locks_values_and_curve_settings_remain(
    maya_cmds, weighted, locked
):
    keyframe, mod, curve = _make(
        maya_cmds, [2] * 8, weighted=weighted, tangent="flat"
    )
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, om.MAngle(0), 0.004, True)
        curve.setTangent(i, om.MAngle(0), 0.007, False)
        curve.setWeightsLocked(i, locked)
        curve.setTangentsLocked(i, locked)
    curve.setPreInfinityType(curve.kCycleRelative)
    curve.setPostInfinityType(curve.kOscillate)
    before = _curve_state(curve)
    keyframe.reduce_keys(tolerance=0)
    mod.do_it_dg()
    assert keyframe.frames() == [0, 7]
    after = _curve_state(curve)
    _assert_state(
        after,
        {
            "curve": before["curve"],
            "keys": [before["keys"][0], before["keys"][-1]],
        },
    )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("weighted", [False, True])
def test_equal_key_values_do_not_hide_between_key_excursions(
    maya_cmds, weighted
):
    keyframe, mod, curve = _make(maya_cmds, [0] * 6, weighted=weighted)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setTangent(i, om.MAngle(0.7), 0.005, True)
        curve.setTangent(i, om.MAngle(-0.7), 0.005, False)
    before = _curve_state(curve)
    keyframe.reduce_keys(tolerance=1e-6)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize("kind", ["animCurveTA", "animCurveTL", "animCurveTU"])
@pytest.mark.parametrize("tolerance,count", [(0.01, 3), (0.03, 2)])
def test_tolerance_is_in_public_units_independent_of_scene_units(
    maya_cmds, kind, tolerance, count
):
    keyframe, mod, _ = _make(maya_cmds, [0, 0.02, 0], kind=kind)
    keyframe.reduce_keys(tolerance=tolerance)
    maya_cmds.currentUnit(angle="rad", linear="m")
    mod.do_it_dg()
    assert keyframe.key_count() == count


@pytest.mark.parametrize("tangent", ["step", "stepnext"])
def test_step_transition_keys_survive_even_large_tolerance(maya_cmds, tangent):
    keyframe, mod, curve = _make(
        maya_cmds, [0, 0, 0, 1, 1, 1, 1], tangent=tangent
    )
    frames = [i / 20 for i in range(121)]
    values = _sample(curve, frames)
    keyframe.reduce_keys(tolerance=100)
    mod.do_it_dg()
    assert keyframe.frames() == [0, 2, 3, 6]
    assert _sample(curve, frames) == values


def test_partial_reduction_keeps_outside_shape(maya_cmds):
    keyframe, mod, curve = _make(
        maya_cmds, [0, 2, 1, 1.1, 2, 1, 0.9, 3, 4], tangent="spline"
    )
    frames = [i / 100 for i in range(801) if i < 250 or i > 650]
    expected = _sample(curve, frames)
    keyframe.reduce_keys(2.5, 6.5, tolerance=10)
    mod.do_it_dg()
    assert _sample(curve, frames) == pytest.approx(expected, abs=1e-11)


@pytest.mark.parametrize("side", ["pre", "post"])
def test_linear_infinity_slope_is_preserved(maya_cmds, side):
    keyframe, mod, curve = _make(maya_cmds, [0, 1, 1.1, 2])
    getattr(curve, "set" + side.capitalize() + "InfinityType")(curve.kLinear)
    frames = [-10000, -1] if side == "pre" else [4, 10000]
    expected = _sample(curve, frames)
    keyframe.reduce_keys(tolerance=100)
    mod.do_it_dg()
    assert _sample(curve, frames) == pytest.approx(expected, abs=1e-9)


def test_negative_subframe_bounds_capture_time_unit(maya_cmds):
    keyframe, mod, curve = _make(
        maya_cmds, frames=[-2.5 + i * 0.5 for i in range(11)]
    )
    before = _curve_state(curve)
    keyframe.reduce_keys(-2, 2, tolerance=0)
    maya_cmds.currentUnit(time="ntsc", updateAnimation=True)
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == [-2.5, -2, 2, 2.5]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("values", [[], [1], [1, 2], [0, 1, 0]])
def test_noop_does_not_leave_work_nodes_or_dirty_scene(maya_cmds, values):
    keyframe, mod, curve = _make(maya_cmds, values)
    before = _curve_state(curve)
    nodes = set(maya_cmds.ls())
    maya_cmds.file(modified=False)
    keyframe.reduce_keys(tolerance=0)
    mod.do_it_dg()
    assert set(maya_cmds.ls()) == nodes
    assert not maya_cmds.file(query=True, modified=True)
    assert _curve_state(curve) == before


def test_missing_curve_is_not_created(maya_cmds):
    node = maya_cmds.createNode("transform")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing.transform(node).tx.keyframe
    )
    keyframe.reduce_keys(tolerance=1)
    mod.do_it_dg()
    assert not keyframe.has_anim_curve()


@pytest.mark.parametrize(
    "args,kwargs,error",
    [
        ((), {}, TypeError),
        ((), {"tolerance": -1}, ValueError),
        ((), {"tolerance": math.nan}, ValueError),
        ((), {"tolerance": math.inf}, ValueError),
        ((), {"tolerance": "1"}, TypeError),
        ((), {"tolerance": True}, TypeError),
        ((), {"tolerance": 0, "preserve_breakdowns": 1}, TypeError),
        ((2, 1), {"tolerance": 0}, ValueError),
        ((math.nan, None), {"tolerance": 0}, ValueError),
        ((None, math.inf), {"tolerance": 0}, ValueError),
        ((1e15, None), {"tolerance": 0}, ValueError),
    ],
)
def test_invalid_arguments_do_not_queue(maya_cmds, args, kwargs, error):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        keyframe.reduce_keys(*args, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


def test_pending_keys_then_reduction_and_query(maya_cmds):
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.animCurveTL(
        name="reducePending"
    )
    keyframe = node.keyframe
    keyframe.set_keys(
        [(i, i) for i in range(11)],
        in_tangent_type="linear",
        out_tangent_type="linear",
    )
    keyframe.reduce_keys(tolerance=0)
    assert not maya_cmds.objExists("reducePending")
    mod.do_it_dg()
    assert keyframe.frames() == [0, 10]
    mod.undo_it()
    assert not maya_cmds.objExists("reducePending")
    mod.redo_it()
    assert keyframe.frames() == [0, 10]


@pytest.mark.parametrize("stage", ["planning", "final_check", "later_edit"])
def test_failure_rolls_back_reduction_and_prior_edits(
    maya_cmds, monkeypatch, stage
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keyframe.set_key(
        20, frame=20, in_tangent_type="linear", out_tangent_type="linear"
    )
    original_compare = _keyframe_reduce._compare

    def compare(actual, *args, **kwargs):
        if stage == "planning" or (
            stage == "final_check" and actual.object() == curve.object()
        ):
            raise RuntimeError("intentional reduction failure")
        return original_compare(actual, *args, **kwargs)

    monkeypatch.setattr(_keyframe_reduce, "_compare", compare)
    keyframe.reduce_keys(tolerance=0)
    if stage == "later_edit":

        def fail(change):
            raise RuntimeError("intentional reduction failure")

        mod.queue_anim_curve_change(fail)
    nodes = set(maya_cmds.ls())
    with pytest.raises(RuntimeError, match="intentional reduction failure"):
        mod.do_it_dg()
    assert set(maya_cmds.ls()) == nodes
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo


def test_time_output_is_explicitly_unsupported(maya_cmds):
    node = maya_cmds.createNode("transform")
    maya_cmds.addAttr(node, longName="timeValue", attributeType="time")
    plug = om.MSelectionList().add(node + ".timeValue").getPlug(0)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    keyframe.reduce_keys(tolerance=0)
    with pytest.raises(RuntimeError, match="TA / TL / TU"):
        mod.do_it_dg()


def test_missing_modifier_is_rejected(maya_cmds):
    _, _, curve = _make(maya_cmds)
    keyframe = CurveKeyframeManager(curve.object())
    with pytest.raises(RuntimeError, match="ModifierManager"):
        keyframe.reduce_keys(tolerance=0)


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent",
    [
        "fixed",
        "linear",
        "auto",
        "spline",
        "autoease",
        "automix",
        "step",
        "stepnext",
    ],
)
def test_error_geometry_matches_maya_evaluation(maya_cmds, weighted, tangent):
    _, _, curve = _make(
        maya_cmds,
        [0, 0.01, -0.02, 0.04, 0.01],
        weighted=weighted,
        tangent=tangent,
    )
    if tangent == "fixed":
        for i in range(curve.numKeys):
            curve.setTangentsLocked(i, False)
            curve.setTangent(i, om.MAngle(0.2), 0.001, True)
            curve.setTangent(i, om.MAngle(-0.4), 0.004, False)
    supported = 0
    for i in range(curve.numKeys - 1):
        segment = _keyframe_reduce._segment(
            _keyframe_reduce._key(curve, i),
            _keyframe_reduce._key(curve, i + 1),
            weighted,
            1,
        )
        if not segment.supported:
            continue
        supported += 1
        for fraction in (0.001, 0.07, 0.31, 0.5, 0.78, 0.99):
            seconds = segment.x[0] + (segment.x[-1] - segment.x[0]) * fraction
            value = segment.split(seconds)[0].y[-1]
            assert value == pytest.approx(
                curve.evaluate(om.MTime(seconds, om.MTime.kSeconds)), abs=1e-9
            )
    assert supported > 0


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("seed", range(5))
def test_accumulated_reduction_error_against_dense_native_samples(
    maya_cmds, weighted, seed
):
    rng = random.Random(seed)
    values = [math.sin(i / 5) + rng.uniform(-0.02, 0.02) for i in range(31)]
    keyframe, mod, curve = _make(
        maya_cmds, values, weighted=weighted, tangent="auto"
    )
    frames = [i / 80 for i in range(2401)]
    original = _sample(curve, frames)
    keyframe.reduce_keys(tolerance=0.04)
    mod.do_it_dg()
    assert curve.numKeys < 31
    assert (
        max(abs(a - b) for a, b in zip(original, _sample(curve, frames)))
        <= 0.04 + 1e-9
    )


@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("target", ["base", "layer"])
def test_reduction_respects_base_and_explicit_layer(
    maya_cmds, override, target
):
    from test_keyframe_anim_layer import _curve_name, _layered
    from test_keyframe_channel import _states
    from test_keyframe_default_layer import _prefer

    keyframe, mod, layers = _layered(maya_cmds, override=override)
    layer = (
        maya_cmds.animLayer(query=True, root=True)
        if target == "base"
        else layers[0]
    )
    name = _curve_name(maya_cmds, layer, keyframe.plug.name())
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    for i in range(11):
        curve.addKey(_time(i), i, curve.kTangentLinear, curve.kTangentLinear)
    _prefer(maya_cmds, layers[1])
    selected = keyframe if target == "base" else keyframe.anim_layer(layer)
    before = _states(maya_cmds)
    selected.reduce_keys(tolerance=0)
    mod.do_it_dg()
    assert selected.frames() == [0, 10]
    after = _states(maya_cmds)
    assert {n: s for n, s in after.items() if n != name} == {
        n: s for n, s in before.items() if n != name
    }
    mod.undo_it()
    assert _states(maya_cmds) == before
    mod.redo_it()
    assert _states(maya_cmds) == after


def test_unrepresentable_weighted_hull_is_conservatively_kept(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds, [0, 0, 0, 0], weighted=True)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setTangent(i, 0.3, 0.2, True, convertUnits=False)
        curve.setTangent(i, 0.3, -0.2, False, convertUnits=False)
    assert not _keyframe_reduce._segment(
        _keyframe_reduce._key(curve, 0),
        _keyframe_reduce._key(curve, 1),
        True,
        1,
    ).supported
    before = _curve_state(curve)
    keyframe.reduce_keys(tolerance=100)
    mod.do_it_dg()
    assert _curve_state(curve) == before


def test_explicit_shared_curve_reduction_keeps_connections(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds)
    names = [maya_cmds.createNode("transform") for _ in range(2)]
    for name in names:
        maya_cmds.connectAttr(curve.name() + ".output", name + ".tx")
    keyframe.reduce_keys(tolerance=0)
    mod.do_it_dg()
    assert keyframe.frames() == [0, 10]
    for name in names:
        assert maya_cmds.isConnected(curve.name() + ".output", name + ".tx")


def test_channel_target_is_resolved_after_reconnection(maya_cmds):
    _, _, first = _make(maya_cmds)
    _, _, second = _make(maya_cmds)
    node = maya_cmds.createNode("transform")
    maya_cmds.connectAttr(first.name() + ".output", node + ".tx")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing.transform(node).tx.keyframe
    )
    keyframe.reduce_keys(tolerance=0)
    maya_cmds.connectAttr(second.name() + ".output", node + ".tx", force=True)
    maya_cmds.rename(node, "renamedReductionTarget")
    mod.do_it_dg()
    assert first.numKeys == 11 and second.numKeys == 2
