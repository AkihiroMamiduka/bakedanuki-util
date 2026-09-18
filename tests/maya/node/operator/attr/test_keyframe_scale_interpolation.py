from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    _keyframe_move,
)
from test_keyframe_move import _make, _time, _assert_state, _history
from test_keyframe_move_interpolation import _curve as _move_curve
from test_keyframe_set_equivalence import (
    _curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _curve(cmds, kind="animCurveTL", weighted=False, tangent="fixed"):
    keys, mod, curve = _move_curve(cmds, kind, weighted, tangent)
    # Newly added fixed TT keys have zero weights, which Maya cannot restore.
    if kind == "animCurveTT" and weighted:
        for frame in (5, 25):
            index = curve.find(_time(frame))
            curve.setTangentsLocked(index, False)
            curve.setWeightsLocked(index, False)
            curve.setTangent(index, om.MAngle(0.3), 0.2, True)
            curve.setTangent(index, om.MAngle(-0.2), 0.3, False)
    return keys, mod, curve


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
@pytest.mark.parametrize(
    "timing,scale,low",
    [
        (dict(time_scale=1.25), 1.25, 10),
        (dict(duration_frames=12.5), 1.25, 10),
        (dict(to_start_frame=11, to_end_frame=23.5), 1.25, 11),
        (dict(time_scale=0.5, offset_frames=2), 0.5, 12),
        (dict(time_scale=0.5, to_start_frame=12), 0.5, 12),
        (dict(time_scale=0.5, to_end_frame=17), 0.5, 12),
        (dict(duration_frames=5, to_start_frame=12), 0.5, 12),
        (dict(duration_frames=5, to_end_frame=17), 0.5, 12),
    ],
)
def test_original_time_weights_and_all_placement_forms(
    maya_cmds, interpolation, timing, scale, low
):
    keys, mod, curve = _curve(maya_cmds)
    for frame in (2.5, 27.5):
        curve.addKey(_time(frame), frame)
    before = _curve_state(curve)
    frames, values = keys.frames(), keys.values()
    quarter = 0.25 if interpolation == "linear" else 0.15625
    weights = [0, quarter, 0.5, 1, 1, 0.5, quarter, 0]
    assert (
        keys.scale_keys(
            10,
            20,
            **timing,
            interpolate_start=0,
            interpolate_end=30,
            interpolation=interpolation,
        )
        is None
    )
    assert _curve_state(curve) == before
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(
        [f + (low + (f - 10) * scale - f) * w for f, w in zip(frames, weights)]
    )
    assert keys.values() == values
    _history(mod, curve, before, _curve_state(curve))


def test_documented_example(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    frames = [10, 15, 20, 25, 30, 40, 50]
    for f in frames:
        curve.addKey(_time(f), f)
    keys.scale_keys(
        20, 30, time_scale=1.5, interpolate_start=10, interpolate_end=50
    )
    mod.do_it_dg()
    assert keys.frames() == [10, 13.75, 20, 27.5, 35, 45, 50]
    assert keys.values() == frames


def test_default_interpolation_is_smoothstep(maya_cmds):
    keys, mod, curve = _curve(maya_cmds)
    curve.addKey(_time(2.5), 99)
    keys.scale_keys(
        10, 20, time_scale=1.5, interpolate_start=0, interpolate_end=30
    )
    mod.do_it_dg()
    assert keys.frames()[1] == pytest.approx(1.9140625)


def test_duplicate_main_boundary_is_inserted_once(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(
        15,
        15,
        time_scale=0.5,
        interpolate_start=5,
        interpolate_end=25,
        interpolation="linear",
        insert_missing=True,
    )
    mod.do_it_dg()
    assert keys.frames() == [0, 5, 11.25, 15, 18.75, 25, 30]
    _history(mod, curve, before, _curve_state(curve))


def test_unrepresentable_weighted_time_tangent_rolls_back(maya_cmds):
    keys, mod, curve = _move_curve(maya_cmds, "animCurveTT", True)
    assert curve.getTangentAngleWeight(curve.find(_time(5)), True)[1] == 0
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.scale_keys(
        10, 20, time_scale=1.5, interpolate_start=0, interpolate_end=30
    )
    with pytest.raises(RuntimeError, match="weighted time tangent"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("scale", [1, 1.5])
def test_even_noop_requires_manager_and_write_access(maya_cmds, scale):
    keys, mod, curve = _make(maya_cmds)
    kwargs = dict(time_scale=scale, interpolate_start=0, interpolate_end=30)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).scale_keys(10, 20, **kwargs)
    keys.scale_keys(10, 20, **kwargs)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "auto", "linear", "step", "stepnext"]
)
@pytest.mark.parametrize("scale", [0.5, 1.5])
def test_effective_tangent_scale_values_metadata_and_history(
    maya_cmds, kind, weighted, tangent, scale
):
    keys, mod, curve = _curve(maya_cmds, kind, weighted, tangent)
    before = _curve_state(curve)
    captured = [
        _keyframe_move.capture_key(curve, i) for i in range(curve.numKeys)
    ]
    keys.scale_keys(
        10, 20, time_scale=scale, interpolate_start=0, interpolate_end=30
    )
    mod.do_it_dg()
    after = _curve_state(curve)
    assert after["curve"] == before["curve"]
    for i, (a, b, w) in enumerate(
        zip(after["keys"], before["keys"], [0, 0.5, 1, 1, 0.5, 0])
    ):
        assert a["flags"] == b["flags"]
        assert a["numeric"][1] == b["numeric"][1]
        if a["flags"][:2] != (curve.kTangentFixed, curve.kTangentFixed):
            continue
        factor = 1 + w * (scale - 1)
        current = _keyframe_move.capture_key(curve, i)
        for actual, old in zip(
            (current.in_tangent, current.out_tangent),
            (captured[i].in_tangent, captured[i].out_tangent),
        ):
            x, y = old
            if isinstance(x, om.MAngle):
                old_x, old_y = (
                    math.cos(x.asRadians()) * y,
                    math.sin(x.asRadians()) * y,
                )
                assert actual[0].asRadians() == pytest.approx(
                    math.atan2(old_y, old_x * factor), abs=1e-7
                )
                if weighted:
                    assert actual[1] == pytest.approx(
                        math.hypot(old_x * factor, old_y), rel=1e-6
                    )
            else:
                assert actual == pytest.approx(
                    (x * factor, y), abs=1e-7, rel=1e-6
                )
        if w == 0:
            assert a["numeric"] == b["numeric"]
    _history(mod, curve, before, after)


@pytest.mark.parametrize("mode", ["replace_range", "merge"])
def test_replacement_uses_only_main_destination_and_overwrites_fade_collision(
    maya_cmds, mode
):
    keys, mod, curve = _curve(maya_cmds, weighted=True)
    for f in (21.25, 22, 40, 42, 45, 46):
        curve.addKey(_time(f), f)
    before = _curve_state(curve)
    # Core 10..20 -> 40..45, fade key 5 -> 21.25, outside the replaced range.
    keys.scale_keys(
        10,
        20,
        time_scale=0.5,
        to_start_frame=40,
        interpolate_start=0,
        mode=mode,
    )
    mod.do_it_dg()
    expected = [
        (0, 0),
        (21.25, 5),
        (22, 22),
        (25, 25),
        (30, 7),
        (40, 4),
        (45, 2),
        (46, 46),
    ]
    if mode == "merge":
        expected.insert(-2, (42, 42))
    assert keys.get_keys() == expected
    _history(mod, curve, before, _curve_state(curve))


def test_stationary_selected_endpoint_survives_replacement(maya_cmds):
    keys, mod, curve = _make(maya_cmds, weighted=True)
    curve.remove(curve.find(_time(20)))
    before = _curve_state(curve)
    # No key at the main end 20. Nominal destination 10..30 includes fixed fade endpoint 30.
    keys.scale_keys(10, 20, time_scale=2, interpolate_end=30)
    mod.do_it_dg()
    assert keys.frames() == [0, 10, 30]
    assert _curve_state(curve)["keys"][-1] == before["keys"][-1]
    assert _curve_state(curve)["keys"][1]["numeric"][2] == pytest.approx(
        before["keys"][1]["numeric"][2] * 2
    )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("scale", [2, 3])
@pytest.mark.parametrize("insert", [False, True])
def test_selected_collision_and_reversal_roll_back_prior_work(
    maya_cmds, scale, insert
):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.scale_keys(
        10,
        20,
        time_scale=scale,
        interpolate_start=0,
        interpolate_end=30,
        insert_missing=insert,
    )
    with pytest.raises(ValueError, match="coincide or change order"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("insert", [False, True])
def test_missing_fade_endpoint_is_not_a_virtual_key(maya_cmds, insert):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(
        10, 20, time_scale=2, interpolate_end=25, insert_missing=insert
    )
    if insert:
        with pytest.raises(ValueError, match="change order"):
            mod.do_it_dg()
        _assert_state(_curve_state(curve), before)
    else:
        mod.do_it_dg()
        assert keys.get_keys() == [(0, 0), (10, 4), (30, 2)]
        _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
@pytest.mark.parametrize("exterior", [False, True])
def test_four_boundaries_sample_original_curve(maya_cmds, kind, exterior):
    keys, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    start, end, low, high = (-5, 35, -10, 40) if exterior else (12, 18, 5, 25)
    frames = sorted([0, 10, 20, 30, start, end, low, high])
    values = [curve.evaluate(_time(f)) for f in frames]
    weights = [
        max(0, min(1, (f - low) / (start - low), (high - f) / (high - end)))
        for f in frames
    ]
    keys.scale_keys(
        start,
        end,
        time_scale=0.75,
        interpolate_start=low,
        interpolate_end=high,
        interpolation="linear",
        insert_missing=True,
    )
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(
        [
            f + (start + (f - start) * 0.75 - f) * w
            for f, w in zip(frames, weights)
        ]
    )
    for i, expected in enumerate(values):
        actual = curve.evaluate(curve.input(i))
        assert (
            actual == expected
            if isinstance(expected, om.MTime)
            else actual == pytest.approx(expected)
        )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "bounds,timing,expected",
    [
        (
            (10, None),
            dict(time_scale=0.5, interpolate_start=0),
            [0, 6.25, 10, 15, 17.5, 20],
        ),
        (
            (None, 20),
            dict(duration_frames=10, interpolate_end=30),
            [0, 2.5, 5, 10, 18.75, 30],
        ),
        (
            (12, 18),
            dict(
                time_scale=0.5,
                interpolate_start=0,
                interpolate_end=30,
                interpolation="linear",
            ),
            [0, 5 + 3.5 * 5 / 12, 10 + 5 / 6, 20 - 10 / 3, 25 - 32.5 / 12, 30],
        ),
        (
            (10, 10),
            dict(
                time_scale=1.5,
                interpolate_start=0,
                interpolate_end=30,
                interpolation="linear",
            ),
            [0, 3.75, 10, 22.5, 26.875, 30],
        ),
    ],
)
def test_open_empty_core_and_zero_width_ranges(
    maya_cmds, bounds, timing, expected
):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(*bounds, **timing)
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(expected)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("insert", [False, True])
def test_missing_implicit_anchor_uses_only_main_keys(maya_cmds, insert):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(
        None,
        -5,
        time_scale=0.5,
        interpolate_end=10,
        interpolation="linear",
        insert_missing=insert,
    )
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(
        [-5, -5 / 3, 10, 20, 30] if insert else [0, 10, 20, 30]
    )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=1),
        dict(duration_frames=6),
        dict(to_start_frame=12, to_end_frame=18),
    ],
)
def test_identity_never_inserts_boundaries(maya_cmds, timing):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    keys.scale_keys(
        12,
        18,
        **timing,
        interpolate_start=5,
        interpolate_end=25,
        insert_missing=True,
    )
    mod.do_it_dg()
    assert _curve_state(curve) == before
    assert not maya_cmds.file(query=True, modified=True)


def test_only_zero_weight_keys_are_noop(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    curve.remove(2)
    curve.remove(1)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    keys.scale_keys(
        10, 20, time_scale=1.5, interpolate_start=0, interpolate_end=30
    )
    mod.do_it_dg()
    assert _curve_state(curve) == before
    assert not maya_cmds.file(query=True, modified=True)


@pytest.mark.parametrize(
    "bounds,kwargs,error",
    [
        ((None, 20), dict(interpolate_start=0), ValueError),
        ((10, None), dict(interpolate_end=30), ValueError),
        ((10, 20), dict(interpolate_start=10), ValueError),
        ((10, 20), dict(interpolate_start=15), ValueError),
        ((10, 20), dict(interpolate_end=20), ValueError),
        ((10, 20), dict(interpolate_end=15), ValueError),
        ((10, 20), dict(interpolate_start=float("nan")), ValueError),
        ((10, 20), dict(interpolate_end=float("inf")), ValueError),
        ((10, 20), dict(interpolate_start=-1e20), ValueError),
        ((10, 20), dict(interpolate_end=1e20), ValueError),
        ((10, 20), dict(interpolate_start=True), TypeError),
        ((10, 20), dict(interpolate_end="30"), TypeError),
        ((10, 20), dict(interpolation="spline"), ValueError),
    ],
)
def test_invalid_interpolation_is_rejected_before_booking(
    maya_cmds, bounds, kwargs, error
):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        keys.scale_keys(*bounds, time_scale=1.5, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
def test_units_negative_times_and_subframes(maya_cmds, kind):
    keys, mod, curve = _curve(maya_cmds, kind, True)
    for i in range(curve.numKeys):
        curve.setInput(i, curve.input(i) - _time(20))
    before = _curve_state(curve)
    keys.scale_keys(
        -10,
        0,
        time_scale=0.5,
        offset_frames=0.5,
        interpolate_start=-20,
        interpolate_end=10,
    )
    maya_cmds.currentUnit(
        time="ntsc", linear="m", angle="rad", updateAnimation=True
    )
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == pytest.approx([-20, -13.5, -9.5, -4.5, 1.5, 10])
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("stage", ["insert", "capture", "remove", "restore"])
def test_partial_failure_rolls_back_insertions_and_prior_edits(
    maya_cmds, monkeypatch, stage
):
    keys, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    helper = {
        "insert": "insert_boundaries",
        "capture": "capture_key",
        "remove": "restore_keys",
        "restore": "restore_keys",
    }[stage]
    original = getattr(_keyframe_move, helper)

    def fail(*args):
        if stage != "remove":
            original(*args)
        raise RuntimeError("injected scaling interpolation failure")

    monkeypatch.setattr(_keyframe_move, helper, fail)
    keys.scale_keys(
        12,
        18,
        time_scale=0.75,
        interpolate_start=5,
        interpolate_end=25,
        insert_missing=True,
    )
    with pytest.raises(
        RuntimeError, match="injected scaling interpolation failure"
    ):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("empty", ["missing", "empty", "range"])
def test_no_target_never_creates_curve(maya_cmds, empty):
    keys, mod, curve = _make(maya_cmds)
    if empty == "missing":
        keys = (
            bdu.Nodes(modifier_manager=mod)
            .existing.transform(maya_cmds.createNode("transform"))
            .tx.keyframe
        )
    elif empty == "empty":
        for i in reversed(range(curve.numKeys)):
            curve.remove(i)
    before = keys.get_keys()
    nodes = set(maya_cmds.ls())
    keys.scale_keys(
        50,
        60,
        time_scale=0.75,
        interpolate_start=40,
        interpolate_end=70,
        insert_missing=empty != "range",
    )
    mod.do_it_dg()
    assert keys.get_keys() == before
    assert set(maya_cmds.ls()) == nodes


def test_pending_creation_and_sequential_edits_never_query_flush(maya_cmds):
    mod = bdu.ModifierManager()
    keys = (
        bdu.Nodes(modifier_manager=mod)
        .create.animCurveTL(name="pendingScaleFalloff")
        .keyframe
    )
    keys.set_keys([(0, 0), (5, 1), (10, 2), (20, 3), (25, 4), (30, 5)])
    keys.add_values(
        10, 20, offset_value=2, interpolate_start=0, interpolate_end=30
    )
    keys.scale_keys(
        10, 20, time_scale=1.5, interpolate_start=0, interpolate_end=30
    )
    with pytest.raises(RuntimeError):
        keys.get_keys()
    assert not maya_cmds.objExists("pendingScaleFalloff")
    mod.do_it_dg()
    expected = [(0, 0), (3.75, 2), (10, 4), (25, 5), (28.75, 5), (30, 5)]
    assert keys.get_keys() == expected
    for _ in range(3):
        mod.undo_it()
        assert not maya_cmds.objExists("pendingScaleFalloff")
        mod.redo_it()
        assert keys.get_keys() == expected
