# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.color_correct import (
    ColClampMaxField,
    ColClampMinField,
    ColGainField,
    ColGammaField,
    ColOffsetField,
    InColorField,
    OutColorField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class ColorCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "colorCorrect"

    inColor = InColorField()
    c = inColor
    inColorR = inColor.inColorR
    cr = inColorR
    inColorG = inColor.inColorG
    cg = inColorG
    inColorB = inColor.inColorB
    cb = inColorB

    inAlpha = FloatField()
    a = inAlpha

    unpremultiplyInput = BoolField()
    up = unpremultiplyInput

    premultiplyResult = BoolField()
    pr = premultiplyResult

    hueShift = FloatField()
    hs = hueShift

    satGain = FloatField()
    sg = satGain

    valGain = FloatField()
    vg = valGain

    colGain = ColGainField()
    ccg = colGain
    colGainR = colGain.colGainR
    ccgr = colGainR
    colGainG = colGain.colGainG
    ccgg = colGainG
    colGainB = colGain.colGainB
    ccgb = colGainB

    colOffset = ColOffsetField()
    co = colOffset
    colOffsetR = colOffset.colOffsetR
    cor = colOffsetR
    colOffsetG = colOffset.colOffsetG
    cog = colOffsetG
    colOffsetB = colOffset.colOffsetB
    cob = colOffsetB

    colGamma = ColGammaField()
    cga = colGamma
    colGammaX = colGamma.colGammaX
    cgax = colGammaX
    colGammaY = colGamma.colGammaY
    cgay = colGammaY
    colGammaZ = colGamma.colGammaZ
    cgaz = colGammaZ

    colClamp = BoolField()
    ccmp = colClamp

    colClampMin = ColClampMinField()
    ccmn = colClampMin
    colClampMinR = colClampMin.colClampMinR
    ccmnr = colClampMinR
    colClampMinG = colClampMin.colClampMinG
    ccmng = colClampMinG
    colClampMinB = colClampMin.colClampMinB
    ccmnb = colClampMinB

    colClampMax = ColClampMaxField()
    ccmx = colClampMax
    colClampMaxR = colClampMax.colClampMaxR
    ccmxr = colClampMaxR
    colClampMaxG = colClampMax.colClampMaxG
    ccmxg = colClampMaxG
    colClampMaxB = colClampMax.colClampMaxB
    ccmxb = colClampMaxB

    alphaGain = FloatField()
    aag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    alphaGamma = FloatField()
    agg = alphaGamma

    alphaClamp = BoolField()
    acmp = alphaClamp

    alphaClampMin = FloatField()
    acmn = alphaClampMin

    alphaClampMax = FloatField()
    acmx = alphaClampMax

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
