# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.color_correct import (
    ColClampMaxField,
    ColClampMinField,
    ColGainField,
    ColGammaField,
    ColOffsetField,
    InColorField,
    OutColorField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "colorCorrect"

    inColor = InColorField(default_value=(0.30000001192092896, 0.30000001192092896, 0.30000001192092896))
    c = inColor
    inColorR = inColor.inColorR
    cr = inColorR
    inColorG = inColor.inColorG
    cg = inColorG
    inColorB = inColor.inColorB
    cb = inColorB

    inAlpha = FloatField(default_value=1.0)
    a = inAlpha

    unpremultiplyInput = BoolField(default_value=False)
    up = unpremultiplyInput

    premultiplyResult = BoolField(default_value=False)
    pr = premultiplyResult

    hueShift = FloatField(default_value=0.0, min_value=0.0, soft_max_value=360.0)
    hs = hueShift

    satGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    sg = satGain

    valGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    vg = valGain

    colGain = ColGainField(default_value=(1.0, 1.0, 1.0))
    ccg = colGain
    colGainR = colGain.colGainR
    ccgr = colGainR
    colGainG = colGain.colGainG
    ccgg = colGainG
    colGainB = colGain.colGainB
    ccgb = colGainB

    colOffset = ColOffsetField(default_value=(0.0, 0.0, 0.0))
    co = colOffset
    colOffsetR = colOffset.colOffsetR
    cor = colOffsetR
    colOffsetG = colOffset.colOffsetG
    cog = colOffsetG
    colOffsetB = colOffset.colOffsetB
    cob = colOffsetB

    colGamma = ColGammaField(default_value=(1.0, 1.0, 1.0))
    cga = colGamma
    colGammaX = colGamma.colGammaX
    cgax = colGammaX
    colGammaY = colGamma.colGammaY
    cgay = colGammaY
    colGammaZ = colGamma.colGammaZ
    cgaz = colGammaZ

    colClamp = BoolField(default_value=False)
    ccmp = colClamp

    colClampMin = ColClampMinField(default_value=(0.0, 0.0, 0.0))
    ccmn = colClampMin
    colClampMinR = colClampMin.colClampMinR
    ccmnr = colClampMinR
    colClampMinG = colClampMin.colClampMinG
    ccmng = colClampMinG
    colClampMinB = colClampMin.colClampMinB
    ccmnb = colClampMinB

    colClampMax = ColClampMaxField(default_value=(1.0, 1.0, 1.0))
    ccmx = colClampMax
    colClampMaxR = colClampMax.colClampMaxR
    ccmxr = colClampMaxR
    colClampMaxG = colClampMax.colClampMaxG
    ccmxg = colClampMaxG
    colClampMaxB = colClampMax.colClampMaxB
    ccmxb = colClampMaxB

    alphaGain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    aag = alphaGain

    alphaOffset = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    ao = alphaOffset

    alphaGamma = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)
    agg = alphaGamma

    alphaClamp = BoolField(default_value=False)
    acmp = alphaClamp

    alphaClampMin = FloatField(default_value=0.0)
    acmn = alphaClampMin

    alphaClampMax = FloatField(default_value=1.0)
    acmx = alphaClampMax

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
