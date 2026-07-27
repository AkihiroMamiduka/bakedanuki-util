# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.light_info import (
    LightDirectionField,
    LightPositionField,
    PointCameraField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedLightInfo(DG):
    __slots__ = ()

    NODE_TYPE = "lightInfo"

    matrixEyeToWorld = FltMatrixField(readable=False)
    e2w = matrixEyeToWorld

    lightDirectionOnly = BoolField(default_value=False, readable=False)
    ldo = lightDirectionOnly

    worldMatrix = FltMatrixField(readable=False)
    wm = worldMatrix

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    lightPosition = LightPositionField(default_value=(0.0, 0.0, 0.0), writable=False)
    lp = lightPosition
    lightPositionX = lightPosition.lightPositionX
    lpx = lightPositionX
    lightPositionY = lightPosition.lightPositionY
    lpy = lightPositionY
    lightPositionZ = lightPosition.lightPositionZ
    lpz = lightPositionZ

    lightDirection = LightDirectionField(default_value=(0.0, 0.0, 1.0), writable=False)
    ld = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ

    sampleDistance = FloatField(default_value=0.0010000000474974513, writable=False)
    sd = sampleDistance
