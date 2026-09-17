from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
    _keyframe_move,
    _keyframe_scale,
)
from test_keyframe_move import _make, _time, _history, _assert_state
from test_keyframe_set_equivalence import (
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "args,timing,expected",
    [
        ((10, 30), dict(time_scale=2), [(0, 0), (10, 4), (30, 2), (50, 7)]),
        (
            (10, 30),
            dict(duration_frames=10),
            [(0, 0), (10, 4), (15, 2), (20, 7)],
        ),
        (
            (10, 30),
            dict(to_start_frame=100, to_end_frame=140),
            [(0, 0), (100, 4), (120, 2), (140, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, to_end_frame=30),
            [(-10, 4), (10, 2), (30, 7)],
        ),
        (
            (10, 30),
            dict(duration_frames=10, to_end_frame=40),
            [(0, 0), (30, 4), (35, 2), (40, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=0.5, offset_frames=-10.25),
            [(-0.25, 4), (4.75, 2), (9.75, 7)],
        ),
        (
            (10, None),
            dict(time_scale=2, to_start_frame=20),
            [(0, 0), (20, 4), (40, 2), (60, 7)],
        ),
        ((None, 20), dict(time_scale=2), [(0, 0), (20, 4), (40, 2)]),
        ((), dict(time_scale=0.5), [(0, 0), (5, 4), (10, 2), (15, 7)]),
        ((12, 28), dict(time_scale=2), [(0, 0), (10, 4), (28, 2)]),
        (
            (12, 28),
            dict(duration_frames=8, to_start_frame=40),
            [(0, 0), (10, 4), (30, 7), (44, 2)],
        ),
    ],
)
def test_placement_and_overlapping_ranges(maya_cmds, args, timing, expected):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    assert keyframe.scale_keys(*args, **timing) is None
    assert keyframe.frames() == [0, 10, 20, 30]
    assert _curve_state(curve) == before
    mod.do_it_dg()
    assert keyframe.get_keys() == pytest.approx(expected)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("mode", ["replace_range", "merge"])
@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=2, to_start_frame=30),
        dict(to_start_frame=30, to_end_frame=50),
    ],
)
def test_destination_range_includes_missing_bounds_and_only_merge_retains_interior(
    maya_cmds, mode, timing
):
    keyframe, mod, curve = _make(maya_cmds)
    for frame, value in ((31, 31), (35, 35), (40, 40), (50, 50), (51, 51)):
        curve.addKey(_time(frame), value)
    before = _curve_state(curve)
    keyframe.scale_keys(15, 25, mode=mode, **timing)
    mod.do_it_dg()
    expected = [(0, 0), (10, 4), (40, 2), (51, 51)]
    if mode == "merge":
        expected = sorted(expected + [(30, 7), (31, 31), (35, 35), (50, 50)])
    assert keyframe.get_keys() == expected
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent",
    [
        "fixed",
        "auto",
        "linear",
        "step",
        "stepnext",
        "clamped",
        "plateau",
        "flat",
        "spline",
        "fast",
        "slow",
        "autocustom",
        "autoease",
        "automix",
    ],
)
@pytest.mark.parametrize("scale", [0.25, 2])
def test_shape_metadata_and_history(maya_cmds, kind, weighted, tangent, scale):
    keyframe, mod, curve = _make(maya_cmds, kind, weighted)
    name = om.MFnDependencyNode(curve.object()).name()
    if tangent != "fixed":
        maya_cmds.keyTangent(
            name,
            edit=True,
            inTangentType=(
                "linear" if tangent in ("step", "stepnext") else tangent
            ),
            outTangentType=tangent,
        )
    before = _curve_state(curve)
    samples = [i / 4 for i in range(-12, 132)]

    def value(fn, frame):
        result = fn.evaluate(_time(frame))
        return (
            result.asUnits(om.MTime.kSeconds)
            if isinstance(result, om.MTime)
            else result
        )

    expected = [value(curve, t) for t in samples]
    if tangent in ("fast", "slow"):
        reference = maya_cmds.duplicate(name)[0]
        maya_cmds.scaleKey(reference, timeScale=scale, timePivot=0)
        fn = oma.MFnAnimCurve(
            om.MSelectionList().add(reference).getDependNode(0)
        )
        expected = [value(fn, t * scale) for t in samples]
    keyframe.scale_keys(time_scale=scale, to_start_frame=40)
    mod.do_it_dg()
    after = _curve_state(curve)
    assert before["curve"] == after["curve"]
    for a, b in zip(after["keys"], before["keys"]):
        assert a["flags"] == b["flags"]
        assert a["numeric"][1] == pytest.approx(b["numeric"][1])
        if tangent == "fixed" and kind != "animCurveTT":
            for index in (2, 4):
                x, y = a["numeric"][index : index + 2]
                old_x, old_y = b["numeric"][index : index + 2]
                assert math.atan2(y, x) == pytest.approx(
                    math.atan2(old_y, old_x * scale), abs=1e-7
                )
                if weighted:
                    assert (x, y) == pytest.approx(
                        (old_x * scale, old_y), rel=1e-6, abs=1e-7
                    )
    assert [value(curve, 40 + t * scale) for t in samples] == pytest.approx(
        expected, abs=2e-6
    )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
@pytest.mark.parametrize(
    "bounds", [(12, 18), (-10, 40), (None, 18), (12, None), (12, 12)]
)
def test_missing_boundaries_sample_original_curve(maya_cmds, kind, bounds):
    keyframe, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    low = 0 if bounds[0] is None else bounds[0]
    high = 30 if bounds[1] is None else bounds[1]
    frames = sorted(
        set(
            [f for f in (0, 10, 20, 30) if low <= f <= high]
            + [f for f in bounds if f is not None]
        )
    )
    values = [curve.evaluate(_time(f)) for f in frames]
    keyframe.scale_keys(
        *bounds, time_scale=2, to_start_frame=60, insert_missing=True
    )
    mod.do_it_dg()
    for frame, wanted in zip(frames, values):
        result = curve.evaluate(_time(60 + (frame - low) * 2))
        assert (
            result == wanted
            if isinstance(wanted, om.MTime)
            else result == pytest.approx(wanted)
        )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("insert_missing", [False, True])
@pytest.mark.parametrize(
    "bounds,timing",
    [
        ((12, 18), dict(time_scale=1)),
        ((12, 18), dict(duration_frames=6)),
        ((1, 5), dict(duration_frames=4)),
        ((12, 28), dict(to_start_frame=12, to_end_frame=28)),
        ((), dict(time_scale=1, offset_frames=0)),
        ((), dict(duration_frames=30, to_end_frame=30)),
    ],
)
def test_identity_is_noop_without_inserting(
    maya_cmds, insert_missing, bounds, timing
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    keyframe.scale_keys(*bounds, **timing, insert_missing=insert_missing)
    mod.do_it_dg()
    assert _curve_state(curve) == before
    assert not maya_cmds.file(query=True, modified=True)


@pytest.mark.parametrize("empty", ["curve", "keys", "missing"])
def test_no_target_does_not_erase_destination_or_create_curve(
    maya_cmds, empty
):
    keyframe, mod, curve = _make(maya_cmds)
    if empty == "curve":
        for i in reversed(range(curve.numKeys)):
            curve.remove(i)
    elif empty == "missing":
        name = maya_cmds.createNode("transform")
        keyframe = (
            bdu.Nodes(modifier_manager=mod)
            .existing.transform(name)
            .tx.keyframe
        )
    before, nodes = keyframe.get_keys(), set(maya_cmds.ls())
    keyframe.scale_keys(
        12,
        18,
        to_start_frame=0,
        to_end_frame=30,
        insert_missing=empty != "keys",
    )
    mod.do_it_dg()
    assert keyframe.get_keys() == before
    assert set(maya_cmds.ls()) == nodes


@pytest.mark.parametrize(
    "bounds,kwargs,error",
    [
        ((), {}, ValueError),
        ((), dict(to_start_frame=30), ValueError),
        ((), dict(time_scale=2, duration_frames=10), ValueError),
        (
            (),
            dict(time_scale=2, to_start_frame=10, to_end_frame=20),
            ValueError,
        ),
        (
            (),
            dict(time_scale=2, offset_frames=10, to_end_frame=20),
            ValueError,
        ),
        ((), dict(to_start_frame=10, to_end_frame=10), ValueError),
        ((), dict(to_start_frame=20, to_end_frame=10), ValueError),
        ((20, 10), dict(time_scale=2), ValueError),
        ((10, 10), dict(duration_frames=10), ValueError),
        ((10, 10), dict(to_start_frame=20, to_end_frame=30), ValueError),
        ((), dict(time_scale=0), ValueError),
        ((), dict(time_scale=-2), ValueError),
        ((), dict(time_scale=float("inf")), ValueError),
        ((), dict(duration_frames=float("nan")), ValueError),
        ((), dict(duration_frames=0), ValueError),
        ((), dict(time_scale=True), TypeError),
        ((), dict(time_scale="2"), TypeError),
        ((True, 10), dict(time_scale=2), TypeError),
        ((), dict(time_scale=2, to_start_frame=float("inf")), ValueError),
        ((), dict(time_scale=2, offset_frames=1e300), ValueError),
        ((), dict(time_scale=2, mode="replace_all"), ValueError),
        ((), dict(time_scale=2, insert_missing=1), TypeError),
    ],
)
def test_invalid_arguments_are_rejected_before_queuing(
    maya_cmds, bounds, kwargs, error
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        keyframe.scale_keys(*bounds, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=2, to_start_frame=40),
        dict(duration_frames=60, to_end_frame=100),
        dict(to_start_frame=40, to_end_frame=100),
    ],
)
@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
def test_units_captured_at_booking(maya_cmds, timing, kind):
    keyframe, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    keyframe.scale_keys(**timing)
    maya_cmds.currentUnit(
        time="ntsc", angle="rad", linear="m", updateAnimation=True
    )
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == [40, 60, 80, 100]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("stage", ["insert", "remove", "restore"])
def test_partial_failure_rolls_back_every_edit(maya_cmds, monkeypatch, stage):
    keyframe, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keyframe.set_key(99, frame=80)
    helper = "insert_boundaries" if stage == "insert" else "_restore"
    module = _keyframe_move if stage == "insert" else _keyframe_scale
    original = getattr(module, helper)

    def fail(*args):
        if stage != "remove":
            original(*args)
        raise RuntimeError("injected scaling failure")

    monkeypatch.setattr(module, helper, fail)
    keyframe.scale_keys(
        12, 18, to_start_frame=0, to_end_frame=30, insert_missing=True
    )
    with pytest.raises(RuntimeError, match="injected scaling failure"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


def test_pending_creation_and_sequential_editing(maya_cmds):
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.animCurveTL(name="pending")
    keyframe = node.keyframe
    keyframe.set_keys([(10, 4), (20, 2), (30, 7)])
    keyframe.move_keys(offset_frames=10)
    keyframe.scale_keys(time_scale=2)
    keyframe.scale_keys(to_start_frame=0, to_end_frame=10)
    with pytest.raises(RuntimeError):
        keyframe.frames()
    assert not maya_cmds.objExists("pending")
    mod.do_it_dg()
    assert keyframe.get_keys() == [(0, 4), (5, 2), (10, 7)]
    for _ in range(2):
        mod.undo_it()
        assert not maya_cmds.objExists("pending")
        mod.redo_it()
        assert keyframe.get_keys() == [(0, 4), (5, 2), (10, 7)]


@pytest.mark.parametrize("mode", ["replace_range", "merge"])
@pytest.mark.parametrize("weighted", [False, True])
def test_partial_edit_preserves_unaffected_fixed_keys(
    maya_cmds, mode, weighted
):
    keyframe, mod, curve = _make(maya_cmds, weighted=weighted)
    before = _curve_state(curve)
    keyframe.scale_keys(10, 20, time_scale=0.5, to_start_frame=22, mode=mode)
    mod.do_it_dg()
    after = _curve_state(curve)
    assert keyframe.frames() == [0, 22, 27, 30]
    for index in (0, 3):
        assert after["keys"][index] == before["keys"][index]
    _history(mod, curve, before, after)


@pytest.mark.parametrize("kind", ["animCurveTA", "animCurveTL", "animCurveTU"])
def test_very_short_weighted_fixed_tangents_are_not_clamped(maya_cmds, kind):
    keyframe, mod, curve = _make(maya_cmds, kind, True)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, om.MAngle(0), 0.01, True)
        curve.setTangent(i, om.MAngle(0), 0.01, False)
    before = _curve_state(curve)
    keyframe.scale_keys(time_scale=0.01)
    mod.do_it_dg()
    for actual, expected in zip(_curve_state(curve)["keys"], before["keys"]):
        assert actual["numeric"][2] == pytest.approx(
            expected["numeric"][2] * 0.01, rel=1e-6, abs=1e-12
        )
    _history(mod, curve, before, _curve_state(curve))


def test_unrepresentable_weighted_time_tangent_rolls_back(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds, "animCurveTT", True)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, om.MAngle(0), 0.01, True)
        curve.setTangent(i, om.MAngle(0), 0.01, False)
    before = _curve_state(curve)
    keyframe.scale_keys(time_scale=0.01)
    with pytest.raises(RuntimeError, match="weighted time tangent"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)


@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=1e-20),
        dict(time_scale=1e300),
        dict(time_scale=1e-5, to_start_frame=1e12),
    ],
)
def test_collapsed_keys_or_overflow_roll_back_prior_work(maya_cmds, timing):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keyframe.set_key(99, frame=80)
    keyframe.scale_keys(**timing)
    with pytest.raises(ValueError):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)


@pytest.mark.parametrize(
    "timing",
    [dict(duration_frames=10), dict(to_start_frame=10, to_end_frame=20)],
)
def test_zero_width_inferred_at_execution_is_rejected(maya_cmds, timing):
    keyframe, mod, curve = _make(maya_cmds)
    for i in (3, 2, 1):
        curve.remove(i)
    before = _curve_state(curve)
    keyframe.scale_keys(**timing)
    with pytest.raises(ValueError, match="zero-width"):
        mod.do_it_dg()
    assert _curve_state(curve) == before


def test_single_key_at_pivot_keeps_time_and_scales_tangent(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keyframe.scale_keys(10, 10, time_scale=2)
    mod.do_it_dg()
    after = _curve_state(curve)
    assert keyframe.frames() == [0, 10, 20, 30]
    assert after["keys"][1]["numeric"][2] == pytest.approx(
        before["keys"][1]["numeric"][2] * 2, rel=1e-6
    )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("scale", [1, 2])
def test_noop_still_requires_manager_and_write_access(maya_cmds, scale):
    keyframe, mod, curve = _make(maya_cmds)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).scale_keys(time_scale=scale)
    keyframe.scale_keys(time_scale=scale)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()


def test_reconnection_and_rename_before_execution(maya_cmds):
    plug, original = _existing_curve(maya_cmds, "target", "doubleLinear")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    _, _, replacement = _make(maya_cmds)
    before = _curve_state(replacement)
    original_before = _curve_state(original)
    keyframe.scale_keys(time_scale=2)
    maya_cmds.disconnectAttr(original.name() + ".output", plug.name())
    maya_cmds.connectAttr(replacement.name() + ".output", plug.name())
    maya_cmds.rename(om.MFnDependencyNode(plug.node()).name(), "renamedTarget")
    mod.do_it_dg()
    assert keyframe.frames() == [0, 20, 40, 60]
    assert _curve_state(original) == original_before
    _history(mod, replacement, before, _curve_state(replacement))


@pytest.mark.parametrize("attribute_type", ["bool", "enum", "long"])
def test_discrete_channels_keep_values(maya_cmds, attribute_type):
    plug, curve = _existing_curve(maya_cmds, "target", attribute_type)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    before = _curve_state(curve)
    keyframe.scale_keys(time_scale=2)
    mod.do_it_dg()
    assert keyframe.frames() == [1, 9, 17]
    assert keyframe.values() == [1, 3, 2]
    _history(mod, curve, before, _curve_state(curve))
