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


def test_keyframe_property_creates_anim_curve_for_float_plug(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node

    node.input1D[0].keyframe.set_direct(12.5, frame=10.0)

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

    node.input1D[0].keyframe.set_direct(
        12.5,
        frame=10.0,
        in_tangent_type=tangent_type,
        out_tangent_type=tangent_type,
    )

    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == [tangent_type]
    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        outTangentType=True,
    ) == [tangent_type]


@pytest.mark.parametrize("tangent_type", TANGENT_TYPES)
def test_keyframe_property_sets_tangent_type_from_constant(
    plus_minus_average_node,
    maya_cmds,
    tangent_type,
):
    node = plus_minus_average_node
    tangent = node.input1D[0].keyframe.tangent

    node.input1D[0].keyframe.set_direct(
        12.5,
        frame=10.0,
        in_tangent_type=getattr(tangent, tangent_type),
        out_tangent_type=getattr(tangent, tangent_type),
    )

    assert maya_cmds.keyTangent(
        "test_input1D_0_",
        query=True,
        inTangentType=True,
    ) == [tangent_type]
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

    node.input1D[0].keyframe.set_direct(
        12.5,
        frame=10.0,
        in_tangent_type=tangent.linear,
        out_tangent_type=tangent.flat,
    )

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


def test_keyframe_property_rejects_unknown_tangent_type_name(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(ValueError, match="Unsupported tangent type"):
        node.input1D[0].keyframe.set_direct(
            12.5,
            frame=10.0,
            in_tangent_type="unknown",
        )


def test_keyframe_property_rejects_unknown_tangent_type_value(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(ValueError, match="Unsupported tangent type"):
        node.input1D[0].keyframe.set_direct(
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

    KeyframeManager(plug, plug_name="test.input1D[0]").set_direct(
        3.5,
        frame=3.0,
    )

    assert maya_cmds.getAttr("test.input1D[0]", time=3.0) == pytest.approx(
        3.5
    )


def test_keyframe_manager_insert_direct_inserts_key_on_existing_anim_curve(
    plus_minus_average_node,
    maya_cmds,
    maya_om,
):
    from bd_util.maya.node.operator.attr import KeyframeManager

    node = plus_minus_average_node
    node.input1D[0].keyframe.set_direct(1.0, frame=1.0)
    node.input1D[0].keyframe.set_direct(10.0, frame=10.0)
    expected_value = maya_cmds.getAttr("test.input1D[0]", time=5.0)

    selection = maya_om.MSelectionList()
    selection.add("test.input1D[0]")
    plug = selection.getPlug(0)

    index = KeyframeManager(
        plug,
        plug_name="test.input1D[0]",
    ).insert_direct(frame=5.0)

    assert index == 1
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


def test_keyframe_property_insert_direct_is_available_from_scalar_plug(
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    node.input1D[0].keyframe.set_direct(1.0, frame=1.0)
    node.input1D[0].keyframe.set_direct(10.0, frame=10.0)

    index = node.input1D[0].keyframe.insert_direct(frame=5.0)

    assert index == 1
    assert maya_cmds.keyframe(
        "test.input1D[0]",
        query=True,
        timeChange=True,
    ) == [1.0, 5.0, 10.0]


def test_keyframe_property_insert_direct_requires_existing_anim_curve(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(RuntimeError, match="no upstream time-input animCurve"):
        node.input1D[0].keyframe.insert_direct(frame=5.0)


def test_keyframe_property_reuses_upstream_anim_curve_from_new_operator(
    modifier_manager,
    plus_minus_average_cls,
    plus_minus_average_node,
    maya_cmds,
):
    node = plus_minus_average_node
    node.input1D[0].keyframe.set_direct(1.0, frame=1.0)

    same_node = plus_minus_average_cls(modifier_manager, name="test")
    same_node.input1D[0].keyframe.set_direct(2.0, frame=2.0)

    source_plugs = maya_cmds.listConnections(
        "test.input1D[0]",
        source=True,
        destination=False,
        plugs=True,
    )
    assert source_plugs == ["test_input1D_0_.output"]
    assert maya_cmds.keyframe(
        "test_input1D_0_",
        query=True,
        keyframeCount=True,
    ) == 2
    assert maya_cmds.getAttr("test.input1D[0]", time=1.0) == pytest.approx(
        1.0
    )
    assert maya_cmds.getAttr("test.input1D[0]", time=2.0) == pytest.approx(
        2.0
    )


def test_delete_anim_curve_removes_managed_anim_curve(
    plus_minus_average_node,
    maya_cmds,
    maya_om,
):
    from bd_util.maya.node.operator.attr import KeyframeManager

    node = plus_minus_average_node
    node.input1D[0].keyframe.set_direct(1.0, frame=1.0)

    selection = maya_om.MSelectionList()
    selection.add("test.input1D[0]")
    plug = selection.getPlug(0)

    assert (
        KeyframeManager(
            plug,
            plug_name="test.input1D[0]",
        ).delete_anim_curve()
        is True
    )
    assert maya_cmds.objExists("test") is True
    assert maya_cmds.objExists("test_input1D_0_") is False


def test_delete_anim_curve_returns_false_without_anim_curve(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    assert node.input1D[0].keyframe.delete_anim_curve() is False


def test_keyframe_property_converts_angle_value_to_anim_curve_radians(
    modifier_manager,
    maya_cmds,
):
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    node = Transform.create(modifier_manager, name="test_transform")
    modifier_manager.do_it_dag()
    modifier_manager.do_it_dg()

    node.rotate.rotateX.keyframe.set_direct(90.0, frame=10.0)

    assert maya_cmds.getAttr(
        "test_transform.rotateX",
        time=10.0,
    ) == pytest.approx(90.0)


def test_keyframe_property_is_not_available_on_compound_plug(
    plus_minus_average_node,
):
    node = plus_minus_average_node

    with pytest.raises(AttributeError):
        node.input3D[0].keyframe


def test_keyframe_property_rejects_output_plug(plus_minus_average_node):
    node = plus_minus_average_node

    with pytest.raises(RuntimeError, match="not writable"):
        node.output3Dx.keyframe.set_direct(1.0, frame=1.0)
