# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.default_light_list import (
    LightDataArrayField,
    LightDataField,
)


class DefaultLightList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultLightList"

    lightDataArray = LightDataArrayField(multi=True)
    lda = lightDataArray

    # TODO: lightDataArray.lightDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    lightData = LightDataField()
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
