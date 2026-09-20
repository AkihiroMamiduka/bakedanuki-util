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


def _object(name):
    selection = om.MSelectionList()
    selection.add(name)
    return selection.getDependNode(0)


def _source(name):
    sources = _plug(name).connectedTo(True, False)
    return None if not sources else sources[0].name()


def _animated_transform(cmds, name="driver"):
    node = cmds.createNode("transform", name=name)
    cmds.setKeyframe(node + ".tx", time=1, value=2)
    cmds.setKeyframe(node + ".tx", time=3, value=6)
    return node


def test_bake_multiple_nodes_with_one_history(maya_cmds):
    cmds = maya_cmds
    driver = _animated_transform(cmds)
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.connectAttr(driver + ".tx", first + ".tx")
    cmds.connectAttr(driver + ".tx", second + ".tx")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)

    assert (
        nodes.keyframes.bake(
            [nodes.existing(first), second],
            1,
            3,
            attributes=["tx"],
        )
        is None
    )
    assert not manager.can_undo
    manager.do_it_dg()

    for node in (first, second):
        source = _source(node + ".tx")
        assert cmds.nodeType(source.split(".")[0]) == "animCurveTL"
        assert cmds.keyframe(
            source.split(".")[0], query=True, timeChange=True
        ) == [1, 2, 3]
    manager.undo_it()
    assert _source(first + ".tx") == driver + ".translateX"
    assert _source(second + ".tx") == driver + ".translateX"
    manager.redo_it()
    assert cmds.nodeType(_source(first + ".tx").split(".")[0]) == (
        "animCurveTL"
    )


def test_explicit_attribute_union_skips_missing_per_node(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.addAttr(first, longName="firstValue", attributeType="double")
    cmds.addAttr(second, longName="secondValue", attributeType="double")
    cmds.setAttr(first + ".firstValue", 2.5)
    cmds.setAttr(second + ".secondValue", 7.5)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake(
        [first, second],
        4,
        4,
        attributes=["firstValue", "secondValue"],
    )
    manager.do_it_dg()

    assert cmds.getAttr(first + ".firstValue", time=4) == 2.5
    assert cmds.getAttr(second + ".secondValue", time=4) == 7.5
    assert (
        cmds.nodeType(_source(first + ".firstValue").split(".")[0])
        == "animCurveTU"
    )
    assert (
        cmds.nodeType(_source(second + ".secondValue").split(".")[0])
        == "animCurveTU"
    )


def test_attribute_missing_from_every_node_rejects_entire_edit(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake(
        [first, second],
        1,
        3,
        attributes=["tx", "transalte"],
    )

    with pytest.raises(ValueError, match="transalte"):
        manager.do_it_dg()
    assert _source(first + ".tx") is None
    assert _source(second + ".tx") is None
    assert not manager.can_undo


def test_existing_unsupported_or_locked_explicit_attribute_fails(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.setAttr(second + ".tx", lock=True)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([first, second], 1, 3, attributes=["tx"])
    with pytest.raises(RuntimeError, match="locked"):
        manager.do_it_dg()
    assert _source(first + ".tx") is None
    assert not manager.can_undo

    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([first, second], 1, 3, attributes=["message"])
    with pytest.raises(TypeError, match="Unsupported"):
        manager.do_it_dg()
    assert not manager.can_undo


def test_automatic_collection_skips_nodes_without_targets(maya_cmds):
    cmds = maya_cmds
    empty = cmds.createNode("network", name="empty")
    target = cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([empty, target], 2, 2)
    manager.do_it_dg()

    assert cmds.nodeType(_source(target + ".tx").split(".")[0]) == (
        "animCurveTL"
    )

    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([empty], 2, 2)
    with pytest.raises(ValueError, match="No supported"):
        manager.do_it_dg()
    assert not manager.can_undo


def test_every_node_is_sampled_before_connections_change(
    maya_cmds, monkeypatch
):
    cmds = maya_cmds
    driver = _animated_transform(cmds)
    middle = cmds.createNode("transform", name="middle")
    target = cmds.createNode("transform", name="target")
    cmds.connectAttr(driver + ".tx", middle + ".tx")
    cmds.connectAttr(middle + ".tx", target + ".tx")
    original_sample = _keyframe_bake._sample
    calls = 0

    def inspect_sample(*args, **kwargs):
        nonlocal calls
        if calls < 2:
            assert cmds.isConnected(driver + ".tx", middle + ".tx")
            assert cmds.isConnected(middle + ".tx", target + ".tx")
        calls += 1
        return original_sample(*args, **kwargs)

    monkeypatch.setattr(_keyframe_bake, "_sample", inspect_sample)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake(
        [target, middle], 1, 3, attributes=["tx"], sample_by=2
    )
    manager.do_it_dg()

    assert calls == 4
    assert cmds.nodeType(_source(middle + ".tx").split(".")[0]) == (
        "animCurveTL"
    )
    assert cmds.nodeType(_source(target + ".tx").split(".")[0]) == (
        "animCurveTL"
    )


def test_later_verification_failure_rolls_back_every_node(
    maya_cmds, monkeypatch
):
    cmds = maya_cmds
    driver = _animated_transform(cmds)
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    cmds.connectAttr(driver + ".tx", first + ".tx")
    cmds.connectAttr(driver + ".tx", second + ".tx")
    original_sample = _keyframe_bake._sample
    calls = 0

    def fail_later(*args, **kwargs):
        nonlocal calls
        calls += 1
        result = original_sample(*args, **kwargs)
        if calls == 4:
            return tuple((frame, value + 1) for frame, value in result)
        return result

    monkeypatch.setattr(_keyframe_bake, "_sample", fail_later)
    curves = set(cmds.ls(type="animCurve") or [])
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([first, second], 1, 3, attributes=["tx"], sample_by=2)

    with pytest.raises(RuntimeError, match="Cannot preserve baked value"):
        manager.do_it_dg()
    assert _source(first + ".tx") == driver + ".translateX"
    assert _source(second + ".tx") == driver + ".translateX"
    assert set(cmds.ls(type="animCurve") or []) == curves
    assert not manager.can_undo


def test_one_layer_is_applied_to_every_node(maya_cmds):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    layer = cmds.animLayer("Correction")
    for node in (first, second):
        cmds.animLayer(layer, edit=True, attribute=node + ".tx")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.anim_layer(layer).bake(
        [first, second], 1, 3, attributes=["tx"]
    )
    manager.do_it_dg()

    for node in (first, second):
        curves = cmds.animLayer(
            layer, query=True, findCurveForPlug=node + ".tx"
        )
        assert curves
        assert cmds.keyframe(curves[0], query=True, timeChange=True) == [
            1,
            2,
            3,
        ]


def test_explicit_layer_membership_failure_keeps_every_node_unchanged(
    maya_cmds,
):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    layer = cmds.animLayer("Correction")
    cmds.animLayer(layer, edit=True, attribute=first + ".tx")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.anim_layer(layer).bake(
        [first, second], 1, 3, attributes=["tx"]
    )

    with pytest.raises(RuntimeError, match="not a member"):
        manager.do_it_dg()
    assert (
        cmds.animLayer(layer, query=True, findCurveForPlug=first + ".tx")
        is None
    )
    assert not manager.can_undo


def test_pending_nodes_and_layer_share_one_history(maya_cmds):
    cmds = maya_cmds
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    first = nodes.create.multiplyDivide(name="first")
    second = nodes.create.multiplyDivide(name="second")
    layer = nodes.create.animLayer(name="PendingLayer")
    layer.add_plugs([first.input1X, second.input1X])
    nodes.keyframes.anim_layer(layer).bake(
        [first, second], 2, 2, attributes=["input1X"]
    )
    manager.do_it_dg()

    for node in ("first", "second"):
        curves = cmds.animLayer(
            "PendingLayer", query=True, findCurveForPlug=node + ".input1X"
        )
        assert curves
        assert cmds.keyframe(curves[0], query=True, timeChange=True) == [2]
    manager.undo_it()
    assert not cmds.objExists("first")
    assert not cmds.objExists("second")
    assert not cmds.objExists("PendingLayer")


def test_total_sample_limit_counts_every_target(maya_cmds, monkeypatch):
    cmds = maya_cmds
    first = cmds.createNode("transform", name="first")
    second = cmds.createNode("transform", name="second")
    monkeypatch.setattr(_keyframe_bake, "_MAX_SAMPLES", 3)
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    nodes.keyframes.bake([first, second], 1, 2, attributes=["tx"])

    with pytest.raises(ValueError, match="total sample points"):
        manager.do_it_dg()
    assert _source(first + ".tx") is None
    assert _source(second + ".tx") is None
    assert not manager.can_undo


@pytest.mark.parametrize(
    "value,error",
    [
        ([], ValueError),
        ("target", TypeError),
        (123, TypeError),
    ],
)
def test_invalid_node_collection_does_not_queue(maya_cmds, value, error):
    maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(error):
        nodes.keyframes.bake(value, 1, 2)
    assert not manager.can_undo


def test_duplicate_nodes_are_rejected_by_identity(maya_cmds):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(ValueError, match="Duplicate"):
        nodes.keyframes.bake(
            [target, _object(target), nodes.existing(target)], 1, 2
        )
    assert not manager.can_undo


@pytest.mark.parametrize(
    "kwargs,error",
    [
        ({"attributes": "tx"}, TypeError),
        ({"attributes": [""]}, ValueError),
        ({"attributes": [1]}, ValueError),
        ({"include_channel_box": 1}, TypeError),
        ({"include_static": 1}, TypeError),
        ({"sample_by": 0}, ValueError),
    ],
)
def test_invalid_bake_arguments_do_not_queue(maya_cmds, kwargs, error):
    target = maya_cmds.createNode("transform", name="target")
    manager = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=manager)
    with pytest.raises(error):
        nodes.keyframes.bake([target], 1, 2, **kwargs)
    assert not manager.can_undo
