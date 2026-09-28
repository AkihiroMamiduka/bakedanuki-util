from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from bd_util.maya.node.operator.attr._keyframe_reduce import capture_curve_key
from bd_util.maya.node.operator.attr._keyframe_snap_error import (
    within_max_deviation,
)

pytestmark = pytest.mark.maya


def _time(frame):
    return om.MTime(frame, om.MTime.kFilm)


def _curve(cmds, values, *, kind="animCurveTU", weighted=False):
    name = cmds.createNode(kind)
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    scale = math.pi / 180 if kind == "animCurveTA" else 1.0
    for frame, value in values:
        curve.addKey(_time(frame), value * scale)
    curve.setIsWeighted(weighted)
    return curve


def _original(curve):
    return (
        tuple(capture_curve_key(curve, i) for i in range(curve.numKeys)),
        curve.isWeighted,
        curve.preInfinityType,
        curve.postInfinityType,
    )


def _snap(curve, source, destination):
    change = oma.MAnimCurveChange()
    curve.insertKey(_time(destination), False, change)
    curve.remove(curve.find(_time(source)), change)
    return change


@pytest.mark.parametrize("weighted", [False, True])
def test_comparator_accepts_unchanged_curve(maya_cmds, weighted):
    curve = _curve(maya_cmds, [(0, 0), (0.4, 10), (2, 0)], weighted=weighted)
    assert within_max_deviation(curve, *_original(curve), 0)


@pytest.mark.parametrize("kind", ["animCurveTA", "animCurveTL", "animCurveTU"])
@pytest.mark.parametrize("weighted", [False, True])
def test_comparator_checks_whole_interior_curve_in_output_units(
    maya_cmds, kind, weighted
):
    curve = _curve(
        maya_cmds, [(0, 0), (0.4, 10), (2, 0)], kind=kind, weighted=weighted
    )
    original = _original(curve)
    change = _snap(curve, 0.4, 1)
    assert not within_max_deviation(curve, *original, 1)
    assert within_max_deviation(curve, *original, 100)
    change.undoIt()


def test_single_key_stays_constant_when_its_time_changes(maya_cmds):
    curve = _curve(maya_cmds, [(0.4, 10)])
    curve.setPreInfinityType(curve.kCycleRelative)
    curve.setPostInfinityType(curve.kLinear)
    original = _original(curve)
    change = _snap(curve, 0.4, 0)
    assert within_max_deviation(curve, *original, 0)
    change.undoIt()


def test_stepnext_jump_is_checked_between_key_times(maya_cmds):
    curve = _curve(maya_cmds, [(0, 0), (0.4, 1), (2, 2)])
    for index in range(curve.numKeys):
        curve.setInTangentType(index, curve.kTangentFlat)
        curve.setOutTangentType(index, curve.kTangentStepNext)
    original = _original(curve)
    change = _snap(curve, 0.4, 1)
    assert not within_max_deviation(curve, *original, 0.5)
    assert within_max_deviation(curve, *original, 2)
    change.undoIt()


def test_cycle_with_changed_period_is_not_provably_bounded(maya_cmds):
    curve = _curve(maya_cmds, [(0.4, 0), (2, 10)])
    curve.setPreInfinityType(curve.kCycle)
    curve.setPostInfinityType(curve.kCycle)
    original = _original(curve)
    change = _snap(curve, 0.4, 0)
    assert not within_max_deviation(curve, *original, 1000)
    change.undoIt()


@pytest.mark.parametrize("mode", ["kCycle", "kCycleRelative", "kOscillate"])
def test_repeated_infinity_with_unchanged_endpoints_uses_core_bound(
    maya_cmds, mode
):
    curve = _curve(maya_cmds, [(0, 0), (0.4, 10), (2, 0)])
    curve.setPreInfinityType(getattr(curve, mode))
    curve.setPostInfinityType(getattr(curve, mode))
    original = _original(curve)
    change = _snap(curve, 0.4, 1)
    assert within_max_deviation(curve, *original, 100)
    change.undoIt()


def test_linear_infinity_with_changed_slope_is_unbounded(maya_cmds):
    curve = _curve(maya_cmds, [(0, 0), (2, 10)])
    curve.setPreInfinityType(curve.kLinear)
    curve.setTangentsLocked(0, False)
    curve.setTangent(0, 1, 1, True, convertUnits=False)
    curve.setInTangentType(0, curve.kTangentFixed)
    original = _original(curve)
    curve.setTangent(0, 1, 2, True, convertUnits=False)
    assert not within_max_deviation(curve, *original, 1000)


def test_constant_infinity_covers_new_range_outside_original_keys(maya_cmds):
    curve = _curve(maya_cmds, [(0.4, 0), (2, 10)])
    original = _original(curve)
    change = _snap(curve, 0.4, 0)
    assert within_max_deviation(curve, *original, 100)
    change.undoIt()
