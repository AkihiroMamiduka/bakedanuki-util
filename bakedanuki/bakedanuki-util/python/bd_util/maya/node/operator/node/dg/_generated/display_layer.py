# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.display_layer import DrawInfoField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.dt.string_array import DataStringArrayField


class _GeneratedDisplayLayer(DG):
    __slots__ = ()

    NODE_TYPE = "displayLayer"

    identification = ShortField(default_value=0)
    id = identification

    drawInfo = DrawInfoField()
    di = drawInfo
    displayType = drawInfo.displayType
    dt = displayType
    levelOfDetail = drawInfo.levelOfDetail
    lod = levelOfDetail
    shading = drawInfo.shading
    s = shading
    texturing = drawInfo.texturing
    t = texturing
    playback = drawInfo.playback
    p = playback
    enabled = drawInfo.enabled
    e = enabled
    visibility = drawInfo.visibility
    v = visibility
    hideOnPlayback = drawInfo.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawInfo.overrideRGBColors
    ovrgbf = overrideRGBColors
    color = drawInfo.color
    c = color
    overrideColorRGB = drawInfo.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawInfo.overrideColorA
    ovca = overrideColorA

    ufeMembers = DataStringArrayField()
    ufem = ufeMembers

    displayOrder = ShortField(default_value=0)
    do = displayOrder
