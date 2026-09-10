# coding: utf-8
from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import KeyframeManager

pytestmark = pytest.mark.maya


@pytest.fixture(autouse=True)
def restore_animation_preferences(new_scene, maya_cmds):
    units = {
        flag: maya_cmds.currentUnit(query=True, **{flag: True})
        for flag in ("linear", "angle", "time")
    }
    tangents = {
        flag: maya_cmds.keyTangent(query=True, g=True, **{flag: True})[0]
        for flag in ("inTangentType", "outTangentType")
    }
    tangents["weightedTangents"] = maya_cmds.keyTangent(
        query=True, g=True, weightedTangents=True
    )
    maya_cmds.currentUnit(linear="cm", angle="deg", time="film")
    try:
        yield
    finally:
        maya_cmds.currentUnit(**units)
        maya_cmds.keyTangent(g=True, **tangents)


def _existing_curve(maya_cmds, name, attribute_type):
    node = maya_cmds.createNode("transform", name=name)
    flags = {"enumName": "A:B:C:D"} if attribute_type == "enum" else {}
    maya_cmds.addAttr(
        node,
        longName="probeValue",
        attributeType=attribute_type,
        keyable=True,
        **flags,
    )
    plug_name = node + ".probeValue"
    for frame, value in ((1.0, 1.0), (5.0, 3.0), (9.0, 2.0)):
        maya_cmds.setKeyframe(
            plug_name, time=frame, value=value, breakdown=frame == 5.0
        )
    selection = om.MSelectionList()
    selection.add(plug_name)
    plug = selection.getPlug(0)
    curve = oma.MFnAnimCurve(plug.sourceWithConversion().node())
    curve.setTangentsLocked(1, False)
    curve.setTangent(1, om.MAngle(0.2, om.MAngle.kRadians), 0.15, True)
    curve.setTangent(1, om.MAngle(-0.4, om.MAngle.kRadians), 0.2, False)
    curve.setWeightsLocked(1, True)
    curve.setPreInfinityType(oma.MFnAnimCurve.kCycle)
    curve.setPostInfinityType(oma.MFnAnimCurve.kLinear)
    return plug, curve


def _curve_state(curve):
    keys = []
    for index in range(curve.numKeys):
        time = curve.input(index)
        value = curve.evaluate(time)
        if isinstance(value, om.MTime):
            value = value.asUnits(om.MTime.kSeconds)
        keys.append(
            {
                "numeric": (
                    time.asUnits(om.MTime.kSeconds),
                    value,
                    *curve.getTangentXY(index, True),
                    *curve.getTangentXY(index, False),
                ),
                "flags": (
                    curve.inTangentType(index),
                    curve.outTangentType(index),
                    curve.tangentsLocked(index),
                    curve.weightsLocked(index),
                    curve.isBreakdown(index),
                ),
            }
        )
    return {
        "curve": (
            curve.animCurveType,
            curve.isWeighted,
            curve.preInfinityType,
            curve.postInfinityType,
        ),
        "keys": keys,
    }


def _assert_curve_state(actual, expected):
    assert actual["curve"] == expected["curve"]
    assert len(actual["keys"]) == len(expected["keys"])
    for actual_key, expected_key in zip(actual["keys"], expected["keys"]):
        assert actual_key["flags"] == expected_key["flags"]
        assert actual_key["numeric"] == pytest.approx(
            expected_key["numeric"], rel=1e-10, abs=1e-10
        )


@pytest.mark.parametrize(
    "attribute_type",
    ["double", "long", "doubleAngle", "doubleLinear", "bool", "enum", "time"],
)
@pytest.mark.parametrize("weighted", [False, True])
@pytest.mark.parametrize("nondefault_units", [False, True])
def test_public_set_matches_cmds_curve_state_and_undo_redo(
    maya_cmds, attribute_type, weighted, nondefault_units
):
    if nondefault_units:
        maya_cmds.currentUnit(linear="m", angle="rad", time="ntsc")
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
    assert before["keys"][1]["flags"] == (
        oma.MFnAnimCurve.kTangentFixed,
        oma.MFnAnimCurve.kTangentFixed,
        False,
        True,
        True,
    )

    mod = bdu.ModifierManager()
    keyframe = KeyframeManager(actual_plug, modifier_manager=mod)
    edits = (
        (5.0, 2.5, "flat", "linear"),
        (7.0, 1.5, None, None),
        (1.0, 0.5, "spline", "flat"),
    )
    for frame, value, in_type, out_type in edits:
        keyframe.set(value, frame, in_type, out_type)
    _assert_curve_state(_curve_state(actual_curve), before)

    # Global defaults are sampled at execution, while existing curve weighting stays.
    maya_cmds.keyTangent(
        g=True,
        inTangentType="linear",
        outTangentType="flat",
        weightedTangents=not weighted,
    )
    for frame, value, in_type, out_type in edits:
        flags = {}
        if in_type is not None:
            flags["inTangentType"] = in_type
        if out_type is not None:
            flags["outTangentType"] = out_type
        if nondefault_units and attribute_type == "doubleAngle":
            value = math.radians(value)
        elif nondefault_units and attribute_type == "doubleLinear":
            value /= 100.0
        maya_cmds.setKeyframe(
            reference_plug.name(), time=frame, value=value, **flags
        )
    expected = _curve_state(reference_curve)
    mod.do_it_dg()
    _assert_curve_state(_curve_state(actual_curve), expected)
    assert actual_curve.numKeys == 4
    assert actual_curve.isWeighted is weighted
    assert expected["keys"][1]["flags"] == (
        oma.MFnAnimCurve.kTangentFixed,
        oma.MFnAnimCurve.kTangentFixed,
        True,
        False,
        False,
    )

    for _ in range(2):
        mod.undo_it()
        _assert_curve_state(_curve_state(actual_curve), before)
        mod.redo_it()
        _assert_curve_state(_curve_state(actual_curve), expected)
