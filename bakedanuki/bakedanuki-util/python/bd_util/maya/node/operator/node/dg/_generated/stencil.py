# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.stencil import (
    ColorGainField,
    ColorKeyField,
    ColorOffsetField,
    DefaultColorField,
    ImageField,
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedStencil(DG):
    __slots__ = ()

    NODE_TYPE = "stencil"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

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

    image = ImageField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    im = image
    imageR = image.imageR
    imr = imageR
    imageG = image.imageG
    img = imageG
    imageB = image.imageB
    imb = imageB

    mask = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    m = mask

    edgeBlend = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    eb = edgeBlend

    keyMasking = BoolField(default_value=False)
    km = keyMasking

    positiveKey = BoolField(default_value=False)
    pk = positiveKey

    colorKey = ColorKeyField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    ck = colorKey
    colorKeyR = colorKey.colorKeyR
    ckr = colorKeyR
    colorKeyG = colorKey.colorKeyG
    ckg = colorKeyG
    colorKeyB = colorKey.colorKeyB
    ckb = colorKeyB

    hueRange = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    hr = hueRange

    saturationRange = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    sr = saturationRange

    valueRange = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    vr = valueRange

    threshold = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    th = threshold
