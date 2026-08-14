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
    maya_cmds.currentUnit(angle="degree")
    return plugin_path


def _axis_x_quaternion(degrees: float) -> tuple[float, float, float, float]:
    half_angle = math.radians(degrees) * 0.5
    return (math.sin(half_angle), 0.0, 0.0, math.cos(half_angle))


def _set_pose(maya_cmds, node: str, index: int, quaternion) -> None:
    maya_cmds.setAttr(
        f"{node}.pose[{index}].poseQuat",
        *quaternion,
        type="double4",
    )


def _weight(maya_cmds, node: str, index: int) -> float:
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142713
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "poseQuat",
        "enabled",
    ]
    assert maya_cmds.attributeQuery(
        "poseQuat", node=node, listChildren=True
    ) == ["poseQuatX", "poseQuatY", "poseQuatZ", "poseQuatW"]
    assert maya_cmds.attributeQuery("kernel", node=node, listEnum=True) == [
        "Gaussian:Exponential:Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "solveStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidRegularization:"
        "InvalidQuaternion:DuplicatePose:RankDeficient:"
        "NumericalFailure:UnsupportedKernel"
    ]
    assert maya_cmds.getAttr(f"{node}.inputQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.radius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.kernel") == 4
    assert maya_cmds.getAttr(f"{node}.regularization") == pytest.approx(1.0e-8)
    assert maya_cmds.getAttr(f"{node}.allowNegativeWeights") is False
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 1


def test_pose_defaults_are_enabled_but_uninitialized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")

    assert maya_cmds.getAttr(f"{node}.pose[3].poseQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 4


def test_sparse_pose_indexes_interpolate_at_pose_centers(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    identity = _axis_x_quaternion(0.0)
    quarter_turn = _axis_x_quaternion(90.0)

    _set_pose(maya_cmds, node, 10, quarter_turn)
    _set_pose(maya_cmds, node, 2, identity)

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0, abs=2.0e-8)
    assert _weight(maya_cmds, node, 10) == pytest.approx(0.0, abs=1.0e-12)
    assert maya_cmds.getAttr(f"{node}.outputWeight", multiIndices=True) == [
        2,
        10,
    ]

    maya_cmds.setAttr(f"{node}.inputQuat", *quarter_turn, type="double4")
    assert _weight(maya_cmds, node, 2) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 10) == pytest.approx(1.0, abs=2.0e-8)
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 0


def test_quaternion_sign_represents_the_same_rotation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    identity = _axis_x_quaternion(0.0)
    quarter_turn = _axis_x_quaternion(90.0)
    _set_pose(maya_cmds, node, 0, identity)
    _set_pose(maya_cmds, node, 1, quarter_turn)

    maya_cmds.setAttr(
        f"{node}.inputQuat",
        *(-value for value in quarter_turn),
        type="double4",
    )
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0, abs=2.0e-8)


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
def test_kernel_formulas_use_angular_distance_over_radius(
    maya_cmds,
    kernel,
    expected,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    _set_pose(maya_cmds, node, 0, _axis_x_quaternion(0.0))
    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(22.5), type="double4"
    )
    maya_cmds.setAttr(f"{node}.kernel", kernel)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(expected, abs=1.0e-12)


def test_disabled_pose_keeps_its_output_index_at_zero(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    identity = _axis_x_quaternion(0.0)
    _set_pose(maya_cmds, node, 2, identity)
    _set_pose(maya_cmds, node, 9, identity)
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_duplicate_rotation_reports_status_and_zeroes_outputs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    quaternion = _axis_x_quaternion(35.0)
    _set_pose(maya_cmds, node, 0, quaternion)
    _set_pose(maya_cmds, node, 4, tuple(-value for value in quaternion))

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
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    _set_pose(maya_cmds, node, 0, _axis_x_quaternion(0.0))

    if invalid_target == "input":
        maya_cmds.setAttr(
            f"{node}.inputQuat", 0.0, 0.0, 0.0, 0.0, type="double4"
        )
    elif invalid_target == "pose":
        _set_pose(maya_cmds, node, 0, (0.0, 0.0, 0.0, 0.0))
    else:
        maya_cmds.setAttr(f"{node}.radius", 0.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == expected_status


def test_negative_weight_clamping_is_optional(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    _set_pose(maya_cmds, node, 0, _axis_x_quaternion(0.0))
    _set_pose(maya_cmds, node, 1, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)
    maya_cmds.setAttr(f"{node}.allowNegativeWeights", True)
    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(180.0), type="double4"
    )

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
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    _set_pose(maya_cmds, node, 0, _axis_x_quaternion(0.0))
    _set_pose(maya_cmds, node, 1, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(90.0), type="double4"
    )
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)

    _set_pose(maya_cmds, node, 1, _axis_x_quaternion(60.0))
    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(60.0), type="double4"
    )
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)

    maya_cmds.setAttr(f"{node}.pose[1].enabled", False)
    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(22.5), type="double4"
    )
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-(0.25**2)))
    assert _weight(maya_cmds, node, 1) == pytest.approx(0.0)

    maya_cmds.setAttr(f"{node}.kernel", 1)
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-0.25))

    maya_cmds.setAttr(f"{node}.radius", 45.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(math.exp(-0.5))

    maya_cmds.setAttr(f"{node}.regularization", 1.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5 * math.exp(-0.5))


def test_removed_pose_removes_matching_output_element(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight")
    _set_pose(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_pose(maya_cmds, node, 10, _axis_x_quaternion(90.0))
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
        node = maya_cmds.createNode("bdRbf_OrientationWeight")
        _set_pose(maya_cmds, node, 0, _axis_x_quaternion(0.0))
        _set_pose(maya_cmds, node, 1, _axis_x_quaternion(90.0))
        assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)

        maya_cmds.setAttr(
            f"{node}.inputQuat", *_axis_x_quaternion(90.0), type="double4"
        )
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.0, abs=1.0e-12)
        assert _weight(maya_cmds, node, 1) == pytest.approx(1.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_creation_and_existing_access(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_orientation_weight import (
        BdRbfOrientationWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdRbf_OrientationWeight(name="rbf_orientation_weight")
    node.pose[2].poseQuat.set(_axis_x_quaternion(0.0))
    node.pose[8].poseQuat.set(_axis_x_quaternion(90.0))
    node.kernel.set(node.kernel.GAUSSIAN)
    modifier_manager.do_it_dg()

    assert isinstance(node, BdRbfOrientationWeight)
    assert node.outputWeight[2].get() == pytest.approx(1.0)
    assert node.outputWeight[8].get() == pytest.approx(0.0, abs=2.0e-8)
    assert isinstance(
        nodes.existing.bdRbf_OrientationWeight(node.name),
        BdRbfOrientationWeight,
    )


def test_scene_round_trip_preserves_pose_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationWeight", name="saved_rbf")
    _set_pose(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_pose(maya_cmds, node, 8, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(
        f"{node}.inputQuat", *_axis_x_quaternion(90.0), type="double4"
    )
    maya_cmds.setAttr(f"{node}.kernel", 1)
    maya_cmds.setAttr(f"{node}.radius", 120.0)

    scene_path = tmp_path / "rbf_orientation_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr("saved_rbf.kernel") == 1
    assert maya_cmds.getAttr("saved_rbf.radius") == pytest.approx(120.0)
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
