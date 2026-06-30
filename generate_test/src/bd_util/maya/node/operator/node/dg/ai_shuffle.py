# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_shuffle import (
    ColorField,
    OutColorField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ChannelREnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3


class ChannelREnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3

    NAME_MAP = {
        R: "R",
        G: "G",
        B: "B",
        A: "A",
    }


class ChannelREnumField(
    EnumField[ChannelREnumAttrOperator, ChannelREnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChannelREnumAttrOperator
    PLUG_CLS = ChannelREnumPlugOperator


class ChannelGEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3


class ChannelGEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3

    NAME_MAP = {
        R: "R",
        G: "G",
        B: "B",
        A: "A",
    }


class ChannelGEnumField(
    EnumField[ChannelGEnumAttrOperator, ChannelGEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChannelGEnumAttrOperator
    PLUG_CLS = ChannelGEnumPlugOperator


class ChannelBEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3


class ChannelBEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3

    NAME_MAP = {
        R: "R",
        G: "G",
        B: "B",
        A: "A",
    }


class ChannelBEnumField(
    EnumField[ChannelBEnumAttrOperator, ChannelBEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChannelBEnumAttrOperator
    PLUG_CLS = ChannelBEnumPlugOperator


class ChannelAEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3


class ChannelAEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    R = 0
    G = 1
    B = 2
    A = 3

    NAME_MAP = {
        R: "R",
        G: "G",
        B: "B",
        A: "A",
    }


class ChannelAEnumField(
    EnumField[ChannelAEnumAttrOperator, ChannelAEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChannelAEnumAttrOperator
    PLUG_CLS = ChannelAEnumPlugOperator


class AiShuffle(DG):
    __slots__ = ()

    NODE_TYPE = "aiShuffle"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField()
    outa = outAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    color = ColorField()
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    alpha = FloatField()

    channelR = ChannelREnumField()
    channel_r = channelR

    channelG = ChannelGEnumField()
    channel_g = channelG

    channelB = ChannelBEnumField()
    channel_b = channelB

    channelA = ChannelAEnumField()
    channel_a = channelA

    negateR = BoolField()
    negate_r = negateR

    negateG = BoolField()
    negate_g = negateG

    negateB = BoolField()
    negate_b = negateB

    negateA = BoolField()
    negate_a = negateA
