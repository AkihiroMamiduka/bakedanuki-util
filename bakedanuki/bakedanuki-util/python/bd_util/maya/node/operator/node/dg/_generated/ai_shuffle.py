# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_shuffle import (
    ColorField,
    OutColorField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


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


class GeneratedAiShuffle(DG):
    __slots__ = ()

    NODE_TYPE = "aiShuffle"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    outa = outAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    color = ColorField(default_value=(0.0, 0.0, 0.0))
    colorR = color.colorR
    colorr = colorR
    colorG = color.colorG
    colorg = colorG
    colorB = color.colorB
    colorb = colorB

    alpha = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    channelR = ChannelREnumField(default_value=0)
    channel_r = channelR

    channelG = ChannelGEnumField(default_value=1)
    channel_g = channelG

    channelB = ChannelBEnumField(default_value=2)
    channel_b = channelB

    channelA = ChannelAEnumField(default_value=3)
    channel_a = channelA

    negateR = BoolField(default_value=False)
    negate_r = negateR

    negateG = BoolField(default_value=False)
    negate_g = negateG

    negateB = BoolField(default_value=False)
    negate_b = negateB

    negateA = BoolField(default_value=False)
    negate_a = negateA
