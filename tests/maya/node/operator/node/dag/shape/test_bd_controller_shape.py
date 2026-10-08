# coding: utf-8
from __future__ import annotations

import os
from pathlib import Path

import pytest

import bd_util as bdu

pytestmark = pytest.mark.maya

SHAPE_NAMES = (
    "Gear",
    "Line1st",
    "Line2nd",
    "Line3rd",
    "CrossLineXY",
    "CrossLineXYZ",
    "Triangle",
    "TriangleFilled",
    "TriangleArrow3D",
    "Square",
    "SquareFilled",
    "SquareArrow2D",
    "SquareArrow3D",
    "SquareArrowCrossLine2D",
    "SquareArrowCrossLine3D",
    "SquareArrowCrossLineTemplate2D",
    "SquareArrowCrossLineTemplate3D",
    "SquareArrow4Way2D",
    "SquareArrow4Way3D",
    "SquareTemplateArrow4Way2D",
    "SquareTemplateArrow4Way3D",
    "Cube",
    "CubeFilled",
    "CubeArrow2D",
    "CubeArrow3D",
    "CubeFin",
    "CubeFinArrow",
    "Octahedron",
    "OctahedronFilled",
    "OctahedronArrow",
    "OctahedronArrowFin",
    "Circle",
    "CircleFilled",
    "CircleArrow2D",
    "CircleArrow3D",
    "Semicircle",
    "SemicircleArrow2D",
    "SemicircleArrow3D",
    "Sphere",
    "SphereFilled",
    "SphereArrow2D",
    "SphereArrow3D",
    "Cylinder",
    "CylinderFilled",
    "CylinderFin",
    "CylinderFinArrow",
    "Arrow",
    "ArrowFin",
    "Pyramid",
    "PyramidFilled",
    "PyramidFin",
    "Cone",
    "ConeFilled",
    "ConeFin",
    "ColorCrossLine",
    "ColorSphere",
    "ColorSphereCrossLine",
)


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
        ":".join(SHAPE_NAMES)
    ]
    assert maya_cmds.getAttr(f"{shape}.shape") == 9
    for attribute, default in (("shape1stAxis", 0), ("shape2ndAxis", 2)):
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
    for attribute, short_name, default in (
        ("shapeLineWidth", "slw", 1.0),
        ("shapeTransparency", "stp", 0.0),
        ("shapeFillTransparency", "sftp", pytest.approx(0.85)),
        ("shapeDrawOnTop", "sdot", False),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    assert maya_cmds.getAttr(f"{shape}.shapeLineWidth", type=True) == "float"
    assert (
        maya_cmds.getAttr(f"{shape}.shapeTransparency", type=True) == "float"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeFillTransparency", type=True)
        == "float"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeDrawOnTop", type=True) == "bool"
    assert maya_cmds.attributeQuery(
        "shapeLineWidth", node=shape, minimum=True
    ) == [1.0]
    assert maya_cmds.attributeQuery(
        "shapeTransparency", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeTransparency", node=shape, maximum=True
    ) == [1.0]
    assert maya_cmds.attributeQuery(
        "shapeFillTransparency", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeFillTransparency", node=shape, maximum=True
    ) == [1.0]
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
    assert not maya_cmds.getAttr(
        f"{shape}.shapeAnimationTransformMatrix", channelBox=True
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
        "shapeLineWidth",
        "shapeTransparency",
        "shapeFillTransparency",
        "shapeDrawOnTop",
    ):
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)

    for index in range(1, 6):
        separator = "_" * index
        assert (
            maya_cmds.attributeQuery(separator, node=shape, shortName=True)
            == separator
        )
        assert maya_cmds.attributeQuery(
            separator, node=shape, listEnum=True
        ) == ["-----------------------------------"]
        assert maya_cmds.getAttr(f"{shape}.{separator}", type=True) == "enum"
        assert maya_cmds.getAttr(f"{shape}.{separator}") == 0
        assert maya_cmds.getAttr(f"{shape}.{separator}", lock=True)
        assert not maya_cmds.getAttr(f"{shape}.{separator}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{separator}", channelBox=True)

    channel_order = maya_cmds.listAttr(shape, channelBox=True)
    ordered_attributes = (
        "shape",
        "shapeDrawOnTop",
        "shapeLineWidth",
        "shapeTransparency",
        "shapeFillTransparency",
        "showShapeOffsetLine",
        "shapeOffsetLineTemplate",
        "_",
        "shape1stAxis",
        "shape2ndAxis",
        "shapeAxisOffset",
        "shapeAxisOffsetDirection",
        "shapeAxisOffsetLength",
        "__",
        "shapeRootSize",
        "shapeTranslateX",
        "shapeRotateX",
        "shapeScaleX",
        "shapeAxisTranslateX",
        "shapeAxisRotateX",
        "shapeAxisScaleX",
        "shapeSize",
        "___",
        "boundsMode",
        "showBoundsPreview",
        "____",
        "customBounds1stAxis",
        "customBounds2ndAxis",
        "customBoundsAxisOffset",
        "customBoundsAxisOffsetDirection",
        "customBoundsAxisOffsetLength",
        "_____",
        "customBoundsRootSize",
        "customBoundsTranslateX",
        "customBoundsRotateX",
        "customBoundsScaleX",
        "customBoundsAxisTranslateX",
        "customBoundsAxisRotateX",
        "customBoundsAxisScaleX",
        "customBoundsSize",
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
        (6, (0.0, -0.37, -0.5, 0.0, 0.5, 0.5)),
        (7, (0.0, -0.37, -0.5, 0.0, 0.5, 0.5)),
        (9, (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (10, (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (21, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (22, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (27, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (28, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (31, (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (32, (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (33, (0.0, -0.5, -0.5, 0.0, 0.625, 0.5)),
        (38, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (39, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (42, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (43, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (48, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (49, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (51, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (52, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
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


def test_sphere_filled_bounds_include_surface_vertices(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = (
        1.0,
        0.0,
        0.0,
        0.0,
        1.0,
        1.0,
        0.0,
        0.0,
        1.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
    )
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix, type="matrix"
    )
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Sphere"))
    wire_bounds = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("SphereFilled"))
    filled_bounds = _bounds(maya_om, shape)

    assert filled_bounds[3] > wire_bounds[3] + 0.1
    assert filled_bounds[0] < wire_bounds[0] - 0.1


@pytest.mark.parametrize(
    "shape_value", range(len(SHAPE_NAMES)), ids=SHAPE_NAMES
)
def test_every_preset_has_a_drawable_extent(
    maya_cmds, maya_om, new_scene, shape_value
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", shape_value)

    bounds = _bounds(maya_om, shape)
    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert any(bounds[axis + 3] > bounds[axis] for axis in range(3))


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (0, (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),  # Gear
        (1, (-0.5, 0.0, 0.0, 0.5, 0.0, 0.0)),  # Line1st
        (2, (0.0, -0.5, 0.0, 0.0, 0.5, 0.0)),  # Line2nd
        (3, (0.0, 0.0, -0.5, 0.0, 0.0, 0.5)),  # Line3rd
        (25, (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5)),  # CubeFin
        (26, (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5)),  # CubeFinArrow
        (29, (-0.5, -0.5, -0.5, 1.5, 0.5, 0.5)),  # OctahedronArrow
        (34, (0.0, -0.5, -0.5, 0.0625, 0.625, 0.5)),  # CircleArrow3D
        (35, (0.0, 0.0, -0.5, 0.0, 0.5, 0.5)),  # Semicircle
        (45, (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5)),  # CylinderFinArrow
        (54, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),  # ColorCrossLine
        (55, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),  # ColorSphere
        (56, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),  # ColorSphereCrossLine
    ),
)
def test_preset_base_and_decoration_bounds(
    maya_cmds, maya_om, new_scene, shape_value, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", shape_value)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (1, (0.0, 0.0, -0.5, 0.0, 0.0, 0.5)),  # Line1st
        (2, (0.0, -0.5, 0.0, 0.0, 0.5, 0.0)),  # Line2nd
        (3, (-0.5, 0.0, 0.0, 0.5, 0.0, 0.0)),  # Line3rd
    ),
)
def test_line_follows_selected_axis_basis(
    maya_cmds, maya_om, new_scene, shape_value, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", shape_value)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)  # +Z

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (6, (-0.5, -0.37, 0.0, 0.5, 0.5, 0.0)),
        (7, (-0.5, -0.37, 0.0, 0.5, 0.5, 0.0)),
        (9, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (10, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (31, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (32, (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (33, (-0.5, -0.5, 0.0, 0.5, 0.625, 0.0)),
    ),
)
def test_planar_shape_faces_first_axis(
    maya_cmds, maya_om, new_scene, shape_value, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", shape_value)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)  # +Z

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_draw_style_attributes_preserve_focus_bounds_and_scene_values(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape_name}.shape", 21)
    maya_cmds.setAttr(f"{shape_name}.shapeTranslateX", 3.0)
    maya_cmds.setAttr(f"{shape_name}.showShapeOffsetLine", True)
    maya_cmds.setAttr(f"{shape_name}.customBoundsSize", 2.0)
    maya_cmds.setAttr(f"{shape_name}.showBoundsPreview", True)

    expected_bounds = {}
    for mode in range(3):
        maya_cmds.setAttr(f"{shape_name}.boundsMode", mode)
        expected_bounds[mode] = _bounds(maya_om, shape_name)

    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    shape.shapeLineWidth.set(2.5)
    shape.shapeTransparency.set(0.375)
    shape.shapeFillTransparency.set(0.25)
    shape.shapeDrawOnTop.set(True)
    mod.do_it_dg()

    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        2.5
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeTransparency"
    ) == pytest.approx(0.375)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    for mode, bounds in expected_bounds.items():
        maya_cmds.setAttr(f"{shape_name}.boundsMode", mode)
        assert _bounds(maya_om, shape_name) == pytest.approx(bounds)

    mod.undo_it()
    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        1.0
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeTransparency"
    ) == pytest.approx(0.0)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.85)
    assert not maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    mod.redo_it()

    scene_path = tmp_path / "controller_shape_draw_style.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        2.5
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeTransparency"
    ) == pytest.approx(0.375)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected_bounds[2])


def test_bounds_modes_and_custom_attribute_defaults(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)

    assert maya_cmds.attributeQuery(
        "boundsMode", node=shape, listEnum=True
    ) == ["Shape:ShapeCentered:Custom"]
    assert maya_cmds.getAttr(f"{shape}.boundsMode") == 0
    assert not maya_cmds.getAttr(f"{shape}.showBoundsPreview")
    assert (
        maya_cmds.attributeQuery(
            "showBoundsPreview", node=shape, shortName=True
        )
        == "sbp"
    )
    assert not maya_cmds.attributeQuery(
        "showCustomBoundsPreview", node=shape, exists=True
    )
    for attribute, default in (
        ("customBounds1stAxis", 0),
        ("customBounds2ndAxis", 2),
        ("customBoundsRootSize", 1.0),
        ("customBoundsAxisOffsetLength", 1.0),
        ("customBoundsAxisOffset", False),
        ("customBoundsAxisOffsetDirection", 0),
        ("customBoundsSize", 1.0),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    for attribute, expected in (
        ("customBoundsTranslate", (0.0, 0.0, 0.0)),
        ("customBoundsRotate", (0.0, 0.0, 0.0)),
        ("customBoundsScale", (1.0, 1.0, 1.0)),
        ("customBoundsAxisTranslate", (0.0, 0.0, 0.0)),
        ("customBoundsAxisRotate", (0.0, 0.0, 0.0)),
        ("customBoundsAxisScale", (1.0, 1.0, 1.0)),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}")[0] == pytest.approx(
            expected
        )
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
        for axis in "XYZ":
            child = f"{attribute}{axis}"
            assert not maya_cmds.getAttr(f"{shape}.{child}", keyable=True)
            assert maya_cmds.getAttr(f"{shape}.{child}", channelBox=True)
    assert not maya_cmds.getAttr(f"{shape}.showBoundsPreview", keyable=True)
    assert maya_cmds.getAttr(f"{shape}.showBoundsPreview", channelBox=True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)
    )


def test_shape_centered_keeps_size_without_position_offsets(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 21)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 5.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateY", 7.0)
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-2.5, -0.5, -0.5, 2.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -2.5, -0.5, 0.5, 2.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    assert _bounds(maya_om, shape) != pytest.approx(
        (-0.5, -2.5, -0.5, 0.5, 2.5, 0.5)
    )


def test_shape_centered_asymmetry_and_animation_matrix(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = maya_cmds.createNode("composeMatrix")
    maya_cmds.setAttr(f"{shape}.shape", 33)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    maya_cmds.connectAttr(
        f"{matrix}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5625, -0.5, 0.0, 0.5625, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{matrix}.inputTranslateX", 3.0)
    maya_cmds.setAttr(f"{matrix}.inputRotateZ", 90.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.4375, 0.0, -0.5, 3.5625, 0.0, 0.5), abs=1.0e-9
    )


def test_custom_bounds_are_independent_and_preview_does_not_change_focus(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -3.0)
    maya_cmds.setAttr(f"{shape}.customBoundsSize", 2.0)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)

    expected = (-4.0, -1.0, -1.0, -2.0, 1.0, 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)
    maya_cmds.setAttr(f"{shape}.showBoundsPreview", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (10.0, -0.5, -0.5, 10.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -5.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-6.0, -1.0, -1.0, -4.0, 1.0, 1.0), abs=1.0e-9
    )


def test_custom_bounds_transform_and_animation_connection(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = maya_cmds.createNode("composeMatrix")
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffsetLength", 4.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", 3.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -0.5, -0.5, 7.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.5, -0.5, -0.5, 3.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)

    maya_cmds.connectAttr(
        f"{matrix}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setKeyframe(matrix, attribute="inputTranslateX", time=1, value=0)
    maya_cmds.setKeyframe(
        matrix, attribute="inputTranslateX", time=10, value=5
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (8.0, -0.5, -0.5, 12.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -0.5, -0.5, 7.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", False)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffsetLength", 1.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", 0.0)
    maya_cmds.setAttr(f"{shape}.customBoundsScaleX", 2.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRotateZ", 90.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -1.0, -0.5, 0.5, 1.0, 0.5), abs=1.0e-9
    )


def test_connected_custom_bounds_input_updates_at_keyframes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setKeyframe(
        shape, attribute="customBoundsTranslateX", time=1, value=0
    )
    maya_cmds.setKeyframe(
        shape, attribute="customBoundsTranslateX", time=10, value=5
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, -0.5, -0.5, 5.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )


def test_view_fit_uses_selected_bounds_mode(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -3.0)
    maya_cmds.select(transform)

    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert maya_cmds.xform(
        transform, query=True, boundingBox=True, worldSpace=True
    ) == pytest.approx((-3.5, -0.5, -0.5, -2.5, 0.5, 0.5), abs=1.0e-9)
    maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
    assert maya_cmds.xform(
        "front", query=True, translation=True, worldSpace=True
    )[0] == pytest.approx(-3.0, abs=1.0e-9)

    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    maya_cmds.setAttr(f"{shape}.showBoundsPreview", True)
    maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
    assert maya_cmds.xform(
        "front", query=True, translation=True, worldSpace=True
    )[0] == pytest.approx(10.0, abs=1.0e-9)


def test_circle_arrow_uses_one_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 33)

    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.625, 0.5), abs=1.0e-9
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
        (1.5, 4.0, 4.5, 2.5, 4.0, 7.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.0, 4.0, 3.0, 3.0, 4.0, 9.0), abs=1.0e-9
    )


def test_animation_matrix_connection_updates_bounds_at_keyframes(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("composeMatrix", name="animatedShapeMatrix")
    maya_cmds.setAttr(f"{shape}.shape", 21)
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
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )

    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (5.0, -0.5, -1.0, 7.0, 0.5, 1.0), abs=1.0e-9
    )

    scene_path = tmp_path / "controller_shape_animation.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (5.0, -0.5, -1.0, 7.0, 0.5, 1.0), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
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
        (0.0, -0.5, 0.0, 0.0, 0.5, 3.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.5, 0.0, 3.0), abs=1.0e-9
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
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.do_it_dg()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.undo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.redo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "expected_position"),
    (
        (0, 2, (1.0, 0.0, 0.0)),  # +X, +Y: identity
        (4, 2, (0.0, 0.0, 1.0)),  # +Z, +Y: local +X becomes +Z
        (5, 2, (0.0, 0.0, -1.0)),  # -Z, +Y: local +X becomes -Z
        (2, 0, (0.0, 1.0, 0.0)),  # +Y, +X: local +X becomes +Y
        (2, 3, (0.0, 1.0, 0.0)),  # Invalid: +Y keeps primary, uses +Z
        (4, 5, (0.0, 0.0, 1.0)),  # Invalid: +Z keeps primary, uses +Y
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


@pytest.mark.parametrize("prefix, mode", (("shape", 0), ("customBounds", 2)))
@pytest.mark.parametrize(
    "first_axis, expected_axes",
    (
        (0, ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))),
        (4, ((0.0, 0.0, 1.0), (0.0, 1.0, 0.0), (-1.0, 0.0, 0.0))),
    ),
)
@pytest.mark.parametrize("component, index", (("X", 0), ("Y", 1), ("Z", 2)))
def test_axis_translation_components_follow_selected_basis(
    maya_cmds,
    maya_om,
    new_scene,
    prefix,
    mode,
    first_axis,
    expected_axes,
    component,
    index,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", mode)
    maya_cmds.setAttr(f"{shape}.{prefix}Size", 0.0)
    maya_cmds.setAttr(f"{shape}.{prefix}1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.{prefix}AxisTranslate{component}", 1.0)

    position = expected_axes[index]
    assert _bounds(maya_om, shape) == pytest.approx(
        (*position, *position), abs=1.0e-9
    )


def test_axis_rotate_x_turns_circle_arrow_around_first_axis(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 33)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotateX", 90.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.625), abs=1.0e-9
    )


@pytest.mark.parametrize("prefix, mode", (("shape", 0), ("customBounds", 2)))
def test_axis_scale_x_follows_first_axis(
    maya_cmds, maya_om, new_scene, prefix, mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", mode)
    maya_cmds.setAttr(f"{shape}.shape", 21)
    maya_cmds.setAttr(f"{shape}.{prefix}1stAxis", 4)  # +Z
    maya_cmds.setAttr(f"{shape}.{prefix}AxisScaleX", 3.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -1.5, 0.5, 0.5, 1.5), abs=1.0e-9
    )


def test_custom_bounds_third_axis_offset_matches_axis_z(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setAttr(f"{shape}.customBoundsSize", 0.0)
    maya_cmds.setAttr(f"{shape}.customBounds1stAxis", 4)  # +Z
    maya_cmds.setAttr(
        f"{shape}.customBoundsAxisOffsetDirection", 4
    )  # +3rdAxis
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0.0, 0.0, -0.5, 0.0, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("size", "expected_bounds"),
    (
        (1.0, (0.0, -0.5, -0.5, 1.0, 0.5, 0.5)),
        (2.0, (-0.5, -1.0, -1.0, 1.5, 1.0, 1.0)),
    ),
)
def test_cube_axis_offset_is_fixed_after_shape_size(
    maya_cmds, maya_om, new_scene, size, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 21)  # Cube
    maya_cmds.setAttr(f"{shape}.shapeSize", size)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("direction", "expected_bounds"),
    (
        (0, (0.0, -0.5, -0.5, 3.0, 0.5, 0.5)),
        (1, (-3.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (2, (-0.5, 0.0, -0.5, 0.5, 3.0, 0.5)),
        (3, (-0.5, -3.0, -0.5, 0.5, 0.0, 0.5)),
        (4, (-0.5, -0.5, 0.0, 0.5, 0.5, 3.0)),
        (5, (-0.5, -0.5, -3.0, 0.5, 0.5, 0.0)),
    ),
)
def test_cube_axis_offset_length_anchors_selected_direction(
    maya_cmds, maya_om, new_scene, direction, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 21)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_axis_offset_length_requires_offset_and_scales_axis_translation(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 21)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 0.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, 0.0, 0.0, 4.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 4.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 1.0, 0.0, 0.0), abs=1.0e-9
    )


def test_axis_offset_length_accepts_distance_connection_across_scene_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(linear="m")
    try:
        _, shape = _create_controller(maya_cmds)
        source = maya_cmds.createNode("transform", name="boneLengthSource")
        maya_cmds.setAttr(f"{shape}.shape", 21)
        maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
        maya_cmds.connectAttr(
            f"{source}.translateX", f"{shape}.shapeAxisOffsetLength"
        )
        maya_cmds.setAttr(f"{source}.translateX", 2.0)
        assert maya_cmds.getAttr(
            f"{shape}.shapeAxisOffsetLength"
        ) == pytest.approx(2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 200.0, 0.5, 0.5), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", 3.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 300.0, 0.5, 0.5), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", -2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
        )
    finally:
        maya_cmds.currentUnit(linear="cm")


def test_axis_offset_length_updates_bounds_after_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", 21)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 2.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 1.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "direction", "expected_position"),
    (
        (4, 2, 0, (0.0, 0.0, 0.5)),
        (4, 2, 1, (0.0, 0.0, -0.5)),
        (4, 2, 2, (0.0, 0.5, 0.0)),
        (4, 2, 3, (0.0, -0.5, 0.0)),
        (4, 2, 4, (-0.5, 0.0, 0.0)),
        (4, 2, 5, (0.5, 0.0, 0.0)),
        (0, 2, 0, (0.5, 0.0, 0.0)),
        (0, 2, 4, (0.0, 0.0, 0.5)),
        (5, 2, 0, (0.0, 0.0, -0.5)),
        (2, 3, 4, (0.5, 0.0, 0.0)),
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
    maya_cmds.setAttr(f"{shape}.shapeAxisScale", 1.0, 2.0, 1.0, type="double3")

    assert _bounds(maya_om, shape) == pytest.approx(
        (2.0, 0.0, 10.0, 2.0, 8.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 8.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 10.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)  # +3rdAxis
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 8.0, 22.0), abs=1.0e-9
    )


def test_axis_offset_does_not_move_offset_line_endpoint(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 1)  # -1stAxis
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.5, 0.0, 0.0, 0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 1.0, 0.0, 0.0), abs=1.0e-9
    )


def test_axis_offset_updates_bounds_after_direct_changes_and_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.5, 0.0, 0.0, 0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )

    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("animated_attribute", "other_attribute", "other_value", "expected_start"),
    (
        ("shapeAxisOffset", "shapeAxisOffsetDirection", 5, (0.0, 0.0, 0.0)),
        ("shapeAxisOffsetDirection", "shapeAxisOffset", 1, (0.5, 0.0, 0.0)),
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
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
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
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


def test_shape_offset_line_expands_bounds_and_round_trips(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (4.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
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
        (0.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )


def test_scene_round_trip_preserves_circle_arrow(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds, name="savedController")
    maya_cmds.setAttr(f"{shape}.shape", 33)
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
    assert maya_cmds.getAttr(f"{shape}.shape") == 33
    assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffset")
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection") == 4
    assert maya_cmds.getAttr(f"{shape}.shapeAxisTranslateZ") == pytest.approx(
        2.0
    )
    assert maya_cmds.getAttr(f"{shape}.shapeSize") == pytest.approx(1.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.75, 1.75, 0.0, 0.9375, 3.25), abs=1.0e-9
    )


def test_nodes_controller_shape_helper_supports_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = nodes.create.controllerShape(name="rig_ctrl")
    shape.shape.set(33)
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
        (0.0, -1.0, 0.0, 0.5, 1.25, 3.0), abs=1.0e-9
    )

    mod.undo_it()
    assert not maya_cmds.objExists("rig_ctrl")
    mod.redo_it()
    assert maya_cmds.objExists(transform.full_path)
    assert maya_cmds.getAttr(f"{shape.full_path}.shape") == 33
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


def test_custom_bounds_node_operator_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    shape.boundsMode.set(2)
    shape.customBoundsSize.set(4.0)
    shape.customBoundsTranslate.set(2.0, 0.0, 0.0)
    shape.showBoundsPreview.set(True)
    mod.do_it_dg()

    expected = (0.0, -2.0, -2.0, 4.0, 2.0, 2.0)
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)
    mod.undo_it()
    assert maya_cmds.getAttr(f"{shape_name}.boundsMode") == 0
    assert not maya_cmds.getAttr(f"{shape_name}.showBoundsPreview")
    mod.redo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)

    scene_path = tmp_path / "controller_shape_custom_bounds.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape_name}.boundsMode") == 2
    assert maya_cmds.getAttr(f"{shape_name}.showBoundsPreview")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)
