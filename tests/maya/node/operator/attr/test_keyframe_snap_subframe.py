from __future__ import annotations

import math

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

import bd_util as bdu
from bd_util.maya.node.operator.attr import CurveKeyframeManager
from test_keyframe_move import _assert_state
from test_keyframe_set_equivalence import (
    _curve_state,
    restore_animation_preferences,
)

pytestmark = pytest.mark.maya


def _time(frame):
    return om.MTime(frame, om.MTime.kFilm)


def _frames(curve):
    return [
        curve.input(i).asUnits(om.MTime.kFilm) for i in range(curve.numKeys)
    ]


def _curve(cmds, keys, *, kind="animCurveTL"):
    name = cmds.createNode(kind)
    curve = oma.MFnAnimCurve(om.MSelectionList().add(name).getDependNode(0))
    for frame, value in keys:
        curve.addKey(
            _time(frame), value, curve.kTangentLinear, curve.kTangentLinear
        )
    return curve


@pytest.mark.parametrize("kind", ["animCurveTA", "animCurveTL", "animCurveTU"])
def test_curve_samples_integer_destination_before_removing_source(
    maya_cmds, kind
):
    curve = _curve(maya_cmds, [(0, 0), (0.75, 10), (2, 0)], kind=kind)
    original_value = curve.evaluate(_time(1))
    original_shape = curve.evaluate(_time(0.75))
    original = _curve_state(curve)
    manager = bdu.ModifierManager()
    keys = CurveKeyframeManager(curve.object(), modifier_manager=manager)

    assert keys.snap_subframe_keys() is None
    assert _curve_state(curve) == original
    manager.do_it_dg()

    assert _frames(curve) == [0, 1, 2]
    assert curve.evaluate(_time(1)) == pytest.approx(original_value)
    assert curve.evaluate(_time(0.75)) != pytest.approx(original_shape)
    changed = _curve_state(curve)
    for _ in range(2):
        manager.undo_it()
        _assert_state(_curve_state(curve), original)
        manager.redo_it()
        _assert_state(_curve_state(curve), changed)


@pytest.mark.parametrize(
    "bounds,expected",
    [
        ((0.25, 1.25), [-2.25, 0, 1, 3.25]),
        ((None, 0.25), [-2, 0, 1.25, 3.25]),
        ((1.25, None), [-2.25, 0.25, 1, 3]),
        ((1.25, 1.25), [-2.25, 0.25, 1, 3.25]),
        ((10, 20), [-2.25, 0.25, 1.25, 3.25]),
    ],
)
def test_range_is_inclusive_and_does_not_insert_boundaries(
    maya_cmds, bounds, expected
):
    curve = _curve(
        maya_cmds,
        [(-2.25, 1), (0.25, 2), (1.25, 3), (3.25, 4)],
    )
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys(*bounds)
    manager.do_it_dg()
    assert _frames(curve) == expected


def test_half_frames_round_away_from_zero(maya_cmds):
    curve = _curve(maya_cmds, [(-2, 0), (-0.5, 1), (0.5, 2), (2, 0)])
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys()
    manager.do_it_dg()
    assert _frames(curve) == [-2, -1, 1, 2]


@pytest.mark.parametrize("preserve", [True, False])
def test_fractional_breakdown_is_kept_or_recreated(maya_cmds, preserve):
    curve = _curve(maya_cmds, [(0, 0), (1.25, 5), (3, 0)])
    curve.setIsBreakdown(1, True)
    original = _curve_state(curve)
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys(preserve_breakdowns=preserve)
    manager.do_it_dg()
    selected_time = 1.25 if preserve else 1
    assert _frames(curve) == [0, selected_time, 3]
    assert curve.isBreakdown(curve.find(_time(selected_time)))
    manager.undo_it()
    _assert_state(_curve_state(curve), original)


@pytest.mark.parametrize(
    "keys",
    [
        [(0, 0), (1, 1), (1.25, 10), (2, 0)],
        [(0, 0), (1.1, 5), (1.4, 7), (2, 0)],
    ],
)
def test_existing_or_second_destination_key_is_a_collision(maya_cmds, keys):
    curve = _curve(maya_cmds, keys)
    original = _curve_state(curve)
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys()
    with pytest.raises(ValueError):
        manager.do_it_dg()
    _assert_state(_curve_state(curve), original)
    assert not manager.can_undo


def test_explicit_deviation_limit_rejects_change_but_default_allows_it(
    maya_cmds,
):
    curve = _curve(maya_cmds, [(0, 0), (0.75, 10), (2, 0)])
    original = _curve_state(curve)
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys(max_deviation=0)
    with pytest.raises(ValueError):
        manager.do_it_dg()
    _assert_state(_curve_state(curve), original)
    assert not manager.can_undo

    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys()
    manager.do_it_dg()
    assert _frames(curve) == [0, 1, 2]
    manager.undo_it()
    _assert_state(_curve_state(curve), original)

    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys(max_deviation=100)
    manager.do_it_dg()
    assert _frames(curve) == [0, 1, 2]


def test_step_next_keeps_discrete_tangent_and_sampled_integer_value(maya_cmds):
    curve = _curve(maya_cmds, [(0, 0), (0.75, 10), (2, 0)], kind="animCurveTU")
    for index in range(curve.numKeys):
        curve.setOutTangentType(index, curve.kTangentStepNext)
    original_integer_value = curve.evaluate(_time(1))
    original_switch_value = curve.evaluate(_time(0.5))
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys()
    manager.do_it_dg()

    assert _frames(curve) == [0, 1, 2]
    assert curve.value(curve.find(_time(1))) == pytest.approx(
        original_integer_value
    )
    assert curve.outTangentType(curve.find(_time(1))) == curve.kTangentStepNext
    assert curve.evaluate(_time(0.5)) != pytest.approx(original_switch_value)


def test_plug_selects_existing_curve_and_captures_ui_time_unit(maya_cmds):
    maya_cmds.currentUnit(time="film")
    name = maya_cmds.createNode("transform")
    for frame, value in ((0, 0), (0.75, 10), (2, 0)):
        maya_cmds.setKeyframe(name + ".tx", time=frame, value=value)
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    original = node.tx.keyframe.get_curve_data()
    assert node.tx.keyframe.snap_subframe_keys() is None
    assert node.tx.keyframe.get_curve_data() == original
    maya_cmds.currentUnit(time="ntsc")
    manager.do_it_dg()
    curve_name = maya_cmds.listConnections(
        name + ".tx", source=True, destination=False, type="animCurve"
    )[0]
    curve = oma.MFnAnimCurve(
        om.MSelectionList().add(curve_name).getDependNode(0)
    )
    times = [
        curve.input(i).asUnits(om.MTime.kSeconds) for i in range(curve.numKeys)
    ]
    assert times == pytest.approx([0, 1 / 24, 2 / 24])


def test_plug_explicit_layer_only_snaps_its_own_curve(maya_cmds):
    target = maya_cmds.createNode("transform")
    for frame, value in ((0, 0), (0.75, 10), (2, 0)):
        maya_cmds.setKeyframe(target + ".tx", time=frame, value=value)
    base_name = maya_cmds.listConnections(
        target + ".tx", source=True, destination=False, type="animCurve"
    )[0]
    base = oma.MFnAnimCurve(
        om.MSelectionList().add(base_name).getDependNode(0)
    )
    layer = maya_cmds.animLayer("Correction", attribute=target + ".tx")
    for frame, value in ((0, 0), (0.75, 5), (2, 0)):
        maya_cmds.setKeyframe(
            target + ".tx",
            time=frame,
            value=value,
            animLayer=layer,
            noResolve=True,
        )
    layer_name = maya_cmds.animLayer(
        layer, query=True, findCurveForPlug=target + ".tx"
    )[0]
    layer_curve = oma.MFnAnimCurve(
        om.MSelectionList().add(layer_name).getDependNode(0)
    )
    manager = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=manager).existing.transform(target)
    node.tx.keyframe.anim_layer(layer).snap_subframe_keys()
    manager.do_it_dg()
    assert _frames(base) == [0, 0.75, 2]
    assert _frames(layer_curve) == [0, 1, 2]


def test_empty_curve_and_missing_curve_are_noops(maya_cmds):
    curve = _curve(maya_cmds, [])
    manager = bdu.ModifierManager()
    CurveKeyframeManager(
        curve.object(), modifier_manager=manager
    ).snap_subframe_keys()
    name = maya_cmds.createNode("transform")
    node = bdu.Nodes(modifier_manager=manager).existing.transform(name)
    node.tx.keyframe.snap_subframe_keys()
    maya_cmds.file(modified=False)
    manager.do_it_dg()
    assert curve.numKeys == 0
    assert not node.tx.keyframe.has_anim_curve()
    assert not maya_cmds.file(query=True, modified=True)


@pytest.mark.parametrize(
    "args,kwargs,error",
    [
        ((2, 1), {}, ValueError),
        ((math.inf, None), {}, ValueError),
        ((), {"preserve_breakdowns": 1}, TypeError),
        ((), {"max_deviation": -1}, ValueError),
        ((), {"max_deviation": math.inf}, ValueError),
        ((), {"max_deviation": "0.1"}, TypeError),
    ],
)
def test_invalid_arguments_are_rejected_at_booking(
    maya_cmds, args, kwargs, error
):
    curve = _curve(maya_cmds, [(0, 0), (0.75, 1), (2, 0)])
    manager = bdu.ModifierManager()
    keys = CurveKeyframeManager(curve.object(), modifier_manager=manager)
    with pytest.raises(error):
        keys.snap_subframe_keys(*args, **kwargs)
    assert not manager.can_undo
