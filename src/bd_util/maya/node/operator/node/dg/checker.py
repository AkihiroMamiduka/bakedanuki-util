# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.checker import (
    Color1Field,
    Color2Field,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Checker(DG):
    __slots__ = ()

    NODE_TYPE = "checker"

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

    color1 = Color1Field()
    c1 = color1
    color1R = color1.color1R
    c1r = color1R
    color1G = color1.color1G
    c1g = color1G
    color1B = color1.color1B
    c1b = color1B

    color2 = Color2Field()
    c2 = color2
    color2R = color2.color2R
    c2r = color2R
    color2G = color2.color2G
    c2g = color2G
    color2B = color2.color2B
    c2b = color2B

    contrast = FloatField()
    ct = contrast
