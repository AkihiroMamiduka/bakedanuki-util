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
    maya_cmds.currentUnit(linear="cm")
    return plugin_path


def _set_source(maya_cmds, node, index, position, *, influence=1.0):
    maya_cmds.setAttr(
        f"{node}.source[{index}].inputPosition",
        *position,
        type="double3",
    )
    maya_cmds.setAttr(f"{node}.source[{index}].influence", influence)


def _set_pose_source(maya_cmds, node, pose_index, source_index, position):
    maya_cmds.setAttr(
        f"{node}.pose[{pose_index}].sourcePosition[{source_index}]",
        *position,
        type="double3",
    )


def _weight(maya_cmds, node, index):
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def _make_single_pose_node(maya_cmds):
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    return node


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x0007F09D
    assert maya_cmds.attributeQuery(
        "source", node=node, listChildren=True
    ) == [
        "inputPosition",
        "influence",
    ]
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "sourcePosition",
        "enabled",
        "useRadiusOverride",
        "innerRadiusOverride",
        "outerRadiusOverride",
    ]
    assert maya_cmds.getAttr(f"{node}.innerRadius") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.outerRadius") == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 6


def test_no_sources_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 6


def test_weighted_rms_distance_is_fallen_off_once(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (3.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (0.0, 4.0, 0.0))
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    distance = math.sqrt((3.0**2 + 4.0**2) / 2.0)
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0 - distance / 10.0)


def test_influence_changes_weighted_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (8.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    before = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.source[8].influence", 3.0)
    assert _weight(maya_cmds, node, 3) < before


def test_inner_radius_plateau_and_outer_boundary(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 6.0)

    _set_source(maya_cmds, node, 2, (2.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    _set_source(maya_cmds, node, 2, (6.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)


def test_pose_radius_override_applies_to_aggregate_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.outerRadius", 6.0)
    _set_source(maya_cmds, node, 2, (4.0, 0.0, 0.0))
    common_weight = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.pose[3].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[3].outerRadiusOverride", 8.0)
    assert _weight(maya_cmds, node, 3) > common_weight


def test_incomplete_pose_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 8


def test_zero_influence_source_is_ignored_but_topology_is_required(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (1000.0, 0.0, 0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (-1000.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_all_zero_influences_report_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionFalloffWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 7


def test_disabled_incomplete_pose_keeps_zero_output(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    _set_pose_source(maya_cmds, node, 9, 8, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)


def test_invalid_radius_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = _make_single_pose_node(maya_cmds)
    maya_cmds.setAttr(f"{node}.innerRadius", 1.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 1.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 2


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds, evaluation_mode
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = _make_single_pose_node(maya_cmds)
        maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
        assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)

        _set_source(maya_cmds, node, 2, (10.0, 0.0, 0.0))
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
    from bd_util.maya.node.operator.node.dg.bd_rbf_multi_position_falloff_weight import (
        BdRbfMultiPositionFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_MultiPositionFalloffWeight(
        name="multi_position_falloff"
    )
    weight.source[2].inputPosition.set((0.0, 0.0, 0.0))
    weight.source[8].inputPosition.set((1.0, 0.0, 0.0))
    weight.source[8].influence.set(2.0)
    weight.pose[7].sourcePosition[2].set((0.0, 0.0, 0.0))
    weight.pose[7].sourcePosition[8].set((1.0, 0.0, 0.0))
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfMultiPositionFalloffWeight)
    assert weight.outputWeight[7].get() == pytest.approx(1.0)
    assert isinstance(
        nodes.existing.bdRbf_MultiPositionFalloffWeight(weight.name),
        BdRbfMultiPositionFalloffWeight,
    )


def test_scene_round_trip_preserves_nested_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_MultiPositionFalloffWeight",
        name="saved_multi_position_falloff",
    )
    _set_source(maya_cmds, node, 2, (1.0, 2.0, 3.0))
    _set_source(maya_cmds, node, 8, (4.0, 5.0, 6.0), influence=2.5)
    _set_pose_source(maya_cmds, node, 7, 2, (1.0, 2.0, 3.0))
    _set_pose_source(maya_cmds, node, 7, 8, (4.0, 5.0, 6.0))

    scene_path = tmp_path / "rbf_multi_position_falloff.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert _weight(
        maya_cmds,
        "saved_multi_position_falloff",
        7,
    ) == pytest.approx(1.0)
