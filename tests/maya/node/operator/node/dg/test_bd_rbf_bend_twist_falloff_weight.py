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


def _compose(
    maya_cmds,
    *,
    twist: float = 0.0,
    bend_h: float = 0.0,
    bend_v: float = 0.0,
    order: int = 0,
    axis_quat=(0.0, 0.0, 0.0, 1.0),
) -> tuple[float, float, float, float]:
    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.inputTwist", twist)
    maya_cmds.setAttr(f"{compose}.inputBendH", bend_h)
    maya_cmds.setAttr(f"{compose}.inputBendV", bend_v)
    maya_cmds.setAttr(f"{compose}.order", order)
    _set_quaternion(maya_cmds, f"{compose}.axisQuat", axis_quat)
    return tuple(maya_cmds.getAttr(f"{compose}.outputQuat")[0])


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
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0007F099
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "poseQuat",
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
    assert maya_cmds.attributeQuery("falloff", node=node, listEnum=True) == [
        "Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "falloffStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidQuaternion:"
        "UnsupportedFalloff:UnsupportedMode:UnsupportedOrder:"
        "NumericalFailure"
    ]
    assert maya_cmds.getAttr(f"{node}.inputQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.axisQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.order") == 0
    assert maya_cmds.getAttr(f"{node}.mode") == 0
    for name, expected in (
        ("bendInnerRadius", 0.0),
        ("bendOuterRadius", 60.0),
        ("twistInnerRadius", 0.0),
        ("twistOuterRadius", 60.0),
    ):
        assert maya_cmds.getAttr(f"{node}.{name}") == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{node}.falloff") == 2
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 1


def test_pose_defaults_to_enabled_but_uninitialized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")

    assert maya_cmds.getAttr(f"{node}.pose[3].poseQuat")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{node}.pose[3].enabled") is True
    assert maya_cmds.getAttr(f"{node}.pose[3].useRadiusOverride") is False
    assert maya_cmds.getAttr(
        f"{node}.pose[3].bendOuterRadiusOverride"
    ) == pytest.approx(60.0)
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 3


def test_bend_only_ignores_twist_but_keeps_bend_amount(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(
        maya_cmds,
        node,
        0,
        _compose(maya_cmds, twist=0.0, bend_h=20.0),
    )
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, twist=140.0, bend_h=60.0),
    )
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.bendInnerRadius", 0.0)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 80.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5, abs=1.0e-10)


def test_bend_only_matches_same_bone_direction_with_different_twist(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(
        maya_cmds,
        node,
        0,
        _compose(maya_cmds, twist=-90.0, bend_h=35.0, bend_v=20.0),
    )
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, twist=110.0, bend_h=35.0, bend_v=20.0),
    )
    maya_cmds.setAttr(f"{node}.mode", 1)

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_bend_twist_multiplies_independent_falloffs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 0, _compose(maya_cmds))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, twist=30.0, bend_h=30.0),
    )
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.25, abs=1.0e-10)


def test_twist_uses_shortest_wrapped_angle_difference(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 0, _compose(maya_cmds, twist=170.0))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, twist=-170.0),
    )
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 40.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.5, abs=1.0e-10)


def test_bend_and_twist_inner_plateaus_are_independent(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 0, _compose(maya_cmds))
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, twist=20.0, bend_v=10.0),
    )
    maya_cmds.setAttr(f"{node}.bendInnerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
    maya_cmds.setAttr(f"{node}.twistInnerRadius", 20.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_pose_radius_override_is_individual_and_not_normalized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    identity = _compose(maya_cmds)
    _set_pose(maya_cmds, node, 2, identity)
    _set_pose(maya_cmds, node, 8, identity)
    _set_quaternion(
        maya_cmds,
        f"{node}.inputQuat",
        _compose(maya_cmds, bend_h=30.0),
    )
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.falloff", 0)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].bendInnerRadiusOverride", 30.0)
    maya_cmds.setAttr(f"{node}.pose[8].bendOuterRadiusOverride", 90.0)

    assert _weight(maya_cmds, node, 2) == pytest.approx(0.5, abs=1.0e-10)
    assert _weight(maya_cmds, node, 8) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 2) + _weight(
        maya_cmds, node, 8
    ) == pytest.approx(1.5, abs=1.0e-10)


def test_bend_only_ignores_invalid_twist_radii_until_mode_changes(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 0, _compose(maya_cmds))
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.twistInnerRadius", 90.0)
    maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True

    maya_cmds.setAttr(f"{node}.mode", 0)
    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == 2


def test_disabled_pose_ignores_invalid_quaternion_and_override(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 2, _compose(maya_cmds))
    maya_cmds.getAttr(f"{node}.pose[9].poseQuat")
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)
    maya_cmds.setAttr(f"{node}.pose[9].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[9].bendInnerRadiusOverride", 90.0)
    maya_cmds.setAttr(f"{node}.pose[9].bendOuterRadiusOverride", 60.0)

    assert _weight(maya_cmds, node, 2) == pytest.approx(1.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize(
    ("invalid_target", "expected_status"),
    (
        ("input", 3),
        ("axis", 3),
        ("pose", 3),
        ("bend_radius", 2),
        ("twist_radius", 2),
        ("override_radius", 2),
    ),
)
def test_invalid_input_reports_status_and_zeroes_outputs(
    maya_cmds,
    invalid_target,
    expected_status,
):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 0, _compose(maya_cmds))

    if invalid_target == "input":
        maya_cmds.setAttr(f"{node}.inputQuatX", math.nan)
    elif invalid_target == "axis":
        _set_quaternion(maya_cmds, f"{node}.axisQuat", (0.0, 0.0, 0.0, 0.0))
    elif invalid_target == "pose":
        maya_cmds.setAttr(f"{node}.pose[0].poseQuatW", math.nan)
    elif invalid_target == "bend_radius":
        maya_cmds.setAttr(f"{node}.bendInnerRadius", 60.0)
        maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
    elif invalid_target == "twist_radius":
        maya_cmds.setAttr(f"{node}.twistInnerRadius", 60.0)
        maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)
    else:
        maya_cmds.setAttr(f"{node}.pose[0].useRadiusOverride", True)
        maya_cmds.setAttr(f"{node}.pose[0].bendInnerRadiusOverride", 90.0)
        maya_cmds.setAttr(f"{node}.pose[0].bendOuterRadiusOverride", 60.0)

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.falloffStatus") == expected_status


def test_axis_quaternion_is_shared_with_bend_twist_convention(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    axis = _axis_quaternion("z", 90.0)
    pose = _compose(
        maya_cmds,
        twist=15.0,
        bend_h=30.0,
        axis_quat=axis,
    )
    _set_pose(maya_cmds, node, 0, pose)
    _set_quaternion(maya_cmds, f"{node}.inputQuat", pose)
    _set_quaternion(maya_cmds, f"{node}.axisQuat", axis)

    assert _weight(maya_cmds, node, 0) == pytest.approx(1.0)


def test_removed_pose_removes_matching_output_element(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    _set_pose(maya_cmds, node, 2, _compose(maya_cmds))
    _set_pose(maya_cmds, node, 10, _compose(maya_cmds, bend_h=20.0))
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
        node = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
        _set_pose(maya_cmds, node, 0, _compose(maya_cmds))
        _set_quaternion(
            maya_cmds,
            f"{node}.inputQuat",
            _compose(maya_cmds, twist=30.0, bend_h=30.0),
        )
        maya_cmds.setAttr(f"{node}.falloff", 0)
        maya_cmds.setAttr(f"{node}.bendOuterRadius", 60.0)
        maya_cmds.setAttr(f"{node}.twistOuterRadius", 60.0)
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.25, abs=1.0e-10)

        maya_cmds.setAttr(f"{node}.mode", 1)
        assert _weight(maya_cmds, node, 0) == pytest.approx(0.5, abs=1.0e-10)
        maya_cmds.setAttr(f"{node}.bendOuterRadius", 90.0)
        assert _weight(maya_cmds, node, 0) == pytest.approx(
            2.0 / 3.0,
            abs=1.0e-10,
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_pose_blend_parent_connection(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    weight = maya_cmds.createNode("bdRbf_BendTwistFalloffWeight")
    blend = maya_cmds.createNode("bdRbf_PoseBlend")
    pose = _compose(maya_cmds, twist=30.0, bend_h=20.0)
    _set_pose(maya_cmds, weight, 8, pose)
    _set_quaternion(maya_cmds, f"{weight}.inputQuat", pose)
    maya_cmds.setAttr(f"{blend}.pose[8].translateY", 5.0)
    maya_cmds.connectAttr(f"{weight}.outputWeight", f"{blend}.weight")

    assert maya_cmds.getAttr(f"{blend}.outputTranslateY") == pytest.approx(5.0)


def test_node_operator_creation_and_parent_connection(
    maya_cmds,
    modifier_manager,
):
    _load_bd_util_nodes(maya_cmds)
    from bd_util.maya.node.operator.node.dg.bd_rbf_bend_twist_falloff_weight import (
        BdRbfBendTwistFalloffWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_BendTwistFalloffWeight(
        name="rbf_bend_twist_falloff_weight"
    )
    blend = nodes.create.bdRbf_PoseBlend(name="rbf_bend_twist_falloff_blend")
    pose = _compose(maya_cmds, twist=30.0, bend_h=20.0)
    weight.pose[8].poseQuat.set(pose)
    weight.inputQuat.set(pose)
    weight.mode.set(weight.mode.BENDONLY)
    blend.pose[8].translate.set((0.0, 5.0, 0.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfBendTwistFalloffWeight)
    assert weight.outputWeight[8].get() == pytest.approx(1.0)
    assert blend.outputTranslate.get() == pytest.approx((0.0, 5.0, 0.0))
    assert isinstance(
        nodes.existing.bdRbf_BendTwistFalloffWeight(weight.name),
        BdRbfBendTwistFalloffWeight,
    )


def test_scene_round_trip_preserves_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_BendTwistFalloffWeight",
        name="saved_bend_twist_falloff",
    )
    pose = _compose(maya_cmds, twist=30.0, bend_h=20.0)
    _set_pose(maya_cmds, node, 8, pose)
    _set_quaternion(maya_cmds, f"{node}.inputQuat", pose)
    maya_cmds.setAttr(f"{node}.mode", 1)
    maya_cmds.setAttr(f"{node}.order", 1)
    maya_cmds.setAttr(f"{node}.falloff", 1)
    maya_cmds.setAttr(f"{node}.bendInnerRadius", 10.0)
    maya_cmds.setAttr(f"{node}.bendOuterRadius", 80.0)
    maya_cmds.setAttr(f"{node}.pose[8].useRadiusOverride", True)
    maya_cmds.setAttr(f"{node}.pose[8].bendInnerRadiusOverride", 20.0)
    maya_cmds.setAttr(f"{node}.pose[8].bendOuterRadiusOverride", 70.0)

    scene_path = tmp_path / "rbf_bend_twist_falloff_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr("saved_bend_twist_falloff.mode") == 1
    assert maya_cmds.getAttr("saved_bend_twist_falloff.order") == 1
    assert maya_cmds.getAttr("saved_bend_twist_falloff.falloff") == 1
    assert maya_cmds.getAttr(
        "saved_bend_twist_falloff.bendInnerRadius"
    ) == pytest.approx(10.0)
    assert (
        maya_cmds.getAttr("saved_bend_twist_falloff.pose[8].useRadiusOverride")
        is True
    )
    assert maya_cmds.getAttr(
        "saved_bend_twist_falloff.outputWeight[8]"
    ) == pytest.approx(1.0)
