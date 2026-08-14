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


def _set_source(
    maya_cmds,
    node: str,
    index: int,
    quaternion,
    *,
    influence: float = 1.0,
) -> None:
    maya_cmds.setAttr(
        f"{node}.source[{index}].inputQuat",
        *quaternion,
        type="double4",
    )
    maya_cmds.setAttr(f"{node}.source[{index}].influence", influence)


def _set_pose_source(
    maya_cmds,
    node: str,
    pose_index: int,
    source_index: int,
    quaternion,
) -> None:
    maya_cmds.setAttr(
        f"{node}.pose[{pose_index}].sourceQuat[{source_index}]",
        *quaternion,
        type="double4",
    )


def _weight(maya_cmds, node: str, index: int) -> float:
    return maya_cmds.getAttr(f"{node}.outputWeight[{index}]")


def test_type_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")

    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x00142719
    assert maya_cmds.attributeQuery(
        "source", node=node, listChildren=True
    ) == [
        "inputQuat",
        "influence",
    ]
    assert maya_cmds.attributeQuery("pose", node=node, listChildren=True) == [
        "sourceQuat",
        "enabled",
    ]
    assert maya_cmds.attributeQuery(
        "sourceQuat", node=node, listChildren=True
    ) == ["sourceQuatX", "sourceQuatY", "sourceQuatZ", "sourceQuatW"]
    assert maya_cmds.attributeQuery("sourceQuat", node=node, multi=True)
    assert maya_cmds.attributeQuery("kernel", node=node, listEnum=True) == [
        "Gaussian:Exponential:Linear:CompactCubic:CompactQuintic"
    ]
    assert maya_cmds.attributeQuery(
        "solveStatus", node=node, listEnum=True
    ) == [
        "Success:NoPoses:InvalidRadius:InvalidRegularization:"
        "InvalidQuaternion:DuplicatePose:RankDeficient:"
        "NumericalFailure:UnsupportedKernel:NoSources=10:"
        "InvalidInfluence:IncompletePose"
    ]
    assert maya_cmds.getAttr(f"{node}.source[3].inputQuat")[
        0
    ] == pytest.approx((0.0, 0.0, 0.0, 1.0))
    assert maya_cmds.getAttr(f"{node}.source[3].influence") == pytest.approx(
        1.0
    )
    assert maya_cmds.getAttr(f"{node}.pose[4].sourceQuat[3]")[
        0
    ] == pytest.approx((0.0, 0.0, 0.0, 0.0))
    assert maya_cmds.getAttr(f"{node}.pose[4].enabled") is True
    assert maya_cmds.getAttr(f"{node}.radius") == pytest.approx(60.0)
    assert maya_cmds.getAttr(f"{node}.kernel") == 4
    assert maya_cmds.getAttr(f"{node}.regularization") == pytest.approx(1.0e-8)
    assert maya_cmds.getAttr(f"{node}.allowNegativeWeights") is False
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 4


def test_no_sources_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_pose_source(maya_cmds, node, 0, 2, _axis_x_quaternion(0.0))

    assert _weight(maya_cmds, node, 0) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 10


def test_single_source_matches_orientation_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 5, _axis_x_quaternion(22.5))
    _set_pose_source(maya_cmds, node, 3, 5, _axis_x_quaternion(0.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(
        math.exp(-(0.25**2)), abs=1.0e-12
    )
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_equal_influence_uses_root_mean_square_distance(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(30.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(60.0))
    _set_pose_source(maya_cmds, node, 4, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 4, 8, _axis_x_quaternion(0.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    normalized_distance_squared = (30.0**2 + 60.0**2) / 2.0 / 90.0**2
    assert _weight(maya_cmds, node, 4) == pytest.approx(
        math.exp(-normalized_distance_squared), abs=1.0e-12
    )


def test_source_influence_weights_distance_and_invalidates_cache(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(
        maya_cmds,
        node,
        2,
        _axis_x_quaternion(30.0),
        influence=3.0,
    )
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(60.0))
    _set_pose_source(maya_cmds, node, 4, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 4, 8, _axis_x_quaternion(0.0))
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    expected_squared = (3.0 * 30.0**2 + 60.0**2) / 4.0 / 90.0**2
    assert _weight(maya_cmds, node, 4) == pytest.approx(
        math.exp(-expected_squared), abs=1.0e-12
    )

    maya_cmds.setAttr(f"{node}.source[2].influence", 1.0)
    equal_expected_squared = (30.0**2 + 60.0**2) / 2.0 / 90.0**2
    assert _weight(maya_cmds, node, 4) == pytest.approx(
        math.exp(-equal_expected_squared), abs=1.0e-12
    )


def test_source_count_normalization_preserves_radius_meaning(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    for source_index in (2, 8):
        _set_source(
            maya_cmds,
            node,
            source_index,
            _axis_x_quaternion(30.0),
        )
        _set_pose_source(
            maya_cmds,
            node,
            4,
            source_index,
            _axis_x_quaternion(0.0),
        )
    maya_cmds.setAttr(f"{node}.kernel", 0)
    maya_cmds.setAttr(f"{node}.radius", 90.0)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 4) == pytest.approx(
        math.exp(-((30.0 / 90.0) ** 2)), abs=1.0e-12
    )


def test_pose_centers_are_orientation_tuples(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(30.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(90.0))

    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(30.0))
    _set_pose_source(maya_cmds, node, 3, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 9, 2, _axis_x_quaternion(30.0))
    _set_pose_source(maya_cmds, node, 9, 8, _axis_x_quaternion(90.0))
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0, abs=1.0e-12)
    assert _weight(maya_cmds, node, 9) == pytest.approx(1.0, abs=1.0e-12)
    assert maya_cmds.getAttr(f"{node}.outputWeight", multiIndices=True) == [
        3,
        9,
    ]


def test_quaternion_sign_and_scale_are_ignored_per_source(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    first = _axis_x_quaternion(30.0)
    second = _axis_x_quaternion(70.0)
    _set_source(maya_cmds, node, 1, tuple(-2.0 * value for value in first))
    _set_source(maya_cmds, node, 6, tuple(3.0 * value for value in second))
    _set_pose_source(maya_cmds, node, 4, 1, first)
    _set_pose_source(maya_cmds, node, 4, 6, second)
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 4) == pytest.approx(1.0, abs=1.0e-12)


def test_incomplete_pose_reports_status_and_zeroes_all_outputs(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is False
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 12


def test_all_zero_influences_report_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(
        maya_cmds,
        node,
        2,
        _axis_x_quaternion(0.0),
        influence=0.0,
    )
    _set_pose_source(maya_cmds, node, 3, 2, (0.0, 0.0, 0.0, 0.0))

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 11


def test_zero_influence_ignores_invalid_quaternion(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(
        maya_cmds,
        node,
        8,
        (0.0, 0.0, 0.0, 0.0),
        influence=0.0,
    )
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 8, (0.0, 0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.regularization", 0.0)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


@pytest.mark.parametrize("invalid_target", ("input", "pose"))
def test_active_invalid_quaternion_reports_status(maya_cmds, invalid_target):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    input_quaternion = _axis_x_quaternion(0.0)
    pose_quaternion = _axis_x_quaternion(0.0)
    if invalid_target == "input":
        input_quaternion = (0.0, 0.0, 0.0, 0.0)
    else:
        pose_quaternion = (0.0, 0.0, 0.0, 0.0)
    _set_source(maya_cmds, node, 2, input_quaternion)
    _set_pose_source(maya_cmds, node, 3, 2, pose_quaternion)

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 4


def test_duplicate_orientation_tuple_reports_status(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(0.0))
    for source_index, degrees in ((2, 20.0), (8, 50.0)):
        quaternion = _axis_x_quaternion(degrees)
        _set_pose_source(maya_cmds, node, 3, source_index, quaternion)
        _set_pose_source(
            maya_cmds,
            node,
            9,
            source_index,
            tuple(-value for value in quaternion),
        )

    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 5


def test_disabled_incomplete_pose_keeps_zero_output(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(0.0))
    _set_source(maya_cmds, node, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 3, 8, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, node, 9, 2, (0.0, 0.0, 0.0, 0.0))
    maya_cmds.setAttr(f"{node}.pose[9].enabled", False)

    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)
    assert _weight(maya_cmds, node, 9) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.isValid") is True


def test_removed_source_quaternion_makes_pose_incomplete(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    for source_index in (2, 8):
        _set_source(maya_cmds, node, source_index, _axis_x_quaternion(0.0))
        _set_pose_source(
            maya_cmds,
            node,
            3,
            source_index,
            _axis_x_quaternion(0.0),
        )
    assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)

    maya_cmds.removeMultiInstance(f"{node}.pose[3].sourceQuat[8]", b=True)
    assert _weight(maya_cmds, node, 3) == pytest.approx(0.0)
    assert maya_cmds.getAttr(f"{node}.solveStatus") == 12


@pytest.mark.parametrize("evaluation_mode", ("off", "serial", "parallel"))
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)
    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
        for source_index in (2, 8):
            _set_source(
                maya_cmds,
                node,
                source_index,
                _axis_x_quaternion(0.0),
            )
            _set_pose_source(
                maya_cmds,
                node,
                3,
                source_index,
                _axis_x_quaternion(0.0),
            )
            _set_pose_source(
                maya_cmds,
                node,
                9,
                source_index,
                _axis_x_quaternion(90.0),
            )
        assert _weight(maya_cmds, node, 3) == pytest.approx(1.0, abs=2.0e-8)

        maya_cmds.setAttr(
            f"{node}.source[2].inputQuat",
            *_axis_x_quaternion(90.0),
            type="double4",
        )
        maya_cmds.setAttr(
            f"{node}.source[8].inputQuat",
            *_axis_x_quaternion(90.0),
            type="double4",
        )
        assert _weight(maya_cmds, node, 3) == pytest.approx(0.0, abs=1.0e-12)
        assert _weight(maya_cmds, node, 9) == pytest.approx(1.0, abs=2.0e-8)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_pose_blend_parent_connection(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    weight = maya_cmds.createNode("bdRbf_MultiOrientationWeight")
    blend = maya_cmds.createNode("bdRbf_PoseBlend")
    _set_source(maya_cmds, weight, 2, _axis_x_quaternion(0.0))
    _set_pose_source(maya_cmds, weight, 7, 2, _axis_x_quaternion(0.0))
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
    from bd_util.maya.node.operator.node.dg.bd_rbf_multi_orientation_weight import (
        BdRbfMultiOrientationWeight,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    weight = nodes.create.bdRbf_MultiOrientationWeight(
        name="rbf_multi_orientation_weight"
    )
    blend = nodes.create.bdRbf_PoseBlend(name="rbf_multi_orientation_blend")
    weight.source[2].inputQuat.set(_axis_x_quaternion(0.0))
    weight.source[8].inputQuat.set(_axis_x_quaternion(90.0))
    weight.source[8].influence.set(2.0)
    weight.pose[7].sourceQuat[2].set(_axis_x_quaternion(0.0))
    weight.pose[7].sourceQuat[8].set(_axis_x_quaternion(90.0))
    blend.pose[7].translate.set((1.0, 2.0, 3.0))
    weight.outputWeight.connect(blend.weight)
    modifier_manager.do_it_dg()

    assert isinstance(weight, BdRbfMultiOrientationWeight)
    assert weight.outputWeight[7].get() == pytest.approx(1.0, abs=2.0e-8)
    assert blend.outputTranslate.get() == pytest.approx((1.0, 2.0, 3.0))
    assert isinstance(
        nodes.existing.bdRbf_MultiOrientationWeight(weight.name),
        BdRbfMultiOrientationWeight,
    )


def test_scene_round_trip_preserves_nested_configuration(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)
    node = maya_cmds.createNode(
        "bdRbf_MultiOrientationWeight",
        name="saved_multi_orientation",
    )
    _set_source(maya_cmds, node, 2, _axis_x_quaternion(20.0))
    _set_source(
        maya_cmds,
        node,
        8,
        _axis_x_quaternion(70.0),
        influence=2.5,
    )
    _set_pose_source(maya_cmds, node, 7, 2, _axis_x_quaternion(20.0))
    _set_pose_source(maya_cmds, node, 7, 8, _axis_x_quaternion(70.0))
    maya_cmds.setAttr(f"{node}.kernel", 1)
    maya_cmds.setAttr(f"{node}.radius", 120.0)

    scene_path = tmp_path / "rbf_multi_orientation_weight.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(
        "saved_multi_orientation.source", multiIndices=True
    ) == [2, 8]
    assert maya_cmds.getAttr(
        "saved_multi_orientation.pose[7].sourceQuat", multiIndices=True
    ) == [2, 8]
    assert maya_cmds.getAttr(
        "saved_multi_orientation.source[8].influence"
    ) == pytest.approx(2.5)
    assert maya_cmds.getAttr("saved_multi_orientation.kernel") == 1
    assert maya_cmds.getAttr(
        "saved_multi_orientation.radius"
    ) == pytest.approx(120.0)
    assert maya_cmds.getAttr(
        "saved_multi_orientation.outputWeight[7]"
    ) == pytest.approx(1.0, abs=2.0e-8)
