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

    scale = FloatField(default_value=6.0, min_value=0.0, soft_max_value=10.0)
    s = scale

    amplitude = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    a = amplitude

    threshold = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tr = threshold

    ratio = FloatField(default_value=0.7070000171661377, min_value=0.0, soft_max_value=1.0)
    ra = ratio

    octaves = ShortField(default_value=3, min_value=1, soft_max_value=10)
    ov = octaves

    frequency = FloatField(default_value=2.0, min_value=0.0, soft_max_value=10.0)
    fq = frequency

    frequencyRatio = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    fr = frequencyRatio

    distortionU = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    ud = distortionU

    distortionV = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    vd = distortionV

    distortionRatio = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    dr = distortionRatio

    gamma = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)
    ga = gamma

    noiseType = ShortField(default_value=0, min_value=0, max_value=2)
    nt = noiseType

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
