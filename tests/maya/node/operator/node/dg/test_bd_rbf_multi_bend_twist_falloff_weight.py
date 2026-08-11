from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def _load_bd_util_nodes(maya_cmds) -> Path:
    default_path = (
        Path(__file__).resolve().parents[6]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip("Build bdUtilNodes.mll before running native tests.")
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    maya_cmds.currentUnit(angle="degree")
    return plugin_path


def _axis_quaternion(axis: str, degrees: float):
    half_angle = math.radians(degrees) * 0.5
    sine = math.sin(half_angle)
    xyz = {
        "x": (sine, 0.0, 0.0),
        "y": (0.0, sine, 0.0),
        "z": (0.0, 0.0, sine),
    }[axis]
    return (*xyz, math.cos(half_angle))


def _set_quaternion(maya_cmds, plug, quaternion):
    maya_cmds.setAttr(plug, *quaternion, type="double4")


def _compose(
    maya_cmds,
    *,
    twist=0.0,
    bend_h=0.0,
    bend_v=0.0,
    order=0,
    axis_quat=(0.0, 0.0, 0.0, 1.0),
):
    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.inputTwist", twist)
    maya_cmds.setAttr(f"{compose}.inputBendH", bend_h)
    maya_cmds.setAttr(f"{compose}.inputBendV", bend_v)
    maya_cmds.setAttr(f"{compose}.order", order)
    _set_quaternion(maya_cmds, f"{compose}.axisQuat", axis_quat)
    return tuple(maya_cmds.getAttr(f"{compose}.outputQuat")[0])


def _set_source(
    maya_cmds,
    node,
    index,
    quaternion,
    *,
    axis_quat=(0.0, 0.0, 0.0, 1.0),
    order=0,
    influence=1.0,
):
    _set_quaternion(
        maya_cmds,
        f"{node}.source[{index}].inputQuat",
        quaternion,
    )
    _set_quaternion(
        maya_cmds,
        f"{node}.source[{index}].axisQuat",
        axis_quat,
    )
    maya_cmds.setAttr(f"{node}.source[{index}].order", order)
    maya_cmds.setAttr(f"{node}.source[{index}].influence", influence)


def _set_pose_source(maya_cmds, node, pose_index, source_index, quaternion):
    _set_quaternion(
        maya_cmds,
        f"{node}.pose[{pose_index}].sourceQuat[{source_index}]",
        quaternion,
    )


def _weight(maya_cmds, node, index):
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def _make_single_pose_node(maya_cmds):
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    _set_source(maya_cmds, node, 2, identity)
    _set_pose_source(maya_cmds, node, 3, 2, identity)
    return node


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x0007F09E
    assert maya_cmds.attributeQuery(
        "source", node=node, listChildren=True
    ) == ["inputQuat", "axisQuat", "order", "influence"]
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "sourceQuat",
        "enabled",
        "useRadiusOverride",
        "bendInnerRadiusOverride",
        "bendOuterRadiusOverride",
        "twistInnerRadiusOverride",
        "twistOuterRadiusOverride",
    ]
    assert maya_cmds.attributeQuery("order", node=node, listEnum=True) == [
        "TwistBend:BendTwist"
    ]
    assert maya_cmds.attributeQuery("mode", node=node, listEnum=True) == [
        "BendTwist:BendOnly"
    ]
    assert maya_cmds.attributeQuery(
        "falloffStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidQuaternion:"
        "UnsupportedFalloff:UnsupportedMode:UnsupportedOrder:"
        "NumericalFailure:NoSources:InvalidInfluence:IncompletePose"
    ]
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 8
    assert maya_cmds.getAttr(f"{node}.source[2].inputQuat")[0] == (
        0.0,
        0.0,
        0.0,
        1.0,
    )
    assert maya_cmds.getAttr(f"{node}.source[2].axisQuat")[0] == (
        0.0,
        0.0,
        0.0,
        1.0,
    )
    assert maya_cmds.getAttr(f"{node}.source[2].order") == 0
    assert maya_cmds.getAttr(f"{node}.source[2].influence") == 1.0
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert maya_cmds.getAttr(f"{node}.mode") == 0
    assert maya_cmds.getAttr(f"{node}.bendInnerRadius") == 0.0
    assert maya_cmds.getAttr(f"{node}.bendOuterRadius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.twistInnerRadius") == 0.0
    assert maya_cmds.getAttr(f"{node}.twistOuterRadius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2


def test_weighted_rms_bend_distance_is_fallen_off_once(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, identity)
    _set_pose_source(maya_cmds, node, 3, 2, identity)
    _set_pose_source(maya_cmds, node, 3, 8, _axis_quaternion("y", 90.0))
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 90.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    normalized_distance = math.sqrt((0.0**2 + 90.0**2) / 2.0) / 90.0
    assert _weight(maya_cmds, node, 3) == pytest.approx(
        1.0 - normalized_distance
    )


def test_weighted_rms_twist_distance_is_fallen_off_once(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, identity)
    _set_pose_source(maya_cmds, node, 3, 2, identity)
    _set_pose_source(maya_cmds, node, 3, 8, _axis_quaternion("x", 90.0))
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 90.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    normalized_distance = math.sqrt((0.0**2 + 90.0**2) / 2.0) / 90.0
    assert _weight(maya_cmds, node, 3) == pytest.approx(
        1.0 - normalized_distance
    )


def test_bend_twist_multiplies_the_two_aggregate_falloffs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, identity)
    _set_pose_source(maya_cmds, node, 3, 2, _axis_quaternion("y", 90.0))
    _set_pose_source(maya_cmds, node, 3, 8, _axis_quaternion("x", 90.0))
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 90.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 90.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    component_weight = 1.0 - math.sqrt(90.0**2 / 2.0) / 90.0
    assert _weight(maya_cmds, node, 3) == pytest.approx(component_weight**2)


def test_per_source_axis_and_order_are_used(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    axis = _axis_quaternion("z", 90.0)
    identity = _axis_quaternion("x", 0.0)
    pose = _compose(
        maya_cmds,
        twist=30.0,
        bend_h=30.0,
        order=1,
        axis_quat=axis,
    )
    _set_source(
        maya_cmds,
        node,
        4,
        identity,
        axis_quat=axis,
        order=1,
    )
    _set_pose_source(maya_cmds, node, 7, 4, pose)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    assert _weight(maya_cmds, node, 7) == pytest.approx(0.25)


def test_influence_changes_weighted_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    _set_source(maya_cmds, node, 2, identity)
    _set_source(maya_cmds, node, 8, identity)
    _set_pose_source(maya_cmds, node, 3, 2, identity)
    _set_pose_source(maya_cmds, node, 3, 8, _axis_quaternion("y", 90.0))
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 120.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    before = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.source[8].influence", 3.0)
    assert _weight(maya_cmds, node, 3) < before


def test_bend_only_ignores_twist_and_invalid_twist_radius(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.twistInnerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 0.0)
    _set_source(maya_cmds, node, 2, _axis_quaternion("x", 150.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_twist_uses_shortest_periodic_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_quaternion("x", 170.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_quaternion("x", -170.0))
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 40.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.5)


def test_invalid_active_radius_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 2


def test_unsupported_active_source_order_reports_status(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    selection = maya_om.MSelectionList()
    selection.add(f"{node}.source[2].order")
    selection.getPlug(0).setShort(7)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 6


def test_pose_radius_override_applies_to_aggregate_distances(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    _set_source(maya_cmds, node, 2, _axis_quaternion("y", 45.0))
    common_weight = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.pose[3].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[3].bendOuterRadiusOverride", 90.0)
    assert _weight(maya_cmds, node, 3) > common_weight


def test_incomplete_pose_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    _set_source(maya_cmds, node, 2, identity)
    _set_source(maya_cmds, node, 8, identity)
    _set_pose_source(maya_cmds, node, 3, 2, identity)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 10


def test_zero_influence_ignores_invalid_source_configuration(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    zero = (0.0, 0.0, 0.0, 0.0)
    _set_source(maya_cmds, node, 2, identity)
    _set_source(
        maya_cmds,
        node,
        8,
        zero,
        axis_quat=zero,
        influence=0.0,
    )
    _set_pose_source(maya_cmds, node, 3, 2, identity)
    _set_pose_source(maya_cmds, node, 3, 8, zero)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_all_zero_influences_report_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    _set_source(maya_cmds, node, 2, identity, influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, identity)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 9


@pytest.mark.parametrize("invalid_target", ("input", "axis", "pose"))
def test_active_invalid_quaternion_reports_status(maya_cmds, invalid_target):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiBendTwistFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    zero = (0.0, 0.0, 0.0, 0.0)
    _set_source(
        maya_cmds,
        node,
        2,
        zero if invalid_target == "input" else identity,
        axis_quat=zero if invalid_target == "axis" else identity,
    )
    _set_pose_source(
        maya_cmds,
        node,
        3,
        2,
        zero if invalid_target == "pose" else identity,
    )

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 3


def test_disabled_incomplete_pose_keeps_zero_output(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    _set_pose_source(maya_cmds, node, 9, 8, (0.0, 0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds, evaluation_mode
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = _make_single_pose_node(maya_cmds)
        maya_cmds.setAttr(f"{node}.mode", 1)
        assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)

        _set_source(maya_cmds, node, 2, _axis_quaternion("y", 60.0))
        assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_pose_blend_parent_connection(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    weight = _make_single_pose_node(maya_cmds)
    blend = maya_cmds.createNode("bdRbf_PoseBlend")
    maya_cmds.setAttr(f"{blend}.pose[3].translate", 1.0, 2.0, 3.0)
    maya_cmds.connectAttr(f"{weight}.outputWeight", f"{blend}.weight")

    assert maya_cmds.getAttr(f"{blend}.outputTranslate")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )


def test_node_operator_nested_multi_and_existing_access(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_multi_bend_twist_falloff_weight import (
        BdRbfMultiBendTwistFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_MultiBendTwistFalloffWeight(
        name="multi_bend_twist_falloff"
    )
    identity = _axis_quaternion("x", 0.0)
    weight.source[2].inputQuat.set(identity)
    weight.source[2].axisQuat.set(identity)
    weight.source[2].order.set(weight.source[2].order.TWISTBEND)
    weight.source[8].inputQuat.set(identity)
    weight.source[8].influence.set(2.0)
    weight.pose[7].sourceQuat[2].set(identity)
    weight.pose[7].sourceQuat[8].set(identity)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfMultiBendTwistFalloffWeight)
    assert weight.outputWeight[7].get() == pytest.approx(1.0)
    assert isinstance(
        nodes.existing.bdRbf_MultiBendTwistFalloffWeight(weight.name),
        BdRbfMultiBendTwistFalloffWeight,
    )


def test_scene_round_trip_preserves_nested_configuration(
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_MultiBendTwistFalloffWeight",
        name="saved_multi_bend_twist_falloff",
    )
    identity = _axis_quaternion("x", 0.0)
    axis = _axis_quaternion("z", 90.0)
    source_two = _axis_quaternion("y", 20.0)
    _set_source(maya_cmds, node, 2, source_two)
    _set_source(
        maya_cmds,
        node,
        8,
        identity,
        axis_quat=axis,
        order=1,
        influence=2.5,
    )
    _set_pose_source(maya_cmds, node, 7, 2, source_two)
    _set_pose_source(maya_cmds, node, 7, 8, identity)

    scene_path = tmp_path / "rbf_multi_bend_twist_falloff.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert _weight(
        maya_cmds,
        "saved_multi_bend_twist_falloff",
        7,
    ) == pytest.approx(1.0)
    assert maya_cmds.getAttr(
        "saved_multi_bend_twist_falloff.source[8].axisQuat"
    )[0] == pytest.approx(axis)
    assert (
        maya_cmds.getAttr("saved_multi_bend_twist_falloff.source[8].order")
        == 1
    )
