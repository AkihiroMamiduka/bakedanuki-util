# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.bump3d import (
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
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class Bump3d(DG):
    __slots__ = ()

    NODE_TYPE = "bump3d"

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

    refPointObj = RefPointObjField()
    rpo = refPointObj
    refPointObjX = refPointObj.refPointObjX
    rpox = refPointObjX
    refPointObjY = refPointObj.refPointObjY
    rpoy = refPointObjY
    refPointObjZ = refPointObj.refPointObjZ
    rpoz = refPointObjZ

    refPointCamera = RefPointCameraField()
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    rayOrigin = RayOriginField()
    ro = rayOrigin
    rayOriginX = rayOrigin.rayOriginX
    rox = rayOriginX
    rayOriginY = rayOrigin.rayOriginY
    roy = rayOriginY
    rayOriginZ = rayOrigin.rayOriginZ
    roz = rayOriginZ

    xPixelAngle = FloatField()
    xpa = xPixelAngle

    infoBits = LongField()
    ib = infoBits

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

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

    bumpDepth = FloatField()
    bd = bumpDepth

    bumpFilter = FloatField()
    bf = bumpFilter

    bumpFilterOffset = FloatField()
    bfo = bumpFilterOffset

    bumpValue = FloatField()
    bv = bumpValue

    outNormal = OutNormalField()
    o = outNormal
    outNormalX = outNormal.outNormalX
    ox = outNormalX
    outNormalY = outNormal.outNormalY
    oy = outNormalY
    outNormalZ = outNormal.outNormalZ
    oz = outNormalZ
