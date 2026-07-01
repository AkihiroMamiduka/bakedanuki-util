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

    inColor = InColorField()
    ic = inColor
    inColorR = inColor.inColorR
    icr = inColorR
    inColorG = inColor.inColorG
    icg = inColorG
    inColorB = inColor.inColorB
    icb = inColorB

    inAlpha = FloatField()
    ia = inAlpha

    channelR = ShortField()
    cr = channelR

    channelG = ShortField()
    cg = channelG

    channelB = ShortField()
    cb = channelB

    channelA = ShortField()
    ca = channelA

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
