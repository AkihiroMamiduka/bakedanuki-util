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
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from .....attr.define.std.dt.matrix import DataMatrixField


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    GEAR = 0
    LINE = 1
    LINEARROWATEND = 2
    LINEARROWATENDS = 3
    LINEWIDEARROWATEND = 4
    LINEWIDEARROWATENDS = 5
    LINESQUAREATEND = 6
    LINESQUAREATENDS = 7
    LINEDIAMONDATEND = 8
    LINEDIAMONDATENDS = 9
    LINECIRCLEATEND = 10
    LINECIRCLEATENDS = 11
    LINETRIANGLEATEND = 12
    LINETRIANGLEATENDS = 13
    CROSSLINE1ST2ND = 14
    CROSSLINE1ST2NDARROWATEND = 15
    CROSSLINE1ST2NDARROWATENDS = 16
    CROSSLINE1ST2NDWIDEARROWATEND = 17
    CROSSLINE1ST2NDWIDEARROWATENDS = 18
    CROSSLINE1ST2NDSQUAREATEND = 19
    CROSSLINE1ST2NDSQUAREATENDS = 20
    CROSSLINE1ST2NDDIAMONDATEND = 21
    CROSSLINE1ST2NDDIAMONDATENDS = 22
    CROSSLINE1ST2NDCIRCLEATEND = 23
    CROSSLINE1ST2NDCIRCLEATENDS = 24
    CROSSLINE1ST2NDTRIANGLEATEND = 25
    CROSSLINE1ST2NDTRIANGLEATENDS = 26
    CROSSLINE1ST3RD = 27
    CROSSLINE1ST3RDARROWATEND = 28
    CROSSLINE1ST3RDARROWATENDS = 29
    CROSSLINE1ST3RDWIDEARROWATEND = 30
    CROSSLINE1ST3RDWIDEARROWATENDS = 31
    CROSSLINE1ST3RDSQUAREATEND = 32
    CROSSLINE1ST3RDSQUAREATENDS = 33
    CROSSLINE1ST3RDDIAMONDATEND = 34
    CROSSLINE1ST3RDDIAMONDATENDS = 35
    CROSSLINE1ST3RDCIRCLEATEND = 36
    CROSSLINE1ST3RDCIRCLEATENDS = 37
    CROSSLINE1ST3RDTRIANGLEATEND = 38
    CROSSLINE1ST3RDTRIANGLEATENDS = 39
    CROSSLINE2ND3RD = 40
    CROSSLINE2ND3RDARROWATEND = 41
    CROSSLINE2ND3RDARROWATENDS = 42
    CROSSLINE2ND3RDWIDEARROWATEND = 43
    CROSSLINE2ND3RDWIDEARROWATENDS = 44
    CROSSLINE2ND3RDSQUAREATEND = 45
    CROSSLINE2ND3RDSQUAREATENDS = 46
    CROSSLINE2ND3RDDIAMONDATEND = 47
    CROSSLINE2ND3RDDIAMONDATENDS = 48
    CROSSLINE2ND3RDCIRCLEATEND = 49
    CROSSLINE2ND3RDCIRCLEATENDS = 50
    CROSSLINE2ND3RDTRIANGLEATEND = 51
    CROSSLINE2ND3RDTRIANGLEATENDS = 52
    CROSSLINE3AXIS = 53
    CROSSLINE3AXISENDCUBE = 54
    CROSSLINE3AXISENDOCTAHEDRON = 55
    CROSSLINE3AXISENDSPHERE = 56
    CROSSLINE3AXISENDPYRAMID = 57
    CROSSLINE3AXISENDCONE = 58
    TRIANGLE = 59
    TRIANGLEARROW3D = 60
    SQUARE = 61
    SQUAREARROW2D = 62
    SQUAREARROW3D = 63
    SQUAREARROWCROSSLINE2D = 64
    SQUAREARROWCROSSLINE3D = 65
    SQUAREARROWCROSSLINETEMPLATE2D = 66
    SQUAREARROWCROSSLINETEMPLATE3D = 67
    SQUAREARROW4WAY2D = 68
    SQUAREARROW4WAY3D = 69
    SQUARETEMPLATEARROW4WAY2D = 70
    SQUARETEMPLATEARROW4WAY3D = 71
    DIAMOND = 72
    CUBE = 73
    CUBEARROW2D = 74
    CUBEARROW3D = 75
    CUBEFIN = 76
    CUBEFINARROW = 77
    OCTAHEDRON = 78
    OCTAHEDRONARROW = 79
    OCTAHEDRONARROWFIN = 80
    CIRCLE = 81
    CIRCLEARROW2D = 82
    CIRCLEARROW3D = 83
    SEMICIRCLE = 84
    SEMICIRCLEARROWATEND = 85
    SEMICIRCLEARROWATENDS = 86
    SEMICIRCLEWIDEARROWATEND = 87
    SEMICIRCLEWIDEARROWATENDS = 88
    SEMICIRCLEARROW2D = 89
    SEMICIRCLEARROW3D = 90
    SPHERE = 91
    SPHEREARROW2D = 92
    SPHEREARROW3D = 93
    CYLINDER = 94
    CYLINDERFIN = 95
    CYLINDERFINARROW = 96
    ARROW = 97
    ARROWFIN = 98
    PYRAMID = 99
    PYRAMIDFIN = 100
    CONE = 101
    CONEFIN = 102
    COLORCROSSLINE3AXIS = 103
    COLORCROSSLINE3AXISENDCUBE = 104
    COLORCROSSLINE3AXISENDOCTAHEDRON = 105
    COLORCROSSLINE3AXISENDSPHERE = 106
    COLORCROSSLINE3AXISENDPYRAMID = 107
    COLORCROSSLINE3AXISENDCONE = 108
    COLORCUBE = 109
    COLORCORNERCUBE = 110
    COLORSPHERE = 111
    COLORSPHEREARROW2D = 112
    COLORSPHEREARROW3D = 113
    COLORSPHERECROSSLINE = 114


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    LINE = 1
    LINEARROWATEND = 2
    LINEARROWATENDS = 3
    LINEWIDEARROWATEND = 4
    LINEWIDEARROWATENDS = 5
    LINESQUAREATEND = 6
    LINESQUAREATENDS = 7
    LINEDIAMONDATEND = 8
    LINEDIAMONDATENDS = 9
    LINECIRCLEATEND = 10
    LINECIRCLEATENDS = 11
    LINETRIANGLEATEND = 12
    LINETRIANGLEATENDS = 13
    CROSSLINE1ST2ND = 14
    CROSSLINE1ST2NDARROWATEND = 15
    CROSSLINE1ST2NDARROWATENDS = 16
    CROSSLINE1ST2NDWIDEARROWATEND = 17
    CROSSLINE1ST2NDWIDEARROWATENDS = 18
    CROSSLINE1ST2NDSQUAREATEND = 19
    CROSSLINE1ST2NDSQUAREATENDS = 20
    CROSSLINE1ST2NDDIAMONDATEND = 21
    CROSSLINE1ST2NDDIAMONDATENDS = 22
    CROSSLINE1ST2NDCIRCLEATEND = 23
    CROSSLINE1ST2NDCIRCLEATENDS = 24
    CROSSLINE1ST2NDTRIANGLEATEND = 25
    CROSSLINE1ST2NDTRIANGLEATENDS = 26
    CROSSLINE1ST3RD = 27
    CROSSLINE1ST3RDARROWATEND = 28
    CROSSLINE1ST3RDARROWATENDS = 29
    CROSSLINE1ST3RDWIDEARROWATEND = 30
    CROSSLINE1ST3RDWIDEARROWATENDS = 31
    CROSSLINE1ST3RDSQUAREATEND = 32
    CROSSLINE1ST3RDSQUAREATENDS = 33
    CROSSLINE1ST3RDDIAMONDATEND = 34
    CROSSLINE1ST3RDDIAMONDATENDS = 35
    CROSSLINE1ST3RDCIRCLEATEND = 36
    CROSSLINE1ST3RDCIRCLEATENDS = 37
    CROSSLINE1ST3RDTRIANGLEATEND = 38
    CROSSLINE1ST3RDTRIANGLEATENDS = 39
    CROSSLINE2ND3RD = 40
    CROSSLINE2ND3RDARROWATEND = 41
    CROSSLINE2ND3RDARROWATENDS = 42
    CROSSLINE2ND3RDWIDEARROWATEND = 43
    CROSSLINE2ND3RDWIDEARROWATENDS = 44
    CROSSLINE2ND3RDSQUAREATEND = 45
    CROSSLINE2ND3RDSQUAREATENDS = 46
    CROSSLINE2ND3RDDIAMONDATEND = 47
    CROSSLINE2ND3RDDIAMONDATENDS = 48
    CROSSLINE2ND3RDCIRCLEATEND = 49
    CROSSLINE2ND3RDCIRCLEATENDS = 50
    CROSSLINE2ND3RDTRIANGLEATEND = 51
    CROSSLINE2ND3RDTRIANGLEATENDS = 52
    CROSSLINE3AXIS = 53
    CROSSLINE3AXISENDCUBE = 54
    CROSSLINE3AXISENDOCTAHEDRON = 55
    CROSSLINE3AXISENDSPHERE = 56
    CROSSLINE3AXISENDPYRAMID = 57
    CROSSLINE3AXISENDCONE = 58
    TRIANGLE = 59
    TRIANGLEARROW3D = 60
    SQUARE = 61
    SQUAREARROW2D = 62
    SQUAREARROW3D = 63
    SQUAREARROWCROSSLINE2D = 64
    SQUAREARROWCROSSLINE3D = 65
    SQUAREARROWCROSSLINETEMPLATE2D = 66
    SQUAREARROWCROSSLINETEMPLATE3D = 67
    SQUAREARROW4WAY2D = 68
    SQUAREARROW4WAY3D = 69
    SQUARETEMPLATEARROW4WAY2D = 70
    SQUARETEMPLATEARROW4WAY3D = 71
    DIAMOND = 72
    CUBE = 73
    CUBEARROW2D = 74
    CUBEARROW3D = 75
    CUBEFIN = 76
    CUBEFINARROW = 77
    OCTAHEDRON = 78
    OCTAHEDRONARROW = 79
    OCTAHEDRONARROWFIN = 80
    CIRCLE = 81
    CIRCLEARROW2D = 82
    CIRCLEARROW3D = 83
    SEMICIRCLE = 84
    SEMICIRCLEARROWATEND = 85
    SEMICIRCLEARROWATENDS = 86
    SEMICIRCLEWIDEARROWATEND = 87
    SEMICIRCLEWIDEARROWATENDS = 88
    SEMICIRCLEARROW2D = 89
    SEMICIRCLEARROW3D = 90
    SPHERE = 91
    SPHEREARROW2D = 92
    SPHEREARROW3D = 93
    CYLINDER = 94
    CYLINDERFIN = 95
    CYLINDERFINARROW = 96
    ARROW = 97
    ARROWFIN = 98
    PYRAMID = 99
    PYRAMIDFIN = 100
    CONE = 101
    CONEFIN = 102
    COLORCROSSLINE3AXIS = 103
    COLORCROSSLINE3AXISENDCUBE = 104
    COLORCROSSLINE3AXISENDOCTAHEDRON = 105
    COLORCROSSLINE3AXISENDSPHERE = 106
    COLORCROSSLINE3AXISENDPYRAMID = 107
    COLORCROSSLINE3AXISENDCONE = 108
    COLORCUBE = 109
    COLORCORNERCUBE = 110
    COLORSPHERE = 111
    COLORSPHEREARROW2D = 112
    COLORSPHEREARROW3D = 113
    COLORSPHERECROSSLINE = 114

    NAME_MAP = {
        GEAR: "Gear",
        LINE: "Line",
        LINEARROWATEND: "LineArrowAtEnd",
        LINEARROWATENDS: "LineArrowAtEnds",
        LINEWIDEARROWATEND: "LineWideArrowAtEnd",
        LINEWIDEARROWATENDS: "LineWideArrowAtEnds",
        LINESQUAREATEND: "LineSquareAtEnd",
        LINESQUAREATENDS: "LineSquareAtEnds",
        LINEDIAMONDATEND: "LineDiamondAtEnd",
        LINEDIAMONDATENDS: "LineDiamondAtEnds",
        LINECIRCLEATEND: "LineCircleAtEnd",
        LINECIRCLEATENDS: "LineCircleAtEnds",
        LINETRIANGLEATEND: "LineTriangleAtEnd",
        LINETRIANGLEATENDS: "LineTriangleAtEnds",
        CROSSLINE1ST2ND: "CrossLine1st2nd",
        CROSSLINE1ST2NDARROWATEND: "CrossLine1st2ndArrowAtEnd",
        CROSSLINE1ST2NDARROWATENDS: "CrossLine1st2ndArrowAtEnds",
        CROSSLINE1ST2NDWIDEARROWATEND: "CrossLine1st2ndWideArrowAtEnd",
        CROSSLINE1ST2NDWIDEARROWATENDS: "CrossLine1st2ndWideArrowAtEnds",
        CROSSLINE1ST2NDSQUAREATEND: "CrossLine1st2ndSquareAtEnd",
        CROSSLINE1ST2NDSQUAREATENDS: "CrossLine1st2ndSquareAtEnds",
        CROSSLINE1ST2NDDIAMONDATEND: "CrossLine1st2ndDiamondAtEnd",
        CROSSLINE1ST2NDDIAMONDATENDS: "CrossLine1st2ndDiamondAtEnds",
        CROSSLINE1ST2NDCIRCLEATEND: "CrossLine1st2ndCircleAtEnd",
        CROSSLINE1ST2NDCIRCLEATENDS: "CrossLine1st2ndCircleAtEnds",
        CROSSLINE1ST2NDTRIANGLEATEND: "CrossLine1st2ndTriangleAtEnd",
        CROSSLINE1ST2NDTRIANGLEATENDS: "CrossLine1st2ndTriangleAtEnds",
        CROSSLINE1ST3RD: "CrossLine1st3rd",
        CROSSLINE1ST3RDARROWATEND: "CrossLine1st3rdArrowAtEnd",
        CROSSLINE1ST3RDARROWATENDS: "CrossLine1st3rdArrowAtEnds",
        CROSSLINE1ST3RDWIDEARROWATEND: "CrossLine1st3rdWideArrowAtEnd",
        CROSSLINE1ST3RDWIDEARROWATENDS: "CrossLine1st3rdWideArrowAtEnds",
        CROSSLINE1ST3RDSQUAREATEND: "CrossLine1st3rdSquareAtEnd",
        CROSSLINE1ST3RDSQUAREATENDS: "CrossLine1st3rdSquareAtEnds",
        CROSSLINE1ST3RDDIAMONDATEND: "CrossLine1st3rdDiamondAtEnd",
        CROSSLINE1ST3RDDIAMONDATENDS: "CrossLine1st3rdDiamondAtEnds",
        CROSSLINE1ST3RDCIRCLEATEND: "CrossLine1st3rdCircleAtEnd",
        CROSSLINE1ST3RDCIRCLEATENDS: "CrossLine1st3rdCircleAtEnds",
        CROSSLINE1ST3RDTRIANGLEATEND: "CrossLine1st3rdTriangleAtEnd",
        CROSSLINE1ST3RDTRIANGLEATENDS: "CrossLine1st3rdTriangleAtEnds",
        CROSSLINE2ND3RD: "CrossLine2nd3rd",
        CROSSLINE2ND3RDARROWATEND: "CrossLine2nd3rdArrowAtEnd",
        CROSSLINE2ND3RDARROWATENDS: "CrossLine2nd3rdArrowAtEnds",
        CROSSLINE2ND3RDWIDEARROWATEND: "CrossLine2nd3rdWideArrowAtEnd",
        CROSSLINE2ND3RDWIDEARROWATENDS: "CrossLine2nd3rdWideArrowAtEnds",
        CROSSLINE2ND3RDSQUAREATEND: "CrossLine2nd3rdSquareAtEnd",
        CROSSLINE2ND3RDSQUAREATENDS: "CrossLine2nd3rdSquareAtEnds",
        CROSSLINE2ND3RDDIAMONDATEND: "CrossLine2nd3rdDiamondAtEnd",
        CROSSLINE2ND3RDDIAMONDATENDS: "CrossLine2nd3rdDiamondAtEnds",
        CROSSLINE2ND3RDCIRCLEATEND: "CrossLine2nd3rdCircleAtEnd",
        CROSSLINE2ND3RDCIRCLEATENDS: "CrossLine2nd3rdCircleAtEnds",
        CROSSLINE2ND3RDTRIANGLEATEND: "CrossLine2nd3rdTriangleAtEnd",
        CROSSLINE2ND3RDTRIANGLEATENDS: "CrossLine2nd3rdTriangleAtEnds",
        CROSSLINE3AXIS: "CrossLine3Axis",
        CROSSLINE3AXISENDCUBE: "CrossLine3AxisEndCube",
        CROSSLINE3AXISENDOCTAHEDRON: "CrossLine3AxisEndOctahedron",
        CROSSLINE3AXISENDSPHERE: "CrossLine3AxisEndSphere",
        CROSSLINE3AXISENDPYRAMID: "CrossLine3AxisEndPyramid",
        CROSSLINE3AXISENDCONE: "CrossLine3AxisEndCone",
        TRIANGLE: "Triangle",
        TRIANGLEARROW3D: "TriangleArrow3D",
        SQUARE: "Square",
        SQUAREARROW2D: "SquareArrow2D",
        SQUAREARROW3D: "SquareArrow3D",
        SQUAREARROWCROSSLINE2D: "SquareArrowCrossLine2D",
        SQUAREARROWCROSSLINE3D: "SquareArrowCrossLine3D",
        SQUAREARROWCROSSLINETEMPLATE2D: "SquareArrowCrossLineTemplate2D",
        SQUAREARROWCROSSLINETEMPLATE3D: "SquareArrowCrossLineTemplate3D",
        SQUAREARROW4WAY2D: "SquareArrow4Way2D",
        SQUAREARROW4WAY3D: "SquareArrow4Way3D",
        SQUARETEMPLATEARROW4WAY2D: "SquareTemplateArrow4Way2D",
        SQUARETEMPLATEARROW4WAY3D: "SquareTemplateArrow4Way3D",
        DIAMOND: "Diamond",
        CUBE: "Cube",
        CUBEARROW2D: "CubeArrow2D",
        CUBEARROW3D: "CubeArrow3D",
        CUBEFIN: "CubeFin",
        CUBEFINARROW: "CubeFinArrow",
        OCTAHEDRON: "Octahedron",
        OCTAHEDRONARROW: "OctahedronArrow",
        OCTAHEDRONARROWFIN: "OctahedronArrowFin",
        CIRCLE: "Circle",
        CIRCLEARROW2D: "CircleArrow2D",
        CIRCLEARROW3D: "CircleArrow3D",
        SEMICIRCLE: "Semicircle",
        SEMICIRCLEARROWATEND: "SemicircleArrowAtEnd",
        SEMICIRCLEARROWATENDS: "SemicircleArrowAtEnds",
        SEMICIRCLEWIDEARROWATEND: "SemicircleWideArrowAtEnd",
        SEMICIRCLEWIDEARROWATENDS: "SemicircleWideArrowAtEnds",
        SEMICIRCLEARROW2D: "SemicircleArrow2D",
        SEMICIRCLEARROW3D: "SemicircleArrow3D",
        SPHERE: "Sphere",
        SPHEREARROW2D: "SphereArrow2D",
        SPHEREARROW3D: "SphereArrow3D",
        CYLINDER: "Cylinder",
        CYLINDERFIN: "CylinderFin",
        CYLINDERFINARROW: "CylinderFinArrow",
        ARROW: "Arrow",
        ARROWFIN: "ArrowFin",
        PYRAMID: "Pyramid",
        PYRAMIDFIN: "PyramidFin",
        CONE: "Cone",
        CONEFIN: "ConeFin",
        COLORCROSSLINE3AXIS: "ColorCrossLine3Axis",
        COLORCROSSLINE3AXISENDCUBE: "ColorCrossLine3AxisEndCube",
        COLORCROSSLINE3AXISENDOCTAHEDRON: "ColorCrossLine3AxisEndOctahedron",
        COLORCROSSLINE3AXISENDSPHERE: "ColorCrossLine3AxisEndSphere",
        COLORCROSSLINE3AXISENDPYRAMID: "ColorCrossLine3AxisEndPyramid",
        COLORCROSSLINE3AXISENDCONE: "ColorCrossLine3AxisEndCone",
        COLORCUBE: "ColorCube",
        COLORCORNERCUBE: "ColorCornerCube",
        COLORSPHERE: "ColorSphere",
        COLORSPHEREARROW2D: "ColorSphereArrow2D",
        COLORSPHEREARROW3D: "ColorSphereArrow3D",
        COLORSPHERECROSSLINE: "ColorSphereCrossLine",
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

    shape = ShapeEnumField(default_value=73)
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

    shapeFill = BoolField(default_value=False)
    sfl = shapeFill

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

    shapePartOffset = DoubleLinearField(default_value=0.0)
    spo = shapePartOffset

    shapePartOffsetAngle = DoubleAngleField(
        default_value=0.0, min_value=-90.0, max_value=90.0
    )
    spoa = shapePartOffsetAngle

    shapePartFinHeight = DoubleLinearField(default_value=0.5)
    spfh = shapePartFinHeight

    shapePartSize = DoubleField(default_value=1.0)
    sps = shapePartSize

    shapePartLengthScale = DoubleField(default_value=1.0)
    spls = shapePartLengthScale

    shapePartWidthScale = DoubleField(default_value=1.0)
    spws = shapePartWidthScale

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
