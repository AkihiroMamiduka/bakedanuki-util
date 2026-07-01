# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.render_target import (
    ColorField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class FrameBufferTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _8_MINUS_BIT_INTEGER_UNSIGNED = 0
    _16_MINUS_BIT_INTEGER_UNSIGNED = 1
    _16_MINUS_BIT_FLOAT = 2
    _32_MINUS_BIT_FLOAT = 3


class FrameBufferTypeEnumAttrOperator(EnumAttrOperator):
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


class NumberOfChannelsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _1 = 1
    _3 = 3
    _4 = 4


class NumberOfChannelsEnumAttrOperator(EnumAttrOperator):
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
    EnumField[NumberOfChannelsEnumAttrOperator, NumberOfChannelsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NumberOfChannelsEnumAttrOperator
    PLUG_CLS = NumberOfChannelsEnumPlugOperator


class RenderTarget(DG):
    __slots__ = ()

    NODE_TYPE = "renderTarget"

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

    outSize = OutSizeField()
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField()
    fha = fileHasAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    renderLayer = MessageField()
    rl = renderLayer

    color = ColorField()
    col = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    alpha = FloatField()
    a = alpha

    renderable = BoolField()
    r = renderable

    renderingOverride = BoolField()
    reno = renderingOverride

    renderer = DataStringField()
    rdr = renderer

    colorProfile = LongField()
    cp = colorProfile

    frameBufferOverride = BoolField()
    fbo = frameBufferOverride

    frameBufferType = FrameBufferTypeEnumField()
    fbt = frameBufferType

    numberOfChannels = NumberOfChannelsEnumField()
    nc = numberOfChannels

    resolutionOverride = BoolField()
    reso = resolutionOverride

    width = LongField()
    w = width

    height = LongField()
    h = height

    camera = MessageField()
    cam = camera
