from __future__ import annotations

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


def _set_quat(maya_cmds, plug: str, value) -> None:
    maya_cmds.setAttr(plug, *value, type="double4")


def _get_quat(maya_cmds, plug: str) -> tuple[float, float, float, float]:
    return tuple(maya_cmds.getAttr(plug)[0])


def test_node_ids_attributes_and_defaults(maya_cmds, maya_om):
    _load_bd_util_nodes(maya_cmds)

    euler = maya_cmds.createNode("bdEuler_Value")
    quat = maya_cmds.createNode("bdQuat_Value")
    selection = maya_om.MSelectionList()
    selection.add(euler)
    selection.add(quat)

    euler_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    quat_fn = maya_om.MFnDependencyNode(selection.getDependNode(1))
    assert euler_fn.typeId.id() == 0x0007F08F
    assert quat_fn.typeId.id() == 0x0007F090

    assert maya_cmds.attributeQuery(
        "value", node=euler, listChildren=True
    ) == ["valueX", "valueY", "valueZ"]
    assert maya_cmds.attributeQuery("value", node=quat, listChildren=True) == [
        "valueX",
        "valueY",
        "valueZ",
        "valueW",
    ]
    assert maya_cmds.attributeQuery(
        "rotateOrder", node=euler, listEnum=True
    ) == ["xyz:yzx:zxy:xzy:yxz:zyx"]
    assert _get_angles(maya_cmds, f"{euler}.value") == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{euler}.rotateOrder") == 0
    assert _get_quat(maya_cmds, f"{quat}.value") == pytest.approx(
        (0.0, 0.0, 0.0, 1.0)
    )


def test_value_attributes_are_editable_and_keyable(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    euler = maya_cmds.createNode("bdEuler_Value")
    quat = maya_cmds.createNode("bdQuat_Value")
    for node, attributes in (
        (euler, ("value", "valueX", "valueY", "valueZ", "rotateOrder")),
        (quat, ("value", "valueX", "valueY", "valueZ", "valueW")),
    ):
        for attribute in attributes:
            for flag in ("readable", "writable", "storable", "keyable"):
                assert maya_cmds.attributeQuery(
                    attribute,
                    node=node,
                    **{flag: True},
                )


def test_euler_value_relays_continuous_angles_and_rotate_order(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    source = maya_cmds.createNode("transform", name="source")
    relay = maya_cmds.createNode("bdEuler_Value", name="relay")
    target = maya_cmds.createNode("transform", name="target")
    maya_cmds.connectAttr(f"{source}.rotate", f"{relay}.value")
    maya_cmds.connectAttr(f"{relay}.value", f"{target}.rotate")
    maya_cmds.connectAttr(f"{source}.rotateOrder", f"{relay}.rotateOrder")
    maya_cmds.connectAttr(f"{relay}.rotateOrder", f"{target}.rotateOrder")

    expected = (450.0, -725.0, 1080.0)
    maya_cmds.setAttr(f"{source}.rotate", *expected, type="double3")
    maya_cmds.setAttr(f"{source}.rotateOrder", 5)

    assert _get_angles(maya_cmds, f"{relay}.value") == pytest.approx(expected)
    assert _get_angles(maya_cmds, f"{target}.rotate") == pytest.approx(
        expected
    )
    assert maya_cmds.getAttr(f"{relay}.rotateOrder") == 5
    assert maya_cmds.getAttr(f"{target}.rotateOrder") == 5
    assert not maya_cmds.ls(type="unitConversion")


def test_quat_value_relays_raw_non_unit_and_signed_values(maya_cmds):
    _load_bd_util_nodes(maya_cmds)

    source = maya_cmds.createNode("bdQuat_Value", name="source")
    relay = maya_cmds.createNode("bdQuat_Value", name="relay")
    target = maya_cmds.createNode("bdQuat_Value", name="target")
    maya_cmds.connectAttr(f"{source}.value", f"{relay}.value")
    maya_cmds.connectAttr(f"{relay}.value", f"{target}.value")

    raw = (2.0, -3.0, 4.0, -5.0)
    _set_quat(maya_cmds, f"{source}.value", raw)
    assert _get_quat(maya_cmds, f"{relay}.value") == pytest.approx(raw)
    assert _get_quat(maya_cmds, f"{target}.value") == pytest.approx(raw)


def test_standard_quat_nodes_connect_without_conversion_nodes(maya_cmds):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.loadPlugin("quatNodes", quiet=True)

    source = maya_cmds.createNode("eulerToQuat")
    relay = maya_cmds.createNode("bdQuat_Value")
    destination = maya_cmds.createNode("quatToEuler")
    maya_cmds.connectAttr(f"{source}.outputQuat", f"{relay}.value")
    maya_cmds.connectAttr(f"{relay}.value", f"{destination}.inputQuat")
    maya_cmds.setAttr(
        f"{source}.inputRotate", 20.0, -35.0, 80.0, type="double3"
    )

    assert _get_quat(maya_cmds, f"{relay}.value") == pytest.approx(
        _get_quat(maya_cmds, f"{source}.outputQuat")
    )
    assert not maya_cmds.ls(type="unitConversion")


def test_node_operator_returns_rotation_value_types(
    modifier_manager,
    maya_cmds,
):
    _load_bd_util_nodes(maya_cmds)

    from bd_util.maya.node.operator.node.dg.bd_euler_value import BdEulerValue
    from bd_util.maya.node.operator.node.dg.bd_quat_value import BdQuatValue

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    euler = nodes.create.bdEuler_Value(name="euler_value")
    quat = nodes.create.bdQuat_Value(name="quat_value")
    euler.value.set((450.0, -725.0, 1080.0))
    euler.rotateOrder.set(4)
    quat.value.set((2.0, -3.0, 4.0, -5.0))
    modifier_manager.do_it_dg()

    assert isinstance(euler, BdEulerValue)
    assert isinstance(euler.value.get(), bdu.DoubleAngle3)
    assert euler.value.get().as_tuple() == pytest.approx(
        (450.0, -725.0, 1080.0)
    )
    assert euler.rotateOrder.get() == 4
    assert isinstance(quat, BdQuatValue)
    assert isinstance(quat.value.get(), bdu.Quat)
    assert quat.value.get().as_tuple() == pytest.approx((2.0, -3.0, 4.0, -5.0))
    assert isinstance(nodes.existing.bdEuler_Value(euler.name), BdEulerValue)
    assert isinstance(nodes.existing.bdQuat_Value(quat.name), BdQuatValue)


@pytest.mark.parametrize("evaluation_mode", ["off", "serial", "parallel"])
def test_dirty_updates_match_in_all_evaluation_modes(
    maya_cmds,
    evaluation_mode,
):
    _load_bd_util_nodes(maya_cmds)

    previous_mode = maya_cmds.evaluationManager(query=True, mode=True)[0]
    try:
        maya_cmds.evaluationManager(mode=evaluation_mode)
        euler_source = maya_cmds.createNode("bdEuler_Value")
        euler_target = maya_cmds.createNode("bdEuler_Value")
        quat_source = maya_cmds.createNode("bdQuat_Value")
        quat_target = maya_cmds.createNode("bdQuat_Value")
        maya_cmds.connectAttr(f"{euler_source}.value", f"{euler_target}.value")
        maya_cmds.connectAttr(f"{quat_source}.value", f"{quat_target}.value")

        maya_cmds.setAttr(
            f"{euler_source}.value", 10.0, 20.0, 30.0, type="double3"
        )
        _set_quat(maya_cmds, f"{quat_source}.value", (1.0, 2.0, 3.0, 4.0))
        assert _get_angles(
            maya_cmds, f"{euler_target}.value"
        ) == pytest.approx((10.0, 20.0, 30.0))
        assert _get_quat(maya_cmds, f"{quat_target}.value") == pytest.approx(
            (1.0, 2.0, 3.0, 4.0)
        )

        maya_cmds.setAttr(f"{euler_source}.valueY", -400.0)
        maya_cmds.setAttr(f"{quat_source}.valueW", -8.0)
        assert _get_angles(
            maya_cmds, f"{euler_target}.value"
        ) == pytest.approx((10.0, -400.0, 30.0))
        assert _get_quat(maya_cmds, f"{quat_target}.value") == pytest.approx(
            (1.0, 2.0, 3.0, -8.0)
        )
    finally:
        maya_cmds.evaluationManager(mode=previous_mode)


def test_values_survive_scene_save_and_reload(
    modifier_manager,
    maya_cmds,
    tmp_path,
):
    _load_bd_util_nodes(maya_cmds)

    nodes = bdu.Nodes(modifier_manager=modifier_manager)
    euler = nodes.create.bdEuler_Value(name="euler_value")
    quat = nodes.create.bdQuat_Value(name="quat_value")
    euler.value.set((450.0, -725.0, 1080.0))
    euler.rotateOrder.set(3)
    quat.value.set((2.0, -3.0, 4.0, -5.0))
    modifier_manager.do_it_dg()

    scene_path = tmp_path / "bd_rotation_value.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    existing_nodes = bdu.Nodes(modifier_manager=bdu.ModifierManager())
    reloaded_euler = existing_nodes.existing.bdEuler_Value("euler_value")
    reloaded_quat = existing_nodes.existing.bdQuat_Value("quat_value")
    assert reloaded_euler.value.get().as_tuple() == pytest.approx(
        (450.0, -725.0, 1080.0)
    )
    assert reloaded_euler.rotateOrder.get() == 3
    assert reloaded_quat.value.get().as_tuple() == pytest.approx(
        (2.0, -3.0, 4.0, -5.0)
    )
