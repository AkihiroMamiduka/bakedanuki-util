from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import _keyframe_bake

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


def _node(name, manager):
    return bdu.Nodes(modifier_manager=manager).existing(name)


def _animated_driver(cmds, attributes=("tx", "ty", "tz")):
    node = cmds.createNode("transform", name="driver")
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


def test_automatic_bake_collects_static_and_animated_keyable_channels(
    maya_cmds,
):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    constraint = cmds.pointConstraint(driver, target)[0]
    frames = (1, 3, 5)
    expected = {
        attr: [
            cmds.getAttr(target + "." + attr, time=frame) for frame in frames
        ]
        for attr in ("tx", "ty", "tz")
    }
    manager = bdu.ModifierManager()

    assert _node(target, manager).keyframes.bake(1, 5, sample_by=2) is None
    assert _source(target + ".tx") != driver + ".translateX"
    assert not manager.can_undo
    manager.do_it_dg()

    for attr in ("tx", "ty", "tz"):
        source = _source(target + "." + attr)
        assert source is not None
        curve = source.split(".")[0]
        assert cmds.nodeType(curve) == "animCurveTL"
        assert cmds.keyframe(curve, query=True, timeChange=True) == [1, 3, 5]
        assert [
            cmds.getAttr(target + "." + attr, time=frame) for frame in frames
        ] == pytest.approx(expected[attr])
    for attr, curve_type, value in (
        ("rx", "animCurveTA", 0.0),
        ("sx", "animCurveTU", 1.0),
    ):
        source = _source(target + "." + attr)
        curve = source.split(".")[0]
        assert cmds.nodeType(curve) == curve_type
        assert cmds.keyframe(curve, query=True, timeChange=True) == [1, 3, 5]
        assert [
            cmds.getAttr(target + "." + attr, time=frame) for frame in frames
        ] == [value] * len(frames)
    assert cmds.objExists(constraint)

    manager.undo_it()
    for attr in ("tx", "ty", "tz"):
        assert cmds.nodeType(_source(target + "." + attr).split(".")[0]) == (
            "pointConstraint"
        )
    assert _source(target + ".rx") is None
    assert _source(target + ".sx") is None
    manager.redo_it()
    assert cmds.nodeType(_source(target + ".tx").split(".")[0]) == (
        "animCurveTL"
    )


def test_multiple_explicit_leaves_detach_parent_once_and_preserve_sibling(
    maya_cmds,
):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".translate", target + ".translate")
    original = _source(target + ".translate")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        5,
        attributes=["translateX", "translateY"],
        include_static=True,
        sample_by=2,
    )
    manager.do_it_dg()

    for attr in ("tx", "ty"):
        assert cmds.nodeType(_source(target + "." + attr).split(".")[0]) == (
            "animCurveTL"
        )
    assert _source(target + ".tz") == driver + ".translateZ"
    manager.undo_it()
    assert _source(target + ".translate") == original
    assert _source(target + ".tx") is None
    assert _source(target + ".ty") is None


def test_explicit_compound_expands_and_deduplicates_leaves(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".translate", target + ".translate")
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        5,
        attributes=["translate", "translateX"],
        include_static=True,
        sample_by=2,
    )
    manager.do_it_dg()

    assert _source(target + ".translate") is None
    for attr in ("tx", "ty", "tz"):
        source = _source(target + "." + attr)
        assert cmds.nodeType(source.split(".")[0]) == "animCurveTL"


def test_explicit_array_uses_only_existing_elements(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("plusMinusAverage", name="target")
    cmds.setAttr(target + ".input1D[2]", 3.5)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        3,
        attributes=["input1D"],
        include_static=True,
    )
    manager.do_it_dg()

    source = _source(target + ".input1D[2]")
    assert cmds.nodeType(source.split(".")[0]) == "animCurveTU"
    assert cmds.getAttr(target + ".input1D", multiIndices=True) == [2]

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        3,
        attributes=["input1D[5]"],
        include_static=True,
    )
    with pytest.raises(ValueError, match="does not exist"):
        manager.do_it_dg()
    assert cmds.getAttr(target + ".input1D", multiIndices=True) == [2]


def test_all_channels_are_sampled_before_any_connection_is_changed(
    maya_cmds, monkeypatch
):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".translate", target + ".translate")
    original_sample = _keyframe_bake._sample
    calls = 0

    def inspect_sample(*args, **kwargs):
        nonlocal calls
        if calls < 2:
            assert cmds.isConnected(
                driver + ".translate", target + ".translate"
            )
        calls += 1
        return original_sample(*args, **kwargs)

    monkeypatch.setattr(_keyframe_bake, "_sample", inspect_sample)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        5,
        attributes=["tx", "ty"],
        include_static=True,
    )
    manager.do_it_dg()
    assert calls == 4


def test_static_filter_and_include_static_are_consistent_for_explicit_attrs(
    maya_cmds,
):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    cmds.setAttr(target + ".sx", 2.5)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(4, 4, attributes=["sx"])
    manager.do_it_dg()
    source = _source(target + ".sx")
    assert cmds.keyframe(
        source.split(".")[0], query=True, timeChange=True
    ) == [4]
    assert cmds.getAttr(target + ".sx", time=4) == 2.5
    manager.undo_it()

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        4, 4, attributes=["sx"], include_static=False
    )
    with pytest.raises(ValueError, match="include_static"):
        manager.do_it_dg()
    assert _source(target + ".sx") is None
    assert not manager.can_undo


def test_channel_box_and_explicit_nonkeyable_collection(maya_cmds):
    cmds = maya_cmds
    driver = cmds.createNode("transform", name="driver")
    target = cmds.createNode("transform", name="target")
    cmds.addAttr(
        driver, longName="custom", attributeType="double", keyable=True
    )
    cmds.addAttr(target, longName="custom", attributeType="double")
    cmds.setAttr(target + ".custom", channelBox=True)
    cmds.setKeyframe(driver + ".custom", time=1, value=2)
    cmds.setKeyframe(driver + ".custom", time=5, value=10)
    cmds.connectAttr(driver + ".custom", target + ".custom")

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(1, 5, include_static=False)
    with pytest.raises(ValueError, match="animated attributes"):
        manager.do_it_dg()
    assert _source(target + ".custom") == driver + ".custom"

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1, 5, include_channel_box=True, sample_by=2
    )
    manager.do_it_dg()
    assert cmds.nodeType(_source(target + ".custom").split(".")[0]) == (
        "animCurveTU"
    )

    manager.undo_it()
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1, 5, attributes=["custom"], sample_by=2
    )
    manager.do_it_dg()
    assert cmds.nodeType(_source(target + ".custom").split(".")[0]) == (
        "animCurveTU"
    )


def test_automatic_collection_skips_locked_but_explicit_rejects_it(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".tx", target + ".tx")
    cmds.setAttr(target + ".ty", lock=True)
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(1, 5, sample_by=2)
    manager.do_it_dg()
    assert cmds.nodeType(_source(target + ".tx").split(".")[0]) == (
        "animCurveTL"
    )

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1, 5, attributes=["ty"], include_static=True
    )
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert not manager.can_undo


def test_explicit_missing_and_unsupported_attributes_fail_at_execution(
    maya_cmds,
):
    target = maya_cmds.createNode("transform", name="target")
    for attribute, error in (("missing", ValueError), ("message", TypeError)):
        manager = bdu.ModifierManager()
        _node(target, manager).keyframes.bake(
            1, 5, attributes=[attribute], include_static=True
        )
        with pytest.raises(error):
            manager.do_it_dg()
        assert not manager.can_undo


def test_explicit_layer_membership_and_automatic_filter(maya_cmds):
    cmds = maya_cmds
    target = cmds.createNode("transform", name="target")
    layer = cmds.animLayer("Upper")
    cmds.animLayer(layer, edit=True, attribute=target + ".tx")

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).bake(
        1, 3, include_static=True
    )
    manager.do_it_dg()
    curves = cmds.animLayer(layer, query=True, findCurveForPlug=target + ".tx")
    assert curves
    assert (
        cmds.animLayer(layer, query=True, findCurveForPlug=target + ".ty")
        is None
    )

    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.anim_layer(layer).bake(
        1, 3, attributes=["ty"], include_static=True
    )
    with pytest.raises(RuntimeError, match="not a member"):
        manager.do_it_dg()
    assert not manager.can_undo


def test_pending_layer_registration_and_node_bake_share_one_history(
    maya_cmds,
):
    cmds = maya_cmds
    target_name = cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    target = nodes.existing.transform(target_name)
    layer = nodes.create.animLayer(name="PendingLayer")
    layer.add_plugs([target.tx])
    target.keyframes.anim_layer(layer).bake(
        1, 3, attributes=["tx"], include_static=True
    )
    manager.do_it_dg()

    curves = cmds.animLayer(
        "PendingLayer", query=True, findCurveForPlug=target_name + ".tx"
    )
    assert curves
    assert cmds.keyframe(curves[0], query=True, timeChange=True) == [1, 2, 3]
    manager.undo_it()
    assert not cmds.objExists("PendingLayer")
    manager.redo_it()
    assert cmds.objExists("PendingLayer")


def test_failure_on_one_source_keeps_every_channel_unchanged(maya_cmds):
    cmds = maya_cmds
    driver = _animated_driver(cmds, attributes=("tx",))
    locked = cmds.createNode("transform", name="lockedDriver")
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".tx", target + ".tx")
    cmds.connectAttr(locked + ".ty", target + ".ty")
    cmds.lockNode(locked, lock=True)
    original_x = _source(target + ".tx")
    original_y = _source(target + ".ty")
    curves = set(cmds.ls(type="animCurve") or [])
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        5,
        attributes=["tx", "ty"],
        include_static=True,
    )

    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert _source(target + ".tx") == original_x
    assert _source(target + ".ty") == original_y
    assert set(cmds.ls(type="animCurve") or []) == curves
    assert not manager.can_undo


def test_later_verification_failure_rolls_back_every_channel(
    maya_cmds, monkeypatch
):
    cmds = maya_cmds
    driver = _animated_driver(cmds)
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".translate", target + ".translate")
    original_sample = _keyframe_bake._sample
    calls = 0

    def fail_on_second_verification(*args, **kwargs):
        nonlocal calls
        calls += 1
        result = original_sample(*args, **kwargs)
        if calls == 4:
            return tuple((frame, value + 1) for frame, value in result)
        return result

    monkeypatch.setattr(_keyframe_bake, "_sample", fail_on_second_verification)
    curves = set(cmds.ls(type="animCurve") or [])
    manager = bdu.ModifierManager()
    _node(target, manager).keyframes.bake(
        1,
        5,
        attributes=["tx", "ty"],
        include_static=True,
    )

    with pytest.raises(RuntimeError, match="Cannot preserve baked value"):
        manager.do_it_dg()
    assert _source(target + ".translate") == driver + ".translate"
    assert _source(target + ".tx") is None
    assert _source(target + ".ty") is None
    assert set(cmds.ls(type="animCurve") or []) == curves
    assert not manager.can_undo


def test_pending_created_node_can_resolve_attributes_when_executed(maya_cmds):
    cmds = maya_cmds
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).create.multiplyDivide(
        name="pendingTarget"
    )
    node.keyframes.bake(2, 2, attributes=["input1X"], include_static=True)
    manager.do_it_dg()

    assert cmds.objExists("pendingTarget")
    source = _source("pendingTarget.input1X")
    curve = source.split(".")[0]
    assert cmds.nodeType(curve) == "animCurveTU"
    assert cmds.keyframe(curve, query=True, timeChange=True) == [2]


@pytest.mark.parametrize(
    "args,kwargs,error",
    [
        ((), {"attributes": "tx"}, TypeError),
        ((), {"attributes": [""]}, ValueError),
        ((), {"attributes": [1]}, ValueError),
        ((), {"include_channel_box": 1}, TypeError),
        ((), {"include_static": 1}, TypeError),
        ((5, 1), {}, ValueError),
        ((1, 5), {"sample_by": 0}, ValueError),
    ],
)
def test_invalid_arguments_do_not_queue_changes(
    maya_cmds, args, kwargs, error
):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    with pytest.raises(error):
        _node(target, manager).keyframes.bake(*args, **kwargs)
    assert not manager.can_undo
