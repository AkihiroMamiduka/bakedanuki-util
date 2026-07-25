# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_logic import (
    ColorAField,
    ColorBField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedColorLogic(DG):
    __slots__ = ()

    NODE_TYPE = "colorLogic"

    colorA = ColorAField(default_value=(1.0, 0.0, 0.5))
    ca = colorA
    colorAR = colorA.colorAR
    car = colorAR
    colorAG = colorA.colorAG
    cag = colorAG
    colorAB = colorA.colorAB
    cab = colorAB

    colorB = ColorBField(default_value=(1.0, 0.0, 0.5))
    cb = colorB
    colorBR = colorB.colorBR
    cbr = colorBR
    colorBG = colorB.colorBG
    cbg = colorBG
    colorBB = colorB.colorBB
    cbb = colorBB

    operation = LongField(default_value=0)
    op = operation

    outBool = BoolField(default_value=False, writable=False)
    ob = outBool
