# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ramp import (
    ColorEntryListField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    V_RAMP = 0
    U_RAMP = 1
    DIAGONAL_RAMP = 2
    RADIAL_RAMP = 3
    CIRCULAR_RAMP = 4
    BOX_RAMP = 5
    UV_RAMP = 6
    FOUR_CORNER_RAMP = 7
    TARTAN_RAMP = 8


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    V_RAMP = 0
    U_RAMP = 1
    DIAGONAL_RAMP = 2
    RADIAL_RAMP = 3
    CIRCULAR_RAMP = 4
    BOX_RAMP = 5
    UV_RAMP = 6
    FOUR_CORNER_RAMP = 7
    TARTAN_RAMP = 8

    NAME_MAP = {
        V_RAMP: "V Ramp",
        U_RAMP: "U Ramp",
        DIAGONAL_RAMP: "Diagonal Ramp",
        RADIAL_RAMP: "Radial Ramp",
        CIRCULAR_RAMP: "Circular Ramp",
        BOX_RAMP: "Box Ramp",
        UV_RAMP: "UV Ramp",
        FOUR_CORNER_RAMP: "Four Corner Ramp",
        TARTAN_RAMP: "Tartan Ramp",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class InterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL_UP = 2
    EXPONENTIAL_DOWN = 3
    SMOOTH = 4
    BUMP = 5
    SPIKE = 6


class InterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    EXPONENTIAL_UP = 2
    EXPONENTIAL_DOWN = 3
    SMOOTH = 4
    BUMP = 5
    SPIKE = 6

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        EXPONENTIAL_UP: "Exponential Up",
        EXPONENTIAL_DOWN: "Exponential Down",
        SMOOTH: "Smooth",
        BUMP: "Bump",
        SPIKE: "Spike",
    }


class InterpolationEnumField(
    EnumField[InterpolationEnumAttrOperator, InterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolationEnumAttrOperator
    PLUG_CLS = InterpolationEnumPlugOperator


class _GeneratedRamp(DG):
    __slots__ = ()

    NODE_TYPE = "ramp"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    type = TypeEnumField(default_value=0)
    t = type

    interpolation = InterpolationEnumField(default_value=1)
    in_ = interpolation

    colorEntryList = ColorEntryListField(multi=True)
    cel = colorEntryList

    colorR = FloatField()
    ecr = colorR

    colorG = FloatField()
    ecg = colorG

    colorB = FloatField()
    ecb = colorB

    uWave = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    uw = uWave

    vWave = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    vw = vWave

    noise = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    n = noise

    noiseFreq = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    nf = noiseFreq

    hueNoise = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    hn = hueNoise

    satNoise = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    sn = satNoise

    valNoise = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    vn = valNoise

    hueNoiseFreq = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    hnf = hueNoiseFreq

    satNoiseFreq = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    snf = satNoiseFreq

    valNoiseFreq = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    vnf = valNoiseFreq

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiCurveImplicitUvs = BoolField(default_value=True, category="arnold")
    ai_curve_implicit_uvs = aiCurveImplicitUvs
