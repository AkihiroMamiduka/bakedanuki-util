# coding: utf-8
from __future__ import annotations

import itertools

import pytest

_REMAP_METHOD_CASES = (
    ("transform", "remap_axes_to_rotate", "rotate"),
    ("transform", "remap_axes_to_rotate_axis", "rotateAxis"),
    ("joint", "remap_axes_to_rotate", "rotate"),
    ("joint", "remap_axes_to_rotate_axis", "rotateAxis"),
    ("joint", "remap_axes_to_joint_orient", "jointOrient"),
)
_AXIS_NAMES = ("x", "y", "z")
_AXIS_VALUES = {
    "x": (1.0, 0.0, 0.0),
    "y": (0.0, 1.0, 0.0),
    "z": (0.0, 0.0, 1.0),
}
_ALL_REMAP_CASES = tuple(
    (
        source_axes,
        tuple(
            f"{sign}{axis_name}"
            for sign, axis_name in zip(signs, remapped_axes)
        ),
    )
    for source_axes in itertools.combinations(_AXIS_NAMES, 2)
    for remapped_axes in itertools.permutations(_AXIS_NAMES, 2)
    for signs in itertools.product(("+", "-"), repeat=2)
)


def _matrix(maya_cmds, attribute):
    return maya_cmds.getAttr(attribute)


def _world_rotation(maya_cmds, maya_om, node_name):
    matrix = maya_om.MMatrix(_matrix(maya_cmds, f"{node_name}.worldMatrix[0]"))
    return maya_om.MTransformationMatrix(matrix).rotation(asQuaternion=True)


def _axis_vector(maya_om, value):
    sign = -1.0 if value.startswith("-") else 1.0
    axis_name = value[-1]
    vector = _AXIS_VALUES[axis_name]
    return maya_om.MVector(*(component * sign for component in vector))


def _assert_rotation_close(actual, expected, *, abs_tolerance=1.0e-9):
    dot = (
        actual.x * expected.x
        + actual.y * expected.y
        + actual.z * expected.z
        + actual.w * expected.w
    )
    assert abs(dot) == pytest.approx(1.0, abs=abs_tolerance)


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _assert_axis_remap(maya_om, before, after, mappings):
    for source_axis, remapped_axis in mappings.items():
        before_direction = maya_om.MVector(
            *_AXIS_VALUES[source_axis]
        ).rotateBy(before)
        after_direction = _axis_vector(maya_om, remapped_axis).rotateBy(after)
        assert before_direction * after_direction == pytest.approx(
            1.0,
            abs=1.0e-9,
        )

    after_x = maya_om.MVector(1.0, 0.0, 0.0).rotateBy(after)
    after_y = maya_om.MVector(0.0, 1.0, 0.0).rotateBy(after)
    after_z = maya_om.MVector(0.0, 0.0, 1.0).rotateBy(after)
    assert (after_x ^ after_y) * after_z == pytest.approx(1.0, abs=1.0e-9)


def _rotation_attributes(node_type):
    if node_type == "joint":
        return "rotateAxis", "rotate", "jointOrient"
    return "rotateAxis", "rotate"


def _set_offset_parent_rotation(maya_cmds, maya_om, node_name, z_degrees):
    matrix = maya_om.MTransformationMatrix()
    matrix.setRotation(
        maya_om.MEulerRotation(
            0.0,
            0.0,
            maya_om.MAngle(
                z_degrees,
                maya_om.MAngle.kDegrees,
            ).asRadians(),
        )
    )
    maya_cmds.setAttr(
        f"{node_name}.offsetParentMatrix",
        *list(matrix.asMatrix()),
        type="matrix",
    )


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute"),
    _REMAP_METHOD_CASES,
)
def test_axis_remap_methods_use_before_to_after_mapping_and_support_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    target_attribute,
    rotate_order,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        node_type,
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{parent}.rotate", 13.0, -27.0, 19.0)
    maya_cmds.setAttr(f"{destination}.rotateOrder", rotate_order)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 9.0, -14.0, 21.0)
    maya_cmds.setAttr(f"{destination}.rotate", 33.0, 16.0, -27.0)
    if node_type == "joint":
        maya_cmds.setAttr(f"{destination}.jointOrient", -12.0, 25.0, 38.0)
    _set_offset_parent_rotation(
        maya_cmds,
        maya_om,
        destination,
        23.0,
    )

    nodes = bdu.Nodes()
    destination_node = getattr(nodes.existing, node_type)(destination)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }
    before_rotation = _world_rotation(maya_cmds, maya_om, destination)

    assert (
        getattr(destination_node, method_name)(x="-y", z="x")
        is destination_node
    )
    assert {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    } == original_values

    nodes.modifier_manager.do_it_dg()

    after_rotation = _world_rotation(maya_cmds, maya_om, destination)
    _assert_axis_remap(
        maya_om,
        before_rotation,
        after_rotation,
        {"x": "-y", "z": "+x"},
    )
    before_x = maya_om.MVector(1.0, 0.0, 0.0).rotateBy(before_rotation)
    before_y = maya_om.MVector(0.0, 1.0, 0.0).rotateBy(before_rotation)
    after_y = maya_om.MVector(0.0, 1.0, 0.0).rotateBy(after_rotation)
    after_z = maya_om.MVector(0.0, 0.0, 1.0).rotateBy(after_rotation)
    assert before_x * (-after_y) == pytest.approx(1.0, abs=1.0e-9)
    assert before_y * (-after_z) == pytest.approx(1.0, abs=1.0e-9)
    for attribute_name, original_value in original_values.items():
        if attribute_name != target_attribute:
            assert getattr(
                destination_node, attribute_name
            ).get() == pytest.approx(original_value)

    nodes.modifier_manager.undo_it()
    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        before_rotation,
    )
    nodes.modifier_manager.redo_it()
    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        after_rotation,
    )


@pytest.mark.parametrize(
    ("source_axes", "remapped_axes"),
    _ALL_REMAP_CASES,
)
def test_axis_remap_supports_every_two_axis_signed_mapping(
    new_scene,
    maya_cmds,
    maya_om,
    source_axes,
    remapped_axes,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{parent}.rotate", -17.0, 29.0, 11.0)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 7.0, -13.0, 19.0)
    maya_cmds.setAttr(f"{destination}.rotate", 23.0, 31.0, -37.0)
    mappings = dict(zip(source_axes, remapped_axes))
    before_rotation = _world_rotation(maya_cmds, maya_om, destination)

    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    destination_node.remap_axes_to_rotate(**mappings)
    nodes.modifier_manager.do_it_dg()

    _assert_axis_remap(
        maya_om,
        before_rotation,
        _world_rotation(maya_cmds, maya_om, destination),
        mappings,
    )


def test_axis_remap_can_compensate_direct_child_world_pose(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    transform_child = maya_cmds.createNode(
        "transform",
        name="transform_child",
        parent=destination,
    )
    joint_child = maya_cmds.createNode(
        "joint",
        name="joint_child",
        parent=destination,
    )
    maya_cmds.setAttr(f"{destination}.rotate", 11.0, -17.0, 23.0)
    maya_cmds.setAttr(f"{transform_child}.translate", 3.0, 4.0, -2.0)
    maya_cmds.setAttr(f"{transform_child}.rotate", -7.0, 13.0, 19.0)
    maya_cmds.setAttr(f"{joint_child}.translate", -4.0, 2.0, 5.0)
    maya_cmds.setAttr(f"{joint_child}.rotate", 5.0, -11.0, 29.0)
    maya_cmds.setAttr(f"{joint_child}.jointOrient", 3.0, 7.0, -13.0)
    original_child_matrices = {
        child: _matrix(maya_cmds, f"{child}.worldMatrix[0]")
        for child in (transform_child, joint_child)
    }
    original_joint_rotate = tuple(
        maya_cmds.getAttr(f"{joint_child}.rotate")[0]
    )

    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    destination_node.remap_axes_to_rotate(
        x="-y",
        z="x",
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr="jointOrient",
    )
    nodes.modifier_manager.do_it_dg()

    for child, original_matrix in original_child_matrices.items():
        _assert_matrix_close(
            _matrix(maya_cmds, f"{child}.worldMatrix[0]"),
            original_matrix,
        )
    assert tuple(
        maya_cmds.getAttr(f"{joint_child}.rotate")[0]
    ) == pytest.approx(original_joint_rotate)


@pytest.mark.parametrize(
    ("keyword_arguments", "error_type", "message"),
    (
        ({}, ValueError, "exactly two"),
        ({"x": "y"}, ValueError, "exactly two"),
        ({"x": "y", "y": "z", "z": "x"}, ValueError, "exactly two"),
        ({"x": "y", "z": "-y"}, ValueError, "distinct"),
        ({"x": object(), "z": "y"}, TypeError, "x"),
        ({"x": "X", "z": "y"}, ValueError, "signed axis"),
        ({"x": "++x", "z": "y"}, ValueError, "signed axis"),
        (
            {
                "x": "y",
                "z": "x",
                "compensate_child_translate": True,
            },
            ValueError,
            "compensate_children=True",
        ),
        (
            {"x": "y", "z": "x", "compensate_children": 1},
            TypeError,
            "compensate_children",
        ),
        (
            {"x": "y", "z": "x", "joint_child_compensation_attr": "axis"},
            ValueError,
            "joint_child_compensation_attr",
        ),
    ),
)
def test_axis_remap_rejects_invalid_values_without_queueing_changes(
    new_scene,
    maya_cmds,
    keyword_arguments,
    error_type,
    message,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotate", 10.0, 20.0, 30.0)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    original_rotate = destination_node.rotate.get()

    with pytest.raises(error_type, match=message):
        destination_node.remap_axes_to_rotate(**keyword_arguments)

    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get() == original_rotate


def test_axis_remap_noop_ignores_locked_rotation_plugs(new_scene, maya_cmds):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotate", lock=True)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    assert (
        destination_node.remap_axes_to_rotate(x="x", z="z") is destination_node
    )
    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get().as_tuple() == (0.0, 0.0, 0.0)


def test_axis_remap_rejects_blocked_selected_rotation_plug(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotateX", lock=True)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match="rotateX"):
        destination_node.remap_axes_to_rotate(x="-y", z="x")
