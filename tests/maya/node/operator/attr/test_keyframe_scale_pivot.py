from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    _keyframe_move,
)
from test_keyframe_move import _make, _time, _assert_state, _history
from test_keyframe_scale_interpolation import _curve
from test_keyframe_set_equivalence import (
    _curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "bounds,timing,expected",
    [
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=20),
            [(0, 4), (20, 2), (40, 7)],
        ),
        (
            (10, 30),
            dict(duration_frames=10, pivot_frame=20),
            [(0, 0), (15, 4), (20, 2), (25, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=30),
            [(-10, 4), (10, 2), (30, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=10),
            [(0, 0), (10, 4), (30, 2), (50, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=None),
            [(0, 0), (10, 4), (30, 2), (50, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=-10),
            [(0, 0), (30, 4), (50, 2), (70, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=0.5, pivot_frame=20, offset_frames=5),
            [(0, 0), (20, 4), (25, 2), (30, 7)],
        ),
        (
            (10, 30),
            dict(duration_frames=10, pivot_frame=20, offset_frames=5),
            [(0, 0), (20, 4), (25, 2), (30, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=1, pivot_frame=100, offset_frames=-2),
            [(0, 0), (8, 4), (18, 2), (28, 7)],
        ),
        (
            (10, None),
            dict(time_scale=0.5, pivot_frame=20),
            [(0, 0), (15, 4), (20, 2), (25, 7)],
        ),
        (
            (None, 20),
            dict(time_scale=0.5, pivot_frame=20),
            [(10, 0), (15, 4), (20, 2), (30, 7)],
        ),
        (
            (),
            dict(time_scale=0.5, pivot_frame=20),
            [(10, 0), (15, 4), (20, 2), (25, 7)],
        ),
        (
            (10, 10),
            dict(time_scale=2, pivot_frame=20),
            [(0, 4), (20, 2), (30, 7)],
        ),
        (
            (10, 30),
            dict(time_scale=2, pivot_frame=None, to_end_frame=30),
            [(-10, 4), (10, 2), (30, 7)],
        ),
    ],
)
def test_pivot_placement_and_offset(maya_cmds, bounds, timing, expected):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    assert keys.scale_keys(*bounds, **timing) is None
    assert keys.get_keys() == [(0, 0), (10, 4), (20, 2), (30, 7)]
    assert _curve_state(curve) == before
    mod.do_it_dg()
    assert keys.get_keys() == pytest.approx(expected)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("mode", ["replace_range", "merge"])
def test_missing_boundaries_still_define_pivoted_replacement(maya_cmds, mode):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(12, 28, time_scale=2, pivot_frame=20, mode=mode)
    mod.do_it_dg()
    assert keys.get_keys() == (
        [(0, 0), (20, 2)]
        if mode == "replace_range"
        else [(0, 0), (10, 4), (20, 2), (30, 7)]
    )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("mode", ["replace_range", "merge"])
def test_fade_collision_outside_pivoted_replacement_is_overwritten(
    maya_cmds, mode
):
    keys, mod, curve = _curve(maya_cmds)
    for frame in (21.25, 22, 42, 46):
        curve.addKey(_time(frame), frame)
    before = _curve_state(curve)
    keys.scale_keys(
        10, 20, time_scale=0.5, pivot_frame=70, interpolate_start=0, mode=mode
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


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("pivot", [0, 15, 30])
@pytest.mark.parametrize("scale", [0.5, 2])
def test_shape_and_metadata_survive_pivot_scaling(
    maya_cmds, kind, weighted, pivot, scale
):
    keys, mod, curve = _make(maya_cmds, kind, weighted)
    before = _curve_state(curve)

    def value(frame):
        result = curve.evaluate(_time(frame))
        return (
            result.asUnits(om.MTime.kSeconds)
            if isinstance(result, om.MTime)
            else result
        )

    samples = [i / 4 for i in range(-12, 132)]
    expected = [value(f) for f in samples]
    keys.scale_keys(time_scale=scale, pivot_frame=pivot)
    mod.do_it_dg()
    assert keys.frames() == [
        pivot + (f - pivot) * scale for f in (0, 10, 20, 30)
    ]
    after = _curve_state(curve)
    assert after["curve"] == before["curve"]
    for a, b in zip(after["keys"], before["keys"]):
        assert a["flags"] == b["flags"]
        assert a["numeric"][1] == b["numeric"][1]
    assert [
        value(pivot + (f - pivot) * scale) for f in samples
    ] == pytest.approx(expected, abs=2e-6)
    _history(mod, curve, before, after)


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
@pytest.mark.parametrize(
    "timing", [dict(time_scale=1.5), dict(duration_frames=15)]
)
@pytest.mark.parametrize("offset", [0, 1])
def test_falloff_weights_pivot_transform_and_offset(
    maya_cmds, interpolation, timing, offset
):
    keys, mod, curve = _curve(maya_cmds, weighted=True)
    for frame in (2.5, 27.5):
        curve.addKey(
            _time(frame), frame, curve.kTangentFixed, curve.kTangentFixed
        )
    before = _curve_state(curve)
    frames, values = keys.frames(), keys.values()
    quarter = 0.25 if interpolation == "linear" else 0.15625
    weights = [0, quarter, 0.5, 1, 1, 0.5, quarter, 0]
    keys.scale_keys(
        10,
        20,
        **timing,
        pivot_frame=15,
        offset_frames=offset,
        interpolate_start=0,
        interpolate_end=30,
        interpolation=interpolation,
    )
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(
        [
            f + (15 + (f - 15) * 1.5 + offset - f) * w
            for f, w in zip(frames, weights)
        ]
    )
    assert keys.values() == values
    after = _curve_state(curve)
    for a, b, w in zip(after["keys"], before["keys"], weights):
        assert a["flags"] == b["flags"]
        for index in (2, 4):
            assert a["numeric"][index : index + 2] == pytest.approx(
                (b["numeric"][index] * (1 + w * 0.5), b["numeric"][index + 1]),
                abs=1e-7,
                rel=1e-6,
            )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("pivot", [15, 20])
def test_pivoted_internal_collision_or_reversal_rolls_back(maya_cmds, pivot):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.scale_keys(
        10,
        20,
        time_scale=2,
        pivot_frame=pivot,
        interpolate_start=0,
        interpolate_end=30,
    )
    with pytest.raises(ValueError, match="coincide or change order"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("insert", [False, True])
def test_pivot_is_not_an_insertion_boundary(maya_cmds, insert):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(
        12,
        18,
        time_scale=0.5,
        pivot_frame=15,
        insert_missing=insert,
        interpolate_start=5,
        interpolate_end=25,
        interpolation="linear",
    )
    mod.do_it_dg()
    assert not keys.has_key(15)
    assert len(keys.frames()) == (8 if insert else 4)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("pivot", [-1e12, 1e12])
@pytest.mark.parametrize(
    "timing", [dict(time_scale=1), dict(duration_frames=4)]
)
def test_identity_with_distant_pivot_does_not_insert_or_modify(
    maya_cmds, pivot, timing
):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    keys.scale_keys(1, 5, **timing, pivot_frame=pivot, insert_missing=True)
    mod.do_it_dg()
    assert _curve_state(curve) == before
    assert not maya_cmds.file(query=True, modified=True)


@pytest.mark.parametrize(
    "timing", [dict(time_scale=0.5), dict(duration_frames=15)]
)
@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
def test_pivot_offset_and_duration_use_booking_units(maya_cmds, timing, kind):
    keys, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    keys.scale_keys(**timing, pivot_frame=20, offset_frames=0.25)
    maya_cmds.currentUnit(
        time="ntsc", linear="m", angle="rad", updateAnimation=True
    )
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == [10.25, 15.25, 20.25, 25.25]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("pivot", [0, 2, -2])
def test_small_scale_preserves_representable_destination(maya_cmds, pivot):
    keys, mod, curve = _make(maya_cmds)
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    curve.addKey(_time(pivot), 0)
    curve.addKey(_time(1e12 + pivot), 1)
    before = _curve_state(curve)
    keys.scale_keys(time_scale=1e-12, pivot_frame=pivot)
    mod.do_it_dg()
    assert keys.frames() == pytest.approx([pivot, pivot + 1], abs=1e-7)
    _history(mod, curve, before, _curve_state(curve))


def test_negative_subframe_pivot(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.scale_keys(time_scale=0.5, pivot_frame=-0.25)
    mod.do_it_dg()
    assert keys.frames() == [-0.125, 4.875, 9.875, 14.875]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "pivot,error",
    [
        (True, TypeError),
        ("20", TypeError),
        (float("nan"), ValueError),
        (float("inf"), ValueError),
        (1e300, ValueError),
    ],
)
def test_invalid_pivot_is_rejected_before_booking(maya_cmds, pivot, error):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        keys.scale_keys(time_scale=2, pivot_frame=pivot)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "timing",
    [
        dict(time_scale=2, to_start_frame=10),
        dict(time_scale=2, to_end_frame=30),
        dict(duration_frames=10, to_start_frame=10),
        dict(duration_frames=10, to_end_frame=30),
        dict(to_start_frame=10, to_end_frame=30),
    ],
)
@pytest.mark.parametrize("pivot", [0, 20])
def test_pivot_and_target_bounds_are_exclusive(maya_cmds, timing, pivot):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(ValueError, match="pivot_frame cannot be combined"):
        keys.scale_keys(10, 30, **timing, pivot_frame=pivot)
    mod.do_it_dg()
    assert _curve_state(curve) == before


def test_unrepresentable_pivoted_placement_rolls_back_prior_edit(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.scale_keys(time_scale=1e300, pivot_frame=20)
    with pytest.raises(ValueError):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("stage", ["insert", "remove", "restore"])
def test_failure_rolls_back_boundary_insertion_and_prior_work(
    maya_cmds, monkeypatch, stage
):
    keys, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    helper = "insert_boundaries" if stage == "insert" else "restore_keys"
    original = getattr(_keyframe_move, helper)

    def fail(*args):
        if stage != "remove":
            original(*args)
        raise RuntimeError("injected pivot failure")

    monkeypatch.setattr(_keyframe_move, helper, fail)
    keys.scale_keys(
        12,
        18,
        time_scale=0.5,
        pivot_frame=15,
        insert_missing=True,
        interpolate_start=5,
        interpolate_end=25,
    )
    with pytest.raises(RuntimeError, match="injected pivot failure"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


def test_pending_creation_and_sequential_editing(maya_cmds):
    mod = bdu.ModifierManager()
    keys = (
        bdu.Nodes(modifier_manager=mod)
        .create.animCurveTL(name="pendingPivot")
        .keyframe
    )
    keys.set_keys([(0, 0), (10, 4), (20, 2), (30, 7)])
    keys.move_keys(offset_frames=5)
    keys.scale_keys(time_scale=0.5, pivot_frame=20, offset_frames=2)
    with pytest.raises(RuntimeError):
        keys.frames()
    assert not maya_cmds.objExists("pendingPivot")
    mod.do_it_dg()
    expected = [(14.5, 0), (19.5, 4), (24.5, 2), (29.5, 7)]
    assert keys.get_keys() == expected
    for _ in range(3):
        mod.undo_it()
        assert not maya_cmds.objExists("pendingPivot")
        mod.redo_it()
        assert keys.get_keys() == expected


@pytest.mark.parametrize("scale", [1, 2])
def test_noop_requires_manager_and_write_access(maya_cmds, scale):
    keys, mod, curve = _make(maya_cmds)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).scale_keys(
            time_scale=scale, pivot_frame=20
        )
    keys.scale_keys(time_scale=scale, pivot_frame=20)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()
