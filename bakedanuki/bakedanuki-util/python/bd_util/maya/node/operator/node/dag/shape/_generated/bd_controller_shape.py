# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.bd_controller_shape import (
    CompInstObjGroupsField,
    ComponentTagsField,
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


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    GEAR = 0
    LINE = 1
    CROSSLINE = 2
    TRIANGLE = 3
    SQUARE = 4
    DIAMOND = 5
    CIRCLE = 6
    ARCRADIAL = 7
    ARCAXIAL = 8
    CROSSARCRADIAL = 9
    CROSSARCAXIAL = 10
    CROSSLINE3AXIS = 11
    CUBE = 12
    OCTAHEDRON = 13
    OCTAHEDRONARROW = 14
    SPHERE = 15
    CYLINDER = 16
    ARROW = 17
    PYRAMID = 18
    CONE = 19
    COLORCROSSLINE3AXIS = 20
    COLORCUBE = 21
    COLORCORNERCUBE = 22
    COLORSPHERE = 23


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    GEAR = 0
    LINE = 1
    CROSSLINE = 2
    TRIANGLE = 3
    SQUARE = 4
    DIAMOND = 5
    CIRCLE = 6
    ARCRADIAL = 7
    ARCAXIAL = 8
    CROSSARCRADIAL = 9
    CROSSARCAXIAL = 10
    CROSSLINE3AXIS = 11
    CUBE = 12
    OCTAHEDRON = 13
    OCTAHEDRONARROW = 14
    SPHERE = 15
    CYLINDER = 16
    ARROW = 17
    PYRAMID = 18
    CONE = 19
    COLORCROSSLINE3AXIS = 20
    COLORCUBE = 21
    COLORCORNERCUBE = 22
    COLORSPHERE = 23

    NAME_MAP = {
        GEAR: "Gear",
        LINE: "Line",
        CROSSLINE: "CrossLine",
        TRIANGLE: "Triangle",
        SQUARE: "Square",
        DIAMOND: "Diamond",
        CIRCLE: "Circle",
        ARCRADIAL: "ArcRadial",
        ARCAXIAL: "ArcAxial",
        CROSSARCRADIAL: "CrossArcRadial",
        CROSSARCAXIAL: "CrossArcAxial",
        CROSSLINE3AXIS: "CrossLine3Axis",
        CUBE: "Cube",
        OCTAHEDRON: "Octahedron",
        OCTAHEDRONARROW: "OctahedronArrow",
        SPHERE: "Sphere",
        CYLINDER: "Cylinder",
        ARROW: "Arrow",
        PYRAMID: "Pyramid",
        CONE: "Cone",
        COLORCROSSLINE3AXIS: "ColorCrossLine3Axis",
        COLORCUBE: "ColorCube",
        COLORCORNERCUBE: "ColorCornerCube",
        COLORSPHERE: "ColorSphere",
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

    shape1stAxis = Shape1stAxisEnumField(default_value=0)
    s1a = shape1stAxis

    shape2ndAxis = Shape2ndAxisEnumField(default_value=2)
    s2a = shape2ndAxis

    shapeAxisSwap = BoolField(default_value=False)
    sasw = shapeAxisSwap

    shape = ShapeEnumField(default_value=12)
    sh = shape

    shapeBaseSpace1stAxisPlus = DoubleLinearField(default_value=0.5)
    sbsp1p = shapeBaseSpace1stAxisPlus

    shapeBaseSpace1stAxisMinus = DoubleLinearField(default_value=-0.5)
    sbsp1m = shapeBaseSpace1stAxisMinus

    shapeBaseSpace2ndAxisPlus = DoubleLinearField(default_value=0.5)
    sbsp2p = shapeBaseSpace2ndAxisPlus

    shapeBaseSpace2ndAxisMinus = DoubleLinearField(default_value=-0.5)
    sbsp2m = shapeBaseSpace2ndAxisMinus

    shapeBaseSpace3rdAxisPlus = DoubleLinearField(default_value=0.5)
    sbsp3p = shapeBaseSpace3rdAxisPlus

    shapeBaseSpace3rdAxisMinus = DoubleLinearField(default_value=-0.5)
    sbsp3m = shapeBaseSpace3rdAxisMinus

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

    shapeWide = BoolField(default_value=False)
    swd = shapeWide

    shapeWideWidth = DoubleLinearField(default_value=0.05, min_value=0.0)
    sww = shapeWideWidth

    shapeArcAngle = DoubleAngleField(
        default_value=180.0, min_value=0.0, max_value=360.0
    )
    saa = shapeArcAngle

    shapeTemplateLine = BoolField(default_value=False)
    stl = shapeTemplateLine

    shapeTemplateLineRate = DoubleField(
        default_value=0.7, min_value=0.0, max_value=1.0
    )
    stlr = shapeTemplateLineRate

    shapeTemplateLineInvert = BoolField(default_value=False)
    stli = shapeTemplateLineInvert

    shapeTemplateFill = BoolField(default_value=False)
    stf = shapeTemplateFill

    shapePartTemplate = BoolField(default_value=False)
    spte = shapePartTemplate

    shapeFinTemplate = BoolField(default_value=False)
    sft = shapeFinTemplate

    shapeGuideLineTemplate = BoolField(default_value=False)
    sglt = shapeGuideLineTemplate

    shapeOffsetLineTemplate = BoolField(default_value=False)
    solt = shapeOffsetLineTemplate

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

    shapePartPrimarySizeScale = DoubleField(default_value=1.0)
    sppss = shapePartPrimarySizeScale

    shapePartOtherSizeScale = DoubleField(default_value=0.5)
    sposs = shapePartOtherSizeScale

    shapePartLengthScale = DoubleField(default_value=1.0)
    spls = shapePartLengthScale

    shapePartWidthScale = DoubleField(default_value=1.0)
    spws = shapePartWidthScale

    shapePartHeightScale = DoubleField(default_value=1.0)
    sphs = shapePartHeightScale

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

    shapeGuideLine = BoolField(default_value=False)
    sgl = shapeGuideLine

    shapeOffsetLine = BoolField(default_value=False)
    sol = shapeOffsetLine

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

    customBoundsBaseSpaceXPlus = DoubleLinearField(default_value=0.5)
    cbbsxp = customBoundsBaseSpaceXPlus

    customBoundsBaseSpaceXMinus = DoubleLinearField(default_value=-0.5)
    cbbsxm = customBoundsBaseSpaceXMinus

    customBoundsBaseSpaceYPlus = DoubleLinearField(default_value=0.5)
    cbbsyp = customBoundsBaseSpaceYPlus

    customBoundsBaseSpaceYMinus = DoubleLinearField(default_value=-0.5)
    cbbsym = customBoundsBaseSpaceYMinus

    customBoundsBaseSpaceZPlus = DoubleLinearField(default_value=0.5)
    cbbszp = customBoundsBaseSpaceZPlus

    customBoundsBaseSpaceZMinus = DoubleLinearField(default_value=-0.5)
    cbbszm = customBoundsBaseSpaceZMinus
