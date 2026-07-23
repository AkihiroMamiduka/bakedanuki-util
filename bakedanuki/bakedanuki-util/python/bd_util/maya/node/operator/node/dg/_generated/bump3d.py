# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bump3d import (
    NormalCameraField,
    OutNormalField,
    PointCameraField,
    PointObjField,
    RayOriginField,
    RefPointCameraField,
    RefPointObjField,
    TangentUCameraField,
    TangentVCameraField,
)
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedBump3d(DG):
    __slots__ = ()

    NODE_TYPE = "bump3d"

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

    refPointObj = RefPointObjField(default_value=(0.0, 0.0, 0.0))
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rpox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    rpoy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    rpoz = refPointObjZ

    refPointCamera = RefPointCameraField(default_value=(0.0, 0.0, 0.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    rayOrigin = RayOriginField(default_value=(0.0, 0.0, 0.0))
    ro = rayOrigin
    rayOriginX = rayOrigin.rayOriginX
    rox = rayOriginX
    rayOriginY = rayOrigin.rayOriginY
    roy = rayOriginY
    rayOriginZ = rayOrigin.rayOriginZ
    roz = rayOriginZ

    xPixelAngle = FloatField(default_value=0.002053000032901764, readable=False)
    xpa = xPixelAngle

    infoBits = LongField(default_value=0)
    ib = infoBits

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

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

    bumpDepth = FloatField(default_value=1.0, soft_min_value=-5.0, soft_max_value=5.0)
    bd = bumpDepth

    bumpFilter = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    bf = bumpFilter

    bumpFilterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    bfo = bumpFilterOffset

    bumpValue = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    bv = bumpValue

    outNormal = OutNormalField(default_value=(0.0, 0.0, 1.0), writable=False)
    o = outNormal
    outNormalX = outNormal.outNormalX
    ox = outNormalX
    outNormalY = outNormal.outNormalY
    oy = outNormalY
    outNormalZ = outNormal.outNormalZ
    oz = outNormalZ
