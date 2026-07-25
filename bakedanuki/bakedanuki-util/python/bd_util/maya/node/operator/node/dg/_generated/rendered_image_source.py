# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.rendered_image_source import (
    OutColorField,
    OutSizeField,
    OutTransparencyField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedRenderedImageSource(DG):
    __slots__ = ()

    NODE_TYPE = "renderedImageSource"

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

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    camera = MessageField(readable=False)
    cam = camera

    renderLayer = MessageField(readable=False)
    lyr = renderLayer

    imageSource = MessageField(readable=False)
    ims = imageSource
