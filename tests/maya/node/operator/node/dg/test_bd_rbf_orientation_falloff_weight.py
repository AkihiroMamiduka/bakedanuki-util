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


def _axis_quaternion(
    axis: str,
    degrees: float,
) -> tuple[float, float, float, float]:
    half_angle = math.radians(degrees) * 0.5
    sine = math.sin(half_angle)
    xyz = {
        "x": (sine, 0.0, 0.0),
        "y": (0.0, sine, 0.0),
        "z": (0.0, 0.0, sine),
    }[axis]
    return (*xyz, math.cos(half_angle))


def _set_quaternion(maya_cmds, plug: str, quaternion) -> None:
    maya_cmds.setAttr(plug, *quaternion, type="double4")


def _set_pose(maya_cmds, node: str, index: int, quaternion) -> None:
    _set_quaternion(
        maya_cmds,
        f"{node}.pose[{index}].poseQuat",
        quaternion,
    )


def _weight(maya_cmds, node: str, index: int) -> float:
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142717
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "poseQuat",
        "enabled",
        "useRadiusOverride",
        "innerRadiusOverride",
        "outerRadiusOverride",
    ]
    assert maya_cmds.attributeQuery(
        "poseQuat", node=node, listChildren=True
    ) == ["poseQuatX", "poseQuatY", "poseQuatZ", "poseQuatW"]
    assert maya_cmds.getAttr(f"{node}.innerRadius", type=True) == (
        "doubleAngle"
    )
    assert maya_cmds.attributeQuery("falloff", node=node, listEnum=True) == [
        "Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "falloffStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidQuaternion:"
        "UnsupportedFalloff:NumericalFailure"
    ]
    assert maya_cmds.getAttr(f"{node}.inputQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.innerRadius") == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.outerRadius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 1


def test_pose_defaults_to_enabled_but_uninitialized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")

    assert maya_cmds.getAttr(f"{node}.pose[3].poseQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert maya_cmds.getAttr(f"{node}.pose[3].useRadiusOverride") is False
    assert maya_cmds.getAttr(
        f"{node}.pose[3].outerRadiusOverride"
    ) == pytest.approx(60.0)
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 3


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
def test_falloff_formulas_use_quaternion_angular_distance(
    maya_cmds,
    falloff,
    expected,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 0, _axis_quaternion("x", 0.0))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _axis_quaternion("x", 30.0),
    )
    maya_cmds.setAttr(f"{node}.innerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 90.0)
    maya_cmds.setAttr(f"{node}.falloff", falloff)

    assert _weight(maya_cmds, node, 0) == pytest.approx(expected, abs=1.0e-12)


def test_quaternion_sign_and_scale_represent_the_same_rotation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    pose = _axis_quaternion("y", 70.0)
    _set_pose(maya_cmds, node, 0, pose)
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        tuple(-3.0 * value for value in pose),
    )

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_inner_plateau_and_outer_boundary(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 0, _axis_quaternion("z", 0.0))
    maya_cmds.setAttr(f"{node}.innerRadius", 20.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 80.0)

    for angle in (0.0, 20.0):
        _set_quaternion(
            maya_cmds,
            f"{node}.inputQuat",
            _axis_quaternion("z", angle),
        )
        assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)

    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _axis_quaternion("z", 80.0),
    )
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)


def test_pose_radius_override_is_individual_and_not_normalized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    identity = _axis_quaternion("x", 0.0)
    _set_pose(maya_cmds, node, 2, identity)
    _set_pose(maya_cmds, node, 8, identity)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.innerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 60.0)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].innerRadiusOverride", 30.0)
    maya_cmds.setAttr(f"{node}.pose[8].outerRadiusOverride", 90.0)
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _axis_quaternion("x", 30.0),
    )

    assert _weight(maya_cmds, node, 2) == pytest.approx(0.5)
    assert _weight(maya_cmds, node, 8) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 2) + _weight(
        maya_cmds, node, 8
    ) == pytest.approx(1.5)


def test_disabled_pose_ignores_invalid_quaternion_and_override(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 2, _axis_quaternion("x", 0.0))
    maya_cmds.getAttr(f"{node}.pose[9].poseQuat")
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)
    maya_cmds.setAttr(f"{node}.pose[9].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[9].innerRadiusOverride", 90.0)
    maya_cmds.setAttr(f"{node}.pose[9].outerRadiusOverride", 60.0)

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
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 0, _axis_quaternion("x", 0.0))

    if invalid_target == "input":
        maya_cmds.setAttr(f"{node}.inputQuatX", math.nan)
    elif invalid_target == "pose":
        maya_cmds.setAttr(f"{node}.pose[0].poseQuatW", math.nan)
    elif invalid_target == "shared_radius":
        maya_cmds.setAttr(f"{node}.innerRadius", 60.0)
        maya_cmds.setAttr(f"{node}.outerRadius", 60.0)
    else:
        maya_cmds.setAttr(f"{node}.pose[0].useRadiusOverride", True)
        maya_cmds.setAttr(f"{node}.pose[0].innerRadiusOverride", 90.0)
        maya_cmds.setAttr(f"{node}.pose[0].outerRadiusOverride", 60.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == expected_status


def test_angle_units_are_converted_consistently(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(angle="radian")
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 0, _axis_quaternion("x", 0.0))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _axis_quaternion("x", 45.0),
    )
    maya_cmds.setAttr(f"{node}.outerRadius", math.pi / 2.0)
    maya_cmds.setAttr(f"{node}.falloff", 0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5)


def test_quaternion_parent_connection_updates_weight(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 0, _axis_quaternion("x", 45.0))
    maya_cmds.connectAttr(f"{compose}.outputQuat", f"{node}.inputQuat")

    maya_cmds.setAttr(f"{compose}.inputTwist", 45.0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_removed_pose_removes_matching_output_element(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    _set_pose(maya_cmds, node, 2, _axis_quaternion("x", 0.0))
    _set_pose(maya_cmds, node, 10, _axis_quaternion("x", 30.0))
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
        node = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
        _set_pose(maya_cmds, node, 0, _axis_quaternion("x", 0.0))
        maya_cmds.setAttr(f"{node}.innerRadius", 10.0)
        maya_cmds.setAttr(f"{node}.outerRadius", 50.0)
        maya_cmds.setAttr(f"{node}.falloff", 0)
        _set_quaternion(
            maya_cmds,
            f"{node}.inputQuat",
            _axis_quaternion("x", 30.0),
        )
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.5)

        maya_cmds.setAttr(f"{node}.outerRadius", 90.0)
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.75)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_pose_blend_parent_connection(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    weight = maya_cmds.createNode("bdRbf_OrientationFalloffWeight")
    blend = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_pose(maya_cmds, weight, 8, _axis_quaternion("x", 45.0))
    _set_quaternion(
        maya_cmds,
        f"{weight}.inputQuat",
        _axis_quaternion("x", 45.0),
    )
    maya_cmds.setAttr(f"{blend}.pose[8].translateY", 5.0)
    maya_cmds.connectAttr(f"{weight}.outputWeight", f"{blend}.weight")

    assert maya_cmds.getAttr(f"{blend}.outputTranslateY") == pytest.approx(5.0)


def test_node_operator_creation_and_parent_connection(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_orientation_falloff_weight import (
        BdRbfOrientationFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_OrientationFalloffWeight(
        name="rbf_orientation_falloff_weight"
    )
    blend = nodes.create.bdRbf_PoseBlend(name="rbf_orientation_falloff_blend")
    pose = _axis_quaternion("x", 45.0)
    weight.pose[8].poseQuat.set(pose)
    weight.inputQuat.set(pose)
    blend.pose[8].translate.set((0.0, 5.0, 0.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfOrientationFalloffWeight)
    assert weight.outputWeight[8].get() == pytest.approx(1.0)
    assert blend.outputTranslate.get() == pytest.approx((0.0, 5.0, 0.0))
    assert isinstance(
        nodes.existing.bdRbf_OrientationFalloffWeight(weight.name),
        BdRbfOrientationFalloffWeight,
    )


def test_scene_round_trip_preserves_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_OrientationFalloffWeight",
        name="saved_orientation_falloff",
    )
    _set_pose(maya_cmds, node, 8, _axis_quaternion("y", 45.0))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _axis_quaternion("y", 45.0),
    )
    maya_cmds.setAttr(f"{node}.innerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.outerRadius", 80.0)
    maya_cmds.setAttr(f"{node}.falloff", 1)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].innerRadiusOverride", 20.0)
    maya_cmds.setAttr(f"{node}.pose[8].outerRadiusOverride", 70.0)

    scene_path = tmp_path / "rbf_orientation_falloff_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(
        "saved_orientation_falloff.innerRadius"
    ) == pytest.approx(10.0)
    assert maya_cmds.getAttr(
        "saved_orientation_falloff.outerRadius"
    ) == pytest.approx(80.0)
    assert maya_cmds.getAttr("saved_orientation_falloff.falloff") == 1
    assert (
        maya_cmds.getAttr(
            "saved_orientation_falloff.pose[8].useRadiusOverride"
        )
        is True
    )
    assert maya_cmds.getAttr(
        "saved_orientation_falloff.outputWeight[8]"
    ) == pytest.approx(1.0)
