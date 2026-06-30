# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mountain import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    RockColorField,
    SnowColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Mountain(DG):
    __slots__ = ()

    NODE_TYPE = "mountain"

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

    snowColor = SnowColorField()
    sc = snowColor
    snowColorR = snowColor.snowColorR
    scr = snowColorR
    snowColorG = snowColor.snowColorG
    scg = snowColorG
    snowColorB = snowColor.snowColorB
    scb = snowColorB

    rockColor = RockColorField()
    rc = rockColor
    rockColorR = rockColor.rockColorR
    rcr = rockColorR
    rockColorG = rockColor.rockColorG
    rcg = rockColorG
    rockColorB = rockColor.rockColorB
    rcb = rockColorB

    amplitude = FloatField()
    a = amplitude

    snowRoughness = FloatField()
    sr = snowRoughness

    rockRoughness = FloatField()
    rr = rockRoughness

    boundary = FloatField()
    bo = boundary

    snowAltitude = FloatField()
    sa = snowAltitude

    snowDropoff = FloatField()
    sd = snowDropoff

    snowSlope = FloatField()
    ss = snowSlope

    depthMax = FloatField()
    dmx = depthMax
