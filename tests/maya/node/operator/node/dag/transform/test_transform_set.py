# coding: utf-8
from __future__ import annotations

import pytest

pytestmark = pytest.mark.maya


_SET_CASES = (
    ("transform", "set_translate", "translate", (4.125, -6.25, 8.5)),
    ("joint", "set_translate", "translate", (4.125, -6.25, 8.5)),
    (
        "transform",
        "set_rotate_axis",
        "rotateAxis",
        (19.125, -28.25, 37.5),
    ),
    (
        "joint",
        "set_rotate_axis",
        "rotateAxis",
        (19.125, -28.25, 37.5),
    ),
    ("transform", "set_rotate", "rotate", (41.25, -52.5, 63.75)),
    ("joint", "set_rotate", "rotate", (41.25, -52.5, 63.75)),
    (
        "joint",
        "set_joint_orient",
        "jointOrient",
        (-27.5, 38.75, -49.125),
    ),
)

_ROTATION_SET_CASES = (
    (
        "transform",
        "set_rotate_axis",
        "rotateAxis",
        (19.125, -28.25, 37.5),
    ),
    (
        "joint",
        "set_rotate_axis",
        "rotateAxis",
        (19.125, -28.25, 37.5),
    ),
    ("transform", "set_rotate", "rotate", (41.25, -52.5, 63.75)),
    ("joint", "set_rotate", "rotate", (41.25, -52.5, 63.75)),
    (
        "joint",
        "set_joint_orient",
        "jointOrient",
        (-27.5, 38.75, -49.125),
    ),
)


def _matrix(maya_cmds, node_name):
    return maya_cmds.getAttr(f"{node_name}.worldMatrix[0]")


def _world_position(matrix):
    return matrix[12], matrix[13], matrix[14]


def _world_rotation(maya_om, matrix):
    return maya_om.MTransformationMatrix(maya_om.MMatrix(matrix)).rotation(
        asQuaternion=True
    )


def _rotation_quaternion(maya_om, value, order):
    radians = tuple(
        maya_om.MAngle(component, maya_om.MAngle.kDegrees).asRadians()
        for component in value
    )
    return maya_om.MEulerRotation(*radians, order).asQuaternion()


def _quaternion_rotation_values(maya_om, quaternion, order):
    euler = quaternion.asEulerRotation()
    euler.reorderIt(order)
    return tuple(
        maya_om.MAngle(component, maya_om.MAngle.kRadians).asDegrees()
        for component in (euler.x, euler.y, euler.z)
    )


def _assert_rotation_close(actual, expected, *, abs_tolerance=1.0e-9):
    dot = (
        actual.x * expected.x
        + actual.y * expected.y
        + actual.z * expected.z
        + actual.w * expected.w
    )
    assert abs(dot) == pytest.approx(1.0, abs=abs_tolerance)


def _assert_world_pose(maya_cmds, maya_om, node_name, expected_matrix):
    actual_matrix = _matrix(maya_cmds, node_name)
    assert _world_position(actual_matrix) == pytest.approx(
        _world_position(expected_matrix),
        abs=1.0e-9,
    )
    _assert_rotation_close(
        _world_rotation(maya_om, actual_matrix),
        _world_rotation(maya_om, expected_matrix),
    )


def _rotation_attributes(node_type):
    if node_type == "joint":
        return "rotateAxis", "rotate", "jointOrient"
    return "rotateAxis", "rotate"


def _set_offset_parent_rotation(maya_cmds, maya_om, node_name, degrees):
    transformation = maya_om.MTransformationMatrix()
    transformation.setRotation(
        maya_om.MEulerRotation(
            0.0,
            0.0,
            maya_om.MAngle(
                degrees,
                maya_om.MAngle.kDegrees,
            ).asRadians(),
        )
    )
    maya_cmds.setAttr(
        f"{node_name}.offsetParentMatrix",
        *list(transformation.asMatrix()),
        type="matrix",
    )


def _create_set_hierarchy(maya_cmds, maya_om, parent_type):
    parent = maya_cmds.createNode(parent_type, name="set_parent")
    transform_child = maya_cmds.createNode(
        "transform",
        name="transform_child",
        parent=parent,
    )
    joint_child = maya_cmds.createNode(
        "joint",
        name="joint_child",
        parent=parent,
    )

    maya_cmds.setAttr(f"{parent}.translate", 1.25, -2.5, 3.75)
    maya_cmds.setAttr(f"{parent}.rotate", 17.0, -23.0, 31.0)
    maya_cmds.setAttr(f"{parent}.rotateOrder", 3)
    maya_cmds.setAttr(f"{parent}.rotateAxis", 4.0, -5.0, 6.0)
    maya_cmds.setAttr(f"{parent}.scale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{parent}.shear", 0.2, -0.1, 0.15)
    maya_cmds.setAttr(f"{parent}.rotatePivot", 0.7, -0.8, 0.9)
    if parent_type == "joint":
        maya_cmds.setAttr(f"{parent}.jointOrient", 11.0, -13.0, 15.0)

    maya_cmds.setAttr(f"{transform_child}.translate", 4.0, -5.0, 6.0)
    maya_cmds.setAttr(f"{transform_child}.rotate", 21.0, -32.0, 43.0)
    maya_cmds.setAttr(f"{transform_child}.rotateOrder", 4)
    maya_cmds.setAttr(f"{transform_child}.rotateAxis", 7.0, -8.0, 9.0)
    maya_cmds.setAttr(f"{transform_child}.rotatePivot", 1.1, -1.2, 1.3)
    _set_offset_parent_rotation(
        maya_cmds,
        maya_om,
        transform_child,
        19.0,
    )

    maya_cmds.setAttr(f"{joint_child}.translate", -3.0, 4.0, -5.0)
    maya_cmds.setAttr(f"{joint_child}.rotate", -24.0, 35.0, -46.0)
    maya_cmds.setAttr(f"{joint_child}.rotateOrder", 5)
    maya_cmds.setAttr(f"{joint_child}.rotateAxis", -6.0, 7.0, -8.0)
    maya_cmds.setAttr(f"{joint_child}.jointOrient", 12.0, -14.0, 16.0)
    return parent, transform_child, joint_child


def _create_world_set_hierarchy(maya_cmds, maya_om, node_type):
    grandparent = maya_cmds.createNode("transform", name="set_grandparent")
    node, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        node_type,
    )
    maya_cmds.parent(node, grandparent, relative=True)
    maya_cmds.setAttr(f"{grandparent}.translate", -3.0, 5.0, 7.0)
    maya_cmds.setAttr(f"{grandparent}.rotate", -19.0, 29.0, -41.0)
    maya_cmds.setAttr(f"{grandparent}.scale", -1.7, 0.6, 2.3)
    maya_cmds.setAttr(f"{grandparent}.shear", -0.15, 0.08, 0.12)
    _set_offset_parent_rotation(maya_cmds, maya_om, node, 27.0)
    return node, transform_child, joint_child


@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name", "target_value"),
    _SET_CASES,
)
def test_node_set_defaults_to_target_attribute_only_and_supports_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
    target_value,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_parent_value = maya_cmds.getAttr(f"{parent}.{attribute_name}")[0]
    original_child_world = _matrix(maya_cmds, transform_child)
    original_child_values = {
        child: {
            "translate": maya_cmds.getAttr(f"{child}.translate")[0],
            "rotate": maya_cmds.getAttr(f"{child}.rotate")[0],
        }
        for child in (transform_child, joint_child)
    }
    original_joint_orient = maya_cmds.getAttr(f"{joint_child}.jointOrient")[0]
    mod = bdu.ModifierManager()
    node = getattr(
        bdu.Nodes(modifier_manager=mod).existing,
        parent_type,
    )(parent)

    assert getattr(node, method_name)(target_value) is node
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        original_parent_value
    )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        target_value
    )
    assert _matrix(maya_cmds, transform_child) != pytest.approx(
        original_child_world
    )
    for child, values in original_child_values.items():
        assert maya_cmds.getAttr(f"{child}.translate")[0] == pytest.approx(
            values["translate"]
        )
        assert maya_cmds.getAttr(f"{child}.rotate")[0] == pytest.approx(
            values["rotate"]
        )
    assert maya_cmds.getAttr(f"{joint_child}.jointOrient")[0] == pytest.approx(
        original_joint_orient
    )

    mod.undo_it()
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        original_parent_value
    )
    mod.redo_it()
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        target_value
    )


@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name", "target_value"),
    _SET_CASES,
)
def test_node_set_accepts_three_scalar_arguments(
    new_scene,
    maya_cmds,
    parent_type,
    method_name,
    attribute_name,
    target_value,
):
    import bd_util as bdu

    parent = maya_cmds.createNode(parent_type, name="parent")
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, parent_type)(parent)

    assert getattr(node, method_name)(*target_value) is node
    nodes.modifier_manager.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        target_value
    )


@pytest.mark.parametrize(
    ("node_type", "method_name", "attribute_name", "target_value"),
    _SET_CASES,
)
def test_node_set_accepts_explicit_local_space(
    new_scene,
    maya_cmds,
    node_type,
    method_name,
    attribute_name,
    target_value,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode(node_type, name="node")
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, node_type)(node_name)

    getattr(node, method_name)(target_value, space="local")
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{node_name}.{attribute_name}")[
        0
    ] == pytest.approx(target_value)


@pytest.mark.parametrize("node_type", ("transform", "joint"))
def test_set_translate_world_space_sets_dag_origin_and_supports_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
):
    import bd_util as bdu

    node_name, _, _ = _create_world_set_hierarchy(
        maya_cmds,
        maya_om,
        node_type,
    )
    target_position = (13.25, -17.5, 23.75)
    original_matrix = _matrix(maya_cmds, node_name)
    original_translate = maya_cmds.getAttr(f"{node_name}.translate")[0]
    original_rotation_values = {
        attribute_name: maya_cmds.getAttr(f"{node_name}.{attribute_name}")[0]
        for attribute_name in _rotation_attributes(node_type)
    }
    mod = bdu.ModifierManager()
    node = getattr(
        bdu.Nodes(modifier_manager=mod).existing,
        node_type,
    )(node_name)

    assert node.set_translate(target_position, space="world") is node
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        original_translate
    )

    mod.do_it_dg()

    assert _world_position(_matrix(maya_cmds, node_name)) == pytest.approx(
        target_position,
        abs=1.0e-9,
    )
    for attribute_name, original_value in original_rotation_values.items():
        assert maya_cmds.getAttr(f"{node_name}.{attribute_name}")[
            0
        ] == pytest.approx(original_value)
    matched_matrix = _matrix(maya_cmds, node_name)

    mod.undo_it()
    assert _matrix(maya_cmds, node_name) == pytest.approx(original_matrix)

    mod.redo_it()
    assert _matrix(maya_cmds, node_name) == pytest.approx(matched_matrix)


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    ("node_type", "method_name", "attribute_name", "target_value"),
    _ROTATION_SET_CASES,
)
def test_rotation_set_world_space_sets_final_world_orientation(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    attribute_name,
    target_value,
    rotate_order,
):
    import bd_util as bdu

    node_name, _, _ = _create_world_set_hierarchy(
        maya_cmds,
        maya_om,
        node_type,
    )
    maya_cmds.setAttr(f"{node_name}.rotateOrder", rotate_order)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: maya_cmds.getAttr(f"{node_name}.{name}")[0]
        for name in attribute_names
    }
    original_translate = maya_cmds.getAttr(f"{node_name}.translate")[0]
    original_rotation = _world_rotation(
        maya_om,
        _matrix(maya_cmds, node_name),
    )
    target_order = (
        rotate_order
        if attribute_name == "rotate"
        else maya_om.MEulerRotation.kXYZ
    )
    target_rotation = _rotation_quaternion(
        maya_om,
        target_value,
        target_order,
    )
    mod = bdu.ModifierManager()
    node = getattr(
        bdu.Nodes(modifier_manager=mod).existing,
        node_type,
    )(node_name)

    assert (
        getattr(node, method_name)(
            target_value,
            space="world",
        )
        is node
    )
    assert {
        name: maya_cmds.getAttr(f"{node_name}.{name}")[0]
        for name in attribute_names
    } == original_values

    mod.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_om, _matrix(maya_cmds, node_name)),
        target_rotation,
    )
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        original_translate
    )
    for name, original_value in original_values.items():
        if name != attribute_name:
            assert maya_cmds.getAttr(f"{node_name}.{name}")[
                0
            ] == pytest.approx(original_value)

    mod.undo_it()
    _assert_rotation_close(
        _world_rotation(maya_om, _matrix(maya_cmds, node_name)),
        original_rotation,
    )

    mod.redo_it()
    _assert_rotation_close(
        _world_rotation(maya_om, _matrix(maya_cmds, node_name)),
        target_rotation,
    )


@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name", "target_value"),
    _SET_CASES,
)
def test_node_set_can_compensate_direct_child_world_pose(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
    target_value,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    original_joint_orient = maya_cmds.getAttr(f"{joint_child}.jointOrient")[0]
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, parent_type)(parent)
    options = {"compensate_children": True}
    if method_name != "set_translate":
        options["compensate_child_translate"] = True

    getattr(node, method_name)(target_value, **options)
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        target_value
    )
    for child, original_world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, original_world_matrix)
    assert maya_cmds.getAttr(f"{joint_child}.jointOrient")[0] == pytest.approx(
        original_joint_orient
    )


@pytest.mark.parametrize(
    ("node_type", "method_name", "attribute_name", "target_value"),
    _SET_CASES,
)
def test_node_set_world_space_can_compensate_direct_child_world_pose(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    attribute_name,
    target_value,
):
    import bd_util as bdu

    node_name, transform_child, joint_child = _create_world_set_hierarchy(
        maya_cmds,
        maya_om,
        node_type,
    )
    original_child_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, node_type)(node_name)
    options = {
        "space": "world",
        "compensate_children": True,
    }
    if method_name != "set_translate":
        options["compensate_child_translate"] = True

    getattr(node, method_name)(target_value, **options)
    nodes.modifier_manager.do_it_dg()

    if method_name == "set_translate":
        assert _world_position(_matrix(maya_cmds, node_name)) == pytest.approx(
            target_value,
            abs=1.0e-9,
        )
    else:
        rotate_order = maya_cmds.getAttr(f"{node_name}.rotateOrder")
        target_order = (
            rotate_order
            if attribute_name == "rotate"
            else maya_om.MEulerRotation.kXYZ
        )
        _assert_rotation_close(
            _world_rotation(maya_om, _matrix(maya_cmds, node_name)),
            _rotation_quaternion(
                maya_om,
                target_value,
                target_order,
            ),
        )
    for child, original_world_matrix in original_child_world_matrices.items():
        _assert_world_pose(
            maya_cmds,
            maya_om,
            child,
            original_world_matrix,
        )


@pytest.mark.parametrize(
    "joint_child_compensation_attr",
    ("rotate", "jointOrient"),
)
@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name", "target_value"),
    _ROTATION_SET_CASES,
)
def test_rotation_set_selects_joint_child_attr_without_changing_translate(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
    target_value,
    joint_child_compensation_attr,
):
    import bd_util as bdu

    parent, _, child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_child_world = _matrix(maya_cmds, child)
    original_translate = maya_cmds.getAttr(f"{child}.translate")[0]
    original_rotate = maya_cmds.getAttr(f"{child}.rotate")[0]
    original_joint_orient = maya_cmds.getAttr(f"{child}.jointOrient")[0]
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, parent_type)(parent)

    getattr(node, method_name)(
        target_value,
        compensate_children=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        target_value
    )
    _assert_rotation_close(
        _world_rotation(maya_om, _matrix(maya_cmds, child)),
        _world_rotation(maya_om, original_child_world),
    )
    assert maya_cmds.getAttr(f"{child}.translate")[0] == pytest.approx(
        original_translate
    )
    if joint_child_compensation_attr == "rotate":
        assert maya_cmds.getAttr(f"{child}.jointOrient")[0] == pytest.approx(
            original_joint_orient
        )
    else:
        assert maya_cmds.getAttr(f"{child}.rotate")[0] == pytest.approx(
            original_rotate
        )


@pytest.mark.parametrize("parent_type", ("transform", "joint"))
def test_set_rotate_axis_compensates_with_gimbal_locked_target(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    nodes = bdu.Nodes()
    node = getattr(nodes.existing, parent_type)(parent)

    node.set_rotate_axis(
        45.0,
        90.0,
        135.0,
        compensate_children=True,
        compensate_child_translate=True,
    )
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{parent}.rotateAxis")[0] == pytest.approx(
        (45.0, 90.0, 135.0)
    )
    for child, original_world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, original_world_matrix)


@pytest.mark.parametrize(
    "joint_child_compensation_attr",
    ("rotate", "jointOrient"),
)
def test_joint_set_sequence_compensates_direct_child_world_pose(
    new_scene,
    maya_cmds,
    maya_om,
    joint_child_compensation_attr,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        "joint",
    )
    original_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    nodes = bdu.Nodes()
    node = nodes.existing.joint(parent)

    node.set_translate(1.0, 2.0, 3.0, compensate_children=True)
    nodes.modifier_manager.do_it_dg()
    node.set_rotate(
        45.0,
        90.0,
        135.0,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    nodes.modifier_manager.do_it_dg()
    node.set_joint_orient(
        45.0,
        90.0,
        135.0,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    nodes.modifier_manager.do_it_dg()

    for child, original_world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, original_world_matrix)


@pytest.mark.parametrize(
    "joint_child_compensation_attr",
    ("rotate", "jointOrient"),
)
def test_set_joint_orient_compensates_with_gimbal_locked_rotate(
    new_scene,
    maya_cmds,
    maya_om,
    joint_child_compensation_attr,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_set_hierarchy(
        maya_cmds,
        maya_om,
        "joint",
    )
    maya_cmds.setAttr(f"{parent}.rotate", 45.0, 90.0, 135.0)
    maya_cmds.setAttr(f"{joint_child}.rotate", 45.0, 90.0, 135.0)
    original_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    nodes = bdu.Nodes()
    node = nodes.existing.joint(parent)

    node.set_joint_orient(
        45.0,
        90.0,
        135.0,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{parent}.jointOrient")[0] == pytest.approx(
        (45.0, 90.0, 135.0)
    )
    for child, original_world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, original_world_matrix)


def test_rotate_compensation_keeps_equivalent_euler_near_gimbal_lock(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("transform", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 17.0, -23.0, 31.0)
    maya_cmds.setAttr(f"{child}.translate", 4.0, -5.0, 6.0)
    maya_cmds.setAttr(f"{child}.rotate", 45.0, 90.0, 135.0)
    original_child_world = _matrix(maya_cmds, child)
    nodes = bdu.Nodes()
    node = nodes.existing.transform(parent)

    node.set_rotate(
        41.25,
        -52.5,
        63.75,
        compensate_children=True,
        compensate_child_translate=True,
    )
    nodes.modifier_manager.do_it_dg()

    _assert_world_pose(maya_cmds, maya_om, child, original_child_world)


@pytest.mark.parametrize(
    ("method_name", "attribute_name"),
    (
        ("set_translate", "translate"),
        ("set_rotate_axis", "rotateAxis"),
        ("set_rotate", "rotate"),
        ("set_joint_orient", "jointOrient"),
    ),
)
def test_node_set_world_space_noop_ignores_blocked_target_plug(
    new_scene,
    maya_cmds,
    maya_om,
    method_name,
    attribute_name,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    node_name = maya_cmds.createNode("joint", name="joint", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 17.0, -23.0, 31.0)
    maya_cmds.setAttr(f"{node_name}.rotateOrder", 4)
    maya_cmds.setAttr(f"{node_name}.rotateAxis", 7.0, -8.0, 9.0)
    maya_cmds.setAttr(f"{node_name}.rotate", 21.0, -32.0, 43.0)
    maya_cmds.setAttr(f"{node_name}.jointOrient", 12.0, -14.0, 16.0)
    maya_cmds.setAttr(f"{node_name}.{attribute_name}X", lock=True)
    original_value = maya_cmds.getAttr(f"{node_name}.{attribute_name}")[0]
    world_matrix = _matrix(maya_cmds, node_name)
    if method_name == "set_translate":
        target_value = _world_position(world_matrix)
    else:
        target_order = (
            maya_cmds.getAttr(f"{node_name}.rotateOrder")
            if attribute_name == "rotate"
            else maya_om.MEulerRotation.kXYZ
        )
        target_value = _quaternion_rotation_values(
            maya_om,
            _world_rotation(maya_om, world_matrix),
            target_order,
        )
    nodes = bdu.Nodes()
    node = nodes.existing.joint(node_name)

    assert (
        getattr(node, method_name)(
            target_value,
            space="world",
        )
        is node
    )
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{node_name}.{attribute_name}")[
        0
    ] == pytest.approx(original_value)


@pytest.mark.parametrize(
    ("method_name", "attribute_name"),
    (
        ("set_translate", "translate"),
        ("set_rotate_axis", "rotateAxis"),
        ("set_rotate", "rotate"),
        ("set_joint_orient", "jointOrient"),
    ),
)
def test_node_set_rejects_invalid_transform_space_without_queueing(
    new_scene,
    maya_cmds,
    method_name,
    attribute_name,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("joint", name="joint")
    original_value = maya_cmds.getAttr(f"{node_name}.{attribute_name}")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.joint(node_name)

    with pytest.raises(TypeError, match="space must be str"):
        getattr(node, method_name)((10.0, 20.0, 30.0), space=1)
    with pytest.raises(ValueError, match="Unsupported transform space"):
        getattr(node, method_name)(
            (10.0, 20.0, 30.0),
            space="object",
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{node_name}.{attribute_name}")[
        0
    ] == pytest.approx(original_value)


def test_node_set_world_space_rejects_instanced_dag_but_local_space_remains_valid(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("transform", name="transform")
    maya_cmds.instance(node_name, name="transform_instance")
    nodes = bdu.Nodes()
    node = nodes.existing.transform(node_name)

    with pytest.raises(RuntimeError, match="instanced DAG node"):
        node.set_translate((10.0, 20.0, 30.0), space="world")

    node.set_translate((1.0, 2.0, 3.0), space="local")
    nodes.modifier_manager.do_it_dg()
    assert maya_cmds.getAttr(f"{node_name}.translate")[0] == pytest.approx(
        (1.0, 2.0, 3.0)
    )


@pytest.mark.parametrize(
    ("method_name", "attribute_name"),
    (
        ("set_translate", "translate"),
        ("set_rotate_axis", "rotateAxis"),
        ("set_rotate", "rotate"),
        ("set_joint_orient", "jointOrient"),
    ),
)
def test_node_set_world_space_rejects_effectively_singular_parent_matrix(
    new_scene,
    maya_cmds,
    method_name,
    attribute_name,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    node_name = maya_cmds.createNode("joint", name="joint", parent=parent)
    maya_cmds.setAttr(f"{parent}.scaleX", 0.0)
    original_value = maya_cmds.getAttr(f"{node_name}.{attribute_name}")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.joint(node_name)

    with pytest.raises(
        RuntimeError, match="invertible effective parent matrix"
    ):
        getattr(node, method_name)(
            (10.0, 20.0, 30.0),
            space="world",
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{node_name}.{attribute_name}")[
        0
    ] == pytest.approx(original_value)


@pytest.mark.parametrize(
    "method_name",
    (
        "set_translate",
        "set_rotate_axis",
        "set_rotate",
        "set_joint_orient",
    ),
)
def test_node_set_rejects_invalid_vector_values(
    new_scene,
    maya_cmds,
    method_name,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("joint", name="joint")
    node = bdu.Nodes().existing.joint(node_name)

    with pytest.raises(TypeError, match=method_name):
        getattr(node, method_name)((1.0, 2.0))
    with pytest.raises(TypeError, match=method_name):
        getattr(node, method_name)(1.0, 2.0)


@pytest.mark.parametrize(
    ("joint_child_compensation_attr", "blocked_attribute"),
    (("rotate", "rotateX"), ("jointOrient", "jointOrientX")),
)
def test_node_set_validates_all_compensation_before_queueing(
    new_scene,
    maya_cmds,
    joint_child_compensation_attr,
    blocked_attribute,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{child}.translate", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{child}.{blocked_attribute}", lock=True)
    original_parent_rotate = maya_cmds.getAttr(f"{parent}.rotate")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(parent)

    with pytest.raises(RuntimeError, match=rf"child\.{blocked_attribute}"):
        node.set_rotate(
            41.25,
            -52.5,
            63.75,
            compensate_children=True,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        original_parent_rotate
    )
