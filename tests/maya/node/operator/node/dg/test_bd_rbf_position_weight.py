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
    node = maya_cmds.createNode("bdRbf_PositionWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142715
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "position",
        "enabled",
    ]
    assert maya_cmds.attributeQuery(
        "position", node=node, listChildren=True
    ) == ["positionX", "positionY", "positionZ"]
    assert maya_cmds.getAttr(f"{node}.inputPositionX", type=True) == (
        "doubleLinear"
    )
    assert (
        maya_cmds.attributeQuery("positionX", node=node, attributeType=True)
        == "doubleLinear"
    )
    assert maya_cmds.getAttr(f"{node}.radius", type=True) == "doubleLinear"
    assert maya_cmds.attributeQuery("kernel", node=node, listEnum=True) == [
        "Gaussian:Exponential:Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "solveStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidRegularization:"
        "InvalidPosition:DuplicatePose:RankDeficient:"
        "NumericalFailure:UnsupportedKernel"
    ]
    assert maya_cmds.getAttr(f"{node}.inputPosition")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.radius") == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.kernel") == 4
    assert maya_cmds.getAttr(f"{node}.regularization") == pytest.approx(1.0e-8)
    assert maya_cmds.getAttr(f"{node}.allowNegativeWeights") is False
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 1


def test_pose_defaults_to_enabled_origin(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")

    assert maya_cmds.getAttr(f"{node}.pose[3].position")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 0


def test_sparse_pose_indexes_interpolate_at_pose_centers(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 10, (10.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0, abs=2.0e-8)
    assert _weight(maya_cmds, node, 10) == pytest.approx(0.0, abs=1.0e-12)
    assert maya_cmds.getAttr(f"{node}.outputWeight", multiIndices=True) == [
        2,
        10,
    ]

    _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 2) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 10) == pytest.approx(1.0, abs=2.0e-8)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 0


def test_distance_is_three_dimensional_euclidean_length(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (3.0, 4.0, 12.0))
    maya_cmds.setAttr(f"{node}.kernel", 1)
    maya_cmds.setAttr(f"{node}.radius", 52.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(
        math.exp(-0.25), abs=1.0e-12
    )


@pytest.mark.parametrize(
    ("kernel", "expected"),
    (
        (0, math.exp(-(0.25**2))),
        (1, math.exp(-0.25)),
        (2, 0.75),
        (3, 1.0 - 3.0 * 0.25**2 + 2.0 * 0.25**3),
        (
            4,
            1.0 - 10.0 * 0.25**3 + 15.0 * 0.25**4 - 6.0 * 0.25**5,
        ),
    ),
)
def test_kernel_formulas_use_distance_over_radius(
    maya_cmds,
    kernel,
    expected,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (2.5, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.kernel", kernel)
    maya_cmds.setAttr(f"{node}.radius", 10.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(expected, abs=1.0e-12)


def test_linear_units_are_converted_consistently(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(linear="m")
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 1, (1.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (0.5, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.radius", 1.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5, abs=1.0e-12)
    assert _weight(maya_cmds, node, 1) == pytest.approx(0.5, abs=1.0e-12)


def test_transform_translate_parent_connects_directly(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    driver = maya_cmds.createNode("transform")
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 1, (10.0, 0.0, 0.0))
    maya_cmds.connectAttr(f"{driver}.translate", f"{node}.inputPosition")

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0, abs=2.0e-8)
    maya_cmds.setAttr(f"{driver}.translateX", 10.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0, abs=2.0e-8)


def test_disabled_pose_keeps_its_output_index_at_zero(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 9, (0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_duplicate_position_reports_status_and_zeroes_outputs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (1.0, 2.0, 3.0))
    _set_pose(maya_cmds, node, 4, (1.0, 2.0, 3.0))

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert _weight(maya_cmds, node, 4) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 5


@pytest.mark.parametrize(
    ("invalid_target", "expected_status"),
    (("input", 4), ("pose", 4), ("radius", 2)),
)
def test_invalid_input_reports_status_and_zeroes_outputs(
    maya_cmds,
    invalid_target,
    expected_status,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))

    if invalid_target == "input":
        maya_cmds.setAttr(f"{node}.inputPositionX", math.nan)
    elif invalid_target == "pose":
        maya_cmds.setAttr(f"{node}.pose[0].positionX", math.nan)
    else:
        maya_cmds.setAttr(f"{node}.radius", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == expected_status


def test_negative_weight_clamping_is_optional(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 1, (10.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (20.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 10.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)
    maya_cmds.setAttr(f"{node}.allowNegativeWeights", True)

    assert _weight(maya_cmds, node, 0) < 0.0
    positive_weight = _weight(maya_cmds, node, 1)
    assert positive_weight > 0.0

    maya_cmds.setAttr(f"{node}.allowNegativeWeights", False)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert _weight(maya_cmds, node, 1) == pytest.approx(positive_weight)


def test_factorization_cache_invalidates_for_every_configuration_input(
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 1, (10.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 10.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)

    _set_pose(maya_cmds, node, 1, (6.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (6.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)

    maya_cmds.setAttr(f"{node}.pose[1].enabled", False)
    _set_input(maya_cmds, node, (2.5, 0.0, 0.0))
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-(0.25**2)))
    assert _weight(maya_cmds, node, 1) == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node}.kernel", 1)
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-0.25))

    maya_cmds.setAttr(f"{node}.radius", 5.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-0.5))

    maya_cmds.setAttr(f"{node}.regularization", 1.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5 * math.exp(-0.5))


def test_removed_pose_removes_matching_output_element(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 10, (10.0, 0.0, 0.0))
    assert _weight(maya_cmds, node, 10) == pytest.approx(0.0, abs=1.0e-12)

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
        node = maya_cmds.createNode("bdRbf_PositionWeight")
        _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0))
        _set_pose(maya_cmds, node, 1, (10.0, 0.0, 0.0))
        assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)

        _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
        assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_creation_and_pose_blend_parent_connection(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_position_weight import (
        BdRbfPositionWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_PositionWeight(name="rbf_position_weight")
    blend = nodes.create.bdRbf_PoseBlend(name="rbf_position_blend")
    weight.pose[2].position.set((0.0, 0.0, 0.0))
    weight.pose[8].position.set((10.0, 0.0, 0.0))
    weight.inputPosition.set((10.0, 0.0, 0.0))
    blend.pose[2].translate.set((0.0, 0.0, 0.0))
    blend.pose[8].translate.set((0.0, 5.0, 0.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfPositionWeight)
    assert weight.outputWeight[8].get() == pytest.approx(1.0, abs=2.0e-8)
    assert blend.outputTranslate.get() == pytest.approx((0.0, 5.0, 0.0))
    assert isinstance(
        nodes.existing.bdRbf_PositionWeight(weight.name),
        BdRbfPositionWeight,
    )


def test_scene_round_trip_preserves_pose_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PositionWeight", name="saved_rbf")
    _set_pose(maya_cmds, node, 2, (0.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 8, (10.0, 0.0, 0.0))
    _set_input(maya_cmds, node, (10.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.kernel", 1)
    maya_cmds.setAttr(f"{node}.radius", 20.0)

    scene_path = tmp_path / "rbf_position_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr("saved_rbf.kernel") == 1
    assert maya_cmds.getAttr("saved_rbf.radius") == pytest.approx(20.0)
    assert maya_cmds.getAttr("saved_rbf.pose[2].enabled") is True
    assert maya_cmds.getAttr("saved_rbf.outputWeight", multiIndices=True) == [
        2,
        8,
    ]
    assert maya_cmds.getAttr("saved_rbf.outputWeight[2]") == pytest.approx(
        0.0, abs=2.0e-8
    )
    assert maya_cmds.getAttr("saved_rbf.outputWeight[8]") == pytest.approx(
        1.0, abs=2.0e-8
    )
