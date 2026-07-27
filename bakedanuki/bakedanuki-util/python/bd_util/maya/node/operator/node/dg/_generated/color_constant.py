# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_constant import (
    InColorField,
    OutColorField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedColorConstant(DG):
    __slots__ = ()

    NODE_TYPE = "colorConstant"

    inColor = InColorField(default_value=(0.30000001192092896, 0.30000001192092896, 0.30000001192092896))
    c = inColor
    inColorR = inColor.inColorR
    cr = inColorR
    inColorG = inColor.inColorG
    cg = inColorG
    inColorB = inColor.inColorB
    cb = inColorB

    inAlpha = FloatField(default_value=1.0)
    a = inAlpha

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
