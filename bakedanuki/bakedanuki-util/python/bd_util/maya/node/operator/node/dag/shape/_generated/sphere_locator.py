# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.sphere_locator import (
    ColorField,
    CompInstObjGroupsField,
    ComponentTagsField,
    LocalPositionField,
    LocalScaleField,
    WorldPositionField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField


class FormatEnumPlugOperator(EnumPlugOperator["FormatEnumAttrOperator"]):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2


class FormatEnumAttrOperator(EnumAttrOperator[FormatEnumPlugOperator]):
    __slots__ = ()

    MIRRORED_BALL = 0
    ANGULAR = 1
    LATLONG = 2

    NAME_MAP = {
        MIRRORED_BALL: "mirrored_ball",
        ANGULAR: "angular",
        LATLONG: "latlong",
    }


class FormatEnumField(
    EnumField[FormatEnumAttrOperator, FormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FormatEnumAttrOperator
    PLUG_CLS = FormatEnumPlugOperator


class SkyFacingEnumPlugOperator(EnumPlugOperator["SkyFacingEnumAttrOperator"]):
    __slots__ = ()

    FRONT = 0
    BACK = 1
    BOTH = 2


class SkyFacingEnumAttrOperator(EnumAttrOperator[SkyFacingEnumPlugOperator]):
    __slots__ = ()

    FRONT = 0
    BACK = 1
    BOTH = 2

    NAME_MAP = {
        FRONT: "front",
        BACK: "back",
        BOTH: "both",
    }


class SkyFacingEnumField(
    EnumField[SkyFacingEnumAttrOperator, SkyFacingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SkyFacingEnumAttrOperator
    PLUG_CLS = SkyFacingEnumPlugOperator


class SamplingEnumPlugOperator(EnumPlugOperator["SamplingEnumAttrOperator"]):
    __slots__ = ()

    LOW_64X64 = 0
    MEDIUM_128X128 = 1
    HIGH_256X256 = 2
    HIGHER_512X512 = 3
    ULTRA_1024X1024 = 4


class SamplingEnumAttrOperator(EnumAttrOperator[SamplingEnumPlugOperator]):
    __slots__ = ()

    LOW_64X64 = 0
    MEDIUM_128X128 = 1
    HIGH_256X256 = 2
    HIGHER_512X512 = 3
    ULTRA_1024X1024 = 4

    NAME_MAP = {
        LOW_64X64: "Low (64x64)",
        MEDIUM_128X128: "Medium (128x128)",
        HIGH_256X256: "High (256x256)",
        HIGHER_512X512: "Higher (512x512)",
        ULTRA_1024X1024: "Ultra (1024x1024)",
    }


class SamplingEnumField(
    EnumField[SamplingEnumAttrOperator, SamplingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SamplingEnumAttrOperator
    PLUG_CLS = SamplingEnumPlugOperator


class GeneratedSphereLocator(Shape):
    __slots__ = ()

    NODE_TYPE = "SphereLocator"

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

    color = ColorField(default_value=(1.0, 1.0, 1.0))
    sc = color
    colorR = color.colorR
    scr = colorR
    colorG = color.colorG
    scg = colorG
    colorB = color.colorB
    scb = colorB

    format = FormatEnumField(default_value=2)
    for_ = format

    skyRadius = FloatField(default_value=1000.0)
    gskrd = skyRadius

    skyFacing = SkyFacingEnumField(default_value=0)
    faci = skyFacing

    sampling = SamplingEnumField(default_value=2)
    spl = sampling

    hwtexalpha = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hwta = hwtexalpha
