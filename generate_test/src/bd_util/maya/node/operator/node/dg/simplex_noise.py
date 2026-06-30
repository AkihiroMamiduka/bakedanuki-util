# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.simplex_noise import (
    OutColorField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class SimplexNoise(DG):
    __slots__ = ()

    NODE_TYPE = "simplexNoise"

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

    scale = FloatField()
    _s = scale

    amplitude = FloatField()
    a = amplitude

    threshold = FloatField()
    tr = threshold

    ratio = FloatField()
    ra = ratio

    octaves = ShortField()
    ov = octaves

    frequency = FloatField()
    fq = frequency

    frequencyRatio = FloatField()
    fr = frequencyRatio

    distortionU = FloatField()
    ud = distortionU

    distortionV = FloatField()
    vd = distortionV

    distortionRatio = FloatField()
    dr = distortionRatio

    gamma = FloatField()
    _ga = gamma

    noiseType = ShortField()
    nt = noiseType

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
