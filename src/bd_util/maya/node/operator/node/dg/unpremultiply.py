# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.unpremultiply import (
    InColorField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Unpremultiply(DG):
    __slots__ = ()

    NODE_TYPE = "unpremultiply"

    inColor = InColorField()
    c = inColor
    inColorR = inColor.inColorR
    cr = inColorR
    inColorG = inColor.inColorG
    cg = inColorG
    inColorB = inColor.inColorB
    cb = inColorB

    inAlpha = FloatField()
    a = inAlpha

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
