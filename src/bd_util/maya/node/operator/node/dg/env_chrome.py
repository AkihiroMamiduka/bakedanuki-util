# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.env_chrome import (
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
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class EnvChrome(DG):
    __slots__ = ()

    NODE_TYPE = "envChrome"

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

    skyColor = SkyColorField()
    sc = skyColor
    skyColorR = skyColor.skyColorR
    scr = skyColorR
    skyColorG = skyColor.skyColorG
    scg = skyColorG
    skyColorB = skyColor.skyColorB
    scb = skyColorB

    zenithColor = ZenithColorField()
    zc = zenithColor
    zenithColorR = zenithColor.zenithColorR
    zcr = zenithColorR
    zenithColorG = zenithColor.zenithColorG
    zcg = zenithColorG
    zenithColorB = zenithColor.zenithColorB
    zcb = zenithColorB

    lightColor = LightColorField()
    lc = lightColor
    lightColorR = lightColor.lightColorR
    lcr = lightColorR
    lightColorG = lightColor.lightColorG
    lcg = lightColorG
    lightColorB = lightColor.lightColorB
    lcb = lightColorB

    lightWidth = FloatField()
    lw = lightWidth

    lightWidthGain = FloatField()
    lwg = lightWidthGain

    lightWidthOffset = FloatField()
    lwo = lightWidthOffset

    lightDepth = FloatField()
    ld = lightDepth

    lightDepthGain = FloatField()
    ldg = lightDepthGain

    lightDepthOffset = FloatField()
    ldo = lightDepthOffset

    realFloor = BoolField()
    rf = realFloor

    floorColor = FloorColorField()
    fc = floorColor
    floorColorR = floorColor.floorColorR
    fcr = floorColorR
    floorColorG = floorColor.floorColorG
    fcg = floorColorG
    floorColorB = floorColor.floorColorB
    fcb = floorColorB

    floorAltitude = FloatField()
    fa = floorAltitude

    horizonColor = HorizonColorField()
    hc = horizonColor
    horizonColorR = horizonColor.horizonColorR
    hcr = horizonColorR
    horizonColorG = horizonColor.horizonColorG
    hcg = horizonColorG
    horizonColorB = horizonColor.horizonColorB
    hcb = horizonColorB

    gridColor = GridColorField()
    gc = gridColor
    gridColorR = gridColor.gridColorR
    gcr = gridColorR
    gridColorG = gridColor.gridColorG
    gcg = gridColorG
    gridColorB = gridColor.gridColorB
    gcb = gridColorB

    gridWidth = FloatField()
    gw = gridWidth

    gridWidthGain = FloatField()
    gwg = gridWidthGain

    gridWidthOffset = FloatField()
    gwo = gridWidthOffset

    gridDepth = FloatField()
    gd = gridDepth

    gridDepthGain = FloatField()
    gdg = gridDepthGain

    gridDepthOffset = FloatField()
    gdo = gridDepthOffset
