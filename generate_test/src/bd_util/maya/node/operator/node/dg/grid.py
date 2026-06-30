# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.grid import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    FillerColorField,
    LineColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Grid(DG):
    __slots__ = ()

    NODE_TYPE = "grid"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    invert = BoolField()
    i = invert

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    colorGain = ColorGainField()
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField()
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField()
    ag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    defaultColor = DefaultColorField()
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

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

    fillerColor = FillerColorField()
    fc = fillerColor
    fillerColorR = fillerColor.fillerColorR
    fcr = fillerColorR
    fillerColorG = fillerColor.fillerColorG
    fcg = fillerColorG
    fillerColorB = fillerColor.fillerColorB
    fcb = fillerColorB

    lineColor = LineColorField()
    lc = lineColor
    lineColorR = lineColor.lineColorR
    lcr = lineColorR
    lineColorG = lineColor.lineColorG
    lcg = lineColorG
    lineColorB = lineColor.lineColorB
    lcb = lineColorB

    contrast = FloatField()
    c = contrast

    uWidth = FloatField()
    uw = uWidth

    vWidth = FloatField()
    vw = vWidth
