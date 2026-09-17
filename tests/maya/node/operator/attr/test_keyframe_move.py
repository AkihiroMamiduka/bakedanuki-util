from __future__ import annotations

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
)
from bd_util.maya.node.operator.attr import _keyframe_move
from test_keyframe_set_equivalence import (
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _time(frame):
    return om.MTime(frame, om.MTime.kFilm)


def _make(cmds, kind="animCurveTL", weighted=False, tangent="fixed"):
    name = cmds.createNode(kind)
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    for frame, value in ((0, 0), (10, 4), (20, 2), (30, 7)):
        curve.addKey(
            _time(frame), _time(value) if kind == "animCurveTT" else value
        )
    curve.setIsWeighted(weighted)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, om.MAngle(0.3), 0.2, True)
        curve.setTangent(i, om.MAngle(-0.2), 0.3, False)
        tangent_type = getattr(
            curve,
            "kTangent"
            + ("StepNext" if tangent == "stepnext" else tangent.capitalize()),
        )
        curve.setInTangentType(
            i,
            (
                curve.kTangentFixed
                if tangent in ("step", "stepnext")
                else tangent_type
            ),
        )
        curve.setOutTangentType(i, tangent_type)
    curve.setIsBreakdown(1, True)
    curve.setTangentsLocked(1, True)
    curve.setWeightsLocked(1, True)
    curve.setPreInfinityType(curve.kCycle)
    curve.setPostInfinityType(curve.kLinear)
    mod = bdu.ModifierManager()
    if kind == "animCurveTT":
        node = cmds.createNode("transform")
        cmds.addAttr(node, longName="timeValue", attributeType="time")
        cmds.connectAttr(name + ".output", node + ".timeValue")
        plug = om.MSelectionList().add(node + ".timeValue").getPlug(0)
        keyframe = KeyframeManager(plug, modifier_manager=mod)
    else:
        keyframe = CurveKeyframeManager(curve.object(), modifier_manager=mod)
    return keyframe, mod, curve


def _assert_state(actual, expected):
    assert actual["curve"] == expected["curve"]
    assert len(actual["keys"]) == len(expected["keys"])
    for a, b in zip(actual["keys"], expected["keys"]):
        assert a["flags"] == b["flags"]
        assert a["numeric"] == pytest.approx(b["numeric"], abs=3e-8, rel=1e-9)


def _history(mod, curve, before, after):
    for _ in range(3):
        mod.undo_it()
        _assert_state(_curve_state(curve), before)
        mod.redo_it()
        _assert_state(_curve_state(curve), after)


@pytest.mark.parametrize(
    "method,args,kwargs,expected",
    [
        (
            "move_key",
            (10,),
            {"to_frame": 15},
            [(0, 0), (15, 4), (20, 2), (30, 7)],
        ),
        ("move_key", (10,), {"offset_frames": 10}, [(0, 0), (20, 4), (30, 7)]),
        (
            "move_key",
            (10,),
            {"to_frame": 25},
            [(0, 0), (20, 2), (25, 4), (30, 7)],
        ),
        (
            "move_keys",
            (10, 20),
            {"offset_frames": 10},
            [(0, 0), (20, 4), (30, 2)],
        ),
        (
            "move_keys",
            (10, 20),
            {"to_start_frame": 20},
            [(0, 0), (20, 4), (30, 2)],
        ),
        (
            "move_keys",
            (10, 20),
            {"to_end_frame": 30},
            [(0, 0), (20, 4), (30, 2)],
        ),
        (
            "move_keys",
            (10, None),
            {"offset_frames": -15},
            [(-5, 4), (0, 0), (5, 2), (15, 7)],
        ),
        (
            "move_keys",
            (None, 20),
            {"offset_frames": 15},
            [(15, 0), (25, 4), (30, 7), (35, 2)],
        ),
        (
            "move_keys",
            (),
            {"to_start_frame": -5},
            [(-5, 0), (5, 4), (15, 2), (25, 7)],
        ),
        (
            "move_keys",
            (),
            {"to_end_frame": 25},
            [(-5, 0), (5, 4), (15, 2), (25, 7)],
        ),
        (
            "move_keys",
            (12, 28),
            {"to_start_frame": 20},
            [(0, 0), (10, 4), (28, 2), (30, 7)],
        ),
        (
            "move_keys",
            (12, 28),
            {"to_end_frame": 40},
            [(0, 0), (10, 4), (30, 7), (32, 2)],
        ),
        (
            "move_key",
            (10,),
            {"offset_frames": -10.25},
            [(-0.25, 4), (0, 0), (20, 2), (30, 7)],
        ),
    ],
)
def test_selection_destinations_overwrite_and_history(
    maya_cmds, method, args, kwargs, expected
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    assert getattr(keyframe, method)(*args, **kwargs) is None
    assert _curve_state(curve) == before
    assert keyframe.frames() == [0, 10, 20, 30]
    mod.do_it_dg()
    assert keyframe.get_keys() == pytest.approx(expected)
    after = _curve_state(curve)
    _history(mod, curve, before, after)


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "auto", "linear", "step", "stepnext"]
)
@pytest.mark.parametrize("destination", [12.5, 20, 25])
def test_metadata_and_curve_settings_survive_all_move_paths(
    maya_cmds, kind, weighted, tangent, destination
):
    keyframe, mod, curve = _make(maya_cmds, kind, weighted, tangent)
    before = _curve_state(curve)
    keyframe.move_key(10, to_frame=destination)
    mod.do_it_dg()
    index = curve.find(_time(destination))
    after = _curve_state(curve)
    moved = after["keys"][index]
    source = before["keys"][1]
    assert moved["flags"] == source["flags"]
    assert moved["numeric"][1] == pytest.approx(
        source["numeric"][1], abs=1e-10
    )
    if tangent == "fixed":
        assert moved["numeric"][2:] == pytest.approx(
            source["numeric"][2:], abs=3e-8, rel=1e-9
        )
    assert after["curve"] == before["curve"]
    for old_index, frame in ((0, 0), (2, 20), (3, 30)):
        if frame == destination:
            continue
        unchanged = after["keys"][curve.find(_time(frame))]
        assert unchanged["flags"] == before["keys"][old_index]["flags"]
        assert (
            unchanged["numeric"][:2]
            == before["keys"][old_index]["numeric"][:2]
        )
        if tangent == "fixed":
            assert (
                unchanged["numeric"][2:]
                == before["keys"][old_index]["numeric"][2:]
            )
    _history(mod, curve, before, after)


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "tangent", ["fixed", "auto", "linear", "step", "stepnext"]
)
@pytest.mark.parametrize("offset", [-12.5, 40])
def test_whole_curve_translation_preserves_evaluation(
    maya_cmds, weighted, tangent, offset
):
    keyframe, mod, curve = _make(maya_cmds, weighted=weighted, tangent=tangent)
    frames = [i / 4 for i in range(-20, 141)]
    values = [curve.evaluate(_time(f)) for f in frames]
    keyframe.move_keys(offset_frames=offset)
    mod.do_it_dg()
    assert [
        curve.evaluate(_time(f + offset)) for f in frames
    ] == pytest.approx(values, abs=1e-9)


@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("args", [(12, 18), (12, 12), (None, 12), (18, None)])
def test_missing_boundaries_insert_values_and_restore_history(
    maya_cmds, kind, weighted, args
):
    keyframe, mod, curve = _make(maya_cmds, kind, weighted)
    before = _curve_state(curve)
    boundaries = sorted({f for f in args if f is not None})
    values = {f: curve.evaluate(_time(f)) for f in boundaries}
    keyframe.move_keys(*args, offset_frames=40, insert_missing=True)
    assert _curve_state(curve) == before
    mod.do_it_dg()
    for frame, value in values.items():
        index = curve.find(_time(frame + 40))
        assert index is not None and curve.find(_time(frame)) is None
        actual = curve.evaluate(curve.input(index))
        if isinstance(value, om.MTime):
            assert actual == value
        else:
            assert actual == pytest.approx(value)
        assert not curve.isBreakdown(index)
    _history(mod, curve, before, _curve_state(curve))


def test_single_missing_key_and_absolute_missing_boundaries(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds)
    expected = curve.evaluate(_time(12))
    keyframe.move_key(12, to_frame=15, insert_missing=True)
    mod.do_it_dg()
    assert curve.find(_time(12)) is None
    assert curve.evaluate(_time(15)) == pytest.approx(expected)
    keyframe.move_keys(12, 18, to_end_frame=28, insert_missing=True)
    mod.do_it_dg()
    assert keyframe.frames() == [0, 10, 20, 22, 25, 28, 30]


@pytest.mark.parametrize("insert_missing", [False, True])
@pytest.mark.parametrize(
    "method,args,kwargs",
    [
        ("move_key", (12,), {"to_frame": 12}),
        ("move_key", (10,), {"offset_frames": 0}),
        ("move_keys", (12, 18), {"offset_frames": 0}),
        ("move_keys", (12, 18), {"to_start_frame": 12}),
        ("move_keys", (), {"to_end_frame": 30}),
    ],
)
def test_zero_move_does_not_insert_or_change_scene(
    maya_cmds, method, args, kwargs, insert_missing
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    maya_cmds.file(modified=False)
    getattr(keyframe, method)(*args, **kwargs, insert_missing=insert_missing)
    mod.do_it_dg()
    assert _curve_state(curve) == before
    assert not maya_cmds.file(query=True, modified=True)


@pytest.mark.parametrize(
    "empty", ["missing_curve", "empty_curve", "missing_keys"]
)
@pytest.mark.parametrize("method", ["move_key", "move_keys"])
def test_missing_targets_are_noops(maya_cmds, empty, method):
    if empty == "missing_curve":
        node = maya_cmds.createNode("transform")
        mod = bdu.ModifierManager()
        keyframe = (
            bdu.Nodes(modifier_manager=mod)
            .existing.transform(node)
            .tx.keyframe
        )
    else:
        keyframe, mod, curve = _make(maya_cmds)
        if empty == "empty_curve":
            for i in reversed(range(curve.numKeys)):
                curve.remove(i)
    before = keyframe.get_keys()
    nodes = set(maya_cmds.ls())
    args = (12,) if method == "move_key" else (12, 18)
    getattr(keyframe, method)(
        *args, offset_frames=10, insert_missing=empty != "missing_keys"
    )
    mod.do_it_dg()
    assert keyframe.get_keys() == before
    assert set(maya_cmds.ls()) == nodes


@pytest.mark.parametrize(
    "method,args,kwargs,error",
    [
        ("move_key", (10,), {}, ValueError),
        ("move_key", (10,), {"offset_frames": 1, "to_frame": 20}, ValueError),
        ("move_key", (None,), {"to_frame": 20}, TypeError),
        ("move_key", (float("nan"),), {"to_frame": 20}, ValueError),
        ("move_key", (10,), {"to_frame": float("inf")}, ValueError),
        ("move_keys", (), {}, ValueError),
        ("move_keys", (20, 10), {"offset_frames": 1}, ValueError),
        ("move_keys", (), {"offset_frames": float("nan")}, ValueError),
        ("move_keys", (), {"to_start_frame": float("inf")}, ValueError),
        ("move_keys", (), {"to_end_frame": float("inf")}, ValueError),
        (
            "move_keys",
            (),
            {"to_start_frame": 10, "to_end_frame": 20},
            ValueError,
        ),
        (
            "move_keys",
            (),
            {"offset_frames": 1, "to_end_frame": 20},
            ValueError,
        ),
        (
            "move_keys",
            (),
            {"offset_frames": 1, "insert_missing": 1},
            TypeError,
        ),
    ],
)
def test_invalid_arguments_do_not_queue_partial_work(
    maya_cmds, method, args, kwargs, error
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(error):
        getattr(keyframe, method)(*args, **kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


@pytest.mark.parametrize(
    "kind", ["animCurveTA", "animCurveTL", "animCurveTU", "animCurveTT"]
)
@pytest.mark.parametrize(
    "kwargs",
    [{"offset_frames": 15}, {"to_start_frame": 25}, {"to_end_frame": 35}],
)
def test_units_captured_before_execution_and_redo(maya_cmds, kind, kwargs):
    keyframe, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    keyframe.move_keys(10, 20, **kwargs)
    maya_cmds.currentUnit(
        time="ntsc", angle="rad", linear="m", updateAnimation=True
    )
    mod.do_it_dg()
    assert [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ] == [0, 25, 30, 35]
    after = _curve_state(curve)
    maya_cmds.currentUnit(
        time="pal", angle="deg", linear="cm", updateAnimation=True
    )
    _history(mod, curve, before, after)


@pytest.mark.parametrize(
    "stage",
    ["after_insert", "after_remove", "after_restore", "after_set_input"],
)
@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
def test_mid_edit_failure_rolls_back_insert_overwrite_and_earlier_edits(
    maya_cmds, monkeypatch, stage, kind
):
    keyframe, mod, curve = _make(maya_cmds, kind, True)
    before = _curve_state(curve)
    keyframe.set_key(99, frame=80)
    helper = (
        "_set_inputs"
        if stage in ("after_insert", "after_set_input")
        else "restore_keys"
    )
    original = getattr(_keyframe_move, helper)

    def fail(*args):
        if stage in ("after_restore", "after_set_input"):
            original(*args)
        raise RuntimeError("injected move failure")

    monkeypatch.setattr(_keyframe_move, helper, fail)
    if stage == "after_insert":
        keyframe.move_key(12, to_frame=15, insert_missing=True)
    elif stage == "after_set_input":
        keyframe.move_key(10, to_frame=12)
    else:
        keyframe.move_key(10, to_frame=20)
    with pytest.raises(RuntimeError, match="injected move failure"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
    assert not mod.can_undo and not mod.can_redo


def test_pending_creation_and_sequential_moves(maya_cmds):
    mod = bdu.ModifierManager()
    curve = bdu.Nodes(modifier_manager=mod).create.animCurveTL(name="pending")
    keyframe = curve.keyframe
    keyframe.set_keys([(10, 4), (20, 2)])
    keyframe.move_key(10, to_frame=15)
    keyframe.move_keys(to_start_frame=30)
    with pytest.raises(RuntimeError):
        keyframe.frames()
    assert not maya_cmds.objExists("pending")
    mod.do_it_dg()
    assert keyframe.get_keys() == [(30, 4), (35, 2)]
    for _ in range(2):
        mod.undo_it()
        assert not maya_cmds.objExists("pending")
        mod.redo_it()
        assert keyframe.get_keys() == [(30, 4), (35, 2)]


@pytest.mark.parametrize("attribute_type", ["bool", "enum", "long"])
def test_numeric_discrete_channels_use_existing_edit_target_scope(
    maya_cmds, attribute_type
):
    plug, curve = _existing_curve(maya_cmds, "target", attribute_type)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    before = _curve_state(curve)
    keyframe.move_key(5, to_frame=9)
    mod.do_it_dg()
    assert keyframe.frames() == [1, 9]
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("frame", [-10, 40])
@pytest.mark.parametrize(
    "infinity", ["Constant", "Linear", "Cycle", "CycleRelative", "Oscillate"]
)
def test_missing_key_outside_key_span_uses_curve_value(
    maya_cmds, frame, infinity
):
    keyframe, mod, curve = _make(maya_cmds)
    curve.setPreInfinityType(getattr(curve, "k" + infinity))
    curve.setPostInfinityType(getattr(curve, "k" + infinity))
    value = curve.evaluate(_time(frame))
    before = _curve_state(curve)
    keyframe.move_key(frame, to_frame=15, insert_missing=True)
    mod.do_it_dg()
    assert curve.find(_time(frame)) is None
    assert curve.evaluate(_time(15)) == pytest.approx(value)
    _history(mod, curve, before, _curve_state(curve))


@pytest.mark.parametrize("bounds", [(-10, 40), (-20, -10), (40, 50)])
@pytest.mark.parametrize("kind", ["animCurveTL", "animCurveTT"])
@pytest.mark.parametrize("infinity", ["Cycle", "CycleRelative", "Oscillate"])
def test_both_exterior_boundaries_sample_before_changing_infinity_period(
    maya_cmds, bounds, kind, infinity
):
    keyframe, mod, curve = _make(maya_cmds, kind)
    curve.setPreInfinityType(getattr(curve, "k" + infinity))
    curve.setPostInfinityType(getattr(curve, "k" + infinity))
    before = _curve_state(curve)
    samples = [curve.evaluate(_time(frame)) for frame in bounds]
    keyframe.move_keys(*bounds, offset_frames=100, insert_missing=True)
    mod.do_it_dg()
    for frame, value in zip(bounds, samples):
        actual = curve.evaluate(_time(frame + 100))
        if isinstance(value, om.MTime):
            assert actual == value
        else:
            assert actual == pytest.approx(value)
    _history(mod, curve, before, _curve_state(curve))


def test_subframe_selection_and_maya_precision_noop(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds)
    curve.addKey(_time(10.25), 12)
    keyframe.move_keys(10.25, 10.25, offset_frames=0.25)
    mod.do_it_dg()
    assert keyframe.frames() == [0, 10, 10.5, 20, 30]
    mod.clear()
    before = _curve_state(curve)
    keyframe.move_key(10, to_frame=10 + 1e-10, insert_missing=True)
    mod.do_it_dg()
    assert _curve_state(curve) == before


def test_explicit_shared_curve_uses_input_time_and_keeps_connections(
    maya_cmds,
):
    keyframe, mod, curve = _make(maya_cmds)
    outputs = [maya_cmds.createNode("transform") for _ in range(2)]
    for node in outputs:
        maya_cmds.connectAttr(curve.name() + ".output", node + ".tx")
    driver = maya_cmds.createNode("animCurveTT")
    time_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(driver).getDependNode(0)
    )
    for frame in (0, 30):
        time_curve.addKey(
            _time(frame),
            _time(frame * 2),
            time_curve.kTangentLinear,
            time_curve.kTangentLinear,
        )
    maya_cmds.connectAttr("time1.outTime", driver + ".input")
    maya_cmds.connectAttr(driver + ".output", curve.name() + ".input")
    maya_cmds.setAttr(outputs[0] + ".tx", lock=True)
    before = _curve_state(curve)
    connections = maya_cmds.listConnections(
        curve.name(), connections=True, plugs=True
    )
    keyframe.move_key(10, to_frame=20)
    renamed = maya_cmds.rename(curve.name(), "renamedCurve")
    mod.do_it_dg()
    assert keyframe.frames() == [0, 20, 30]
    assert maya_cmds.getAttr(outputs[1] + ".tx", time=10) == 4
    assert maya_cmds.isConnected(driver + ".output", renamed + ".input")
    assert len(
        maya_cmds.listConnections(renamed, connections=True, plugs=True)
    ) == len(connections)
    _history(mod, curve, before, _curve_state(curve))


def test_channel_reconnection_and_rename_are_resolved_at_execution(maya_cmds):
    plug, original = _existing_curve(maya_cmds, "target", "doubleLinear")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    _, _, replacement = _make(maya_cmds)
    original_before, replacement_before = _curve_state(original), _curve_state(
        replacement
    )
    keyframe.move_key(10, to_frame=20)
    maya_cmds.disconnectAttr(original.name() + ".output", plug.name())
    maya_cmds.connectAttr(replacement.name() + ".output", plug.name())
    maya_cmds.rename(om.MFnDependencyNode(plug.node()).name(), "renamedTarget")
    mod.do_it_dg()
    assert keyframe.get_keys() == [(0, 0), (20, 4), (30, 7)]
    assert _curve_state(original) == original_before
    _history(mod, replacement, replacement_before, _curve_state(replacement))


@pytest.mark.parametrize("offset", [0, 10])
def test_noop_does_not_bypass_manager_or_write_requirements(maya_cmds, offset):
    keyframe, mod, curve = _make(maya_cmds)
    with pytest.raises(RuntimeError, match="ModifierManager"):
        CurveKeyframeManager(curve.object()).move_keys(offset_frames=offset)
    keyframe.move_key(12, offset_frames=offset)
    maya_cmds.lockNode(curve.name(), lock=True)
    with pytest.raises(RuntimeError, match="locked"):
        mod.do_it_dg()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"offset_frames": 1e20},
        {"to_start_frame": 1e20},
        {"start_frame": -1e20, "offset_frames": 1},
        {"end_frame": 1e20, "offset_frames": 1},
    ],
)
def test_unrepresentable_times_do_not_wrap_into_other_frames(
    maya_cmds, kwargs
):
    keyframe, mod, curve = _make(maya_cmds)
    before = _curve_state(curve)
    with pytest.raises(ValueError, match="representable"):
        keyframe.move_keys(**kwargs)
    mod.do_it_dg()
    assert _curve_state(curve) == before


def test_destination_overflow_rolls_back_earlier_edits(maya_cmds):
    keyframe, mod, curve = _make(maya_cmds)
    curve.addKey(_time(1e12), 4)
    before = _curve_state(curve)
    keyframe.set_key(12, frame=12)
    keyframe.move_keys(offset_frames=1e12)
    with pytest.raises(ValueError, match="representable"):
        mod.do_it_dg()
    _assert_state(_curve_state(curve), before)
