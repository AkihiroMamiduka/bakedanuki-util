# coding: utf-8
from __future__ import annotations

import builtins

import pytest

pytestmark = pytest.mark.maya


_ROUND_CASES = (
    ("transform", "round_translate", "translate"),
    ("joint", "round_translate", "translate"),
    ("transform", "round_rotate", "rotate"),
    ("joint", "round_rotate", "rotate"),
    ("joint", "round_joint_orient", "jointOrient"),
)


def _matrix(maya_cmds, node_name):
    return maya_cmds.getAttr(f"{node_name}.worldMatrix[0]")


def _world_position(matrix):
    return matrix[12], matrix[13], matrix[14]


def _world_rotation(maya_om, matrix):
    return maya_om.MTransformationMatrix(maya_om.MMatrix(matrix)).rotation(
        asQuaternion=True
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


def _create_round_hierarchy(maya_cmds, maya_om, parent_type):
    parent = maya_cmds.createNode(parent_type, name="round_parent")
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

    maya_cmds.setAttr(f"{parent}.translate", 1.23456, -2.34567, 3.45678)
    maya_cmds.setAttr(f"{parent}.rotate", 17.23456, -23.34567, 31.45678)
    maya_cmds.setAttr(f"{parent}.rotateOrder", 3)
    maya_cmds.setAttr(f"{parent}.rotateAxis", 4.0, -5.0, 6.0)
    maya_cmds.setAttr(f"{parent}.scale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{parent}.shear", 0.2, -0.1, 0.15)
    maya_cmds.setAttr(f"{parent}.rotatePivot", 0.7, -0.8, 0.9)
    if parent_type == "joint":
        maya_cmds.setAttr(
            f"{parent}.jointOrient",
            11.23456,
            -13.34567,
            15.45678,
        )

    maya_cmds.setAttr(
        f"{transform_child}.translate",
        4.321,
        -5.432,
        6.543,
    )
    maya_cmds.setAttr(f"{transform_child}.rotate", 21.0, -32.0, 43.0)
    maya_cmds.setAttr(f"{transform_child}.rotateOrder", 4)
    maya_cmds.setAttr(f"{transform_child}.rotateAxis", 7.0, -8.0, 9.0)
    maya_cmds.setAttr(f"{transform_child}.scale", 1.2, 0.8, 1.4)
    maya_cmds.setAttr(f"{transform_child}.shear", 0.1, -0.05, 0.08)
    maya_cmds.setAttr(
        f"{transform_child}.rotatePivot",
        1.1,
        -1.2,
        1.3,
    )
    _set_offset_parent_rotation(
        maya_cmds,
        maya_om,
        transform_child,
        19.0,
    )

    maya_cmds.setAttr(f"{joint_child}.translate", -3.21, 4.32, -5.43)
    maya_cmds.setAttr(f"{joint_child}.rotate", -24.0, 35.0, -46.0)
    maya_cmds.setAttr(f"{joint_child}.rotateOrder", 5)
    maya_cmds.setAttr(f"{joint_child}.rotateAxis", -6.0, 7.0, -8.0)
    maya_cmds.setAttr(f"{joint_child}.jointOrient", 12.0, -14.0, 16.0)

    return parent, transform_child, joint_child


@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name"),
    _ROUND_CASES,
)
def test_node_round_compensates_direct_child_world_pose_and_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_round_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_parent_value = maya_cmds.getAttr(f"{parent}.{attribute_name}")[0]
    original_world_matrices = {
        child: _matrix(maya_cmds, child)
        for child in (transform_child, joint_child)
    }
    original_transform_scale = maya_cmds.getAttr(f"{transform_child}.scale")[0]
    original_transform_shear = maya_cmds.getAttr(f"{transform_child}.shear")[0]
    original_joint_orient = maya_cmds.getAttr(f"{joint_child}.jointOrient")[0]

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent_node = getattr(nodes.existing, parent_type)(parent)

    round_kwargs = {"compensate_children": True}
    if method_name != "round_translate":
        round_kwargs["compensate_child_translate"] = True
    assert getattr(parent_node, method_name)(3, **round_kwargs) is parent_node
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        original_parent_value
    )

    mod.do_it_dg()

    expected_parent_value = tuple(
        builtins.round(value, 3) for value in original_parent_value
    )
    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        expected_parent_value
    )
    for child, world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, world_matrix)
    assert maya_cmds.getAttr(f"{transform_child}.scale")[0] == pytest.approx(
        original_transform_scale
    )
    assert maya_cmds.getAttr(f"{transform_child}.shear")[0] == pytest.approx(
        original_transform_shear
    )
    assert maya_cmds.getAttr(f"{joint_child}.jointOrient")[0] == pytest.approx(
        original_joint_orient
    )
    compensated_values = {
        child: {
            "translate": maya_cmds.getAttr(f"{child}.translate")[0],
            "rotation": maya_cmds.getAttr(f"{child}.rotate")[0],
        }
        for child in (transform_child, joint_child)
    }

    mod.undo_it()

    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        original_parent_value
    )

    mod.redo_it()

    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        expected_parent_value
    )
    for child, world_matrix in original_world_matrices.items():
        _assert_world_pose(maya_cmds, maya_om, child, world_matrix)
        assert maya_cmds.getAttr(f"{child}.translate")[0] == pytest.approx(
            compensated_values[child]["translate"]
        )
        assert maya_cmds.getAttr(f"{child}.rotate")[0] == pytest.approx(
            compensated_values[child]["rotation"]
        )


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    "joint_child_compensation_attr",
    ("rotate", "jointOrient"),
)
@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name"),
    (
        ("transform", "round_rotate", "rotate"),
        ("joint", "round_rotate", "rotate"),
        ("joint", "round_joint_orient", "jointOrient"),
    ),
)
def test_rotation_round_compensation_supports_all_rotate_orders(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
    rotate_order,
    joint_child_compensation_attr,
):
    import bd_util as bdu

    parent = maya_cmds.createNode(parent_type, name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotateOrder", rotate_order)
    maya_cmds.setAttr(f"{parent}.rotate", 63.23456, -47.34567, 28.45678)
    maya_cmds.setAttr(f"{parent}.rotateAxis", 7.0, -11.0, 13.0)
    maya_cmds.setAttr(f"{child}.translate", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{child}.rotateOrder", rotate_order)
    maya_cmds.setAttr(f"{child}.rotate", -31.0, 42.0, -53.0)
    maya_cmds.setAttr(f"{child}.rotateAxis", -5.0, 8.0, -12.0)
    maya_cmds.setAttr(f"{child}.jointOrient", 17.0, -19.0, 23.0)
    if parent_type == "joint":
        maya_cmds.setAttr(
            f"{parent}.jointOrient",
            34.23456,
            -26.34567,
            18.45678,
        )

    original_child_world = _matrix(maya_cmds, child)
    original_child_rotate = maya_cmds.getAttr(f"{child}.rotate")[0]
    original_child_joint_orient = maya_cmds.getAttr(f"{child}.jointOrient")[0]
    original_parent_value = maya_cmds.getAttr(f"{parent}.{attribute_name}")[0]
    nodes = bdu.Nodes()
    parent_node = getattr(nodes.existing, parent_type)(parent)

    getattr(parent_node, method_name)(
        3,
        compensate_children=True,
        compensate_child_translate=True,
        joint_child_compensation_attr=joint_child_compensation_attr,
    )
    nodes.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr(f"{parent}.{attribute_name}")[0] == pytest.approx(
        tuple(builtins.round(value, 3) for value in original_parent_value)
    )
    if joint_child_compensation_attr == "rotate":
        assert maya_cmds.getAttr(f"{child}.jointOrient")[0] == pytest.approx(
            original_child_joint_orient
        )
    else:
        assert maya_cmds.getAttr(f"{child}.rotate")[0] == pytest.approx(
            original_child_rotate
        )
    _assert_world_pose(maya_cmds, maya_om, child, original_child_world)


@pytest.mark.parametrize(
    ("parent_type", "method_name", "attribute_name"),
    _ROUND_CASES,
)
def test_node_round_defaults_to_no_child_compensation(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
    attribute_name,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_round_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    original_child_world = _matrix(maya_cmds, transform_child)
    original_child_values = {
        child: {
            "translate": maya_cmds.getAttr(f"{child}.translate")[0],
            "rotate": maya_cmds.getAttr(f"{child}.rotate")[0],
        }
        for child in (transform_child, joint_child)
    }
    original_joint_orient = maya_cmds.getAttr(f"{joint_child}.jointOrient")[0]
    nodes = bdu.Nodes()
    parent_node = getattr(nodes.existing, parent_type)(parent)

    getattr(parent_node, method_name)(3)
    nodes.modifier_manager.do_it_dg()

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


@pytest.mark.parametrize(
    ("parent_type", "method_name"),
    (
        ("transform", "round_rotate"),
        ("joint", "round_rotate"),
        ("joint", "round_joint_orient"),
    ),
)
def test_rotation_round_defaults_to_orientation_only_child_compensation(
    new_scene,
    maya_cmds,
    maya_om,
    parent_type,
    method_name,
):
    import bd_util as bdu

    parent, transform_child, joint_child = _create_round_hierarchy(
        maya_cmds,
        maya_om,
        parent_type,
    )
    children = transform_child, joint_child
    original_world_matrices = {
        child: _matrix(maya_cmds, child) for child in children
    }
    original_translates = {
        child: maya_cmds.getAttr(f"{child}.translate")[0] for child in children
    }
    original_joint_orient = maya_cmds.getAttr(f"{joint_child}.jointOrient")[0]
    for child in children:
        maya_cmds.setAttr(f"{child}.translateX", lock=True)

    nodes = bdu.Nodes()
    parent_node = getattr(nodes.existing, parent_type)(parent)
    getattr(parent_node, method_name)(3, compensate_children=True)
    nodes.modifier_manager.do_it_dg()

    for child, original_world_matrix in original_world_matrices.items():
        _assert_rotation_close(
            _world_rotation(maya_om, _matrix(maya_cmds, child)),
            _world_rotation(maya_om, original_world_matrix),
        )
        assert maya_cmds.getAttr(f"{child}.translate")[0] == pytest.approx(
            original_translates[child]
        )
    assert maya_cmds.getAttr(f"{joint_child}.jointOrient")[0] == pytest.approx(
        original_joint_orient
    )
    assert _world_position(
        _matrix(maya_cmds, transform_child)
    ) != pytest.approx(
        _world_position(original_world_matrices[transform_child]),
        abs=1.0e-10,
    )


def test_node_round_rejects_non_bool_compensate_children(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("joint", name="test_joint")
    node = bdu.Nodes().existing.joint(node_name)

    for method_name in (
        "round_translate",
        "round_rotate",
        "round_joint_orient",
    ):
        with pytest.raises(
            TypeError, match="compensate_children must be bool"
        ):
            getattr(node, method_name)(3, compensate_children=1)


@pytest.mark.parametrize(
    "method_name",
    ("round_rotate", "round_joint_orient"),
)
def test_rotation_round_rejects_invalid_child_compensation_options(
    new_scene,
    maya_cmds,
    method_name,
):
    import bd_util as bdu

    node_name = maya_cmds.createNode("joint", name="test_joint")
    node = bdu.Nodes().existing.joint(node_name)

    with pytest.raises(
        TypeError, match="compensate_child_translate must be bool"
    ):
        getattr(node, method_name)(3, compensate_child_translate=1)
    with pytest.raises(
        ValueError,
        match="compensate_child_translate=True requires",
    ):
        getattr(node, method_name)(3, compensate_child_translate=True)
    with pytest.raises(
        TypeError, match="joint_child_compensation_attr must be str"
    ):
        getattr(node, method_name)(3, joint_child_compensation_attr=1)
    with pytest.raises(
        ValueError, match="joint_child_compensation_attr must be"
    ):
        getattr(node, method_name)(
            3,
            joint_child_compensation_attr="rotation",
        )


@pytest.mark.parametrize(
    ("joint_child_compensation_attr", "blocked_attribute"),
    (("rotate", "rotateX"), ("jointOrient", "jointOrientX")),
)
def test_node_round_validates_selected_rotation_before_queueing(
    new_scene,
    maya_cmds,
    joint_child_compensation_attr,
    blocked_attribute,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 17.23456, -23.34567, 31.45678)
    maya_cmds.setAttr(f"{child}.translate", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{child}.{blocked_attribute}", lock=True)
    original_parent_rotate = maya_cmds.getAttr(f"{parent}.rotate")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(parent)

    with pytest.raises(RuntimeError, match=rf"child\.{blocked_attribute}"):
        node.round_rotate(
            3,
            compensate_children=True,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        original_parent_rotate
    )

    node.round_rotate(3)
    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        tuple(builtins.round(value, 3) for value in original_parent_rotate)
    )


def test_node_round_rejects_connected_child_compensation_plug_atomically(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    driver = maya_cmds.createNode("transform", name="driver")
    maya_cmds.setAttr(f"{parent}.rotate", 17.23456, -23.34567, 31.45678)
    maya_cmds.setAttr(f"{child}.translate", 2.0, 3.0, 4.0)
    maya_cmds.connectAttr(
        f"{driver}.rotateX",
        f"{child}.jointOrientX",
    )
    original_parent_rotate = maya_cmds.getAttr(f"{parent}.rotate")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(parent)

    with pytest.raises(RuntimeError, match=r"child\.jointOrientX"):
        node.round_rotate(
            3,
            compensate_children=True,
            joint_child_compensation_attr="jointOrient",
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        original_parent_rotate
    )


def test_rotation_round_only_validates_translate_when_requested(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("joint", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 17.23456, -23.34567, 31.45678)
    maya_cmds.setAttr(f"{child}.translate", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{child}.translateX", lock=True)
    original_parent_rotate = maya_cmds.getAttr(f"{parent}.rotate")[0]
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing.transform(parent)

    with pytest.raises(RuntimeError, match=r"child\.translateX"):
        node.round_rotate(
            3,
            compensate_children=True,
            compensate_child_translate=True,
        )

    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        original_parent_rotate
    )

    node.round_rotate(3, compensate_children=True)
    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{parent}.rotate")[0] == pytest.approx(
        tuple(builtins.round(value, 3) for value in original_parent_rotate)
    )


def test_node_round_ignores_non_inheriting_child_and_noop_child_blockers(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("transform", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.rotate", 17.23456, -23.34567, 31.45678)
    maya_cmds.setAttr(f"{child}.inheritsTransform", False)
    maya_cmds.setAttr(f"{child}.translateX", lock=True)
    maya_cmds.setAttr(f"{child}.rotateX", lock=True)
    original_child_world = _matrix(maya_cmds, child)
    nodes = bdu.Nodes()
    node = nodes.existing.transform(parent)

    node.round_rotate(3, compensate_children=True)
    nodes.modifier_manager.do_it_dg()

    assert _matrix(maya_cmds, child) == pytest.approx(original_child_world)

    maya_cmds.setAttr(f"{parent}.rotate", 1.0, 2.0, 3.0)
    assert node.round_rotate(3, compensate_children=True) is node


@pytest.mark.parametrize("instanced_node", ("parent", "child"))
def test_node_round_compensation_rejects_instanced_dag(
    new_scene,
    maya_cmds,
    instanced_node,
):
    import bd_util as bdu

    parent = maya_cmds.createNode("transform", name="parent")
    child = maya_cmds.createNode("transform", name="child", parent=parent)
    maya_cmds.setAttr(f"{parent}.translate", 1.23456, 2.34567, 3.45678)
    maya_cmds.instance(parent if instanced_node == "parent" else child)
    node = bdu.Nodes().existing.transform(parent)

    with pytest.raises(RuntimeError, match="instanced"):
        node.round_translate(3, compensate_children=True)
