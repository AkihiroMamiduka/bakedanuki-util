# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.cpv_color import OutColorField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class CpvColor(DG):
    __slots__ = ()

    NODE_TYPE = "cpvColor"

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

    outOpacity = FloatField()
    oo = outOpacity
