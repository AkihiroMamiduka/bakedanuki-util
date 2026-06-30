# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.env_cube import (
    BackField,
    BottomField,
    FilterSizeField,
    FrontField,
    LeftField,
    NormalCameraField,
    OutColorField,
    PointWorldField,
    RayDirectionField,
    RightField,
    TopField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class LookupTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    REFLECTION = 0
    NORMAL = 1


class LookupTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    REFLECTION = 0
    NORMAL = 1

    NAME_MAP = {
        REFLECTION: "reflection",
        NORMAL: "normal",
    }


class LookupTypeEnumField(
    EnumField[LookupTypeEnumAttrOperator, LookupTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LookupTypeEnumAttrOperator
    PLUG_CLS = LookupTypeEnumPlugOperator


class EnvCube(DG):
    __slots__ = ()

    NODE_TYPE = "envCube"

    objectType = CharField()
    ot = objectType

    placementMatrix = FltMatrixField()
    pm = placementMatrix

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    xPixelAngle = FloatField()
    xpa = xPixelAngle

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    rayDirection = RayDirectionField()
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    uf = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    ufx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    ufy = uvFilterSizeY

    filterSize = FilterSizeField()
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField()
    oa = outAlpha

    pointWorld = PointWorldField()
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    infiniteSize = BoolField()
    ie = infiniteSize

    lookupType = LookupTypeEnumField()
    lt = lookupType

    left = LeftField()
    le = left
    leftR = left.leftR
    ler = leftR
    leftG = left.leftG
    leg = leftG
    leftB = left.leftB
    leb = leftB

    right = RightField()
    ri = right
    rightR = right.rightR
    rir = rightR
    rightG = right.rightG
    rig = rightG
    rightB = right.rightB
    rib = rightB

    top = TopField()
    to = top
    topR = top.topR
    tor = topR
    topG = top.topG
    tog = topG
    topB = top.topB
    tob = topB

    bottom = BottomField()
    bo = bottom
    bottomR = bottom.bottomR
    bor = bottomR
    bottomG = bottom.bottomG
    bog = bottomG
    bottomB = bottom.bottomB
    bob = bottomB

    front = FrontField()
    fr = front
    frontR = front.frontR
    frr = frontR
    frontG = front.frontG
    frg = frontG
    frontB = front.frontB
    frb = frontB

    back = BackField()
    ba = back
    backR = back.backR
    bar = backR
    backG = back.backG
    bag = backG
    backB = back.backB
    bab = backB

    infoBits = LongField()
    ib = infoBits
