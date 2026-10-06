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
from .....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class ShapeEnumPlugOperator(EnumPlugOperator["ShapeEnumAttrOperator"]):
    __slots__ = ()

    SQUARE = 0
    CUBE = 1
    CIRCLE = 2
    CIRCLEARROW = 3


class ShapeEnumAttrOperator(EnumAttrOperator[ShapeEnumPlugOperator]):
    __slots__ = ()

    SQUARE = 0
    CUBE = 1
    CIRCLE = 2
    CIRCLEARROW = 3

    NAME_MAP = {
        SQUARE: "Square",
        CUBE: "Cube",
        CIRCLE: "Circle",
        CIRCLEARROW: "CircleArrow",
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

    shape = ShapeEnumField(default_value=0)
    sh = shape

    shape1stAxis = Shape1stAxisEnumField(default_value=4)
    s1a = shape1stAxis

    shape2ndAxis = Shape2ndAxisEnumField(default_value=2)
    s2a = shape2ndAxis

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

    shapeAxisOffsetLength = DoubleLinearField(default_value=1.0, min_value=0.0)
    saol = shapeAxisOffsetLength

    shapeAxisOffset = BoolField(default_value=False)
    sao = shapeAxisOffset

    shapeAxisOffsetDirection = ShapeAxisOffsetDirectionEnumField(
        default_value=0
    )
    saod = shapeAxisOffsetDirection

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

    showShapeOffsetLine = BoolField(default_value=False)
    ssol = showShapeOffsetLine

    shapeOffsetLineTemplate = BoolField(default_value=False)
    solt = shapeOffsetLineTemplate
