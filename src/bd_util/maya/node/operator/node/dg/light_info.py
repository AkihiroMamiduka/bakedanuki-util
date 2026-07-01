# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.light_info import (
    LightDirectionField,
    LightPositionField,
    PointCameraField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class LightInfo(DG):
    __slots__ = ()

    NODE_TYPE = "lightInfo"

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    lightDirectionOnly = BoolField()
    ldo = lightDirectionOnly

    worldMatrix = FltMatrixField()
    wm = worldMatrix

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    lightPosition = LightPositionField()
    lp = lightPosition
    lightPositionX = lightPosition.lightPositionX
    lpx = lightPositionX
    lightPositionY = lightPosition.lightPositionY
    lpy = lightPositionY
    lightPositionZ = lightPosition.lightPositionZ
    lpz = lightPositionZ

    lightDirection = LightDirectionField()
    ld = lightDirection
    lightDirectionX = lightDirection.lightDirectionX
    ldx = lightDirectionX
    lightDirectionY = lightDirection.lightDirectionY
    ldy = lightDirectionY
    lightDirectionZ = lightDirection.lightDirectionZ
    ldz = lightDirectionZ

    sampleDistance = FloatField()
    sd = sampleDistance
