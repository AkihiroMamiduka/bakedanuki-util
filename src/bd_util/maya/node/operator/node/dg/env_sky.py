# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.env_sky import (
    CloudBrightnessField,
    FilterSizeField,
    FloorColorField,
    HaloBrightnessField,
    NormalCameraField,
    OutColorField,
    PointCameraField,
    RayDirectionField,
    RefPointCameraField,
    SkyBrightnessField,
    SunBrightnessField,
    SunsetBrightnessField,
    UvCoordField,
    UvFilterSizeField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField


class EnvSky(DG):
    __slots__ = ()

    NODE_TYPE = "envSky"

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

    refPointCamera = RefPointCameraField()
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    totalBrightness = FloatField()
    tb = totalBrightness

    sunBrightness = SunBrightnessField()
    su = sunBrightness
    sunBrightnessR = sunBrightness.sunBrightnessR
    sur = sunBrightnessR
    sunBrightnessG = sunBrightness.sunBrightnessG
    sug = sunBrightnessG
    sunBrightnessB = sunBrightness.sunBrightnessB
    sub = sunBrightnessB

    haloBrightness = HaloBrightnessField()
    hb = haloBrightness
    haloBrightnessR = haloBrightness.haloBrightnessR
    hbr = haloBrightnessR
    haloBrightnessG = haloBrightness.haloBrightnessG
    hbg = haloBrightnessG
    haloBrightnessB = haloBrightness.haloBrightnessB
    hbb = haloBrightnessB

    elevation = DoubleAngleField()
    e = elevation

    azimuth = DoubleAngleField()
    az = azimuth

    size = FloatField()
    sz = size

    blur = FloatField()
    b = blur

    skyBrightness = SkyBrightnessField()
    sk = skyBrightness
    skyBrightnessR = skyBrightness.skyBrightnessR
    skr = skyBrightnessR
    skyBrightnessG = skyBrightness.skyBrightnessG
    skg = skyBrightnessG
    skyBrightnessB = skyBrightness.skyBrightnessB
    skb = skyBrightnessB

    airDensity = FloatField()
    ad = airDensity

    dustDensity = FloatField()
    dd = dustDensity

    skyThickness = FloatField()
    st = skyThickness

    skyRadius = FloatField()
    sr = skyRadius

    hasFloor = BoolField()
    hf = hasFloor

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

    useTexture = BoolField()
    ut = useTexture

    cloudTexture = FloatField()
    ct = cloudTexture

    cloudBrightness = CloudBrightnessField()
    cb = cloudBrightness
    cloudBrightnessR = cloudBrightness.cloudBrightnessR
    cbr = cloudBrightnessR
    cloudBrightnessG = cloudBrightness.cloudBrightnessG
    cbg = cloudBrightnessG
    cloudBrightnessB = cloudBrightness.cloudBrightnessB
    cbb = cloudBrightnessB

    sunsetBrightness = SunsetBrightnessField()
    ss = sunsetBrightness
    sunsetBrightnessR = sunsetBrightness.sunsetBrightnessR
    ssr = sunsetBrightnessR
    sunsetBrightnessG = sunsetBrightness.sunsetBrightnessG
    ssg = sunsetBrightnessG
    sunsetBrightnessB = sunsetBrightness.sunsetBrightnessB
    ssb = sunsetBrightnessB

    density = FloatField()
    d = density

    threshold = FloatField()
    t = threshold

    power = FloatField()
    po = power

    altitude = FloatField()
    a = altitude

    haloSize = FloatField()
    hs = haloSize

    skySamples = FloatField()
    ssa = skySamples

    floorSamples = FloatField()
    fsa = floorSamples

    cloudSamples = FloatField()
    csa = cloudSamples
