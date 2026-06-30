# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.stencil import (
    ColorGainField,
    ColorKeyField,
    ColorOffsetField,
    DefaultColorField,
    ImageField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class Stencil(DG):
    __slots__ = ()

    NODE_TYPE = "stencil"

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

    image = ImageField()
    im = image
    imageR = image.imageR
    imr = imageR
    imageG = image.imageG
    img = imageG
    imageB = image.imageB
    imb = imageB

    mask = FloatField()
    m = mask

    edgeBlend = FloatField()
    eb = edgeBlend

    keyMasking = BoolField()
    km = keyMasking

    positiveKey = BoolField()
    pk = positiveKey

    colorKey = ColorKeyField()
    ck = colorKey
    colorKeyR = colorKey.colorKeyR
    ckr = colorKeyR
    colorKeyG = colorKey.colorKeyG
    ckg = colorKeyG
    colorKeyB = colorKey.colorKeyB
    ckb = colorKeyB

    hueRange = FloatField()
    hr = hueRange

    saturationRange = FloatField()
    sr = saturationRange

    valueRange = FloatField()
    vr = valueRange

    threshold = FloatField()
    th = threshold
