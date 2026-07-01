# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.water import (
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
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class Water(DG):
    __slots__ = ()

    NODE_TYPE = "water"

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

    numberOfWaves = ShortField()
    nw = numberOfWaves

    waveTime = FloatField()
    wt = waveTime

    waveVelocity = FloatField()
    wv = waveVelocity

    waveAmplitude = FloatField()
    wa = waveAmplitude

    waveFrequency = FloatField()
    wf = waveFrequency

    subWaveFrequency = FloatField()
    swf = subWaveFrequency

    smoothness = FloatField()
    s = smoothness

    windUV = WindUVField()
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    rippleTime = FloatField()
    rt = rippleTime

    rippleFrequency = FloatField()
    rf = rippleFrequency

    rippleAmplitude = FloatField()
    ra = rippleAmplitude

    dropSize = FloatField()
    ds = dropSize

    rippleOrigin = RippleOriginField()
    rc = rippleOrigin
    rippleOriginU = rippleOrigin.rippleOriginU
    rcu = rippleOriginU
    rippleOriginV = rippleOrigin.rippleOriginV
    rcv = rippleOriginV

    groupVelocity = FloatField()
    gv = groupVelocity

    phaseVelocity = FloatField()
    pv = phaseVelocity

    spreadStart = FloatField()
    ss = spreadStart

    spreadRate = FloatField()
    sr = spreadRate

    reflectionBox = BoolField()
    rb = reflectionBox

    boxMin = BoxMinField()
    bmn = boxMin
    boxMinU = boxMin.boxMinU
    bu1 = boxMinU
    boxMinV = boxMin.boxMinV
    bv1 = boxMinV

    boxMax = BoxMaxField()
    bmx = boxMax
    boxMaxU = boxMax.boxMaxU
    bu2 = boxMaxU
    boxMaxV = boxMax.boxMaxV
    bv2 = boxMaxV

    fast = BoolField()
    fa = fast
