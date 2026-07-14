# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.channels import (
    InColorField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class Channels(DG):
    __slots__ = ()

    NODE_TYPE = "channels"

    inColor = InColorField(default_value=(0.30000001192092896, 0.30000001192092896, 0.30000001192092896))
    ic = inColor
    inColorR = inColor.inColorR
    icr = inColorR
    inColorG = inColor.inColorG
    icg = inColorG
    inColorB = inColor.inColorB
    icb = inColorB

    inAlpha = FloatField(default_value=1.0)
    ia = inAlpha

    channelR = ShortField(default_value=0, min_value=0, max_value=3)
    cr = channelR

    channelG = ShortField(default_value=1, min_value=0, max_value=3)
    cg = channelG

    channelB = ShortField(default_value=2, min_value=0, max_value=3)
    cb = channelB

    channelA = ShortField(default_value=3, min_value=0, max_value=3)
    ca = channelA

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
