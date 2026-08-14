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


def _compact_quintic(value):
    if value >= 1.0:
        return 0.0
    return 1.0 - 10.0 * value**3 + 15.0 * value**4 - 6.0 * value**5


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x0014271A
    assert maya_cmds.attributeQuery(
        "source", node=node, listChildren=True
    ) == [
        "inputPosition",
        "influence",
    ]
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "sourcePosition",
        "enabled",
    ]
    assert maya_cmds.getAttr(f"{node}.kernel") == 4
    assert maya_cmds.getAttr(f"{node}.radius") == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.regularization") == pytest.approx(1.0e-8)
    assert maya_cmds.getAttr(f"{node}.allowNegativeWeights") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 10


def test_no_sources_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 10


def test_weighted_rms_distance_uses_influence(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0), influence=1.0)
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0), influence=3.0)
    _set_pose_source(maya_cmds, node, 3, 2, (3.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (0.0, 4.0, 0.0))
    maya_cmds.setAttr(f"{node}.radius", 10.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    distance = math.sqrt((1.0 * 3.0**2 + 3.0 * 4.0**2) / 4.0)
    assert _weight(maya_cmds, node, 3) == pytest.approx(
        _compact_quintic(distance / 10.0)
    )


def test_source_count_normalization_preserves_radius_meaning(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    single = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    multi = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, single, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, single, 3, 2, (5.0, 0.0, 0.0))
    for source_index in (2, 8, 11):
        _set_source(maya_cmds, multi, source_index, (0.0, 0.0, 0.0))
        _set_pose_source(maya_cmds, multi, 3, source_index, (5.0, 0.0, 0.0))
    for node in (single, multi):
        maya_cmds.setAttr(f"{node}.radius", 10.0)
        maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, multi, 3) == pytest.approx(
        _weight(maya_cmds, single, 3)
    )


def test_influence_change_rebuilds_configuration(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.radius", 20.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)
    before = _weight(maya_cmds, node, 3)

    maya_cmds.setAttr(f"{node}.source[8].influence", 3.0)
    assert _weight(maya_cmds, node, 3) < before


def test_position_tuple_disambiguates_poses(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (10.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 9, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 9, 8, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(1.0)


def test_incomplete_pose_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 12


def test_zero_influence_source_is_ignored_but_topology_is_required(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_source(maya_cmds, node, 8, (0.0, 0.0, 0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (1000.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_all_zero_influences_report_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0), influence=0.0)
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 11


def test_duplicate_position_tuple_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, (0.0, 0.0, 0.0))
        _set_pose_source(maya_cmds, node, 3, source_index, (1.0, 2.0, 3.0))
        _set_pose_source(maya_cmds, node, 9, source_index, (1.0, 2.0, 3.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 5


def test_disabled_incomplete_pose_keeps_zero_output(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, (0.0, 0.0, 0.0))
        _set_pose_source(maya_cmds, node, 3, source_index, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, node, 9, 2, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds, evaluation_mode
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdRbf_MultiPositionWeight")
        _set_source(maya_cmds, node, 2, (0.0, 0.0, 0.0))
        _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0))
        _set_pose_source(maya_cmds, node, 9, 2, (10.0, 0.0, 0.0))
        assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)

        _set_source(maya_cmds, node, 2, (10.0, 0.0, 0.0))
        assert _weight(maya_cmds, node, 9) == pytest.approx(1.0, abs=2.0e-8)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_pose_blend_parent_connection(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    weight = maya_cmds.createNode("bdRbf_MultiPositionWeight")
    blend = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_source(maya_cmds, weight, 2, (0.0, 0.0, 0.0))
    _set_pose_source(maya_cmds, weight, 7, 2, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{blend}.pose[7].translate", 1.0, 2.0, 3.0)
    maya_cmds.connectAttr(f"{weight}.outputWeight", f"{blend}.weight")

    assert maya_cmds.getAttr(f"{blend}.outputTranslate")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )


def test_node_operator_nested_multi_and_existing_access(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_multi_position_weight import (
        BdRbfMultiPositionWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_MultiPositionWeight(name="multi_position")
    blend = nodes.create.bdRbf_PoseBlend(name="multi_position_blend")
    weight.source[2].inputPosition.set((0.0, 0.0, 0.0))
    weight.source[8].inputPosition.set((1.0, 0.0, 0.0))
    weight.source[8].influence.set(2.0)
    weight.pose[7].sourcePosition[2].set((0.0, 0.0, 0.0))
    weight.pose[7].sourcePosition[8].set((1.0, 0.0, 0.0))
    blend.pose[7].translate.set((1.0, 2.0, 3.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfMultiPositionWeight)
    assert weight.outputWeight[7].get() == pytest.approx(1.0, abs=2.0e-8)
    assert isinstance(
        nodes.existing.bdRbf_MultiPositionWeight(weight.name),
        BdRbfMultiPositionWeight,
    )


def test_scene_round_trip_preserves_nested_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_MultiPositionWeight",
        name="saved_multi_position",
    )
    _set_source(maya_cmds, node, 2, (1.0, 2.0, 3.0))
    _set_source(maya_cmds, node, 8, (4.0, 5.0, 6.0), influence=2.5)
    _set_pose_source(maya_cmds, node, 7, 2, (1.0, 2.0, 3.0))
    _set_pose_source(maya_cmds, node, 7, 8, (4.0, 5.0, 6.0))

    scene_path = tmp_path / "rbf_multi_position_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(
        "saved_multi_position.source", multiIndices=True
    ) == [
        2,
        8,
    ]
    assert _weight(maya_cmds, "saved_multi_position", 7) == pytest.approx(
        1.0,
        abs=2.0e-8,
    )
