# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.sampler_info import (
    NormalCameraField,
    PixelCenterField,
    PointCameraField,
    PointObjField,
    PointWorldField,
    RayDirectionField,
    TangentUCameraField,
    TangentVCameraField,
    UvCoordField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedSamplerInfo(DG):
    __slots__ = ()

    NODE_TYPE = "samplerInfo"

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    pointObj = PointObjField(default_value=(0.0, 0.0, 0.0))
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointWorld = PointWorldField(default_value=(0.0, 0.0, 0.0))
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0))
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    tangentUCamera = TangentUCameraField(default_value=(1.0, 0.0, 0.0))
    tu = tangentUCamera
    tangentUx = tangentUCamera.tangentUx
    tux = tangentUx
    tangentUy = tangentUCamera.tangentUy
    tuy = tangentUy
    tangentUz = tangentUCamera.tangentUz
    tuz = tangentUz

    tangentVCamera = TangentVCameraField(default_value=(0.0, 1.0, 0.0))
    tv = tangentVCamera
    tangentVx = tangentVCamera.tangentVx
    tvx = tangentVx
    tangentVy = tangentVCamera.tangentVy
    tvy = tangentVy
    tangentVz = tangentVCamera.tangentVz
    tvz = tangentVz

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    pixelCenter = PixelCenterField(default_value=(0.0, 0.0))
    pc = pixelCenter
    pixelCenterX = pixelCenter.pixelCenterX
    pcx = pixelCenterX
    pixelCenterY = pixelCenter.pixelCenterY
    pcy = pixelCenterY

    flippedNormal = BoolField(default_value=False)
    fn = flippedNormal

    facingRatio = FloatField(default_value=0.0)
    fr = facingRatio
