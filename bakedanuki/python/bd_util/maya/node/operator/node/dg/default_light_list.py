# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.default_light_list import (
    LightDataArrayField,
    LightDataField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class DefaultLightList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultLightList"

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    lda = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    lightData = LightDataField(writable=False)
    ltd = lightData
    lightDirectionOut = lightData.lightDirectionOut
    ldo = lightDirectionOut
    lightIntensityOut = lightData.lightIntensityOut
    lw = lightIntensityOut
    lightAmbientOut = lightData.lightAmbientOut
    lya = lightAmbientOut
    lightDiffuseOut = lightData.lightDiffuseOut
    lyf = lightDiffuseOut
    lightSpecularOut = lightData.lightSpecularOut
    lys = lightSpecularOut
    lightShadowFractionOut = lightData.lightShadowFractionOut
    sfo = lightShadowFractionOut
    preShadowIntensityOut = lightData.preShadowIntensityOut
    psio = preShadowIntensityOut
    lightBlindDataOut = lightData.lightBlindDataOut
    lbdo = lightBlindDataOut
