# coding: utf-8
from __future__ import annotations

import pytest

_ROTATION_METHOD_CASES = (
    ("transform", "rotation_to_rotate", "rotate"),
    ("transform", "rotation_to_rotate_axis", "rotateAxis"),
    ("joint", "rotation_to_rotate", "rotate"),
    ("joint", "rotation_to_rotate_axis", "rotateAxis"),
    ("joint", "rotation_to_joint_orient", "jointOrient"),
)


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _rotation_attributes(node_type: str) -> tuple[str, ...]:
    if node_type == "joint":
        return "rotateAxis", "rotate", "jointOrient"
    return "rotateAxis", "rotate"


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute"),
    _ROTATION_METHOD_CASES,
)
def test_rotation_to_methods_preserve_matrix_and_support_undo_redo(
    new_scene,
    maya_cmds,
    node_type,
    method_name,
    target_attribute,
    rotate_order,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode(node_type, name=f"test_{node_type}")
    maya_cmds.setAttr(f"{node_name}.rotateOrder", rotate_order)
    maya_cmds.setAttr(
        f"{node_name}.rotateAxis",
        -120.0,
        89.0,
        370.0,
        type="double3",
    )
    maya_cmds.setAttr(
        f"{node_name}.rotate",
        225.0,
        -91.0,
        47.0,
        type="double3",
    )
    if node_type == "joint":
        maya_cmds.setAttr(
            f"{node_name}.jointOrient",
            -33.0,
            181.0,
            92.0,
            type="double3",
        )

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = getattr(nodes.existing, node_type)(node_name)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(node, name).get()) for name in attribute_names
    }
    original_matrix = node.matrix.get().matrix

    assert getattr(node, method_name)() is node
    assert {
        name: tuple(getattr(node, name).get()) for name in attribute_names
    } == original_values

    mod.do_it_dg()

    _assert_matrix_close(node.matrix.get().matrix, original_matrix)
    assert node.rotateOrder.get() == rotate_order
    for attribute_name in attribute_names:
        if attribute_name != target_attribute:
            assert getattr(node, attribute_name).get() == pytest.approx(
                (0.0, 0.0, 0.0)
            )
    consolidated_values = {
        name: tuple(getattr(node, name).get()) for name in attribute_names
    }

    mod.undo_it()

    _assert_matrix_close(node.matrix.get().matrix, original_matrix)
    for attribute_name, original_value in original_values.items():
        assert getattr(node, attribute_name).get() == pytest.approx(
            original_value
        )

    mod.redo_it()

    _assert_matrix_close(node.matrix.get().matrix, original_matrix)
    for attribute_name, consolidated_value in consolidated_values.items():
        assert getattr(node, attribute_name).get() == pytest.approx(
            consolidated_value
        )


def test_rotation_to_rejects_locked_plug_before_queuing_changes(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="test_transform")
    maya_cmds.setAttr(
        f"{node_name}.rotateAxis",
        10.0,
        20.0,
        30.0,
        type="double3",
    )
    maya_cmds.setAttr(
        f"{node_name}.rotate",
        40.0,
        50.0,
        60.0,
        type="double3",
    )
    maya_cmds.setAttr(f"{node_name}.rotateY", lock=True)
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)
    original_rotate_axis = node.rotateAxis.get()
    original_rotate = node.rotate.get()

    with pytest.raises(RuntimeError, match=r"test_transform\.rotateY"):
        node.rotation_to_rotate_axis()

    assert node.rotateAxis.get() == original_rotate_axis
    assert node.rotate.get() == original_rotate


def test_joint_rotation_to_rejects_incoming_joint_orient_connection(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    driver_name = maya_cmds.createNode("transform", name="driver")
    joint_name = maya_cmds.createNode("joint", name="test_joint")
    maya_cmds.connectAttr(
        f"{driver_name}.rotateX",
        f"{joint_name}.jointOrientX",
    )
    nodes = bdu.Nodes()
    joint = nodes.existing.joint(joint_name)

    with pytest.raises(RuntimeError, match=r"test_joint\.jointOrientX"):
        joint.rotation_to_rotate()


def test_rotation_to_rejects_keyframed_rotation(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="test_transform")
    maya_cmds.setKeyframe(node_name, attribute="rotateAxisZ", value=30.0)
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    with pytest.raises(RuntimeError, match=r"test_transform\.rotateAxisZ"):
        node.rotation_to_rotate()
