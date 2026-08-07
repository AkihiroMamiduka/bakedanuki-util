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


def _set_quat(maya_cmds, plug: str, value) -> None:
    maya_cmds.setAttr(plug, *value, type="double4")


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _get_angles(maya_cmds, plug: str) -> tuple[float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _normalized(value) -> tuple[float, float, float, float]:
    length = math.sqrt(sum(component * component for component in value))
    return tuple(component / length for component in value)


def _assert_same_rotation(actual, expected, tolerance=1.0e-9) -> None:
    actual = _normalized(actual)
    expected = _normalized(expected)
    dot = abs(sum(a * b for a, b in zip(actual, expected)))
    assert dot == pytest.approx(1.0, abs=tolerance)


def _axis_quat(axis: str, degrees: float):
    half_angle = math.radians(degrees) * 0.5
    xyz = {
        "x": (math.sin(half_angle), 0.0, 0.0),
        "y": (0.0, math.sin(half_angle), 0.0),
        "z": (0.0, 0.0, math.sin(half_angle)),
    }[axis]
    return (*xyz, math.cos(half_angle))


def _bend_quat(horizontal_degrees: float, vertical_degrees: float):
    horizontal = math.radians(horizontal_degrees)
    vertical = math.radians(vertical_degrees)
    bend_angle = math.hypot(horizontal, vertical)
    if bend_angle == 0.0:
        return (0.0, 0.0, 0.0, 1.0)

    half_angle = 0.5 * bend_angle
    scale = math.sin(half_angle) / bend_angle
    return (
        0.0,
        horizontal * scale,
        vertical * scale,
        math.cos(half_angle),
    )


def _product(maya_om, first, second):
    result = maya_om.MQuaternion(*first) * maya_om.MQuaternion(*second)
    return (result.x, result.y, result.z, result.w)


def test_node_ids_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    selection = maya_om.MSelectionList()
    selection.add(decompose)
    selection.add(compose)
    decompose_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    compose_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))

    assert decompose_fn.typeId.id() == 0x0007F089
    assert compose_fn.typeId.id() == 0x0007F08A
    assert maya_cmds.attributeQuery(
        "output", node=decompose, listChildren=True
    ) == [
        "outputTwist",
        "outputBendH",
        "outputBendV",
    ]
    assert maya_cmds.attributeQuery(
        "input", node=compose, listChildren=True
    ) == [
        "inputTwist",
        "inputBendH",
        "inputBendV",
    ]
    assert maya_cmds.attributeQuery("order", node=compose, listEnum=True) == [
        "TwistBend:BendTwist"
    ]
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert _get_quat(maya_cmds, f"{compose}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(0.0)
    assert maya_cmds.attributeQuery(
        "bendRatio", node=decompose, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "bendRatio", node=decompose, maximum=True
    ) == [1.0]
    for removed_attribute in (
        "axisOrientationQuat",
        "outputBendHorizontal",
        "outputBendVertical",
        "isValid",
        "isSingular",
    ):
        assert not maya_cmds.attributeQuery(
            removed_attribute, node=decompose, exists=True
        )
    for removed_attribute in (
        "inputBendHorizontal",
        "inputBendVertical",
        "axisOrientationQuat",
        "isValid",
    ):
        assert not maya_cmds.attributeQuery(
            removed_attribute, node=compose, exists=True
        )


@pytest.mark.parametrize("order", [0, 1])
def test_compose_matches_factor_order_and_decomposes_back(
    maya_cmds,
    maya_om,
    order,
):
    _load_bd_util_nodes(maya_cmds)

    angles = (45.0, 60.0, -35.0)
    twist = _axis_quat("x", angles[0])
    bend = _bend_quat(angles[1], angles[2])
    expected = (
        _product(maya_om, twist, bend)
        if order == 0
        else _product(maya_om, bend, twist)
    )

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.input", *angles, type="double3")
    maya_cmds.setAttr(f"{compose}.order", order)
    actual = _get_quat(maya_cmds, f"{compose}.outputQuat")
    _assert_same_rotation(actual, expected)

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    _set_quat(maya_cmds, f"{decompose}.inputQuat", actual)
    maya_cmds.setAttr(f"{decompose}.order", order)
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        angles
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(
        math.hypot(angles[1], angles[2]) / 180.0
    )


@pytest.mark.parametrize(
    ("bend_degrees", "expected_ratio"),
    [
        (0.0, 0.0),
        (45.0, 0.25),
        (90.0, 0.5),
        (135.0, 0.75),
        (180.0, 1.0),
    ],
)
def test_bend_ratio_is_linear_from_aligned_to_opposite_axis(
    maya_cmds,
    bend_degrees,
    expected_ratio,
):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    _set_quat(
        maya_cmds,
        f"{decompose}.inputQuat",
        _axis_quat("y", bend_degrees),
    )

    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(
        expected_ratio
    )


def test_factor_orders_are_distinct_for_combined_rotation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.input", 70.0, 45.0, 30.0, type="double3")
    first = _get_quat(maya_cmds, f"{compose}.outputQuat")
    maya_cmds.setAttr(f"{compose}.order", 1)
    second = _get_quat(maya_cmds, f"{compose}.outputQuat")

    actual = _normalized(first)
    expected = _normalized(second)
    assert abs(sum(a * b for a, b in zip(actual, expected))) < 0.999


def test_decompose_is_scale_and_quaternion_sign_invariant(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.input", -125.0, 50.0, -70.0, type="double3")
    quaternion = _get_quat(maya_cmds, f"{compose}.outputQuat")

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    results = []
    for scale in (1.0, -1.0, 7.5, -3.0):
        _set_quat(
            maya_cmds,
            f"{decompose}.inputQuat",
            tuple(component * scale for component in quaternion),
        )
        results.append(_get_angles(maya_cmds, f"{decompose}.output"))

    for result in results:
        assert result == pytest.approx(results[0])
        assert -180.0 <= result[0] < 180.0
        assert math.hypot(result[1], result[2]) <= 180.0


def test_axis_quat_changes_the_semantic_frame(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    orientation = _axis_quat("z", 90.0)
    canonical = _axis_quat("x", 80.0)
    inverse_orientation = (
        -orientation[0],
        -orientation[1],
        -orientation[2],
        orientation[3],
    )
    input_quaternion = _product(
        maya_om,
        _product(maya_om, inverse_orientation, canonical),
        orientation,
    )

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    _set_quat(maya_cmds, f"{decompose}.inputQuat", input_quaternion)
    _set_quat(
        maya_cmds,
        f"{decompose}.axisQuat",
        orientation,
    )
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (80.0, 0.0, 0.0), abs=1.0e-8
    )

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.inputTwist", 80.0)
    _set_quat(
        maya_cmds,
        f"{compose}.axisQuat",
        orientation,
    )
    _assert_same_rotation(
        _get_quat(maya_cmds, f"{compose}.outputQuat"),
        input_quaternion,
    )


@pytest.mark.parametrize(
    ("quaternion", "expected"),
    [
        ((0.0, 1.0, 0.0, 0.0), (0.0, 180.0, 0.0)),
        ((0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 180.0)),
    ],
)
def test_antipodal_bend_uses_documented_singular_fallback(
    maya_cmds,
    quaternion,
    expected,
):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    _set_quat(maya_cmds, f"{decompose}.inputQuat", quaternion)
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        expected
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(1.0)

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.connectAttr(f"{decompose}.output", f"{compose}.input")
    _assert_same_rotation(
        _get_quat(maya_cmds, f"{compose}.outputQuat"),
        quaternion,
    )


def test_invalid_inputs_return_safe_fallbacks(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    _set_quat(maya_cmds, f"{decompose}.inputQuat", (0.0, 0.0, 0.0, 0.0))
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(0.0)

    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(f"{compose}.inputTwist", math.nan)
    assert _get_quat(maya_cmds, f"{compose}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )

    maya_cmds.setAttr(f"{compose}.inputTwist", 0.0)
    _set_quat(
        maya_cmds,
        f"{compose}.axisQuat",
        (0.0, 0.0, 0.0, 0.0),
    )
    assert _get_quat(maya_cmds, f"{compose}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )


def test_compound_output_connects_directly_to_compound_input(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    compose_source = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    compose_destination = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    maya_cmds.setAttr(
        f"{compose_source}.input", -30.0, 65.0, 25.0, type="double3"
    )
    maya_cmds.connectAttr(
        f"{compose_source}.outputQuat", f"{decompose}.inputQuat"
    )
    maya_cmds.connectAttr(
        f"{decompose}.output", f"{compose_destination}.input"
    )

    _assert_same_rotation(
        _get_quat(maya_cmds, f"{compose_destination}.outputQuat"),
        _get_quat(maya_cmds, f"{compose_source}.outputQuat"),
    )
    assert not maya_cmds.ls(type="unitConversion")


def test_standard_quaternion_nodes_connect_without_conversion(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    to_quaternion = maya_cmds.createNode("eulerToQuat")
    decompose = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    to_euler = maya_cmds.createNode("quatToEuler")
    maya_cmds.connectAttr(
        f"{to_quaternion}.outputQuat", f"{decompose}.inputQuat"
    )
    maya_cmds.connectAttr(f"{decompose}.output", f"{compose}.input")
    maya_cmds.connectAttr(f"{compose}.outputQuat", f"{to_euler}.inputQuat")

    assert not maya_cmds.ls(type="unitConversion")


def test_node_operator_types_and_direct_connection(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_quat_compose_bend_twist import (
        BdQuatComposeBendTwist,
    )
    from bd_util.maya.node.operator.node.dg.bd_quat_decompose_bend_twist import (
        BdQuatDecomposeBendTwist,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    compose = nodes.create.bdQuat_ComposeBendTwist(name="compose")
    decompose = nodes.create.bdQuat_DecomposeBendTwist(name="decompose")
    compose.input.set((35.0, 40.0, -20.0))
    compose.outputQuat > decompose.inputQuat
    modifier_manager.do_it_dg()

    assert isinstance(compose, BdQuatComposeBendTwist)
    assert isinstance(decompose, BdQuatDecomposeBendTwist)
    assert isinstance(compose.outputQuat.get(), bdu.Quat)
    assert decompose.output.get().as_tuple() == pytest.approx(
        (35.0, 40.0, -20.0)
    )
    assert decompose.bendRatio.get() == pytest.approx(
        math.hypot(40.0, -20.0) / 180.0
    )
    assert isinstance(
        nodes.existing.bdQuat_ComposeBendTwist(compose.name),
        BdQuatComposeBendTwist,
    )
    assert isinstance(
        nodes.existing.bdQuat_DecomposeBendTwist(decompose.name),
        BdQuatDecomposeBendTwist,
    )


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_child_dirty_updates_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        compose = maya_cmds.createNode("bdQuat_ComposeBendTwist")
        maya_cmds.setAttr(f"{compose}.inputTwist", 20.0)
        first = _get_quat(maya_cmds, f"{compose}.outputQuat")
        maya_cmds.setAttr(f"{compose}.inputTwist", 75.0)
        second = _get_quat(maya_cmds, f"{compose}.outputQuat")
        _assert_same_rotation(first, _axis_quat("x", 20.0))
        _assert_same_rotation(second, _axis_quat("x", 75.0))
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_nodes_survive_scene_save_and_reload(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)

    compose = maya_cmds.createNode(
        "bdQuat_ComposeBendTwist", name="composeBendTwist"
    )
    decompose = maya_cmds.createNode(
        "bdQuat_DecomposeBendTwist", name="decomposeBendTwist"
    )
    maya_cmds.setAttr(f"{compose}.input", 25.0, -55.0, 70.0, type="double3")
    maya_cmds.connectAttr(f"{compose}.outputQuat", f"{decompose}.inputQuat")

    scene_path = tmp_path / "bd_quat_bend_twist.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert _get_angles(
        maya_cmds, "decomposeBendTwist.output"
    ) == pytest.approx((25.0, -55.0, 70.0))
    assert maya_cmds.getAttr("decomposeBendTwist.bendRatio") == pytest.approx(
        math.hypot(-55.0, 70.0) / 180.0
    )
