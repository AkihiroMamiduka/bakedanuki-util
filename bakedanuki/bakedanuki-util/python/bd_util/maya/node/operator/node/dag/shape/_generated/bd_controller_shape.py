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
    LINE2ND = 3
    LINE3RD = 4
    CROSSLINEXY = 5
    CROSSLINEXYZ = 6
    TRIANGLE = 7
    TRIANGLEFILLED = 8
    TRIANGLEARROW3D = 9
    TRIANGLEARROW3DFILLED = 10
    SQUARE = 11
    SQUAREFILLED = 12
    SQUAREARROW2D = 13
    SQUAREARROW2DFILLED = 14
    SQUAREARROW3D = 15
    SQUAREARROW3DFILLED = 16
    SQUAREARROWCROSSLINE2D = 17
    SQUAREARROWCROSSLINE2DFILLED = 18
    SQUAREARROWCROSSLINE3D = 19
    SQUAREARROWCROSSLINE3DFILLED = 20
    SQUAREARROWCROSSLINETEMPLATE2D = 21
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 22
    SQUAREARROWCROSSLINETEMPLATE3D = 23
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 24
    SQUAREARROW4WAY2D = 25
    SQUAREARROW4WAY2DFILLED = 26
    SQUAREARROW4WAY3D = 27
    SQUAREARROW4WAY3DFILLED = 28
    SQUARETEMPLATEARROW4WAY2D = 29
    SQUARETEMPLATEARROW4WAY2DFILLED = 30
    SQUARETEMPLATEARROW4WAY3D = 31
    SQUARETEMPLATEARROW4WAY3DFILLED = 32
    CUBE = 33
    CUBEFILLED = 34
    CUBEARROW2D = 35
    CUBEARROW2DFILLED = 36
    CUBEARROW3D = 37
    CUBEARROW3DFILLED = 38
    CUBEFIN = 39
    CUBEFINFILLED = 40
    CUBEFINARROW = 41
    CUBEFINARROWFILLED = 42
    OCTAHEDRON = 43
    OCTAHEDRONFILLED = 44
    OCTAHEDRONARROW = 45
    OCTAHEDRONARROWFILLED = 46
    OCTAHEDRONARROWFIN = 47
    OCTAHEDRONARROWFINFILLED = 48
    CIRCLE = 49
    CIRCLEFILLED = 50
    CIRCLEARROW2D = 51
    CIRCLEARROW2DFILLED = 52
    CIRCLEARROW3D = 53
    CIRCLEARROW3DFILLED = 54
    SEMICIRCLE = 55
    SEMICIRCLEFILLED = 56
    SEMICIRCLEARROW2D = 57
    SEMICIRCLEARROW2DFILLED = 58
    SEMICIRCLEARROW3D = 59
    SEMICIRCLEARROW3DFILLED = 60
    SPHERE = 61
    SPHEREFILLED = 62
    SPHEREARROW2D = 63
    SPHEREARROW2DFILLED = 64
    SPHEREARROW3D = 65
    SPHEREARROW3DFILLED = 66
    CYLINDER = 67
    CYLINDERFILLED = 68
    CYLINDERFIN = 69
    CYLINDERFINFILLED = 70
    CYLINDERFINARROW = 71
    CYLINDERFINARROWFILLED = 72
    ARROW = 73
    ARROWFILLED = 74
    ARROWFIN = 75
    ARROWFINFILLED = 76
    PYRAMID = 77
    PYRAMIDFILLED = 78
    PYRAMIDFIN = 79
    PYRAMIDFINFILLED = 80
    CONE = 81
    CONEFILLED = 82
    CONEFIN = 83
    CONEFINFILLED = 84
    COLORCROSSLINE = 85
    COLORSPHERE = 86
    COLORSPHEREFILLED = 87
    COLORSPHEREARROW2D = 88
    COLORSPHEREARROW2DFILLED = 89
    COLORSPHEREARROW3D = 90
    COLORSPHEREARROW3DFILLED = 91
    COLORSPHERECROSSLINE = 92
    COLORSPHERECROSSLINEFILLED = 93


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    GEARFILLED = 1
    LINE1ST = 2
    LINE2ND = 3
    LINE3RD = 4
    CROSSLINEXY = 5
    CROSSLINEXYZ = 6
    TRIANGLE = 7
    TRIANGLEFILLED = 8
    TRIANGLEARROW3D = 9
    TRIANGLEARROW3DFILLED = 10
    SQUARE = 11
    SQUAREFILLED = 12
    SQUAREARROW2D = 13
    SQUAREARROW2DFILLED = 14
    SQUAREARROW3D = 15
    SQUAREARROW3DFILLED = 16
    SQUAREARROWCROSSLINE2D = 17
    SQUAREARROWCROSSLINE2DFILLED = 18
    SQUAREARROWCROSSLINE3D = 19
    SQUAREARROWCROSSLINE3DFILLED = 20
    SQUAREARROWCROSSLINETEMPLATE2D = 21
    SQUAREARROWCROSSLINETEMPLATE2DFILLED = 22
    SQUAREARROWCROSSLINETEMPLATE3D = 23
    SQUAREARROWCROSSLINETEMPLATE3DFILLED = 24
    SQUAREARROW4WAY2D = 25
    SQUAREARROW4WAY2DFILLED = 26
    SQUAREARROW4WAY3D = 27
    SQUAREARROW4WAY3DFILLED = 28
    SQUARETEMPLATEARROW4WAY2D = 29
    SQUARETEMPLATEARROW4WAY2DFILLED = 30
    SQUARETEMPLATEARROW4WAY3D = 31
    SQUARETEMPLATEARROW4WAY3DFILLED = 32
    CUBE = 33
    CUBEFILLED = 34
    CUBEARROW2D = 35
    CUBEARROW2DFILLED = 36
    CUBEARROW3D = 37
    CUBEARROW3DFILLED = 38
    CUBEFIN = 39
    CUBEFINFILLED = 40
    CUBEFINARROW = 41
    CUBEFINARROWFILLED = 42
    OCTAHEDRON = 43
    OCTAHEDRONFILLED = 44
    OCTAHEDRONARROW = 45
    OCTAHEDRONARROWFILLED = 46
    OCTAHEDRONARROWFIN = 47
    OCTAHEDRONARROWFINFILLED = 48
    CIRCLE = 49
    CIRCLEFILLED = 50
    CIRCLEARROW2D = 51
    CIRCLEARROW2DFILLED = 52
    CIRCLEARROW3D = 53
    CIRCLEARROW3DFILLED = 54
    SEMICIRCLE = 55
    SEMICIRCLEFILLED = 56
    SEMICIRCLEARROW2D = 57
    SEMICIRCLEARROW2DFILLED = 58
    SEMICIRCLEARROW3D = 59
    SEMICIRCLEARROW3DFILLED = 60
    SPHERE = 61
    SPHEREFILLED = 62
    SPHEREARROW2D = 63
    SPHEREARROW2DFILLED = 64
    SPHEREARROW3D = 65
    SPHEREARROW3DFILLED = 66
    CYLINDER = 67
    CYLINDERFILLED = 68
    CYLINDERFIN = 69
    CYLINDERFINFILLED = 70
    CYLINDERFINARROW = 71
    CYLINDERFINARROWFILLED = 72
    ARROW = 73
    ARROWFILLED = 74
    ARROWFIN = 75
    ARROWFINFILLED = 76
    PYRAMID = 77
    PYRAMIDFILLED = 78
    PYRAMIDFIN = 79
    PYRAMIDFINFILLED = 80
    CONE = 81
    CONEFILLED = 82
    CONEFIN = 83
    CONEFINFILLED = 84
    COLORCROSSLINE = 85
    COLORSPHERE = 86
    COLORSPHEREFILLED = 87
    COLORSPHEREARROW2D = 88
    COLORSPHEREARROW2DFILLED = 89
    COLORSPHEREARROW3D = 90
    COLORSPHEREARROW3DFILLED = 91
    COLORSPHERECROSSLINE = 92
    COLORSPHERECROSSLINEFILLED = 93

    NAME_MAP = {
        GEAR: "Gear",
        GEARFILLED: "GearFilled",
        LINE1ST: "Line1st",
        LINE2ND: "Line2nd",
        LINE3RD: "Line3rd",
        CROSSLINEXY: "CrossLineXY",
        CROSSLINEXYZ: "CrossLineXYZ",
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
        COLORCROSSLINE: "ColorCrossLine",
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

    shape = ShapeEnumField(default_value=33)
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
