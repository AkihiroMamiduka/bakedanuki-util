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


def _axis_x_quaternion(degrees):
    half_angle = math.radians(degrees) * 0.5
    return (math.sin(half_angle), 0.0, 0.0, math.cos(half_angle))


def _set_source(maya_cmds, node, index, quaternion, *, influence=1.0):
    maya_cmds.setAttr(
        f"{node}.source[{index}].inputQuat",
        *quaternion,
        type="double4",
    )
    maya_cmds.setAttr(f"{node}.source[{index}].influence", influence)


def _set_pose_source(maya_cmds, node, pose_index, source_index, quaternion):
    maya_cmds.setAttr(
        f"{node}.pose[{pose_index}].sourceQuat[{source_index}]",
        *quaternion,
        type="double4",
    )


def _weight(maya_cmds, node, index):
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def _make_single_pose_node(maya_cmds):
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    return node


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x0007F09C
    assert maya_cmds.attributeQuery(
        "source", node=node, listChildren=True
    ) == [
        "inputQuat",
        "influence",
    ]
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "sourceQuat",
        "enabled",
        "useRadiusOverride",
        "innerRadiusOverride",
        "outerRadiusOverride",
    ]
    assert maya_cmds.getAttr(f"{node}.innerRadius") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.outerRadius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 6


def test_no_sources_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 6


def test_weighted_rms_distance_is_fallen_off_once(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 8, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(f"{node}.outerRadius", 90.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    normalized_distance = math.sqrt((0.0**2 + 90.0**2) / 2.0) / 90.0
    assert _weight(maya_cmds, node, 3) == pytest.approx(
        1.0 - normalized_distance
    )


def test_influence_changes_weighted_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 8, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(f"{node}.outerRadius", 120.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    before = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.source[8].influence", 3.0)
    assert _weight(maya_cmds, node, 3) < before


def test_inner_radius_plateau_and_outer_boundary(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.innerRadius", 20.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 60.0)

    _set_source(maya_cmds, node, 2, _axis_x_quaternion(20.0))
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(60.0))
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)


def test_pose_radius_override_applies_to_aggregate_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.outerRadius", 60.0)
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(45.0))
    common_weight = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.pose[3].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[3].outerRadiusOverride", 90.0)
    assert _weight(maya_cmds, node, 3) > common_weight


def test_quaternion_sign_and_scale_are_equivalent(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    quaternion = _axis_x_quaternion(30.0)
    _set_source(maya_cmds, node, 2, quaternion)
    _set_pose_source(
        maya_cmds,
        node,
        3,
        2,
        tuple(-2.0 * value for value in quaternion),
    )

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)


def test_incomplete_pose_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 8


def test_zero_influence_ignores_invalid_quaternion(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0, 0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (0.0, 0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_all_zero_influences_report_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 7


@pytest.mark.parametrize("invalid_target", ("input", "pose"))
def test_active_invalid_quaternion_reports_status(maya_cmds, invalid_target):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationFalloffWeight")
    input_quaternion = _axis_x_quaternion(0.0)
    pose_quaternion = _axis_x_quaternion(0.0)
    if invalid_target == "input":
        input_quaternion = (0.0, 0.0, 0.0, 0.0)
    else:
        pose_quaternion = (0.0, 0.0, 0.0, 0.0)
    _set_source(maya_cmds, node, 2, input_quaternion)
    _set_pose_source(maya_cmds, node, 3, 2, pose_quaternion)

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
        maya_cmds.setAttr(f"{node}.outerRadius", 90.0)
        assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)

        _set_source(maya_cmds, node, 2, _axis_x_quaternion(90.0))
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
    from bd_util.maya.node.operator.node.dg.bd_rbf_multi_orientation_falloff_weight import (
        BdRbfMultiOrientationFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_MultiOrientationFalloffWeight(
        name="multi_orientation_falloff"
    )
    weight.source[2].inputQuat.set(_axis_x_quaternion(0.0))
    weight.source[8].inputQuat.set(_axis_x_quaternion(30.0))
    weight.source[8].influence.set(2.0)
    weight.pose[7].sourceQuat[2].set(_axis_x_quaternion(0.0))
    weight.pose[7].sourceQuat[8].set(_axis_x_quaternion(30.0))
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfMultiOrientationFalloffWeight)
    assert weight.outputWeight[7].get() == pytest.approx(1.0)
    assert isinstance(
        nodes.existing.bdRbf_MultiOrientationFalloffWeight(weight.name),
        BdRbfMultiOrientationFalloffWeight,
    )


def test_scene_round_trip_preserves_nested_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_MultiOrientationFalloffWeight",
        name="saved_multi_orientation_falloff",
    )
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(20.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(70.0), influence=2.5)
    _set_pose_source(maya_cmds, node, 7, 2, _axis_x_quaternion(20.0))
    _set_pose_source(maya_cmds, node, 7, 8, _axis_x_quaternion(70.0))

    scene_path = tmp_path / "rbf_multi_orientation_falloff.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert _weight(
        maya_cmds,
        "saved_multi_orientation_falloff",
        7,
    ) == pytest.approx(1.0)
