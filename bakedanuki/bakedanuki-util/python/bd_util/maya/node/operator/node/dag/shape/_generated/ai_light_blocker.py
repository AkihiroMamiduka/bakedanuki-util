# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.ai_light_blocker import (
    CompInstObjGroupsField,
    ComponentTagsField,
    LocalPositionField,
    LocalScaleField,
    ShaderField,
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


class GeometryTypeEnumPlugOperator(
    EnumPlugOperator["GeometryTypeEnumAttrOperator"]
):
    __slots__ = ()

    BOX = 0
    SPHERE = 1
    PLANE = 2
    CYLINDER = 3


class GeometryTypeEnumAttrOperator(
    EnumAttrOperator[GeometryTypeEnumPlugOperator]
):
    __slots__ = ()

    BOX = 0
    SPHERE = 1
    PLANE = 2
    CYLINDER = 3

    NAME_MAP = {
        BOX: "box",
        SPHERE: "sphere",
        PLANE: "plane",
        CYLINDER: "cylinder",
    }


class GeometryTypeEnumField(
    EnumField[GeometryTypeEnumAttrOperator, GeometryTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeometryTypeEnumAttrOperator
    PLUG_CLS = GeometryTypeEnumPlugOperator


class RampAxisEnumPlugOperator(EnumPlugOperator["RampAxisEnumAttrOperator"]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class RampAxisEnumAttrOperator(EnumAttrOperator[RampAxisEnumPlugOperator]):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "x",
        Y: "y",
        Z: "z",
    }


class RampAxisEnumField(
    EnumField[RampAxisEnumAttrOperator, RampAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampAxisEnumAttrOperator
    PLUG_CLS = RampAxisEnumPlugOperator


class GeneratedAiLightBlocker(Shape):
    __slots__ = ()

    NODE_TYPE = "aiLightBlocker"

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

    geometryType = GeometryTypeEnumField(default_value=0)
    geometry_type = geometryType

    density = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    dens = density

    shader = ShaderField(default_value=(0.0, 0.0, 0.0))
    shad = shader
    shaderR = shader.shaderR
    shadr = shaderR
    shaderG = shader.shaderG
    shadg = shaderG
    shaderB = shader.shaderB
    shadb = shaderB

    roundness = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    rnds = roundness

    widthEdge = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    width_edge = widthEdge

    heightEdge = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    height_edge = heightEdge

    ramp = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    rmp = ramp

    rampAxis = RampAxisEnumField(default_value=0)
    ramp_axis = rampAxis
