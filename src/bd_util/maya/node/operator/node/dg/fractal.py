# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.fractal import (
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Fractal(DG):
    __slots__ = ()

    NODE_TYPE = "fractal"

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

    amplitude = FloatField()
    a = amplitude

    ratio = FloatField()
    ra = ratio

    threshold = FloatField()
    th = threshold

    levelMin = FloatField()
    lmn = levelMin

    levelMax = FloatField()
    lmx = levelMax

    frequencyRatio = FloatField()
    fr = frequencyRatio

    bias = FloatField()
    bs = bias

    inflection = BoolField()
    in_ = inflection

    animated = BoolField()
    an = animated

    timeRatio = FloatField()
    tr = timeRatio

    time = FloatField()
    ti = time
