from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
)
from bd_util.maya.node.operator.attr import _keyframe_move
from test_keyframe_move import _make, _time, _assert_state, _history
from test_keyframe_set_equivalence import (
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _curve(cmds, kind="animCurveTL", weighted=False, tangent="fixed"):
    keys, mod, curve = _make(cmds, kind, weighted, tangent)
    for f in (5, 25):
        curve.addKey(
            _time(f),
            _time(f) if kind == "animCurveTT" else f,
            curve.kTangentFixed,
            curve.kTangentFixed,
        )
    return keys, mod, curve


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
@pytest.mark.parametrize("offset", [-4, 4])
@pytest.mark.parametrize("placement", ["offset", "to_start", "to_end"])
def test_weights_use_original_times_for_relative_and_absolute_moves(
    maya_cmds, interpolation, offset, placement
):
    keys, mod, curve = _curve(maya_cmds)
    for frame in (2.5, 27.5):
        curve.addKey(_time(frame), frame)
    before = _curve_state(curve)
    frames, values = keys.frames(), keys.values()
    amount = offset + {"offset": 0, "to_start": 10, "to_end": 20}[placement]
    assert (
        keys.move_frames(
            10,
            20,
            **{placement: amount},
            interpolate_start=0,
            interpolate_end=30,
            interpolation=interpolation,
        )
        is None
    )
    assert keys.frames() == frames
    assert _curve_state(curve) == before
    mod.do_it_dg()
    quarter = 0.25 if interpolation == "linear" else 0.15625
    weights = [0, quarter, 0.5, 1, 1, 0.5, quarter, 0]
    assert keys.frames() == pytest.approx(
        [f + offset * w for f, w in zip(frames, weights)]
    )
    assert keys.values() == values
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "auto", "linear", "step", "stepnext"]
)
@pytest.mark.parametrize("offset", [-4, 4])
def test_tangents_metadata_and_history_survive_nonuniform_movement(
    maya_cmds, kind, weighted, tangent, offset
):
    keys, mod, curve = _curve(maya_cmds, kind, weighted, tangent)
    before = _curve_state(curve)
    keys.move_frames(
        10, 20, offset=offset, interpolate_start=0, interpolate_end=30
    )
    mod.do_it_dg()
    after = _curve_state(curve)
    assert after["curve"] == before["curve"]
    assert keys.frames() == [
        0,
        5 + offset / 2,
        10 + offset,
        20 + offset,
        25 + offset / 2,
        30,
    ]
    for a, b in zip(after["keys"], before["keys"]):
        assert a["flags"] == b["flags"]
        assert a["numeric"][1] == b["numeric"][1]
        if b["flags"][:2] == (curve.kTangentFixed, curve.kTangentFixed):
            assert a["numeric"][2:] == b["numeric"][2:]
    _history(mod, curve, before, after)


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
@pytest.mark.parametrize("offset", [-15, -10, 10, 15])
@pytest.mark.parametrize("insert", [False, True])
def test_internal_collisions_and_reversals_roll_back_prior_edits(
    maya_cmds, interpolation, offset, insert
):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.move_frames(
        10,
        20,
        offset=offset,
        interpolate_start=0,
        interpolate_end=30,
        interpolation=interpolation,
        insert_missing=insert,
    )
    with pytest.raises(ValueError, match="coincide or change order"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


def test_stationary_fade_endpoint_is_protected_from_overwrite(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.move_frames(
        10, 20, offset=10, interpolate_start=0, interpolate_end=30
    )
    with pytest.raises(ValueError, match="coincide"):
        mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize("offset", [10, 12])
@pytest.mark.parametrize("side", ["start", "end"])
@pytest.mark.parametrize("weighted", [False, True])
def test_external_collision_and_crossing_keep_existing_move_policy(
    maya_cmds, offset, side, weighted
):
    keys, mod, curve = _curve(maya_cmds, weighted=weighted)
    before = _curve_state(curve)
    if side == "start":
        kwargs = dict(interpolate_start=0, offset=offset)
        mapping = {0: 0, 5: 5 + offset / 2, 10: 10 + offset, 20: 20 + offset}
    else:
        kwargs = dict(interpolate_end=30, offset=-offset)
        mapping = {
            10: 10 - offset,
            20: 20 - offset,
            25: 25 - offset / 2,
            30: 30,
        }
    expected = {
        f: (v, data)
        for (f, v), data in zip(keys.get_keys(), before["keys"])
        if f not in mapping and f not in mapping.values()
    }
    for (frame, value), data in zip(keys.get_keys(), before["keys"]):
        if frame in mapping:
            expected[mapping[frame]] = (value, data)
    keys.move_frames(10, 20, **kwargs)
    mod.do_it_dg()
    assert keys.get_keys() == [(f, expected[f][0]) for f in sorted(expected)]
    for (f, (_, data)), actual in zip(
        sorted(expected.items()), _curve_state(curve)["keys"]
    ):
        assert actual["flags"] == data["flags"]
        assert actual["numeric"][1:] == pytest.approx(
            data["numeric"][1:], abs=1e-12
        )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
@pytest.mark.parametrize("exterior", [False, True])
@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
def test_only_four_explicit_boundaries_are_inserted_and_sampled_before_editing(
    maya_cmds, kind, exterior, interpolation
):
    keys, mod, curve = _make(maya_cmds, kind, weighted=True)
    before = _curve_state(curve)
    start, end, low, high = (-5, 35, -10, 40) if exterior else (12, 18, 5, 25)
    frames = sorted([0, 10, 20, 30, start, end, low, high])
    values = [curve.evaluate(_time(f)) for f in frames]
    weights = [
        max(0, min(1, (f - low) / (start - low), (high - f) / (high - end)))
        for f in frames
    ]
    if interpolation == "smoothstep":
        weights = [w * w * (3 - 2 * w) for w in weights]
    expected_frames = [f + 2 * w for f, w in zip(frames, weights)]
    keys.move_frames(
        start,
        end,
        offset=2,
        interpolate_start=low,
        interpolate_end=high,
        interpolation=interpolation,
        insert_missing=True,
    )
    mod.do_it_dg()
    assert keys.frames() == pytest.approx(expected_frames)
    for i, value in enumerate(values):
        actual = curve.evaluate(curve.input(i))
        if isinstance(value, om.MTime):
            assert actual == value
        else:
            assert actual == pytest.approx(value)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("insert", [False, True])
def test_colliding_missing_boundary_is_checked_before_insertion(
    maya_cmds, insert
):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    # With no key at 25 the two core keys keep their order. An explicit insertion protects 25.
    keys.move_frames(
        10, 20, offset=6, interpolate_end=25, insert_missing=insert
    )
    if insert:
        with pytest.raises(ValueError, match="change order"):
            mod.do_it_dg()
        assert _curve_state(curve) == before
    else:
        mod.do_it_dg()
        assert keys.frames() == [0, 16, 26, 30]
        _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "bounds,kwargs,expected",
    [
        (
            (10, None),
            dict(to_start=14, interpolate_start=0),
            [0, 7, 14, 24, 29, 34],
        ),
        (
            (None, 20),
            dict(to_end=16, interpolate_end=30),
            [-4, 1, 6, 16, 23, 30],
        ),
        (
            (10, 20),
            dict(to_start=14, interpolate_end=30),
            [0, 5, 14, 24, 27, 30],
        ),
        (
            (10, 20),
            dict(to_end=16, interpolate_start=0),
            [0, 3, 6, 16, 25, 30],
        ),
        (
            (None, 20),
            dict(to_start=2, interpolate_end=30),
            [2, 7, 12, 22, 26, 30],
        ),
        (
            (10, None),
            dict(to_end=28, interpolate_start=0),
            [0, 4, 8, 18, 23, 28],
        ),
    ],
)
def test_one_sided_and_open_ranges_keep_core_absolute_anchor(
    maya_cmds, bounds, kwargs, expected
):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.move_frames(*bounds, **kwargs)
    mod.do_it_dg()
    assert keys.frames() == expected
    _history(mod, curve, before, _curve_state(curve))


def test_missing_core_keys_still_move_existing_fade_keys(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.move_frames(
        12,
        18,
        to_start=14,
        interpolate_start=0,
        interpolate_end=30,
        interpolation="linear",
    )
    mod.do_it_dg()
    assert keys.frames() == pytest.approx([0, 10 + 5 / 3, 20 + 5 / 3, 30])
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("insert", [False, True])
def test_implicit_absolute_anchor_requires_core_key(maya_cmds, insert):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.move_frames(
        None,
        -5,
        to_start=-4,
        interpolate_end=10,
        insert_missing=insert,
        interpolation="linear",
    )
    mod.do_it_dg()
    if insert:
        assert keys.frames() == pytest.approx([-4, 2 / 3, 10, 20, 30])
    else:
        assert _curve_state(curve) == before
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "placement",
    [dict(offset=0), dict(to_start=12), dict(to_end=18)],
)
def test_zero_move_never_inserts_boundaries(maya_cmds, placement):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    keys.move_frames(
        12,
        18,
        **placement,
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
    keys.move_frames(10, 20, offset=5, interpolate_start=0, interpolate_end=30)
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
        keys.move_frames(*bounds, offset=5, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize(
    "placement",
    [dict(offset=4), dict(to_start=14), dict(to_end=24)],
)
def test_all_time_arguments_are_captured_at_booking(
    maya_cmds, kind, placement
):
    keys, mod, curve = _curve(maya_cmds, kind, weighted=True)
    before = _curve_state(curve)
    keys.move_frames(
        10, 20, **placement, interpolate_start=0, interpolate_end=30
    )
    maya_cmds.currentUnit(
        time="ntsc", linear="m", angle="rad", updateAnimation=True
    )
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == [0, 7, 14, 24, 27, 30]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("stage", ["insert", "set_input", "remove", "restore"])
def test_partial_failure_rolls_back_boundary_insertion_and_prior_work(
    maya_cmds, monkeypatch, stage
):
    keys, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    helper = {
        "insert": "insert_boundaries",
        "set_input": "_set_inputs",
        "remove": "restore_keys",
        "restore": "restore_keys",
    }[stage]
    original = getattr(_keyframe_move, helper)

    def fail(*args):
        if stage != "remove":
            original(*args)
        raise RuntimeError("injected interpolation failure")

    monkeypatch.setattr(_keyframe_move, helper, fail)
    if stage in ("insert", "set_input"):
        keys.move_frames(
            12,
            18,
            offset=2,
            interpolate_start=5,
            interpolate_end=25,
            insert_missing=True,
        )
    else:
        keys.move_frames(10, 20, offset=12, interpolate_start=0)
    with pytest.raises(RuntimeError, match="injected interpolation failure"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


@pytest.mark.parametrize("empty", ["missing", "empty", "range"])
def test_missing_targets_do_not_create_curves(maya_cmds, empty):
    keys, mod, curve = _make(maya_cmds)
    if empty == "missing":
        name = maya_cmds.createNode("transform")
        keys = (
            bdu.Nodes(modifier_manager=mod)
            .existing.transform(name)
            .tx.keyframe
        )
    elif empty == "empty":
        for i in reversed(range(curve.numKeys)):
            curve.remove(i)
    before = keys.get_keys()
    nodes = set(maya_cmds.ls())
    keys.move_frames(
        50,
        60,
        offset=2,
        interpolate_start=40,
        interpolate_end=70,
        insert_missing=empty != "range",
    )
    mod.do_it_dg()
    assert keys.get_keys() == before
    assert set(maya_cmds.ls()) == nodes


def test_pending_keys_and_sequential_edits_are_used_without_query_flush(
    maya_cmds,
):
    mod = bdu.ModifierManager()
    keys = (
        bdu.Nodes(modifier_manager=mod)
        .create.animCurveTL(name="pendingFalloff")
        .keyframe
    )
    keys.set_keys([(0, 0), (5, 1), (10, 2), (20, 3), (25, 4), (30, 5)])
    keys.add_values(10, 20, offset=2, interpolate_start=0, interpolate_end=30)
    keys.move_frames(10, 20, offset=4, interpolate_start=0, interpolate_end=30)
    with pytest.raises(RuntimeError):
        keys.get_keys()
    assert not maya_cmds.objExists("pendingFalloff")
    mod.do_it_dg()
    expected = [(0, 0), (7, 2), (14, 4), (24, 5), (27, 5), (30, 5)]
    assert keys.get_keys() == expected
    for _ in range(3):
        mod.undo_it()
        assert not maya_cmds.objExists("pendingFalloff")
        mod.redo_it()
        assert keys.get_keys() == expected


def test_reconnection_and_rename_are_resolved_at_execution(maya_cmds):
    plug, original = _existing_curve(maya_cmds, "target", "doubleLinear")
    mod = bdu.ModifierManager()
    keys = KeyframeManager(plug, modifier_manager=mod)
    _, _, replacement = _curve(maya_cmds)
    before, original_before = _curve_state(replacement), _curve_state(original)
    keys.move_frames(10, 20, offset=4, interpolate_start=0, interpolate_end=30)
    maya_cmds.disconnectAttr(original.name() + ".output", plug.name())
    maya_cmds.connectAttr(replacement.name() + ".output", plug.name())
    maya_cmds.rename(om.MFnDependencyNode(plug.node()).name(), "renamedTarget")
    mod.do_it_dg()
    assert keys.frames() == [0, 7, 14, 24, 27, 30]
    assert _curve_state(original) == original_before
    _history(mod, replacement, before, _curve_state(replacement))


@pytest.mark.parametrize("offset", [0, 4])
def test_interpolation_requires_manager_and_write_access_even_for_noop(
    maya_cmds, offset
):
    keys, mod, curve = _make(maya_cmds)
    kwargs = dict(offset=offset, interpolate_start=0, interpolate_end=30)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).move_frames(10, 20, **kwargs)
    keys.move_frames(10, 20, **kwargs)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()


def test_negative_times_and_subframe_offsets(maya_cmds):
    keys, mod, curve = _curve(maya_cmds)
    for i in range(curve.numKeys):
        curve.setInput(i, curve.input(i) - _time(20))
    before = _curve_state(curve)
    keys.move_frames(
        -10, 0, offset=0.5, interpolate_start=-20, interpolate_end=10
    )
    mod.do_it_dg()
    assert keys.frames() == [-20, -14.75, -9.5, 0.5, 5.25, 10]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("weighted", [False, True])
def test_reinsertion_preserves_short_weighted_and_raw_nonweighted_tangents(
    maya_cmds, weighted
):
    keys, mod, curve = _curve(maya_cmds, weighted=weighted)
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    x, y = (1e-8, 2e-8) if weighted else (0.6, 1.6)
    curve.addKeysWithTangents(
        om.MTimeArray([_time(f) for f in (0, 5, 10, 20, 25, 30)]),
        om.MDoubleArray(range(6)),
        tangentInType=curve.kTangentFixed,
        tangentOutType=curve.kTangentFixed,
        tangentInXArray=om.MDoubleArray([x] * 6),
        tangentInYArray=om.MDoubleArray([y] * 6),
        tangentOutXArray=om.MDoubleArray([x] * 6),
        tangentOutYArray=om.MDoubleArray([y] * 6),
        tangentsLockedArray=[True] * 6,
        weightsLockedArray=[True] * 6,
        convertUnits=False,
    )
    before = _curve_state(curve)
    keys.move_frames(10, 20, offset=12, interpolate_start=0)
    mod.do_it_dg()
    after = _curve_state(curve)
    assert keys.frames() == [0, 11, 22, 25, 30, 32]
    assert keys.values() == [0, 1, 2, 4, 5, 3]
    for i, old_index in enumerate((0, 1, 2, 4, 5, 3)):
        assert after["keys"][i]["flags"] == before["keys"][old_index]["flags"]
        assert (
            after["keys"][i]["numeric"][1:]
            == before["keys"][old_index]["numeric"][1:]
        )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("reinsert", [False, True])
def test_short_weighted_time_tangent_is_preserved_or_rolls_back(
    maya_cmds, reinsert
):
    keys, mod, curve = _make(maya_cmds, "animCurveTT", True)
    curve.insertKey(_time(10.01))
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    keys.move_frames(10, 20, offset=40 if reinsert else 1, interpolate_start=0)
    if reinsert:
        with pytest.raises(RuntimeError, match="weighted time tangent"):
            mod.do_it_dg()
        _assert_state(_curve_state(curve), before)
    else:
        mod.do_it_dg()
        assert keys.frames() == pytest.approx([0, 11, 11.01, 21, 30, 80])
        after = _curve_state(curve)
        for actual, expected in zip(after["keys"][:5], before["keys"]):
            assert actual["flags"] == expected["flags"]
            assert actual["numeric"][1:] == pytest.approx(
                expected["numeric"][1:], abs=3e-8, rel=1e-9
            )
        _history(mod, curve, before, after)


def test_zero_width_core_supports_falloff(maya_cmds):
    keys, mod, curve = _curve(maya_cmds)
    before = _curve_state(curve)
    keys.move_frames(10, 10, offset=2, interpolate_start=0, interpolate_end=20)
    mod.do_it_dg()
    assert keys.frames() == [0, 6, 12, 20, 25, 30]
    _history(mod, curve, before, _curve_state(curve))
