# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.cpv_color import OutColorField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedCpvColor(DG):
    __slots__ = ()

    NODE_TYPE = "cpvColor"

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

    outOpacity = FloatField(default_value=0.0, writable=False)
    oo = outOpacity
