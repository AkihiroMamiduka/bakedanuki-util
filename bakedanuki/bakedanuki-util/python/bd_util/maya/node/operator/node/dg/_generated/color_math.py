# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_math import (
    ColorAField,
    ColorBField,
    OutColorField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedColorMath(DG):
    __slots__ = ()

    NODE_TYPE = "colorMath"

    colorA = ColorAField(default_value=(1.0, 0.0, 0.0))
    ca = colorA
    colorAR = colorA.colorAR
    car = colorAR
    colorAG = colorA.colorAG
    cag = colorAG
    colorAB = colorA.colorAB
    cab = colorAB

    alphaA = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    aa = alphaA

    colorB = ColorBField(default_value=(0.0, 1.0, 0.0))
    cb = colorB
    colorBR = colorB.colorBR
    cbr = colorBR
    colorBG = colorB.colorBG
    cbg = colorBG
    colorBB = colorB.colorBB
    cbb = colorBB

    alphaB = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ab = alphaB

    operation = LongField(default_value=0, min_value=0, max_value=8)
    cnd = operation

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
