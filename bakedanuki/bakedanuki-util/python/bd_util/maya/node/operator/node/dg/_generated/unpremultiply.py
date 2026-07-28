# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.unpremultiply import (
    InColorField,
    OutColorField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedUnpremultiply(DG):
    __slots__ = ()

    NODE_TYPE = "unpremultiply"

    inColor = InColorField(default_value=(1.0, 0.0, 0.5))
    c = inColor
    inColorR = inColor.inColorR
    cr = inColorR
    inColorG = inColor.inColorG
    cg = inColorG
    inColorB = inColor.inColorB
    cb = inColorB

    inAlpha = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
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
