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
    _ic = inColor
    inColorR = inColor.inColorR
    _icr = inColorR
    inColorG = inColor.inColorG
    _icg = inColorG
    inColorB = inColor.inColorB
    _icb = inColorB

    inAlpha = FloatField()
    _ia = inAlpha

    channelR = ShortField()
    _cr = channelR

    channelG = ShortField()
    _cg = channelG

    channelB = ShortField()
    _cb = channelB

    channelA = ShortField()
    _ca = channelA

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
