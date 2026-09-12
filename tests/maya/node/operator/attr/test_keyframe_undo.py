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

    assert keyframe.set_key(2.5, frame=1) is None
    keyframe.set_key(7.5, frame=2)
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
    keyframe.set_key(4.0, frame=8)
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
    keyframe.set_key(
        9, frame=1, in_tangent_type="flat", out_tangent_type="linear"
    )
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

    plug.keyframe.set_key(12.0, frame=12)
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
    node.angleValue.keyframe.set_key(90.0, frame=1)
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
        node.input1D[0].keyframe.set_key(value, frame, in_tangent_type=tangent)
    mod.do_it_dg()
    assert not maya_cmds.ls(type="animCurve")


@pytest.mark.parametrize(
    "method,args",
    [
        ("set_key", (1, 1)),
        ("insert_key", (1,)),
        ("set_tangent", (1,)),
        ("delete_key", (1,)),
        ("delete_keys", ()),
        ("delete_anim_curve", ()),
    ],
)
def test_standalone_manager_requires_explicit_modifier(
    plus_minus_average_node,
    method,
    args,
):
    keyframe = KeyframeManager(plus_minus_average_node.input1D[0].plug)
    with pytest.raises(RuntimeError, match="requires a ModifierManager"):
        getattr(keyframe, method)(*args)


def test_zero_keys_failure_restores_earlier_queued_key(new_scene, maya_cmds):
    name = maya_cmds.createNode("transform")
    maya_cmds.setAttr(name + ".translateY", lock=True)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(name)
    node.translate.translateX.keyframe.set_key(2, frame=1)
    node.translate.translateY.keyframe.set_key(3, frame=1)
    with pytest.raises(RuntimeError):
        mod.do_it_dg()
    assert not maya_cmds.ls(type="animCurve")
    assert not mod.can_undo
    assert not mod.can_redo
    node.translate.translateX.keyframe.set_key(4, frame=2)
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
    maya_cmds.disconnectAttr(source, second + ".translateX")
    maya_cmds.connectAttr(source, first + ".translateX", force=True)
    assert keyframe.frames() == [3.0]
    assert keyframe.values() == [4.0]


@pytest.fixture
def existing_keyframe(new_scene, maya_cmds):
    name = maya_cmds.createNode("transform", name="keyTarget")
    for frame, value in ((1, 2), (5, 8), (9, 4)):
        maya_cmds.setKeyframe(
            name + ".translateX",
            time=frame,
            value=value,
            inTangentType="spline",
            outTangentType="spline",
        )
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod)
        .existing(name)
        .translate.translateX.keyframe
    )
    maya_cmds.flushUndo()
    return mod, keyframe


def _curve_state(maya_cmds, keyframe):
    plug_name = keyframe.plug.name()
    state = {
        "frames": keyframe.frames(),
        "values": keyframe.values(),
        "breakdowns": maya_cmds.keyframe(
            plug_name, query=True, breakdown=True
        ),
    }
    for flag in (
        "inTangentType",
        "outTangentType",
        "inAngle",
        "outAngle",
        "inWeight",
        "outWeight",
        "lock",
        "weightLock",
        "weightedTangents",
    ):
        state[flag] = maya_cmds.keyTangent(
            plug_name, query=True, **{flag: True}
        )
    return state


def _assert_curve_state(actual, expected):
    assert actual.keys() == expected.keys()
    numeric = {
        "frames",
        "values",
        "inAngle",
        "outAngle",
        "inWeight",
        "outWeight",
    }
    for field in actual:
        if field in numeric and expected[field] is not None:
            assert actual[field] == pytest.approx(expected[field]), field
        else:
            assert actual[field] == expected[field], field


@pytest.mark.parametrize(
    "method,kwargs,expected_frames",
    [
        ("insert_key", {"frame": 3, "breakdown": True}, [1.0, 3.0, 5.0, 9.0]),
        (
            "set_tangent",
            {
                "frame": 5,
                "in_tangent_type": "flat",
                "out_tangent_type": "linear",
            },
            [1.0, 5.0, 9.0],
        ),
        ("delete_key", {"frame": 5}, [1.0, 9.0]),
        ("delete_keys", {"start_frame": 1, "end_frame": 5}, [9.0]),
        ("delete_keys", {}, []),
    ],
)
def test_edits_are_deferred_and_restore_complete_curve_on_undo_redo(
    existing_keyframe, maya_cmds, method, kwargs, expected_frames
):
    mod, keyframe = existing_keyframe
    before = _curve_state(maya_cmds, keyframe)
    assert getattr(keyframe, method)(**kwargs) is None
    assert not mod.can_undo
    _assert_curve_state(_curve_state(maya_cmds, keyframe), before)
    mod.do_it_dg()
    assert keyframe.frames() == expected_frames
    assert keyframe.has_anim_curve()
    after = _curve_state(maya_cmds, keyframe)
    assert maya_cmds.undoInfo(query=True, undoQueueEmpty=True)
    for _ in range(2):
        mod.undo_it()
        _assert_curve_state(_curve_state(maya_cmds, keyframe), before)
        mod.redo_it()
        _assert_curve_state(_curve_state(maya_cmds, keyframe), after)


def test_insert_preserves_shape_and_breakdown(existing_keyframe, maya_cmds):
    mod, keyframe = existing_keyframe
    frames = [i / 4 for i in range(4, 37)]
    before = [maya_cmds.getAttr(keyframe.plug.name(), time=t) for t in frames]
    keyframe.insert_key(3, breakdown=True)
    mod.do_it_dg()
    after = [maya_cmds.getAttr(keyframe.plug.name(), time=t) for t in frames]
    assert after == pytest.approx(before)
    assert maya_cmds.keyframe(
        keyframe.plug.name(), query=True, time=(3, 3), breakdown=True
    ) == [3.0]


@pytest.mark.parametrize("method", ["delete_key", "delete_keys"])
def test_deleting_last_key_keeps_empty_curve(
    existing_keyframe, maya_cmds, method
):
    mod, keyframe = existing_keyframe
    curve = maya_cmds.listConnections(keyframe.plug.name(), source=True)[0]
    if method == "delete_key":
        for frame in keyframe.frames():
            keyframe.delete_key(frame)
    else:
        keyframe.delete_keys()
    mod.do_it_dg()
    assert keyframe.frames() == []
    assert maya_cmds.objExists(curve)
    assert keyframe.has_anim_curve()
    mod.undo_it()
    assert keyframe.frames() == [1.0, 5.0, 9.0]
    mod.redo_it()
    assert keyframe.has_anim_curve()
    assert keyframe.frames() == []


@pytest.mark.parametrize("delete_curve", [False, True])
def test_set_edit_delete_set_order_on_pending_renamed_node(
    new_scene, maya_cmds, delete_curve
):
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).create.plusMinusAverage(
        name="oldName"
    )
    keyframe = node.input1D[0].keyframe
    keyframe.set_key(1, 1)
    keyframe.set_key(9, 9)
    keyframe.insert_key(5)
    mod.dg_mod.renameNode(keyframe.plug.node(), "newName")
    keyframe.set_tangent(5, in_tangent_type="flat")
    if delete_curve:
        keyframe.delete_anim_curve()
    else:
        keyframe.delete_keys()
    keyframe.set_key(7, 3)
    mod.do_it_dg()
    assert keyframe.frames() == [3.0]
    assert keyframe.values() == [7.0]
    assert maya_cmds.objExists("newName")
    for _ in range(2):
        mod.undo_it()
        assert not maya_cmds.objExists("newName")
        assert not maya_cmds.ls(type="animCurve")
        mod.redo_it()
        assert keyframe.frames() == [3.0]
        assert keyframe.values() == [7.0]


def test_delete_anim_curve_rejects_shared_curve_without_changing_connections(
    existing_keyframe, maya_cmds
):
    mod, keyframe = existing_keyframe
    second = maya_cmds.createNode("transform", name="sharedTarget")
    output = maya_cmds.listConnections(keyframe.plug.name(), plugs=True)[0]
    curve = output.split(".")[0]
    before = _curve_state(maya_cmds, keyframe)
    maya_cmds.connectAttr(output, second + ".translateX")
    keyframe.delete_anim_curve()
    assert maya_cmds.objExists(curve)
    with pytest.raises(RuntimeError, match="unshared"):
        mod.do_it_dg()
    assert maya_cmds.objExists(curve)
    assert maya_cmds.isConnected(output, keyframe.plug.name())
    assert maya_cmds.isConnected(output, second + ".translateX")
    maya_cmds.disconnectAttr(output, second + ".translateX")
    _assert_curve_state(_curve_state(maya_cmds, keyframe), before)


@pytest.mark.parametrize(
    "method,kwargs,expected_frames",
    [
        ("insert_key", {"frame": 3}, [1.25, 3.75, 6.25, 11.25]),
        (
            "set_tangent",
            {"frame": 5, "in_tangent_type": "flat"},
            [1.25, 6.25, 11.25],
        ),
        ("delete_key", {"frame": 5}, [1.25, 11.25]),
        ("delete_keys", {"start_frame": 1, "end_frame": 5}, [11.25]),
        ("delete_keys", {"end_frame": 5}, [11.25]),
        ("delete_keys", {"start_frame": 5}, [1.25]),
    ],
)
def test_edits_capture_time_units_when_queued(
    existing_keyframe, maya_cmds, method, kwargs, expected_frames
):
    mod, keyframe = existing_keyframe
    getattr(keyframe, method)(**kwargs)
    maya_cmds.currentUnit(time="ntsc")
    mod.do_it_dg()
    assert keyframe.frames() == pytest.approx(expected_frames)
    if method == "set_tangent":
        assert maya_cmds.keyTangent(
            keyframe.plug.name(),
            query=True,
            time=(6.25, 6.25),
            inTangentType=True,
        ) == ["flat"]
    mod.undo_it()
    assert keyframe.frames() == pytest.approx([1.25, 6.25, 11.25])
    mod.redo_it()
    assert keyframe.frames() == pytest.approx(expected_frames)


@pytest.mark.parametrize(
    "method,kwargs",
    [
        ("insert_key", {"frame": float("nan")}),
        ("set_tangent", {"frame": float("inf")}),
        (
            "set_tangent",
            {
                "frame": 5,
                "in_tangent_type": "flat",
                "out_tangent_type": "invalid",
            },
        ),
        ("delete_key", {"frame": float("-inf")}),
        ("delete_keys", {"start_frame": float("nan")}),
        ("delete_keys", {"end_frame": float("inf")}),
        ("delete_keys", {"start_frame": 9, "end_frame": 1}),
    ],
)
def test_invalid_edits_do_not_queue_partial_changes(
    existing_keyframe, maya_cmds, method, kwargs
):
    mod, keyframe = existing_keyframe
    before = _curve_state(maya_cmds, keyframe)
    with pytest.raises(ValueError):
        getattr(keyframe, method)(**kwargs)
    mod.do_it_dg()
    _assert_curve_state(_curve_state(maya_cmds, keyframe), before)


@pytest.mark.parametrize("delete_curve", [False, True])
def test_failed_insert_rolls_back_previous_edits_in_flush(
    existing_keyframe, maya_cmds, delete_curve
):
    mod, keyframe = existing_keyframe
    before = _curve_state(maya_cmds, keyframe)
    second = maya_cmds.createNode("transform")
    missing = (
        bdu.Nodes(modifier_manager=mod)
        .existing(second)
        .translate.translateX.keyframe
    )
    keyframe.set_key(12, 12)
    keyframe.delete_key(5)
    if delete_curve:
        keyframe.delete_anim_curve()
    missing.insert_key(3)
    with pytest.raises(RuntimeError, match="no channel animCurve"):
        mod.do_it_dg()
    _assert_curve_state(_curve_state(maya_cmds, keyframe), before)
    assert not mod.can_undo
    assert not mod.can_redo
    keyframe.insert_key(3)
    mod.do_it_dg()
    assert keyframe.frames() == [1.0, 3.0, 5.0, 9.0]


def test_delete_range_includes_negative_fractional_endpoints(
    new_scene, maya_cmds
):
    name = maya_cmds.createNode("plusMinusAverage")
    for frame in (-2.5, -1.25, 0.125, 1.5):
        maya_cmds.setKeyframe(name + ".input1D[0]", time=frame, value=frame)
    mod = bdu.ModifierManager()
    keyframe = (
        bdu.Nodes(modifier_manager=mod).existing(name).input1D[0].keyframe
    )
    keyframe.delete_keys(start_frame=-1.25, end_frame=0.125)
    maya_cmds.currentUnit(time="ntsc")
    mod.do_it_dg()
    assert keyframe.frames() == pytest.approx([-3.125, 1.875])
    mod.undo_it()
    assert keyframe.frames() == pytest.approx(
        [-3.125, -1.5625, 0.15625, 1.875]
    )
    mod.redo_it()
    assert keyframe.frames() == pytest.approx([-3.125, 1.875])
