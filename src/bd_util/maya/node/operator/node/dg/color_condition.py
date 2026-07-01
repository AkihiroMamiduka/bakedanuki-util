# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_condition import (
    ColorAField,
    ColorBField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorCondition(DG):
    __slots__ = ()

    NODE_TYPE = "colorCondition"

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

    condition = BoolField()
    cnd = condition

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
