# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_logic import (
    ColorAField,
    ColorBField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class ColorLogic(DG):
    __slots__ = ()

    NODE_TYPE = "colorLogic"

    colorA = ColorAField()
    ca = colorA
    colorAR = colorA.colorAR
    car = colorAR
    colorAG = colorA.colorAG
    cag = colorAG
    colorAB = colorA.colorAB
    cab = colorAB

    colorB = ColorBField()
    cb = colorB
    colorBR = colorB.colorBR
    cbr = colorBR
    colorBG = colorB.colorBG
    cbg = colorBG
    colorBB = colorB.colorBB
    cbb = colorBB

    operation = LongField()
    op = operation

    outBool = BoolField()
    ob = outBool
