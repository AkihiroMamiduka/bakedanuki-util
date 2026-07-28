# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.render_target import (
    ColorField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class FrameBufferTypeEnumPlugOperator(
    EnumPlugOperator["FrameBufferTypeEnumAttrOperator"]
):
    __slots__ = ()

    _8_MINUS_BIT_INTEGER_UNSIGNED = 0
    _16_MINUS_BIT_INTEGER_UNSIGNED = 1
    _16_MINUS_BIT_FLOAT = 2
    _32_MINUS_BIT_FLOAT = 3


class FrameBufferTypeEnumAttrOperator(
    EnumAttrOperator[FrameBufferTypeEnumPlugOperator]
):
    __slots__ = ()

    _8_MINUS_BIT_INTEGER_UNSIGNED = 0
    _16_MINUS_BIT_INTEGER_UNSIGNED = 1
    _16_MINUS_BIT_FLOAT = 2
    _32_MINUS_BIT_FLOAT = 3

    NAME_MAP = {
        _8_MINUS_BIT_INTEGER_UNSIGNED: "8-bit Integer (unsigned)",
        _16_MINUS_BIT_INTEGER_UNSIGNED: "16-bit Integer (unsigned)",
        _16_MINUS_BIT_FLOAT: "16-bit Float",
        _32_MINUS_BIT_FLOAT: "32-bit Float",
    }


class FrameBufferTypeEnumField(
    EnumField[FrameBufferTypeEnumAttrOperator, FrameBufferTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrameBufferTypeEnumAttrOperator
    PLUG_CLS = FrameBufferTypeEnumPlugOperator


class NumberOfChannelsEnumPlugOperator(
    EnumPlugOperator["NumberOfChannelsEnumAttrOperator"]
):
    __slots__ = ()

    _1 = 1
    _3 = 3
    _4 = 4


class NumberOfChannelsEnumAttrOperator(
    EnumAttrOperator[NumberOfChannelsEnumPlugOperator]
):
    __slots__ = ()

    _1 = 1
    _3 = 3
    _4 = 4

    NAME_MAP = {
        _1: "1",
        _3: "3",
        _4: "4",
    }


class NumberOfChannelsEnumField(
    EnumField[
        NumberOfChannelsEnumAttrOperator, NumberOfChannelsEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NumberOfChannelsEnumAttrOperator
    PLUG_CLS = NumberOfChannelsEnumPlugOperator


class GeneratedRenderTarget(DG):
    __slots__ = ()

    NODE_TYPE = "renderTarget"

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

    outSize = OutSizeField(default_value=(0.0, 0.0), writable=False)
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField(default_value=False, writable=False)
    fha = fileHasAlpha

    outTransparency = OutTransparencyField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    renderLayer = MessageField(readable=False)
    rl = renderLayer

    color = ColorField(default_value=(0.0, 0.0, 0.0))
    col = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    alpha = FloatField(default_value=0.0)
    a = alpha

    renderable = BoolField(default_value=True)
    r = renderable

    renderingOverride = BoolField(default_value=False)
    reno = renderingOverride

    renderer = DataStringField()
    rdr = renderer

    colorProfile = LongField(default_value=0)
    cp = colorProfile

    frameBufferOverride = BoolField(default_value=False)
    fbo = frameBufferOverride

    frameBufferType = FrameBufferTypeEnumField(default_value=0)
    fbt = frameBufferType

    numberOfChannels = NumberOfChannelsEnumField(default_value=3)
    nc = numberOfChannels

    resolutionOverride = BoolField(default_value=False)
    reso = resolutionOverride

    width = LongField(
        default_value=640, min_value=2, soft_min_value=128, soft_max_value=8192
    )
    w = width

    height = LongField(
        default_value=480, min_value=2, soft_min_value=128, soft_max_value=8192
    )
    h = height

    camera = MessageField(readable=False)
    cam = camera
