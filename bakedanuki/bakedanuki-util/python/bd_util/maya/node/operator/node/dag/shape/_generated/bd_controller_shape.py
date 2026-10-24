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
    WIDELINE = 2
    CROSSLINE1ST2ND = 3
    WIDECROSSLINE1ST2ND = 4
    CROSSLINE1ST3RD = 5
    WIDECROSSLINE1ST3RD = 6
    CROSSLINE2ND3RD = 7
    WIDECROSSLINE2ND3RD = 8
    CROSSLINE3AXIS = 9
    TRIANGLE = 10
    SQUARE = 11
    SQUARECROSSLINE = 12
    SQUARECROSSLINETEMPLATE = 13
    SQUARETEMPLATE = 14
    DIAMOND = 15
    CUBE = 16
    OCTAHEDRON = 17
    OCTAHEDRONARROW = 18
    CIRCLE = 19
    WIDECIRCLERADIAL = 20
    WIDECIRCLEAXIAL = 21
    SPHERE = 22
    CYLINDER = 23
    ARROW = 24
    PYRAMID = 25
    CONE = 26
    COLORCROSSLINE3AXIS = 27
    COLORCUBE = 28
    COLORCORNERCUBE = 29
    COLORSPHERE = 30
    COLORSPHERECROSSLINE = 31


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    LINE = 1
    WIDELINE = 2
    CROSSLINE1ST2ND = 3
    WIDECROSSLINE1ST2ND = 4
    CROSSLINE1ST3RD = 5
    WIDECROSSLINE1ST3RD = 6
    CROSSLINE2ND3RD = 7
    WIDECROSSLINE2ND3RD = 8
    CROSSLINE3AXIS = 9
    TRIANGLE = 10
    SQUARE = 11
    SQUARECROSSLINE = 12
    SQUARECROSSLINETEMPLATE = 13
    SQUARETEMPLATE = 14
    DIAMOND = 15
    CUBE = 16
    OCTAHEDRON = 17
    OCTAHEDRONARROW = 18
    CIRCLE = 19
    WIDECIRCLERADIAL = 20
    WIDECIRCLEAXIAL = 21
    SPHERE = 22
    CYLINDER = 23
    ARROW = 24
    PYRAMID = 25
    CONE = 26
    COLORCROSSLINE3AXIS = 27
    COLORCUBE = 28
    COLORCORNERCUBE = 29
    COLORSPHERE = 30
    COLORSPHERECROSSLINE = 31

    NAME_MAP = {
        GEAR: "Gear",
        LINE: "Line",
        WIDELINE: "WideLine",
        CROSSLINE1ST2ND: "CrossLine1st2nd",
        WIDECROSSLINE1ST2ND: "WideCrossLine1st2nd",
        CROSSLINE1ST3RD: "CrossLine1st3rd",
        WIDECROSSLINE1ST3RD: "WideCrossLine1st3rd",
        CROSSLINE2ND3RD: "CrossLine2nd3rd",
        WIDECROSSLINE2ND3RD: "WideCrossLine2nd3rd",
        CROSSLINE3AXIS: "CrossLine3Axis",
        TRIANGLE: "Triangle",
        SQUARE: "Square",
        SQUARECROSSLINE: "SquareCrossLine",
        SQUARECROSSLINETEMPLATE: "SquareCrossLineTemplate",
        SQUARETEMPLATE: "SquareTemplate",
        DIAMOND: "Diamond",
        CUBE: "Cube",
        OCTAHEDRON: "Octahedron",
        OCTAHEDRONARROW: "OctahedronArrow",
        CIRCLE: "Circle",
        WIDECIRCLERADIAL: "WideCircleRadial",
        WIDECIRCLEAXIAL: "WideCircleAxial",
        SPHERE: "Sphere",
        CYLINDER: "Cylinder",
        ARROW: "Arrow",
        PYRAMID: "Pyramid",
        CONE: "Cone",
        COLORCROSSLINE3AXIS: "ColorCrossLine3Axis",
        COLORCUBE: "ColorCube",
        COLORCORNERCUBE: "ColorCornerCube",
        COLORSPHERE: "ColorSphere",
        COLORSPHERECROSSLINE: "ColorSphereCrossLine",
    }


class ShapeEnumField(EnumField[ShapeEnumAttrOperator, ShapeEnumPlugOperator]):
    __slots__ = ()

    ATTR_CLS = ShapeEnumAttrOperator
    PLUG_CLS = ShapeEnumPlugOperator


class ShapePartShapeEnumPlugOperator(
    EnumPlugOperator["ShapePartShapeEnumAttrOperator"]
):
    __slots__ = ()

    ARROW2D = 0
    ARROW3D = 1
    TRIANGLE = 2
    SQUARE = 3
    DIAMOND = 4
    CIRCLE = 5
    CUBE = 6
    OCTAHEDRON = 7
    SPHERE = 8
    PYRAMID = 9
    CONE = 10


class ShapePartShapeEnumAttrOperator(
    EnumAttrOperator[ShapePartShapeEnumPlugOperator]
):
    __slots__ = ()

    ARROW2D = 0
    ARROW3D = 1
    TRIANGLE = 2
    SQUARE = 3
    DIAMOND = 4
    CIRCLE = 5
    CUBE = 6
    OCTAHEDRON = 7
    SPHERE = 8
    PYRAMID = 9
    CONE = 10

    NAME_MAP = {
        ARROW2D: "Arrow2D",
        ARROW3D: "Arrow3D",
        TRIANGLE: "Triangle",
        SQUARE: "Square",
        DIAMOND: "Diamond",
        CIRCLE: "Circle",
        CUBE: "Cube",
        OCTAHEDRON: "Octahedron",
        SPHERE: "Sphere",
        PYRAMID: "Pyramid",
        CONE: "Cone",
    }


class ShapePartShapeEnumField(
    EnumField[ShapePartShapeEnumAttrOperator, ShapePartShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapePartShapeEnumAttrOperator
    PLUG_CLS = ShapePartShapeEnumPlugOperator


class ShapePartTypeEnumPlugOperator(
    EnumPlugOperator["ShapePartTypeEnumAttrOperator"]
):
    __slots__ = ()

    ATEND = 0
    ATENDS = 1
    ATAPEX = 2


class ShapePartTypeEnumAttrOperator(
    EnumAttrOperator[ShapePartTypeEnumPlugOperator]
):
    __slots__ = ()

    ATEND = 0
    ATENDS = 1
    ATAPEX = 2

    NAME_MAP = {
        ATEND: "AtEnd",
        ATENDS: "AtEnds",
        ATAPEX: "AtApex",
    }


class ShapePartTypeEnumField(
    EnumField[ShapePartTypeEnumAttrOperator, ShapePartTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapePartTypeEnumAttrOperator
    PLUG_CLS = ShapePartTypeEnumPlugOperator


class ShapeFinTypeEnumPlugOperator(
    EnumPlugOperator["ShapeFinTypeEnumAttrOperator"]
):
    __slots__ = ()

    STANDARD = 0
    TAPERED = 1


class ShapeFinTypeEnumAttrOperator(
    EnumAttrOperator[ShapeFinTypeEnumPlugOperator]
):
    __slots__ = ()

    STANDARD = 0
    TAPERED = 1

    NAME_MAP = {
        STANDARD: "Standard",
        TAPERED: "Tapered",
    }


class ShapeFinTypeEnumField(
    EnumField[ShapeFinTypeEnumAttrOperator, ShapeFinTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShapeFinTypeEnumAttrOperator
    PLUG_CLS = ShapeFinTypeEnumPlugOperator


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

    shapeAnimationTransformMatrix = DataMatrixField()
    satm = shapeAnimationTransformMatrix

    shapeDrawOnTop = BoolField(default_value=False)
    sdot = shapeDrawOnTop

    shapeLineWidth = FloatField(default_value=1.0, min_value=1.0)
    slw = shapeLineWidth

    shapeLineTransparency = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    slt = shapeLineTransparency

    shapeFill = BoolField(default_value=False)
    sfl = shapeFill

    shapeFillTransparency = FloatField(
        default_value=0.8500000238418579, min_value=0.0, max_value=1.0
    )
    sftp = shapeFillTransparency

    shape = ShapeEnumField(default_value=16)
    sh = shape

    shapeWideWidth = DoubleLinearField(default_value=0.05, min_value=0.0)
    sww = shapeWideWidth

    shapeCircleAngle = DoubleAngleField(
        default_value=360.0, min_value=0.0, max_value=360.0
    )
    sca = shapeCircleAngle

    shapePart = BoolField(default_value=False)
    spt = shapePart

    shapePartShape = ShapePartShapeEnumField(default_value=0)
    spsh = shapePartShape

    shapePartType = ShapePartTypeEnumField(default_value=0)
    sptp = shapePartType

    shapePartOffset = DoubleLinearField(default_value=0.0)
    spo = shapePartOffset

    shapePartSize = DoubleField(default_value=1.0)
    sps = shapePartSize

    shapePartLengthScale = DoubleField(default_value=1.0)
    spls = shapePartLengthScale

    shapePartWidthScale = DoubleField(default_value=1.0)
    spws = shapePartWidthScale

    shapeFin = BoolField(default_value=False)
    sfn = shapeFin

    shapeFinType = ShapeFinTypeEnumField(default_value=0)
    sfnt = shapeFinType

    shapeFinHeight = DoubleLinearField(default_value=0.5)
    sfnh = shapeFinHeight

    shapeFinSize = DoubleField(default_value=1.0)
    sfns = shapeFinSize

    shapeFinWidthScale = DoubleField(default_value=1.0)
    sfnws = shapeFinWidthScale

    shapeOffsetLine = BoolField(default_value=False)
    sol = shapeOffsetLine

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
