from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_bake
from bd_util.maya.node._animation_clip_capture import layer_input
from bd_util.maya.node.operator.attr import KeyframeManager

pytestmark = [pytest.mark.maya, pytest.mark.usefixtures("new_scene")]


@pytest.fixture(autouse=True)
def scene_settings(maya_cmds):
    cmds = maya_cmds
    time = cmds.currentUnit(query=True, time=True)
    minimum = cmds.playbackOptions(query=True, minTime=True)
    maximum = cmds.playbackOptions(query=True, maxTime=True)
    cmds.currentUnit(time="film")
    yield
    cmds.currentUnit(time=time)
    cmds.playbackOptions(minTime=minimum, maxTime=maximum)


def _plug(name):
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getPlug(0)


def _source(name):
    sources = _plug(name).connectedTo(True, False)
    return None if not sources else sources[0].name()


def _keyframe(name, manager):
    return KeyframeManager(_plug(name), modifier_manager=manager)


def _keys(cmds, name):
    return list(
        zip(
            cmds.keyframe(name, query=True, timeChange=True) or [],
            cmds.keyframe(name, query=True, valueChange=True) or [],
        )
    )


def _curve(name):
    selection = om.MSelectionList()
    selection.add(name)
    return oma.MFnAnimCurve(selection.getDependNode(0))


def _values(cmds, name, frames):
    return [cmds.getAttr(name, time=frame) for frame in frames]


def _animated_driver(cmds, name="driver", attributes=("tx", "ty", "tz")):
    node = cmds.createNode("transform", name=name)
    for index, attribute in enumerate(attributes, 1):
        for frame, value in ((1, index * 2), (5, index * 10)):
            cmds.setKeyframe(
                node + "." + attribute,
                time=frame,
                value=value,
                inTangentType="linear",
                outTangentType="linear",
            )
    return node


def test_default_playback_range_bakes_one_constraint_channel(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    constraint = cmds.pointConstraint(driver, target)[0]
    frames = tuple(range(1, 6))
    expected = _values(cmds, target + ".tx", frames)
    original_x = _source(target + ".tx")
    original_y = _source(target + ".ty")
    cmds.playbackOptions(minTime=1, maxTime=5)
    cmds.currentTime(3)
    cmds.select(driver)
    manager = bdu.ModifierManager()

    assert _keyframe(target + ".tx", manager).bake() is None
    cmds.playbackOptions(minTime=2, maxTime=4)
    assert _source(target + ".tx") == original_x
    assert not manager.can_undo

    manager.do_it_dg()
    curve = _source(target + ".tx").split(".")[0]
    assert cmds.nodeType(curve) == "animCurveTL"
    assert cmds.keyframe(curve, query=True, timeChange=True) == list(frames)
    assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)
    assert _source(target + ".ty") == original_y
    assert cmds.objExists(constraint)
    assert cmds.currentTime(query=True) == 3
    assert cmds.ls(selection=True) == [driver]

    for _ in range(2):
        manager.undo_it()
        assert _source(target + ".tx") == original_x
        assert _source(target + ".ty") == original_y
        assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)
        manager.redo_it()
        assert (
            cmds.nodeType(_source(target + ".tx").split(".")[0])
            == "animCurveTL"
        )
        assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)


def test_explicit_subframe_range_includes_end_and_keeps_expression(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    expression = cmds.expression(
        name="driverExpression", string="target.rx = time * 10;"
    )
    frames = (-1.5, 0.0, 1.5, 2.5)
    expected = _values(cmds, target + ".rx", frames)
    manager = bdu.ModifierManager()
    _keyframe(target + ".rx", manager).bake(-1.5, 2.5, sample_by=1.5)
    manager.do_it_dg()

    curve = _source(target + ".rx").split(".")[0]
    assert cmds.nodeType(curve) == "animCurveTA"
    assert cmds.keyframe(curve, query=True, timeChange=True) == list(frames)
    assert _values(cmds, target + ".rx", frames) == pytest.approx(expected)
    assert cmds.keyTangent(curve, query=True, inTangentType=True) == [
        "linear"
    ] * len(frames)
    assert cmds.keyTangent(curve, query=True, outTangentType=True) == [
        "linear"
    ] * len(frames)
    assert cmds.objExists(expression)


def test_execution_samples_current_scene_after_reservation(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    constraint = cmds.pointConstraint(driver, target)[0]
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5, sample_by=2)
    cmds.keyframe(driver + ".tx", edit=True, valueChange=100)
    expected = _values(cmds, target + ".tx", (1, 3, 5))

    manager.do_it_dg()
    assert _values(cmds, target + ".tx", (1, 3, 5)) == pytest.approx(expected)
    assert cmds.objExists(constraint)


def test_reservation_time_unit_defines_physical_sample_times(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    cmds.pointConstraint(driver, target)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5, sample_by=2)

    cmds.currentUnit(time="ntsc", updateAnimation=False)
    current_frames = (1.25, 3.75, 6.25)
    expected = _values(cmds, target + ".tx", current_frames)
    manager.do_it_dg()

    curve = _source(target + ".tx").split(".")[0]
    assert cmds.keyframe(curve, query=True, timeChange=True) == list(
        current_frames
    )
    assert _values(cmds, target + ".tx", current_frames) == pytest.approx(
        expected
    )


def test_static_channel_creates_constant_curve(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    cmds.setAttr(target + ".sx", 2.5)
    manager = bdu.ModifierManager()
    _keyframe(target + ".sx", manager).bake(4, 4)
    manager.do_it_dg()

    curve = _source(target + ".sx").split(".")[0]
    assert cmds.nodeType(curve) == "animCurveTU"
    assert _keys(cmds, curve) == [(4.0, 2.5)]
    assert _values(cmds, target + ".sx", (-10, 4, 20)) == [2.5, 2.5, 2.5]


def test_discrete_channel_uses_step_tangents(maya_cmds):
    cmds = maya_cmds
    driver = cmds.createNode("transform", name="driver")
    target = cmds.createNode("transform", name="target")
    for frame, value in ((1, False), (3, True)):
        cmds.setKeyframe(
            driver + ".visibility",
            time=frame,
            value=value,
            outTangentType="step",
        )
    cmds.connectAttr(driver + ".visibility", target + ".visibility")
    expected = _values(cmds, target + ".visibility", (1, 2, 3))
    manager = bdu.ModifierManager()
    _keyframe(target + ".visibility", manager).bake(1, 3)
    manager.do_it_dg()

    curve = _source(target + ".visibility").split(".")[0]
    assert cmds.keyTangent(curve, query=True, outTangentType=True) == [
        "step",
        "step",
        "step",
    ]
    assert _values(cmds, target + ".visibility", (1, 2, 3)) == expected


def test_enum_channel_uses_step_tangents(maya_cmds):
    cmds = maya_cmds
    driver = cmds.createNode("transform", name="driver")
    target = cmds.createNode("transform", name="target")
    for node in (driver, target):
        cmds.addAttr(
            node, longName="mode", attributeType="enum", enumName="A:B:C"
        )
    for frame, value in ((1, 0), (3, 2)):
        cmds.setKeyframe(
            driver + ".mode",
            time=frame,
            value=value,
            outTangentType="step",
        )
    cmds.connectAttr(driver + ".mode", target + ".mode")
    manager = bdu.ModifierManager()
    _keyframe(target + ".mode", manager).bake(1, 3)
    manager.do_it_dg()

    curve = _source(target + ".mode").split(".")[0]
    assert cmds.keyTangent(curve, query=True, outTangentType=True) == [
        "step",
        "step",
        "step",
    ]
    assert _values(cmds, target + ".mode", (1, 2, 3)) == [0, 0, 2]


def test_existing_direct_curve_is_reused_and_fully_replaced(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    for frame, value in ((-10, -3), (1, 2), (5, 10), (20, 50)):
        cmds.setKeyframe(
            target + ".tx", time=frame, value=value, outTangentType="linear"
        )
    curve = _source(target + ".tx").split(".")[0]
    cmds.keyTangent(curve, edit=True, weightedTangents=True)
    _curve(curve).setPreInfinityType(oma.MFnAnimCurve.kCycle)
    _curve(curve).setPostInfinityType(oma.MFnAnimCurve.kLinear)
    original_keys = _keys(cmds, curve)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5, sample_by=2)
    manager.do_it_dg()

    assert _source(target + ".tx") == curve + ".output"
    assert cmds.keyframe(curve, query=True, timeChange=True) == [1, 3, 5]
    assert cmds.keyTangent(curve, query=True, weightedTangents=True) == [False]
    assert _curve(curve).preInfinityType == oma.MFnAnimCurve.kConstant
    assert _curve(curve).postInfinityType == oma.MFnAnimCurve.kConstant
    manager.undo_it()
    assert _keys(cmds, curve) == original_keys
    assert cmds.keyTangent(curve, query=True, weightedTangents=True) == [True]
    assert _curve(curve).preInfinityType == oma.MFnAnimCurve.kCycle
    assert _curve(curve).postInfinityType == oma.MFnAnimCurve.kLinear


def test_shared_curve_is_preserved_for_other_destination(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("animCurveTL", name="sharedCurve")
    for frame, value in ((1, 2), (5, 10)):
        cmds.setKeyframe(source, time=frame, value=value)
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.connectAttr(source + ".output", first + ".tx")
    cmds.connectAttr(source + ".output", second + ".tx")
    manager = bdu.ModifierManager()
    _keyframe(first + ".tx", manager).bake(1, 5)
    manager.do_it_dg()

    assert _source(first + ".tx") != source + ".output"
    assert _source(second + ".tx") == source + ".output"
    assert cmds.objExists(source)
    assert _keys(cmds, source) == [(1.0, 2.0), (5.0, 10.0)]
    manager.undo_it()
    assert _source(first + ".tx") == source + ".output"


def test_parent_compound_connection_preserves_siblings(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".translate", target + ".translate")
    frames = (1, 3, 5)
    expected = _values(cmds, target + ".tx", frames)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5, sample_by=2)
    manager.do_it_dg()

    assert (
        cmds.nodeType(_source(target + ".tx").split(".")[0]) == "animCurveTL"
    )
    assert _source(target + ".ty") == driver + ".translateY"
    assert _source(target + ".tz") == driver + ".translateZ"
    assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)
    manager.undo_it()
    assert _source(target + ".translate") == driver + ".translate"
    assert _source(target + ".tx") is None
    assert _source(target + ".ty") is None
    manager.redo_it()
    assert _source(target + ".ty") == driver + ".translateY"


def _layered_channel(cmds):
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    for frame, value in ((1, 3), (5, 7)):
        cmds.setKeyframe(
            target + ".tx",
            animLayer=layer,
            time=frame,
            value=value,
            noResolve=True,
            inTangentType="linear",
            outTangentType="linear",
        )
    cmds.setAttr(layer + ".weight", 0.5)
    destination = layer_input(_plug(target + ".tx"), None)
    source = destination.connectedTo(True, False)
    if source:
        cmds.disconnectAttr(source[0].name(), destination.name())
    cmds.connectAttr(driver + ".tx", destination.name())
    return driver, target, layer, destination


def test_default_bake_replaces_base_input_and_preserves_other_layer(maya_cmds):
    cmds = maya_cmds
    driver, target, layer, destination = _layered_channel(cmds)
    frames = (1, 2, 3, 4, 5)
    expected = _values(cmds, target + ".tx", frames)
    layer_curve = cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_keys = _keys(cmds, layer_curve)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5)
    manager.do_it_dg()

    assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)
    assert _source(destination.name()).endswith(".output")
    assert _source(destination.name()) != driver + ".translateX"
    assert _keys(cmds, layer_curve) == layer_keys
    assert cmds.getAttr(layer + ".weight") == 0.5
    manager.undo_it()
    assert _source(destination.name()) == driver + ".translateX"
    assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)


def test_explicit_layer_bake_replaces_only_that_layer_input(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    for frame, value in ((1, 10), (5, 20)):
        cmds.setKeyframe(target + ".tx", time=frame, value=value)
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")
    destination = layer_input(_plug(target + ".tx"), layer)
    cmds.connectAttr(driver + ".tx", destination.name(), force=True)
    frames = (1, 3, 5)
    expected = _values(cmds, target + ".tx", frames)
    base_curve = cmds.animLayer(
        cmds.animLayer(query=True, root=True),
        query=True,
        findCurveForPlug=target + ".tx",
    )[0]
    base_keys = _keys(cmds, base_curve)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).anim_layer(layer).bake(
        1, 5, sample_by=2
    )
    manager.do_it_dg()

    assert _values(cmds, target + ".tx", frames) == pytest.approx(expected)
    assert _source(destination.name()) != driver + ".translateX"
    assert _keys(cmds, base_curve) == base_keys
    assert cmds.animLayer(layer, query=True, findCurveForPlug=target + ".tx")
    manager.undo_it()
    assert _source(destination.name()) == driver + ".translateX"


@pytest.mark.parametrize(
    "lock_kind", ["target_plug", "target_node", "source_node", "layer"]
)
def test_locked_targets_fail_without_partial_changes(maya_cmds, lock_kind):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    constraint = cmds.pointConstraint(driver, target)[0]
    keyframe = None
    if lock_kind == "target_plug":
        cmds.setAttr(target + ".tx", lock=True)
    elif lock_kind == "target_node":
        cmds.lockNode(target, lock=True)
    elif lock_kind == "source_node":
        cmds.lockNode(constraint, lock=True)
    else:
        layer = cmds.animLayer("Upper")
        cmds.animLayer(layer, edit=True, attribute=target + ".tx")
        cmds.setAttr(layer + ".lock", True)
    manager = bdu.ModifierManager()
    keyframe = _keyframe(target + ".tx", manager)
    if lock_kind == "layer":
        keyframe = keyframe.anim_layer(layer)
    original = _source(target + ".tx")
    keyframe.bake(1, 5)
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert _source(target + ".tx") == original
    assert not manager.can_undo


def test_referenced_channel_fails_without_changes(maya_cmds, tmp_path):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    for frame, value in ((1, 2), (5, 10)):
        cmds.setKeyframe(target + ".tx", time=frame, value=value)
    path = str(tmp_path / "bake_reference.ma")
    cmds.file(rename=path)
    cmds.file(save=True, type="mayaAscii")
    cmds.file(new=True, force=True)
    cmds.file(path, reference=True, namespace="ref")
    plug = "ref:target.tx"
    original = _keys(cmds, _source(plug).split(".")[0])
    manager = bdu.ModifierManager()
    _keyframe(plug, manager).bake(1, 5)

    with pytest.raises(RuntimeError, match="referenced"):
        manager.do_it_dg()
    assert _keys(cmds, _source(plug).split(".")[0]) == original
    assert not manager.can_undo


def test_later_failure_rolls_back_connection_and_created_curve(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    cmds.pointConstraint(driver, target)
    original = _source(target + ".tx")
    curves = set(cmds.ls(type="animCurve") or [])
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5)

    def fail(modifier):
        del modifier
        raise RuntimeError("injected failure")

    manager.queue_dg_modifier(fail)
    with pytest.raises(RuntimeError, match="injected failure"):
        manager.do_it_dg()
    assert _source(target + ".tx") == original
    assert set(cmds.ls(type="animCurve") or []) == curves
    assert not manager.can_undo


def test_post_bake_verification_failure_rolls_back_changes(
    maya_cmds, monkeypatch
):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    cmds.pointConstraint(driver, target)
    original = _source(target + ".tx")
    curves = set(cmds.ls(type="animCurve") or [])
    sample = _keyframe_bake._sample
    call_count = 0

    def changed_verification(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        result = sample(*args, **kwargs)
        if call_count == 2:
            return tuple((frame, value + 1) for frame, value in result)
        return result

    monkeypatch.setattr(_keyframe_bake, "_sample", changed_verification)
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5)

    with pytest.raises(RuntimeError, match="Cannot preserve baked value"):
        manager.do_it_dg()
    assert _source(target + ".tx") == original
    assert set(cmds.ls(type="animCurve") or []) == curves
    assert not manager.can_undo


@pytest.mark.parametrize(
    "args,kwargs,error",
    [
        ((5, 1), {}, ValueError),
        ((float("nan"), 1), {}, ValueError),
        ((1, float("inf")), {}, ValueError),
        ((True, 5), {}, TypeError),
        (("1", 5), {}, TypeError),
        ((1, 5), {"sample_by": 0}, ValueError),
        ((1, 5), {"sample_by": -1}, ValueError),
        ((1, 5), {"sample_by": True}, TypeError),
        ((1, 5), {"sample_by": "1"}, TypeError),
        ((0, 10_000_001), {"sample_by": 1}, ValueError),
    ],
)
def test_invalid_arguments_do_not_queue_changes(
    maya_cmds, args, kwargs, error
):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    with pytest.raises(error):
        _keyframe(target + ".tx", manager).bake(*args, **kwargs)
    assert _source(target + ".tx") is None
    assert not manager.can_undo


def test_bake_requires_modifier_and_supported_scalar(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    with pytest.raises(RuntimeError, match="ModifierManager"):
        KeyframeManager(_plug(target + ".tx")).bake(1, 5)
    cmds.addAttr(target, longName="timeValue", attributeType="time")
    manager = bdu.ModifierManager()
    with pytest.raises(RuntimeError, match="TA / TL / TU"):
        _keyframe(target + ".timeValue", manager).bake(1, 5)
    assert not manager.can_undo


def test_nonfinite_sample_is_rejected_and_connection_is_preserved(maya_cmds):
    cmds = maya_cmds
    source = cmds.createNode("multiplyDivide", name="source")
    target = cmds.createNode("transform", name="target")
    cmds.setAttr(source + ".input1X", float("nan"))
    cmds.connectAttr(source + ".outputX", target + ".tx")
    manager = bdu.ModifierManager()
    _keyframe(target + ".tx", manager).bake(1, 5)
    with pytest.raises(ValueError, match="finite"):
        manager.do_it_dg()
    assert _source(target + ".tx") == source + ".outputX"
    assert not manager.can_undo
