# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

import bd_util as bdu
from bd_util.maya.node.operator.node.dag.shape._generated.bd_controller_shape import (
    ShapeEnumAttrOperator,
    ShapeEnumPlugOperator,
)

pytestmark = pytest.mark.maya

SHAPE_NAMES = (
    "Gear",
    "GearFilled",
    "Line1st",
    "Line1stArrowAtStart",
    "Line1stArrowAtStartFilled",
    "Line1stArrowAtEnd",
    "Line1stArrowAtEndFilled",
    "Line1stArrowAtEnds",
    "Line1stArrowAtEndsFilled",
    "Line1stWideArrowAtStart",
    "Line1stWideArrowAtStartFilled",
    "Line1stWideArrowAtEnd",
    "Line1stWideArrowAtEndFilled",
    "Line1stWideArrowAtEnds",
    "Line1stWideArrowAtEndsFilled",
    "Line2nd",
    "Line2ndArrowAtStart",
    "Line2ndArrowAtStartFilled",
    "Line2ndArrowAtEnd",
    "Line2ndArrowAtEndFilled",
    "Line2ndArrowAtEnds",
    "Line2ndArrowAtEndsFilled",
    "Line2ndWideArrowAtStart",
    "Line2ndWideArrowAtStartFilled",
    "Line2ndWideArrowAtEnd",
    "Line2ndWideArrowAtEndFilled",
    "Line2ndWideArrowAtEnds",
    "Line2ndWideArrowAtEndsFilled",
    "Line3rd",
    "Line3rdArrowAtStart",
    "Line3rdArrowAtStartFilled",
    "Line3rdArrowAtEnd",
    "Line3rdArrowAtEndFilled",
    "Line3rdArrowAtEnds",
    "Line3rdArrowAtEndsFilled",
    "Line3rdWideArrowAtStart",
    "Line3rdWideArrowAtStartFilled",
    "Line3rdWideArrowAtEnd",
    "Line3rdWideArrowAtEndFilled",
    "Line3rdWideArrowAtEnds",
    "Line3rdWideArrowAtEndsFilled",
    "CrossLine1st2nd",
    "CrossLine1st2ndArrowAt1stStart",
    "CrossLine1st2ndArrowAt1stStartFilled",
    "CrossLine1st2ndArrowAt1stEnd",
    "CrossLine1st2ndArrowAt1stEndFilled",
    "CrossLine1st2ndArrowAt2ndStart",
    "CrossLine1st2ndArrowAt2ndStartFilled",
    "CrossLine1st2ndArrowAt2ndEnd",
    "CrossLine1st2ndArrowAt2ndEndFilled",
    "CrossLine1st2ndArrowAtEnds",
    "CrossLine1st2ndArrowAtEndsFilled",
    "CrossLine1st2ndWideArrowAt1stStart",
    "CrossLine1st2ndWideArrowAt1stStartFilled",
    "CrossLine1st2ndWideArrowAt1stEnd",
    "CrossLine1st2ndWideArrowAt1stEndFilled",
    "CrossLine1st2ndWideArrowAt2ndStart",
    "CrossLine1st2ndWideArrowAt2ndStartFilled",
    "CrossLine1st2ndWideArrowAt2ndEnd",
    "CrossLine1st2ndWideArrowAt2ndEndFilled",
    "CrossLine1st2ndWideArrowAtEnds",
    "CrossLine1st2ndWideArrowAtEndsFilled",
    "CrossLine1st3rd",
    "CrossLine1st3rdArrowAt1stStart",
    "CrossLine1st3rdArrowAt1stStartFilled",
    "CrossLine1st3rdArrowAt1stEnd",
    "CrossLine1st3rdArrowAt1stEndFilled",
    "CrossLine1st3rdArrowAt3rdStart",
    "CrossLine1st3rdArrowAt3rdStartFilled",
    "CrossLine1st3rdArrowAt3rdEnd",
    "CrossLine1st3rdArrowAt3rdEndFilled",
    "CrossLine1st3rdArrowAtEnds",
    "CrossLine1st3rdArrowAtEndsFilled",
    "CrossLine1st3rdWideArrowAt1stStart",
    "CrossLine1st3rdWideArrowAt1stStartFilled",
    "CrossLine1st3rdWideArrowAt1stEnd",
    "CrossLine1st3rdWideArrowAt1stEndFilled",
    "CrossLine1st3rdWideArrowAt3rdStart",
    "CrossLine1st3rdWideArrowAt3rdStartFilled",
    "CrossLine1st3rdWideArrowAt3rdEnd",
    "CrossLine1st3rdWideArrowAt3rdEndFilled",
    "CrossLine1st3rdWideArrowAtEnds",
    "CrossLine1st3rdWideArrowAtEndsFilled",
    "CrossLine2nd3rd",
    "CrossLine2nd3rdArrowAt2ndStart",
    "CrossLine2nd3rdArrowAt2ndStartFilled",
    "CrossLine2nd3rdArrowAt2ndEnd",
    "CrossLine2nd3rdArrowAt2ndEndFilled",
    "CrossLine2nd3rdArrowAt3rdStart",
    "CrossLine2nd3rdArrowAt3rdStartFilled",
    "CrossLine2nd3rdArrowAt3rdEnd",
    "CrossLine2nd3rdArrowAt3rdEndFilled",
    "CrossLine2nd3rdArrowAtEnds",
    "CrossLine2nd3rdArrowAtEndsFilled",
    "CrossLine2nd3rdWideArrowAt2ndStart",
    "CrossLine2nd3rdWideArrowAt2ndStartFilled",
    "CrossLine2nd3rdWideArrowAt2ndEnd",
    "CrossLine2nd3rdWideArrowAt2ndEndFilled",
    "CrossLine2nd3rdWideArrowAt3rdStart",
    "CrossLine2nd3rdWideArrowAt3rdStartFilled",
    "CrossLine2nd3rdWideArrowAt3rdEnd",
    "CrossLine2nd3rdWideArrowAt3rdEndFilled",
    "CrossLine2nd3rdWideArrowAtEnds",
    "CrossLine2nd3rdWideArrowAtEndsFilled",
    "CrossLine3Axis",
    "CrossLine3AxisEndCube",
    "CrossLine3AxisEndCubeFilled",
    "CrossLine3AxisEndOctahedron",
    "CrossLine3AxisEndOctahedronFilled",
    "CrossLine3AxisEndSphere",
    "CrossLine3AxisEndSphereFilled",
    "CrossLine3AxisEndPyramid",
    "CrossLine3AxisEndPyramidFilled",
    "CrossLine3AxisEndCone",
    "CrossLine3AxisEndConeFilled",
    "Triangle",
    "TriangleFilled",
    "TriangleArrow3D",
    "TriangleArrow3DFilled",
    "Square",
    "SquareFilled",
    "SquareArrow2D",
    "SquareArrow2DFilled",
    "SquareArrow3D",
    "SquareArrow3DFilled",
    "SquareArrowCrossLine2D",
    "SquareArrowCrossLine2DFilled",
    "SquareArrowCrossLine3D",
    "SquareArrowCrossLine3DFilled",
    "SquareArrowCrossLineTemplate2D",
    "SquareArrowCrossLineTemplate2DFilled",
    "SquareArrowCrossLineTemplate3D",
    "SquareArrowCrossLineTemplate3DFilled",
    "SquareArrow4Way2D",
    "SquareArrow4Way2DFilled",
    "SquareArrow4Way3D",
    "SquareArrow4Way3DFilled",
    "SquareTemplateArrow4Way2D",
    "SquareTemplateArrow4Way2DFilled",
    "SquareTemplateArrow4Way3D",
    "SquareTemplateArrow4Way3DFilled",
    "Cube",
    "CubeFilled",
    "CubeArrow2D",
    "CubeArrow2DFilled",
    "CubeArrow3D",
    "CubeArrow3DFilled",
    "CubeFin",
    "CubeFinFilled",
    "CubeFinArrow",
    "CubeFinArrowFilled",
    "Octahedron",
    "OctahedronFilled",
    "OctahedronArrow",
    "OctahedronArrowFilled",
    "OctahedronArrowFin",
    "OctahedronArrowFinFilled",
    "Circle",
    "CircleFilled",
    "CircleArrow2D",
    "CircleArrow2DFilled",
    "CircleArrow3D",
    "CircleArrow3DFilled",
    "Semicircle",
    "SemicircleFilled",
    "SemicircleArrowAtStart",
    "SemicircleArrowAtStartFilled",
    "SemicircleArrowAtEnd",
    "SemicircleArrowAtEndFilled",
    "SemicircleArrowAtEnds",
    "SemicircleArrowAtEndsFilled",
    "SemicircleWideArrowAtStart",
    "SemicircleWideArrowAtStartFilled",
    "SemicircleWideArrowAtEnd",
    "SemicircleWideArrowAtEndFilled",
    "SemicircleWideArrowAtEnds",
    "SemicircleWideArrowAtEndsFilled",
    "SemicircleArrow2D",
    "SemicircleArrow2DFilled",
    "SemicircleArrow3D",
    "SemicircleArrow3DFilled",
    "Sphere",
    "SphereFilled",
    "SphereArrow2D",
    "SphereArrow2DFilled",
    "SphereArrow3D",
    "SphereArrow3DFilled",
    "Cylinder",
    "CylinderFilled",
    "CylinderFin",
    "CylinderFinFilled",
    "CylinderFinArrow",
    "CylinderFinArrowFilled",
    "Arrow",
    "ArrowFilled",
    "ArrowFin",
    "ArrowFinFilled",
    "Pyramid",
    "PyramidFilled",
    "PyramidFin",
    "PyramidFinFilled",
    "Cone",
    "ConeFilled",
    "ConeFin",
    "ConeFinFilled",
    "ColorCrossLine3Axis",
    "ColorCrossLine3AxisEndCube",
    "ColorCrossLine3AxisEndCubeFilled",
    "ColorCrossLine3AxisEndOctahedron",
    "ColorCrossLine3AxisEndOctahedronFilled",
    "ColorCrossLine3AxisEndSphere",
    "ColorCrossLine3AxisEndSphereFilled",
    "ColorCrossLine3AxisEndPyramid",
    "ColorCrossLine3AxisEndPyramidFilled",
    "ColorCrossLine3AxisEndCone",
    "ColorCrossLine3AxisEndConeFilled",
    "ColorCube",
    "ColorCubeFilled",
    "ColorCornerCube",
    "ColorCornerCubeFilled",
    "ColorSphere",
    "ColorSphereFilled",
    "ColorSphereArrow2D",
    "ColorSphereArrow2DFilled",
    "ColorSphereArrow3D",
    "ColorSphereArrow3DFilled",
    "ColorSphereCrossLine",
    "ColorSphereCrossLineFilled",
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


def _create_controller(
    maya_cmds,
    *,
    name="controller",
    shape_value=SHAPE_NAMES.index("Square"),
    bounds_mode=0,
) -> tuple[str, str]:
    transform = maya_cmds.createNode("transform", name=name)
    shape = maya_cmds.createNode(
        "bdControllerShape", parent=transform, name=f"{name}Shape"
    )
    if shape_value is not None:
        maya_cmds.setAttr(f"{shape}.shape", shape_value)
    if bounds_mode is not None:
        maya_cmds.setAttr(f"{shape}.boundsMode", bounds_mode)
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


def test_generated_shape_enum_matches_presets():
    assert ShapeEnumAttrOperator.NAME_MAP == dict(enumerate(SHAPE_NAMES))
    assert all(
        getattr(ShapeEnumPlugOperator, name.upper()) == index
        for index, name in enumerate(SHAPE_NAMES)
    )


def test_node_type_defaults_and_single_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(
        maya_cmds, shape_value=None, bounds_mode=None
    )

    selection = maya_om.MSelectionList()
    selection.add(shape)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0014271F
    assert maya_cmds.nodeType(shape) == "bdControllerShape"
    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert maya_cmds.attributeQuery("shape", node=shape, listEnum=True) == [
        ":".join(SHAPE_NAMES)
    ]
    assert maya_cmds.getAttr(f"{shape}.shape") == SHAPE_NAMES.index("Cube")
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
    for attribute, short_name, kind, default in (
        ("shapePartOffset", "spo", "doubleLinear", 0.0),
        ("shapePartFinHeight", "spfh", "doubleLinear", 0.5),
        ("shapePartSize", "sps", "double", 1.0),
        ("shapePartLengthScale", "spls", "double", 1.0),
        ("shapePartWidthScale", "spws", "double", 1.0),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
            default
        )
        assert maya_cmds.getAttr(f"{shape}.{attribute}", type=True) == kind
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert not maya_cmds.attributeQuery(
            attribute, node=shape, minExists=True
        )
        assert not maya_cmds.attributeQuery(
            attribute, node=shape, maxExists=True
        )
    assert maya_cmds.getAttr(f"{shape}.shapePartOffsetAngle") == 0.0
    assert (
        maya_cmds.getAttr(f"{shape}.shapePartOffsetAngle", type=True)
        == "doubleAngle"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapePartOffsetAngle", node=shape, shortName=True
        )
        == "spoa"
    )
    assert maya_cmds.attributeQuery(
        "shapePartOffsetAngle", node=shape, minimum=True
    ) == [-90.0]
    assert maya_cmds.attributeQuery(
        "shapePartOffsetAngle", node=shape, maximum=True
    ) == [90.0]
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
        "shapePartOffset",
        "shapePartOffsetAngle",
        "shapePartFinHeight",
        "shapePartSize",
        "shapePartLengthScale",
        "shapePartWidthScale",
        "showShapeOffsetLine",
        "shapeOffsetLineTemplate",
        "shapeLineWidth",
        "shapeTransparency",
        "shapeFillTransparency",
        "shapeDrawOnTop",
    ):
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)

    for index in range(1, 7):
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
        "shapePartOffset",
        "shapePartOffsetAngle",
        "shapePartFinHeight",
        "shapePartSize",
        "shapePartLengthScale",
        "shapePartWidthScale",
        "______",
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
        (SHAPE_NAMES.index("Triangle"), (0.0, -0.37, -0.5, 0.0, 0.5, 0.5)),
        (
            SHAPE_NAMES.index("TriangleFilled"),
            (0.0, -0.37, -0.5, 0.0, 0.5, 0.5),
        ),
        (SHAPE_NAMES.index("Square"), (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (SHAPE_NAMES.index("SquareFilled"), (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (SHAPE_NAMES.index("Cube"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (SHAPE_NAMES.index("CubeFilled"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (SHAPE_NAMES.index("Octahedron"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            SHAPE_NAMES.index("OctahedronFilled"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        (SHAPE_NAMES.index("Circle"), (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (SHAPE_NAMES.index("CircleFilled"), (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (
            SHAPE_NAMES.index("CircleArrow2D"),
            (0.0, -0.5, -0.5, 0.0, 0.625, 0.5),
        ),
        (SHAPE_NAMES.index("Sphere"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (SHAPE_NAMES.index("SphereFilled"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (SHAPE_NAMES.index("Cylinder"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            SHAPE_NAMES.index("CylinderFilled"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        (SHAPE_NAMES.index("Pyramid"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            SHAPE_NAMES.index("PyramidFilled"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        (SHAPE_NAMES.index("Cone"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (SHAPE_NAMES.index("ConeFilled"), (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
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
    "filled_name",
    tuple(name for name in SHAPE_NAMES if name.endswith("Filled")),
)
def test_filled_preset_preserves_outline_bounds(
    maya_cmds, maya_om, new_scene, filled_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    base_name = filled_name.removesuffix("Filled")
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index(base_name))
    outline_bounds = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index(filled_name))

    assert _bounds(maya_om, shape) == pytest.approx(outline_bounds, abs=1.0e-9)


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (SHAPE_NAMES.index("Gear"), (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),  # Gear
        (
            SHAPE_NAMES.index("Line1st"),
            (-0.5, 0.0, 0.0, 0.5, 0.0, 0.0),
        ),  # Line1st
        (
            SHAPE_NAMES.index("Line2nd"),
            (0.0, -0.5, 0.0, 0.0, 0.5, 0.0),
        ),  # Line2nd
        (
            SHAPE_NAMES.index("Line3rd"),
            (0.0, 0.0, -0.5, 0.0, 0.0, 0.5),
        ),  # Line3rd
        (
            SHAPE_NAMES.index("CubeFin"),
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CubeFin
        (
            SHAPE_NAMES.index("CubeFinArrow"),
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CubeFinArrow
        (
            SHAPE_NAMES.index("OctahedronArrow"),
            (-0.5, -0.5, -0.5, 1.5, 0.5, 0.5),
        ),  # OctahedronArrow
        (
            SHAPE_NAMES.index("CircleArrow3D"),
            (0.0, -0.5, -0.5, 0.0625, 0.625, 0.5),
        ),  # CircleArrow3D
        (
            SHAPE_NAMES.index("Semicircle"),
            (0.0, 0.0, -0.5, 0.0, 0.5, 0.5),
        ),  # Semicircle
        (
            SHAPE_NAMES.index("CylinderFinArrow"),
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CylinderFinArrow
        (
            SHAPE_NAMES.index("ColorCrossLine3Axis"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorCrossLine3Axis
        (
            SHAPE_NAMES.index("ColorSphere"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorSphere
        (
            SHAPE_NAMES.index("ColorSphereArrow2D"),
            (-0.5, -0.5, -0.5, 0.625, 0.5, 0.5),
        ),  # ColorSphereArrow2D
        (
            SHAPE_NAMES.index("ColorSphereArrow3D"),
            (-0.5, -0.5, -0.5, 0.625, 0.5, 0.5),
        ),  # ColorSphereArrow3D
        (
            SHAPE_NAMES.index("ColorSphereCrossLine"),
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorSphereCrossLine
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
        (
            SHAPE_NAMES.index("Line1st"),
            (0.0, 0.0, -0.5, 0.0, 0.0, 0.5),
        ),  # Line1st
        (
            SHAPE_NAMES.index("Line2nd"),
            (0.0, -0.5, 0.0, 0.0, 0.5, 0.0),
        ),  # Line2nd
        (
            SHAPE_NAMES.index("Line3rd"),
            (-0.5, 0.0, 0.0, 0.5, 0.0, 0.0),
        ),  # Line3rd
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
    ("shape_name", "expected"),
    (
        ("CrossLine1st2nd", (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        ("CrossLine1st3rd", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("CrossLine2nd3rd", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        ("CrossLine3Axis", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
    ),
)
def test_crossline_uses_named_axis_plane(
    maya_cmds, maya_om, new_scene, shape_name, expected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    ("base_name", "expected"),
    (
        ("Line1st", (-0.5, -0.05, 0.0, 0.5, 0.05, 0.0)),
        ("Line2nd", (-0.05, -0.5, 0.0, 0.05, 0.5, 0.0)),
        ("Line3rd", (-0.05, 0.0, -0.5, 0.05, 0.0, 0.5)),
        ("CrossLine1st2nd", (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        ("CrossLine1st3rd", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("CrossLine2nd3rd", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        ("Semicircle", (0.0, 0.0, -0.55, 0.0, 0.5, 0.55)),
    ),
)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("remap_axes", (False, True))
@pytest.mark.parametrize("wide", (False, True))
def test_end_arrow_extent_and_axis_transform(
    maya_cmds,
    maya_om,
    new_scene,
    base_name,
    expected,
    filled,
    remap_axes,
    wide,
):
    _load_bd_util_nodes(maya_cmds)
    shape_name = (
        base_name
        + ("WideArrowAtEnds" if wide else "ArrowAtEnds")
        + ("Filled" if filled else "")
    )
    if wide and base_name == "Semicircle":
        expected = (0.0, 0.0, -0.55, 0.0, 0.525, 0.55)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    if remap_axes:
        maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)  # +Z
        maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 3.0, 4.0)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.5)
        xmin, ymin, zmin, xmax, ymax, zmax = expected
        expected = (
            1.5 * (1.0 - 2.0 * zmax),
            1.5 * (2.0 + 3.0 * ymin),
            1.5 * (3.0 + 4.0 * xmin),
            1.5 * (1.0 - 2.0 * zmin),
            1.5 * (2.0 + 3.0 * ymax),
            1.5 * (3.0 + 4.0 * xmax),
        )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    ("end_shape", "extent"),
    (
        ("Cube", 0.55),
        ("Octahedron", 0.55),
        ("Sphere", 0.55),
        ("Pyramid", 0.5),
        ("Cone", 0.5),
    ),
)
@pytest.mark.parametrize("colored", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("remap_axes", (False, True))
def test_crossline_end_solids_extent_and_axis_transform(
    maya_cmds,
    maya_om,
    new_scene,
    end_shape,
    extent,
    colored,
    filled,
    remap_axes,
):
    _load_bd_util_nodes(maya_cmds)
    shape_name = (
        ("Color" if colored else "")
        + "CrossLine3AxisEnd"
        + end_shape
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    expected = (-extent, -extent, -extent, extent, extent, extent)
    if remap_axes:
        maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)
        maya_cmds.setAttr(f"{shape}.shapeScale", -2.0, 3.0, 4.0)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.5)
        expected = (
            1.5 * (1.0 - 2.0 * extent),
            1.5 * (2.0 - 3.0 * extent),
            1.5 * (3.0 - 4.0 * extent),
            1.5 * (1.0 + 2.0 * extent),
            1.5 * (2.0 + 3.0 * extent),
            1.5 * (3.0 + 4.0 * extent),
        )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    ("shape_value", "expected_bounds"),
    (
        (SHAPE_NAMES.index("Triangle"), (-0.5, -0.37, 0.0, 0.5, 0.5, 0.0)),
        (
            SHAPE_NAMES.index("TriangleFilled"),
            (-0.5, -0.37, 0.0, 0.5, 0.5, 0.0),
        ),
        (SHAPE_NAMES.index("Square"), (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (SHAPE_NAMES.index("SquareFilled"), (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (SHAPE_NAMES.index("Circle"), (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (SHAPE_NAMES.index("CircleFilled"), (-0.5, -0.5, 0.0, 0.5, 0.5, 0.0)),
        (
            SHAPE_NAMES.index("CircleArrow2D"),
            (-0.5, -0.5, 0.0, 0.5, 0.625, 0.0),
        ),
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
    maya_cmds.setAttr(f"{shape_name}.shape", SHAPE_NAMES.index("Cube"))
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
    _, shape = _create_controller(
        maya_cmds, shape_value=None, bounds_mode=None
    )

    assert maya_cmds.attributeQuery(
        "boundsMode", node=shape, listEnum=True
    ) == ["Shape:ShapeCentered:Custom"]
    assert maya_cmds.getAttr(f"{shape}.boundsMode") == 1
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
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    )


def test_shape_centered_keeps_size_without_position_offsets(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("CircleArrow2D"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("CircleArrow2D"))

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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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


@pytest.mark.parametrize(
    "end_shape", ("Cube", "Octahedron", "Sphere", "Pyramid", "Cone")
)
@pytest.mark.parametrize("colored", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("offset", "length", "width", "round_extent", "pointed_extent"),
    (
        (0.1, 2.0, 3.0, 0.7, 0.6),
        (-0.2, 0.5, 4.0, 0.325, 0.3),
        (0.0, 2.0, 12.0, 0.6, 0.6),
        (0.1, -2.0, -3.0, 0.7, 0.8),
        (-0.6, 1.0, 1.0, 0.15, 0.2),
        (0.1, 0.0, 1.0, 0.6, 0.6),
        (0.1, 1.0, 0.0, 0.65, 0.6),
    ),
)
def test_part_transform_bounds(
    maya_cmds,
    maya_om,
    new_scene,
    end_shape,
    colored,
    filled,
    offset,
    length,
    width,
    round_extent,
    pointed_extent,
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        ("Color" if colored else "")
        + "CrossLine3AxisEnd"
        + end_shape
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", length)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", width)
    extent = (
        pointed_extent if end_shape in ("Pyramid", "Cone") else round_extent
    )
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, -extent, -extent, extent, extent, extent), abs=1e-9
    )


@pytest.mark.parametrize(
    ("attribute", "value", "extent"),
    (
        ("shapePartOffset", 0.2, 0.75),
        ("shapePartLengthScale", 3.0, 0.65),
        ("shapePartWidthScale", 14.0, 0.7),
        ("shapePartSize", 3.0, 0.65),
    ),
)
@pytest.mark.parametrize("connected", (False, True))
def test_part_attribute_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, attribute, value, extent, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index("ColorCrossLine3AxisEndCubeFilled"),
    )
    target = f"{shape}.{attribute}"
    if connected:
        if attribute == "shapePartOffset":
            source = maya_cmds.createNode("addDoubleLinear")
            target = f"{source}.input1"
            maya_cmds.connectAttr(f"{source}.output", f"{shape}.{attribute}")
        else:
            source = maya_cmds.createNode("multiplyDivide")
            target = f"{source}.input1X"
            maya_cmds.setAttr(target, 1.0)
            maya_cmds.setAttr(f"{source}.input2X", 1.0)
            maya_cmds.connectAttr(f"{source}.outputX", f"{shape}.{attribute}")
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.55, -0.55, -0.55, 0.55, 0.55, 0.55)
    )
    maya_cmds.setAttr(target, value)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, -extent, -extent, extent, extent, extent)
    )
    maya_cmds.setAttr(target, 0.0 if attribute == "shapePartOffset" else 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.55, -0.55, -0.55, 0.55, 0.55, 0.55)
    )


@pytest.mark.parametrize(
    ("end_shape", "extent"), (("Cube", 0.7), ("Cone", 0.6))
)
def test_part_animation_updates_bounds(
    maya_cmds, maya_om, new_scene, end_shape, extent
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index(
            "ColorCrossLine3AxisEnd" + end_shape + "Filled"
        ),
    )
    for attribute, first, last in (
        ("shapePartOffset", 0, 0.1),
        ("shapePartLengthScale", 1, 2),
        ("shapePartWidthScale", 1, 3),
    ):
        maya_cmds.setKeyframe(shape, attribute=attribute, time=1, value=first)
        maya_cmds.setKeyframe(shape, attribute=attribute, time=10, value=last)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, -extent, -extent, extent, extent, extent)
    )
    maya_cmds.currentTime(1)
    initial = 0.55 if end_shape == "Cube" else 0.5
    assert _bounds(maya_om, shape) == pytest.approx(
        (-initial, -initial, -initial, initial, initial, initial)
    )


def test_part_offset_uses_scene_distance_units(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        _, shape = _create_controller(
            maya_cmds, shape_value=SHAPE_NAMES.index("CrossLine3AxisEndCube")
        )
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 1.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.65, -0.65, -0.65, 0.65, 0.65, 0.65)
        )
        maya_cmds.currentUnit(linear="cm")
        assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == pytest.approx(
            0.1
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


@pytest.mark.parametrize("mode", (0, 1, 2))
def test_part_transform_bounds_modes(maya_cmds, maya_om, new_scene, mode):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index("CrossLine3AxisEndCubeFilled"),
        bounds_mode=mode,
    )
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 3.0)
    center = 2.0 if mode == 0 else 0.0
    extent = 0.5 if mode == 2 else 0.7
    assert _bounds(maya_om, shape) == pytest.approx(
        (center - extent, -extent, -extent, center + extent, extent, extent)
    )


def test_part_transform_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shape.set(SHAPE_NAMES.index("ColorCrossLine3AxisEndConeFilled"))
    shape.shapePartOffset.set(0.1)
    shape.shapePartFinHeight.set(0.75)
    shape.shapePartLengthScale.set(2.0)
    shape.shapePartWidthScale.set(3.0)
    shape.shapePartSize.set(2.0)
    shape.shapeSize.set(2.0)
    shape.shapeRootSize.set(2.0)
    shape.shapeTranslate.set(1.0, 2.0, 3.0)
    mod.do_it_dg()
    expected = (-0.4, 1.6, 3.6, 4.4, 6.4, 8.4)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(
        (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "part_transform.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    for attribute, value in (
        ("shapePartOffset", 0.1),
        ("shapePartFinHeight", 0.75),
        ("shapePartLengthScale", 2),
        ("shapePartWidthScale", 3),
        ("shapePartSize", 2),
    ):
        assert maya_cmds.getAttr(f"{name}.{attribute}") == pytest.approx(value)


@pytest.mark.parametrize(
    "shape_name",
    (
        "Cube",
        "CrossLine3Axis",
        "ColorSphereFilled",
        "ColorCornerCubeFilled",
    ),
)
def test_part_attributes_leave_plain_shapes_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 4.0)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 2.0)
    assert _bounds(maya_om, shape) == pytest.approx(before)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("shape_name", "expected"),
    (
        ("SquareArrow2D", (0, -0.5, -0.5, 0, 0.975, 0.5)),
        ("SquareArrow3D", (0, -0.5, -0.5, 0.09375, 0.975, 0.5)),
        ("SquareArrowCrossLine2D", (0, -0.5, -0.5, 0, 0.975, 0.5)),
        ("SquareArrowCrossLine3D", (0, -0.5, -0.5, 0.09375, 0.975, 0.5)),
        ("SquareArrowCrossLineTemplate2D", (0, -0.5, -0.5, 0, 0.975, 0.5)),
        (
            "SquareArrowCrossLineTemplate3D",
            (0, -0.5, -0.5, 0.09375, 0.975, 0.5),
        ),
        ("SquareArrow4Way2D", (0, -0.7875, -0.7875, 0, 0.975, 0.7875)),
        ("SquareArrow4Way3D", (0, -0.7875, -0.7875, 0.09375, 0.975, 0.7875)),
        ("SquareTemplateArrow4Way2D", (0, -0.7875, -0.7875, 0, 0.975, 0.7875)),
        (
            "SquareTemplateArrow4Way3D",
            (0, -0.7875, -0.7875, 0.09375, 0.975, 0.7875),
        ),
        ("TriangleArrow3D", (0, -2.01, -0.5, 0.75, 0.6, 0.5)),
        ("CubeArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("CubeArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("CircleArrow2D", (0, -0.5, -0.5, 0, 0.975, 0.5)),
        ("CircleArrow3D", (0, -0.5, -0.5, 0.09375, 0.975, 0.5)),
        ("SemicircleArrow2D", (0, 0, -0.5, 0, 0.975, 0.5)),
        ("SemicircleArrow3D", (0, 0, -0.5, 0.09375, 0.975, 0.5)),
        ("SphereArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("SphereArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("ColorSphereArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("ColorSphereArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("CubeFin", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CubeFinArrow", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CylinderFin", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CylinderFinArrow", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("PyramidFin", (-0.75, -0.5, -0.5, 0.75, 1.0, 0.5)),
        ("ConeFin", (-0.75, -0.5, -0.5, 0.75, 1.0, 0.5)),
        ("Arrow", (-2.4, 0, -0.75, 0.6, 0, 0.75)),
        ("ArrowFin", (-2.4, 0, -0.75, 0.6, 1.0, 0.75)),
        ("OctahedronArrow", (-0.5, -0.75, -0.75, 3.6, 0.75, 0.75)),
        ("OctahedronArrowFin", (-1.525, -0.75, -0.75, 4.625, 1.0, 0.75)),
        ("Line1stArrowAtEnds", (-0.6, -0.075, 0, 0.6, 0.075, 0)),
        ("Line2ndArrowAtEnds", (-0.075, -0.6, 0, 0.075, 0.6, 0)),
        ("Line3rdArrowAtEnds", (-0.075, 0, -0.6, 0.075, 0, 0.6)),
        ("CrossLine1st2ndArrowAtEnds", (-0.6, -0.6, 0, 0.6, 0.6, 0)),
        ("CrossLine1st3rdArrowAtEnds", (-0.6, 0, -0.6, 0.6, 0, 0.6)),
        ("CrossLine2nd3rdArrowAtEnds", (0, -0.6, -0.6, 0, 0.6, 0.6)),
        ("SemicircleArrowAtEnds", (0, -0.1, -0.575, 0, 0.5, 0.575)),
        ("Line1stWideArrowAtEnds", (-0.6, -0.075, 0, 0.6, 0.075, 0)),
        ("Line2ndWideArrowAtEnds", (-0.075, -0.6, 0, 0.075, 0.6, 0)),
        ("Line3rdWideArrowAtEnds", (-0.075, 0, -0.6, 0.075, 0, 0.6)),
        ("CrossLine1st2ndWideArrowAtEnds", (-0.6, -0.6, 0, 0.6, 0.6, 0)),
        ("CrossLine1st3rdWideArrowAtEnds", (-0.6, 0, -0.6, 0.6, 0, 0.6)),
        ("CrossLine2nd3rdWideArrowAtEnds", (0, -0.6, -0.6, 0, 0.6, 0.6)),
        ("SemicircleWideArrowAtEnds", (0, -0.1, -0.575, 0, 0.5375, 0.575)),
    ),
)
def test_arrow_and_fin_part_size_bounds(
    maya_cmds, maya_om, new_scene, shape_name, expected, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = shape_name + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    for attribute, value in (
        ("shapePartOffset", 0.1),
        ("shapePartLengthScale", 1.5),
        ("shapePartWidthScale", 0.75),
        ("shapePartSize", 2.0),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 1.0)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.5)
    maya_cmds.setAttr(f"{shape}.shapePartFinHeight", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_NAMES if "CrossLine3AxisEnd" in name]
)
def test_terminal_part_size_multiplies_both_scales(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 2.0)
    extent = 0.6 if "Pyramid" in shape_name or "Cone" in shape_name else 0.8
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, -extent, -extent, extent, extent, extent)
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("fin_name", "body_name", "max_y"),
    (
        ("CubeFin", "Cube", 1.75),
        ("CubeFinArrow", "Cube", 1.75),
        ("CylinderFin", "Cylinder", 1.75),
        ("CylinderFinArrow", "Cylinder", 1.75),
        ("PyramidFin", "Pyramid", 1.25),
        ("ConeFin", "Cone", 1.25),
        ("OctahedronArrowFin", "OctahedronArrow", 1.25),
        ("ArrowFin", "Arrow", 1.25),
    ),
)
def test_fin_height_is_independent_and_zero_keeps_body(
    maya_cmds, maya_om, new_scene, filled, fin_name, body_name, max_y
):
    _load_bd_util_nodes(maya_cmds)
    suffix = "Filled" if filled else ""
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(fin_name + suffix)
    )
    maya_cmds.setAttr(f"{shape}.shapePartFinHeight", 1.25)
    assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)
    for attribute, value in (
        ("shapePartOffset", 0.3),
        ("shapePartLengthScale", 3),
        ("shapePartWidthScale", 1.5),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)
    maya_cmds.setAttr(f"{shape}.shapePartFinHeight", 0)
    actual = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index(body_name + suffix))
    assert actual == pytest.approx(_bounds(maya_om, shape))


@pytest.mark.parametrize("connected", (False, True))
def test_fin_height_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("CubeFinFilled")
    )
    target = f"{shape}.shapePartFinHeight"
    if connected:
        source = maya_cmds.createNode("addDoubleLinear")
        target = f"{source}.input1"
        maya_cmds.setAttr(target, 0.5)
        maya_cmds.connectAttr(
            f"{source}.output", f"{shape}.shapePartFinHeight"
        )
    for height in (0.5, 0.25, 1, 0):
        maya_cmds.setAttr(target, height)
        assert _bounds(maya_om, shape)[4] == pytest.approx(0.5 + height)


def test_fin_height_size_survives_other_scale_cancellation(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("CubeFinFilled")
    )
    maya_cmds.setAttr(f"{shape}.shapePartSize", 2)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 0.5)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 1.5, 0.5)
    )


def test_fin_height_uses_distance_units(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("CubeFinFilled")
    )
    previous = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        assert maya_cmds.getAttr(f"{shape}.shapePartFinHeight") == 5
        maya_cmds.setAttr(f"{shape}.shapePartFinHeight", 10)
        assert _bounds(maya_om, shape)[4] == pytest.approx(1.5)
    finally:
        maya_cmds.currentUnit(linear=previous)


def test_fin_height_animation_updates_bounds(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("CubeFinFilled")
    )
    for time, height in ((1, 0), (10, 1)):
        maya_cmds.setKeyframe(
            shape, attribute="shapePartFinHeight", time=time, value=height
        )
    for time, max_y in ((10, 1.5), (1, 0.5), (10, 1.5)):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)


def test_fin_part_size_animation_and_bounds_modes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("CubeFinFilled")
    )
    maya_cmds.setKeyframe(shape, attribute="shapePartSize", time=1, value=1)
    maya_cmds.setKeyframe(shape, attribute="shapePartSize", time=10, value=2)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1, -0.5, -0.5, 3, 1.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    assert _bounds(maya_om, shape) == pytest.approx((-1, -1, -0.5, 1, 1, 0.5))
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.5, -0.5, -0.5, 2.5, 1, 0.5)
    )


@pytest.mark.parametrize("filled", (False, True))
def test_semicircle_wide_part_retains_outer_arc_when_inner_radius_collapses(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleWideArrowAtEnds" + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 25)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, -0.1, -1.75, 0, 1.125, 1.75)
    )


@pytest.mark.parametrize("filled", (False, True))
def test_wide_end_arrow_negative_offset_moves_heads_past_origin(
    maya_cmds, maya_om, new_scene, filled
):
    import math

    _load_bd_util_nodes(maya_cmds)
    name = "Line1stWideArrowAtEnds" + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", -0.8)
    extent = 0.3 + 0.1 * math.cos(math.pi / 6)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, -0.05, 0, extent, 0.05, 0)
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (-90, -89.9, -60, -30, 0, 30, 60, 89.9, 90))
def test_semicircle_angle_bounds(maya_cmds, maya_om, new_scene, filled, angle):
    _load_bd_util_nodes(maya_cmds)
    name = "Semicircle" + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffsetAngle", angle)
    extent = 0.5 if angle >= 0 else 0.5 * math.cos(math.radians(angle))
    low = -0.5 * math.sin(math.radians(angle))
    if filled and -90 < angle < 0:
        low = 0.0
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, low, -extent, 0, 0.5, extent), abs=1e-9
    )
    # 矢印のない円弧は長さ・太さ・直線方向の移動では変えない。
    for attribute, value in (
        ("shapePartOffset", 0.3),
        ("shapePartSize", 2),
        ("shapePartLengthScale", 3),
        ("shapePartWidthScale", 4),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, low, -extent, 0, 0.5, extent), abs=1e-9
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "base_name",
    (
        "SemicircleArrow2D",
        "SemicircleArrow3D",
        "SemicircleArrowAtEnds",
        "SemicircleWideArrowAtEnds",
    ),
)
@pytest.mark.parametrize("angle", (-90, -30, 30, 90))
def test_semicircle_angle_and_part_scales_remain_finite(
    maya_cmds, maya_om, new_scene, filled, base_name, angle
):
    _load_bd_util_nodes(maya_cmds)
    name = base_name + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    for attribute, value in (
        ("shapePartOffsetAngle", angle),
        ("shapePartOffset", 0.3),
        ("shapePartSize", 0.5),
        ("shapePartLengthScale", 2),
        ("shapePartWidthScale", 3),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert all(math.isfinite(value) and abs(value) < 2 for value in bounds)
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index(base_name))
    outline_bounds = _bounds(maya_om, shape)
    if (
        filled
        and base_name in ("SemicircleArrow2D", "SemicircleArrow3D")
        and -90 < angle < 0
    ):
        assert bounds[1] == pytest.approx(0.0)
        assert outline_bounds[1] > 0.0
        assert bounds[:1] + bounds[2:] == pytest.approx(
            outline_bounds[:1] + outline_bounds[2:]
        )
    else:
        assert outline_bounds == pytest.approx(bounds)


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_semicircle_angle_rotates_endpoint_offset_direction(
    maya_cmds, maya_om, new_scene, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        "Semicircle"
        + ("Wide" if wide else "")
        + "ArrowAtEnds"
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffsetAngle", 30)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.3)
    low = -0.25 - 0.3 * math.cos(math.pi / 6)
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            0,
            low,
            -0.525 if wide else -0.5,
            0,
            0.525 if wide else 0.5,
            0.525 if wide else 0.5,
        )
    )


@pytest.mark.parametrize("connected", (False, True))
def test_semicircle_angle_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("SemicircleFilled")
    )
    target = f"{shape}.shapePartOffsetAngle"
    if connected:
        source = maya_cmds.createNode("bdDblA_Value")
        target = f"{source}.value"
        maya_cmds.connectAttr(target, f"{shape}.shapePartOffsetAngle")
    assert _bounds(maya_om, shape) == pytest.approx((0, 0, -0.5, 0, 0.5, 0.5))
    maya_cmds.setAttr(target, 30)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, -0.25, -0.5, 0, 0.5, 0.5)
    )
    maya_cmds.setAttr(target, -30)
    extent = 0.5 * math.cos(math.pi / 6)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, 0, -extent, 0, 0.5, extent)
    )
    if connected:
        # 接続元の角度に制限がなくても、円弧は0–360度の範囲に収める。
        maya_cmds.setAttr(target, 180)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0, -0.5, -0.5, 0, 0.5, 0.5)
        )


def test_semicircle_angle_uses_scene_angle_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="rad")
        _, shape = _create_controller(
            maya_cmds, shape_value=SHAPE_NAMES.index("Semicircle")
        )
        maya_cmds.setAttr(f"{shape}.shapePartOffsetAngle", math.pi / 6)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0, -0.25, -0.5, 0, 0.5, 0.5)
        )
        maya_cmds.currentUnit(angle="deg")
        assert maya_cmds.getAttr(
            f"{shape}.shapePartOffsetAngle"
        ) == pytest.approx(30)
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


@pytest.mark.parametrize("mode", (0, 1, 2))
@pytest.mark.parametrize(
    ("angle", "shape_bounds", "centered_bounds"),
    (
        (30, (2, -0.25, -0.5, 2, 0.5, 0.5), (0, -0.375, -0.5, 0, 0.375, 0.5)),
        (
            -30,
            (2, 0, -math.sqrt(3) / 4, 2, 0.5, math.sqrt(3) / 4),
            (0, -0.25, -math.sqrt(3) / 4, 0, 0.25, math.sqrt(3) / 4),
        ),
    ),
)
def test_semicircle_angle_animation_and_bounds_modes(
    maya_cmds, maya_om, new_scene, mode, angle, shape_bounds, centered_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index("SemicircleFilled"),
        bounds_mode=mode,
    )
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2)
    maya_cmds.setKeyframe(
        shape, attribute="shapePartOffsetAngle", time=1, value=0
    )
    maya_cmds.setKeyframe(
        shape, attribute="shapePartOffsetAngle", time=10, value=angle
    )
    maya_cmds.currentTime(10)
    expected = (
        shape_bounds,
        centered_bounds,
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected[mode])
    maya_cmds.currentTime(1)
    if mode == 0:
        assert _bounds(maya_om, shape) == pytest.approx(
            (2, 0, -0.5, 2, 0.5, 0.5)
        )


def test_semicircle_angle_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shape.set(SHAPE_NAMES.index("SemicircleFilled"))
    shape.shapePartOffsetAngle.set(30)
    shape.shapeSize.set(2)
    shape.shapeRootSize.set(2)
    shape.shapeTranslate.set(1, 2, 3)
    mod.do_it_dg()
    expected = (2, 3, 4, 2, 6, 8)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(
        (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "semicircle_angle.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert maya_cmds.getAttr(f"{name}.shapePartOffsetAngle") == pytest.approx(
        30
    )
    assert _bounds(maya_om, name) == pytest.approx(expected)


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_NAMES if "Semicircle" not in name]
)
def test_semicircle_angle_leaves_other_shapes_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePartOffsetAngle", 30)
    assert _bounds(maya_om, shape) == pytest.approx(before)


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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("CircleArrow2D"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))  # Cube
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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
        maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("Cube"))
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


@pytest.mark.parametrize(
    ("shape_name", "expected"),
    (
        ("ColorCube", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCubeFilled", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCornerCube", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCornerCubeFilled", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("Line1stWideArrowAtEndsFilled", (2.0, 3.6, 5.0, 2.0, 4.4, 7.0)),
        (
            "CrossLine1st2ndWideArrowAtEndsFilled",
            (2.0, 0.0, 5.0, 2.0, 8.0, 7.0),
        ),
        ("SemicircleWideArrowAtEndsFilled", (-11.2, 4.0, 6.0, 15.2, 8.2, 6.0)),
        ("CrossLine3AxisEndCubeFilled", (-11.2, -0.4, 4.9, 15.2, 8.4, 7.1)),
        (
            "ColorCrossLine3AxisEndSphereFilled",
            (-2.4, -0.4, 2.7, 6.4, 8.4, 9.3),
        ),
        ("CrossLine3AxisEndPyramidFilled", (-10.0, 0.0, 5.0, 14.0, 8.0, 7.0)),
        (
            "ColorCrossLine3AxisEndConeFilled",
            (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0),
        ),
    ),
)
def test_preset_transform_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name, expected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name_in_scene = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name_in_scene)
    shape.shape.set(SHAPE_NAMES.index(shape_name))
    shape.shape1stAxis.set(4)
    shape.shape2ndAxis.set(2)
    shape.shapeSize.set(2.0)
    shape.shapeAxisScale.set(1.0, 2.0, 3.0)
    shape.shapeScale.set(2.0, 1.0, 0.5)
    shape.shapeTranslate.set(1.0, 2.0, 3.0)
    shape.shapeRootSize.set(2.0)
    shape.shapeTransparency.set(0.25)
    shape.shapeFillTransparency.set(0.6)
    mod.do_it_dg()

    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)

    scene_path = tmp_path / f"{shape_name}.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(
        f"{shape_name_in_scene}.shape"
    ) == SHAPE_NAMES.index(shape_name)
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)
    assert maya_cmds.getAttr(
        f"{shape_name_in_scene}.shapeTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(
        f"{shape_name_in_scene}.shapeFillTransparency"
    ) == pytest.approx(0.6)
    assert maya_cmds.getAttr(f"{shape_name_in_scene}.shape1stAxis") == 4


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_NAMES if name.startswith("Color")]
)
@pytest.mark.parametrize("bounds_mode", (0, 1))
def test_color_shapes_ignore_orientation_attributes(
    maya_cmds, maya_om, new_scene, shape_name, bounds_mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index(shape_name),
        bounds_mode=bounds_mode,
    )
    for attribute, value in (
        ("shapeAxisScale", (0.75, 1.25, 2.0)),
        ("shapeScale", (1.5, 0.8, 2.5)),
        ("shapeTranslate", (0.25, -0.5, 0.75)),
        ("shapeAxisTranslate", (0.1, -0.2, 0.3)),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", *value)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 1.6)
    expected = _bounds(maya_om, shape)
    for first, second in ((5, 1), (4, 4)):
        maya_cmds.setAttr(f"{shape}.shape1stAxis", first)
        maya_cmds.setAttr(f"{shape}.shape2ndAxis", second)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == first
        assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == second
    for attribute in ("shapeRotate", "shapeAxisRotate"):
        maya_cmds.setAttr(f"{shape}.{attribute}", 23.0, 41.0, -17.0)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.{attribute}")[0] == (
            23.0,
            41.0,
            -17.0,
        )


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_NAMES if name.startswith("Color")]
)
@pytest.mark.parametrize(
    "attribute", ("shapeScale", "shapeAxisScale", "shapeSize", "shapeRootSize")
)
def test_color_shapes_use_scale_magnitudes(
    maya_cmds, maya_om, new_scene, shape_name, attribute
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 0.25, -0.5, 0.75)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslate", 0.1, -0.2, 0.3)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.showShapeOffsetLine", True)
    vector = attribute in ("shapeScale", "shapeAxisScale")
    positive = (2.0, 3.0, 4.0) if vector else (2.0,)
    negative = (-2.0, 3.0, -4.0) if vector else (-2.0,)
    maya_cmds.setAttr(f"{shape}.{attribute}", *positive)
    expected = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.{attribute}", *negative)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    stored = maya_cmds.getAttr(f"{shape}.{attribute}")
    assert (stored[0] if vector else (stored,)) == negative


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_NAMES if name.startswith("Color")]
)
def test_color_shapes_apply_animation_matrix_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(shape_name)
    )
    before = _bounds(maya_om, shape)
    matrix = (0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0.5, 0, 4, -5, 6, 1)
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix, type="matrix"
    )
    xmin, ymin, zmin, xmax, ymax, zmax = before
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            3 * ymin + 4,
            2 * xmin - 5,
            0.5 * zmin + 6,
            3 * ymax + 4,
            2 * xmax - 5,
            0.5 * zmax + 6,
        )
    )
    assert (
        tuple(maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix"))
        == matrix
    )


def test_color_matrix_connection_keeps_rotation_shear_and_reflection(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("ColorCornerCubeFilled")
    )
    source = maya_cmds.createNode("composeMatrix")
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setAttr(f"{source}.inputScale", -2.0, 3.0, 0.5)
    maya_cmds.setAttr(f"{source}.inputShear", 0.25, -0.4, 0.15)
    maya_cmds.setAttr(f"{source}.inputTranslate", 1.0, 2.0, -3.0)
    maya_cmds.setAttr(f"{shape}.shapeRotate", 17.0, 29.0, 43.0)
    for angle in (31.0, -57.0):
        maya_cmds.setAttr(f"{source}.inputRotate", 13.0, 27.0, angle)
        values = maya_cmds.getAttr(f"{source}.outputMatrix")
        matrix = maya_om.MMatrix(values)
        points = [
            maya_om.MPoint(x, y, z) * matrix
            for x in (-0.5, 0.5)
            for y in (-0.5, 0.5)
            for z in (-0.5, 0.5)
        ]
        expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
            max(p[i] for p in points) for i in range(3)
        )
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert (
            maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix")
            == values
        )
    maya_cmds.setAttr(f"{transform}.rotate", 23.0, 37.0, 51.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{transform}.rotate")[0] == (23.0, 37.0, 51.0)


def test_color_orientation_connections_survive_shape_switch_and_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index("ColorSphereArrow3DFilled")
    )
    driver = maya_cmds.createNode("transform", name="orientationDriver")
    maya_cmds.connectAttr(f"{driver}.rotate", f"{shape}.shapeRotate")
    maya_cmds.connectAttr(f"{driver}.scale", f"{shape}.shapeAxisScale")
    maya_cmds.setAttr(f"{driver}.scale", 2.0, 3.0, 4.0)
    expected = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{driver}.scale", -2.0, 3.0, -4.0)
    maya_cmds.setKeyframe(driver, attribute="rotateZ", time=1, value=0)
    maya_cmds.setKeyframe(driver, attribute="rotateZ", time=10, value=37)
    for time in (1, 10):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
    maya_cmds.setAttr(
        f"{shape}.shape", SHAPE_NAMES.index("SphereArrow3DFilled")
    )
    normal = _bounds(maya_om, shape)
    assert normal != pytest.approx(expected)
    maya_cmds.setAttr(
        f"{shape}.shape", SHAPE_NAMES.index("ColorSphereArrow3DFilled")
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    scene_path = tmp_path / "color_orientation.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.isConnected(f"{driver}.rotate", f"{shape}.shapeRotate")
    assert maya_cmds.isConnected(f"{driver}.scale", f"{shape}.shapeAxisScale")
    assert maya_cmds.getAttr(f"{shape}.shapeRotateZ") == pytest.approx(37)
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScale")[0] == (-2.0, 3.0, -4.0)
    maya_cmds.setAttr(
        f"{shape}.shape", SHAPE_NAMES.index("SphereArrow3DFilled")
    )
    assert _bounds(maya_om, shape) == pytest.approx(normal)


def test_color_shape_keeps_custom_bounds_transform_independent(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_value=SHAPE_NAMES.index("ColorCornerCubeFilled"),
        bounds_mode=2,
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisScale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslate", 1.0, 2.0, 3.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRootSize", -1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-2.5, -3, -5, 0.5, -1, -1)
    )


def test_scene_round_trip_preserves_circle_arrow(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds, name="savedController")
    maya_cmds.setAttr(f"{shape}.shape", SHAPE_NAMES.index("CircleArrow2D"))
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
    assert maya_cmds.getAttr(f"{shape}.shape") == SHAPE_NAMES.index(
        "CircleArrow2D"
    )
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
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.controllerShape(name="rig_ctrl")
    shape.boundsMode.set(0)
    shape.shape.set(SHAPE_NAMES.index("CircleArrow2D"))
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
    assert maya_cmds.getAttr(f"{shape.full_path}.shape") == SHAPE_NAMES.index(
        "CircleArrow2D"
    )
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


@pytest.mark.parametrize(
    "base,axis,side", (("Line1st", 0, 1), ("Line2nd", 1, 0), ("Line3rd", 2, 0))
)
@pytest.mark.parametrize("end,sign", (("Start", -1), ("End", 1)))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size",
    (
        (0, 1, 1, 1),
        (0.2, 1.5, 2, 1),
        (-0.2, 0.5, 1, 2),
        (0.1, -2, -3, 1),
        (-1.2, 1, 1, 1),
        (0.1, 0, 0, 1),
        (0.1, 1, 1, 0),
    ),
)
def test_single_end_line_arrow_keeps_opposite_endpoint(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    axis,
    side,
    end,
    sign,
    wide,
    filled,
    offset,
    length,
    width,
    size,
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        base
        + ("Wide" if wide else "")
        + "ArrowAt"
        + end
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    tip = sign * (0.5 + offset)
    shoulder = sign * (
        0.5 + offset - 0.1 * math.cos(math.pi / 6) * length * size
    )
    low, high = [0.0] * 3, [0.0] * 3
    low[axis], high[axis] = min(-sign * 0.5, tip, shoulder), max(
        -sign * 0.5, tip, shoulder
    )
    low[side], high[side] = -0.05 * abs(width * size), 0.05 * abs(width * size)
    assert _bounds(maya_om, shape) == pytest.approx((*low, *high), abs=1e-9)


@pytest.mark.parametrize("end", ("Start", "End"))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (-90, -30, 0, 30, 90))
@pytest.mark.parametrize("offset", (0, 0.2))
def test_single_end_semicircle_arrow_follows_endpoint_and_tangent(
    maya_cmds, maya_om, new_scene, end, filled, angle, offset
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleArrowAt" + end + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffsetAngle", angle)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    start, finish = -math.radians(angle), math.pi + math.radians(angle)
    arc_angles = [start, finish] + [
        a
        for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2)
        if start <= a <= finish
    ]
    points = [(0, 0.5 * math.sin(a), 0.5 * math.cos(a)) for a in arc_angles]
    a = start if end == "Start" else finish
    radial_y, radial_z = math.sin(a), math.cos(a)
    direction_y, direction_z = (
        (-radial_z, radial_y) if end == "Start" else (radial_z, -radial_y)
    )
    tip_y, tip_z = (
        0.5 * radial_y + offset * direction_y,
        0.5 * radial_z + offset * direction_z,
    )
    points.append((0, tip_y, tip_z))
    depth = 0.1 * math.cos(math.pi / 6)
    for sign in (-1, 1):
        points.append(
            (
                0,
                tip_y - depth * direction_y + sign * 0.05 * radial_y,
                tip_z - depth * direction_z + sign * 0.05 * radial_z,
            )
        )
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("end", ("Start", "End"))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("offset", (0, 0.2))
def test_single_end_wide_semicircle_keeps_flat_cap(
    maya_cmds, maya_om, new_scene, end, filled, offset
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleWideArrowAt" + end + ("Filled" if filled else "")
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    low_z, high_z = (-0.525, 0.55) if end == "Start" else (-0.55, 0.525)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, -offset, low_z, 0, 0.525, high_z), abs=1e-9
    )


@pytest.mark.parametrize(
    "base,axes",
    (
        ("CrossLine1st2nd", (0, 1)),
        ("CrossLine1st3rd", (0, 2)),
        ("CrossLine2nd3rd", (1, 2)),
    ),
)
@pytest.mark.parametrize("endpoint", range(4))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size",
    (
        (0, 1, 1, 1),
        (0.2, 1.5, 2, 1),
        (-0.2, 0.5, 1, 2),
        (0.1, -2, -3, 1),
        (-1.2, 1, 1, 1),
        (0.1, 3, 22, 1),
        (0.1, 0, 1, 1),
        (0.1, 1, 0, 1),
        (0.1, 1, 1, 0),
    ),
)
def test_single_cross_arrow_bounds_follow_only_selected_endpoint(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    axes,
    endpoint,
    wide,
    filled,
    offset,
    length,
    width,
    size,
):
    _load_bd_util_nodes(maya_cmds)
    axis = axes[endpoint // 2]
    side = next(value for value in axes if value != axis)
    start = endpoint % 2 == 0
    sign = -1 if start else 1
    label = ("1st", "2nd", "3rd")[axis]
    name = (
        base
        + ("Wide" if wide else "")
        + "ArrowAt"
        + label
        + ("Start" if start else "End")
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(
        maya_cmds, shape_value=SHAPE_NAMES.index(name)
    )
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    tip = sign * (0.5 + offset)
    shoulder = tip - sign * 0.1 * math.cos(math.pi / 6) * length * size
    points = []
    for body_axis in axes:
        body_side = next(value for value in axes if value != body_axis)
        for body_sign in (-1, 1):
            along = body_sign * 0.5
            if body_axis == axis and body_sign == sign:
                along = shoulder if wide else tip
            for transverse_sign in (-1, 1):
                point = [0.0, 0.0, 0.0]
                point[body_axis] = along
                point[body_side] = (
                    transverse_sign * 0.025 * abs(width * size) if wide else 0
                )
                points.append(point)
    points.append([tip if i == axis else 0 for i in range(3)])
    for transverse_sign in (-1, 1):
        point = [0.0, 0.0, 0.0]
        point[axis] = shoulder
        point[side] = transverse_sign * 0.05 * abs(width * size)
        points.append(point)
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    extent = [(expected[i + 3] - expected[i]) * 0.5 for i in range(3)]
    assert _bounds(maya_om, shape) == pytest.approx(
        tuple(-value for value in extent) + tuple(extent), abs=1e-9
    )


@pytest.mark.parametrize(
    "shape_name",
    (
        "CrossLine1st2ndArrowAt1stEndFilled",
        "CrossLine1st3rdWideArrowAt3rdStartFilled",
        "CrossLine2nd3rdWideArrowAt2ndEndFilled",
    ),
)
def test_single_cross_arrow_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shape.set(getattr(ShapeEnumPlugOperator, shape_name.upper()))
    shape.shapePartOffset.set(0.2)
    shape.shapePartLengthScale.set(2)
    shape.shapePartWidthScale.set(1.5)
    shape.shape1stAxis.set(4)
    shape.shape2ndAxis.set(0)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    mod.undo_it()
    assert _bounds(maya_om, name) != pytest.approx(expected)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "single_cross_arrow.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shape") == SHAPE_NAMES.index(shape_name)


def test_single_end_shape_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEWIDEARROWATENDFILLED)
    shape.shapePartOffset.set(0.2)
    shape.shapePartOffsetAngle.set(30)
    shape.shapePartLengthScale.set(2)
    shape.shapePartWidthScale.set(1.5)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    mod.undo_it()
    assert _bounds(maya_om, name) != pytest.approx(expected)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "single_end_arrow.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shape") == SHAPE_NAMES.index(
        "SemicircleWideArrowAtEndFilled"
    )


def test_custom_bounds_node_operator_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds, bounds_mode=None)
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
    assert maya_cmds.getAttr(f"{shape_name}.boundsMode") == 1
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
