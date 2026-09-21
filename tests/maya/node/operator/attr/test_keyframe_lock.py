from __future__ import annotations

from dataclasses import replace

import pytest
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

pytestmark = pytest.mark.maya


def _curve(keyframe):
    return oma.MFnAnimCurve(keyframe.plug.sourceWithConversion().node())


def _unlocked_curve(node, *, weighted):
    keyframe = node.input1D[0].keyframe
    keyframe.set_keys(
        [(frame, frame * frame) for frame in (1, 2, 3, 4)],
        in_tangent_type="linear",
        out_tangent_type="linear",
    )
    node.modifier_manager.do_it_dg()
    curve = _curve(keyframe)
    curve.setIsWeighted(weighted)
    curve.setPreInfinityType(oma.MFnAnimCurve.kLinear)
    curve.setPostInfinityType(oma.MFnAnimCurve.kCycleRelative)
    for index in range(curve.numKeys):
        curve.setTangentsLocked(index, False)
        curve.setWeightsLocked(index, False)
        curve.setIsBreakdown(index, index == 1)
    node.modifier_manager.clear()
    return keyframe, curve


@pytest.mark.parametrize("weighted", [False, True])
def test_set_tangent_locks_changes_only_existing_key_flags(
    plus_minus_average_node,
    weighted,
):
    node = plus_minus_average_node
    keyframe, _ = _unlocked_curve(node, weighted=weighted)
    before = keyframe.get_curve_data()
    assert before is not None

    keyframe.set_tangent_locks(
        2,
        3,
        tangents_locked=True,
        weights_locked=True,
    )
    assert keyframe.get_curve_data() == before
    node.modifier_manager.do_it_dg()

    expected = replace(
        before,
        keys=tuple(
            replace(
                key,
                tangents_locked=2 <= key.frame <= 3,
                weights_locked=2 <= key.frame <= 3,
            )
            for key in before.keys
        ),
    )
    assert keyframe.get_curve_data() == expected
    assert keyframe.frames() == [1, 2, 3, 4]

    for _ in range(3):
        node.modifier_manager.undo_it()
        assert keyframe.get_curve_data() == before
        node.modifier_manager.redo_it()
        assert keyframe.get_curve_data() == expected


def test_set_tangent_lock_and_open_ranges_change_independent_flags(
    plus_minus_average_node,
):
    node = plus_minus_average_node
    keyframe, _ = _unlocked_curve(node, weighted=True)

    assert keyframe.set_tangent_lock(2, tangents_locked=True) is None
    keyframe.set_tangent_locks(
        end_frame=3,
        weights_locked=True,
    )
    node.modifier_manager.do_it_dg()
    data = keyframe.get_curve_data()
    assert data is not None
    assert [key.tangents_locked for key in data.keys] == [
        False,
        True,
        False,
        False,
    ]
    assert [key.weights_locked for key in data.keys] == [
        True,
        True,
        True,
        False,
    ]

    keyframe.set_tangent_locks(
        start_frame=3,
        tangents_locked=True,
        weights_locked=False,
    )
    node.modifier_manager.do_it_dg()
    data = keyframe.get_curve_data()
    assert data is not None
    assert [key.tangents_locked for key in data.keys] == [
        False,
        True,
        True,
        True,
    ]
    assert [key.weights_locked for key in data.keys] == [
        True,
        True,
        False,
        False,
    ]


def test_set_tangent_locks_no_ops_without_existing_targets(
    plus_minus_average_node,
):
    node = plus_minus_average_node
    keyframe = node.input1D[0].keyframe

    keyframe.set_tangent_locks(tangents_locked=True)
    node.modifier_manager.do_it_dg()
    assert not keyframe.has_anim_curve()

    keyframe.set_keys([(1, 1), (2, 2)])
    node.modifier_manager.do_it_dg()
    before = keyframe.get_curve_data()
    keyframe.set_tangent_locks(10, 20, weights_locked=True)
    keyframe.set_tangent_locks(1, 2)
    node.modifier_manager.do_it_dg()
    assert keyframe.get_curve_data() == before


def test_set_tangent_locks_follows_earlier_queued_keys(
    plus_minus_average_node,
):
    node = plus_minus_average_node
    keyframe = node.input1D[0].keyframe
    keyframe.set_keys([(1, 1), (2, 2), (3, 3)])
    keyframe.set_tangent_locks(
        2,
        None,
        tangents_locked=False,
        weights_locked=True,
    )
    assert not keyframe.has_anim_curve()

    node.modifier_manager.do_it_dg()
    data = keyframe.get_curve_data()
    assert data is not None
    assert [key.tangents_locked for key in data.keys] == [True, False, False]
    assert [key.weights_locked for key in data.keys] == [False, True, True]


@pytest.mark.parametrize(
    "call,error,match",
    [
        (
            lambda keyframe: keyframe.set_tangent_locks(
                2, 1, tangents_locked=True
            ),
            ValueError,
            "start_frame",
        ),
        (
            lambda keyframe: keyframe.set_tangent_locks(
                float("nan"), tangents_locked=True
            ),
            ValueError,
            "finite",
        ),
        (
            lambda keyframe: keyframe.set_tangent_locks(tangents_locked=1),
            TypeError,
            "tangents_locked",
        ),
        (
            lambda keyframe: keyframe.set_tangent_lock(
                1, weights_locked="yes"
            ),
            TypeError,
            "weights_locked",
        ),
    ],
)
def test_set_tangent_locks_rejects_invalid_arguments(
    plus_minus_average_node,
    call,
    error,
    match,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    with pytest.raises(error, match=match):
        call(keyframe)
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert not keyframe.has_anim_curve()


def test_set_tangent_locks_capture_ui_time_unit(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    keyframe, _ = _unlocked_curve(node, weighted=False)
    keyframe.set_tangent_locks(2, 3, tangents_locked=True)
    maya_cmds.currentUnit(time="ntsc")
    node.modifier_manager.do_it_dg()

    data = keyframe.get_curve_data()
    assert data is not None
    assert [key.frame for key in data.keys] == pytest.approx(
        [1.25, 2.5, 3.75, 5.0]
    )
    assert [key.tangents_locked for key in data.keys] == [
        False,
        True,
        True,
        False,
    ]
