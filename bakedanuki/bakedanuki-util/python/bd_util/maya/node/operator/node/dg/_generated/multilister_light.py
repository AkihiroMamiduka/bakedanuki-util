# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.multilister_light import (
    LightDataField,
    PointCameraField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedMultilisterLight(DG):
    __slots__ = ()

    NODE_TYPE = "multilisterLight"

    inLightIntensity = FloatField(default_value=1.0, readable=False)
    ili = inLightIntensity

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0), readable=False)
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    lightData = LightDataField(writable=False)
    ltd = lightData
    lightDirection = lightData.lightDirection
    ld = lightDirection
    lightIntensity = lightData.lightIntensity
    li = lightIntensity
    lightAmbient = lightData.lightAmbient
    la = lightAmbient
    lightDiffuse = lightData.lightDiffuse
    ldf = lightDiffuse
    lightSpecular = lightData.lightSpecular
    ls = lightSpecular
    lightShadowFraction = lightData.lightShadowFraction
    lsf = lightShadowFraction
    preShadowIntensity = lightData.preShadowIntensity
    psi = preShadowIntensity
    lightBlindData = lightData.lightBlindData
    lbd = lightBlindData
