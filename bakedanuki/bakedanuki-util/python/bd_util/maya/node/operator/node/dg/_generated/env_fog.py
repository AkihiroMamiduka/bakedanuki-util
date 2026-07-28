# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.env_fog import (
    AirColorField,
    AirOpacityField,
    ColorField,
    FilterSizeField,
    FogColorField,
    FogOpacityField,
    LightDataArrayField,
    OutColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    PointCameraField,
    PointWorldField,
    RayDirectionField,
    SunColorField,
    WaterColorField,
    WaterOpacityField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator["MatteOpacityModeEnumAttrOperator"]):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator[MatteOpacityModeEnumPlugOperator]):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2

    NAME_MAP = {
        BLACK_HOLE: "Black Hole",
        SOLID_MATTE: "Solid Matte",
        OPACITY_GAIN: "Opacity Gain",
    }


class MatteOpacityModeEnumField(
    EnumField[MatteOpacityModeEnumAttrOperator, MatteOpacityModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MatteOpacityModeEnumAttrOperator
    PLUG_CLS = MatteOpacityModeEnumPlugOperator


class DistanceClipPlanesEnumPlugOperator(EnumPlugOperator["DistanceClipPlanesEnumAttrOperator"]):
    __slots__ = ()

    CAMERA_NEAR_SLASH_FAR = 0
    FOG_NEAR_SLASH_FAR = 1


class DistanceClipPlanesEnumAttrOperator(EnumAttrOperator[DistanceClipPlanesEnumPlugOperator]):
    __slots__ = ()

    CAMERA_NEAR_SLASH_FAR = 0
    FOG_NEAR_SLASH_FAR = 1

    NAME_MAP = {
        CAMERA_NEAR_SLASH_FAR: "Camera Near/Far",
        FOG_NEAR_SLASH_FAR: "Fog Near/Far",
    }


class DistanceClipPlanesEnumField(
    EnumField[DistanceClipPlanesEnumAttrOperator, DistanceClipPlanesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DistanceClipPlanesEnumAttrOperator
    PLUG_CLS = DistanceClipPlanesEnumPlugOperator


class FogTypeEnumPlugOperator(EnumPlugOperator["FogTypeEnumAttrOperator"]):
    __slots__ = ()

    UNIFORM_FOG = 0
    ATMOSPHERIC = 1
    SKY = 2
    WATER = 3
    WATER_SLASH_FOG = 4
    WATER_SLASH_ATMOS = 5
    WATER_SLASH_SKY = 6


class FogTypeEnumAttrOperator(EnumAttrOperator[FogTypeEnumPlugOperator]):
    __slots__ = ()

    UNIFORM_FOG = 0
    ATMOSPHERIC = 1
    SKY = 2
    WATER = 3
    WATER_SLASH_FOG = 4
    WATER_SLASH_ATMOS = 5
    WATER_SLASH_SKY = 6

    NAME_MAP = {
        UNIFORM_FOG: "Uniform Fog",
        ATMOSPHERIC: "Atmospheric",
        SKY: "Sky",
        WATER: "Water",
        WATER_SLASH_FOG: "Water/Fog",
        WATER_SLASH_ATMOS: "Water/Atmos",
        WATER_SLASH_SKY: "Water/Sky",
    }


class FogTypeEnumField(
    EnumField[FogTypeEnumAttrOperator, FogTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogTypeEnumAttrOperator
    PLUG_CLS = FogTypeEnumPlugOperator


class FogAxisEnumPlugOperator(EnumPlugOperator["FogAxisEnumAttrOperator"]):
    __slots__ = ()

    X = 0
    MINUS_X = 1
    Y = 2
    MINUS_Y = 3
    Z = 4
    MINUS_Z = 5


class FogAxisEnumAttrOperator(EnumAttrOperator[FogAxisEnumPlugOperator]):
    __slots__ = ()

    X = 0
    MINUS_X = 1
    Y = 2
    MINUS_Y = 3
    Z = 4
    MINUS_Z = 5

    NAME_MAP = {
        X: "X",
        MINUS_X: "-X",
        Y: "Y",
        MINUS_Y: "-Y",
        Z: "Z",
        MINUS_Z: "-Z",
    }


class FogAxisEnumField(
    EnumField[FogAxisEnumAttrOperator, FogAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FogAxisEnumAttrOperator
    PLUG_CLS = FogAxisEnumPlugOperator


class GeneratedEnvFog(DG):
    __slots__ = ()

    NODE_TYPE = "envFog"

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0), readable=False)
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    lightDataArray = LightDataArrayField(multi=True, readable=False)
    ltd = lightDataArray

    lightDirectionX = FloatField()
    ldx = lightDirectionX

    lightDirectionY = FloatField()
    ldy = lightDirectionY

    lightDirectionZ = FloatField()
    ldz = lightDirectionZ

    lightIntensityR = FloatField()
    lir = lightIntensityR

    lightIntensityG = FloatField()
    lig = lightIntensityG

    lightIntensityB = FloatField()
    lib = lightIntensityB

    color = ColorField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    density = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    d = density

    fastDropOff = BoolField(default_value=False)
    fd = fastDropOff

    colorBasedTransparency = BoolField(default_value=True)
    cbt = colorBasedTransparency

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField(default_value=(0.0, 0.0, 0.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    pointCamera = PointCameraField(default_value=(0.0, 0.0, 0.0))
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    pointWorld = PointWorldField(default_value=(0.0, 0.0, 0.0))
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0))
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    distanceClipPlanes = DistanceClipPlanesEnumField(default_value=1, readable=False)
    dcp = distanceClipPlanes

    useLayer = BoolField(default_value=False)
    ul = useLayer

    useHeight = BoolField(default_value=False)
    uh = useHeight

    blendRange = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    br = blendRange

    saturationDistance = FloatField(default_value=100.0, min_value=0.001, soft_max_value=200.0)
    sdt = saturationDistance

    fogNearDistance = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=200.0)
    fnd = fogNearDistance

    fogFarDistance = FloatField(default_value=200.0, soft_min_value=0.0, soft_max_value=200.0)
    ffd = fogFarDistance

    layer = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    l = layer

    minHeight = FloatField(default_value=-1.0, soft_min_value=-10.0, soft_max_value=10.0)
    mnh = minHeight

    maxHeight = FloatField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    mxh = maxHeight

    useDistance = BoolField(default_value=False)
    ud = useDistance

    startDistance = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=100.0)
    sd = startDistance

    endDistance = FloatField(default_value=-1.0, min_value=-1.0, soft_max_value=100.0)
    ed = endDistance

    physicalFog = BoolField(default_value=False)
    sff = physicalFog

    fogType = FogTypeEnumField(default_value=0)
    ftp = fogType

    fogDensity = DoubleField(default_value=0.4, soft_min_value=0.0, soft_max_value=1.0)
    fdn = fogDensity

    fogColor = FogColorField(default_value=(1.0, 1.0, 1.0))
    fcl = fogColor
    fogColorR = fogColor.fogColorR
    fcr = fogColorR
    fogColorG = fogColor.fogColorG
    fcg = fogColorG
    fogColorB = fogColor.fogColorB
    fcb = fogColorB

    fogOpacity = FogOpacityField(default_value=(0.5, 0.5, 0.5))
    fop = fogOpacity
    fogOpacityR = fogOpacity.fogOpacityR
    for_ = fogOpacityR
    fogOpacityG = fogOpacity.fogOpacityG
    fog = fogOpacityG
    fogOpacityB = fogOpacity.fogOpacityB
    fob = fogOpacityB

    fogMinHeight = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    fmh = fogMinHeight

    fogMaxHeight = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    fxh = fogMaxHeight

    fogDecay = DoubleField(default_value=0.2, soft_min_value=0.0, soft_max_value=1.0)
    fdc = fogDecay

    fogLightScatter = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    flc = fogLightScatter

    airDensity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.1)
    adn = airDensity

    airColor = AirColorField(default_value=(0.6000000238418579, 0.800000011920929, 1.0))
    acl = airColor
    airColorR = airColor.airColorR
    acr = airColorR
    airColorG = airColor.airColorG
    acg = airColorG
    airColorB = airColor.airColorB
    acb = airColorB

    airOpacity = AirOpacityField(default_value=(0.3700000047683716, 0.4699999988079071, 0.8999999761581421))
    aop = airOpacity
    airOpacityR = airOpacity.airOpacityR
    aor = airOpacityR
    airOpacityG = airOpacity.airOpacityG
    aog = airOpacityG
    airOpacityB = airOpacity.airOpacityB
    aob = airOpacityB

    airMinHeight = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=1000.0)
    amh = airMinHeight

    airMaxHeight = DoubleField(default_value=50.0, soft_min_value=0.0, soft_max_value=1000.0)
    axh = airMaxHeight

    airDecay = DoubleField(default_value=0.1, soft_min_value=0.0, soft_max_value=1.0)
    adc = airDecay

    airLightScatter = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    alc = airLightScatter

    waterDensity = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=0.1)
    wdn = waterDensity

    waterColor = WaterColorField(default_value=(0.6000000238418579, 0.800000011920929, 1.0))
    wcl = waterColor
    waterColorR = waterColor.waterColorR
    wcr = waterColorR
    waterColorG = waterColor.waterColorG
    wcg = waterColorG
    waterColorB = waterColor.waterColorB
    wcb = waterColorB

    waterOpacity = WaterOpacityField(default_value=(0.3700000047683716, 0.4699999988079071, 0.8999999761581421))
    wop = waterOpacity
    waterOpacityR = waterOpacity.waterOpacityR
    wor = waterOpacityR
    waterOpacityG = waterOpacity.waterOpacityG
    wog = waterOpacityG
    waterOpacityB = waterOpacity.waterOpacityB
    wob = waterOpacityB

    waterLevel = DoubleField(default_value=0.0, soft_min_value=-1000.0, soft_max_value=0.0)
    wlv = waterLevel

    waterDepth = DoubleField(default_value=50.0, soft_min_value=0.0, soft_max_value=1000.0)
    wdp = waterDepth

    waterLightDecay = DoubleField(default_value=2.0, soft_min_value=0.0, soft_max_value=10.0)
    wdc = waterLightDecay

    waterLightScatter = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    wlc = waterLightScatter

    planetRadius = DoubleField(default_value=1000.0, soft_min_value=0.0, soft_max_value=10000.0)
    prd = planetRadius

    fogAxis = FogAxisEnumField(default_value=2)
    fax = fogAxis

    sunIntensity = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    sin = sunIntensity

    sunAzimuth = DoubleField(default_value=0.0, soft_min_value=-180.0, soft_max_value=180.0)
    saz = sunAzimuth

    sunElevation = DoubleField(default_value=45.0, soft_min_value=0.0, soft_max_value=90.0)
    sel = sunElevation

    sunColor = SunColorField(default_value=(1.0, 1.0, 1.0))
    snc = sunColor
    sunColorR = sunColor.sunColorR
    snr = sunColorR
    sunColorG = sunColor.sunColorG
    sng = sunColorG
    sunColorB = sunColor.sunColorB
    snb = sunColorB
