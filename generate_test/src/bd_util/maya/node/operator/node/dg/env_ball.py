# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.env_ball import (
    FilterSizeField,
    ImageField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    RayDirectionField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class EnvBall(DG):
    __slots__ = ()

    NODE_TYPE = "envBall"

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

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    image = ImageField()
    so = image
    imageR = image.imageR
    sor = imageR
    imageG = image.imageG
    sog = imageG
    imageB = image.imageB
    sob = imageB

    inclination = FloatField()
    i = inclination

    elevation = FloatField()
    e = elevation

    skyRadius = FloatField()
    sr = skyRadius

    bottom = FloatField()
    bo = bottom

    top = FloatField()
    to = top

    left = FloatField()
    le = left

    right = FloatField()
    ri = right

    front = FloatField()
    fr = front

    back = FloatField()
    ba = back

    reflect = BoolField()
    ref = reflect

    eyeSpace = BoolField()
    eye = eyeSpace

    infoBits = LongField()
    ib = infoBits
