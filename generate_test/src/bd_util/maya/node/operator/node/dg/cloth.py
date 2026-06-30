# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.cloth import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    GapColorField,
    OutColorField,
    UColorField,
    UvCoordField,
    UvFilterSizeField,
    VColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Cloth(DG):
    __slots__ = ()

    NODE_TYPE = "cloth"

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

    gapColor = GapColorField()
    gc = gapColor
    gapColorR = gapColor.gapColorR
    gcr = gapColorR
    gapColorG = gapColor.gapColorG
    gcg = gapColorG
    gapColorB = gapColor.gapColorB
    gcb = gapColorB

    uColor = UColorField()
    uc = uColor
    uColorR = uColor.uColorR
    ucr = uColorR
    uColorG = uColor.uColorG
    ucg = uColorG
    uColorB = uColor.uColorB
    ucb = uColorB

    vColor = VColorField()
    vc = vColor
    vColorR = vColor.vColorR
    vcr = vColorR
    vColorG = vColor.vColorG
    vcg = vColorG
    vColorB = vColor.vColorB
    vcb = vColorB

    uWidth = FloatField()
    uwi = uWidth

    vWidth = FloatField()
    vwi = vWidth

    uWave = FloatField()
    uwa = uWave

    vWave = FloatField()
    vwa = vWave

    randomness = FloatField()
    r = randomness

    widthSpread = FloatField()
    ws = widthSpread

    brightSpread = FloatField()
    bs = brightSpread
