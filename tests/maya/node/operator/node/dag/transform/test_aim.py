# coding: utf-8
from __future__ import annotations

import math

import pytest

_AIM_METHOD_CASES = (
    ("transform", "aim_to_rotate", "rotate"),
    ("transform", "aim_to_rotate_axis", "rotateAxis"),
    ("joint", "aim_to_rotate", "rotate"),
    ("joint", "aim_to_rotate_axis", "rotateAxis"),
    ("joint", "aim_to_joint_orient", "jointOrient"),
)

_CHILD_AIM_METHOD_CASES = (
    ("transform", "aim_child_to_rotate", "rotate"),
    ("transform", "aim_child_to_rotate_axis", "rotateAxis"),
    ("joint", "aim_child_to_rotate", "rotate"),
    ("joint", "aim_child_to_rotate_axis", "rotateAxis"),
    ("joint", "aim_child_to_joint_orient", "jointOrient"),
)


def _matrix(maya_cmds, attribute):
    return maya_cmds.getAttr(attribute)


def _world_rotation(maya_cmds, maya_om, node_name):
    matrix = maya_om.MMatrix(_matrix(maya_cmds, f"{node_name}.worldMatrix[0]"))
    return maya_om.MTransformationMatrix(matrix).rotation(asQuaternion=True)


def _world_rotate_pivot(maya_cmds, node_name):
    return tuple(
        maya_cmds.xform(
            node_name, query=True, worldSpace=True, rotatePivot=True
        )
    )


def _normalized(maya_om, value):
    vector = maya_om.MVector(*value)
    vector.normalize()
    return vector


def _orthogonalized(maya_om, value, axis):
    vector = _normalized(maya_om, value)
    vector -= axis * (vector * axis)
    vector.normalize()
    return vector


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


def _assert_aim_axes(
    maya_cmds,
    maya_om,
    node_name,
    *,
    aim_point,
    aim_axis,
    up_point=None,
    up_axis=(0.0, 1.0, 0.0),
    origin=None,
):
    if origin is None:
        origin = _world_rotate_pivot(maya_cmds, node_name)
    origin = maya_om.MPoint(*origin)
    world_rotation = _world_rotation(maya_cmds, maya_om, node_name)
    local_aim_axis = _normalized(maya_om, aim_axis)
    actual_aim_axis = local_aim_axis.rotateBy(world_rotation)
    expected_aim_axis = _normalized(
        maya_om,
        maya_om.MPoint(*aim_point) - origin,
    )
    assert actual_aim_axis * expected_aim_axis == pytest.approx(
        1.0,
        abs=1.0e-9,
    )

    if up_point is None:
        return
    local_up_axis = _orthogonalized(
        maya_om,
        up_axis,
        local_aim_axis,
    )
    actual_up_axis = local_up_axis.rotateBy(world_rotation)
    expected_up_axis = _orthogonalized(
        maya_om,
        maya_om.MPoint(*up_point) - origin,
        expected_aim_axis,
    )
    assert actual_up_axis * expected_up_axis == pytest.approx(
        1.0,
        abs=1.0e-9,
    )


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
    _AIM_METHOD_CASES,
)
def test_aim_methods_set_selected_attribute_and_support_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    target_attribute,
    rotate_order,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="destination_parent")
    destination = maya_cmds.createNode(
        node_type,
        name="destination",
        parent=parent,
    )
    aim_target = maya_cmds.createNode("transform", name="aim_target")
    up_target = maya_cmds.createNode("transform", name="up_target")
    maya_cmds.setAttr(f"{parent}.translate", 2.0, -3.0, 4.0)
    maya_cmds.setAttr(f"{parent}.rotate", 13.0, -27.0, 19.0)
    maya_cmds.setAttr(f"{destination}.translate", 1.0, 2.0, -3.0)
    maya_cmds.setAttr(f"{destination}.rotateOrder", rotate_order)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 9.0, -14.0, 21.0)
    maya_cmds.setAttr(f"{destination}.rotate", 33.0, 16.0, -27.0)
    maya_cmds.setAttr(f"{destination}.rotatePivot", 0.7, -0.8, 0.9)
    if node_type == "joint":
        maya_cmds.setAttr(
            f"{destination}.jointOrient",
            -12.0,
            25.0,
            38.0,
        )
    _set_offset_parent_rotation(
        maya_cmds,
        maya_om,
        destination,
        23.0,
    )
    maya_cmds.setAttr(f"{aim_target}.translate", 9.0, 4.0, -6.0)
    maya_cmds.setAttr(f"{aim_target}.rotatePivot", 0.5, -0.25, 0.75)
    maya_cmds.setAttr(f"{up_target}.translate", -3.0, 11.0, 5.0)
    maya_cmds.setAttr(f"{up_target}.rotatePivot", -0.4, 0.6, -0.2)

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    destination_node = getattr(nodes.existing, node_type)(destination)
    aim_target_node = nodes.existing.transform(aim_target)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }
    original_rotation = _world_rotation(maya_cmds, maya_om, destination)
    original_translate = destination_node.translate.get()
    original_pivot = _world_rotate_pivot(maya_cmds, destination)
    aim_point = _world_rotate_pivot(maya_cmds, aim_target)
    up_point = _world_rotate_pivot(maya_cmds, up_target)
    aim_axis = (-2.0, 1.0, 0.5)
    up_axis = (0.25, 3.0, 1.0)

    assert (
        getattr(destination_node, method_name)(
            aim_target_node,
            aim_axis=aim_axis,
            up_target=up_target,
            up_axis=up_axis,
        )
        is destination_node
    )
    assert {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    } == original_values

    mod.do_it_dg()

    _assert_aim_axes(
        maya_cmds,
        maya_om,
        destination,
        aim_point=aim_point,
        aim_axis=aim_axis,
        up_point=up_point,
        up_axis=up_axis,
        origin=original_pivot,
    )
    assert destination_node.translate.get() == original_translate
    if node_type == "transform":
        assert _world_rotate_pivot(maya_cmds, destination) == pytest.approx(
            original_pivot
        )
    for attribute_name, original_value in original_values.items():
        if attribute_name != target_attribute:
            assert getattr(
                destination_node,
                attribute_name,
            ).get() == pytest.approx(original_value)
    aimed_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }

    mod.undo_it()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        original_rotation,
    )
    for attribute_name, original_value in original_values.items():
        assert getattr(
            destination_node,
            attribute_name,
        ).get() == pytest.approx(original_value)

    mod.redo_it()

    _assert_aim_axes(
        maya_cmds,
        maya_om,
        destination,
        aim_point=aim_point,
        aim_axis=aim_axis,
        up_point=up_point,
        up_axis=up_axis,
        origin=original_pivot,
    )
    for attribute_name, aimed_value in aimed_values.items():
        assert getattr(
            destination_node,
            attribute_name,
        ).get() == pytest.approx(aimed_value)


@pytest.mark.parametrize("coordinate_space", ("world", "local"))
def test_aim_coordinates_use_requested_space_and_default_world_space(
    new_scene,
    maya_cmds,
    maya_om,
    coordinate_space,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{parent}.translate", 4.0, -3.0, 2.0)
    maya_cmds.setAttr(f"{parent}.rotate", 17.0, 31.0, -23.0)
    maya_cmds.setAttr(f"{destination}.translate", 1.0, -2.0, 3.0)
    maya_cmds.setAttr(f"{destination}.rotatePivot", 0.5, -0.75, 1.25)
    _set_offset_parent_rotation(
        maya_cmds,
        maya_om,
        destination,
        29.0,
    )
    aim_coordinate = (8.0, 2.0, -1.0)
    up_coordinate = (-2.0, 7.0, 4.0)
    if coordinate_space == "local":
        parent_matrix = maya_om.MMatrix(
            _matrix(maya_cmds, f"{destination}.parentMatrix[0]")
        )
        aim_point = maya_om.MPoint(*aim_coordinate) * parent_matrix
        up_point = maya_om.MPoint(*up_coordinate) * parent_matrix
        keyword_arguments = {"coordinate_space": "local"}
    else:
        aim_point = maya_om.MPoint(*aim_coordinate)
        up_point = maya_om.MPoint(*up_coordinate)
        keyword_arguments = {}

    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    destination_node.aim_to_rotate(
        aim_coordinate,
        up_target=up_coordinate,
        **keyword_arguments,
    )
    nodes.modifier_manager.do_it_dg()

    _assert_aim_axes(
        maya_cmds,
        maya_om,
        destination,
        aim_point=(aim_point.x, aim_point.y, aim_point.z),
        aim_axis=(1.0, 0.0, 0.0),
        up_point=(up_point.x, up_point.y, up_point.z),
    )


def test_aim_without_up_uses_shortest_rotation_from_current_pose(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.translate", 2.0, -1.0, 3.0)
    maya_cmds.setAttr(f"{destination}.rotate", 20.0, 30.0, 40.0)
    aim_point = (4.0, 7.0, -3.0)
    aim_axis = _normalized(maya_om, (1.0, 0.0, 0.0))
    origin = maya_om.MPoint(*_world_rotate_pivot(maya_cmds, destination))
    current_rotation = _world_rotation(maya_cmds, maya_om, destination)
    current_aim_axis = aim_axis.rotateBy(current_rotation)
    target_aim_axis = _normalized(
        maya_om,
        maya_om.MPoint(*aim_point) - origin,
    )
    expected_rotation = current_rotation * current_aim_axis.rotateTo(
        target_aim_axis
    )

    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    destination_node.aim_to_rotate(aim_point)
    nodes.modifier_manager.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        expected_rotation,
    )


def test_aim_without_up_uses_current_up_axis_for_antiparallel_aim(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    destination_node.aim_to_rotate((-10.0, 0.0, 0.0))
    nodes.modifier_manager.do_it_dg()

    rotation = _world_rotation(maya_cmds, maya_om, destination)
    world_aim_axis = maya_om.MVector(1.0, 0.0, 0.0).rotateBy(rotation)
    world_up_axis = maya_om.MVector(0.0, 1.0, 0.0).rotateBy(rotation)
    assert world_aim_axis * maya_om.MVector(-1.0, 0.0, 0.0) == pytest.approx(
        1.0,
        abs=1.0e-9,
    )
    assert world_up_axis * maya_om.MVector(0.0, 1.0, 0.0) == pytest.approx(
        1.0,
        abs=1.0e-9,
    )


@pytest.mark.parametrize(
    ("aim_target", "keyword_arguments", "error_type", "message"),
    (
        ((0.0, 0.0, 0.0), {}, ValueError, "aim_target"),
        (
            (1.0, 0.0, 0.0),
            {"aim_axis": (0.0, 0.0, 0.0)},
            ValueError,
            "aim_axis",
        ),
        (
            (1.0, 0.0, 0.0),
            {"up_axis": (0.0, 0.0, 0.0)},
            ValueError,
            "up_axis",
        ),
        (
            (1.0, 0.0, 0.0),
            {"up_axis": (2.0, 0.0, 0.0)},
            ValueError,
            "parallel",
        ),
        (
            (1.0, 0.0, 0.0),
            {"up_target": (2.0, 0.0, 0.0)},
            ValueError,
            "parallel",
        ),
        ((math.inf, 0.0, 0.0), {}, ValueError, "finite"),
        ((1.0, 2.0), {}, TypeError, "aim_target"),
        (
            (1.0, 0.0, 0.0),
            {"coordinate_space": object()},
            TypeError,
            "coordinate_space",
        ),
        (
            (1.0, 0.0, 0.0),
            {"coordinate_space": "object"},
            ValueError,
            "coordinate space",
        ),
    ),
)
def test_aim_rejects_invalid_values_without_queueing_changes(
    new_scene,
    maya_cmds,
    aim_target,
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
        destination_node.aim_to_rotate(
            aim_target,
            **keyword_arguments,
        )

    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get() == original_rotate


@pytest.mark.parametrize("target_kind", ("name", "operator"))
def test_aim_rejects_non_transform_targets(
    new_scene,
    maya_cmds,
    target_kind,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    shape = maya_cmds.createNode(
        "mesh",
        name="targetShape",
        parent=maya_cmds.createNode("transform", name="target"),
    )
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    target = shape if target_kind == "name" else nodes.existing.mesh(shape)

    with pytest.raises(TypeError, match="aim_target.*Transform"):
        destination_node.aim_to_rotate(target)


def test_aim_rejects_missing_node_name(new_scene, maya_cmds):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(ValueError, match="aim_target"):
        destination_node.aim_to_rotate("missing_target")


@pytest.mark.parametrize("instanced_node", ("destination", "aim_target"))
def test_aim_rejects_instanced_nodes(
    new_scene,
    maya_cmds,
    instanced_node,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    aim_target = maya_cmds.createNode("transform", name="aim_target")
    maya_cmds.setAttr(f"{aim_target}.translateX", 10.0)
    maya_cmds.instance(
        destination if instanced_node == "destination" else aim_target
    )
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    aim_target_node = nodes.existing.transform(aim_target)

    with pytest.raises(RuntimeError, match="instanced"):
        destination_node.aim_to_rotate(aim_target_node)


def test_aim_can_compensate_direct_child_world_pose(
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
    maya_cmds.setAttr(f"{destination}.rotatePivot", 2.0, -1.0, 0.5)
    maya_cmds.setAttr(f"{transform_child}.translate", 3.0, 4.0, -2.0)
    maya_cmds.setAttr(f"{transform_child}.rotate", 11.0, -17.0, 23.0)
    maya_cmds.setAttr(f"{joint_child}.translate", -4.0, 2.0, 5.0)
    maya_cmds.setAttr(f"{joint_child}.rotate", -13.0, 19.0, -29.0)
    original_child_matrices = {
        child: _matrix(maya_cmds, f"{child}.worldMatrix[0]")
        for child in (transform_child, joint_child)
    }
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    destination_node.aim_to_rotate(
        (8.0, 7.0, -4.0),
        up_target=(-3.0, 9.0, 6.0),
        compensate_children=True,
        compensate_child_translate=True,
    )
    nodes.modifier_manager.do_it_dg()

    for child, original_matrix in original_child_matrices.items():
        _assert_matrix_close(
            _matrix(maya_cmds, f"{child}.worldMatrix[0]"),
            original_matrix,
        )


def test_aim_noop_ignores_locked_rotation_plugs(new_scene, maya_cmds):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotate", lock=True)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    assert destination_node.aim_to_rotate((10.0, 0.0, 0.0)) is destination_node
    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get().as_tuple() == (0.0, 0.0, 0.0)


def test_aim_rejects_blocked_selected_rotation_plug(new_scene, maya_cmds):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotateZ", lock=True)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match="rotateZ"):
        destination_node.aim_to_rotate((0.0, 10.0, 0.0))


def test_aim_rejects_effectively_singular_parent_matrix(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{parent}.scaleX", 0.0)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match="invertible effective parent"):
        destination_node.aim_to_rotate((0.0, 10.0, 0.0))


@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute"),
    _CHILD_AIM_METHOD_CASES,
)
def test_child_aim_methods_select_transform_child_and_preserve_children(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    target_attribute,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="destination_parent")
    destination = maya_cmds.createNode(
        node_type,
        name="destination",
        parent=parent,
    )
    maya_cmds.createNode("mesh", name="destinationShape", parent=destination)
    first_child = maya_cmds.createNode(
        "transform",
        name="first_child",
        parent=destination,
    )
    aimed_child = maya_cmds.createNode(
        "joint",
        name="aimed_child",
        parent=destination,
    )
    maya_cmds.setAttr(f"{parent}.rotate", 13.0, -21.0, 8.0)
    maya_cmds.setAttr(f"{destination}.translate", 1.0, 2.0, -3.0)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 7.0, -11.0, 17.0)
    maya_cmds.setAttr(f"{destination}.rotate", 23.0, 5.0, -31.0)
    maya_cmds.setAttr(f"{destination}.rotatePivot", 0.4, -0.3, 0.7)
    if node_type == "joint":
        maya_cmds.setAttr(f"{destination}.jointOrient", -9.0, 19.0, 27.0)
    maya_cmds.setAttr(f"{first_child}.translate", -2.0, 3.0, 1.0)
    maya_cmds.setAttr(f"{first_child}.rotate", 11.0, -17.0, 29.0)
    maya_cmds.setAttr(f"{aimed_child}.translate", 5.0, 2.0, -1.0)
    maya_cmds.setAttr(f"{aimed_child}.rotate", -13.0, 7.0, 19.0)
    maya_cmds.setAttr(f"{aimed_child}.jointOrient", 3.0, -5.0, 11.0)

    nodes = bdu.Nodes()
    destination_node = getattr(nodes.existing, node_type)(destination)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }
    original_rotation = _world_rotation(maya_cmds, maya_om, destination)
    original_origin = _world_rotate_pivot(maya_cmds, destination)
    aimed_point = _world_rotate_pivot(maya_cmds, aimed_child)
    original_child_matrices = {
        child: _matrix(maya_cmds, f"{child}.worldMatrix[0]")
        for child in (first_child, aimed_child)
    }
    up_point = (-4.0, 10.0, 6.0)
    aim_axis = (1.0, 0.0, 0.0)
    up_axis = (0.0, 0.0, 1.0)

    assert (
        getattr(destination_node, method_name)(
            1,
            aim_axis=aim_axis,
            up_target=up_point,
            up_axis=up_axis,
        )
        is destination_node
    )
    assert {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    } == original_values

    nodes.modifier_manager.do_it_dg()

    _assert_aim_axes(
        maya_cmds,
        maya_om,
        destination,
        aim_point=aimed_point,
        aim_axis=aim_axis,
        up_point=up_point,
        up_axis=up_axis,
        origin=original_origin,
    )
    for child, original_matrix in original_child_matrices.items():
        _assert_matrix_close(
            _matrix(maya_cmds, f"{child}.worldMatrix[0]"),
            original_matrix,
        )
    for attribute_name, original_value in original_values.items():
        if attribute_name != target_attribute:
            assert getattr(
                destination_node, attribute_name
            ).get() == pytest.approx(original_value)

    aimed_rotation = _world_rotation(maya_cmds, maya_om, destination)
    nodes.modifier_manager.undo_it()
    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        original_rotation,
    )
    nodes.modifier_manager.redo_it()
    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        aimed_rotation,
    )


def test_child_aim_parent_up_vector_uses_effective_parent_orientation(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    child = maya_cmds.createNode(
        "transform",
        name="child",
        parent=destination,
    )
    maya_cmds.setAttr(f"{parent}.rotate", 19.0, -37.0, 28.0)
    maya_cmds.setAttr(f"{destination}.translate", 2.0, -1.0, 3.0)
    maya_cmds.setAttr(f"{destination}.rotate", -17.0, 11.0, 23.0)
    maya_cmds.setAttr(f"{child}.translate", 4.0, 2.0, -1.0)
    original_child_matrix = _matrix(maya_cmds, f"{child}.worldMatrix[0]")
    origin = maya_om.MPoint(*_world_rotate_pivot(maya_cmds, destination))
    aim_point = _world_rotate_pivot(maya_cmds, child)
    parent_matrix = maya_om.MMatrix(
        _matrix(maya_cmds, f"{destination}.parentMatrix[0]")
    )
    parent_rotation = maya_om.MTransformationMatrix(parent_matrix).rotation(
        asQuaternion=True
    )
    parent_up_vector = (0.0, 0.0, 2.0)
    world_up_vector = maya_om.MVector(*parent_up_vector).rotateBy(
        parent_rotation
    )
    up_point = origin + world_up_vector

    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    destination_node.aim_child_to_rotate(
        aim_axis=(1.0, 0.0, 0.0),
        up_axis=(0.0, 0.0, 1.0),
        parent_up_vector=parent_up_vector,
    )
    nodes.modifier_manager.do_it_dg()

    _assert_aim_axes(
        maya_cmds,
        maya_om,
        destination,
        aim_point=aim_point,
        aim_axis=(1.0, 0.0, 0.0),
        up_point=(up_point.x, up_point.y, up_point.z),
        up_axis=(0.0, 0.0, 1.0),
        origin=(origin.x, origin.y, origin.z),
    )
    _assert_matrix_close(
        _matrix(maya_cmds, f"{child}.worldMatrix[0]"),
        original_child_matrix,
    )


@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute"),
    _CHILD_AIM_METHOD_CASES,
)
def test_child_aim_end_defaults_to_effective_parent_orientation(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    target_attribute,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    destination = maya_cmds.createNode(
        node_type,
        name="destination",
        parent=parent,
    )
    maya_cmds.createNode("mesh", name="destinationShape", parent=destination)
    maya_cmds.setAttr(f"{parent}.rotate", 21.0, -32.0, 14.0)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 7.0, 13.0, -19.0)
    maya_cmds.setAttr(f"{destination}.rotate", -23.0, 17.0, 29.0)
    if node_type == "joint":
        maya_cmds.setAttr(f"{destination}.jointOrient", 11.0, -5.0, 31.0)

    nodes = bdu.Nodes()
    destination_node = getattr(nodes.existing, node_type)(destination)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }
    expected_parent_rotation = maya_om.MTransformationMatrix(
        maya_om.MMatrix(_matrix(maya_cmds, f"{destination}.parentMatrix[0]"))
    ).rotation(asQuaternion=True)

    assert getattr(destination_node, method_name)() is destination_node
    nodes.modifier_manager.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        expected_parent_rotation,
    )
    for attribute_name, original_value in original_values.items():
        if attribute_name != target_attribute:
            assert getattr(
                destination_node, attribute_name
            ).get() == pytest.approx(original_value)


def test_child_aim_end_can_raise_without_queueing_changes(
    new_scene, maya_cmds
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{destination}.rotate", 10.0, 20.0, 30.0)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    original_rotate = destination_node.rotate.get()

    with pytest.raises(ValueError, match="direct Transform child"):
        destination_node.aim_child_to_rotate(end_behavior="error")

    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get() == original_rotate


@pytest.mark.parametrize(
    ("arguments", "keyword_arguments", "error_type", "message"),
    (
        ((True,), {}, TypeError, "child_index"),
        ((-1,), {}, ValueError, "child_index"),
        ((1,), {}, IndexError, "out of range"),
        ((), {"end_behavior": object()}, TypeError, "end_behavior"),
        ((), {"end_behavior": "zero"}, ValueError, "end behavior"),
        (
            (),
            {
                "up_target": (0.0, 1.0, 0.0),
                "parent_up_vector": (0.0, 0.0, 1.0),
            },
            ValueError,
            "cannot be specified together",
        ),
        (
            (),
            {"parent_up_vector": (0.0, 0.0, 0.0)},
            ValueError,
            "parent_up_vector",
        ),
        (
            (),
            {"parent_up_vector": (1.0, 0.0, 0.0)},
            ValueError,
            "parallel",
        ),
        (
            (),
            {"joint_child_compensation_attr": "rotateAxis"},
            ValueError,
            "joint_child_compensation_attr",
        ),
    ),
)
def test_child_aim_rejects_invalid_values_without_queueing_changes(
    new_scene,
    maya_cmds,
    arguments,
    keyword_arguments,
    error_type,
    message,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    child = maya_cmds.createNode(
        "transform",
        name="child",
        parent=destination,
    )
    maya_cmds.setAttr(f"{child}.translateX", 5.0)
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    original_rotate = destination_node.rotate.get()

    with pytest.raises(error_type, match=message):
        destination_node.aim_child_to_rotate(
            *arguments,
            **keyword_arguments,
        )

    nodes.modifier_manager.do_it_dg()
    assert destination_node.rotate.get() == original_rotate


def test_child_aim_defaults_joint_child_compensation_to_joint_orient(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("joint", name="destination")
    child = maya_cmds.createNode("joint", name="child", parent=destination)
    maya_cmds.setAttr(f"{child}.translate", 4.0, 2.0, 1.0)
    maya_cmds.setAttr(f"{child}.rotate", 11.0, -17.0, 23.0)
    maya_cmds.setAttr(f"{child}.jointOrient", -7.0, 13.0, 19.0)
    original_child_matrix = _matrix(maya_cmds, f"{child}.worldMatrix[0]")
    original_child_rotate = tuple(maya_cmds.getAttr(f"{child}.rotate")[0])
    original_child_joint_orient = tuple(
        maya_cmds.getAttr(f"{child}.jointOrient")[0]
    )

    nodes = bdu.Nodes()
    destination_node = nodes.existing.joint(destination)
    destination_node.aim_child_to_joint_orient(
        aim_axis=(1.0, 0.0, 0.0),
        up_axis=(0.0, 0.0, 1.0),
        parent_up_vector=(0.0, 0.0, 1.0),
    )
    nodes.modifier_manager.do_it_dg()

    _assert_matrix_close(
        _matrix(maya_cmds, f"{child}.worldMatrix[0]"),
        original_child_matrix,
    )
    assert tuple(maya_cmds.getAttr(f"{child}.rotate")[0]) == pytest.approx(
        original_child_rotate
    )
    assert tuple(
        maya_cmds.getAttr(f"{child}.jointOrient")[0]
    ) != pytest.approx(original_child_joint_orient)
