from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
)
from bd_util.maya.node.operator.attr import (
    _keyframe_move,
    _keyframe_scale,
    _keyframe_value,
)
from test_keyframe_move import _assert_state, _history, _make, _time
from test_keyframe_set_equivalence import (
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya

EDITS = [
    ("set_value", (10,), dict(value=5), [0, 5, 2, 7]),
    ("set_values", (10, 20), dict(value=5), [0, 5, 5, 7]),
    ("add_value", (10,), dict(offset_value=-3), [0, 1, 2, 7]),
    ("add_values", (10, 20), dict(offset_value=-3), [0, 1, -1, 7]),
    ("scale_value", (10,), dict(value_scale=2, pivot_value=10), [0, -2, 2, 7]),
    (
        "scale_values",
        (10, 20),
        dict(value_scale=2, pivot_value=10),
        [0, -2, -6, 7],
    ),
]


@pytest.mark.parametrize("method,args,kwargs,expected", EDITS)
def test_six_methods_are_deferred_and_keep_times(
    maya_cmds, method, args, kwargs, expected
):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    assert getattr(keys, method)(*args, **kwargs) is None
    assert keys.values() == [0, 4, 2, 7]
    assert _curve_state(curve) == before
    mod.do_it_dg()
    assert keys.frames() == [0, 10, 20, 30]
    assert keys.values() == pytest.approx(expected)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "bounds,expected",
    [
        ((), [1, 5, 3, 8]),
        ((None, 10), [1, 5, 2, 7]),
        ((20, None), [0, 4, 3, 8]),
        ((10, 10), [0, 5, 2, 7]),
        ((11, 19), [0, 4, 2, 7]),
        ((-20.5, -0.25), [0, 4, 2, 7]),
    ],
)
def test_inclusive_and_open_ranges(maya_cmds, bounds, expected):
    keys, mod, curve = _make(maya_cmds)
    keys.add_values(*bounds, offset_value=1)
    mod.do_it_dg()
    assert keys.values() == expected


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "auto", "linear", "step", "stepnext"]
)
@pytest.mark.parametrize("operation", ["set", "add", "scale"])
def test_values_metadata_and_history(
    maya_cmds, kind, weighted, tangent, operation
):
    keys, mod, curve = _make(maya_cmds, kind, weighted, tangent)
    before = _curve_state(curve)
    kwargs = {
        "set": dict(value=5),
        "add": dict(offset_value=3),
        "scale": dict(value_scale=-2, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_value")(10, **kwargs)
    mod.do_it_dg()
    after = _curve_state(curve)
    assert after["curve"] == before["curve"]
    unit = (
        math.pi / 180
        if kind == "animCurveTA"
        else 1 / 24 if kind == "animCurveTT" else 1
    )
    for i, (a, b) in enumerate(zip(after["keys"], before["keys"])):
        assert a["flags"] == b["flags"]
        assert a["numeric"][0] == b["numeric"][0]
        old = b["numeric"][1]
        expected = (
            old
            if i != 1
            else {
                "set": 5 * unit,
                "add": old + 3 * unit,
                "scale": unit + (old - unit) * -2,
            }[operation]
        )
        assert a["numeric"][1] == pytest.approx(expected)
        if tangent == "fixed":
            if operation != "scale" or i != 1:
                assert a["numeric"][2:] == b["numeric"][2:]
            elif kind != "animCurveTT":
                for side in (2, 4):
                    x, y = b["numeric"][side : side + 2]
                    y *= -2
                    if not weighted:
                        length = math.hypot(x, y)
                        x, y = x / length, y / length
                    assert a["numeric"][side : side + 2] == pytest.approx(
                        (x, y), abs=1e-12
                    )
    _history(mod, curve, before, after)


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("scale", [-2, 0, 0.5, 2])
def test_whole_curve_scale_transforms_shape(maya_cmds, kind, weighted, scale):
    keys, mod, curve = _make(maya_cmds, kind, weighted)
    before = _curve_state(curve)

    def evaluate(frame):
        value = curve.evaluate(_time(frame))
        return (
            value.asUnits(om.MTime.kSeconds)
            if isinstance(value, om.MTime)
            else value
        )

    frames = [i / 4 for i in range(-20, 141)]
    original = [evaluate(f) for f in frames]
    keys.scale_values(value_scale=scale, pivot_value=1)
    mod.do_it_dg()
    pivot = (
        math.pi / 180
        if kind == "animCurveTA"
        else 1 / 24 if kind == "animCurveTT" else 1
    )
    assert [evaluate(f) for f in frames] == pytest.approx(
        [pivot + (v - pivot) * scale for v in original], abs=1e-6
    )
    _history(mod, curve, before, _curve_state(curve))


def _falloff_curve(cmds):
    keys, mod, curve = _make(cmds, weighted=True)
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    for f in (0, 10, 12.5, 15, 20, 25, 30, 35, 37.5, 40, 50):
        i = curve.addKey(_time(f), 2, curve.kTangentFixed, curve.kTangentFixed)
        curve.setTangentsLocked(i, False)
        curve.setTangent(i, 0.6, 0.8, True, convertUnits=False)
        curve.setTangent(i, 0.6, 0.8, False, convertUnits=False)
    return keys, mod, curve


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
@pytest.mark.parametrize("operation", ["set", "add", "scale"])
def test_falloff_weights_existing_keys_and_tangents(
    maya_cmds, interpolation, operation
):
    keys, mod, curve = _falloff_curve(maya_cmds)
    before = _curve_state(curve)
    kwargs = {
        "set": dict(value=6),
        "add": dict(offset_value=4),
        "scale": dict(value_scale=-3, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_values")(
        20,
        30,
        interpolate_start=10,
        interpolate_end=40,
        interpolation=interpolation,
        **kwargs,
    )
    mod.do_it_dg()
    weights = [0, 0, 0.25, 0.5, 1, 1, 1, 0.5, 0.25, 0, 0]
    if interpolation == "smoothstep":
        weights = [w * w * (3 - 2 * w) for w in weights]
    assert keys.values() == pytest.approx(
        [2 + (4 if operation != "scale" else -4) * w for w in weights]
    )
    after = _curve_state(curve)
    assert keys.frames() == [0, 10, 12.5, 15, 20, 25, 30, 35, 37.5, 40, 50]
    for a, b, w in zip(after["keys"], before["keys"], weights):
        assert a["flags"] == b["flags"]
        for side in (2, 4):
            x, y = b["numeric"][side : side + 2]
            if operation == "scale":
                y *= 1 - 4 * w
            assert a["numeric"][side : side + 2] == pytest.approx(
                (x, y), abs=1e-12
            )
        if w == 0:
            assert a == b
    _history(mod, curve, before, after)


@pytest.mark.parametrize("side", ["start", "end"])
def test_one_sided_falloff_defaults_to_smoothstep(maya_cmds, side):
    keys, mod, curve = _falloff_curve(maya_cmds)
    if side == "start":
        keys.add_values(20, offset_value=4, interpolate_start=10)
        expected = [2, 2, 2.625, 4, 6, 6, 6, 6, 6, 6, 6]
    else:
        keys.add_values(None, 30, offset_value=4, interpolate_end=40)
        expected = [6, 6, 6, 6, 6, 6, 6, 4, 2.625, 2, 2]
    mod.do_it_dg()
    assert keys.values() == expected


@pytest.mark.parametrize("interpolation", ["linear", "smoothstep"])
def test_sparse_keys_are_not_resampled_or_re_eased(maya_cmds, interpolation):
    keys, mod, curve = _make(maya_cmds)
    for i in range(curve.numKeys):
        curve.setValue(i, 0)
        curve.setTangentsLocked(i, False)
        curve.setTangent(i, 1, 0, True, convertUnits=False)
        curve.setTangent(i, 1, 0, False, convertUnits=False)
    keys.add_values(
        10,
        20,
        offset_value=5,
        interpolate_start=0,
        interpolate_end=30,
        interpolation=interpolation,
    )
    mod.do_it_dg()
    assert keys.get_keys() == [(0, 0), (10, 5), (20, 5), (30, 0)]
    assert curve.evaluate(_time(2.5)) == pytest.approx(0.78125)


@pytest.mark.parametrize("operation", ["set", "add", "scale"])
@pytest.mark.parametrize("exterior", [False, True])
@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
def test_explicit_insertion_adds_only_core_and_fade_boundaries(
    maya_cmds, operation, exterior, kind
):
    keys, mod, curve = _make(maya_cmds, kind, weighted=True)
    before = _curve_state(curve)
    start, end, fade_start, fade_end = (
        (-5, 35, -10, 40) if exterior else (12, 18, 5, 25)
    )
    frames = sorted([0, 10, 20, 30, start, end, fade_start, fade_end])
    old = [curve.evaluate(_time(f)) for f in frames]
    old = [
        v.asUnits(om.MTime.kFilm) if isinstance(v, om.MTime) else v
        for v in old
    ]
    weights = [
        max(
            0,
            min(
                1,
                (f - fade_start) / (start - fade_start),
                (fade_end - f) / (fade_end - end),
            ),
        )
        for f in frames
    ]
    kwargs = {
        "set": dict(value=9),
        "add": dict(offset_value=5),
        "scale": dict(value_scale=2, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_values")(
        start,
        end,
        interpolate_start=fade_start,
        interpolate_end=fade_end,
        interpolation="linear",
        insert_missing=True,
        **kwargs,
    )
    mod.do_it_dg()
    assert keys.frames() == frames
    actual = [
        v.asUnits(om.MTime.kFilm) if isinstance(v, om.MTime) else v
        for v in keys.values()
    ]
    assert actual == pytest.approx(
        [
            v
            + w
            * (
                {"set": 9, "add": v + 5, "scale": 1 + (v - 1) * 2}[operation]
                - v
            )
            for v, w in zip(old, weights)
        ]
    )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("insert", [False, True])
@pytest.mark.parametrize(
    "method,kwargs",
    [
        ("set_value", dict(value=9)),
        ("add_value", dict(offset_value=5)),
        ("scale_value", dict(value_scale=2)),
    ],
)
def test_single_missing_subframe(maya_cmds, insert, method, kwargs):
    keys, mod, curve = _make(maya_cmds)
    frame = -2.25
    before = _curve_state(curve)
    old = curve.evaluate(_time(frame))
    getattr(keys, method)(frame, insert_missing=insert, **kwargs)
    mod.do_it_dg()
    if insert:
        assert keys.frames() == [-2.25, 0, 10, 20, 30]
        assert keys.values()[0] == pytest.approx(
            {"set_value": 9, "add_value": old + 5, "scale_value": old * 2}[
                method
            ]
        )
    else:
        assert _curve_state(curve) == before
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize(
    "method,kwargs",
    [
        ("add_values", dict(offset_value=0)),
        ("scale_values", dict(value_scale=1)),
    ],
)
def test_identity_is_noop_even_with_insertion(maya_cmds, method, kwargs):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    getattr(keys, method)(
        12,
        18,
        interpolate_start=5,
        interpolate_end=25,
        insert_missing=True,
        **kwargs,
    )
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize("method,args,kwargs,expected", EDITS)
@pytest.mark.parametrize("empty", [False, True])
def test_missing_and_empty_curves_are_not_created(
    maya_cmds, method, args, kwargs, expected, empty
):
    mod = bdu.ModifierManager()
    if empty:
        keys, mod, curve = _make(maya_cmds)
        for i in reversed(range(curve.numKeys)):
            curve.remove(i)
    else:
        name = maya_cmds.createNode("transform")
        keys = (
            bdu.Nodes(modifier_manager=mod)
            .existing.transform(name)
            .tx.keyframe
        )
    nodes = set(maya_cmds.ls())
    getattr(keys, method)(*args, insert_missing=True, **kwargs)
    mod.do_it_dg()
    assert keys.frames() == []
    assert set(maya_cmds.ls()) == nodes


@pytest.mark.parametrize(
    "method,args,kwargs,error",
    [
        ("set_value", (None,), dict(value=1), TypeError),
        ("add_value", (True,), dict(offset_value=1), TypeError),
        ("scale_value", ("1",), dict(value_scale=2), TypeError),
        ("set_values", (20, 10), dict(value=1), ValueError),
        ("add_values", (float("nan"), None), dict(offset_value=1), ValueError),
        ("scale_values", (1e300, None), dict(value_scale=2), ValueError),
        ("set_values", (), dict(value=True), TypeError),
        ("set_values", (), dict(value=float("inf")), ValueError),
        ("add_values", (), dict(offset_value="1"), TypeError),
        ("add_values", (), dict(offset_value=float("nan")), ValueError),
        ("scale_values", (), dict(value_scale=float("inf")), ValueError),
        ("scale_values", (), dict(value_scale=10**1000), ValueError),
        (
            "scale_values",
            (),
            dict(value_scale=2, pivot_value=False),
            TypeError,
        ),
        (
            "scale_values",
            (),
            dict(value_scale=2, pivot_value=float("inf")),
            ValueError,
        ),
        ("set_values", (), dict(value=1, interpolate_start=0), ValueError),
        ("set_values", (), dict(value=1, interpolate_end=30), ValueError),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_start=10),
            ValueError,
        ),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_end=20),
            ValueError,
        ),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_start=15),
            ValueError,
        ),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_end=15),
            ValueError,
        ),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_start=float("nan")),
            ValueError,
        ),
        (
            "set_values",
            (10, 20),
            dict(value=1, interpolate_end=True),
            TypeError,
        ),
        ("set_values", (), dict(value=1, interpolation="spline"), ValueError),
        ("set_values", (), dict(value=1, insert_missing=1), TypeError),
    ],
)
def test_invalid_arguments_are_rejected_before_booking(
    maya_cmds, method, args, kwargs, error
):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        getattr(keys, method)(*args, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("operation", ["set", "add", "scale"])
def test_units_are_captured_at_booking(maya_cmds, kind, operation):
    keys, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    kwargs = {
        "set": dict(value=9),
        "add": dict(offset_value=5),
        "scale": dict(value_scale=2, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_values")(
        10, 20, interpolate_start=0, interpolate_end=30, **kwargs
    )
    maya_cmds.currentUnit(
        time="ntsc", linear="m", angle="rad", updateAnimation=True
    )
    mod.do_it_dg()
    unit = (
        math.pi / 180
        if kind == "animCurveTA"
        else 1 / 24 if kind == "animCurveTT" else 1
    )
    after = _curve_state(curve)
    for i, (a, b) in enumerate(zip(after["keys"], before["keys"])):
        assert a["numeric"][0] == b["numeric"][0]
        old = b["numeric"][1]
        expected = (
            old
            if i in (0, 3)
            else {
                "set": 9 * unit,
                "add": old + 5 * unit,
                "scale": unit + (old - unit) * 2,
            }[operation]
        )
        assert a["numeric"][1] == pytest.approx(expected)
    _history(mod, curve, before, after)


@pytest.mark.parametrize("stage", ["insert", "value", "remove", "restore"])
def test_partial_failure_rolls_back_prior_work(maya_cmds, monkeypatch, stage):
    keys, mod, curve = _make(maya_cmds, weighted=True)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    module, helper = {
        "insert": (_keyframe_move, "insert_boundaries"),
        "value": (_keyframe_value, "_set_value"),
        "remove": (_keyframe_scale, "restore_scaled_keys"),
        "restore": (_keyframe_scale, "restore_scaled_keys"),
    }[stage]
    original = getattr(module, helper)

    def fail(*args):
        if stage != "remove":
            original(*args)
        raise RuntimeError("injected value failure")

    monkeypatch.setattr(module, helper, fail)
    if stage == "value":
        keys.add_values(12, 18, offset_value=5, insert_missing=True)
    else:
        keys.scale_values(12, 18, value_scale=2, insert_missing=True)
    with pytest.raises(RuntimeError, match="injected value failure"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


def test_pending_creation_and_sequential_operations(maya_cmds):
    mod = bdu.ModifierManager()
    keys = (
        bdu.Nodes(modifier_manager=mod)
        .create.animCurveTL(name="pendingValues")
        .keyframe
    )
    keys.set_keys([(10, 4), (20, 2), (30, 7)])
    keys.set_value(10, value=5)
    keys.add_values(offset_value=1)
    keys.scale_values(value_scale=-2, pivot_value=1)
    with pytest.raises(RuntimeError):
        keys.values()
    assert not maya_cmds.objExists("pendingValues")
    mod.do_it_dg()
    assert keys.get_keys() == [(10, -9), (20, -3), (30, -13)]
    for _ in range(3):
        mod.undo_it()
        assert not maya_cmds.objExists("pendingValues")
        mod.redo_it()
        assert keys.get_keys() == [(10, -9), (20, -3), (30, -13)]


@pytest.mark.parametrize("operation", ["set", "add", "scale"])
@pytest.mark.parametrize("attribute_type", ["bool", "enum", "long"])
def test_discrete_channels_edit_raw_curve_values(
    maya_cmds, operation, attribute_type
):
    plug, curve = _existing_curve(maya_cmds, "target", attribute_type)
    mod = bdu.ModifierManager()
    keys = KeyframeManager(plug, modifier_manager=mod)
    before = _curve_state(curve)
    kwargs = {
        "set": dict(value=1.5),
        "add": dict(offset_value=0.5),
        "scale": dict(value_scale=0.5),
    }[operation]
    getattr(keys, operation + "_values")(**kwargs)
    mod.do_it_dg()
    assert (
        keys.values()
        == {
            "set": [1.5, 1.5, 1.5],
            "add": [1.5, 3.5, 2.5],
            "scale": [0.5, 1.5, 1],
        }[operation]
    )
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("operation", ["add", "scale"])
def test_noop_still_requires_manager_and_write_access(maya_cmds, operation):
    keys, mod, curve = _make(maya_cmds)
    kwargs = (
        dict(offset_value=0) if operation == "add" else dict(value_scale=1)
    )
    with pytest.raises(RuntimeError, match="ModifierManager"):
        getattr(CurveKeyframeManager(curve.object()), operation + "_values")(
            **kwargs
        )
    getattr(keys, operation + "_values")(**kwargs)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()


@pytest.mark.parametrize("operation", ["add", "scale"])
def test_value_overflow_rolls_back_prior_edits(maya_cmds, operation):
    keys, mod, curve = _make(maya_cmds)
    curve.setValue(1, 1e308)
    before = _curve_state(curve)
    keys.set_key(99, frame=80)
    kwargs = (
        dict(offset_value=1e308)
        if operation == "add"
        else dict(value_scale=1e308)
    )
    getattr(keys, operation + "_values")(**kwargs)
    with pytest.raises(ValueError, match="finite"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)


@pytest.mark.parametrize("operation", ["set", "add", "scale"])
@pytest.mark.parametrize("channel", ["translateY", "rotateZ", "scaleX"])
@pytest.mark.parametrize("override", [False, True])
@pytest.mark.parametrize("base", [False, True])
def test_layer_values_are_raw_and_do_not_resolve_composed_result(
    maya_cmds, operation, channel, override, base
):
    from test_keyframe_anim_layer import _layered

    original, mod, layers = _layered(maya_cmds, channel, override=override)
    keys = original if base else original.anim_layer(layers[0])
    old = keys.values()
    other = original.anim_layer(layers[1]).get_curve_data()
    kwargs = {
        "set": dict(value=5),
        "add": dict(offset_value=3),
        "scale": dict(value_scale=-2, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_values")(**kwargs)
    mod.do_it_dg()
    assert keys.values() == pytest.approx(
        [
            {"set": 5, "add": v + 3, "scale": 1 + (v - 1) * -2}[operation]
            for v in old
        ]
    )
    assert original.anim_layer(layers[1]).get_curve_data() == other


@pytest.mark.parametrize("operation", ["set", "add", "scale"])
def test_reconnection_and_rename_before_execution(maya_cmds, operation):
    plug, original = _existing_curve(maya_cmds, "target", "doubleLinear")
    mod = bdu.ModifierManager()
    keys = KeyframeManager(plug, modifier_manager=mod)
    _, _, replacement = _make(maya_cmds)
    before = _curve_state(replacement)
    original_before = _curve_state(original)
    kwargs = {
        "set": dict(value=5),
        "add": dict(offset_value=3),
        "scale": dict(value_scale=-2, pivot_value=1),
    }[operation]
    getattr(keys, operation + "_values")(**kwargs)
    maya_cmds.disconnectAttr(original.name() + ".output", plug.name())
    maya_cmds.connectAttr(replacement.name() + ".output", plug.name())
    maya_cmds.rename(om.MFnDependencyNode(plug.node()).name(), "renamedTarget")
    mod.do_it_dg()
    assert keys.values() == pytest.approx(
        [
            {"set": 5, "add": v + 3, "scale": 1 + (v - 1) * -2}[operation]
            for v in (0, 4, 2, 7)
        ]
    )
    assert _curve_state(original) == original_before
    _history(mod, replacement, before, _curve_state(replacement))


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("scale", [0, -0.25])
def test_short_weighted_and_unnormalized_nonweighted_tangents(
    maya_cmds, weighted, scale
):
    keys, mod, curve = _make(maya_cmds, weighted=weighted)
    for i in reversed(range(curve.numKeys)):
        curve.remove(i)
    x, y = (1e-8, 2e-8) if weighted else (0.6, 1.6)
    curve.addKeysWithTangents(
        om.MTimeArray([_time(f) for f in (0, 10, 20)]),
        om.MDoubleArray([0, 4, 2]),
        tangentInType=curve.kTangentFixed,
        tangentOutType=curve.kTangentFixed,
        tangentInXArray=om.MDoubleArray([x] * 3),
        tangentInYArray=om.MDoubleArray([y] * 3),
        tangentOutXArray=om.MDoubleArray([x] * 3),
        tangentOutYArray=om.MDoubleArray([y] * 3),
        tangentsLockedArray=[False, True, False],
        weightsLockedArray=[False, True, False],
        convertUnits=False,
    )
    before = _curve_state(curve)
    keys.scale_values(
        10, 10, value_scale=scale, interpolate_start=0, interpolate_end=20
    )
    mod.do_it_dg()
    after = _curve_state(curve)
    assert after["keys"][0] == before["keys"][0]
    assert after["keys"][2] == before["keys"][2]
    expected = (x, y * scale)
    if not weighted:
        length = math.hypot(*expected)
        expected = tuple(v / length for v in expected)
    assert curve.getTangentXY(1, True) == pytest.approx(expected, abs=1e-20)
    assert curve.getTangentXY(1, False) == pytest.approx(expected, abs=1e-20)
    _history(mod, curve, before, after)


def test_set_same_value_keeps_tangents_but_can_insert_boundary(maya_cmds):
    keys, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    keys.set_value(10, value=4)
    mod.do_it_dg()
    assert _curve_state(curve) == before
    mod = bdu.ModifierManager()
    keys = CurveKeyframeManager(curve.object(), modifier_manager=mod)
    value = curve.evaluate(_time(12))
    keys.set_values(12, 12, value=value, insert_missing=True)
    mod.do_it_dg()
    assert keys.frames() == [0, 10, 12, 20, 30]
    assert curve.evaluate(_time(12)) == pytest.approx(value)
    _history(mod, curve, before, _curve_state(curve))


def test_tt_value_precision_limit_rolls_back(maya_cmds):
    keys, mod, curve = _make(maya_cmds, "animCurveTT")
    before = _curve_state(curve)
    keys.add_value(10, offset_value=1)
    keys.set_value(20, value=1e300)
    with pytest.raises(ValueError, match="representable time"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
