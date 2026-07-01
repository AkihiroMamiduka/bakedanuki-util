# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.render_pass import (
    BackupField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.dt.string import DataStringField


class RenderPass(DG):
    __slots__ = ()

    NODE_TYPE = "renderPass"

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

    owner = MessageField(multi=True)
    ow = owner

    passID = DataStringField()
    pid = passID

    renderable = BoolField()
    r = renderable

    frameBufferType = LongField()
    fbt = frameBufferType

    numChannels = ShortField()
    nc = numChannels

    filtering = BoolField()
    flt = filtering

    passGroupName = DataStringField()
    pgn = passGroupName

    backup = BackupField(multi=True)
    bak = backup

    colorProfile = LongField()
    cp = colorProfile
