# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ais_env_facade import (
    BackgroundColorField,
    ExtraLightInfoField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAISEnvFacade(DG):
    __slots__ = ()

    NODE_TYPE = "AISEnvFacade"

    sharedLibName = DataStringField()
    sln = sharedLibName

    connection = MessageField()
    c = connection

    uiName = DataStringField()
    uin = uiName

    keyWords = DataStringField()
    kwds = keyWords

    uiScript = DataStringField()
    uis = uiScript

    uniqueID = DataStringField()
    uid = uniqueID

    minMentalRayQualityNode = MessageField()
    minmrq = minMentalRayQualityNode

    maxMentalRayQualityNode = MessageField()
    maxmrq = maxMentalRayQualityNode

    antiAliasingQuality = ShortField(default_value=1, min_value=1, max_value=10)
    aaq = antiAliasingQuality

    reflectionsQuality = ShortField(default_value=1, min_value=1, max_value=10)
    rflq = reflectionsQuality

    refractionsQuality = ShortField(default_value=1, min_value=1, max_value=10)
    rfrq = refractionsQuality

    globalIlluminationQuality = ShortField(default_value=1, min_value=1, max_value=10)
    giq = globalIlluminationQuality

    tessellationQuality = ShortField(default_value=1, min_value=1, max_value=10)
    tq = tessellationQuality

    factoryAntiAliasingQuality = ShortField(default_value=1, min_value=1, max_value=10)
    faaq = factoryAntiAliasingQuality

    factoryReflectionsQuality = ShortField(default_value=1, min_value=1, max_value=10)
    frflq = factoryReflectionsQuality

    factoryRefractionsQuality = ShortField(default_value=1, min_value=1, max_value=10)
    frfrq = factoryRefractionsQuality

    factoryGlobalIlluminationQuality = ShortField(default_value=1, min_value=1, max_value=10)
    fgiq = factoryGlobalIlluminationQuality

    factoryTessellationQuality = ShortField(default_value=1, min_value=1, max_value=10)
    ftq = factoryTessellationQuality

    testAntiAliasingQuality = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    taaq = testAntiAliasingQuality

    testReflectionsQuality = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    trflq = testReflectionsQuality

    testRefractionsQuality = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    trfrq = testRefractionsQuality

    testGlobalIlluminationQuality = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    tgiq = testGlobalIlluminationQuality

    testTessellationQuality = FloatField(default_value=1.0, min_value=1.0, max_value=10.0)
    ttq = testTessellationQuality

    hasFloor = BoolField(default_value=False, readable=False)
    hf = hasFloor

    floorHeight = FloatField(default_value=0.0, readable=False)
    fh = floorHeight

    backgroundColor = BackgroundColorField(default_value=(0.699999988079071, 0.699999988079071, 0.699999988079071), readable=False)
    bc = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    bcr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    bcg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    bcb = backgroundColorB

    hasInfiniteStage = BoolField(default_value=False)
    his = hasInfiniteStage

    originalStageRadius = FloatField(default_value=1.0, min_value=0.0)
    osr = originalStageRadius

    hasUserDefinedStageRadius = BoolField(default_value=False)
    hudsr = hasUserDefinedStageRadius

    userDefinedStageRadius = FloatField(default_value=1.0, min_value=0.0)
    udsr = userDefinedStageRadius

    extraLightInfo = ExtraLightInfoField(multi=True)
    eli = extraLightInfo

    extraLightColorR = FloatField()
    elcr = extraLightColorR

    extraLightColorG = FloatField()
    elcg = extraLightColorG

    extraLightColorb = FloatField()
    elcb = extraLightColorb

    extraLightShadowColorR = FloatField()
    elscr = extraLightShadowColorR

    extraLightShadowColorG = FloatField()
    elscg = extraLightShadowColorG

    extraLightShadowColorB = FloatField()
    elscb = extraLightShadowColorB
