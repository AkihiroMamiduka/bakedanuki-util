# coding: utf-8
from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager

from test_keyframe_set_equivalence import (
    _assert_curve_state,
    _curve_state,
    _existing_curve,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _new_keyframe(maya_cmds, attribute_type="double"):
    node = maya_cmds.createNode("transform", name="bulkTarget")
    maya_cmds.addAttr(
        node, longName="probeValue", attributeType=attribute_type, keyable=True
    )
    selection = om.MSelectionList()
    selection.add(node + ".probeValue")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(selection.getPlug(0), modifier_manager=mod)
    return mod, keyframe


@pytest.mark.parametrize(
    "attribute_type",
    ["double", "long", "doubleAngle", "doubleLinear", "bool", "enum", "time"],
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("explicit_tangents", [False, True])
def test_set_keys_matches_sequential_set_key_with_unsorted_duplicate_inputs(
    maya_cmds, attribute_type, weighted, explicit_tangents
):
    maya_cmds.keyTangent(
        g=True,
        inTangentType="spline",
        outTangentType="spline",
        weightedTangents=weighted,
    )
    reference_plug, reference_curve = _existing_curve(
        maya_cmds, "referenceTarget", attribute_type
    )
    actual_plug, actual_curve = _existing_curve(
        maya_cmds, "managedTarget", attribute_type
    )
    before = _curve_state(actual_curve)
    _assert_curve_state(before, _curve_state(reference_curve))
    reference_mod = bdu.ModifierManager()
    reference = KeyframeManager(reference_plug, modifier_manager=reference_mod)
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(actual_plug, modifier_manager=mod)
    frames = [9.0, 3.0, 5.0, 5.0, 1.0, 12.0, -2.0, 9.0]
    values = [1.0, 2.0, 0.5, 2.5, 0.0, 1.5, 2.0, 3.0]
    in_type = "flat" if explicit_tangents else None
    out_type = "linear" if explicit_tangents else None

    assert (
        keyframe.set_keys(
            values,
            frames=frames,
            in_tangent_type=in_type,
            out_tangent_type=out_type,
        )
        is None
    )
    for frame, value in zip(frames, values):
        reference.set_key(value, frame, in_type, out_type)
    _assert_curve_state(_curve_state(actual_curve), before)
    maya_cmds.keyTangent(
        g=True,
        inTangentType="linear",
        outTangentType="flat",
        weightedTangents=not weighted,
    )
    reference_mod.do_it_dg()
    mod.do_it_dg()
    expected = _curve_state(reference_curve)
    _assert_curve_state(_curve_state(actual_curve), expected)
    assert keyframe.frames() == [-2.0, 1.0, 3.0, 5.0, 9.0, 12.0]
    for _ in range(2):
        mod.undo_it()
        _assert_curve_state(_curve_state(actual_curve), before)
        mod.redo_it()
        _assert_curve_state(_curve_state(actual_curve), expected)


@pytest.mark.parametrize("use_generator", [False, True])
def test_set_keys_snapshots_inputs_and_creates_curve_only_on_execution(
    maya_cmds, use_generator
):
    mod, keyframe = _new_keyframe(maya_cmds)
    values = [9.0, 2.0, 7.0]
    frames = [3.0, 1.0, 3.0]
    consumed = []

    def generate(label, items):
        for item in items:
            consumed.append((label, item))
            yield item

    value_input = generate("values", values) if use_generator else values
    frame_input = generate("frames", frames) if use_generator else frames
    keyframe.set_keys(value_input, frames=frame_input)
    if use_generator:
        assert len(consumed) == 6
    values[:] = [100.0]
    frames[:] = [100.0]
    assert not keyframe.has_anim_curve()
    assert not mod.can_undo
    mod.do_it_dg()
    assert keyframe.frames() == [1.0, 3.0]
    assert keyframe.values() == [2.0, 7.0]
    for _ in range(2):
        mod.undo_it()
        assert not keyframe.has_anim_curve()
        mod.redo_it()
        assert keyframe.frames() == [1.0, 3.0]
        assert keyframe.values() == [2.0, 7.0]


@pytest.mark.parametrize(
    "attribute_type,expected_values",
    [
        ("doubleAngle", [math.pi / 2, math.pi]),
        ("doubleLinear", [90.0, 180.0]),
        ("time", [90.0 / 24, 180.0 / 24]),
    ],
)
def test_set_keys_captures_units_before_execution(
    maya_cmds, attribute_type, expected_values
):
    mod, keyframe = _new_keyframe(maya_cmds, attribute_type)
    maya_cmds.currentUnit(linear="m", angle="rad", time="film")
    keyframe.set_keys([90.0, 180.0], frames=[12.0, 24.0])
    maya_cmds.currentUnit(linear="mm", angle="deg", time="ntsc")
    mod.do_it_dg()
    curve = oma.MFnAnimCurve(keyframe.plug.sourceWithConversion().node())
    after = _curve_state(curve)
    assert keyframe.frames() == [15.0, 30.0]
    assert [key["numeric"][1] for key in after["keys"]] == pytest.approx(
        expected_values
    )
    for _ in range(2):
        mod.undo_it()
        assert not keyframe.has_anim_curve()
        mod.redo_it()
        _assert_curve_state(_curve_state(curve), after)


def test_set_keys_captures_entry_units_before_consuming_generator(maya_cmds):
    mod, keyframe = _new_keyframe(maya_cmds, "time")

    def values():
        yield 12.0
        maya_cmds.currentUnit(time="ntsc")
        yield 24.0

    keyframe.set_keys(values(), frames=[12.0, 24.0])
    mod.do_it_dg()
    curve = oma.MFnAnimCurve(keyframe.plug.sourceWithConversion().node())
    assert keyframe.frames() == [15.0, 30.0]
    assert [
        curve.evaluate(curve.input(index)).asUnits(om.MTime.kSeconds)
        for index in range(curve.numKeys)
    ] == pytest.approx([0.5, 1.0])


@pytest.mark.parametrize(
    "values,frames,error",
    [
        ([1.0], [1.0, 2.0], ValueError),
        ([1.0, 2.0], [1.0], ValueError),
        ([], [1.0], ValueError),
        ([1.0], [], ValueError),
        ([1.0, float("nan")], [1.0, 2.0], ValueError),
        ([1.0, float("inf")], [1.0, 2.0], ValueError),
        ([1.0, 2.0], [1.0, float("-inf")], ValueError),
        ("12", [1.0, 2.0], TypeError),
        (b"12", [1.0, 2.0], TypeError),
        ([1.0, 2.0], "12", TypeError),
        ([1.0, 2.0], b"12", TypeError),
        ([1.0, object()], [1.0, 2.0], TypeError),
    ],
)
def test_invalid_set_keys_preserves_previously_pending_operations(
    maya_cmds, values, frames, error
):
    mod, keyframe = _new_keyframe(maya_cmds)
    keyframe.set_key(3.0, 3.0)
    with pytest.raises(error):
        keyframe.set_keys(values, frames=frames)
    keyframe.set_key(9.0, 9.0)
    mod.do_it_dg()
    assert keyframe.frames() == [3.0, 9.0]
    assert keyframe.values() == [3.0, 9.0]
    mod.undo_it()
    assert not keyframe.has_anim_curve()


def test_generator_failure_does_not_queue_part_of_batch(maya_cmds):
    mod, keyframe = _new_keyframe(maya_cmds)
    keyframe.set_key(3.0, 3.0)

    def values():
        yield 1.0
        raise RuntimeError("input generation failed")

    with pytest.raises(RuntimeError, match="input generation failed"):
        keyframe.set_keys(values(), frames=[1.0, 2.0])
    mod.do_it_dg()
    assert keyframe.frames() == [3.0]
    assert keyframe.values() == [3.0]


def test_invalid_tangent_does_not_queue_batch(maya_cmds):
    mod, keyframe = _new_keyframe(maya_cmds)
    keyframe.set_key(3.0, 3.0)
    with pytest.raises(ValueError, match="Unsupported tangent type"):
        keyframe.set_keys(
            [1.0, 2.0], frames=[1.0, 2.0], out_tangent_type="unknown"
        )
    mod.do_it_dg()
    assert keyframe.frames() == [3.0]


def test_empty_set_keys_does_not_replace_pending_modifier(maya_cmds):
    mod, keyframe = _new_keyframe(maya_cmds)
    keyframe.set_key(3.0, 3.0)
    pending = mod.dg_mod
    assert keyframe.set_keys([], frames=iter(())) is None
    assert mod.dg_mod is pending
    assert not keyframe.has_anim_curve()
    mod.do_it_dg()
    assert keyframe.frames() == [3.0]


@pytest.mark.parametrize("values,frames", [([], []), ([1.0], [1.0])])
def test_set_keys_requires_modifier_manager(maya_cmds, values, frames):
    _, keyframe = _new_keyframe(maya_cmds)
    standalone = KeyframeManager(keyframe.plug)
    with pytest.raises(RuntimeError, match="requires a ModifierManager"):
        standalone.set_keys(values, frames=frames)


def test_set_keys_rejects_compound_plug(maya_cmds):
    node = maya_cmds.createNode("transform")
    selection = om.MSelectionList()
    selection.add(node + ".translate")
    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(selection.getPlug(0), modifier_manager=mod)
    with pytest.raises(TypeError, match="scalar"):
        keyframe.set_keys([1.0], frames=[1.0])
    mod.do_it_dg()
    assert not maya_cmds.ls(type="animCurve")
