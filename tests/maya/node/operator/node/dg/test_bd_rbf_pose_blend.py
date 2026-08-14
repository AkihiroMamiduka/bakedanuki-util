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


def _set_pose(
    maya_cmds,
    node: str,
    index: int,
    *,
    translate=(0.0, 0.0, 0.0),
    rotate=(0.0, 0.0, 0.0),
    scale=(1.0, 1.0, 1.0),
) -> None:
    maya_cmds.setAttr(
        f"{node}.pose[{index}].translate",
        *translate,
        type="double3",
    )
    maya_cmds.setAttr(
        f"{node}.pose[{index}].rotate",
        *rotate,
        type="double3",
    )
    maya_cmds.setAttr(
        f"{node}.pose[{index}].scale",
        *scale,
        type="double3",
    )


def _get_triple(maya_cmds, plug: str) -> tuple[float, float, float]:
    return maya_cmds.getAttr(plug)[0]


def _get_quaternion(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return maya_cmds.getAttr(plug)[0]


def _quaternion_from_euler(
    maya_om,
    degrees: tuple[float, float, float],
    rotate_order: int = 0,
) -> tuple[float, float, float, float]:
    quaternion = maya_om.MEulerRotation(
        *(math.radians(value) for value in degrees),
        rotate_order,
    ).asQuaternion()
    return quaternion.x, quaternion.y, quaternion.z, quaternion.w


def _assert_same_rotation(actual, expected, *, abs_tolerance=1.0e-10):
    dot = abs(sum(left * right for left, right in zip(actual, expected)))
    assert dot == pytest.approx(1.0, abs=abs_tolerance)


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142714
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "translate",
        "rotate",
        "scale",
        "enabled",
    ]
    assert maya_cmds.attributeQuery("weight", node=node, multi=True)
    assert (
        maya_cmds.getAttr(f"{node}.baseTranslateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{node}.pose[0].translateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{node}.outputTranslateX", type=True)
        == "doubleLinear"
    )
    assert maya_cmds.attributeQuery(
        "blendStatus", node=node, listEnum=True
    ) == [
        "Success:InvalidWeight:InvalidTranslate:InvalidRotate:InvalidScale:"
        "UnsupportedRotateOrder:NumericalFailure"
    ]
    assert _get_triple(maya_cmds, f"{node}.baseTranslate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert _get_triple(maya_cmds, f"{node}.baseRotate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert _get_triple(maya_cmds, f"{node}.baseScale") == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert maya_cmds.getAttr(f"{node}.rotateOrder") == 0
    assert maya_cmds.getAttr(f"{node}.isValid") is True
    assert maya_cmds.getAttr(f"{node}.blendStatus") == 0


def test_no_matching_pose_returns_base_values(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    maya_cmds.setAttr(f"{node}.baseTranslate", 4.0, -2.0, 7.0, type="double3")
    maya_cmds.setAttr(f"{node}.baseRotate", 15.0, 25.0, -35.0, type="double3")
    maya_cmds.setAttr(f"{node}.baseScale", 1.5, 0.75, 2.0, type="double3")
    maya_cmds.setAttr(f"{node}.weight[9]", 1.0)

    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (4.0, -2.0, 7.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputScale") == pytest.approx(
        (1.5, 0.75, 2.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputRotate") == pytest.approx(
        (15.0, 25.0, -35.0)
    )
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_half_weight_blends_translate_rotate_and_scale(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(
        maya_cmds,
        node,
        2,
        translate=(10.0, 4.0, -2.0),
        rotate=(90.0, 0.0, 0.0),
        scale=(2.0, 3.0, 4.0),
    )
    maya_cmds.setAttr(f"{node}.weight[2]", 0.5)

    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (5.0, 2.0, -1.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputRotate") == pytest.approx(
        (45.0, 0.0, 0.0),
        abs=1.0e-10,
    )
    assert _get_triple(maya_cmds, f"{node}.outputScale") == pytest.approx(
        (1.5, 2.0, 2.5)
    )


def test_negative_weight_extrapolates_from_base(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(
        maya_cmds,
        node,
        0,
        translate=(10.0, 0.0, 0.0),
        rotate=(90.0, 0.0, 0.0),
        scale=(2.0, 2.0, 2.0),
    )
    maya_cmds.setAttr(f"{node}.weight[0]", -0.5)

    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (-5.0, 0.0, 0.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputRotate") == pytest.approx(
        (-45.0, 0.0, 0.0), abs=1.0e-10
    )
    assert _get_triple(maya_cmds, f"{node}.outputScale") == pytest.approx(
        (0.5, 0.5, 0.5)
    )


def test_weight_one_reaches_pose_from_non_identity_base(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    base_rotate = (20.0, -15.0, 10.0)
    pose_rotate = (-30.0, 40.0, 25.0)
    maya_cmds.setAttr(f"{node}.rotateOrder", 4)
    maya_cmds.setAttr(f"{node}.baseTranslate", 2.0, 3.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{node}.baseRotate", *base_rotate, type="double3")
    maya_cmds.setAttr(f"{node}.baseScale", 1.5, 2.0, 0.5, type="double3")
    _set_pose(
        maya_cmds,
        node,
        7,
        translate=(-5.0, 8.0, 1.0),
        rotate=pose_rotate,
        scale=(0.75, 1.25, 3.0),
    )
    maya_cmds.setAttr(f"{node}.weight[7]", 1.0)

    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (-5.0, 8.0, 1.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputScale") == pytest.approx(
        (0.75, 1.25, 3.0)
    )
    _assert_same_rotation(
        _get_quaternion(maya_cmds, f"{node}.outputQuat"),
        _quaternion_from_euler(maya_om, pose_rotate, 4),
    )


def test_multiple_rotations_are_accumulated_in_log_space(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, node, 8, rotate=(-90.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 2, rotate=(90.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.weight[8]", 0.25)
    maya_cmds.setAttr(f"{node}.weight[2]", 0.5)

    _assert_same_rotation(
        _get_quaternion(maya_cmds, f"{node}.outputQuat"),
        _quaternion_from_euler(maya_om, (22.5, 0.0, 0.0)),
    )


def test_rotation_uses_shortest_path_and_deterministic_half_turn(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, node, 0, rotate=(270.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.weight[0]", 0.5)
    _assert_same_rotation(
        _get_quaternion(maya_cmds, f"{node}.outputQuat"),
        _quaternion_from_euler(maya_om, (-45.0, 0.0, 0.0)),
    )

    positive = maya_cmds.createNode("bdRbf_PoseBlend")
    negative = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, positive, 0, rotate=(180.0, 0.0, 0.0))
    _set_pose(maya_cmds, negative, 0, rotate=(-180.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{positive}.weight[0]", 0.5)
    maya_cmds.setAttr(f"{negative}.weight[0]", 0.5)
    _assert_same_rotation(
        _get_quaternion(maya_cmds, f"{positive}.outputQuat"),
        _get_quaternion(maya_cmds, f"{negative}.outputQuat"),
    )


def test_disabled_and_unmatched_pose_indexes_are_ignored(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, node, 2, translate=(10.0, 0.0, 0.0))
    _set_pose(maya_cmds, node, 8, translate=(20.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[2].enabled", False)
    maya_cmds.setAttr(f"{node}.weight[2]", 1.0)
    maya_cmds.setAttr(f"{node}.weight[99]", 1.0)

    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    maya_cmds.setAttr(f"{node}.pose[2].enabled", True)
    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (10.0, 0.0, 0.0)
    )


def test_rbf_weight_parent_connection_preserves_sparse_indexes(
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)
    weight_node = maya_cmds.createNode("bdRbf_OrientationWeight")
    blend_node = maya_cmds.createNode("bdRbf_PoseBlend")
    identity = (0.0, 0.0, 0.0, 1.0)
    quarter_turn = _quaternion_from_euler(maya_om, (90.0, 0.0, 0.0))
    maya_cmds.setAttr(
        f"{weight_node}.pose[2].poseQuat", *identity, type="double4"
    )
    maya_cmds.setAttr(
        f"{weight_node}.pose[8].poseQuat", *quarter_turn, type="double4"
    )
    maya_cmds.setAttr(
        f"{weight_node}.inputQuat", *quarter_turn, type="double4"
    )
    _set_pose(maya_cmds, blend_node, 2)
    _set_pose(
        maya_cmds,
        blend_node,
        8,
        translate=(1.0, 2.0, 3.0),
        rotate=(90.0, 0.0, 0.0),
        scale=(2.0, 1.5, 0.5),
    )
    maya_cmds.connectAttr(
        f"{weight_node}.outputWeight",
        f"{blend_node}.weight",
    )

    assert (
        maya_cmds.connectionInfo(
            f"{blend_node}.weight", sourceFromDestination=True
        )
        == f"{weight_node}.outputWeight"
    )
    assert maya_cmds.getAttr(f"{blend_node}.weight", multiIndices=True) == [
        2,
        8,
    ]
    assert _get_triple(
        maya_cmds, f"{blend_node}.outputTranslate"
    ) == pytest.approx((1.0, 2.0, 3.0), abs=1.0e-7)
    assert _get_triple(
        maya_cmds, f"{blend_node}.outputScale"
    ) == pytest.approx((2.0, 1.5, 0.5), abs=2.0e-8)
    _assert_same_rotation(
        _get_quaternion(maya_cmds, f"{blend_node}.outputQuat"),
        quarter_turn,
        abs_tolerance=2.0e-8,
    )


def test_outputs_connect_directly_to_transform_trs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    blend_node = maya_cmds.createNode("bdRbf_PoseBlend")
    target = maya_cmds.createNode("transform")
    _set_pose(
        maya_cmds,
        blend_node,
        0,
        translate=(2.0, 3.0, 4.0),
        rotate=(45.0, 0.0, 0.0),
        scale=(1.5, 2.0, 0.75),
    )
    maya_cmds.setAttr(f"{blend_node}.weight[0]", 1.0)
    maya_cmds.connectAttr(
        f"{blend_node}.outputTranslate",
        f"{target}.translate",
    )
    maya_cmds.connectAttr(f"{blend_node}.outputRotate", f"{target}.rotate")
    maya_cmds.connectAttr(f"{blend_node}.outputScale", f"{target}.scale")

    assert _get_triple(maya_cmds, f"{target}.translate") == pytest.approx(
        (2.0, 3.0, 4.0)
    )
    assert _get_triple(maya_cmds, f"{target}.rotate") == pytest.approx(
        (45.0, 0.0, 0.0), abs=1.0e-10
    )
    assert _get_triple(maya_cmds, f"{target}.scale") == pytest.approx(
        (1.5, 2.0, 0.75)
    )


@pytest.mark.parametrize(
    ("invalid_target", "expected_status"),
    (
        ("weight", 1),
        ("translate", 2),
        ("rotate", 3),
        ("scale", 4),
    ),
)
def test_invalid_values_report_status_and_return_base(
    maya_cmds,
    invalid_target,
    expected_status,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    maya_cmds.setAttr(f"{node}.baseTranslate", 2.0, 3.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{node}.baseScale", 1.5, 2.0, 0.5, type="double3")
    _set_pose(maya_cmds, node, 0, translate=(5.0, 6.0, 7.0))
    maya_cmds.setAttr(f"{node}.weight[0]", 1.0)

    if invalid_target == "weight":
        maya_cmds.setAttr(f"{node}.weight[0]", float("nan"))
    elif invalid_target == "translate":
        maya_cmds.setAttr(f"{node}.pose[0].translateX", float("nan"))
    elif invalid_target == "rotate":
        maya_cmds.setAttr(f"{node}.pose[0].rotateX", float("nan"))
    else:
        maya_cmds.setAttr(f"{node}.pose[0].scaleX", float("inf"))

    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.blendStatus") == expected_status
    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (2.0, 3.0, 4.0)
    )
    assert _get_triple(maya_cmds, f"{node}.outputScale") == pytest.approx(
        (1.5, 2.0, 0.5)
    )


def test_numerical_overflow_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, node, 0, translate=(1.0e308, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.weight[0]", 1.0e308)

    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.blendStatus") == 6
    assert _get_triple(maya_cmds, f"{node}.outputTranslate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdRbf_PoseBlend")
        _set_pose(maya_cmds, node, 0, rotate=(90.0, 0.0, 0.0))
        maya_cmds.setAttr(f"{node}.weight[0]", 0.25)
        assert _get_triple(maya_cmds, f"{node}.outputRotate") == pytest.approx(
            (22.5, 0.0, 0.0), abs=1.0e-10
        )

        maya_cmds.setAttr(f"{node}.weight[0]", 0.75)
        assert _get_triple(maya_cmds, f"{node}.outputRotate") == pytest.approx(
            (67.5, 0.0, 0.0), abs=1.0e-10
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_creation_and_parent_weight_connection(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_pose_blend import (
        BdRbfPoseBlend,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight_node = nodes.create.bdRbf_OrientationWeight(name="rbf_weight")
    blend_node = nodes.create.bdRbf_PoseBlend(name="rbf_blend")
    weight_node.pose[2].poseQuat.set((0.0, 0.0, 0.0, 1.0))
    blend_node.pose[2].translate.set((1.0, 2.0, 3.0))
    blend_node.pose[2].rotate.set((45.0, 0.0, 0.0))
    blend_node.pose[2].scale.set((2.0, 1.5, 0.5))
    weight_node.outputWeight.connect(blend_node.weight)
    modifier_manager.do_it_dg()

    assert isinstance(blend_node, BdRbfPoseBlend)
    assert blend_node.outputTranslate.get().as_tuple() == pytest.approx(
        (1.0, 2.0, 3.0), abs=1.0e-7
    )
    assert blend_node.outputRotate.get().as_tuple() == pytest.approx(
        (45.0, 0.0, 0.0), abs=1.0e-6
    )
    assert blend_node.outputScale.get().as_tuple() == pytest.approx(
        (2.0, 1.5, 0.5), abs=2.0e-8
    )
    assert isinstance(blend_node.outputQuat.get(), bdu.Quat)
    assert isinstance(
        nodes.existing.bdRbf_PoseBlend(blend_node.name),
        BdRbfPoseBlend,
    )


def test_scene_round_trip_preserves_parent_connection(
    maya_cmds, maya_om, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    weight_node = maya_cmds.createNode(
        "bdRbf_OrientationWeight", name="saved_weight"
    )
    blend_node = maya_cmds.createNode("bdRbf_PoseBlend", name="saved_blend")
    identity = (0.0, 0.0, 0.0, 1.0)
    quarter_turn = _quaternion_from_euler(maya_om, (90.0, 0.0, 0.0))
    maya_cmds.setAttr(
        f"{weight_node}.pose[2].poseQuat", *identity, type="double4"
    )
    maya_cmds.setAttr(
        f"{weight_node}.pose[8].poseQuat", *quarter_turn, type="double4"
    )
    maya_cmds.setAttr(
        f"{weight_node}.inputQuat", *quarter_turn, type="double4"
    )
    _set_pose(maya_cmds, blend_node, 2)
    _set_pose(maya_cmds, blend_node, 8, translate=(3.0, 4.0, 5.0))
    maya_cmds.connectAttr(
        f"{weight_node}.outputWeight",
        f"{blend_node}.weight",
    )

    scene_path = tmp_path / "rbf_pose_blend.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert (
        maya_cmds.connectionInfo(
            "saved_blend.weight", sourceFromDestination=True
        )
        == "saved_weight.outputWeight"
    )
    assert _get_triple(
        maya_cmds, "saved_blend.outputTranslate"
    ) == pytest.approx((3.0, 4.0, 5.0), abs=1.0e-7)
