# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.env_chrome import (
    FilterSizeField,
    FloorColorField,
    GridColorField,
    HorizonColorField,
    LightColorField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    RayDirectionField,
    SkyColorField,
    UvCoordField,
    UvFilterSizeField,
    ZenithColorField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.char import CharField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedEnvChrome(DG):
    __slots__ = ()

    NODE_TYPE = "envChrome"

    objectType = CharField(default_value=1, min_value=0, max_value=255)
    ot = objectType

    placementMatrix = FltMatrixField()
    pm = placementMatrix

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    xPixelAngle = FloatField(default_value=0.002053000032901764, readable=False)
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

    skyColor = SkyColorField(default_value=(0.7839999794960022, 0.7839999794960022, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    sc = skyColor
    skyColorR = skyColor.skyColorR
    scr = skyColorR
    skyColorG = skyColor.skyColorG
    scg = skyColorG
    skyColorB = skyColor.skyColorB
    scb = skyColorB

    zenithColor = ZenithColorField(default_value=(0.3919999897480011, 0.3919999897480011, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    zc = zenithColor
    zenithColorR = zenithColor.zenithColorR
    zcr = zenithColorR
    zenithColorG = zenithColor.zenithColorG
    zcg = zenithColorG
    zenithColorB = zenithColor.zenithColorB
    zcb = zenithColorB

    lightColor = LightColorField(default_value=(0.7839999794960022, 0.7839999794960022, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    lc = lightColor
    lightColorR = lightColor.lightColorR
    lcr = lightColorR
    lightColorG = lightColor.lightColorG
    lcg = lightColorG
    lightColorB = lightColor.lightColorB
    lcb = lightColorB

    lightWidth = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    lw = lightWidth

    lightWidthGain = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    lwg = lightWidthGain

    lightWidthOffset = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    lwo = lightWidthOffset

    lightDepth = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    ld = lightDepth

    lightDepthGain = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ldg = lightDepthGain

    lightDepthOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    ldo = lightDepthOffset

    realFloor = BoolField(default_value=True)
    rf = realFloor

    floorColor = FloorColorField(default_value=(0.5879999995231628, 0.5879999995231628, 0.7839999794960022), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    fc = floorColor
    floorColorR = floorColor.floorColorR
    fcr = floorColorR
    floorColorG = floorColor.floorColorG
    fcg = floorColorG
    floorColorB = floorColor.floorColorB
    fcb = floorColorB

    floorAltitude = FloatField(default_value=-1.0, min_value=-1.0, max_value=1.0)
    fa = floorAltitude

    horizonColor = HorizonColorField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    hc = horizonColor
    horizonColorR = horizonColor.horizonColorR
    hcr = horizonColorR
    horizonColorG = horizonColor.horizonColorG
    hcg = horizonColorG
    horizonColorB = horizonColor.horizonColorB
    hcb = horizonColorB

    gridColor = GridColorField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gc = gridColor
    gridColorR = gridColor.gridColorR
    gcr = gridColorR
    gridColorG = gridColor.gridColorG
    gcg = gridColorG
    gridColorB = gridColor.gridColorB
    gcb = gridColorB

    gridWidth = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    gw = gridWidth

    gridWidthGain = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gwg = gridWidthGain

    gridWidthOffset = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gwo = gridWidthOffset

    gridDepth = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    gd = gridDepth

    gridDepthGain = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    gdg = gridDepthGain

    gridDepthOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gdo = gridDepthOffset
