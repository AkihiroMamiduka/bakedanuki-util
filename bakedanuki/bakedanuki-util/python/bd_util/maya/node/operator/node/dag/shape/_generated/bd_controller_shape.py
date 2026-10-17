# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.bd_controller_shape import (
    CompInstObjGroupsField,
    ComponentTagsField,
    CustomBoundsAxisRotateField,
    CustomBoundsAxisScaleField,
    CustomBoundsAxisTranslateField,
    CustomBoundsRotateField,
    CustomBoundsScaleField,
    CustomBoundsTranslateField,
    LocalPositionField,
    LocalScaleField,
    ShapeAxisRotateField,
    ShapeAxisScaleField,
    ShapeAxisTranslateField,
    ShapeRotateField,
    ShapeScaleField,
    ShapeTranslateField,
    WorldPositionField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from .....attr.define.std.dt.matrix import DataMatrixField


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    GEAR = 0
    GEARFILLED = 1
    LINE1ST = 2
    LINE1STENDARROW = 3
    LINE1STENDARROWFILLED = 4
    LINE1STWIDEENDARROW = 5
    LINE1STWIDEENDARROWFILLED = 6
    LINE2ND = 7
    LINE2NDENDARROW = 8
    LINE2NDENDARROWFILLED = 9
    LINE2NDWIDEENDARROW = 10
    LINE2NDWIDEENDARROWFILLED = 11
    LINE3RD = 12
    LINE3RDENDARROW = 13
    LINE3RDENDARROWFILLED = 14
    LINE3RDWIDEENDARROW = 15
    LINE3RDWIDEENDARROWFILLED = 16
    CROSSLINE1ST2ND = 17
    CROSSLINE1ST2NDENDARROW = 18
    CROSSLINE1ST2NDENDARROWFILLED = 19
    CROSSLINE1ST2NDWIDEENDARROW = 20
    CROSSLINE1ST2NDWIDEENDARROWFILLED = 21
    CROSSLINE1ST3RD = 22
    CROSSLINE1ST3RDENDARROW = 23
    CROSSLINE1ST3RDENDARROWFILLED = 24
    CROSSLINE1ST3RDWIDEENDARROW = 25
    CROSSLINE1ST3RDWIDEENDARROWFILLED = 26
    CROSSLINE2ND3RD = 27
    CROSSLINE2ND3RDENDARROW = 28
    CROSSLINE2ND3RDENDARROWFILLED = 29
    CROSSLINE2ND3RDWIDEENDARROW = 30
    CROSSLINE2ND3RDWIDEENDARROWFILLED = 31
    CROSSLINE3AXIS = 32
    TRIANGLE = 33
    TRIANGLEFILLED = 34
    TRIANGLEARROW3D = 35
    TRIANGLEARROW3DFILLED = 36
    SQUARE = 37
    SQUAREFILLED = 38
    SQUAREARROW2D = 39
    SQUAREARROW2DFILLED = 40
    SQUAREARROW3D = 41
    SQUAREARROW3DFILLED = 42
    SQUAREARROWCROSSLINE2D = 43
    SQUAREARROWCROSSLINE2DFILLED = 44
    SQUAREARROWCROSSLINE3D = 45
    SQUAREARROWCROSSLINE3DFILLED = 46
    SQUAREARROWCROSSLINETEMPLATE2D = 47
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 48
    SQUAREARROWCROSSLINETEMPLATE3D = 49
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 50
    SQUAREARROW4WAY2D = 51
    SQUAREARROW4WAY2DFILLED = 52
    SQUAREARROW4WAY3D = 53
    SQUAREARROW4WAY3DFILLED = 54
    SQUARETEMPLATEARROW4WAY2D = 55
    SQUARETEMPLATEARROW4WAY2DFILLED = 56
    SQUARETEMPLATEARROW4WAY3D = 57
    SQUARETEMPLATEARROW4WAY3DFILLED = 58
    CUBE = 59
    CUBEFILLED = 60
    CUBEARROW2D = 61
    CUBEARROW2DFILLED = 62
    CUBEARROW3D = 63
    CUBEARROW3DFILLED = 64
    CUBEFIN = 65
    CUBEFINFILLED = 66
    CUBEFINARROW = 67
    CUBEFINARROWFILLED = 68
    OCTAHEDRON = 69
    OCTAHEDRONFILLED = 70
    OCTAHEDRONARROW = 71
    OCTAHEDRONARROWFILLED = 72
    OCTAHEDRONARROWFIN = 73
    OCTAHEDRONARROWFINFILLED = 74
    CIRCLE = 75
    CIRCLEFILLED = 76
    CIRCLEARROW2D = 77
    CIRCLEARROW2DFILLED = 78
    CIRCLEARROW3D = 79
    CIRCLEARROW3DFILLED = 80
    SEMICIRCLE = 81
    SEMICIRCLEFILLED = 82
    SEMICIRCLEENDARROW = 83
    SEMICIRCLEENDARROWFILLED = 84
    SEMICIRCLEWIDEENDARROW = 85
    SEMICIRCLEWIDEENDARROWFILLED = 86
    SEMICIRCLEARROW2D = 87
    SEMICIRCLEARROW2DFILLED = 88
    SEMICIRCLEARROW3D = 89
    SEMICIRCLEARROW3DFILLED = 90
    SPHERE = 91
    SPHEREFILLED = 92
    SPHEREARROW2D = 93
    SPHEREARROW2DFILLED = 94
    SPHEREARROW3D = 95
    SPHEREARROW3DFILLED = 96
    CYLINDER = 97
    CYLINDERFILLED = 98
    CYLINDERFIN = 99
    CYLINDERFINFILLED = 100
    CYLINDERFINARROW = 101
    CYLINDERFINARROWFILLED = 102
    ARROW = 103
    ARROWFILLED = 104
    ARROWFIN = 105
    ARROWFINFILLED = 106
    PYRAMID = 107
    PYRAMIDFILLED = 108
    PYRAMIDFIN = 109
    PYRAMIDFINFILLED = 110
    CONE = 111
    CONEFILLED = 112
    CONEFIN = 113
    CONEFINFILLED = 114
    COLORCROSSLINE3AXIS = 115
    COLORCUBE = 116
    COLORCUBEFILLED = 117
    COLORCORNERCUBE = 118
    COLORCORNERCUBEFILLED = 119
    COLORSPHERE = 120
    COLORSPHEREFILLED = 121
    COLORSPHEREARROW2D = 122
    COLORSPHEREARROW2DFILLED = 123
    COLORSPHEREARROW3D = 124
    COLORSPHEREARROW3DFILLED = 125
    COLORSPHERECROSSLINE = 126
    COLORSPHERECROSSLINEFILLED = 127


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    GEARFILLED = 1
    LINE1ST = 2
    LINE1STENDARROW = 3
    LINE1STENDARROWFILLED = 4
    LINE1STWIDEENDARROW = 5
    LINE1STWIDEENDARROWFILLED = 6
    LINE2ND = 7
    LINE2NDENDARROW = 8
    LINE2NDENDARROWFILLED = 9
    LINE2NDWIDEENDARROW = 10
    LINE2NDWIDEENDARROWFILLED = 11
    LINE3RD = 12
    LINE3RDENDARROW = 13
    LINE3RDENDARROWFILLED = 14
    LINE3RDWIDEENDARROW = 15
    LINE3RDWIDEENDARROWFILLED = 16
    CROSSLINE1ST2ND = 17
    CROSSLINE1ST2NDENDARROW = 18
    CROSSLINE1ST2NDENDARROWFILLED = 19
    CROSSLINE1ST2NDWIDEENDARROW = 20
    CROSSLINE1ST2NDWIDEENDARROWFILLED = 21
    CROSSLINE1ST3RD = 22
    CROSSLINE1ST3RDENDARROW = 23
    CROSSLINE1ST3RDENDARROWFILLED = 24
    CROSSLINE1ST3RDWIDEENDARROW = 25
    CROSSLINE1ST3RDWIDEENDARROWFILLED = 26
    CROSSLINE2ND3RD = 27
    CROSSLINE2ND3RDENDARROW = 28
    CROSSLINE2ND3RDENDARROWFILLED = 29
    CROSSLINE2ND3RDWIDEENDARROW = 30
    CROSSLINE2ND3RDWIDEENDARROWFILLED = 31
    CROSSLINE3AXIS = 32
    TRIANGLE = 33
    TRIANGLEFILLED = 34
    TRIANGLEARROW3D = 35
    TRIANGLEARROW3DFILLED = 36
    SQUARE = 37
    SQUAREFILLED = 38
    SQUAREARROW2D = 39
    SQUAREARROW2DFILLED = 40
    SQUAREARROW3D = 41
    SQUAREARROW3DFILLED = 42
    SQUAREARROWCROSSLINE2D = 43
    SQUAREARROWCROSSLINE2DFILLED = 44
    SQUAREARROWCROSSLINE3D = 45
    SQUAREARROWCROSSLINE3DFILLED = 46
    SQUAREARROWCROSSLINETEMPLATE2D = 47
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 48
    SQUAREARROWCROSSLINETEMPLATE3D = 49
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 50
    SQUAREARROW4WAY2D = 51
    SQUAREARROW4WAY2DFILLED = 52
    SQUAREARROW4WAY3D = 53
    SQUAREARROW4WAY3DFILLED = 54
    SQUARETEMPLATEARROW4WAY2D = 55
    SQUARETEMPLATEARROW4WAY2DFILLED = 56
    SQUARETEMPLATEARROW4WAY3D = 57
    SQUARETEMPLATEARROW4WAY3DFILLED = 58
    CUBE = 59
    CUBEFILLED = 60
    CUBEARROW2D = 61
    CUBEARROW2DFILLED = 62
    CUBEARROW3D = 63
    CUBEARROW3DFILLED = 64
    CUBEFIN = 65
    CUBEFINFILLED = 66
    CUBEFINARROW = 67
    CUBEFINARROWFILLED = 68
    OCTAHEDRON = 69
    OCTAHEDRONFILLED = 70
    OCTAHEDRONARROW = 71
    OCTAHEDRONARROWFILLED = 72
    OCTAHEDRONARROWFIN = 73
    OCTAHEDRONARROWFINFILLED = 74
    CIRCLE = 75
    CIRCLEFILLED = 76
    CIRCLEARROW2D = 77
    CIRCLEARROW2DFILLED = 78
    CIRCLEARROW3D = 79
    CIRCLEARROW3DFILLED = 80
    SEMICIRCLE = 81
    SEMICIRCLEFILLED = 82
    SEMICIRCLEENDARROW = 83
    SEMICIRCLEENDARROWFILLED = 84
    SEMICIRCLEWIDEENDARROW = 85
    SEMICIRCLEWIDEENDARROWFILLED = 86
    SEMICIRCLEARROW2D = 87
    SEMICIRCLEARROW2DFILLED = 88
    SEMICIRCLEARROW3D = 89
    SEMICIRCLEARROW3DFILLED = 90
    SPHERE = 91
    SPHEREFILLED = 92
    SPHEREARROW2D = 93
    SPHEREARROW2DFILLED = 94
    SPHEREARROW3D = 95
    SPHEREARROW3DFILLED = 96
    CYLINDER = 97
    CYLINDERFILLED = 98
    CYLINDERFIN = 99
    CYLINDERFINFILLED = 100
    CYLINDERFINARROW = 101
    CYLINDERFINARROWFILLED = 102
    ARROW = 103
    ARROWFILLED = 104
    ARROWFIN = 105
    ARROWFINFILLED = 106
    PYRAMID = 107
    PYRAMIDFILLED = 108
    PYRAMIDFIN = 109
    PYRAMIDFINFILLED = 110
    CONE = 111
    CONEFILLED = 112
    CONEFIN = 113
    CONEFINFILLED = 114
    COLORCROSSLINE3AXIS = 115
    COLORCUBE = 116
    COLORCUBEFILLED = 117
    COLORCORNERCUBE = 118
    COLORCORNERCUBEFILLED = 119
    COLORSPHERE = 120
    COLORSPHEREFILLED = 121
    COLORSPHEREARROW2D = 122
    COLORSPHEREARROW2DFILLED = 123
    COLORSPHEREARROW3D = 124
    COLORSPHEREARROW3DFILLED = 125
    COLORSPHERECROSSLINE = 126
    COLORSPHERECROSSLINEFILLED = 127

    NAME_MAP = {
        GEAR: "Gear",
        GEARFILLED: "GearFilled",
        LINE1ST: "Line1st",
        LINE1STENDARROW: "Line1stEndArrow",
        LINE1STENDARROWFILLED: "Line1stEndArrowFilled",
        LINE1STWIDEENDARROW: "Line1stWideEndArrow",
        LINE1STWIDEENDARROWFILLED: "Line1stWideEndArrowFilled",
        LINE2ND: "Line2nd",
        LINE2NDENDARROW: "Line2ndEndArrow",
        LINE2NDENDARROWFILLED: "Line2ndEndArrowFilled",
        LINE2NDWIDEENDARROW: "Line2ndWideEndArrow",
        LINE2NDWIDEENDARROWFILLED: "Line2ndWideEndArrowFilled",
        LINE3RD: "Line3rd",
        LINE3RDENDARROW: "Line3rdEndArrow",
        LINE3RDENDARROWFILLED: "Line3rdEndArrowFilled",
        LINE3RDWIDEENDARROW: "Line3rdWideEndArrow",
        LINE3RDWIDEENDARROWFILLED: "Line3rdWideEndArrowFilled",
        CROSSLINE1ST2ND: "CrossLine1st2nd",
        CROSSLINE1ST2NDENDARROW: "CrossLine1st2ndEndArrow",
        CROSSLINE1ST2NDENDARROWFILLED: "CrossLine1st2ndEndArrowFilled",
        CROSSLINE1ST2NDWIDEENDARROW: "CrossLine1st2ndWideEndArrow",
        CROSSLINE1ST2NDWIDEENDARROWFILLED: "CrossLine1st2ndWideEndArrowFilled",
        CROSSLINE1ST3RD: "CrossLine1st3rd",
        CROSSLINE1ST3RDENDARROW: "CrossLine1st3rdEndArrow",
        CROSSLINE1ST3RDENDARROWFILLED: "CrossLine1st3rdEndArrowFilled",
        CROSSLINE1ST3RDWIDEENDARROW: "CrossLine1st3rdWideEndArrow",
        CROSSLINE1ST3RDWIDEENDARROWFILLED: "CrossLine1st3rdWideEndArrowFilled",
        CROSSLINE2ND3RD: "CrossLine2nd3rd",
        CROSSLINE2ND3RDENDARROW: "CrossLine2nd3rdEndArrow",
        CROSSLINE2ND3RDENDARROWFILLED: "CrossLine2nd3rdEndArrowFilled",
        CROSSLINE2ND3RDWIDEENDARROW: "CrossLine2nd3rdWideEndArrow",
        CROSSLINE2ND3RDWIDEENDARROWFILLED: "CrossLine2nd3rdWideEndArrowFilled",
        CROSSLINE3AXIS: "CrossLine3Axis",
        TRIANGLE: "Triangle",
        TRIANGLEFILLED: "TriangleFilled",
        TRIANGLEARROW3D: "TriangleArrow3D",
        TRIANGLEARROW3DFILLED: "TriangleArrow3DFilled",
        SQUARE: "Square",
        SQUAREFILLED: "SquareFilled",
        SQUAREARROW2D: "SquareArrow2D",
        SQUAREARROW2DFILLED: "SquareArrow2DFilled",
        SQUAREARROW3D: "SquareArrow3D",
        SQUAREARROW3DFILLED: "SquareArrow3DFilled",
        SQUAREARROWCROSSLINE2D: "SquareArrowCrossLine2D",
        SQUAREARROWCROSSLINE2DFILLED: "SquareArrowCrossLine2DFilled",
        SQUAREARROWCROSSLINE3D: "SquareArrowCrossLine3D",
        SQUAREARROWCROSSLINE3DFILLED: "SquareArrowCrossLine3DFilled",
        SQUAREARROWCROSSLINETEMPLATE2D: "SquareArrowCrossLineTemplate2D",
        SQUAREARROWCROSSLINETEMPLATE2DFILLED: (
            "SquareArrowCrossLineTemplate2DFilled"
        ),
        SQUAREARROWCROSSLINETEMPLATE3D: "SquareArrowCrossLineTemplate3D",
        SQUAREARROWCROSSLINETEMPLATE3DFILLED: (
            "SquareArrowCrossLineTemplate3DFilled"
        ),
        SQUAREARROW4WAY2D: "SquareArrow4Way2D",
        SQUAREARROW4WAY2DFILLED: "SquareArrow4Way2DFilled",
        SQUAREARROW4WAY3D: "SquareArrow4Way3D",
        SQUAREARROW4WAY3DFILLED: "SquareArrow4Way3DFilled",
        SQUARETEMPLATEARROW4WAY2D: "SquareTemplateArrow4Way2D",
        SQUARETEMPLATEARROW4WAY2DFILLED: "SquareTemplateArrow4Way2DFilled",
        SQUARETEMPLATEARROW4WAY3D: "SquareTemplateArrow4Way3D",
        SQUARETEMPLATEARROW4WAY3DFILLED: "SquareTemplateArrow4Way3DFilled",
        CUBE: "Cube",
        CUBEFILLED: "CubeFilled",
        CUBEARROW2D: "CubeArrow2D",
        CUBEARROW2DFILLED: "CubeArrow2DFilled",
        CUBEARROW3D: "CubeArrow3D",
        CUBEARROW3DFILLED: "CubeArrow3DFilled",
        CUBEFIN: "CubeFin",
        CUBEFINFILLED: "CubeFinFilled",
        CUBEFINARROW: "CubeFinArrow",
        CUBEFINARROWFILLED: "CubeFinArrowFilled",
        OCTAHEDRON: "Octahedron",
        OCTAHEDRONFILLED: "OctahedronFilled",
        OCTAHEDRONARROW: "OctahedronArrow",
        OCTAHEDRONARROWFILLED: "OctahedronArrowFilled",
        OCTAHEDRONARROWFIN: "OctahedronArrowFin",
        OCTAHEDRONARROWFINFILLED: "OctahedronArrowFinFilled",
        CIRCLE: "Circle",
        CIRCLEFILLED: "CircleFilled",
        CIRCLEARROW2D: "CircleArrow2D",
        CIRCLEARROW2DFILLED: "CircleArrow2DFilled",
        CIRCLEARROW3D: "CircleArrow3D",
        CIRCLEARROW3DFILLED: "CircleArrow3DFilled",
        SEMICIRCLE: "Semicircle",
        SEMICIRCLEFILLED: "SemicircleFilled",
        SEMICIRCLEENDARROW: "SemicircleEndArrow",
        SEMICIRCLEENDARROWFILLED: "SemicircleEndArrowFilled",
        SEMICIRCLEWIDEENDARROW: "SemicircleWideEndArrow",
        SEMICIRCLEWIDEENDARROWFILLED: "SemicircleWideEndArrowFilled",
        SEMICIRCLEARROW2D: "SemicircleArrow2D",
        SEMICIRCLEARROW2DFILLED: "SemicircleArrow2DFilled",
        SEMICIRCLEARROW3D: "SemicircleArrow3D",
        SEMICIRCLEARROW3DFILLED: "SemicircleArrow3DFilled",
        SPHERE: "Sphere",
        SPHEREFILLED: "SphereFilled",
        SPHEREARROW2D: "SphereArrow2D",
        SPHEREARROW2DFILLED: "SphereArrow2DFilled",
        SPHEREARROW3D: "SphereArrow3D",
        SPHEREARROW3DFILLED: "SphereArrow3DFilled",
        CYLINDER: "Cylinder",
        CYLINDERFILLED: "CylinderFilled",
        CYLINDERFIN: "CylinderFin",
        CYLINDERFINFILLED: "CylinderFinFilled",
        CYLINDERFINARROW: "CylinderFinArrow",
        CYLINDERFINARROWFILLED: "CylinderFinArrowFilled",
        ARROW: "Arrow",
        ARROWFILLED: "ArrowFilled",
        ARROWFIN: "ArrowFin",
        ARROWFINFILLED: "ArrowFinFilled",
        PYRAMID: "Pyramid",
        PYRAMIDFILLED: "PyramidFilled",
        PYRAMIDFIN: "PyramidFin",
        PYRAMIDFINFILLED: "PyramidFinFilled",
        CONE: "Cone",
        CONEFILLED: "ConeFilled",
        CONEFIN: "ConeFin",
        CONEFINFILLED: "ConeFinFilled",
        COLORCROSSLINE3AXIS: "ColorCrossLine3Axis",
        COLORCUBE: "ColorCube",
        COLORCUBEFILLED: "ColorCubeFilled",
        COLORCORNERCUBE: "ColorCornerCube",
        COLORCORNERCUBEFILLED: "ColorCornerCubeFilled",
        COLORSPHERE: "ColorSphere",
        COLORSPHEREFILLED: "ColorSphereFilled",
        COLORSPHEREARROW2D: "ColorSphereArrow2D",
        COLORSPHEREARROW2DFILLED: "ColorSphereArrow2DFilled",
        COLORSPHEREARROW3D: "ColorSphereArrow3D",
        COLORSPHEREARROW3DFILLED: "ColorSphereArrow3DFilled",
        COLORSPHERECROSSLINE: "ColorSphereCrossLine",
        COLORSPHERECROSSLINEFILLED: "ColorSphereCrossLineFilled",
    }


class ShapeEnumField(EnumField[ShapeEnumAttrOperator, ShapeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShapeEnumAttrOperator
    PLUG_CLS = ShapeEnumPlugOperator


class Shape1stAxisEnumPlugOperator(
    EnumPlugOperator["Shape1stAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class Shape1stAxisEnumAttrOperator(
    EnumAttrOperator[Shape1stAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class Shape1stAxisEnumField(
    EnumField[Shape1stAxisEnumAttrOperator, Shape1stAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shape1stAxisEnumAttrOperator
    PLUG_CLS = Shape1stAxisEnumPlugOperator


class Shape2ndAxisEnumPlugOperator(
    EnumPlugOperator["Shape2ndAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class Shape2ndAxisEnumAttrOperator(
    EnumAttrOperator[Shape2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class Shape2ndAxisEnumField(
    EnumField[Shape2ndAxisEnumAttrOperator, Shape2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Shape2ndAxisEnumAttrOperator
    PLUG_CLS = Shape2ndAxisEnumPlugOperator


class ShapeAxisOffsetDirectionEnumPlugOperator(
    EnumPlugOperator["ShapeAxisOffsetDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5


class ShapeAxisOffsetDirectionEnumAttrOperator(
    EnumAttrOperator[ShapeAxisOffsetDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5

    NAME_MAP = {
        PLUS_1STAXIS: "+1stAxis",
        MINUS_1STAXIS: "-1stAxis",
        PLUS_2NDAXIS: "+2ndAxis",
        MINUS_2NDAXIS: "-2ndAxis",
        PLUS_3RDAXIS: "+3rdAxis",
        MINUS_3RDAXIS: "-3rdAxis",
    }


class ShapeAxisOffsetDirectionEnumField(
    EnumField[
        ShapeAxisOffsetDirectionEnumAttrOperator,
        ShapeAxisOffsetDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ShapeAxisOffsetDirectionEnumAttrOperator
    PLUG_CLS = ShapeAxisOffsetDirectionEnumPlugOperator


class BoundsModeEnumPlugOperator(
    EnumPlugOperator["BoundsModeEnumAttrOperator"]
):
    __slots__ = ()

    SHAPE = 0
    SHAPECENTERED = 1
    CUSTOM = 2


class BoundsModeEnumAttrOperator(EnumAttrOperator[BoundsModeEnumPlugOperator]):
    __slots__ = ()

    SHAPE = 0
    SHAPECENTERED = 1
    CUSTOM = 2

    NAME_MAP = {
        SHAPE: "Shape",
        SHAPECENTERED: "ShapeCentered",
        CUSTOM: "Custom",
    }


class BoundsModeEnumField(
    EnumField[BoundsModeEnumAttrOperator, BoundsModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundsModeEnumAttrOperator
    PLUG_CLS = BoundsModeEnumPlugOperator


class CustomBounds1stAxisEnumPlugOperator(
    EnumPlugOperator["CustomBounds1stAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class CustomBounds1stAxisEnumAttrOperator(
    EnumAttrOperator[CustomBounds1stAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class CustomBounds1stAxisEnumField(
    EnumField[
        CustomBounds1stAxisEnumAttrOperator,
        CustomBounds1stAxisEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBounds1stAxisEnumAttrOperator
    PLUG_CLS = CustomBounds1stAxisEnumPlugOperator


class CustomBounds2ndAxisEnumPlugOperator(
    EnumPlugOperator["CustomBounds2ndAxisEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5


class CustomBounds2ndAxisEnumAttrOperator(
    EnumAttrOperator[CustomBounds2ndAxisEnumPlugOperator]
):
    __slots__ = ()

    PLUS_X = 0
    MINUS_X = 1
    PLUS_Y = 2
    MINUS_Y = 3
    PLUS_Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        PLUS_X: "+X",
        MINUS_X: "-X",
        PLUS_Y: "+Y",
        MINUS_Y: "-Y",
        PLUS_Z: "+Z",
        MINUS_Z: "-Z",
    }


class CustomBounds2ndAxisEnumField(
    EnumField[
        CustomBounds2ndAxisEnumAttrOperator,
        CustomBounds2ndAxisEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBounds2ndAxisEnumAttrOperator
    PLUG_CLS = CustomBounds2ndAxisEnumPlugOperator


class CustomBoundsAxisOffsetDirectionEnumPlugOperator(
    EnumPlugOperator["CustomBoundsAxisOffsetDirectionEnumAttrOperator"]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5


class CustomBoundsAxisOffsetDirectionEnumAttrOperator(
    EnumAttrOperator[CustomBoundsAxisOffsetDirectionEnumPlugOperator]
):
    __slots__ = ()

    PLUS_1STAXIS = 0
    MINUS_1STAXIS = 1
    PLUS_2NDAXIS = 2
    MINUS_2NDAXIS = 3
    PLUS_3RDAXIS = 4
    MINUS_3RDAXIS = 5

    NAME_MAP = {
        PLUS_1STAXIS: "+1stAxis",
        MINUS_1STAXIS: "-1stAxis",
        PLUS_2NDAXIS: "+2ndAxis",
        MINUS_2NDAXIS: "-2ndAxis",
        PLUS_3RDAXIS: "+3rdAxis",
        MINUS_3RDAXIS: "-3rdAxis",
    }


class CustomBoundsAxisOffsetDirectionEnumField(
    EnumField[
        CustomBoundsAxisOffsetDirectionEnumAttrOperator,
        CustomBoundsAxisOffsetDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CustomBoundsAxisOffsetDirectionEnumAttrOperator
    PLUG_CLS = CustomBoundsAxisOffsetDirectionEnumPlugOperator


class GeneratedBdControllerShape(Shape):
    __slots__ = ()

    NODE_TYPE = "bdControllerShape"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    underWorldObject = BoolField(default_value=False)
    uwo = underWorldObject

    localPosition = LocalPositionField(default_value=(0.0, 0.0, 0.0))
    lp = localPosition
    localPositionX = localPosition.localPositionX
    lpx = localPositionX
    localPositionY = localPosition.localPositionY
    lpy = localPositionY
    localPositionZ = localPosition.localPositionZ
    lpz = localPositionZ

    worldPosition = WorldPositionField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    wp = worldPosition

    localScale = LocalScaleField(default_value=(1.0, 1.0, 1.0))
    los = localScale
    localScaleX = localScale.localScaleX
    lsx = localScaleX
    localScaleY = localScale.localScaleY
    lsy = localScaleY
    localScaleZ = localScale.localScaleZ
    lsz = localScaleZ

    shape = ShapeEnumField(default_value=59)
    sh = shape

    shapeAnimationTransformMatrix = DataMatrixField()
    satm = shapeAnimationTransformMatrix

    shapeDrawOnTop = BoolField(default_value=False)
    sdot = shapeDrawOnTop

    shapeLineWidth = FloatField(default_value=1.0, min_value=1.0)
    slw = shapeLineWidth

    shapeTransparency = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    stp = shapeTransparency

    shapeFillTransparency = FloatField(
        default_value=0.8500000238418579, min_value=0.0, max_value=1.0
    )
    sftp = shapeFillTransparency

    showShapeOffsetLine = BoolField(default_value=False)
    ssol = showShapeOffsetLine

    shapeOffsetLineTemplate = BoolField(default_value=False)
    solt = shapeOffsetLineTemplate

    shape1stAxis = Shape1stAxisEnumField(default_value=0)
    s1a = shape1stAxis

    shape2ndAxis = Shape2ndAxisEnumField(default_value=2)
    s2a = shape2ndAxis

    shapeAxisOffset = BoolField(default_value=False)
    sao = shapeAxisOffset

    shapeAxisOffsetDirection = ShapeAxisOffsetDirectionEnumField(
        default_value=0
    )
    saod = shapeAxisOffsetDirection

    shapeAxisOffsetLength = DoubleLinearField(default_value=1.0, min_value=0.0)
    saol = shapeAxisOffsetLength

    shapeRootSize = DoubleField(default_value=1.0)
    srs = shapeRootSize

    shapeTranslate = ShapeTranslateField(default_value=(0.0, 0.0, 0.0))
    st = shapeTranslate
    shapeTranslateX = shapeTranslate.shapeTranslateX
    stx = shapeTranslateX
    shapeTranslateY = shapeTranslate.shapeTranslateY
    sty = shapeTranslateY
    shapeTranslateZ = shapeTranslate.shapeTranslateZ
    stz = shapeTranslateZ

    shapeRotate = ShapeRotateField(default_value=(0.0, 0.0, 0.0))
    sr = shapeRotate
    shapeRotateX = shapeRotate.shapeRotateX
    srx = shapeRotateX
    shapeRotateY = shapeRotate.shapeRotateY
    sry = shapeRotateY
    shapeRotateZ = shapeRotate.shapeRotateZ
    srz = shapeRotateZ

    shapeScale = ShapeScaleField(default_value=(1.0, 1.0, 1.0))
    ssc = shapeScale
    shapeScaleX = shapeScale.shapeScaleX
    sscx = shapeScaleX
    shapeScaleY = shapeScale.shapeScaleY
    sscy = shapeScaleY
    shapeScaleZ = shapeScale.shapeScaleZ
    sscz = shapeScaleZ

    shapeAxisTranslate = ShapeAxisTranslateField(default_value=(0.0, 0.0, 0.0))
    sat = shapeAxisTranslate
    shapeAxisTranslateX = shapeAxisTranslate.shapeAxisTranslateX
    satx = shapeAxisTranslateX
    shapeAxisTranslateY = shapeAxisTranslate.shapeAxisTranslateY
    saty = shapeAxisTranslateY
    shapeAxisTranslateZ = shapeAxisTranslate.shapeAxisTranslateZ
    satz = shapeAxisTranslateZ

    shapeAxisRotate = ShapeAxisRotateField(default_value=(0.0, 0.0, 0.0))
    sar = shapeAxisRotate
    shapeAxisRotateX = shapeAxisRotate.shapeAxisRotateX
    sarx = shapeAxisRotateX
    shapeAxisRotateY = shapeAxisRotate.shapeAxisRotateY
    sary = shapeAxisRotateY
    shapeAxisRotateZ = shapeAxisRotate.shapeAxisRotateZ
    sarz = shapeAxisRotateZ

    shapeAxisScale = ShapeAxisScaleField(default_value=(1.0, 1.0, 1.0))
    sasc = shapeAxisScale
    shapeAxisScaleX = shapeAxisScale.shapeAxisScaleX
    sascx = shapeAxisScaleX
    shapeAxisScaleY = shapeAxisScale.shapeAxisScaleY
    sascy = shapeAxisScaleY
    shapeAxisScaleZ = shapeAxisScale.shapeAxisScaleZ
    sascz = shapeAxisScaleZ

    shapeSize = DoubleField(default_value=1.0)
    ss = shapeSize

    boundsMode = BoundsModeEnumField(default_value=1)
    bdm = boundsMode

    showBoundsPreview = BoolField(default_value=False)
    sbp = showBoundsPreview

    customBounds1stAxis = CustomBounds1stAxisEnumField(default_value=0)
    cb1a = customBounds1stAxis

    customBounds2ndAxis = CustomBounds2ndAxisEnumField(default_value=2)
    cb2a = customBounds2ndAxis

    customBoundsAxisOffset = BoolField(default_value=False)
    cbao = customBoundsAxisOffset

    customBoundsAxisOffsetDirection = CustomBoundsAxisOffsetDirectionEnumField(
        default_value=0
    )
    cbaod = customBoundsAxisOffsetDirection

    customBoundsAxisOffsetLength = DoubleLinearField(
        default_value=1.0, min_value=0.0
    )
    cbaol = customBoundsAxisOffsetLength

    customBoundsRootSize = DoubleField(default_value=1.0)
    cbrs = customBoundsRootSize

    customBoundsTranslate = CustomBoundsTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbt = customBoundsTranslate
    customBoundsTranslateX = customBoundsTranslate.customBoundsTranslateX
    cbtx = customBoundsTranslateX
    customBoundsTranslateY = customBoundsTranslate.customBoundsTranslateY
    cbty = customBoundsTranslateY
    customBoundsTranslateZ = customBoundsTranslate.customBoundsTranslateZ
    cbtz = customBoundsTranslateZ

    customBoundsRotate = CustomBoundsRotateField(default_value=(0.0, 0.0, 0.0))
    cbr = customBoundsRotate
    customBoundsRotateX = customBoundsRotate.customBoundsRotateX
    cbrx = customBoundsRotateX
    customBoundsRotateY = customBoundsRotate.customBoundsRotateY
    cbry = customBoundsRotateY
    customBoundsRotateZ = customBoundsRotate.customBoundsRotateZ
    cbrz = customBoundsRotateZ

    customBoundsScale = CustomBoundsScaleField(default_value=(1.0, 1.0, 1.0))
    cbsc = customBoundsScale
    customBoundsScaleX = customBoundsScale.customBoundsScaleX
    cbscx = customBoundsScaleX
    customBoundsScaleY = customBoundsScale.customBoundsScaleY
    cbscy = customBoundsScaleY
    customBoundsScaleZ = customBoundsScale.customBoundsScaleZ
    cbscz = customBoundsScaleZ

    customBoundsAxisTranslate = CustomBoundsAxisTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbat = customBoundsAxisTranslate
    customBoundsAxisTranslateX = (
        customBoundsAxisTranslate.customBoundsAxisTranslateX
    )
    cbatx = customBoundsAxisTranslateX
    customBoundsAxisTranslateY = (
        customBoundsAxisTranslate.customBoundsAxisTranslateY
    )
    cbaty = customBoundsAxisTranslateY
    customBoundsAxisTranslateZ = (
        customBoundsAxisTranslate.customBoundsAxisTranslateZ
    )
    cbatz = customBoundsAxisTranslateZ

    customBoundsAxisRotate = CustomBoundsAxisRotateField(
        default_value=(0.0, 0.0, 0.0)
    )
    cbar = customBoundsAxisRotate
    customBoundsAxisRotateX = customBoundsAxisRotate.customBoundsAxisRotateX
    cbarx = customBoundsAxisRotateX
    customBoundsAxisRotateY = customBoundsAxisRotate.customBoundsAxisRotateY
    cbary = customBoundsAxisRotateY
    customBoundsAxisRotateZ = customBoundsAxisRotate.customBoundsAxisRotateZ
    cbarz = customBoundsAxisRotateZ

    customBoundsAxisScale = CustomBoundsAxisScaleField(
        default_value=(1.0, 1.0, 1.0)
    )
    cbasc = customBoundsAxisScale
    customBoundsAxisScaleX = customBoundsAxisScale.customBoundsAxisScaleX
    cbascx = customBoundsAxisScaleX
    customBoundsAxisScaleY = customBoundsAxisScale.customBoundsAxisScaleY
    cbascy = customBoundsAxisScaleY
    customBoundsAxisScaleZ = customBoundsAxisScale.customBoundsAxisScaleZ
    cbascz = customBoundsAxisScaleZ

    customBoundsSize = DoubleField(default_value=1.0)
    cbs = customBoundsSize
