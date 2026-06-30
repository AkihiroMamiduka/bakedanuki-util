# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_composite import (
    ColorAField,
    ColorBField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class ColorComposite(DG):
    __slots__ = ()

    NODE_TYPE = "colorComposite"

    colorA = ColorAField()
    _ca = colorA
    colorAR = colorA.colorAR
    _car = colorAR
    colorAG = colorA.colorAG
    _cag = colorAG
    colorAB = colorA.colorAB
    _cab = colorAB

    alphaA = FloatField()
    _aa = alphaA

    colorB = ColorBField()
    _cb = colorB
    colorBR = colorB.colorBR
    _cbr = colorBR
    colorBG = colorB.colorBG
    _cbg = colorBG
    colorBB = colorB.colorBB
    _cbb = colorBB

    alphaB = FloatField()
    _ab = alphaB

    operation = ShortField()
    _op = operation

    factor = FloatField()
    _fx = factor

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
