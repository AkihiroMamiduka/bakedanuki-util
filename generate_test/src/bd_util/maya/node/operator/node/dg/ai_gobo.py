# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_gobo import (
    OffsetField,
    OutColorField,
    OutTransparencyField,
    SlidemapField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FilterModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLEND = 0
    REPLACE = 1
    ADD = 2
    SUB = 3
    MIX = 4


class FilterModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLEND = 0
    REPLACE = 1
    ADD = 2
    SUB = 3
    MIX = 4

    NAME_MAP = {
        BLEND: "blend",
        REPLACE: "replace",
        ADD: "add",
        SUB: "sub",
        MIX: "mix",
    }


class FilterModeEnumField(
    EnumField[FilterModeEnumAttrOperator, FilterModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterModeEnumAttrOperator
    PLUG_CLS = FilterModeEnumPlugOperator


class SwrapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4


class SwrapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4

    NAME_MAP = {
        PERIODIC: "periodic",
        BLACK: "black",
        CLAMP: "clamp",
        MIRROR: "mirror",
        FILE: "file",
    }


class SwrapEnumField(
    EnumField[SwrapEnumAttrOperator, SwrapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SwrapEnumAttrOperator
    PLUG_CLS = SwrapEnumPlugOperator


class TwrapEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4


class TwrapEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4

    NAME_MAP = {
        PERIODIC: "periodic",
        BLACK: "black",
        CLAMP: "clamp",
        MIRROR: "mirror",
        FILE: "file",
    }


class TwrapEnumField(
    EnumField[TwrapEnumAttrOperator, TwrapEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TwrapEnumAttrOperator
    PLUG_CLS = TwrapEnumPlugOperator


class AiGobo(DG):
    __slots__ = ()

    NODE_TYPE = "aiGobo"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    slidemap = SlidemapField()
    slidemapR = slidemap.slidemapR
    slidemapr = slidemapR
    slidemapG = slidemap.slidemapG
    slidemapg = slidemapG
    slidemapB = slidemap.slidemapB
    slidemapb = slidemapB

    rotate = FloatField(multi=True)

    offset = OffsetField()
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY

    density = FloatField()

    filterMode = FilterModeEnumField()
    filter_mode = filterMode

    swrap = SwrapEnumField()

    twrap = TwrapEnumField()

    sscale = FloatField()

    tscale = FloatField()
