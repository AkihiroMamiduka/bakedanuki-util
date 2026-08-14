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


def _set_quat(maya_cmds, plug: str, value) -> None:
    maya_cmds.setAttr(plug, *value, type="double4")


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def _product(maya_om, *values) -> tuple[float, float, float, float]:
    if not values:
        return (0.0, 0.0, 0.0, 1.0)

    result = maya_om.MQuaternion(*values[0])
    for value in values[1:]:
        result *= maya_om.MQuaternion(*value)
    return (result.x, result.y, result.z, result.w)


def _axis_quat(axis: str, degrees: float):
    half_angle = math.radians(degrees) * 0.5
    xyz = {
        "x": (math.sin(half_angle), 0.0, 0.0),
        "y": (0.0, math.sin(half_angle), 0.0),
        "z": (0.0, 0.0, math.sin(half_angle)),
    }[axis]
    return (*xyz, math.cos(half_angle))


def test_node_id_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    selection = maya_om.MSelectionList()
    selection.add(node)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))

    assert node_fn.typeId.id() == 0x00142707
    assert maya_cmds.attributeQuery("inputQuat", node=node, multi=True)
    assert maya_cmds.attributeQuery(
        "inputQuat", node=node, listChildren=True
    ) == ["inputQuatX", "inputQuatY", "inputQuatZ", "inputQuatW"]
    assert maya_cmds.attributeQuery(
        "outputQuat", node=node, listChildren=True
    ) == ["outputQuatX", "outputQuatY", "outputQuatZ", "outputQuatW"]
    assert maya_cmds.getAttr(f"{node}.inputQuat[3]")[0] == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )


def test_empty_and_single_input_preserve_identity_and_raw_value(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )

    raw = (1.0, 2.0, 3.0, 4.0)
    _set_quat(maya_cmds, f"{node}.inputQuat[7]", raw)
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(raw)


def test_sparse_inputs_fold_by_ascending_logical_index(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    qx = _axis_quat("x", 90.0)
    qy = _axis_quat("y", 90.0)
    qz = _axis_quat("z", 35.0)
    node = maya_cmds.createNode("bdQuat_MultiplyMulti")

    _set_quat(maya_cmds, f"{node}.inputQuat[20]", qz)
    _set_quat(maya_cmds, f"{node}.inputQuat[2]", qx)
    _set_quat(maya_cmds, f"{node}.inputQuat[9]", qy)

    actual = _get_quat(maya_cmds, f"{node}.outputQuat")
    expected = _product(maya_om, qx, qy, qz)
    reverse_creation_order = _product(maya_om, qz, qx, qy)
    assert actual == pytest.approx(expected)
    assert actual != pytest.approx(reverse_creation_order)


def test_multiplication_order_matches_quat_prod_chain(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    values = (
        _axis_quat("x", 40.0),
        _axis_quat("y", -65.0),
        _axis_quat("z", 125.0),
    )
    multi = maya_cmds.createNode("bdQuat_MultiplyMulti")
    for index, value in zip((2, 9, 20), values):
        _set_quat(maya_cmds, f"{multi}.inputQuat[{index}]", value)

    first = maya_cmds.createNode("quatProd")
    second = maya_cmds.createNode("quatProd")
    _set_quat(maya_cmds, f"{first}.input1Quat", values[0])
    _set_quat(maya_cmds, f"{first}.input2Quat", values[1])
    maya_cmds.connectAttr(
        f"{first}.outputQuat", f"{second}.input1Quat", force=True
    )
    _set_quat(maya_cmds, f"{second}.input2Quat", values[2])

    assert _get_quat(maya_cmds, f"{multi}.outputQuat") == pytest.approx(
        _get_quat(maya_cmds, f"{second}.outputQuat")
    )


def test_non_unit_and_zero_quaternions_are_not_normalized(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    first = (1.0, 2.0, 3.0, 4.0)
    second = (-2.0, 0.5, 1.5, 3.0)
    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    _set_quat(maya_cmds, f"{node}.inputQuat[0]", first)
    _set_quat(maya_cmds, f"{node}.inputQuat[1]", second)

    actual = _get_quat(maya_cmds, f"{node}.outputQuat")
    assert actual == pytest.approx(_product(maya_om, first, second))
    assert sum(component * component for component in actual) != pytest.approx(
        1.0
    )

    _set_quat(maya_cmds, f"{node}.inputQuat[2]", (0.0, 0.0, 0.0, 0.0))
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        (0.0, 0.0, 0.0, 0.0)
    )


def test_nonfinite_single_input_is_preserved_without_validation(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    _set_quat(
        maya_cmds,
        f"{node}.inputQuat[3]",
        (math.nan, math.inf, -math.inf, 2.0),
    )
    actual = _get_quat(maya_cmds, f"{node}.outputQuat")

    assert math.isnan(actual[0])
    assert actual[1] == math.inf
    assert actual[2] == -math.inf
    assert actual[3] == 2.0


def test_removing_an_element_recomputes_the_product(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    qx = _axis_quat("x", 30.0)
    qy = _axis_quat("y", 60.0)
    qz = _axis_quat("z", 90.0)
    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    for index, value in zip((2, 9, 20), (qx, qy, qz)):
        _set_quat(maya_cmds, f"{node}.inputQuat[{index}]", value)

    maya_cmds.removeMultiInstance(f"{node}.inputQuat[9]", b=True)
    assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
        _product(maya_om, qx, qz)
    )


@pytest.mark.parametrize(
    ("output_child", "component_index"),
    [
        ("outputQuatX", 0),
        ("outputQuatY", 1),
        ("outputQuatZ", 2),
        ("outputQuatW", 3),
    ],
)
def test_output_children_can_be_requested_directly(
    maya_cmds,
    maya_om,
    output_child,
    component_index,
):
    _load_bd_util_nodes(maya_cmds)

    first = _axis_quat("x", 50.0)
    second = _axis_quat("y", 70.0)
    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
    _set_quat(maya_cmds, f"{node}.inputQuat[0]", first)
    _set_quat(maya_cmds, f"{node}.inputQuat[1]", second)

    expected = _product(maya_om, first, second)[component_index]
    assert maya_cmds.getAttr(f"{node}.{output_child}") == pytest.approx(
        expected
    )


def test_child_input_dependencies_cover_output_compound(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    node = maya_cmds.createNode("bdQuat_MultiplyMulti")
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
    for input_child in (
        "inputQuatX",
        "inputQuatY",
        "inputQuatZ",
        "inputQuatW",
    ):
        affected = node_fn.getAffectedAttributes(
            node_fn.attribute(input_child)
        )
        assert {
            maya_om.MFnAttribute(attribute).name for attribute in affected
        } == expected


def test_standard_quat_nodes_connect_without_conversion_nodes(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    source = maya_cmds.createNode("quatProd")
    product = maya_cmds.createNode("bdQuat_MultiplyMulti")
    destination = maya_cmds.createNode("quatToEuler")
    value = _axis_quat("z", 80.0)
    _set_quat(maya_cmds, f"{source}.input1Quat", value)
    maya_cmds.connectAttr(
        f"{source}.outputQuat", f"{product}.inputQuat[4]", force=True
    )
    maya_cmds.connectAttr(
        f"{product}.outputQuat", f"{destination}.inputQuat", force=True
    )

    assert _get_quat(maya_cmds, f"{product}.outputQuat") == pytest.approx(
        value
    )
    assert not maya_cmds.ls(type="unitConversion")


def test_node_operator_supports_quat_values_and_next(
    modifier_manager,
    maya_cmds,
    maya_om,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_quat_multiply_multi import (
        BdQuatMultiplyMulti,
    )

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdQuat_MultiplyMulti(name="product")
    node.inputQuat[next].set(_axis_quat("x", 30.0))
    node.inputQuat[next].set(_axis_quat("y", 50.0))
    modifier_manager.do_it_dg()

    assert isinstance(node, BdQuatMultiplyMulti)
    assert isinstance(node.outputQuat.get(), bdu.Quat)
    assert node.outputQuat.get().as_tuple() == pytest.approx(
        _product(
            maya_om,
            _axis_quat("x", 30.0),
            _axis_quat("y", 50.0),
        )
    )
    assert isinstance(
        nodes.existing.bdQuat_MultiplyMulti(node.name),
        BdQuatMultiplyMulti,
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
        node = maya_cmds.createNode("bdQuat_MultiplyMulti")
        qx = _axis_quat("x", 30.0)
        qy = _axis_quat("y", 50.0)
        _set_quat(maya_cmds, f"{node}.inputQuat[2]", qx)
        _set_quat(maya_cmds, f"{node}.inputQuat[9]", qy)
        assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
            _product(maya_om, qx, qy)
        )

        maya_cmds.setAttr(f"{node}.inputQuat[2].inputQuatX", 0.5)
        changed_qx = (0.5, qx[1], qx[2], qx[3])
        assert _get_quat(maya_cmds, f"{node}.outputQuat") == pytest.approx(
            _product(maya_om, changed_qx, qy)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_node_survives_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    maya_om,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    qx = _axis_quat("x", 25.0)
    qy = _axis_quat("y", -75.0)
    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    node = nodes.create.bdQuat_MultiplyMulti(name="product")
    node.inputQuat[2].set(qx)
    node.inputQuat[9].set(qy)
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_quat_multiply_multi.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    existing = existing_nodes.existing.bdQuat_MultiplyMulti("product")
    assert existing.outputQuat.get().as_tuple() == pytest.approx(
        _product(maya_om, qx, qy)
    )
