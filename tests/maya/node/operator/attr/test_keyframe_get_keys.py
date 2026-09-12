# coding: utf-8
from __future__ import annotations

import pytest
from maya.api import OpenMaya as om

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager

pytestmark = pytest.mark.maya


@pytest.fixture(autouse=True)
def restore_units(new_scene, maya_cmds):
    units = {
        flag: maya_cmds.currentUnit(query=True, **{flag: True})
        for flag in ("linear", "angle", "time")
    }
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    yield
    maya_cmds.currentUnit(**units)


def _new_keyframe(maya_cmds, attribute_type="double", *, manager=None):
    node = maya_cmds.createNode("transform", name="getKeysTarget")
    flags = {"enumName": "A:B:C:D"} if attribute_type == "enum" else {}
    maya_cmds.addAttr(
        node,
        longName="probeValue",
        attributeType=attribute_type,
        keyable=True,
        **flags,
    )
    selection = om.MSelectionList()
    selection.add(node + ".probeValue")
    return KeyframeManager(selection.getPlug(0), modifier_manager=manager)


def _seed_keys(maya_cmds, keyframe, pairs):
    for frame, value in pairs:
        maya_cmds.setKeyframe(
            keyframe.plug.name(),
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )


def _assert_pairs(actual, expected):
    assert isinstance(actual, list)
    assert len(actual) == len(expected)
    for pair, expected_pair in zip(actual, expected):
        assert isinstance(pair, tuple)
        assert len(pair) == 2
        assert all(type(value) is float for value in pair)
        assert pair == pytest.approx(expected_pair)


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (None, None, [(-3.0, 30.0), (1.0, 10.0), (4.5, 45.0), (9.0, 90.0)]),
        (1.0, 9.0, [(1.0, 10.0), (4.5, 45.0), (9.0, 90.0)]),
        (2.0, 8.0, [(4.5, 45.0)]),
        (None, 1.0, [(-3.0, 30.0), (1.0, 10.0)]),
        (4.5, None, [(4.5, 45.0), (9.0, 90.0)]),
        (4.5, 4.5, [(4.5, 45.0)]),
        (5.0, 5.0, []),
        (10.0, None, []),
        (None, -4.0, []),
    ],
)
def test_get_keys_returns_only_existing_keys_in_inclusive_range(
    maya_cmds, start, end, expected
):
    keyframe = _new_keyframe(maya_cmds)
    _seed_keys(
        maya_cmds,
        keyframe,
        [(9.0, 90.0), (1.0, 10.0), (4.5, 45.0), (-3.0, 30.0)],
    )

    _assert_pairs(keyframe.get_keys(start, end), expected)


@pytest.mark.parametrize("curve_state", ["absent", "empty"])
def test_get_keys_returns_empty_without_time_input_keys(
    maya_cmds, curve_state
):
    keyframe = _new_keyframe(maya_cmds)
    if curve_state != "absent":
        curve = maya_cmds.createNode("animCurveTU")
        maya_cmds.connectAttr(curve + ".output", keyframe.plug.name())

    assert keyframe.get_keys() == []
    assert keyframe.get_keys(start_frame=1.0, end_frame=9.0) == []


@pytest.mark.parametrize("has_curve", [False, True])
@pytest.mark.parametrize(
    "start,end",
    [
        (9.0, 1.0),
        (float("nan"), None),
        (None, float("nan")),
        (float("inf"), None),
        (None, float("inf")),
        (float("-inf"), None),
        (None, float("-inf")),
    ],
)
def test_get_keys_rejects_invalid_ranges_even_without_a_curve(
    maya_cmds, has_curve, start, end
):
    keyframe = _new_keyframe(maya_cmds)
    if has_curve:
        _seed_keys(maya_cmds, keyframe, [(1.0, 10.0)])

    with pytest.raises(ValueError):
        keyframe.get_keys(start_frame=start, end_frame=end)


@pytest.mark.parametrize("changed_units", [False, True])
@pytest.mark.parametrize(
    "attribute_type,values",
    [
        ("double", [1.25, -2.5, 3.75]),
        ("long", [1.0, 3.0, 2.0]),
        ("doubleAngle", [45.0, 90.0, 180.0]),
        ("doubleLinear", [10.0, 25.0, 50.0]),
        ("time", [6.0, 12.0, 18.0]),
        ("bool", [0.0, 1.0, 0.0]),
        ("enum", [0.0, 2.0, 1.0]),
    ],
)
def test_get_keys_returns_public_units_and_roundtrips_through_set_keys(
    maya_cmds, attribute_type, values, changed_units
):
    source = _new_keyframe(maya_cmds, attribute_type)
    frames = [1.0, 4.5, 9.0]
    _seed_keys(maya_cmds, source, zip(frames, values))
    if changed_units:
        maya_cmds.currentUnit(linear="m", angle="rad", time="ntsc")
    frame_scale = 1.25 if changed_units else 1.0
    value_scale = frame_scale if attribute_type == "time" else 1.0
    expected = [
        (frame * frame_scale, value * value_scale)
        for frame, value in zip(frames, values)
    ]

    pairs = source.get_keys()
    _assert_pairs(pairs, expected)
    _assert_pairs(
        source.get_keys(expected[1][0], expected[2][0]), expected[1:]
    )
    mod = bdu.ModifierManager()
    destination = _new_keyframe(maya_cmds, attribute_type, manager=mod)
    destination.set_keys(pairs)
    assert destination.get_keys() == []
    mod.do_it_dg()
    _assert_pairs(destination.get_keys(), expected)
    for _ in range(2):
        mod.undo_it()
        assert destination.get_keys() == []
        mod.redo_it()
        _assert_pairs(destination.get_keys(), expected)


def test_get_keys_does_not_flush_pending_edits_and_returns_a_snapshot(
    maya_cmds,
):
    mod = bdu.ModifierManager()
    keyframe = _new_keyframe(maya_cmds, manager=mod)
    _seed_keys(maya_cmds, keyframe, [(1.0, 10.0)])
    snapshot = keyframe.get_keys()
    keyframe.set_key(20.0, 2.0)
    pending_modifier = mod.dg_mod

    assert keyframe.get_keys() == [(1.0, 10.0)]
    assert mod.dg_mod is pending_modifier
    assert not mod.can_undo
    mod.do_it_dg()
    assert keyframe.get_keys() == [(1.0, 10.0), (2.0, 20.0)]
    assert snapshot == [(1.0, 10.0)]
    snapshot[0] = (99.0, 99.0)
    snapshot.append((100.0, 100.0))
    assert keyframe.get_keys() == [(1.0, 10.0), (2.0, 20.0)]
    mod.undo_it()
    assert keyframe.get_keys() == [(1.0, 10.0)]


@pytest.mark.parametrize(
    "source_type,values",
    [
        ("double", [0.5, 1.0]),
        ("doubleAngle", [45.0, 90.0]),
        ("doubleLinear", [10.0, 20.0]),
        ("time", [6.0, 12.0]),
    ],
)
def test_get_keys_uses_curve_units_independently_of_custom_value_reader(
    maya_cmds, source_type, values
):
    source = _new_keyframe(maya_cmds, source_type)
    _seed_keys(maya_cmds, source, zip([1.0, 11.0], values))
    expected = list(zip([1.0, 11.0], values))

    _assert_pairs(source.get_keys(), expected)

    def reject_plug_value_reader(value):
        raise AssertionError("get_keys must convert by the curve type")

    standalone = KeyframeManager(
        source.plug, value_reader=reject_plug_value_reader
    )
    _assert_pairs(standalone.get_keys(), expected)


def test_get_keys_excludes_constraint_driver_keys(
    maya_cmds,
):
    driver = maya_cmds.createNode("transform", name="getKeysDriver")
    target = maya_cmds.createNode("transform", name="constrainedGetKeysTarget")
    maya_cmds.setAttr(target + ".translateX", 5.0)
    maya_cmds.pointConstraint(driver, target, maintainOffset=True)
    for frame, value in [(1.0, 0.0), (11.0, 10.0)]:
        maya_cmds.setKeyframe(
            driver + ".translateX",
            time=frame,
            value=value,
            inTangentType="linear",
            outTangentType="linear",
        )
    keyframe = bdu.Nodes().existing(target).translateX.keyframe

    assert keyframe.get_keys() == []
    assert keyframe.get_keys(2.0, 10.0) == []
    assert [
        maya_cmds.getAttr(target + ".translateX", time=frame)
        for frame in (1.0, 6.0, 11.0)
    ] == pytest.approx([5.0, 10.0, 15.0])
