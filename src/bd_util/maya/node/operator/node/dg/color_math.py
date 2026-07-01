# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_math import (
    ColorAField,
    ColorBField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ColorMath(DG):
    __slots__ = ()

    NODE_TYPE = "colorMath"

    colorA = ColorAField()
    ca = colorA
    colorAR = colorA.colorAR
    car = colorAR
    colorAG = colorA.colorAG
    cag = colorAG
    colorAB = colorA.colorAB
    cab = colorAB

    alphaA = FloatField()
    aa = alphaA

    colorB = ColorBField()
    cb = colorB
    colorBR = colorB.colorBR
    cbr = colorBR
    colorBG = colorB.colorBG
    cbg = colorBG
    colorBB = colorB.colorBB
    cbb = colorBB

    alphaB = FloatField()
    ab = alphaB

    operation = LongField()
    cnd = operation

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
