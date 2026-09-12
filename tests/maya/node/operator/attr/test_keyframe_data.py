from __future__ import annotations

import json
from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    AnimCurveData,
    KeyData,
    KeyframeManager,
)
from bd_util.maya.node.operator.attr import _keyframe_snapshot as snapshot
from test_keyframe_set_equivalence import (
    _existing_curve,
    _curve_state,
    _assert_curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _destination(cmds, attribute_type, *, existing=False):
    if existing:
        return _existing_curve(cmds, "destination", attribute_type)[0]
    node = cmds.createNode("transform", name="destination")
    cmds.addAttr(
        node, longName="value", attributeType=attribute_type, keyable=True
    )
    selection = om.MSelectionList()
    selection.add(node + ".value")
    return selection.getPlug(0)


def _assert_equivalent(actual, expected):
    assert actual["curve"] == expected["curve"]
    assert len(actual["keys"]) == len(expected["keys"])
    for a, b in zip(actual["keys"], expected["keys"]):
        assert a["flags"] == b["flags"]
        assert a["numeric"] == pytest.approx(b["numeric"], rel=2e-6, abs=2e-7)


@pytest.mark.parametrize(
    "attribute_type", ["double", "doubleAngle", "doubleLinear"]
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("existing", [False, True])
def test_json_roundtrip_units_shape_and_repeated_history(
    maya_cmds, attribute_type, weighted, existing
):
    plug, source = _existing_curve(maya_cmds, "source", attribute_type)
    source.setIsWeighted(weighted)
    before_source = _curve_state(source)
    sample_times = (-1.0, 0.02, 0.07, 0.17, 0.22, 0.33, 0.5, 1.0)
    samples = [
        source.evaluate(om.MTime(t, om.MTime.kSeconds)) for t in sample_times
    ]
    data = KeyframeManager(plug).get_curve_data()
    assert data is not None
    assert data.keys[1].value == pytest.approx(3.0)
    data = AnimCurveData.from_dict(
        json.loads(json.dumps(data.to_dict(), allow_nan=False))
    )
    destination = _destination(maya_cmds, attribute_type, existing=existing)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(destination, modifier_manager=mod)
    before = (
        _curve_state(
            oma.MFnAnimCurve(destination.sourceWithConversion().node())
        )
        if existing
        else None
    )
    maya_cmds.flushUndo()
    keyframe.set_curve_data(data)
    assert not mod.can_undo
    maya_cmds.currentUnit(
        angle="rad", linear="m", time="ntsc", updateAnimation=False
    )
    before = (
        _curve_state(
            oma.MFnAnimCurve(destination.sourceWithConversion().node())
        )
        if existing
        else None
    )
    maya_cmds.flushUndo()
    mod.do_it_dg()
    restored = oma.MFnAnimCurve(destination.sourceWithConversion().node())
    _assert_equivalent(_curve_state(restored), before_source)
    for seconds, expected in zip(sample_times, samples):
        time = om.MTime(seconds, om.MTime.kSeconds)
        assert restored.evaluate(time) == pytest.approx(
            expected, rel=2e-6, abs=2e-7
        )
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        if before is None:
            assert destination.sourceWithConversion().isNull
        else:
            _assert_curve_state(_curve_state(restored), before)
        mod.redo_it()
        _assert_equivalent(_curve_state(restored), before_source)


@pytest.mark.parametrize("tangent", tuple(snapshot._TANGENTS))
@pytest.mark.parametrize("weighted", [False, True])
def test_tangent_types_roundtrip(maya_cmds, tangent, weighted):
    plug, source = _existing_curve(maya_cmds, "source", "double")
    source.setIsWeighted(weighted)
    for i in range(source.numKeys):
        source.setTangentsLocked(i, False)
        source.setInTangentType(i, snapshot._TANGENTS[tangent])
        source.setOutTangentType(i, snapshot._TANGENTS[tangent])
    data = KeyframeManager(plug).get_curve_data()
    mod = bdu.ModifierManager()
    target = _destination(maya_cmds, "double")
    KeyframeManager(target, modifier_manager=mod).set_curve_data(data)
    mod.do_it_dg()
    actual = oma.MFnAnimCurve(target.sourceWithConversion().node())
    _assert_equivalent(_curve_state(actual), _curve_state(source))
    for frame in (0, 1.5, 3, 4, 5.5, 8, 10):
        time = om.MTime(frame, om.MTime.uiUnit())
        assert actual.evaluate(time) == pytest.approx(
            source.evaluate(time), rel=2e-6, abs=2e-7
        )


def test_partial_keys_preserve_other_fixed_keys_and_infinity(maya_cmds):
    plug, curve = _existing_curve(maya_cmds, "source", "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    before = _curve_state(curve)
    keys = keyframe.get_key_data(5, 5, include_boundaries=False)
    assert len(keys) == 1
    assert keyframe.get_key_data(5.1, 8.9, include_boundaries=False) == []
    assert (
        KeyData.from_dict(json.loads(json.dumps(keys[0].to_dict()))) == keys[0]
    )
    keyframe.set_key_data([replace(keys[0], value=8)])
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1.0, 1.0), (5.0, 8.0), (9.0, 2.0)]
    assert (curve.preInfinityType, curve.postInfinityType) == before["curve"][
        2:
    ]
    mod.undo_it()
    _assert_curve_state(_curve_state(curve), before)
    mod.redo_it()
    assert curve.value(1) == 8


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "attribute_type", ["double", "doubleAngle", "doubleLinear"]
)
def test_mixed_tangents_weights_locks_and_infinity(
    maya_cmds, weighted, attribute_type
):
    plug, source = _existing_curve(maya_cmds, "source", attribute_type)
    for i in reversed(range(source.numKeys)):
        source.remove(i)
    source.setIsWeighted(weighted)
    tangent_names = tuple(snapshot._TANGENTS)
    for i in range(len(tangent_names)):
        source.addKey(om.MTime(i * 3 + 0.5, om.MTime.uiUnit()), (i % 4) * 0.7)
    for i, tangent in enumerate(tangent_names):
        source.setTangentsLocked(i, False)
        source.setWeightsLocked(i, False)
        source.setTangent(
            i, 0.025, (i % 3 - 1) * 0.08, True, convertUnits=False
        )
        source.setTangent(
            i, 0.045, (i % 2 - 1) * 0.06, False, convertUnits=False
        )
        source.setInTangentType(i, snapshot._TANGENTS[tangent])
        source.setOutTangentType(i, snapshot._TANGENTS[tangent_names[-1 - i]])
        source.setWeightsLocked(i, bool(i % 2))
        source.setTangentsLocked(i, bool(i % 3))
        source.setIsBreakdown(i, bool(i % 4))
    source.setPreInfinityType(oma.MFnAnimCurve.kOscillate)
    source.setPostInfinityType(oma.MFnAnimCurve.kCycleRelative)
    data = KeyframeManager(plug).get_curve_data()
    target = _destination(maya_cmds, attribute_type)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    actual = oma.MFnAnimCurve(target.sourceWithConversion().node())
    _assert_equivalent(_curve_state(actual), _curve_state(source))
    for frame in range(-50, 100):
        time = om.MTime(frame + 0.25, om.MTime.uiUnit())
        assert actual.evaluate(time) == pytest.approx(
            source.evaluate(time), rel=2e-6, abs=2e-7
        )


def test_queue_order_capture_and_partial_creation(maya_cmds):
    plug, source = _existing_curve(maya_cmds, "source", "double")
    data = KeyframeManager(plug).get_curve_data()
    target = _destination(maya_cmds, "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    keys = list(data.keys)
    keyframe.set_key_data(
        iter(keys),
        seconds_per_frame=data.seconds_per_frame,
    )
    keys.clear()
    assert keyframe.get_curve_data() is None
    assert keyframe.get_key_data() == []
    keyframe.set_key_data([replace(data.keys[1], value=6)])
    keyframe.set_key(4, frame=8)
    mod.do_it_dg()
    assert keyframe.get_keys() == [
        (1.0, 1.0),
        (5.0, 6.0),
        (8.0, 4.0),
        (9.0, 2.0),
    ]
    mod.undo_it()
    assert keyframe.get_curve_data() is None
    mod.redo_it()
    assert keyframe.get_keys()[1] == (5.0, 6.0)


def test_partial_failure_does_not_change_closed_history(maya_cmds):
    plug, source = _existing_curve(maya_cmds, "source", "double")
    data = KeyframeManager(plug).get_curve_data()
    target = _destination(maya_cmds, "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    keyframe.set_key(20, frame=2)
    keyframe.set_key_data(data.keys)

    def fail(change):
        raise RuntimeError("injected failure")

    mod.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="injected failure"):
        mod.do_it_dg()
    assert keyframe.get_keys() == [(1.0, 1.0), (5.0, 3.0), (9.0, 2.0)]
    assert mod.can_undo
    mod.undo_it()
    assert keyframe.get_curve_data() is None


@pytest.mark.parametrize("existing", [False, True])
def test_empty_full_curve_and_empty_partial(maya_cmds, existing):
    plug, curve = _existing_curve(maya_cmds, "source", "double")
    data = replace(KeyframeManager(plug).get_curve_data(), keys=())
    target = _destination(maya_cmds, "double", existing=existing)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    before = keyframe.get_curve_data()
    keyframe.set_key_data([])
    assert not mod.can_undo
    keyframe.set_curve_data(data)
    mod.do_it_dg()
    assert keyframe.get_curve_data() == data
    mod.undo_it()
    assert keyframe.get_curve_data() == before
    mod.redo_it()
    assert keyframe.get_curve_data() == data


@pytest.mark.parametrize("existing", [False, True])
def test_restore_failure_rolls_back_entire_batch(
    maya_cmds, existing, monkeypatch
):
    plug, curve = _existing_curve(maya_cmds, "source", "double")
    data = KeyframeManager(plug).get_curve_data()
    target = _destination(maya_cmds, "double", existing=existing)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    before = keyframe.get_curve_data()
    keyframe.set_curve_data(data)
    # Failure after keys, tangents and locks have already been edited.
    with monkeypatch.context() as patch:
        patch.delitem(snapshot._INFINITY, "linear")
        with pytest.raises(KeyError):
            mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    assert not mod.can_undo


@pytest.mark.parametrize(
    "restriction",
    [
        "target_lock",
        "node_lock",
        "curve_lock",
        "key_lock",
        "layer",
        "shared",
        "quaternion",
    ],
)
@pytest.mark.parametrize("method", ["set_curve_data", "set_weighted"])
def test_reject_unsupported_destination_without_changes(
    maya_cmds, restriction, method
):
    plug, curve = _existing_curve(maya_cmds, "source", "doubleAngle")
    data = KeyframeManager(plug).get_curve_data()
    before = _curve_state(curve)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    if method == "set_curve_data":
        keyframe.set_curve_data(data)
    else:
        keyframe.set_weighted(not curve.isWeighted)
    if restriction == "target_lock":
        maya_cmds.setAttr(plug.name(), lock=True)
    elif restriction == "node_lock":
        maya_cmds.lockNode(om.MFnDependencyNode(plug.node()).name(), lock=True)
    elif restriction == "curve_lock":
        maya_cmds.lockNode(curve.name(), lock=True)
    elif restriction == "key_lock":
        maya_cmds.setAttr(curve.name() + ".ktv[1].kv", lock=True)
    elif restriction == "layer":
        maya_cmds.animLayer("Layer", attribute=plug.name())
    elif restriction == "shared":
        other = maya_cmds.createNode("transform")
        maya_cmds.connectAttr(curve.name() + ".output", other + ".rx")
    else:
        curve.findPlug("rotationInterpolation", False).setInt(2)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    _assert_curve_state(_curve_state(curve), before)


@pytest.mark.parametrize(
    "bad",
    [
        "missing",
        "extra",
        "schema",
        "old_schema",
        "nan",
        "bool",
        "tangent",
        "xy",
        "order",
        "duplicate",
        "rate",
        "weighted",
    ],
)
def test_invalid_json_rejected(maya_cmds, bad):
    plug, _ = _existing_curve(maya_cmds, "source", "double")
    data = json.loads(
        json.dumps(KeyframeManager(plug).get_curve_data().to_dict())
    )
    if bad == "missing":
        del data["keys"][0]["breakdown"]
    elif bad == "extra":
        data["unexpected"] = 1
    elif bad == "schema":
        data["schema_version"] = 3
    elif bad == "old_schema":
        data["schema_version"] = 1
    elif bad == "nan":
        data["keys"][0]["value"] = float("nan")
    elif bad == "bool":
        data["keys"][0]["frame"] = True
    elif bad == "tangent":
        data["keys"][0]["in_tangent_type"] = "global"
    elif bad == "xy":
        data["keys"][0]["out_tangent_xy"] = [1]
    elif bad == "order":
        data["keys"].reverse()
    elif bad == "duplicate":
        data["keys"][1]["frame"] = data["keys"][0]["frame"]
    elif bad == "rate":
        data["seconds_per_frame"] = 0
    else:
        data["weighted"] = 1
    with pytest.raises((ValueError, TypeError)):
        AnimCurveData.from_dict(data)


def test_data_type_mismatch_does_not_queue(maya_cmds):
    plug, curve = _existing_curve(maya_cmds, "source", "double")
    data = KeyframeManager(plug).get_curve_data()
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    with pytest.raises(ValueError):
        keyframe.set_curve_data(replace(data, curve_type="animCurveTA"))
    with pytest.raises(ValueError):
        keyframe.get_key_data(10, 1)
    assert not mod.can_undo
    assert keyframe.get_curve_data() == data


def _fixed_curve(cmds, name, attribute_type, weighted):
    plug, curve = _existing_curve(cmds, name, attribute_type)
    curve.setIsWeighted(weighted)
    for i in range(curve.numKeys):
        curve.setTangentsLocked(i, False)
        curve.setWeightsLocked(i, False)
        curve.setTangent(i, 0.03, (i - 1) * 0.06, True, convertUnits=False)
        curve.setTangent(i, 0.09, (i % 2) * 0.04, False, convertUnits=False)
    return plug, curve


@pytest.mark.parametrize("source_weighted", [False, True])
@pytest.mark.parametrize("destination_weighted", [False, True])
@pytest.mark.parametrize(
    "attribute_type", ["double", "doubleAngle", "doubleLinear"]
)
def test_partial_uses_destination_weighted_and_matches_native_conversion(
    maya_cmds, source_weighted, destination_weighted, attribute_type
):
    plug, source = _fixed_curve(
        maya_cmds, "source", attribute_type, source_weighted
    )
    _, expected = _fixed_curve(
        maya_cmds, "reference", attribute_type, source_weighted
    )
    data = KeyframeManager(plug).get_key_data()
    source_before = _curve_state(source)
    expected.setIsWeighted(destination_weighted)
    target = _destination(maya_cmds, attribute_type, existing=True)
    actual = oma.MFnAnimCurve(target.sourceWithConversion().node())
    actual.setIsWeighted(destination_weighted)
    before = _curve_state(actual)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    keyframe.set_key_data(data)
    maya_cmds.currentUnit(linear="m", angle="rad")
    mod.do_it_dg()
    assert keyframe.get_weighted() is destination_weighted
    _assert_equivalent(_curve_state(actual), _curve_state(expected))
    for frame in (0, 1.5, 3, 4.5, 5.5, 7, 9, 10):
        time = om.MTime(frame, om.MTime.uiUnit())
        assert actual.evaluate(time) == pytest.approx(
            expected.evaluate(time), rel=2e-6, abs=2e-7
        )
    _assert_curve_state(_curve_state(source), source_before)
    for _ in range(2):
        mod.undo_it()
        _assert_curve_state(_curve_state(actual), before)
        mod.redo_it()
        _assert_equivalent(_curve_state(actual), _curve_state(expected))


@pytest.mark.parametrize("method", ["set_key_data", "set_curve_data"])
@pytest.mark.parametrize("weighted", [False, True])
def test_mutable_key_data_is_validated_and_copied_at_reservation(
    maya_cmds, method, weighted
):
    plug, _ = _fixed_curve(maya_cmds, "source", "double", weighted)
    data = KeyframeManager(plug).get_curve_data()
    for key in data.keys:
        key.frame += 12
        key.value *= 2
        key.breakdown = not key.breakdown
    mutable_xy = [0.05, 0.1]
    data.keys[1].in_tangent_xy = mutable_xy
    target = _destination(maya_cmds, "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    expected_values = [(key.frame, key.value) for key in data.keys]
    if method == "set_key_data":
        keyframe.set_key_data(data.keys)
    else:
        keyframe.set_curve_data(data)
    # Changes to the caller's objects after reservation must not affect execution.
    data.keys[1].frame = float("nan")
    data.keys[1].value = 1000
    data.keys[1].in_tangent_type = "invalid"
    mutable_xy[:] = [-1, float("inf")]
    assert keyframe.get_curve_data() is None
    mod.do_it_dg()
    assert keyframe.get_keys() == expected_values
    actual = keyframe.get_curve_data()
    assert actual.keys[1].in_tangent_type == "fixed"
    assert actual.keys[1].in_tangent_xy[1] / actual.keys[1].in_tangent_xy[
        0
    ] == pytest.approx(2)
    assert actual.weighted is (
        weighted if method == "set_curve_data" else False
    )
    for _ in range(2):
        mod.undo_it()
        assert keyframe.get_curve_data() is None
        mod.redo_it()
        assert keyframe.get_keys() == expected_values


@pytest.mark.parametrize(
    "method", ["set_key_data", "set_curve_data", "to_dict"]
)
@pytest.mark.parametrize(
    "field,value",
    [
        ("frame", float("nan")),
        ("frame", "bad"),
        ("value", float("inf")),
        ("in_tangent_type", "invalid"),
        ("out_tangent_xy", (-1, 0)),
        ("in_tangent_xy", (1,)),
        ("breakdown", 1),
        ("frame", 9.0),
    ],
)
def test_mutated_invalid_data_fails_before_reservation(
    maya_cmds, method, field, value
):
    plug, curve = _existing_curve(maya_cmds, "source", "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    data = keyframe.get_curve_data()
    setattr(data.keys[0], field, value)
    before = _curve_state(curve)
    with pytest.raises((TypeError, ValueError)):
        if method == "set_key_data":
            keyframe.set_key_data(data.keys)
        elif method == "set_curve_data":
            keyframe.set_curve_data(data)
        else:
            data.to_dict()
    _assert_curve_state(_curve_state(curve), before)
    assert not mod.can_undo


def test_partial_new_curve_default_is_independent_of_global_preferences(
    maya_cmds,
):
    plug, _ = _fixed_curve(maya_cmds, "source", "double", True)
    keys = KeyframeManager(plug).get_key_data()
    target = _destination(maya_cmds, "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    keyframe.set_key_data(keys)
    maya_cmds.keyTangent(g=True, weightedTangents=True)
    mod.do_it_dg()
    assert keyframe.get_weighted() is False


@pytest.mark.parametrize("weighted", [False, True])
def test_weighted_edit_matches_native_and_repeated_history(
    maya_cmds, weighted
):
    plug, curve = _fixed_curve(maya_cmds, "source", "double", weighted)
    _, reference = _fixed_curve(maya_cmds, "reference", "double", weighted)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(plug, modifier_manager=mod)
    before = _curve_state(curve)
    maya_cmds.flushUndo()
    keyframe.set_weighted(not weighted)
    assert keyframe.get_weighted() is weighted
    mod.do_it_dg()
    reference.setIsWeighted(not weighted)
    assert keyframe.get_weighted() is not weighted
    _assert_equivalent(_curve_state(curve), _curve_state(reference))
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        _assert_equivalent(_curve_state(curve), before)
        mod.redo_it()
        _assert_equivalent(_curve_state(curve), _curve_state(reference))


def test_weighted_queued_creation_order_noop_and_failure_rollback(maya_cmds):
    target = _destination(maya_cmds, "double")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    assert keyframe.get_weighted() is None
    keyframe.set_keys([(1, 0), (5, 1)])
    keyframe.set_weighted(True)
    keyframe.set_weighted(True)
    mod.do_it_dg()
    assert keyframe.get_weighted() is True
    before = keyframe.get_curve_data()
    keyframe.set_weighted(False)

    def fail(change):
        raise RuntimeError("injected failure")

    mod.queue_anim_curve_change(fail)
    with pytest.raises(RuntimeError, match="injected failure"):
        mod.do_it_dg()
    assert keyframe.get_curve_data() == before
    mod.undo_it()
    assert keyframe.get_weighted() is None
    mod.redo_it()
    assert keyframe.get_weighted() is True


def test_weighted_missing_curve_invalid_input_and_manager(maya_cmds):
    target = _destination(maya_cmds, "double")
    with pytest.raises(RuntimeError, match="ModifierManager"):
        KeyframeManager(target).set_weighted(True)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(target, modifier_manager=mod)
    for invalid in (1, "True", None):
        with pytest.raises(TypeError):
            keyframe.set_weighted(invalid)
    keyframe.set_weighted(True)
    with pytest.raises(RuntimeError, match="No channel"):
        mod.do_it_dg()
    assert keyframe.get_weighted() is None
    assert not mod.can_undo
