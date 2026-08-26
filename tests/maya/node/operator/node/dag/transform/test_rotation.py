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

_SET_ROTATION_METHOD_CASES = (
    (
        "transform",
        "set_rotate_axis_with_rotate",
        "rotateAxis",
        (),
    ),
    (
        "transform",
        "set_rotate_with_rotate_axis",
        "rotate",
        (),
    ),
    (
        "joint",
        "set_rotate_axis_with_rotate",
        "rotateAxis",
        ("jointOrient",),
    ),
    (
        "joint",
        "set_rotate_with_rotate_axis",
        "rotate",
        ("jointOrient",),
    ),
    (
        "joint",
        "set_joint_orient_with_rotate",
        "jointOrient",
        ("rotateAxis",),
    ),
    (
        "joint",
        "set_rotate_with_joint_orient",
        "rotate",
        ("rotateAxis",),
    ),
)


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _rotation_attributes(node_type: str) -> tuple[str, ...]:
    if node_type == "joint":
        return "rotateAxis", "rotate", "jointOrient"
    return "rotateAxis", "rotate"


def _set_initial_rotation_values(maya_cmds, node_name, node_type):
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
        407.0,
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


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute", "unchanged_attributes"),
    _SET_ROTATION_METHOD_CASES,
)
def test_set_rotation_methods_preserve_matrix_and_support_undo_redo(
    new_scene,
    maya_cmds,
    node_type,
    method_name,
    target_attribute,
    unchanged_attributes,
    rotate_order,
):
    import bd_util as bdu

    target_value = (37.0, -28.0, 415.0)
    node_name = maya_cmds.createNode(node_type, name=f"test_{node_type}")
    maya_cmds.setAttr(f"{node_name}.rotateOrder", rotate_order)
    _set_initial_rotation_values(maya_cmds, node_name, node_type)

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    node = getattr(nodes.existing, node_type)(node_name)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(node, name).get()) for name in attribute_names
    }
    original_matrix = node.matrix.get().matrix

    assert getattr(node, method_name)(target_value) is node
    assert {
        name: tuple(getattr(node, name).get()) for name in attribute_names
    } == original_values

    mod.do_it_dg()

    _assert_matrix_close(node.matrix.get().matrix, original_matrix)
    assert getattr(node, target_attribute).get() == pytest.approx(target_value)
    for attribute_name in unchanged_attributes:
        assert getattr(node, attribute_name).get() == pytest.approx(
            original_values[attribute_name]
        )
    changed_values = {
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
    for attribute_name, changed_value in changed_values.items():
        assert getattr(node, attribute_name).get() == pytest.approx(
            changed_value
        )


def test_set_rotation_methods_accept_three_scalar_values(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="test_transform")
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    assert node.set_rotate_axis_with_rotate(10.0, 20.0, 30.0) is node
    nodes.modifier_manager.do_it_dg()

    assert node.rotateAxis.get() == pytest.approx((10.0, 20.0, 30.0))


def test_set_rotation_methods_accept_compound_rotation_value(
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
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)
    rotation_value = node.rotateAxis.get()

    assert node.set_rotate_axis_with_rotate(rotation_value) is node
    nodes.modifier_manager.do_it_dg()

    assert node.rotateAxis.get() == rotation_value


@pytest.mark.parametrize(
    "values",
    (
        (10.0,),
        (10.0, 20.0),
        (10.0, 20.0, 30.0, 40.0),
        ([10.0, 20.0],),
        ([10.0, object(), 30.0],),
    ),
)
def test_set_rotation_methods_reject_invalid_values_before_queuing_changes(
    new_scene,
    maya_cmds,
    values,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="test_transform")
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)
    original_rotate_axis = node.rotateAxis.get()
    original_rotate = node.rotate.get()

    with pytest.raises(TypeError, match="set_rotate_axis_with_rotate"):
        node.set_rotate_axis_with_rotate(*values)

    nodes.modifier_manager.do_it_dg()
    assert node.rotateAxis.get() == original_rotate_axis
    assert node.rotate.get() == original_rotate


@pytest.mark.parametrize(
    ("node_type", "method_name", "locked_attribute"),
    (
        ("transform", "set_rotate_axis_with_rotate", "rotateY"),
        ("transform", "set_rotate_with_rotate_axis", "rotateAxisZ"),
        ("joint", "set_joint_orient_with_rotate", "jointOrientX"),
        ("joint", "set_rotate_with_joint_orient", "rotateZ"),
    ),
)
def test_set_rotation_methods_reject_locked_written_plug(
    new_scene,
    maya_cmds,
    node_type,
    method_name,
    locked_attribute,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode(node_type, name=f"test_{node_type}")
    maya_cmds.setAttr(f"{node_name}.{locked_attribute}", lock=True)
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, node_type)(node_name)

    with pytest.raises(RuntimeError, match=locked_attribute):
        getattr(node, method_name)((10.0, 20.0, 30.0))


@pytest.mark.parametrize(
    ("method_name", "untouched_attribute"),
    (
        ("set_rotate_axis_with_rotate", "jointOrientX"),
        ("set_joint_orient_with_rotate", "rotateAxisX"),
    ),
)
def test_set_joint_rotation_methods_ignore_blocked_untouched_plug(
    new_scene,
    maya_cmds,
    method_name,
    untouched_attribute,
):
    import bd_util as bdu

    joint_name = maya_cmds.createNode("joint", name="test_joint")
    _set_initial_rotation_values(maya_cmds, joint_name, "joint")
    maya_cmds.setAttr(f"{joint_name}.{untouched_attribute}", lock=True)
    nodes = bdu.Nodes()
    joint = nodes.existing.joint(joint_name)
    original_matrix = joint.matrix.get().matrix

    assert getattr(joint, method_name)((10.0, 20.0, 30.0)) is joint
    nodes.modifier_manager.do_it_dg()

    _assert_matrix_close(joint.matrix.get().matrix, original_matrix)


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
