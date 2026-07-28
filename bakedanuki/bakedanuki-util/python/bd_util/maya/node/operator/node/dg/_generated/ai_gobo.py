# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_gobo import (
    OffsetField,
    OutColorField,
    OutTransparencyField,
    SlidemapField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class FilterModeEnumPlugOperator(EnumPlugOperator["FilterModeEnumAttrOperator"]):
    __slots__ = ()

    BLEND = 0
    REPLACE = 1
    ADD = 2
    SUB = 3
    MIX = 4


class FilterModeEnumAttrOperator(EnumAttrOperator[FilterModeEnumPlugOperator]):
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


class SwrapEnumPlugOperator(EnumPlugOperator["SwrapEnumAttrOperator"]):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4


class SwrapEnumAttrOperator(EnumAttrOperator[SwrapEnumPlugOperator]):
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


class TwrapEnumPlugOperator(EnumPlugOperator["TwrapEnumAttrOperator"]):
    __slots__ = ()

    PERIODIC = 0
    BLACK = 1
    CLAMP = 2
    MIRROR = 3
    FILE = 4


class TwrapEnumAttrOperator(EnumAttrOperator[TwrapEnumPlugOperator]):
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


class GeneratedAiGobo(DG):
    __slots__ = ()

    NODE_TYPE = "aiGobo"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    slidemap = SlidemapField(default_value=(1.0, 1.0, 1.0))
    slidemapR = slidemap.slidemapR
    slidemapr = slidemapR
    slidemapG = slidemap.slidemapG
    slidemapg = slidemapG
    slidemapB = slidemap.slidemapB
    slidemapb = slidemapB

    rotate = FloatField(multi=True, default_value=0.0, min_value=0.0, max_value=360.0)

    offset = OffsetField(default_value=(0.0, 0.0))
    offsetX = offset.offsetX
    offsetx = offsetX
    offsetY = offset.offsetY
    offsety = offsetY

    density = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    filterMode = FilterModeEnumField(default_value=0)
    filter_mode = filterMode

    swrap = SwrapEnumField(default_value=2)

    twrap = TwrapEnumField(default_value=2)

    sscale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1000.0)

    tscale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1000.0)
