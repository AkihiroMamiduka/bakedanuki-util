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
        pytest.skip(
            "bdUtilNodes.mll is not built. "
            "Run scripts/build-native-maya2025.cmd first."
        )

    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    maya_cmds.currentUnit(linear="cm")
    return plugin_path


def _set_pose(maya_cmds, node: str, index: int, position) -> None:
    maya_cmds.setAttr(
        f"{node}.pose[{index}].position",
        *position,
        type="double3",
    )


def _set_input(maya_cmds, node: str, position) -> None:
    maya_cmds.setAttr(
        f"{node}.inputPosition",
        *position,
        type="double3",
    )


def _weight(maya_cmds, node: str, index: int) -> float:
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142716
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "position",
        "enabled",
        "useRadiusOverride",
        "innerRadiusOverride",
        "outerRadiusOverride",
    ]
    assert maya_cmds.attributeQuery(
        "position", node=node, listChildren=True
    ) == ["positionX", "positionY", "positionZ"]
    assert maya_cmds.getAttr(f"{node}.inputPositionX", type=True) == (
        "doubleLinear"
    )
    assert maya_cmds.getAttr(f"{node}.innerRadius", type=True) == (
        "doubleLinear"
    )
    assert maya_cmds.getAttr(f"{node}.outerRadius", type=True) == (
        "doubleLinear"
    )
    assert maya_cmds.attributeQuery("falloff", node=node, listEnum=True) == [
        "Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "falloffStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidPosition:"
        "UnsupportedFalloff:NumericalFailure"
    ]
    assert maya_cmds.getAttr(f"{node}.inputPosition")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.innerRadius") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.outerRadius") == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 1


def test_pose_defaults_to_enabled_origin_and_shared_radius(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")

    assert maya_cmds.getAttr(f"{node}.pose[3].position")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert maya_cmds.getAttr(f"{node}.pose[3].useRadiusOverride") is False
    assert maya_cmds.getAttr(
        f"{node}.pose[3].innerRadiusOverride"
    ) == pytest.approx(0.0)
    assert maya_cmds.getAttr(
        f"{node}.pose[3].outerRadiusOverride"
    ) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 0


@pytest.mark.parametrize(
    ("falloff", "expected"),
    (
        (0, 0.75),
        (1, 1.0 - 3.0 * 0.25**2 + 2.0 * 0.25**3),
        (
            2,
            1.0 - 10.0 * 0.25**3 + 15.0 * 0.25**4 - 6.0 * 0.25**5,
        ),
    ),
)
def test_falloff_formulas_use_inner_to_outer_normalized_distance(
    maya_cmds,
    falloff,
    expected,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.falloff", falloff)
    _set_input(maya_cmds, node, (4.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 0) == pytest.approx(expected, abs=1.0e-12)


def test_weight_is_one_inside_inner_and_zero_at_outer_radius(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)

    _set_input(maya_cmds, node, (1.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)
    _set_input(maya_cmds, node, (2.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)
    _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    _set_input(maya_cmds, node, (20.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)


def test_distance_is_three_dimensional_euclidean_length(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (3.0, 4.0, 12.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 52.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.75, abs=1.0e-12)


def test_pose_radius_override_is_individual_and_not_normalized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 8, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].innerRadiusOverride", 10.0)
    maya_cmds.setAttr(f"{node}.pose[8].outerRadiusOverride", 20.0)
    _set_input(maya_cmds, node, (5.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 2) == pytest.approx(0.5, abs=1.0e-12)
    assert _weight(maya_cmds, node, 8) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 2) + _weight(
        maya_cmds, node, 8
    ) == pytest.approx(1.5)


def test_disabled_override_values_are_ignored_until_enabled(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.pose[0].innerRadiusOverride", 5.0)
    maya_cmds.setAttr(f"{node}.pose[0].outerRadiusOverride", 2.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True

    maya_cmds.setAttr(f"{node}.pose[0].useRadiusOverride", True)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 2


def test_disabled_pose_keeps_output_zero_and_ignores_invalid_values(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 9, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].positionX", math.nan)
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize(
    ("invalid_target", "expected_status"),
    (
        ("input", 3),
        ("pose", 3),
        ("shared_radius", 2),
        ("override_radius", 2),
    ),
)
def test_invalid_input_reports_status_and_zeroes_outputs(
    maya_cmds,
    invalid_target,
    expected_status,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))

    if invalid_target == "input":
        maya_cmds.setAttr(f"{node}.inputPositionX", math.nan)
    elif invalid_target == "pose":
        maya_cmds.setAttr(f"{node}.pose[0].positionX", math.nan)
    elif invalid_target == "shared_radius":
        maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
        maya_cmds.setAttr(f"{node}.outerRadius", 2.0)
    else:
        maya_cmds.setAttr(f"{node}.pose[0].useRadiusOverride", True)
        maya_cmds.setAttr(f"{node}.pose[0].innerRadiusOverride", 2.0)
        maya_cmds.setAttr(f"{node}.pose[0].outerRadiusOverride", 1.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == expected_status


def test_linear_units_are_converted_consistently(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(linear="m")
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (0.5, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 1.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5, abs=1.0e-12)


def test_transform_translate_parent_connects_directly(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    driver = maya_cmds.createNode("transform")
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 0, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 1.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
    maya_cmds.connectAttr(f"{driver}.translate", f"{node}.inputPosition")

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    maya_cmds.setAttr(f"{driver}.translateX", 10.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_removed_pose_removes_matching_output_element(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 10, (10.0, 0.0, 0.0))
    assert maya_cmds.getAttr(f"{node}.outputWeight", multiIndices=True) == [
        2,
        10,
    ]

    maya_cmds.removeMultiInstance(f"{node}.pose[10]", b=True)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.outputWeight", multiIndices=True) == [2]


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdRbf_PositionFalloffWeight")
        _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
        maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
        maya_cmds.setAttr(f"{node}.outerRadius", 10.0)
        assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)

        _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
        maya_cmds.setAttr(f"{node}.outerRadius", 18.0)
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.5)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_creation_and_pose_blend_parent_connection(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_position_falloff_weight import (
        BdRbfPositionFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_PositionFalloffWeight(
        name="rbf_position_falloff_weight"
    )
    blend = nodes.create.bdRbf_PoseBlend(name="rbf_position_falloff_blend")
    weight.pose[2].position.set((0.0, 0.0, 0.0))
    weight.pose[8].position.set((10.0, 0.0, 0.0))
    weight.inputPosition.set((10.0, 0.0, 0.0))
    weight.innerRadius.set(1.0)
    weight.outerRadius.set(10.0)
    blend.pose[2].translate.set((0.0, 0.0, 0.0))
    blend.pose[8].translate.set((0.0, 5.0, 0.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfPositionFalloffWeight)
    assert weight.outputWeight[8].get() == pytest.approx(1.0)
    assert blend.outputTranslate.get() == pytest.approx((0.0, 5.0, 0.0))
    assert isinstance(
        nodes.existing.bdRbf_PositionFalloffWeight(weight.name),
        BdRbfPositionFalloffWeight,
    )


def test_scene_round_trip_preserves_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_PositionFalloffWeight",
        name="saved_falloff",
    )
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 8, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 2.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 12.0)
    maya_cmds.setAttr(f"{node}.falloff", 1)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].innerRadiusOverride", 3.0)
    maya_cmds.setAttr(f"{node}.pose[8].outerRadiusOverride", 8.0)
    _set_input(maya_cmds, node, (10.0, 0.0, 0.0))

    scene_path = tmp_path / "rbf_position_falloff_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr("saved_falloff.innerRadius") == pytest.approx(2.0)
    assert maya_cmds.getAttr("saved_falloff.outerRadius") == pytest.approx(
        12.0
    )
    assert maya_cmds.getAttr("saved_falloff.falloff") == 1
    assert maya_cmds.getAttr("saved_falloff.pose[8].useRadiusOverride") is True
    assert maya_cmds.getAttr(
        "saved_falloff.pose[8].innerRadiusOverride"
    ) == pytest.approx(3.0)
    assert maya_cmds.getAttr(
        "saved_falloff.pose[8].outerRadiusOverride"
    ) == pytest.approx(8.0)
    assert maya_cmds.getAttr("saved_falloff.outputWeight[2]") == pytest.approx(
        0.0
    )
    assert maya_cmds.getAttr("saved_falloff.outputWeight[8]") == pytest.approx(
        1.0
    )
