# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.premultiply import (
    InColorField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Premultiply(DG):
    __slots__ = ()

    NODE_TYPE = "premultiply"

    inColor = InColorField()
    _c = inColor
    inColorR = inColor.inColorR
    _cr = inColorR
    inColorG = inColor.inColorG
    _cg = inColorG
    inColorB = inColor.inColorB
    _cb = inColorB

    inAlpha = FloatField()
    _a = inAlpha

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
