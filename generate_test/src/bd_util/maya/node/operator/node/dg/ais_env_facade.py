# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ais_env_facade import (
    BackgroundColorField,
    ExtraLightInfoField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.dt.string import DataStringField


class AISEnvFacade(DG):
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

    antiAliasingQuality = ShortField()
    aaq = antiAliasingQuality

    reflectionsQuality = ShortField()
    rflq = reflectionsQuality

    refractionsQuality = ShortField()
    rfrq = refractionsQuality

    globalIlluminationQuality = ShortField()
    giq = globalIlluminationQuality

    tessellationQuality = ShortField()
    tq = tessellationQuality

    factoryAntiAliasingQuality = ShortField()
    faaq = factoryAntiAliasingQuality

    factoryReflectionsQuality = ShortField()
    frflq = factoryReflectionsQuality

    factoryRefractionsQuality = ShortField()
    frfrq = factoryRefractionsQuality

    factoryGlobalIlluminationQuality = ShortField()
    fgiq = factoryGlobalIlluminationQuality

    factoryTessellationQuality = ShortField()
    ftq = factoryTessellationQuality

    testAntiAliasingQuality = FloatField()
    taaq = testAntiAliasingQuality

    testReflectionsQuality = FloatField()
    trflq = testReflectionsQuality

    testRefractionsQuality = FloatField()
    trfrq = testRefractionsQuality

    testGlobalIlluminationQuality = FloatField()
    tgiq = testGlobalIlluminationQuality

    testTessellationQuality = FloatField()
    ttq = testTessellationQuality

    hasFloor = BoolField()
    hf = hasFloor

    floorHeight = FloatField()
    fh = floorHeight

    backgroundColor = BackgroundColorField()
    bc = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    bcr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    bcg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    bcb = backgroundColorB

    hasInfiniteStage = BoolField()
    his = hasInfiniteStage

    originalStageRadius = FloatField()
    osr = originalStageRadius

    hasUserDefinedStageRadius = BoolField()
    hudsr = hasUserDefinedStageRadius

    userDefinedStageRadius = FloatField()
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
