# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.env_sky import (
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
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.char import CharField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField


class GeneratedEnvSky(DG):
    __slots__ = ()

    NODE_TYPE = "envSky"

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

    refPointCamera = RefPointCameraField(default_value=(0.0, 0.0, 0.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ

    totalBrightness = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=5.0)
    tb = totalBrightness

    sunBrightness = SunBrightnessField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    su = sunBrightness
    sunBrightnessR = sunBrightness.sunBrightnessR
    sur = sunBrightnessR
    sunBrightnessG = sunBrightness.sunBrightnessG
    sug = sunBrightnessG
    sunBrightnessB = sunBrightness.sunBrightnessB
    sub = sunBrightnessB

    haloBrightness = HaloBrightnessField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    hb = haloBrightness
    haloBrightnessR = haloBrightness.haloBrightnessR
    hbr = haloBrightnessR
    haloBrightnessG = haloBrightness.haloBrightnessG
    hbg = haloBrightnessG
    haloBrightnessB = haloBrightness.haloBrightnessB
    hbb = haloBrightnessB

    elevation = DoubleAngleField(default_value=45.0, min_value=-90.0, max_value=90.0, soft_min_value=0.0)
    e = elevation

    azimuth = DoubleAngleField(default_value=145.0, min_value=0.0, max_value=360.0)
    az = azimuth

    size = FloatField(default_value=0.531000018119812, min_value=0.0, soft_max_value=20.0)
    sz = size

    blur = FloatField(default_value=1.0, min_value=0.0, soft_max_value=20.0)
    b = blur

    skyBrightness = SkyBrightnessField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    sk = skyBrightness
    skyBrightnessR = skyBrightness.skyBrightnessR
    skr = skyBrightnessR
    skyBrightnessG = skyBrightness.skyBrightnessG
    skg = skyBrightnessG
    skyBrightnessB = skyBrightness.skyBrightnessB
    skb = skyBrightnessB

    airDensity = FloatField(default_value=1.0, min_value=0.0, max_value=3.0)
    ad = airDensity

    dustDensity = FloatField(default_value=0.0, min_value=0.0, max_value=3.0)
    dd = dustDensity

    skyThickness = FloatField(default_value=1000.0, min_value=100.0, max_value=10000.0)
    st = skyThickness

    skyRadius = FloatField(default_value=50.0, min_value=0.01, soft_max_value=300.0)
    sr = skyRadius

    hasFloor = BoolField(default_value=True)
    hf = hasFloor

    floorColor = FloorColorField(default_value=(0.4000000059604645, 0.4000000059604645, 0.4000000059604645), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    fc = floorColor
    floorColorR = floorColor.floorColorR
    fcr = floorColorR
    floorColorG = floorColor.floorColorG
    fcg = floorColorG
    floorColorB = floorColor.floorColorB
    fcb = floorColorB

    floorAltitude = FloatField(default_value=-10.0, min_value=-100.0, max_value=100.0)
    fa = floorAltitude

    useTexture = BoolField(default_value=False)
    ut = useTexture

    cloudTexture = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    ct = cloudTexture

    cloudBrightness = CloudBrightnessField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    cb = cloudBrightness
    cloudBrightnessR = cloudBrightness.cloudBrightnessR
    cbr = cloudBrightnessR
    cloudBrightnessG = cloudBrightness.cloudBrightnessG
    cbg = cloudBrightnessG
    cloudBrightnessB = cloudBrightness.cloudBrightnessB
    cbb = cloudBrightnessB

    sunsetBrightness = SunsetBrightnessField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    ss = sunsetBrightness
    sunsetBrightnessR = sunsetBrightness.sunsetBrightnessR
    ssr = sunsetBrightnessR
    sunsetBrightnessG = sunsetBrightness.sunsetBrightnessG
    ssg = sunsetBrightnessG
    sunsetBrightnessB = sunsetBrightness.sunsetBrightnessB
    ssb = sunsetBrightnessB

    density = FloatField(default_value=1.0, min_value=0.0, max_value=5.0)
    d = density

    threshold = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    t = threshold

    power = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    po = power

    altitude = FloatField(default_value=0.20000000298023224, min_value=0.0, max_value=1.0)
    a = altitude

    haloSize = FloatField(default_value=20.0, min_value=0.0, max_value=50.0)
    hs = haloSize

    skySamples = FloatField(default_value=5.0, min_value=0.0, max_value=5.0)
    ssa = skySamples

    floorSamples = FloatField(default_value=1.0, min_value=0.0, max_value=3.0)
    fsa = floorSamples

    cloudSamples = FloatField(default_value=5.0, min_value=0.0, max_value=5.0)
    csa = cloudSamples
