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
    _c = inColor
    inColorR = inColor.inColorR
    _cr = inColorR
    inColorG = inColor.inColorG
    _cg = inColorG
    inColorB = inColor.inColorB
    _cb = inColorB

    inAlpha = FloatField()
    _a = inAlpha

    unpremultiplyInput = BoolField()
    _up = unpremultiplyInput

    premultiplyResult = BoolField()
    _pr = premultiplyResult

    hueShift = FloatField()
    _hs = hueShift

    satGain = FloatField()
    _sg = satGain

    valGain = FloatField()
    _vg = valGain

    colGain = ColGainField()
    _ccg = colGain
    colGainR = colGain.colGainR
    _ccgr = colGainR
    colGainG = colGain.colGainG
    _ccgg = colGainG
    colGainB = colGain.colGainB
    _ccgb = colGainB

    colOffset = ColOffsetField()
    _co = colOffset
    colOffsetR = colOffset.colOffsetR
    _cor = colOffsetR
    colOffsetG = colOffset.colOffsetG
    _cog = colOffsetG
    colOffsetB = colOffset.colOffsetB
    _cob = colOffsetB

    colGamma = ColGammaField()
    _cga = colGamma
    colGammaX = colGamma.colGammaX
    _cgax = colGammaX
    colGammaY = colGamma.colGammaY
    _cgay = colGammaY
    colGammaZ = colGamma.colGammaZ
    _cgaz = colGammaZ

    colClamp = BoolField()
    _ccmp = colClamp

    colClampMin = ColClampMinField()
    _ccmn = colClampMin
    colClampMinR = colClampMin.colClampMinR
    _ccmnr = colClampMinR
    colClampMinG = colClampMin.colClampMinG
    _ccmng = colClampMinG
    colClampMinB = colClampMin.colClampMinB
    _ccmnb = colClampMinB

    colClampMax = ColClampMaxField()
    _ccmx = colClampMax
    colClampMaxR = colClampMax.colClampMaxR
    _ccmxr = colClampMaxR
    colClampMaxG = colClampMax.colClampMaxG
    _ccmxg = colClampMaxG
    colClampMaxB = colClampMax.colClampMaxB
    _ccmxb = colClampMaxB

    alphaGain = FloatField()
    _aag = alphaGain

    alphaOffset = FloatField()
    _ao = alphaOffset

    alphaGamma = FloatField()
    _agg = alphaGamma

    alphaClamp = BoolField()
    _acmp = alphaClamp

    alphaClampMin = FloatField()
    _acmn = alphaClampMin

    alphaClampMax = FloatField()
    _acmx = alphaClampMax

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
