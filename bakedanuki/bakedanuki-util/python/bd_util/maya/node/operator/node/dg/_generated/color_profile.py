# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_profile import (
    TransformField,
    WhitepointField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class ColorProfileTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10


class ColorProfileTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR_SRGB = 2
    SRGB = 3
    LINEAR_REC_709 = 4
    HDTV_REC_709 = 5
    CIE_XYZ = 10

    NAME_MAP = {
        LINEAR_SRGB: "Linear sRGB",
        SRGB: "sRGB",
        LINEAR_REC_709: "Linear Rec. 709",
        HDTV_REC_709: "HDTV (Rec. 709)",
        CIE_XYZ: "CIE XYZ",
    }


class ColorProfileTypeEnumField(
    EnumField[ColorProfileTypeEnumAttrOperator, ColorProfileTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorProfileTypeEnumAttrOperator
    PLUG_CLS = ColorProfileTypeEnumPlugOperator


class _GeneratedColorProfile(DG):
    __slots__ = ()

    NODE_TYPE = "colorProfile"

    colorProfileType = ColorProfileTypeEnumField(default_value=2)
    cpt = colorProfileType

    gamma = FloatField(default_value=1.0)
    gam = gamma

    gammaOffset = FloatField(default_value=0.0)
    gmo = gammaOffset

    forceGamma = BoolField(default_value=False)
    fga = forceGamma

    colorTemperature = LongField(default_value=0)
    tmp = colorTemperature

    whitepoint = WhitepointField(default_value=(0.0, 0.0, 0.0))
    wp = whitepoint
    whitepointR = whitepoint.whitepointR
    wpr = whitepointR
    whitepointG = whitepoint.whitepointG
    wpg = whitepointG
    whitepointB = whitepoint.whitepointB
    wpb = whitepointB

    intensity = FloatField(default_value=0.0)
    int = intensity

    transform = TransformField()
    tr = transform
    transformRow1 = transform.transformRow1
    tr1 = transformRow1
    transformRow2 = transform.transformRow2
    tr2 = transformRow2
    transformRow3 = transform.transformRow3
    tr3 = transformRow3
