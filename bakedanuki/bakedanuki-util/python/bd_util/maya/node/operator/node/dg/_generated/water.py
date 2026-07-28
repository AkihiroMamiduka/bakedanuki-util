# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.water import (
    BoxMaxField,
    BoxMinField,
    ColorGainField,
    ColorOffsetField,
    DefaultColorField,
    OutColorField,
    RippleOriginField,
    UvCoordField,
    UvFilterSizeField,
    WindUVField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField


class GeneratedWater(DG):
    __slots__ = ()

    NODE_TYPE = "water"

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

    filter = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    f = filter

    filterOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(
        default_value=(1.0, 1.0, 1.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(
        default_value=(0.0, 0.0, 0.0),
        min_value=(0.0, 0.0, 0.0),
        max_value=(2.0, 2.0, 2.0),
    )
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ag = alphaGain

    alphaOffset = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    ao = alphaOffset

    defaultColor = DefaultColorField(
        default_value=(0.5, 0.5, 0.5),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
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

    numberOfWaves = ShortField(default_value=8, min_value=0, soft_max_value=32)
    nw = numberOfWaves

    waveTime = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    wt = waveTime

    waveVelocity = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=1.0
    )
    wv = waveVelocity

    waveAmplitude = FloatField(
        default_value=0.05000000074505806, min_value=0.0, soft_max_value=1.0
    )
    wa = waveAmplitude

    waveFrequency = FloatField(
        default_value=4.0, min_value=0.0, soft_max_value=20.0
    )
    wf = waveFrequency

    subWaveFrequency = FloatField(
        default_value=0.125, min_value=0.0, soft_max_value=1.0
    )
    swf = subWaveFrequency

    smoothness = FloatField(
        default_value=2.0, min_value=0.0, soft_max_value=5.0
    )
    s = smoothness

    windUV = WindUVField(
        default_value=(1.0, 0.0), min_value=(-1.0, -1.0), max_value=(1.0, 1.0)
    )
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    rippleTime = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    rt = rippleTime

    rippleFrequency = FloatField(
        default_value=25.0, min_value=0.0, soft_max_value=25.0
    )
    rf = rippleFrequency

    rippleAmplitude = FloatField(
        default_value=0.05000000074505806, min_value=0.0, soft_max_value=1.0
    )
    ra = rippleAmplitude

    dropSize = FloatField(
        default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0
    )
    ds = dropSize

    rippleOrigin = RippleOriginField(
        default_value=(0.5, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0)
    )
    rc = rippleOrigin
    rippleOriginU = rippleOrigin.rippleOriginU
    rcu = rippleOriginU
    rippleOriginV = rippleOrigin.rippleOriginV
    rcv = rippleOriginV

    groupVelocity = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )
    gv = groupVelocity

    phaseVelocity = FloatField(
        default_value=2.5, min_value=0.0, soft_max_value=10.0
    )
    pv = phaseVelocity

    spreadStart = FloatField(
        default_value=0.004999999888241291, min_value=0.0, soft_max_value=1.0
    )
    ss = spreadStart

    spreadRate = FloatField(
        default_value=0.30000001192092896, min_value=0.0, soft_max_value=1.0
    )
    sr = spreadRate

    reflectionBox = BoolField(default_value=False)
    rb = reflectionBox

    boxMin = BoxMinField(
        default_value=(0.0, 0.0), min_value=(-1.0, -1.0), max_value=(1.0, 1.0)
    )
    bmn = boxMin
    boxMinU = boxMin.boxMinU
    bu1 = boxMinU
    boxMinV = boxMin.boxMinV
    bv1 = boxMinV

    boxMax = BoxMaxField(
        default_value=(1.0, 1.0), min_value=(-1.0, -1.0), max_value=(1.0, 1.0)
    )
    bmx = boxMax
    boxMaxU = boxMax.boxMaxU
    bu2 = boxMaxU
    boxMaxV = boxMax.boxMaxV
    bv2 = boxMaxV

    fast = BoolField(default_value=True)
    fa = fast
