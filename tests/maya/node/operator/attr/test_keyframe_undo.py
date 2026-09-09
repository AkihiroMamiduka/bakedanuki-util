# coding: utf-8
from __future__ import annotations

import pytest

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager
from bd_util.maya.node.operator.attr.extra.add_attr import AddAttr
from bd_util.maya.node.operator.node.dag.transform._core import Transform

pytestmark = pytest.mark.maya


class KeyframeTransform(Transform):
    __slots__ = ()

    angleValue = AddAttr.at.double_angle(default_value=0.0)
    floatAngleValue = AddAttr.at.float_angle(default_value=0.0)
    distanceValue = AddAttr.at.double_linear(default_value=0.0)
    floatDistanceValue = AddAttr.at.float_linear(default_value=0.0)
    timeValue = AddAttr.at.time(default_value=0.0)


@pytest.fixture(autouse=True)
def restore_units(maya_cmds):
    units = {
        flag: maya_cmds.currentUnit(query=True, **{flag: True})
        for flag in ("linear", "angle", "time")
    }
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    yield
    maya_cmds.currentUnit(**units)


def test_set_waits_for_execution_and_queries_follow_undo_redo(
    new_scene,
    maya_cmds,
):
    name = maya_cmds.createNode("plusMinusAverage", name="existing")
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing(name).input1D[0].keyframe
    )
    maya_cmds.flushUndo()

    assert keyframe.set(2.5, frame=1) is None
    keyframe.set(7.5, frame=2)
    assert keyframe.frames() == []
    assert not mod.can_undo
    mod.do_it_dg()

    assert keyframe.frames() == [1.0, 2.0]
    assert keyframe.values() == pytest.approx([2.5, 7.5])
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        assert not keyframe.has_anim_curve()
        assert keyframe.key_count() == 0
        assert keyframe.values() == []
        assert not maya_cmds.ls(type="animCurve")
        mod.redo_it()
        assert keyframe.frames() == [1.0, 2.0]
        assert keyframe.values() == pytest.approx([2.5, 7.5])


def test_set_on_pending_node_and_rename_undo_together(new_scene, maya_cmds):
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = nodes.create.plusMinusAverage(name="beforeRename")
    keyframe = node.input1D[0].keyframe
    mod.dg_mod.renameNode(keyframe.plug.node(), "afterRename")
    keyframe.set(4.0, frame=8)
    mod.do_it_dg()

    assert maya_cmds.getAttr("afterRename.input1D[0]", time=8) == 4.0
    mod.undo_it()
    assert not maya_cmds.objExists("afterRename")
    assert not maya_cmds.ls(type="animCurve")
    mod.redo_it()
    assert maya_cmds.getAttr("afterRename.input1D[0]", time=8) == 4.0


def test_overwriting_key_restores_value_and_tangents(new_scene, maya_cmds):
    name = maya_cmds.createNode("transform")
    plug_name = name + ".translateX"
    maya_cmds.setKeyframe(
        plug_name,
        time=1,
        value=3,
        inTangentType="linear",
        outTangentType="flat",
    )
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod)
        .existing(name)
        .translate.translateX.keyframe
    )
    keyframe.set(9, frame=1, in_tangent_type="flat", out_tangent_type="linear")
    mod.do_it_dg()
    assert keyframe.values() == [9.0]
    assert maya_cmds.keyTangent(plug_name, query=True, inTangentType=True) == [
        "linear"
    ]
    mod.undo_it()
    assert keyframe.values() == [3.0]
    assert maya_cmds.keyTangent(plug_name, query=True, inTangentType=True) == [
        "linear"
    ]
    assert maya_cmds.keyTangent(
        plug_name, query=True, outTangentType=True
    ) == ["flat"]
    mod.redo_it()
    assert keyframe.values() == [9.0]
    assert maya_cmds.keyTangent(plug_name, query=True, inTangentType=True) == [
        "linear"
    ]
    assert maya_cmds.keyTangent(
        plug_name, query=True, outTangentType=True
    ) == ["flat"]


@pytest.mark.parametrize(
    "attribute",
    [
        "angleValue",
        "floatAngleValue",
        "distanceValue",
        "floatDistanceValue",
        "timeValue",
    ],
)
@pytest.mark.parametrize("change_units_after_queue", [False, True])
def test_keyframe_units_match_set_and_survive_pending_unit_changes(
    new_scene,
    maya_cmds,
    attribute,
    change_units_after_queue,
):
    mod = bdu.ModifierManager()
    node = KeyframeTransform.create(mod, name="unitTarget")
    mod.do_it_dag()
    mod.do_it_dg()
    plug = getattr(node, attribute)
    maya_cmds.currentUnit(linear="m", angle="rad", time="film")
    plug.set(12.0)
    mod.do_it_dg()
    assert plug.get() == pytest.approx(12.0)
    mod.clear()

    plug.keyframe.set(12.0, frame=12)
    if change_units_after_queue:
        maya_cmds.currentUnit(linear="mm", angle="deg", time="ntsc")
    expected_frame = 15.0 if change_units_after_queue else 12.0
    expected_value = expected_frame if attribute == "timeValue" else 12.0
    mod.do_it_dg()
    maya_cmds.currentTime(expected_frame)

    assert plug.keyframe.frames() == pytest.approx([expected_frame])
    assert plug.keyframe.values() == pytest.approx([expected_value])
    assert plug.get() == pytest.approx(expected_value)
    mod.undo_it()
    assert not plug.keyframe.has_anim_curve()
    assert plug.get() == pytest.approx(expected_value)
    mod.redo_it()
    assert plug.keyframe.values() == pytest.approx([expected_value])


def test_keyframe_on_pending_extra_attribute(new_scene, maya_cmds):
    mod = bdu.ModifierManager()
    node = KeyframeTransform.create(mod, name="extraTarget")
    mod.do_it_dag()
    node.angleValue.keyframe.set(90.0, frame=1)
    mod.do_it_dg()
    assert node.angleValue.keyframe.values() == pytest.approx([90.0])
    mod.undo_it()
    assert not maya_cmds.objExists("extraTarget")
    assert not maya_cmds.ls(type="animCurve")
    mod.redo_it()
    assert node.angleValue.keyframe.values() == pytest.approx([90.0])


@pytest.mark.parametrize(
    "value,frame,tangent",
    [
        (float("nan"), 1.0, None),
        (1.0, float("inf"), None),
        (1.0, 1.0, "invalid"),
    ],
)
def test_invalid_arguments_do_not_queue_or_create_curve(
    plus_minus_average_node,
    maya_cmds,
    value,
    frame,
    tangent,
):
    node = plus_minus_average_node
    mod = node.modifier_manager
    mod.clear()
    with pytest.raises(ValueError):
        node.input1D[0].keyframe.set(value, frame, in_tangent_type=tangent)
    mod.do_it_dg()
    assert not maya_cmds.ls(type="animCurve")


def test_standalone_manager_requires_explicit_modifier(
    plus_minus_average_node,
):
    keyframe = KeyframeManager(plus_minus_average_node.input1D[0].plug)
    with pytest.raises(RuntimeError, match="requires a ModifierManager"):
        keyframe.set(1, frame=1)


def test_zero_keys_failure_restores_earlier_queued_key(new_scene, maya_cmds):
    name = maya_cmds.createNode("transform")
    maya_cmds.setAttr(name + ".translateY", lock=True)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(name)
    node.translate.translateX.keyframe.set(2, frame=1)
    node.translate.translateY.keyframe.set(3, frame=1)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert not maya_cmds.ls(type="animCurve")
    assert not mod.can_undo
    assert not mod.can_redo
    node.translate.translateX.keyframe.set(4, frame=2)
    mod.do_it_dg()
    assert node.translate.translateX.keyframe.frames() == [2.0]


def test_queries_follow_reconnected_curve(new_scene, maya_cmds):
    first = maya_cmds.createNode("transform", name="first")
    second = maya_cmds.createNode("transform", name="second")
    maya_cmds.setKeyframe(first + ".translateX", time=1, value=2)
    maya_cmds.setKeyframe(second + ".translateX", time=3, value=4)
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod)
        .existing(first)
        .translate.translateX.keyframe
    )
    assert keyframe.values() == [2.0]
    source = maya_cmds.listConnections(second + ".translateX", plugs=True)[0]
    maya_cmds.connectAttr(source, first + ".translateX", force=True)
    assert keyframe.frames() == [3.0]
    assert keyframe.values() == [4.0]
