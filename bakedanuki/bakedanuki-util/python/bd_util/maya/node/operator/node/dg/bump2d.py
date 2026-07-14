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

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

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

    adjustEdges = BoolField(default_value=False)
    ae = adjustEdges

    bumpDepth = FloatField(default_value=1.0, soft_min_value=-5.0, soft_max_value=5.0)
    bd = bumpDepth

    bumpInterp = BumpInterpEnumField(default_value=0)
    bi = bumpInterp

    bumpFilter = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    bf = bumpFilter

    bumpFilterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    bfo = bumpFilterOffset

    bumpValue = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    bv = bumpValue

    provide3dInfo = BoolField(default_value=False)
    p3d = provide3dInfo

    outNormal = OutNormalField(default_value=(0.0, 0.0, 1.0), writable=False)
    o = outNormal
    outNormalX = outNormal.outNormalX
    ox = outNormalX
    outNormalY = outNormal.outNormalY
    oy = outNormalY
    outNormalZ = outNormal.outNormalZ
    oz = outNormalZ

    vertexUvOne = VertexUvOneField(default_value=(0.0, 0.0))
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField(default_value=(0.0, 0.0))
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexCameraOne = VertexCameraOneField(default_value=(0.0, 0.0, 0.0))
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField(default_value=(0.0, 0.0, 0.0))
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiFlipR = BoolField(default_value=False, category="arnold")
    flip_r = aiFlipR

    aiFlipG = BoolField(default_value=False, category="arnold")
    flip_g = aiFlipG

    aiSwapTangents = BoolField(default_value=False, category="arnold")
    swap_tangents = aiSwapTangents

    aiUseDerivatives = BoolField(default_value=True, category="arnold")
    use_derivatives = aiUseDerivatives
