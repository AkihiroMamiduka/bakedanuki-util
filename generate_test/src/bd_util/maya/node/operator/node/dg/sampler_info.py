# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sampler_info import (
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
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SamplerInfo(DG):
    __slots__ = ()

    NODE_TYPE = "samplerInfo"

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    pointObj = PointObjField()
    po = pointObj
    pointObjX = pointObj.pointObjX
    pox = pointObjX
    pointObjY = pointObj.pointObjY
    poy = pointObjY
    pointObjZ = pointObj.pointObjZ
    poz = pointObjZ

    pointWorld = PointWorldField()
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    rayDirection = RayDirectionField()
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    tangentUCamera = TangentUCameraField()
    tu = tangentUCamera
    tangentUx = tangentUCamera.tangentUx
    tux = tangentUx
    tangentUy = tangentUCamera.tangentUy
    tuy = tangentUy
    tangentUz = tangentUCamera.tangentUz
    tuz = tangentUz

    tangentVCamera = TangentVCameraField()
    tv = tangentVCamera
    tangentVx = tangentVCamera.tangentVx
    tvx = tangentVx
    tangentVy = tangentVCamera.tangentVy
    tvy = tangentVy
    tangentVz = tangentVCamera.tangentVz
    tvz = tangentVz

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    pixelCenter = PixelCenterField()
    pc = pixelCenter
    pixelCenterX = pixelCenter.pixelCenterX
    pcx = pixelCenterX
    pixelCenterY = pixelCenter.pixelCenterY
    pcy = pixelCenterY

    flippedNormal = BoolField()
    fn = flippedNormal

    facingRatio = FloatField()
    fr = facingRatio
