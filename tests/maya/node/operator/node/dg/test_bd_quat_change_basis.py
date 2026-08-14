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
    return plugin_path


def _axis_quat(axis: str, degrees: float):
    half_angle = math.radians(degrees) * 0.5
    xyz = {
        "x": (math.sin(half_angle), 0.0, 0.0),
        "y": (0.0, math.sin(half_angle), 0.0),
        "z": (0.0, 0.0, math.sin(half_angle)),
    }[axis]
    return (*xyz, math.cos(half_angle))


def _set_quat(maya_cmds, plug: str, value) -> None:
    maya_cmds.setAttr(plug, *value, type="double4")


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _expected(maya_om, input_quat, axis_quat, direction):
    input_value = maya_om.MQuaternion(*input_quat)
    axis_value = maya_om.MQuaternion(*axis_quat)
    inverse_axis = axis_value.inverse()
    if direction == 0:
        result = inverse_axis * input_value * axis_value
    else:
        result = axis_value * input_value * inverse_axis
    return (result.x, result.y, result.z, result.w)


def _standard_chain(maya_cmds, input_quat, axis_quat, direction):
    maya_cmds.loadPlugin("quatNodes", quiet=True)
    inverse = maya_cmds.createNode("quatInvert")
    first = maya_cmds.createNode("quatProd")
    second = maya_cmds.createNode("quatProd")
    _set_quat(maya_cmds, f"{inverse}.inputQuat", axis_quat)

    if direction == 0:
        maya_cmds.connectAttr(f"{inverse}.outputQuat", f"{first}.input1Quat")
        _set_quat(maya_cmds, f"{first}.input2Quat", input_quat)
        maya_cmds.connectAttr(f"{first}.outputQuat", f"{second}.input1Quat")
        _set_quat(maya_cmds, f"{second}.input2Quat", axis_quat)
    else:
        _set_quat(maya_cmds, f"{first}.input1Quat", axis_quat)
        _set_quat(maya_cmds, f"{first}.input2Quat", input_quat)
        maya_cmds.connectAttr(f"{first}.outputQuat", f"{second}.input1Quat")
        maya_cmds.connectAttr(f"{inverse}.outputQuat", f"{second}.input2Quat")
    return second


def test_node_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x00142710
    for parent, children in (
        (
            "inputQuat",
            ["inputQuatX", "inputQuatY", "inputQuatZ", "inputQuatW"],
        ),
        (
            "axisQuat",
            ["axisQuatX", "axisQuatY", "axisQuatZ", "axisQuatW"],
        ),
        (
            "outputQuat",
            ["outputQuatX", "outputQuatY", "outputQuatZ", "outputQuatW"],
        ),
    ):
        assert (
            maya_cmds.attributeQuery(parent, node=node, listChildren=True)
            == children
        )
    assert maya_cmds.attributeQuery("direction", node=node, listEnum=True) == [
        "ApplyAxis:RemoveAxis"
    ]
    assert _get_quat(maya_cmds, f"{node}.inputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert _get_quat(maya_cmds, f"{node}.axisQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{node}.direction") == 0
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )


@pytest.mark.parametrize(
    ("direction", "expected_axis"),
    [
        (0, (0.0, 1.0, 0.0)),
        (1, (0.0, -1.0, 0.0)),
    ],
)
def test_direction_reorients_axis_in_maya_convention(
    maya_cmds,
    maya_om,
    direction,
    expected_axis,
):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    _set_quat(maya_cmds, f"{node}.inputQuat", _axis_quat("x", 30.0))
    _set_quat(maya_cmds, f"{node}.axisQuat", _axis_quat("z", 90.0))
    maya_cmds.setAttr(f"{node}.direction", direction)

    result = maya_om.MQuaternion(*_get_quat(maya_cmds, f"{node}.outputQuat"))
    axis, angle = result.asAxisAngle()
    assert tuple(axis) == pytest.approx(expected_axis, abs=1.0e-12)
    assert math.degrees(angle) == pytest.approx(30.0, abs=1.0e-10)


@pytest.mark.parametrize("direction", [0, 1])
def test_matches_standard_invert_and_product_chain_without_normalizing(
    maya_cmds,
    direction,
):
    _load_bd_util_nodes(maya_cmds)

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    _set_quat(maya_cmds, f"{node}.inputQuat", input_quat)
    _set_quat(maya_cmds, f"{node}.axisQuat", axis_quat)
    maya_cmds.setAttr(f"{node}.direction", direction)

    standard = _standard_chain(
        maya_cmds,
        input_quat,
        axis_quat,
        direction,
    )
    actual = _get_quat(maya_cmds, f"{node}.outputQuat")
    assert actual == pytest.approx(
        _get_quat(maya_cmds, f"{standard}.outputQuat"),
        abs=1.0e-12,
    )
    assert sum(component * component for component in actual) != pytest.approx(
        1.0
    )
    assert not maya_cmds.ls(type="unitConversion")


def test_apply_then_remove_restores_raw_input(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    apply_node = maya_cmds.createNode("bdQuat_ChangeBasis")
    remove_node = maya_cmds.createNode("bdQuat_ChangeBasis")
    _set_quat(maya_cmds, f"{apply_node}.inputQuat", input_quat)
    _set_quat(maya_cmds, f"{apply_node}.axisQuat", axis_quat)
    maya_cmds.connectAttr(
        f"{apply_node}.outputQuat", f"{remove_node}.inputQuat"
    )
    _set_quat(maya_cmds, f"{remove_node}.axisQuat", axis_quat)
    maya_cmds.setAttr(f"{remove_node}.direction", 1)

    assert _get_quat(maya_cmds, f"{remove_node}.outputQuat") == pytest.approx(
        input_quat, abs=1.0e-12
    )


def test_quaternion_signs_are_not_canonicalized(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    nodes = [maya_cmds.createNode("bdQuat_ChangeBasis") for _ in range(3)]
    for node in nodes:
        maya_cmds.setAttr(f"{node}.direction", 0)
    _set_quat(maya_cmds, f"{nodes[0]}.inputQuat", input_quat)
    _set_quat(maya_cmds, f"{nodes[0]}.axisQuat", axis_quat)
    _set_quat(maya_cmds, f"{nodes[1]}.inputQuat", input_quat)
    _set_quat(
        maya_cmds,
        f"{nodes[1]}.axisQuat",
        tuple(-value for value in axis_quat),
    )
    _set_quat(
        maya_cmds,
        f"{nodes[2]}.inputQuat",
        tuple(-value for value in input_quat),
    )
    _set_quat(maya_cmds, f"{nodes[2]}.axisQuat", axis_quat)

    output = _get_quat(maya_cmds, f"{nodes[0]}.outputQuat")
    assert _get_quat(maya_cmds, f"{nodes[1]}.outputQuat") == pytest.approx(
        output
    )
    assert _get_quat(maya_cmds, f"{nodes[2]}.outputQuat") == pytest.approx(
        tuple(-value for value in output)
    )


def test_zero_axis_is_not_silently_replaced(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    _set_quat(maya_cmds, f"{node}.inputQuat", (1.0, 2.0, 3.0, 4.0))
    _set_quat(maya_cmds, f"{node}.axisQuat", (0.0, 0.0, 0.0, 0.0))
    assert all(
        math.isnan(value)
        for value in _get_quat(maya_cmds, f"{node}.outputQuat")
    )


def test_input_dependencies_cover_output_compound(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    expected = {
        "outputQuat",
        "outputQuatX",
        "outputQuatY",
        "outputQuatZ",
        "outputQuatW",
    }
    for input_attribute in (
        "inputQuat",
        "inputQuatX",
        "inputQuatY",
        "inputQuatZ",
        "inputQuatW",
        "axisQuat",
        "axisQuatX",
        "axisQuatY",
        "axisQuatZ",
        "axisQuatW",
        "direction",
    ):
        affected = node_fn.getAffectedAttributes(
            node_fn.attribute(input_attribute)
        )
        assert {
            maya_om.MFnAttribute(attribute).name for attribute in affected
        } == expected


def test_output_child_can_be_requested_directly(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    node = maya_cmds.createNode("bdQuat_ChangeBasis")
    _set_quat(maya_cmds, f"{node}.inputQuat", input_quat)
    _set_quat(maya_cmds, f"{node}.axisQuat", axis_quat)
    assert maya_cmds.getAttr(f"{node}.outputQuatW") == pytest.approx(
        _expected(maya_om, input_quat, axis_quat, 0)[3]
    )


def test_node_operator_supports_quaternion_values_and_direction(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg._generated.bd_quat_change_basis import (
        DirectionEnumPlugOperator,
    )
    from bd_util.maya.node.operator.node.dg.bd_quat_change_basis import (
        BdQuatChangeBasis,
    )

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdQuat_ChangeBasis(name="change_basis")
    node.inputQuat.set(input_quat)
    node.axisQuat.set(axis_quat)
    node.direction.set(DirectionEnumPlugOperator.REMOVEAXIS)
    modifier_manager.do_it_dg()

    assert isinstance(node, BdQuatChangeBasis)
    assert isinstance(node.inputQuat.get(), bdu.Quat)
    assert isinstance(node.axisQuat.get(), bdu.Quat)
    assert isinstance(node.outputQuat.get(), bdu.Quat)
    assert node.outputQuat.get().as_tuple() == pytest.approx(
        _expected(maya_om, input_quat, axis_quat, 1)
    )
    assert isinstance(
        nodes.existing.bdQuat_ChangeBasis(node.name),
        BdQuatChangeBasis,
    )


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    maya_om,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        node = maya_cmds.createNode("bdQuat_ChangeBasis")
        input_quat = _axis_quat("x", 30.0)
        axis_quat = _axis_quat("z", 90.0)
        _set_quat(maya_cmds, f"{node}.inputQuat", input_quat)
        _set_quat(maya_cmds, f"{node}.axisQuat", axis_quat)
        assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
            _expected(maya_om, input_quat, axis_quat, 0)
        )

        maya_cmds.setAttr(f"{node}.direction", 1)
        assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
            _expected(maya_om, input_quat, axis_quat, 1)
        )

        maya_cmds.setAttr(f"{node}.axisQuatW", 0.5)
        changed_axis = (*axis_quat[:3], 0.5)
        assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
            _expected(maya_om, input_quat, changed_axis, 1)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_scene_round_trip(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    input_quat = (1.0, -2.0, 3.0, -4.0)
    axis_quat = (0.5, -1.0, 0.25, 2.0)
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdQuat_ChangeBasis(name="change_basis")
    node.inputQuat.set(input_quat)
    node.axisQuat.set(axis_quat)
    node.direction.set(1)
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_quat_change_basis.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    existing = existing_nodes.existing.bdQuat_ChangeBasis("change_basis")
    assert existing.direction.get() == 1
    assert existing.outputQuat.get().as_tuple() == pytest.approx(
        _expected(maya_om, input_quat, axis_quat, 1)
    )
