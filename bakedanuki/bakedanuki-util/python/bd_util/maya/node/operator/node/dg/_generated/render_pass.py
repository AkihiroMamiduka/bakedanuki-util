# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.render_pass import (
    BackupField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.dt.string import DataStringField


class GeneratedRenderPass(DG):
    __slots__ = ()

    NODE_TYPE = "renderPass"

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

    owner = MessageField(multi=True, readable=False)
    ow = owner

    passID = DataStringField()
    pid = passID

    renderable = BoolField(default_value=True)
    r = renderable

    frameBufferType = LongField(default_value=2)
    fbt = frameBufferType

    numChannels = ShortField(default_value=3)
    nc = numChannels

    filtering = BoolField(default_value=True)
    flt = filtering

    passGroupName = DataStringField()
    pgn = passGroupName

    backup = BackupField(multi=True, readable=False, writable=False)
    bak = backup

    colorProfile = LongField(default_value=0)
    cp = colorProfile
