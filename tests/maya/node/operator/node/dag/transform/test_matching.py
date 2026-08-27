# coding: utf-8
from __future__ import annotations

import pytest

_ROTATION_MATCH_CASES = (
    ("transform", "match_rotation_to_rotate", "rotate"),
    ("transform", "match_rotation_to_rotate_axis", "rotateAxis"),
    ("joint", "match_rotation_to_rotate", "rotate"),
    ("joint", "match_rotation_to_rotate_axis", "rotateAxis"),
    ("joint", "match_rotation_to_joint_orient", "jointOrient"),
)


def _matrix(maya_cmds, attribute):
    return maya_cmds.getAttr(attribute)


def _world_position(maya_cmds, node_name):
    matrix = _matrix(maya_cmds, f"{node_name}.worldMatrix[0]")
    return matrix[12], matrix[13], matrix[14]


def _world_rotation(maya_cmds, maya_om, node_name):
    matrix = maya_om.MMatrix(_matrix(maya_cmds, f"{node_name}.worldMatrix[0]"))
    return maya_om.MTransformationMatrix(matrix).rotation(asQuaternion=True)


def _assert_vector_close(actual, expected, *, abs=1.0e-9):
    assert tuple(actual) == pytest.approx(tuple(expected), abs=abs)


def _assert_matrix_close(actual, expected, *, abs=1.0e-9):
    assert list(actual) == pytest.approx(list(expected), abs=abs)


def _assert_rotation_close(actual, expected, *, abs_tolerance=1.0e-9):
    dot = (
        actual.x * expected.x
        + actual.y * expected.y
        + actual.z * expected.z
        + actual.w * expected.w
    )
    assert abs(dot) == pytest.approx(1.0, abs=abs_tolerance)


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


def test_match_position_matches_dag_origin_and_supports_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    parent = maya_cmds.createNode("transform", name="destination_parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{source}.translate", 12.0, -7.0, 9.0)
    maya_cmds.setAttr(f"{parent}.translate", 2.0, -3.0, 5.0)
    maya_cmds.setAttr(f"{parent}.rotate", 17.0, 31.0, -23.0)
    maya_cmds.setAttr(f"{parent}.scale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{parent}.shear", 0.2, -0.1, 0.15)
    maya_cmds.setAttr(f"{destination}.translate", 1.0, 2.0, 3.0)
    maya_cmds.setAttr(f"{destination}.rotatePivot", 4.0, -2.0, 1.0)
    maya_cmds.setAttr(f"{destination}.rotate", 27.0, -19.0, 43.0)
    _set_offset_parent_rotation(maya_cmds, maya_om, destination, 35.0)

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)
    original_matrix = destination_node.worldMatrix[0].get().matrix
    original_translate = destination_node.translate.get()

    assert destination_node.match_position(source_node) is destination_node
    assert destination_node.translate.get() == original_translate

    mod.do_it_dg()

    _assert_vector_close(
        _world_position(maya_cmds, destination),
        _world_position(maya_cmds, source),
    )
    matched_matrix = destination_node.worldMatrix[0].get().matrix

    mod.undo_it()

    _assert_matrix_close(
        destination_node.worldMatrix[0].get().matrix,
        original_matrix,
    )
    assert destination_node.translate.get() == original_translate

    mod.redo_it()

    _assert_matrix_close(
        destination_node.worldMatrix[0].get().matrix,
        matched_matrix,
    )


@pytest.mark.parametrize(
    ("space", "axes", "basis_attribute"),
    (
        ("world", "x", None),
        ("local", "x", "parentMatrix[0]"),
        ("object", "yz", "worldMatrix[0]"),
    ),
)
def test_match_position_projects_delta_onto_selected_space_axes(
    new_scene,
    maya_cmds,
    maya_om,
    space,
    axes,
    basis_attribute,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    parent = maya_cmds.createNode("transform", name="destination_parent")
    destination = maya_cmds.createNode(
        "transform",
        name="destination",
        parent=parent,
    )
    maya_cmds.setAttr(f"{source}.translate", 11.0, -3.0, 17.0)
    maya_cmds.setAttr(f"{parent}.rotateZ", 30.0)
    maya_cmds.setAttr(f"{destination}.translate", 2.0, 5.0, -7.0)
    maya_cmds.setAttr(f"{destination}.rotateZ", 40.0)
    _set_offset_parent_rotation(maya_cmds, maya_om, destination, 60.0)

    before = maya_om.MVector(*_world_position(maya_cmds, destination))
    source_position = maya_om.MVector(*_world_position(maya_cmds, source))
    delta = source_position - before
    if basis_attribute is None:
        basis_rotation = maya_om.MQuaternion()
    else:
        basis_matrix = maya_om.MMatrix(
            _matrix(maya_cmds, f"{destination}.{basis_attribute}")
        )
        basis_rotation = maya_om.MTransformationMatrix(basis_matrix).rotation(
            asQuaternion=True
        )
    basis_delta = delta.rotateBy(basis_rotation.inverse())
    masked_basis_delta = maya_om.MVector(
        basis_delta.x if "x" in axes else 0.0,
        basis_delta.y if "y" in axes else 0.0,
        basis_delta.z if "z" in axes else 0.0,
    )
    expected = before + masked_basis_delta.rotateBy(basis_rotation)

    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)
    destination_node.match_position(
        source_node,
        axes=axes,
        space=space,
    )
    nodes.modifier_manager.do_it_dg()

    _assert_vector_close(
        _world_position(maya_cmds, destination),
        expected,
    )


def test_match_position_accepts_shape_source(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    source_transform = maya_cmds.createNode("transform", name="source")
    source_shape = maya_cmds.createNode(
        "mesh",
        name="sourceShape",
        parent=source_transform,
    )
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{source_transform}.translate", 3.0, 5.0, 7.0)

    nodes = bdu.Nodes()
    source_node = nodes.existing.mesh(source_shape)
    destination_node = nodes.existing.transform(destination)
    destination_node.match_position(source_node)
    nodes.modifier_manager.do_it_dg()

    _assert_vector_close(
        _world_position(maya_cmds, destination),
        _world_position(maya_cmds, source_shape),
    )


def test_match_position_ignores_blocked_unchanged_translate_plug(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{source}.translate", 10.0, 20.0, 30.0)
    maya_cmds.setAttr(f"{destination}.translate", 1.0, 2.0, 3.0)
    maya_cmds.setAttr(f"{destination}.translateY", lock=True)

    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)
    destination_node.match_position(source_node, axes="x")
    nodes.modifier_manager.do_it_dg()

    assert destination_node.translate.get() == pytest.approx((10.0, 2.0, 3.0))


def test_match_position_rejects_blocked_required_translate_plug(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{source}.translateX", 10.0)
    maya_cmds.setAttr(f"{destination}.translateX", lock=True)
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match=r"destination\.translateX"):
        destination_node.match_position(source_node, axes="x")


def test_match_position_rejects_connected_required_translate_plug(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    driver = maya_cmds.createNode("transform", name="driver")
    maya_cmds.setAttr(f"{source}.translateX", 10.0)
    maya_cmds.connectAttr(
        f"{driver}.translateX",
        f"{destination}.translateX",
    )
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match=r"destination\.translateX"):
        destination_node.match_position(source_node, axes="x")


@pytest.mark.parametrize(
    ("argument_name", "value", "error_type"),
    (
        ("axes", "", ValueError),
        ("axes", "yx", ValueError),
        ("axes", "xx", ValueError),
        ("axes", 1, TypeError),
        ("space", "parent", ValueError),
        ("space", 1, TypeError),
    ),
)
def test_match_position_rejects_invalid_options(
    new_scene,
    maya_cmds,
    argument_name,
    value,
    error_type,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(error_type, match=argument_name):
        destination_node.match_position(
            source_node,
            **{argument_name: value},
        )


@pytest.mark.parametrize("rotate_order", range(6))
@pytest.mark.parametrize(
    ("node_type", "method_name", "target_attribute"),
    _ROTATION_MATCH_CASES,
)
def test_match_rotation_methods_match_world_rotation_and_support_undo_redo(
    new_scene,
    maya_cmds,
    maya_om,
    node_type,
    method_name,
    target_attribute,
    rotate_order,
):
    import bd_util as bdu

    source_parent = maya_cmds.createNode("transform", name="source_parent")
    source = maya_cmds.createNode(
        "transform",
        name="source",
        parent=source_parent,
    )
    destination_parent = maya_cmds.createNode(
        "transform",
        name="destination_parent",
    )
    destination = maya_cmds.createNode(
        node_type,
        name="destination",
        parent=destination_parent,
    )
    maya_cmds.setAttr(f"{source_parent}.rotate", 17.0, -23.0, 31.0)
    maya_cmds.setAttr(f"{source}.rotate", -42.0, 28.0, 73.0)
    maya_cmds.setAttr(f"{destination_parent}.rotate", 11.0, 37.0, -19.0)
    maya_cmds.setAttr(f"{destination}.rotateOrder", rotate_order)
    maya_cmds.setAttr(f"{destination}.rotateAxis", 9.0, -14.0, 21.0)
    maya_cmds.setAttr(f"{destination}.rotate", 33.0, 16.0, -27.0)
    maya_cmds.setAttr(f"{destination}.rotatePivot", 4.0, -2.0, 1.0)
    if node_type == "joint":
        maya_cmds.setAttr(
            f"{destination}.jointOrient",
            -12.0,
            25.0,
            38.0,
        )
    _set_offset_parent_rotation(maya_cmds, maya_om, destination, 23.0)

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    source_node = nodes.existing.transform(source)
    destination_node = getattr(nodes.existing, node_type)(destination)
    attribute_names = _rotation_attributes(node_type)
    original_values = {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    }
    original_translation = destination_node.translate.get()
    original_rotation = _world_rotation(maya_cmds, maya_om, destination)

    assert (
        getattr(destination_node, method_name)(source_node) is destination_node
    )
    assert {
        name: tuple(getattr(destination_node, name).get())
        for name in attribute_names
    } == original_values

    mod.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        _world_rotation(maya_cmds, maya_om, source),
    )
    assert destination_node.translate.get() == original_translation
    for attribute_name, original_value in original_values.items():
        if attribute_name != target_attribute:
            assert getattr(
                destination_node, attribute_name
            ).get() == pytest.approx(original_value)
    matched_values = {
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
            destination_node, attribute_name
        ).get() == pytest.approx(original_value)

    mod.redo_it()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        _world_rotation(maya_cmds, maya_om, source),
    )
    for attribute_name, matched_value in matched_values.items():
        assert getattr(
            destination_node, attribute_name
        ).get() == pytest.approx(matched_value)


def test_match_rotation_accepts_shape_source(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    source_transform = maya_cmds.createNode("transform", name="source")
    source_shape = maya_cmds.createNode(
        "mesh",
        name="sourceShape",
        parent=source_transform,
    )
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{source_transform}.rotate", 17.0, -23.0, 31.0)
    nodes = bdu.Nodes()
    source_node = nodes.existing.mesh(source_shape)
    destination_node = nodes.existing.transform(destination)

    destination_node.match_rotation_to_rotate(source_node)
    nodes.modifier_manager.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        _world_rotation(maya_cmds, maya_om, source_shape),
    )


def test_match_rotation_does_not_compensate_dag_origin_for_rotate_pivot(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.setAttr(f"{source}.rotateZ", 90.0)
    maya_cmds.setAttr(f"{destination}.rotatePivotX", 5.0)
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)
    original_position = _world_position(maya_cmds, destination)
    original_translate = destination_node.translate.get()

    destination_node.match_rotation_to_rotate(source_node)
    nodes.modifier_manager.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        _world_rotation(maya_cmds, maya_om, source),
    )
    assert destination_node.translate.get() == original_translate
    assert _world_position(maya_cmds, destination) != pytest.approx(
        original_position
    )


def test_match_rotation_rejects_blocked_selected_plug(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("joint", name="destination")
    maya_cmds.setAttr(f"{destination}.jointOrientY", lock=True)
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.joint(destination)

    with pytest.raises(RuntimeError, match=r"destination\.jointOrientY"):
        destination_node.match_rotation_to_joint_orient(source_node)


def test_match_rotation_ignores_blocked_untouched_rotation_plug(
    new_scene,
    maya_cmds,
    maya_om,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("joint", name="destination")
    maya_cmds.setAttr(f"{source}.rotate", 10.0, 20.0, 30.0)
    maya_cmds.setAttr(f"{destination}.rotateAxisX", lock=True)
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.joint(destination)

    destination_node.match_rotation_to_joint_orient(source_node)
    nodes.modifier_manager.do_it_dg()

    _assert_rotation_close(
        _world_rotation(maya_cmds, maya_om, destination),
        _world_rotation(maya_cmds, maya_om, source),
    )


@pytest.mark.parametrize(
    "method_name",
    ("match_position", "match_rotation_to_rotate"),
)
def test_match_methods_require_dag_source(
    new_scene,
    maya_cmds,
    method_name,
):
    import bd_util as bdu

    destination = maya_cmds.createNode("transform", name="destination")
    source = maya_cmds.createNode("plusMinusAverage", name="source")
    nodes = bdu.Nodes()
    destination_node = nodes.existing.transform(destination)
    source_node = nodes.existing.plusMinusAverage(source)

    with pytest.raises(TypeError, match="source must be DAG"):
        getattr(destination_node, method_name)(source_node)


@pytest.mark.parametrize("instanced_node", ("source", "destination"))
def test_match_methods_reject_instanced_dag(
    new_scene,
    maya_cmds,
    instanced_node,
):
    import bd_util as bdu

    source = maya_cmds.createNode("transform", name="source")
    destination = maya_cmds.createNode("transform", name="destination")
    maya_cmds.instance(source if instanced_node == "source" else destination)
    nodes = bdu.Nodes()
    source_node = nodes.existing.transform(source)
    destination_node = nodes.existing.transform(destination)

    with pytest.raises(RuntimeError, match="instanced DAG"):
        destination_node.match_position(source_node)
