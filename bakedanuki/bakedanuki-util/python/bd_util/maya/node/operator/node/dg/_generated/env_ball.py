# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.env_ball import (
    FilterSizeField,
    ImageField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    RayDirectionField,
    UvCoordField,
    UvFilterSizeField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.char import CharField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedEnvBall(DG):
    __slots__ = ()

    NODE_TYPE = "envBall"

    objectType = CharField(default_value=1, min_value=0, max_value=255)
    ot = objectType

    placementMatrix = FltMatrixField()
    pm = placementMatrix

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    xPixelAngle = FloatField(
        default_value=0.002053000032901764, readable=False
    )
    xpa = xPixelAngle

    normalCamera = NormalCameraField(default_value=(0.0, 0.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0))
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    uf = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    ufx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    ufy = uvFilterSizeY

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0))
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    image = ImageField(
        default_value=(0.5, 0.5, 0.5),
        min_value=(0.0, 0.0, 0.0),
        max_value=(1.0, 1.0, 1.0),
    )
    so = image
    imageR = image.imageR
    sor = imageR
    imageG = image.imageG
    sog = imageG
    imageB = image.imageB
    sob = imageB

    inclination = FloatField(
        default_value=0.0, min_value=0.0, max_value=3.141592653589793
    )
    i = inclination

    elevation = FloatField(
        default_value=0.0,
        min_value=-1.5707963267948966,
        max_value=1.5707963267948966,
    )
    e = elevation

    skyRadius = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=20.0
    )
    sr = skyRadius

    bottom = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    bo = bottom

    top = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    to = top

    left = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    le = left

    right = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    ri = right

    front = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    fr = front

    back = FloatField(default_value=0.0, min_value=0.0, soft_max_value=20.0)
    ba = back

    reflect = BoolField(default_value=True)
    ref = reflect

    eyeSpace = BoolField(default_value=False)
    eye = eyeSpace

    infoBits = LongField(default_value=0)
    ib = infoBits
