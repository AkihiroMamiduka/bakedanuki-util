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
    _ca = colorA
    colorAR = colorA.colorAR
    _car = colorAR
    colorAG = colorA.colorAG
    _cag = colorAG
    colorAB = colorA.colorAB
    _cab = colorAB

    colorB = ColorBField()
    _cb = colorB
    colorBR = colorB.colorBR
    _cbr = colorBR
    colorBG = colorB.colorBG
    _cbg = colorBG
    colorBB = colorB.colorBB
    _cbb = colorBB

    operation = LongField()
    _op = operation

    outBool = BoolField()
    ob = outBool
