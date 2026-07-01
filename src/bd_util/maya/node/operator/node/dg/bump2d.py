# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.bump2d import (
    NormalCameraField,
    OutNormalField,
    PointCameraField,
    PointObjField,
    RayOriginField,
    RefPointCameraField,
    RefPointObjField,
    TangentUCameraField,
    TangentVCameraField,
    UvCoordField,
    UvFilterSizeField,
    VertexCameraOneField,
    VertexCameraTwoField,
    VertexUvOneField,
    VertexUvTwoField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class BumpInterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BUMP = 0
    TANGENT_SPACE_NORMALS = 1
    OBJECT_SPACE_NORMALS = 2


class BumpInterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BUMP = 0
    TANGENT_SPACE_NORMALS = 1
    OBJECT_SPACE_NORMALS = 2

    NAME_MAP = {
        BUMP: "Bump",
        TANGENT_SPACE_NORMALS: "Tangent Space Normals",
        OBJECT_SPACE_NORMALS: "Object Space Normals",
    }


class BumpInterpEnumField(
    EnumField[BumpInterpEnumAttrOperator, BumpInterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BumpInterpEnumAttrOperator
    PLUG_CLS = BumpInterpEnumPlugOperator


class Bump2d(DG):
    __slots__ = ()

    NODE_TYPE = "bump2d"

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

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

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

    adjustEdges = BoolField()
    ae = adjustEdges

    bumpDepth = FloatField()
    bd = bumpDepth

    bumpInterp = BumpInterpEnumField()
    bi = bumpInterp

    bumpFilter = FloatField()
    bf = bumpFilter

    bumpFilterOffset = FloatField()
    bfo = bumpFilterOffset

    bumpValue = FloatField()
    bv = bumpValue

    provide3dInfo = BoolField()
    p3d = provide3dInfo

    outNormal = OutNormalField()
    o = outNormal
    outNormalX = outNormal.outNormalX
    ox = outNormalX
    outNormalY = outNormal.outNormalY
    oy = outNormalY
    outNormalZ = outNormal.outNormalZ
    oz = outNormalZ

    vertexUvOne = VertexUvOneField()
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField()
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexCameraOne = VertexCameraOneField()
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField()
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiFlipR = BoolField()
    flip_r = aiFlipR

    aiFlipG = BoolField()
    flip_g = aiFlipG

    aiSwapTangents = BoolField()
    swap_tangents = aiSwapTangents

    aiUseDerivatives = BoolField()
    use_derivatives = aiUseDerivatives
