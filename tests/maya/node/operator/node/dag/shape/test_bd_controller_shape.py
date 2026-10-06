# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya


def _load_bd_util_nodes(maya_cmds) -> None:
    default_path = (
        Path(__file__).resolve().parents[7]
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
        pytest.skip("bdUtilNodes.mll is not built")
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    maya_cmds.currentUnit(angle="degree")


def _create_controller(maya_cmds, *, name="controller") -> tuple[str, str]:
    transform = maya_cmds.createNode("transform", name=name)
    shape = maya_cmds.createNode(
        "bdControllerShape", parent=transform, name=f"{name}Shape"
    )
    return transform, shape


def _bounds(maya_om, shape: str) -> tuple[float, ...]:
    selection = maya_om.MSelectionList()
    selection.add(shape)
    bounds = maya_om.MFnDagNode(selection.getDagPath(0)).boundingBox
    return (
        bounds.min.x,
        bounds.min.y,
        bounds.min.z,
        bounds.max.x,
        bounds.max.y,
        bounds.max.z,
    )


def test_node_type_defaults_and_single_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)

    selection = maya_om.MSelectionList()
    selection.add(shape)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0014271F
    assert maya_cmds.nodeType(shape) == "bdControllerShape"
    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert maya_cmds.attributeQuery("shape", node=shape, listEnum=True) == [
        "Square:Cube:Circle:CircleArrow"
    ]
    assert maya_cmds.getAttr(f"{shape}.shape") == 0
    for attribute, default in (("shape1stAxis", 4), ("shape2ndAxis", 2)):
        assert maya_cmds.attributeQuery(
            attribute, node=shape, listEnum=True
        ) == ["+X:-X:+Y:-Y:+Z:-Z"]
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
    assert maya_cmds.getAttr(f"{shape}.shapeRootSize") == pytest.approx(1.0)
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix", type=True)
        == "matrix"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAnimationTransformMatrix", node=shape, attributeType=True
        )
        == "typed"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAnimationTransformMatrix", node=shape, shortName=True
        )
        == "satm"
    )
    matrix_data = maya_om.MFnMatrixData(
        node_fn.findPlug("shapeAnimationTransformMatrix", False).asMObject()
    )
    assert list(matrix_data.matrix()) == pytest.approx(list(maya_om.MMatrix()))
    assert maya_cmds.getAttr(f"{shape}.shapeTranslate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeRotate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeScale")[0] == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(
        f"{shape}.shapeAxisOffsetLength"
    ) == pytest.approx(1.0)
    assert (
        maya_cmds.attributeQuery(
            "shapeAxisOffsetLength", node=shape, shortName=True
        )
        == "saol"
    )
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetLength", node=shape, minExists=True
    )
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetLength", node=shape, minimum=True
    ) == [0.0]
    assert not maya_cmds.getAttr(f"{shape}.shapeAxisOffset")
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection") == 0
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetDirection", node=shape, listEnum=True
    ) == ["+1stAxis:-1stAxis:+2ndAxis:-2ndAxis:+3rdAxis:-3rdAxis"]
    assert (
        maya_cmds.attributeQuery("shapeAxisOffset", node=shape, shortName=True)
        == "sao"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAxisOffsetDirection", node=shape, shortName=True
        )
        == "saod"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisTranslate")[
        0
    ] == pytest.approx((0.0, 0.0, 0.0))
    assert maya_cmds.getAttr(f"{shape}.shapeAxisRotate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScale")[0] == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeSize") == pytest.approx(1.0)
    assert not maya_cmds.getAttr(f"{shape}.showShapeOffsetLine")
    assert not maya_cmds.getAttr(f"{shape}.shapeOffsetLineTemplate")
    assert (
        maya_cmds.attributeQuery(
            "shapeOffsetLineTemplate", node=shape, shortName=True
        )
        == "solt"
    )
    assert not maya_cmds.attributeQuery(
        "shapeOffsetLineSelectable", node=shape, exists=True
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeTranslateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeRotateX", type=True) == "doubleAngle"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeScaleX", type=True) == "double"
    assert not maya_cmds.getAttr(
        f"{shape}.shapeAnimationTransformMatrix", keyable=True
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisOffsetLength", type=True)
        == "doubleLinear"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffset", type=True) == "bool"
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection", type=True)
        == "enum"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisTranslateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisRotateX", type=True)
        == "doubleAngle"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScaleX", type=True) == "double"
    for attribute in (
        "shape",
        "shape1stAxis",
        "shape2ndAxis",
        "shapeRootSize",
        "shapeTranslate",
        "shapeTranslateX",
        "shapeTranslateY",
        "shapeTranslateZ",
        "shapeRotate",
        "shapeRotateX",
        "shapeRotateY",
        "shapeRotateZ",
        "shapeScale",
        "shapeScaleX",
        "shapeScaleY",
        "shapeScaleZ",
        "shapeAxisOffsetLength",
        "shapeAxisOffset",
        "shapeAxisOffsetDirection",
        "shapeAxisTranslate",
        "shapeAxisTranslateX",
        "shapeAxisTranslateY",
        "shapeAxisTranslateZ",
        "shapeAxisRotate",
        "shapeAxisRotateX",
        "shapeAxisRotateY",
        "shapeAxisRotateZ",
        "shapeAxisScale",
        "shapeAxisScaleX",
        "shapeAxisScaleY",
        "shapeAxisScaleZ",
        "shapeSize",
        "showShapeOffsetLine",
        "shapeOffsetLineTemplate",
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)

    channel_order = maya_cmds.listAttr(shape, keyable=True)
    ordered_attributes = (
        "shape",
        "shape1stAxis",
        "shape2ndAxis",
        "shapeRootSize",
        "shapeTranslateX",
        "shapeRotateX",
        "shapeScaleX",
        "shapeAxisOffsetLength",
        "shapeAxisOffset",
        "shapeAxisOffsetDirection",
        "shapeAxisTranslateX",
        "shapeAxisRotateX",
        "shapeAxisScaleX",
        "shapeSize",
        "showShapeOffsetLine",
        "shapeOffsetLineTemplate",
    )
    assert [
        channel_order.index(attribute) for attribute in ordered_attributes
    ] == sorted(
        channel_order.index(attribute) for attribute in ordered_attributes
    )


def test_inherited_locator_channels_are_hidden_only_on_controller_shape(
    maya_cmds, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    locator_shape = maya_cmds.createNode(
        "locator", name="standardLocatorShape"
    )
    inherited_channels = (
        "localPositionX",
        "localPositionY",
        "localPositionZ",
        "localScaleX",
        "localScaleY",
        "localScaleZ",
    )

    def assert_channel_visibility() -> None:
        for attribute in inherited_channels:
            assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
            assert not maya_cmds.getAttr(
                f"{shape}.{attribute}", channelBox=True
            )
            assert maya_cmds.getAttr(
                f"{locator_shape}.{attribute}", channelBox=True
            )

    assert_channel_visibility()

    scene_path = tmp_path / "controller_shape_channels.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert_channel_visibility()


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (0, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (1, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (2, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (3, (-0.32, -0.32, 0.0, 0.32, 0.5, 0.0)),
    ),
)
def test_shape_bounds(
    maya_cmds, maya_om, new_scene, shape_value, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", shape_value)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_circle_arrow_uses_one_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 3)

    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.32, -0.32, 0.0, 0.32, 0.5, 0.0), abs=1.0e-9
    )


def test_shape_transform_order_and_dirty_bounds(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeRotate", 0.0, 0.0, 90.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 1.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.5)

    assert _bounds(maya_om, shape) == pytest.approx(
        (1.5, 3.0, 6.0, 2.5, 5.0, 6.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.0, 2.0, 6.0, 3.0, 6.0, 6.0), abs=1.0e-9
    )


def test_animation_matrix_connection_updates_bounds_at_keyframes(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("composeMatrix", name="animatedShapeMatrix")
    maya_cmds.setAttr(f"{shape}.shape", 1)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 2.0)
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setKeyframe(source, attribute="inputTranslateX", time=1, value=0)
    maya_cmds.setKeyframe(
        source, attribute="inputTranslateX", time=10, value=5
    )
    maya_cmds.setKeyframe(source, attribute="inputScaleZ", time=1, value=1)
    maya_cmds.setKeyframe(source, attribute="inputScaleZ", time=10, value=2)

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 2.0), abs=1.0e-9
    )

    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, -0.5, 0.0, 5.5, 0.5, 4.0), abs=1.0e-9
    )

    scene_path = tmp_path / "controller_shape_animation.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, -0.5, 0.0, 5.5, 0.5, 4.0), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 2.0), abs=1.0e-9
    )


def test_animation_matrix_moves_offset_line_endpoint_from_origin(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("composeMatrix", name="animatedShapeMatrix")
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setAttr(f"{source}.inputTranslateZ", 3.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 3.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 3.5), abs=1.0e-9
    )


def test_animation_matrix_set_uses_modifier_history(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    matrix = maya_om.MMatrix((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1))

    shape.shapeAnimationTransformMatrix.set(matrix)
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0), abs=1.0e-9
    )
    mod.do_it_dg()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (1.5, -0.5, 0.0, 2.5, 0.5, 0.0), abs=1.0e-9
    )
    mod.undo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0), abs=1.0e-9
    )
    mod.redo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (1.5, -0.5, 0.0, 2.5, 0.5, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "expected_position"),
    (
        (4, 2, (1.0, 0.0, 0.0)),  # +Z, +Y: identity
        (0, 2, (0.0, 0.0, -1.0)),  # +X, +Y: local +X becomes -Z
        (5, 2, (-1.0, 0.0, 0.0)),  # -Z, +Y: local +X becomes -X
        (2, 0, (0.0, 0.0, 1.0)),  # +Y, +X: local +X becomes +Z
        (2, 3, (-1.0, 0.0, 0.0)),  # Invalid: +Y keeps primary, uses +Z
        (4, 5, (1.0, 0.0, 0.0)),  # Invalid: +Z keeps primary, uses +Y
    ),
)
def test_axis_orientation_and_invalid_pair_fallback(
    maya_cmds, maya_om, new_scene, first_axis, second_axis, expected_position
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", second_axis)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_position, *expected_position), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("size", "expected_bounds"),
    (
        (1.0, (-0.5, -0.5, 0.0, 0.5, 0.5, 1.0)),
        (2.0, (-1.0, -1.0, -0.5, 1.0, 1.0, 1.5)),
    ),
)
def test_cube_axis_offset_is_fixed_after_shape_size(
    maya_cmds, maya_om, new_scene, size, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 1)  # Cube
    maya_cmds.setAttr(f"{shape}.shapeSize", size)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("direction", "expected_bounds"),
    (
        (0, (-0.5, -0.5, 0.0, 0.5, 0.5, 3.0)),
        (1, (-0.5, -0.5, -3.0, 0.5, 0.5, 0.0)),
        (2, (-0.5, 0.0, -0.5, 0.5, 3.0, 0.5)),
        (3, (-0.5, -3.0, -0.5, 0.5, 0.0, 0.5)),
        (4, (0.0, -0.5, -0.5, 3.0, 0.5, 0.5)),
        (5, (-3.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
    ),
)
def test_cube_axis_offset_length_anchors_selected_direction(
    maya_cmds, maya_om, new_scene, direction, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 1)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_axis_offset_length_also_scales_centered_shape_and_axis_translation(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 1)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -1.5, 0.5, 0.5, 1.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 0.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 4.5, 0.0, 0.0, 4.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 4.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 3.0), abs=1.0e-9
    )


def test_axis_offset_length_accepts_distance_connection_across_scene_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(linear="m")
    try:
        _, shape = _create_controller(maya_cmds)
        source = maya_cmds.createNode("transform", name="boneLengthSource")
        maya_cmds.setAttr(f"{shape}.shape", 1)
        maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
        maya_cmds.connectAttr(
            f"{source}.translateX", f"{shape}.shapeAxisOffsetLength"
        )
        maya_cmds.setAttr(f"{source}.translateX", 2.0)
        assert maya_cmds.getAttr(
            f"{shape}.shapeAxisOffsetLength"
        ) == pytest.approx(2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.5, -0.5, 0.0, 0.5, 0.5, 200.0), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", 3.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.5, -0.5, 0.0, 0.5, 0.5, 300.0), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", -2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0), abs=1.0e-9
        )
    finally:
        maya_cmds.currentUnit(linear="cm")


def test_axis_offset_length_updates_bounds_after_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 1)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 2.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 2.0), abs=1.0e-9
    )
    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 1.0), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 2.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "direction", "expected_position"),
    (
        (4, 2, 0, (0.0, 0.0, 0.5)),
        (4, 2, 1, (0.0, 0.0, -0.5)),
        (4, 2, 2, (0.0, 0.5, 0.0)),
        (4, 2, 3, (0.0, -0.5, 0.0)),
        (4, 2, 4, (0.5, 0.0, 0.0)),
        (4, 2, 5, (-0.5, 0.0, 0.0)),
        (0, 2, 0, (0.5, 0.0, 0.0)),
        (0, 2, 4, (0.0, 0.0, -0.5)),
        (5, 2, 0, (0.0, 0.0, -0.5)),
        (2, 3, 4, (-0.5, 0.0, 0.0)),
    ),
)
def test_axis_offset_uses_selected_basis_and_invalid_pair_fallback(
    maya_cmds,
    maya_om,
    new_scene,
    first_axis,
    second_axis,
    direction,
    expected_position,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", second_axis)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_position, *expected_position), abs=1.0e-9
    )


def test_axis_transform_is_between_outer_and_inner_transform(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)  # +X
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)  # +Y
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 3.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisScale", 2.0, 1.0, 1.0, type="double3")

    assert _bounds(maya_om, shape) == pytest.approx(
        (-4.0, 8.0, 2.0, 8.0, 8.0, 10.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-4.0, 0.0, 0.0, 8.0, 8.0, 10.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-4.0, 0.0, 0.0, 8.0, 10.0, 10.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)  # +3rdAxis
    assert _bounds(maya_om, shape) == pytest.approx(
        (-4.0, 0.0, -2.0, 8.0, 8.0, 6.0), abs=1.0e-9
    )


def test_axis_offset_does_not_move_offset_line_endpoint(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 1)  # -1stAxis
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.5, 0.0, 0.0, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 1.0), abs=1.0e-9
    )


def test_axis_offset_updates_bounds_after_direct_changes_and_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.5, 0.0, 0.0, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0.0, 0.0, -0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )

    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0.0, 0.0, -0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("animated_attribute", "other_attribute", "other_value", "expected_start"),
    (
        ("shapeAxisOffset", "shapeAxisOffsetDirection", 5, (0.0, 0.0, 0.0)),
        ("shapeAxisOffsetDirection", "shapeAxisOffset", 1, (0.0, 0.0, 0.5)),
    ),
)
def test_connected_axis_offset_updates_bounds_at_keyframes(
    maya_cmds,
    maya_om,
    new_scene,
    animated_attribute,
    other_attribute,
    other_value,
    expected_start,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.{other_attribute}", other_value)
    maya_cmds.setKeyframe(shape, attribute=animated_attribute, time=1, value=0)
    maya_cmds.setKeyframe(
        shape,
        attribute=animated_attribute,
        time=10,
        value=1 if animated_attribute == "shapeAxisOffset" else 5,
    )

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_start, *expected_start), abs=1.0e-9
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0.0, 0.0, -0.5, 0.0, 0.0), abs=1.0e-9
    )


def test_connected_axis_translation_updates_bounds_at_keyframes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setKeyframe(
        shape, attribute="shapeAxisTranslateX", time=1, value=0
    )
    maya_cmds.setKeyframe(
        shape, attribute="shapeAxisTranslateX", time=10, value=2
    )

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0), abs=1.0e-9
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.5, -0.5, 0.0, 2.5, 0.5, 0.0), abs=1.0e-9
    )


def test_shape_offset_line_expands_bounds_and_round_trips(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -1.0, 0.0, 5.0, 1.0, 0.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -1.0, 0.0, 5.0, 1.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeOffsetLineTemplate", True)

    scene_path = tmp_path / "controller_shape_offset_line.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(f"{shape}.showShapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape}.shapeOffsetLineTemplate")
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -1.0, 0.0, 5.0, 1.0, 0.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -1.0, 0.0, 5.0, 1.0, 0.0), abs=1.0e-9
    )


def test_scene_round_trip_preserves_circle_arrow(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds, name="savedController")
    maya_cmds.setAttr(f"{shape}.shape", 3)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)  # +X
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)  # +Y
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)  # +3rdAxis
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeSize", 1.5)

    scene_path = tmp_path / "controller_shape.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert maya_cmds.getAttr(f"{shape}.shape") == 3
    assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffset")
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection") == 4
    assert maya_cmds.getAttr(f"{shape}.shapeAxisTranslateZ") == pytest.approx(
        2.0
    )
    assert maya_cmds.getAttr(f"{shape}.shapeSize") == pytest.approx(1.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.0, -0.48, -0.98, 2.0, 0.75, -0.02), abs=1.0e-9
    )


def test_nodes_controller_shape_helper_supports_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = nodes.create.controllerShape(name="rig_ctrl")
    shape.shape.set(3)
    shape.shape1stAxis.set(0)
    shape.shape2ndAxis.set(2)
    shape.shapeAxisOffset.set(True)
    shape.shapeAxisOffsetDirection.set(0)
    shape.shapeAxisTranslate.set(0.0, 0.0, 2.0)
    shape.shapeSize.set(2.0)
    shape.showShapeOffsetLine.set(True)
    shape.shapeOffsetLineTemplate.set(True)
    mod.do_it_dag()
    mod.do_it_dg()

    assert maya_cmds.nodeType(shape.full_path) == "bdControllerShape"
    assert maya_cmds.getAttr(f"{shape.full_path}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape.full_path}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffset")
    assert (
        maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffsetDirection") == 0
    )
    assert maya_cmds.getAttr(
        f"{shape.full_path}.shapeAxisTranslateZ"
    ) == pytest.approx(2.0)
    assert maya_cmds.getAttr(f"{shape.full_path}.showShapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLineTemplate")
    assert maya_cmds.listRelatives(
        transform.full_path, shapes=True, fullPath=True
    ) == [shape.full_path]
    assert _bounds(maya_om, shape.full_path) == pytest.approx(
        (0.0, -0.64, -0.64, 2.5, 1.0, 0.64), abs=1.0e-9
    )

    mod.undo_it()
    assert not maya_cmds.objExists("rig_ctrl")
    mod.redo_it()
    assert maya_cmds.objExists(transform.full_path)
    assert maya_cmds.getAttr(f"{shape.full_path}.shape") == 3
    assert maya_cmds.getAttr(f"{shape.full_path}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape.full_path}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffset")
    assert (
        maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffsetDirection") == 0
    )
    assert maya_cmds.getAttr(
        f"{shape.full_path}.shapeAxisTranslateZ"
    ) == pytest.approx(2.0)
    assert maya_cmds.getAttr(f"{shape.full_path}.showShapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLineTemplate")
