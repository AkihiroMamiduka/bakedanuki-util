# coding: utf-8
from __future__ import annotations

import pytest

pytestmark = pytest.mark.maya

TANGENT_TYPES = (
    "auto",
    "clamped",
    "fast",
    "flat",
    "linear",
    "plateau",
    "slow",
    "spline",
    "step",
    "stepnext",
)


def _expected_in_tangent_type(maya_cmds, tangent_type):
    if tangent_type not in ("step", "stepnext"):
        return tangent_type
    curve = maya_cmds.createNode("animCurveTU")
    try:
        maya_cmds.setKeyframe(
            curve, time=1, value=0, inTangentType=tangent_type
        )
        return maya_cmds.keyTangent(curve, query=True, inTangentType=True)[0]
    finally:
        maya_cmds.delete(curve)


def test_keyframe_property_creates_anim_curve_for_float_plug(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node

    node.input1D[0].keyframe.set_key(12.5, frame=10.0)
    node.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr("test.input1D[0]", time=10.0) == pytest.approx(
        12.5
    )

    source_plugs = maya_cmds.listConnections(
        "test.input1D[0]",
        source=True,
        destination=False,
        plugs=True,
    )
    assert source_plugs == ["test_input1D_0_.output"]


def test_keyframe_property_returns_empty_query_values_without_anim_curve(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe

    assert keyframe.has_anim_curve() is False
    assert keyframe.key_count() == 0
    assert keyframe.frames() == []
    assert keyframe.values() == []
    assert keyframe.has_key(1.0) is False


def test_keyframe_property_reads_key_frames_and_values(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_key(1.5, frame=1.0)
    keyframe.set_key(2.5, frame=2.0)
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.has_anim_curve() is True
    assert keyframe.key_count() == 2
    assert keyframe.frames() == [1.0, 2.0]
    assert keyframe.values() == pytest.approx([1.5, 2.5])
    assert keyframe.has_key(1.0) is True
    assert keyframe.has_key(3.0) is False


def test_keyframe_property_exposes_tangent_type_constants(
    plus_minus_average_node,
):
    from bd_util.maya.node.operator.attr import TangentType

    node = plus_minus_average_node

    assert node.input1D[0].keyframe.tangent is TangentType
    assert isinstance(node.input1D[0].keyframe.tangent.linear, int)


@pytest.mark.parametrize("tangent_type", TANGENT_TYPES)
def test_keyframe_property_sets_in_and_out_tangent_type(
    plus_minus_average_node,
    maya_cmds,
    tangent_type,
):
    node = plus_minus_average_node
    expected_in_type = _expected_in_tangent_type(maya_cmds, tangent_type)

    node.input1D[0].keyframe.set_key(
        12.5,
        frame=10.0,
        in_tangent_type=tangent_type,
        out_tangent_type=tangent_type,
    )
    node.modifier_manager.do_it_dg()

    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == [expected_in_type]
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        outTangentType=True,
    ) == [tangent_type]


def test_common_tangent_type_sets_both_sides_and_specific_side_overrides(
    plus_minus_average_node,
    maya_cmds,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_keys(
        [(1, 0), (2, 1), (3, 0)],
        tangent_type="flat",
        out_tangent_type="linear",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    curve = "test_input1D_0_"
    assert (
        maya_cmds.keyTangent(curve, query=True, inTangentType=True)
        == ["flat"] * 3
    )
    assert (
        maya_cmds.keyTangent(curve, query=True, outTangentType=True)
        == ["linear"] * 3
    )

    keyframe.set_tangents(
        2,
        3,
        tangent_type="auto",
        out_tangent_type="step",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert maya_cmds.keyTangent(curve, query=True, inTangentType=True) == [
        "flat",
        "auto",
        "auto",
    ]
    assert maya_cmds.keyTangent(curve, query=True, outTangentType=True) == [
        "linear",
        "step",
        "step",
    ]


def test_single_key_tangent_arguments_are_keyword_only(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    with pytest.raises(TypeError):
        keyframe.set_key(1, 1, "linear")
    with pytest.raises(TypeError):
        keyframe.set_tangent(1, "linear")


@pytest.mark.parametrize("tangent_type", TANGENT_TYPES)
def test_keyframe_property_sets_tangent_type_from_constant(
    plus_minus_average_node,
    maya_cmds,
    tangent_type,
):
    node = plus_minus_average_node
    tangent = node.input1D[0].keyframe.tangent
    expected_in_type = _expected_in_tangent_type(maya_cmds, tangent_type)

    node.input1D[0].keyframe.set_key(
        12.5,
        frame=10.0,
        in_tangent_type=getattr(tangent, tangent_type),
        out_tangent_type=getattr(tangent, tangent_type),
    )
    node.modifier_manager.do_it_dg()

    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == [expected_in_type]
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        outTangentType=True,
    ) == [tangent_type]


def test_keyframe_property_sets_different_in_and_out_tangent_types(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    tangent = node.input1D[0].keyframe.tangent

    node.input1D[0].keyframe.set_key(
        12.5,
        frame=10.0,
        in_tangent_type=tangent.linear,
        out_tangent_type=tangent.flat,
    )
    node.modifier_manager.do_it_dg()

    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == ["linear"]
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        outTangentType=True,
    ) == ["flat"]


def test_keyframe_property_sets_tangent_type_on_existing_key(
    plus_minus_average_node,
    maya_cmds,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    tangent = keyframe.tangent
    keyframe.set_key(
        12.5,
        frame=10.0,
        in_tangent_type=tangent.linear,
        out_tangent_type=tangent.flat,
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert (
        keyframe.set_tangent(
            10.0,
            in_tangent_type=tangent.flat,
            out_tangent_type=tangent.linear,
        )
        is None
    )
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == ["flat"]
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        outTangentType=True,
    ) == ["linear"]


def test_keyframe_property_set_tangent_ignores_missing_key(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe

    assert keyframe.set_tangent(10.0, in_tangent_type="linear") is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.frames() == []

    keyframe.set_key(12.5, frame=1.0)
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.set_tangent(10.0, in_tangent_type="linear") is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.frames() == [1.0]


@pytest.mark.parametrize(
    "start_frame,end_frame,expected",
    [
        (1.5, 3.5, ["spline", "flat", "flat", "spline"]),
        (None, 2.0, ["flat", "flat", "spline", "spline"]),
        (3.0, None, ["spline", "spline", "flat", "flat"]),
        (None, None, ["flat", "flat", "flat", "flat"]),
    ],
)
def test_keyframe_property_sets_tangents_on_existing_keys_in_range(
    plus_minus_average_node,
    maya_cmds,
    start_frame,
    end_frame,
    expected,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_keys(
        [(frame, frame * 2) for frame in (1, 2, 3, 4)],
        in_tangent_type="spline",
        out_tangent_type="spline",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert (
        keyframe.set_tangents(
            start_frame,
            end_frame,
            out_tangent_type="flat",
        )
        is None
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.frames() == [1.0, 2.0, 3.0, 4.0]
    assert keyframe.values() == pytest.approx([2.0, 4.0, 6.0, 8.0])
    assert (
        maya_cmds.keyTangent("test_input1D_0_", query=True, inTangentType=True)
        == ["spline"] * 4
    )
    assert (
        maya_cmds.keyTangent(
            "test_input1D_0_", query=True, outTangentType=True
        )
        == expected
    )


def test_keyframe_property_set_tangents_preserves_metadata_and_history(
    plus_minus_average_node,
    maya_cmds,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_keys(
        [(frame, frame * frame) for frame in (1, 2, 3, 4)],
        in_tangent_type="linear",
        out_tangent_type="linear",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()
    curve = "test_input1D_0_"
    maya_cmds.keyTangent(curve, edit=True, weightedTangents=True)
    maya_cmds.keyTangent(
        curve,
        edit=True,
        time=(2, 2),
        lock=True,
        weightLock=True,
    )
    maya_cmds.keyframe(curve, edit=True, time=(2, 2), breakdown=True)
    plus_minus_average_node.modifier_manager.clear()
    before = keyframe.get_curve_data()
    assert before is not None

    keyframe.set_tangents(2, 3, in_tangent_type="flat")
    plus_minus_average_node.modifier_manager.do_it_dg()
    after = keyframe.get_curve_data()
    assert after is not None
    assert [key.in_tangent_type for key in after.keys] == [
        "linear",
        "flat",
        "flat",
        "linear",
    ]
    assert [key.out_tangent_type for key in after.keys] == ["linear"] * 4
    assert [key.frame for key in after.keys] == [
        key.frame for key in before.keys
    ]
    assert [key.value for key in after.keys] == pytest.approx(
        [key.value for key in before.keys]
    )
    assert [key.tangents_locked for key in after.keys] == [
        key.tangents_locked for key in before.keys
    ]
    assert [key.weights_locked for key in after.keys] == [
        key.weights_locked for key in before.keys
    ]
    assert [key.breakdown for key in after.keys] == [
        key.breakdown for key in before.keys
    ]
    assert after.weighted == before.weighted
    assert after.pre_infinity == before.pre_infinity
    assert after.post_infinity == before.post_infinity

    for _ in range(2):
        plus_minus_average_node.modifier_manager.undo_it()
        assert keyframe.get_curve_data() == before
        plus_minus_average_node.modifier_manager.redo_it()
        assert keyframe.get_curve_data() == after


def test_keyframe_property_set_tangents_no_ops_without_targets(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe

    assert keyframe.set_tangents(out_tangent_type="flat") is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert not keyframe.has_anim_curve()

    keyframe.set_keys([(1, 1), (2, 2)], out_tangent_type="linear")
    plus_minus_average_node.modifier_manager.do_it_dg()
    before = keyframe.get_curve_data()
    keyframe.set_tangents(10, 20, out_tangent_type="flat")
    keyframe.set_tangents(1, 2)
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.get_curve_data() == before


def test_keyframe_property_set_tangents_follows_earlier_queued_keys(
    plus_minus_average_node,
    maya_cmds,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_keys(
        [(1, 1), (2, 2), (3, 3)],
        out_tangent_type="linear",
    )
    keyframe.set_tangents(2, None, out_tangent_type="flat")
    assert not keyframe.has_anim_curve()

    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.frames() == [1.0, 2.0, 3.0]
    assert maya_cmds.keyTangent(
        "test_input1D_0_", query=True, outTangentType=True
    ) == ["linear", "flat", "flat"]


def test_keyframe_property_set_tangents_supports_negative_subframes(
    plus_minus_average_node,
    maya_cmds,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_keys(
        [(frame, frame) for frame in (-2.5, -1.25, 0.125, 1.5)],
        in_tangent_type="linear",
        out_tangent_type="linear",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    keyframe.set_tangents(
        -1.25,
        0.125,
        in_tangent_type="flat",
        out_tangent_type="auto",
    )
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.frames() == pytest.approx([-2.5, -1.25, 0.125, 1.5])
    assert maya_cmds.keyTangent(
        "test_input1D_0_", query=True, inTangentType=True
    ) == ["linear", "flat", "flat", "linear"]
    assert maya_cmds.keyTangent(
        "test_input1D_0_", query=True, outTangentType=True
    ) == ["linear", "auto", "auto", "linear"]


@pytest.mark.parametrize(
    "call,match",
    [
        (
            lambda keyframe: keyframe.set_tangents(
                2, 1, out_tangent_type="linear"
            ),
            "start_frame",
        ),
        (
            lambda keyframe: keyframe.set_tangents(
                float("nan"), out_tangent_type="linear"
            ),
            "finite",
        ),
        (
            lambda keyframe: keyframe.set_tangents(
                end_frame=float("inf"), out_tangent_type="linear"
            ),
            "finite",
        ),
        (
            lambda keyframe: keyframe.set_tangents(out_tangent_type="unknown"),
            "Unsupported tangent type",
        ),
    ],
)
def test_keyframe_property_set_tangents_rejects_invalid_arguments(
    plus_minus_average_node,
    call,
    match,
):
    with pytest.raises(ValueError, match=match):
        call(plus_minus_average_node.input1D[0].keyframe)


def test_keyframe_property_rejects_unknown_tangent_type_name(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(ValueError, match="Unsupported tangent type"):
        node.input1D[0].keyframe.set_key(
            12.5,
            frame=10.0,
            in_tangent_type="unknown",
        )


def test_keyframe_property_rejects_unknown_tangent_type_value(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(ValueError, match="Unsupported tangent type"):
        node.input1D[0].keyframe.set_key(
            12.5,
            frame=10.0,
            in_tangent_type=999999,
        )


def test_keyframe_manager_can_be_used_with_mplug_directly(
    plus_minus_average_node,
    maya_cmds,
    maya_om,
):
    from bd_util.maya.node.operator.attr import KeyframeManager

    selection = maya_om.MSelectionList()
    selection.add("test.input1D[0]")
    plug = selection.getPlug(0)

    manager = plus_minus_average_node.modifier_manager
    KeyframeManager(
        plug,
        plug_name="test.input1D[0]",
        modifier_manager=manager,
    ).set_key(
        3.5,
        frame=3.0,
    )
    manager.do_it_dg()

    assert maya_cmds.getAttr("test.input1D[0]", time=3.0) == pytest.approx(3.5)


def test_keyframe_manager_insert_inserts_key_on_existing_anim_curve(
    plus_minus_average_node,
    maya_cmds,
    maya_om,
):
    from bd_util.maya.node.operator.attr import KeyframeManager

    node = plus_minus_average_node
    node.input1D[0].keyframe.set_key(1.0, frame=1.0)
    node.input1D[0].keyframe.set_key(10.0, frame=10.0)
    node.modifier_manager.do_it_dg()
    expected_value = maya_cmds.getAttr("test.input1D[0]", time=5.0)

    selection = maya_om.MSelectionList()
    selection.add("test.input1D[0]")
    plug = selection.getPlug(0)

    result = KeyframeManager(
        plug,
        plug_name="test.input1D[0]",
        modifier_manager=node.modifier_manager,
    ).insert_key(frame=5.0)

    assert result is None
    node.modifier_manager.do_it_dg()
    assert maya_cmds.keyframe(
        "test.input1D[0]",
        query=True,
        timeChange=True,
    ) == [1.0, 5.0, 10.0]
    assert maya_cmds.keyframe(
        "test.input1D[0]",
        query=True,
        valueChange=True,
        time=(5.0, 5.0),
    ) == pytest.approx([expected_value])


def test_keyframe_property_insert_is_available_from_scalar_plug(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    node.input1D[0].keyframe.set_key(1.0, frame=1.0)
    node.input1D[0].keyframe.set_key(10.0, frame=10.0)
    node.modifier_manager.do_it_dg()

    assert node.input1D[0].keyframe.insert_key(frame=5.0) is None
    node.modifier_manager.do_it_dg()

    assert maya_cmds.keyframe(
        "test.input1D[0]",
        query=True,
        timeChange=True,
    ) == [1.0, 5.0, 10.0]


def test_keyframe_property_delete_key_removes_key_at_frame(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_key(1.0, frame=1.0)
    keyframe.set_key(2.0, frame=2.0)
    keyframe.set_key(3.0, frame=3.0)
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.delete_key(2.0) is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.frames() == [1.0, 3.0]
    assert keyframe.values() == pytest.approx([1.0, 3.0])
    assert keyframe.delete_key(2.0) is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.frames() == [1.0, 3.0]


def test_keyframe_property_delete_key_ignores_missing_anim_curve(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe

    assert keyframe.delete_key(1.0) is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert not keyframe.has_anim_curve()


def test_keyframe_property_delete_keys_removes_keys_in_range(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    for frame in (1.0, 2.0, 3.0, 4.0):
        keyframe.set_key(frame, frame=frame)
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.delete_keys(start_frame=2.0, end_frame=3.0) is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.frames() == [1.0, 4.0]
    assert keyframe.values() == pytest.approx([1.0, 4.0])


def test_keyframe_property_delete_keys_without_range_removes_all_keys(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_key(1.0, frame=1.0)
    keyframe.set_key(2.0, frame=2.0)
    plus_minus_average_node.modifier_manager.do_it_dg()

    assert keyframe.delete_keys() is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert keyframe.key_count() == 0
    assert keyframe.frames() == []


def test_keyframe_property_delete_keys_ignores_missing_anim_curve(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe

    assert keyframe.delete_keys() is None
    plus_minus_average_node.modifier_manager.do_it_dg()
    assert not keyframe.has_anim_curve()


def test_keyframe_property_delete_keys_rejects_reversed_range(
    plus_minus_average_node,
):
    keyframe = plus_minus_average_node.input1D[0].keyframe
    keyframe.set_key(1.0, frame=1.0)
    plus_minus_average_node.modifier_manager.do_it_dg()

    with pytest.raises(ValueError, match="start_frame"):
        keyframe.delete_keys(start_frame=2.0, end_frame=1.0)


def test_keyframe_property_insert_requires_existing_anim_curve_at_execution(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    node.input1D[0].keyframe.insert_key(frame=5.0)
    with pytest.raises(RuntimeError, match="no channel animCurve"):
        node.modifier_manager.do_it_dg()


def test_keyframe_property_reuses_direct_anim_curve_from_new_operator(
    modifier_manager,
    plus_minus_average_cls,
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    node.input1D[0].keyframe.set_key(1.0, frame=1.0)
    modifier_manager.do_it_dg()

    same_node = plus_minus_average_cls(modifier_manager, name="test")
    same_node.input1D[0].keyframe.set_key(2.0, frame=2.0)
    modifier_manager.do_it_dg()

    source_plugs = maya_cmds.listConnections(
        "test.input1D[0]",
        source=True,
        destination=False,
        plugs=True,
    )
    assert source_plugs == ["test_input1D_0_.output"]
    assert (
        maya_cmds.keyframe(
            "test_input1D_0_",
            query=True,
            keyframeCount=True,
        )
        == 2
    )
    assert maya_cmds.getAttr("test.input1D[0]", time=1.0) == pytest.approx(1.0)
    assert maya_cmds.getAttr("test.input1D[0]", time=2.0) == pytest.approx(2.0)


def test_delete_anim_curve_removes_managed_anim_curve(
    plus_minus_average_node,
    maya_cmds,
    maya_om,
):
    from bd_util.maya.node.operator.attr import KeyframeManager

    node = plus_minus_average_node
    node.input1D[0].keyframe.set_key(1.0, frame=1.0)
    node.modifier_manager.do_it_dg()

    selection = maya_om.MSelectionList()
    selection.add("test.input1D[0]")
    plug = selection.getPlug(0)

    assert (
        KeyframeManager(
            plug,
            plug_name="test.input1D[0]",
            modifier_manager=node.modifier_manager,
        ).delete_anim_curve()
        is None
    )
    node.modifier_manager.do_it_dg()
    assert maya_cmds.objExists("test") is True
    assert maya_cmds.objExists("test_input1D_0_") is False


def test_delete_anim_curve_ignores_missing_anim_curve(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    assert node.input1D[0].keyframe.delete_anim_curve() is None
    node.modifier_manager.do_it_dg()
    assert not node.input1D[0].keyframe.has_anim_curve()


def test_keyframe_property_converts_angle_value_to_anim_curve_radians(
    modifier_manager,
    maya_cmds,
):
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    node = Transform.create(modifier_manager, name="test_transform")
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()

    node.rotate.rotateX.keyframe.set_key(90.0, frame=10.0)
    modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(
        "test_transform.rotateX",
        time=10.0,
    ) == pytest.approx(90.0)
    assert node.rotate.rotateX.keyframe.values() == pytest.approx([90.0])


def test_keyframe_property_is_not_available_on_compound_plug(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(AttributeError):
        node.input3D[0].keyframe


def test_keyframe_property_rejects_output_plug(plus_minus_average_node):
    node = plus_minus_average_node

    with pytest.raises(RuntimeError, match="not writable"):
        node.output3Dx.keyframe.set_key(1.0, frame=1.0)
