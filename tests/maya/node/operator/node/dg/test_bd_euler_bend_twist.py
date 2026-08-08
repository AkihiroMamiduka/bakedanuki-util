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


def _get_angles(maya_cmds, plug: str) -> tuple[float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _normalized(value) -> tuple[float, float, float, float]:
    length = math.sqrt(sum(component * component for component in value))
    return tuple(component / length for component in value)


def _assert_same_rotation(actual, expected, tolerance=1.0e-9) -> None:
    actual = _normalized(actual)
    expected = _normalized(expected)
    dot = abs(sum(a * b for a, b in zip(actual, expected)))
    assert dot == pytest.approx(1.0, abs=tolerance)


def test_node_ids_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
    compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    selection = maya_om.MSelectionList()
    selection.add(decompose)
    selection.add(compose)
    decompose_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    compose_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))

    assert decompose_fn.typeId.id() == 0x0007F08D
    assert compose_fn.typeId.id() == 0x0007F08E
    assert maya_cmds.attributeQuery(
        "inputRotate", node=decompose, listChildren=True
    ) == ["inputRotateX", "inputRotateY", "inputRotateZ"]
    assert maya_cmds.attributeQuery(
        "axisRotate", node=decompose, listChildren=True
    ) == ["axisRotateX", "axisRotateY", "axisRotateZ"]
    assert maya_cmds.attributeQuery(
        "output", node=decompose, listChildren=True
    ) == ["outputTwist", "outputBendH", "outputBendV"]
    assert maya_cmds.attributeQuery(
        "input", node=compose, listChildren=True
    ) == ["inputTwist", "inputBendH", "inputBendV"]
    assert maya_cmds.attributeQuery(
        "outputRotate", node=compose, listChildren=True
    ) == ["outputRotateX", "outputRotateY", "outputRotateZ"]
    for node, attribute in (
        (decompose, "inputRotateOrder"),
        (decompose, "axisRotateOrder"),
        (compose, "axisRotateOrder"),
        (compose, "outputRotateOrder"),
    ):
        assert maya_cmds.attributeQuery(
            attribute, node=node, listEnum=True
        ) == ["xyz:yzx:zxy:xzy:yxz:zyx"]
    for node in (decompose, compose):
        assert maya_cmds.attributeQuery("order", node=node, listEnum=True) == [
            "TwistBend:BendTwist"
        ]

    assert _get_angles(maya_cmds, f"{decompose}.inputRotate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(0.0)
    assert _get_angles(maya_cmds, f"{compose}.outputRotate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{compose}.outputRotateOrder", settable=True)


@pytest.mark.parametrize(
    (
        "input_rotate",
        "input_rotate_order",
        "axis_rotate",
        "axis_rotate_order",
        "order",
    ),
    [
        ((35.0, -48.0, 72.0), 0, (0.0, 0.0, 0.0), 0, 0),
        ((35.0, -48.0, 72.0), 5, (0.0, 0.0, 0.0), 0, 1),
        ((15.0, 30.0, -20.0), 2, (25.0, -40.0, 10.0), 4, 0),
        ((-110.0, 55.0, 80.0), 3, (-30.0, 15.0, 70.0), 1, 1),
    ],
)
def test_decompose_matches_standard_conversion_and_quaternion_node(
    maya_cmds,
    input_rotate,
    input_rotate_order,
    axis_rotate,
    axis_rotate_order,
    order,
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    euler_node = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
    maya_cmds.setAttr(
        f"{euler_node}.inputRotate", *input_rotate, type="double3"
    )
    maya_cmds.setAttr(f"{euler_node}.inputRotateOrder", input_rotate_order)
    maya_cmds.setAttr(f"{euler_node}.axisRotate", *axis_rotate, type="double3")
    maya_cmds.setAttr(f"{euler_node}.axisRotateOrder", axis_rotate_order)
    maya_cmds.setAttr(f"{euler_node}.order", order)

    input_to_quat = maya_cmds.createNode("eulerToQuat")
    axis_to_quat = maya_cmds.createNode("eulerToQuat")
    quat_node = maya_cmds.createNode("bdQuat_DecomposeBendTwist")
    maya_cmds.setAttr(
        f"{input_to_quat}.inputRotate", *input_rotate, type="double3"
    )
    maya_cmds.setAttr(f"{input_to_quat}.inputRotateOrder", input_rotate_order)
    maya_cmds.setAttr(
        f"{axis_to_quat}.inputRotate", *axis_rotate, type="double3"
    )
    maya_cmds.setAttr(f"{axis_to_quat}.inputRotateOrder", axis_rotate_order)
    maya_cmds.connectAttr(
        f"{input_to_quat}.outputQuat", f"{quat_node}.inputQuat"
    )
    maya_cmds.connectAttr(
        f"{axis_to_quat}.outputQuat", f"{quat_node}.axisQuat"
    )
    maya_cmds.setAttr(f"{quat_node}.order", order)

    assert _get_angles(maya_cmds, f"{euler_node}.output") == pytest.approx(
        _get_angles(maya_cmds, f"{quat_node}.output"), abs=1.0e-9
    )
    assert maya_cmds.getAttr(f"{euler_node}.bendRatio") == pytest.approx(
        maya_cmds.getAttr(f"{quat_node}.bendRatio"), abs=1.0e-12
    )


@pytest.mark.parametrize(
    (
        "components",
        "axis_rotate",
        "axis_rotate_order",
        "order",
        "output_rotate_order",
    ),
    [
        ((35.0, -48.0, 72.0), (0.0, 0.0, 0.0), 0, 0, 0),
        ((35.0, -48.0, 72.0), (0.0, 0.0, 0.0), 0, 1, 5),
        ((15.0, 30.0, -20.0), (25.0, -40.0, 10.0), 4, 0, 2),
        ((-110.0, 55.0, 80.0), (-30.0, 15.0, 70.0), 1, 1, 3),
    ],
)
def test_compose_matches_quaternion_node_and_standard_conversion(
    maya_cmds,
    components,
    axis_rotate,
    axis_rotate_order,
    order,
    output_rotate_order,
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    euler_node = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    maya_cmds.setAttr(f"{euler_node}.input", *components, type="double3")
    maya_cmds.setAttr(f"{euler_node}.axisRotate", *axis_rotate, type="double3")
    maya_cmds.setAttr(f"{euler_node}.axisRotateOrder", axis_rotate_order)
    maya_cmds.setAttr(f"{euler_node}.order", order)
    maya_cmds.setAttr(f"{euler_node}.outputRotateOrder", output_rotate_order)

    axis_to_quat = maya_cmds.createNode("eulerToQuat")
    quat_node = maya_cmds.createNode("bdQuat_ComposeBendTwist")
    quat_to_euler = maya_cmds.createNode("quatToEuler")
    maya_cmds.setAttr(
        f"{axis_to_quat}.inputRotate", *axis_rotate, type="double3"
    )
    maya_cmds.setAttr(f"{axis_to_quat}.inputRotateOrder", axis_rotate_order)
    maya_cmds.setAttr(f"{quat_node}.input", *components, type="double3")
    maya_cmds.connectAttr(
        f"{axis_to_quat}.outputQuat", f"{quat_node}.axisQuat"
    )
    maya_cmds.setAttr(f"{quat_node}.order", order)
    maya_cmds.connectAttr(
        f"{quat_node}.outputQuat", f"{quat_to_euler}.inputQuat"
    )
    maya_cmds.setAttr(f"{quat_to_euler}.inputRotateOrder", output_rotate_order)

    assert _get_angles(
        maya_cmds, f"{euler_node}.outputRotate"
    ) == pytest.approx(
        _get_angles(maya_cmds, f"{quat_to_euler}.outputRotate"),
        abs=1.0e-9,
    )


@pytest.mark.parametrize("order", [0, 1])
@pytest.mark.parametrize("rotate_order", range(6))
def test_compose_decompose_round_trip(
    maya_cmds,
    order,
    rotate_order,
):
    _load_bd_util_nodes(maya_cmds)

    compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    decompose = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
    maya_cmds.setAttr(f"{compose}.input", 35.0, -40.0, 25.0, type="double3")
    maya_cmds.setAttr(
        f"{compose}.axisRotate", 20.0, -15.0, 30.0, type="double3"
    )
    maya_cmds.setAttr(f"{compose}.axisRotateOrder", 4)
    maya_cmds.setAttr(f"{compose}.order", order)
    maya_cmds.setAttr(f"{compose}.outputRotateOrder", rotate_order)
    maya_cmds.connectAttr(
        f"{compose}.outputRotate", f"{decompose}.inputRotate"
    )
    maya_cmds.setAttr(f"{decompose}.inputRotateOrder", rotate_order)
    maya_cmds.setAttr(
        f"{decompose}.axisRotate", 20.0, -15.0, 30.0, type="double3"
    )
    maya_cmds.setAttr(f"{decompose}.axisRotateOrder", 4)
    maya_cmds.setAttr(f"{decompose}.order", order)

    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (35.0, -40.0, 25.0), abs=1.0e-9
    )


def test_transform_rotate_and_rotate_order_connect_directly(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    source = maya_cmds.createNode("transform")
    axis = maya_cmds.createNode("transform")
    target = maya_cmds.createNode("transform")
    decompose = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
    compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    maya_cmds.setAttr(f"{source}.rotate", 35.0, -48.0, 72.0, type="double3")
    maya_cmds.setAttr(f"{source}.rotateOrder", 4)
    maya_cmds.setAttr(f"{axis}.rotate", 20.0, -15.0, 30.0, type="double3")
    maya_cmds.setAttr(f"{axis}.rotateOrder", 2)
    maya_cmds.setAttr(f"{target}.rotateOrder", 5)

    maya_cmds.connectAttr(f"{source}.rotate", f"{decompose}.inputRotate")
    maya_cmds.connectAttr(
        f"{source}.rotateOrder", f"{decompose}.inputRotateOrder"
    )
    maya_cmds.connectAttr(f"{axis}.rotate", f"{decompose}.axisRotate")
    maya_cmds.connectAttr(
        f"{axis}.rotateOrder", f"{decompose}.axisRotateOrder"
    )
    maya_cmds.connectAttr(f"{decompose}.output", f"{compose}.input")
    maya_cmds.connectAttr(f"{axis}.rotate", f"{compose}.axisRotate")
    maya_cmds.connectAttr(f"{axis}.rotateOrder", f"{compose}.axisRotateOrder")
    maya_cmds.connectAttr(
        f"{target}.rotateOrder", f"{compose}.outputRotateOrder"
    )
    maya_cmds.connectAttr(f"{compose}.outputRotate", f"{target}.rotate")

    source_to_quat = maya_cmds.createNode("eulerToQuat")
    target_to_quat = maya_cmds.createNode("eulerToQuat")
    maya_cmds.connectAttr(f"{source}.rotate", f"{source_to_quat}.inputRotate")
    maya_cmds.connectAttr(
        f"{source}.rotateOrder", f"{source_to_quat}.inputRotateOrder"
    )
    maya_cmds.connectAttr(f"{target}.rotate", f"{target_to_quat}.inputRotate")
    maya_cmds.connectAttr(
        f"{target}.rotateOrder", f"{target_to_quat}.inputRotateOrder"
    )
    _assert_same_rotation(
        _get_quat(maya_cmds, f"{target_to_quat}.outputQuat"),
        _get_quat(maya_cmds, f"{source_to_quat}.outputQuat"),
    )
    assert not maya_cmds.ls(type="unitConversion")


def test_output_rotate_order_changes_representation_not_orientation(
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    to_quat = maya_cmds.createNode("eulerToQuat")
    maya_cmds.setAttr(f"{compose}.input", 35.0, -48.0, 72.0, type="double3")
    maya_cmds.connectAttr(f"{compose}.outputRotate", f"{to_quat}.inputRotate")
    maya_cmds.connectAttr(
        f"{compose}.outputRotateOrder", f"{to_quat}.inputRotateOrder"
    )

    maya_cmds.setAttr(f"{compose}.outputRotateOrder", 0)
    first_angles = _get_angles(maya_cmds, f"{compose}.outputRotate")
    first_quat = _get_quat(maya_cmds, f"{to_quat}.outputQuat")
    maya_cmds.setAttr(f"{compose}.outputRotateOrder", 5)
    second_angles = _get_angles(maya_cmds, f"{compose}.outputRotate")
    second_quat = _get_quat(maya_cmds, f"{to_quat}.outputQuat")

    assert first_angles != pytest.approx(second_angles)
    _assert_same_rotation(first_quat, second_quat)


def test_non_finite_inputs_use_safe_fallbacks(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    decompose = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
    compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
    maya_cmds.setAttr(f"{decompose}.inputRotateX", math.nan)
    maya_cmds.setAttr(f"{compose}.inputTwist", math.nan)

    assert _get_angles(maya_cmds, f"{decompose}.output") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{decompose}.bendRatio") == pytest.approx(0.0)
    assert _get_angles(maya_cmds, f"{compose}.outputRotate") == pytest.approx(
        (0.0, 0.0, 0.0)
    )


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        compose = maya_cmds.createNode("bdEuler_ComposeBendTwist")
        decompose = maya_cmds.createNode("bdEuler_DecomposeBendTwist")
        maya_cmds.connectAttr(
            f"{compose}.outputRotate", f"{decompose}.inputRotate"
        )
        maya_cmds.setAttr(f"{compose}.inputTwist", 20.0)
        first = maya_cmds.getAttr(f"{decompose}.outputTwist")
        maya_cmds.setAttr(f"{compose}.inputTwist", 75.0)
        second = maya_cmds.getAttr(f"{decompose}.outputTwist")
        assert first == pytest.approx(20.0)
        assert second == pytest.approx(75.0)
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_operator_types_and_direct_connection(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_euler_compose_bend_twist import (
        BdEulerComposeBendTwist,
    )
    from bd_util.maya.node.operator.node.dg.bd_euler_decompose_bend_twist import (
        BdEulerDecomposeBendTwist,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    compose = nodes.create.bdEuler_ComposeBendTwist(name="compose")
    decompose = nodes.create.bdEuler_DecomposeBendTwist(name="decompose")
    compose.input.set((35.0, -40.0, 25.0))
    compose.outputRotate > decompose.inputRotate
    compose.outputRotateOrder > decompose.inputRotateOrder
    modifier_manager.do_it_dg()

    assert isinstance(compose, BdEulerComposeBendTwist)
    assert isinstance(decompose, BdEulerDecomposeBendTwist)
    assert isinstance(compose.outputRotate.get(), bdu.DoubleAngle3)
    assert isinstance(decompose.output.get(), bdu.DoubleAngle3)
    assert decompose.output.get().as_tuple() == pytest.approx(
        (35.0, -40.0, 25.0)
    )
    assert isinstance(
        nodes.existing.bdEuler_ComposeBendTwist(compose.name),
        BdEulerComposeBendTwist,
    )
    assert isinstance(
        nodes.existing.bdEuler_DecomposeBendTwist(decompose.name),
        BdEulerDecomposeBendTwist,
    )


def test_nodes_survive_scene_save_and_reload(maya_cmds, tmp_path):
    _load_bd_util_nodes(maya_cmds)

    compose = maya_cmds.createNode(
        "bdEuler_ComposeBendTwist", name="eulerComposeBendTwist"
    )
    decompose = maya_cmds.createNode(
        "bdEuler_DecomposeBendTwist", name="eulerDecomposeBendTwist"
    )
    maya_cmds.setAttr(f"{compose}.input", 35.0, -40.0, 25.0, type="double3")
    maya_cmds.setAttr(
        f"{compose}.axisRotate", 20.0, -15.0, 30.0, type="double3"
    )
    maya_cmds.setAttr(f"{compose}.axisRotateOrder", 4)
    maya_cmds.setAttr(f"{compose}.order", 1)
    maya_cmds.setAttr(f"{compose}.outputRotateOrder", 5)
    maya_cmds.connectAttr(
        f"{compose}.outputRotate", f"{decompose}.inputRotate"
    )
    maya_cmds.setAttr(f"{decompose}.inputRotateOrder", 5)
    maya_cmds.setAttr(
        f"{decompose}.axisRotate", 20.0, -15.0, 30.0, type="double3"
    )
    maya_cmds.setAttr(f"{decompose}.axisRotateOrder", 4)
    maya_cmds.setAttr(f"{decompose}.order", 1)

    scene_path = tmp_path / "bd_euler_bend_twist.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert _get_angles(
        maya_cmds, "eulerDecomposeBendTwist.output"
    ) == pytest.approx((35.0, -40.0, 25.0), abs=1.0e-9)
