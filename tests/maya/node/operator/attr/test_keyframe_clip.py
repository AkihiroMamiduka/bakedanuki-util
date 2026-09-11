from __future__ import annotations

import json

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import AnimCurveData, KeyframeManager
from bd_util.maya.node.operator.attr import _keyframe_snapshot as snapshot
from test_keyframe_set_equivalence import restore_animation_preferences

pytestmark = pytest.mark.maya


def _source(cmds, weighted=False, tangent="auto", attribute_type="double"):
    node = cmds.createNode("transform", name="source")
    cmds.addAttr(
        node, longName="value", attributeType=attribute_type, keyable=True
    )
    selection = om.MSelectionList()
    selection.add(node + ".value")
    plug = selection.getPlug(0)
    curve = oma.MFnAnimCurve()
    curve.create(plug)
    curve.setIsWeighted(weighted)
    for frame, value in ((-100, 0), (-50, 5), (0, -2), (50, 8), (100, 1)):
        curve.addKey(
            om.MTime(frame, om.MTime.uiUnit()),
            value,
            oma.MFnAnimCurve.kTangentAuto,
            snapshot._TANGENTS[tangent],
        )
    for i in range(curve.numKeys):
        curve.setIsBreakdown(i, i % 2 == 1)
    if weighted:
        for i in range(curve.numKeys):
            curve.setTangentsLocked(i, False)
            curve.setWeightsLocked(i, False)
            x, y = curve.getTangentXY(i, True)
            curve.setTangent(i, x * 0.6, y * 0.6, True, convertUnits=False)
    return KeyframeManager(plug), curve


def _restore(cmds, data):
    name = cmds.createNode("transform", name="destination")
    attribute = {
        "animCurveTA": "rx",
        "animCurveTL": "tx",
        "animCurveTU": "sx",
    }[data.curve_type]
    selection = om.MSelectionList()
    selection.add(name + "." + attribute)
    plug = selection.getPlug(0)
    mod = bdu.ModifierManager()
    manager = KeyframeManager(plug, modifier_manager=mod)
    manager.set_curve_data(
        AnimCurveData.from_dict(json.loads(json.dumps(data.to_dict())))
    )
    mod.do_it_dg()
    return manager, oma.MFnAnimCurve(plug), mod


def _assert_shape(source, actual, start, end):
    frames = [start + (end - start) * i / 300 for i in range(301)]
    frames += [
        frame + offset
        for frame in (-100, -50, 0, 50, 100)
        for offset in (-0.001, 0, 0.001)
        if start <= frame + offset <= end
    ]
    for frame in frames:
        time = om.MTime(frame, om.MTime.uiUnit())
        assert actual.evaluate(time) == pytest.approx(
            source.evaluate(time), rel=2e-6, abs=2e-7
        ), frame


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("tangent", tuple(snapshot._TANGENTS))
def test_clip_preserves_shape_for_tangent_types(maya_cmds, weighted, tangent):
    manager, source = _source(maya_cmds, weighted, tangent)
    before = manager.get_curve_data()
    data = manager.get_curve_data(-75, 75)
    assert [key.frame for key in data.keys] == [-75, -50, 0, 50, 75]
    assert [key.breakdown for key in data.keys[1:-1]] == [True, False, True]
    assert not data.keys[0].breakdown and not data.keys[-1].breakdown
    assert manager.get_key_data(-75, 75) == list(data.keys)
    assert manager.get_curve_data() == before
    destination, actual, mod = _restore(maya_cmds, data)
    _assert_shape(source, actual, -75, 75)
    for _ in range(2):
        mod.undo_it()
        assert destination.get_curve_data() is None
        mod.redo_it()
        _assert_shape(source, actual, -75, 75)


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize(
    "attribute_type", ["double", "doubleAngle", "doubleLinear"]
)
@pytest.mark.parametrize(
    "bounds, frames",
    [
        ((-75, -60), [-75, -60]),
        ((-50, 50), [-50, 0, 50]),
        ((None, 25), [-100, -50, 0, 25]),
        ((-25, None), [-25, 0, 50, 100]),
        ((12.25, 12.25), [12.25]),
        ((0, 0), [0]),
    ],
)
def test_clip_bounds_units_and_single_frame(
    maya_cmds, weighted, attribute_type, bounds, frames
):
    manager, source = _source(
        maya_cmds, weighted, attribute_type=attribute_type
    )
    maya_cmds.currentUnit(angle="rad", linear="m")
    data = manager.get_curve_data(*bounds)
    assert [key.frame for key in data.keys] == frames
    _, actual, _ = _restore(maya_cmds, data)
    _assert_shape(source, actual, frames[0], frames[-1])
    seconds = frames[0] * data.seconds_per_frame
    expected = source.evaluate(om.MTime(seconds, om.MTime.kSeconds))
    maya_cmds.currentUnit(time="ntsc", updateAnimation=False)
    _, actual, _ = _restore(maya_cmds, data)
    assert actual.evaluate(
        om.MTime(seconds, om.MTime.kSeconds)
    ) == pytest.approx(expected)


@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("tangent", ["auto", "step", "stepnext"])
@pytest.mark.parametrize("infinity", ["constant", "linear"])
@pytest.mark.parametrize("bounds", [(-150, 150), (-175, -125), (125, 175)])
def test_clip_extends_constant_and_linear_infinity(
    maya_cmds, weighted, tangent, infinity, bounds
):
    manager, source = _source(maya_cmds, weighted, tangent)
    source.setPreInfinityType(snapshot._INFINITY[infinity])
    source.setPostInfinityType(snapshot._INFINITY[infinity])
    data = manager.get_curve_data(*bounds)
    assert data.keys[0].frame == bounds[0] and data.keys[-1].frame == bounds[1]
    _, actual, _ = _restore(maya_cmds, data)
    _assert_shape(source, actual, *bounds)


@pytest.mark.parametrize("infinity", ["cycle", "cycleRelative", "oscillate"])
@pytest.mark.parametrize(
    "bounds", [(-150, 25), (-25, 150), (-200, -150), (150, 200)]
)
def test_clip_rejects_cyclic_extrapolation(maya_cmds, infinity, bounds):
    manager, source = _source(maya_cmds)
    source.setPreInfinityType(snapshot._INFINITY[infinity])
    source.setPostInfinityType(snapshot._INFINITY[infinity])
    before = manager.get_curve_data()
    with pytest.raises(RuntimeError, match="cyclic infinity"):
        manager.get_curve_data(*bounds)
    assert manager.get_curve_data() == before
    assert (
        manager.get_curve_data(*bounds, include_boundaries=False) is not None
    )
    data = manager.get_curve_data(-75, 75)
    _, actual, _ = _restore(maya_cmds, data)
    _assert_shape(source, actual, -75, 75)


def test_existing_keys_only_and_unbounded_query_preserve_metadata(maya_cmds):
    manager, _ = _source(maya_cmds, True)
    full = manager.get_curve_data()
    assert full == manager.get_curve_data(include_boundaries=False)
    assert manager.get_key_data() == list(full.keys)
    assert manager.get_key_data(-75, -60, include_boundaries=False) == []
    data = manager.get_curve_data(-50, 50, include_boundaries=False)
    assert data.keys == full.keys[1:4]
    assert manager.get_key_data(-50, 50, include_boundaries=False) == list(
        data.keys
    )


@pytest.mark.parametrize("modified", [False, True])
@pytest.mark.parametrize("fail", [False, True])
def test_query_preserves_scene_history_pending_work_and_temporary_nodes(
    maya_cmds, monkeypatch, modified, fail
):
    manager, source = _source(maya_cmds)
    before = manager.get_curve_data()
    mod = bdu.ModifierManager()
    pending = KeyframeManager(manager.plug, modifier_manager=mod)
    pending.set_key(999, frame=999)
    marker = maya_cmds.createNode("transform", name="undoMarker")
    maya_cmds.setAttr(marker + ".tx", 5)
    maya_cmds.undo()
    history = (
        maya_cmds.undoInfo(q=True, undoName=True),
        maya_cmds.undoInfo(q=True, redoName=True),
    )
    nodes = set(maya_cmds.ls())
    selection = maya_cmds.ls(selection=True)
    time = maya_cmds.currentTime(q=True)
    added = []
    handles = []
    native_restore = snapshot._restore_key_data

    def restore(curve, *args, **kwargs):
        handles.append(om.MObjectHandle(curve.object()))
        native_restore(curve, *args, **kwargs)
        if fail:
            raise RuntimeError("injected clip failure")

    monkeypatch.setattr(snapshot, "_restore_key_data", restore)
    callback = om.MDGMessage.addNodeAddedCallback(
        lambda node, client: added.append(node), "animCurve"
    )
    maya_cmds.file(modified=modified)
    try:
        if fail:
            with pytest.raises(RuntimeError, match="injected clip failure"):
                pending.get_curve_data(-75, 75)
        else:
            pending.get_curve_data(-75, 75)
        assert maya_cmds.file(q=True, modified=True) == modified
        assert not added
        assert handles and all(not handle.isAlive() for handle in handles)
        assert set(maya_cmds.ls()) == nodes
        assert maya_cmds.ls(selection=True) == selection
        assert maya_cmds.currentTime(q=True) == time
        assert (
            maya_cmds.undoInfo(q=True, undoName=True),
            maya_cmds.undoInfo(q=True, redoName=True),
        ) == history
        assert manager.get_curve_data() == before
        assert not mod.can_undo
        maya_cmds.redo()
        assert maya_cmds.getAttr(marker + ".tx") == 5
    finally:
        om.MMessage.removeCallback(callback)


@pytest.mark.parametrize("keys", [0, 1])
def test_empty_and_single_key_curve(maya_cmds, keys):
    manager, source = _source(maya_cmds)
    for i in reversed(range(keys, source.numKeys)):
        source.remove(i)
    source.setPreInfinityType(oma.MFnAnimCurve.kCycle)
    source.setPostInfinityType(oma.MFnAnimCurve.kCycle)
    data = manager.get_curve_data(-150, 150)
    assert [key.frame for key in data.keys] == (
        [-150, -100, 150] if keys else []
    )
    if keys:
        _, actual, _ = _restore(maya_cmds, data)
        _assert_shape(source, actual, -150, 150)


@pytest.mark.parametrize("method", ["get_key_data", "get_curve_data"])
@pytest.mark.parametrize(
    "kwargs",
    [
        {"start_frame": 2, "end_frame": 1},
        {"start_frame": float("nan")},
        {"end_frame": float("inf")},
        {"include_boundaries": 1},
    ],
)
def test_invalid_range_rejected_even_without_curve(maya_cmds, method, kwargs):
    node = maya_cmds.createNode("transform")
    selection = om.MSelectionList()
    selection.add(node + ".tx")
    manager = KeyframeManager(selection.getPlug(0))
    with pytest.raises((ValueError, TypeError)):
        getattr(manager, method)(**kwargs)
    assert manager.get_key_data(-50, 50) == []
    assert manager.get_curve_data(-50, 50) is None
