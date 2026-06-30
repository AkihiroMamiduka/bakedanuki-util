# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ramp import (
    ColorEntryListField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


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


class Ramp(DG):
    __slots__ = ()

    NODE_TYPE = "ramp"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    invert = BoolField()
    i = invert

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    colorGain = ColorGainField()
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField()
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField()
    ag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    defaultColor = DefaultColorField()
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    type = TypeEnumField()
    t = type

    interpolation = InterpolationEnumField()
    in_ = interpolation

    colorEntryList = ColorEntryListField(multi=True)
    cel = colorEntryList

    # TODO: colorEntryList.colorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: colorEntryList.colorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: colorEntryList.colorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    uWave = FloatField()
    uw = uWave

    vWave = FloatField()
    vw = vWave

    noise = FloatField()
    n = noise

    noiseFreq = FloatField()
    nf = noiseFreq

    hueNoise = FloatField()
    hn = hueNoise

    satNoise = FloatField()
    sn = satNoise

    valNoise = FloatField()
    vn = valNoise

    hueNoiseFreq = FloatField()
    hnf = hueNoiseFreq

    satNoiseFreq = FloatField()
    snf = satNoiseFreq

    valNoiseFreq = FloatField()
    vnf = valNoiseFreq

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiCurveImplicitUvs = BoolField()
    ai_curve_implicit_uvs = aiCurveImplicitUvs
