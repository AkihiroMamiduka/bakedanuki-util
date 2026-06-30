# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ocean_shader import (
    AmbientColorField,
    EnvironmentField,
    FilterSizeField,
    FoamColorField,
    IncandescenceField,
    LightDataArrayField,
    NormalCameraField,
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    PointCameraField,
    RayDirectionField,
    RefPointCameraField,
    ReflectedColorField,
    SpecularColorField,
    TransparencyField,
    TriangleNormalCameraField,
    WaterColorField,
    WaveHeightField,
    WavePeakingField,
    WaveTurbulenceField,
    WindUVField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField


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


class OceanShader(DG):
    __slots__ = ()

    NODE_TYPE = "oceanShader"

    objectId = AddrField()
    oi = objectId

    primitiveId = LongField()
    pi = primitiveId

    raySampler = AddrField()
    rtr = raySampler

    rayDepth = ShortField()
    rd = rayDepth

    rayInstance = LongField()
    ryi = rayInstance

    refractionLimit = ShortField()
    rdl = refractionLimit

    refractiveIndex = FloatField()
    rfi = refractiveIndex

    mediumRefractiveIndex = FloatField()
    mrfi = mediumRefractiveIndex

    refractions = BoolField()
    rfc = refractions

    diffuse = FloatField()
    dc = diffuse

    rayDirection = RayDirectionField()
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    waterColor = WaterColorField()
    wc = waterColor
    waterColorR = waterColor.waterColorR
    wcr = waterColorR
    waterColorG = waterColor.waterColorG
    wcg = waterColorG
    waterColorB = waterColor.waterColorB
    wcb = waterColorB

    transparency = TransparencyField()
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    ambientColor = AmbientColorField()
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField()
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    translucence = FloatField()
    tc = translucence

    translucenceFocus = FloatField()
    tcf = translucenceFocus

    translucenceDepth = FloatField()
    trsd = translucenceDepth

    opacityDepth = FloatField()
    opad = opacityDepth

    glowIntensity = FloatField()
    gi = glowIntensity

    specularGlow = FloatField()
    spg = specularGlow

    shadowAttenuation = FloatField()
    fakc = shadowAttenuation

    eccentricity = FloatField()
    ec = eccentricity

    specularity = FloatField()
    spl = specularity

    reflectionLimit = ShortField()
    fll = reflectionLimit

    specularColor = SpecularColorField()
    sc = specularColor
    specularColorR = specularColor.specularColorR
    sr = specularColorR
    specularColorG = specularColor.specularColorG
    sg = specularColorG
    specularColorB = specularColor.specularColorB
    sb = specularColorB

    reflectivity = FloatField()
    rfl = reflectivity

    environment = EnvironmentField(multi=True)
    env = environment

    # TODO: environment.environment_ColorR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: environment.environment_ColorG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: environment.environment_ColorB (attributeType=None, dataType=None) は未対応のため手動で追加してください

    reflectedColor = ReflectedColorField()
    rc = reflectedColor
    reflectedColorR = reflectedColor.reflectedColorR
    rr = reflectedColorR
    reflectedColorG = reflectedColor.reflectedColorG
    rg = reflectedColorG
    reflectedColorB = reflectedColor.reflectedColorB
    rb = reflectedColorB

    triangleNormalCamera = TriangleNormalCameraField()
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    reflectionSpecularity = FloatField()
    rsp = reflectionSpecularity

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

    outGlowColor = OutGlowColorField()
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    pointCamera = PointCameraField()
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField()
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    filterSize = FilterSizeField()
    fs = filterSize
    filterSizeX = filterSize.filterSizeX
    fsx = filterSizeX
    filterSizeY = filterSize.filterSizeY
    fsy = filterSizeY
    filterSizeZ = filterSize.filterSizeZ
    fsz = filterSizeZ

    matrixWorldToEye = FltMatrixField()
    wte = matrixWorldToEye

    matrixEyeToWorld = FltMatrixField()
    e2w = matrixEyeToWorld

    lightDataArray = LightDataArrayField(multi=True)
    ltd = lightDataArray

    # TODO: lightDataArray.lightDirectionX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightDirectionZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityR (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityG (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: lightDataArray.lightIntensityB (attributeType=None, dataType=None) は未対応のため手動で追加してください

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

    time = TimeField()
    ti = time

    scale = FloatField()
    scl = scale

    windUV = WindUVField()
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    observerSpeed = FloatField()
    os = observerSpeed

    waveDirSpread = FloatField()
    wd = waveDirSpread

    numFrequencies = FloatField()
    nf = numFrequencies

    waveLengthMin = FloatField()
    wlm = waveLengthMin

    waveLengthMax = FloatField()
    wlx = waveLengthMax

    waveHeight = WaveHeightField(multi=True)
    wh = waveHeight

    waveTurbulence = WaveTurbulenceField(multi=True)
    wtb = waveTurbulence

    wavePeaking = WavePeakingField(multi=True)
    wp = wavePeaking

    waveHeightOffset = FloatField()
    who = waveHeightOffset

    troughShadowing = FloatField()
    tsh = troughShadowing

    foamColor = FoamColorField()
    fc = foamColor
    foamColorR = foamColor.foamColorR
    fcr = foamColorR
    foamColorG = foamColor.foamColorG
    fcg = foamColorG
    foamColorB = foamColor.foamColorB
    fcb = foamColorB

    foamEmission = FloatField()
    fme = foamEmission

    foamThreshold = FloatField()
    fmt = foamThreshold

    foamOffset = FloatField()
    fmo = foamOffset

    outFoam = FloatField()
    ofm = outFoam

    displacement = FloatField()
    d = displacement

    bumpBlur = FloatField()
    bbl = bumpBlur

    horizonFilter = FloatField()
    hft = horizonFilter

    waveSpeed = FloatField()
    wvs = waveSpeed

    refPointCamera = RefPointCameraField()
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ
