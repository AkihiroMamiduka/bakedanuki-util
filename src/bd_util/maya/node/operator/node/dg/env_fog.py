# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.env_fog import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class MatteOpacityModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACK_HOLE = 0
    SOLID_MATTE = 1
    OPACITY_GAIN = 2


class MatteOpacityModeEnumAttrOperator(EnumAttrOperator):
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


class DistanceClipPlanesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CAMERA_NEAR_SLASH_FAR = 0
    FOG_NEAR_SLASH_FAR = 1


class DistanceClipPlanesEnumAttrOperator(EnumAttrOperator):
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


class FogTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNIFORM_FOG = 0
    ATMOSPHERIC = 1
    SKY = 2
    WATER = 3
    WATER_SLASH_FOG = 4
    WATER_SLASH_ATMOS = 5
    WATER_SLASH_SKY = 6


class FogTypeEnumAttrOperator(EnumAttrOperator):
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


class FogAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    MINUS_X = 1
    Y = 2
    MINUS_Y = 3
    Z = 4
    MINUS_Z = 5


class FogAxisEnumAttrOperator(EnumAttrOperator):
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


class EnvFog(DG):
    __slots__ = ()

    NODE_TYPE = "envFog"

    filterSize = FilterSizeField()
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    lightDataArray = LightDataArrayField(multi=True)
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

    color = ColorField()
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    density = FloatField()
    d = density

    fastDropOff = BoolField()
    fd = fastDropOff

    colorBasedTransparency = BoolField()
    cbt = colorBasedTransparency

    matteOpacityMode = MatteOpacityModeEnumField()
    mom = matteOpacityMode

    matteOpacity = FloatField()
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField()
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    pointCamera = PointCameraField()
    p = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    pointWorld = PointWorldField()
    pw = pointWorld
    pointWorldX = pointWorld.pointWorldX
    pwx = pointWorldX
    pointWorldY = pointWorld.pointWorldY
    pwy = pointWorldY
    pointWorldZ = pointWorld.pointWorldZ
    pwz = pointWorldZ

    rayDirection = RayDirectionField()
    r = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    ry = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rz = rayDirectionZ

    distanceClipPlanes = DistanceClipPlanesEnumField()
    dcp = distanceClipPlanes

    useLayer = BoolField()
    ul = useLayer

    useHeight = BoolField()
    uh = useHeight

    blendRange = FloatField()
    br = blendRange

    saturationDistance = FloatField()
    sdt = saturationDistance

    fogNearDistance = FloatField()
    fnd = fogNearDistance

    fogFarDistance = FloatField()
    ffd = fogFarDistance

    layer = FloatField()
    l = layer

    minHeight = FloatField()
    mnh = minHeight

    maxHeight = FloatField()
    mxh = maxHeight

    useDistance = BoolField()
    ud = useDistance

    startDistance = FloatField()
    sd = startDistance

    endDistance = FloatField()
    ed = endDistance

    physicalFog = BoolField()
    sff = physicalFog

    fogType = FogTypeEnumField()
    ftp = fogType

    fogDensity = DoubleField()
    fdn = fogDensity

    fogColor = FogColorField()
    fcl = fogColor
    fogColorR = fogColor.fogColorR
    fcr = fogColorR
    fogColorG = fogColor.fogColorG
    fcg = fogColorG
    fogColorB = fogColor.fogColorB
    fcb = fogColorB

    fogOpacity = FogOpacityField()
    fop = fogOpacity
    fogOpacityR = fogOpacity.fogOpacityR
    for_ = fogOpacityR
    fogOpacityG = fogOpacity.fogOpacityG
    fog = fogOpacityG
    fogOpacityB = fogOpacity.fogOpacityB
    fob = fogOpacityB

    fogMinHeight = DoubleField()
    fmh = fogMinHeight

    fogMaxHeight = DoubleField()
    fxh = fogMaxHeight

    fogDecay = DoubleField()
    fdc = fogDecay

    fogLightScatter = DoubleField()
    flc = fogLightScatter

    airDensity = DoubleField()
    adn = airDensity

    airColor = AirColorField()
    acl = airColor
    airColorR = airColor.airColorR
    acr = airColorR
    airColorG = airColor.airColorG
    acg = airColorG
    airColorB = airColor.airColorB
    acb = airColorB

    airOpacity = AirOpacityField()
    aop = airOpacity
    airOpacityR = airOpacity.airOpacityR
    aor = airOpacityR
    airOpacityG = airOpacity.airOpacityG
    aog = airOpacityG
    airOpacityB = airOpacity.airOpacityB
    aob = airOpacityB

    airMinHeight = DoubleField()
    amh = airMinHeight

    airMaxHeight = DoubleField()
    axh = airMaxHeight

    airDecay = DoubleField()
    adc = airDecay

    airLightScatter = DoubleField()
    alc = airLightScatter

    waterDensity = DoubleField()
    wdn = waterDensity

    waterColor = WaterColorField()
    wcl = waterColor
    waterColorR = waterColor.waterColorR
    wcr = waterColorR
    waterColorG = waterColor.waterColorG
    wcg = waterColorG
    waterColorB = waterColor.waterColorB
    wcb = waterColorB

    waterOpacity = WaterOpacityField()
    wop = waterOpacity
    waterOpacityR = waterOpacity.waterOpacityR
    wor = waterOpacityR
    waterOpacityG = waterOpacity.waterOpacityG
    wog = waterOpacityG
    waterOpacityB = waterOpacity.waterOpacityB
    wob = waterOpacityB

    waterLevel = DoubleField()
    wlv = waterLevel

    waterDepth = DoubleField()
    wdp = waterDepth

    waterLightDecay = DoubleField()
    wdc = waterLightDecay

    waterLightScatter = DoubleField()
    wlc = waterLightScatter

    planetRadius = DoubleField()
    prd = planetRadius

    fogAxis = FogAxisEnumField()
    fax = fogAxis

    sunIntensity = DoubleField()
    sin = sunIntensity

    sunAzimuth = DoubleField()
    saz = sunAzimuth

    sunElevation = DoubleField()
    sel = sunElevation

    sunColor = SunColorField()
    snc = sunColor
    sunColorR = sunColor.sunColorR
    snr = sunColorR
    sunColorG = sunColor.sunColorG
    sng = sunColorG
    sunColorB = sunColor.sunColorB
    snb = sunColorB
