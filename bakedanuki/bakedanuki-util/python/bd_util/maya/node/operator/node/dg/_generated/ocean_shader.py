# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ocean_shader import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.time import TimeField


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


class GeneratedOceanShader(DG):
    __slots__ = ()

    NODE_TYPE = "oceanShader"

    objectId = AddrField(default_value=0.0, readable=False)
    oi = objectId

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    raySampler = AddrField(default_value=0.0, readable=False)
    rtr = raySampler

    rayDepth = ShortField(default_value=0, readable=False)
    rd = rayDepth

    rayInstance = LongField(default_value=0, readable=False)
    ryi = rayInstance

    refractionLimit = ShortField(default_value=6, min_value=0, soft_max_value=10)
    rdl = refractionLimit

    refractiveIndex = FloatField(default_value=1.2999999523162842, min_value=0.01, soft_max_value=3.0)
    rfi = refractiveIndex

    mediumRefractiveIndex = FloatField(default_value=1.0, readable=False)
    mrfi = mediumRefractiveIndex

    refractions = BoolField(default_value=False)
    rfc = refractions

    diffuse = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    dc = diffuse

    rayDirection = RayDirectionField(default_value=(0.0, 0.0, 1.0), readable=False)
    rad = rayDirection
    rayDirectionX = rayDirection.rayDirectionX
    rdx = rayDirectionX
    rayDirectionY = rayDirection.rayDirectionY
    rdy = rayDirectionY
    rayDirectionZ = rayDirection.rayDirectionZ
    rdz = rayDirectionZ

    waterColor = WaterColorField(default_value=(0.0, 0.36000001430511475, 0.4000000059604645))
    wc = waterColor
    waterColorR = waterColor.waterColorR
    wcr = waterColorR
    waterColorG = waterColor.waterColorG
    wcg = waterColorG
    waterColorB = waterColor.waterColorB
    wcb = waterColorB

    transparency = TransparencyField(default_value=(0.0, 0.0, 0.0))
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    ambientColor = AmbientColorField(default_value=(0.0, 0.0, 0.0))
    ambc = ambientColor
    ambientColorR = ambientColor.ambientColorR
    acr = ambientColorR
    ambientColorG = ambientColor.ambientColorG
    acg = ambientColorG
    ambientColorB = ambientColor.ambientColorB
    acb = ambientColorB

    incandescence = IncandescenceField(default_value=(0.0, 0.0, 0.0))
    ic = incandescence
    incandescenceR = incandescence.incandescenceR
    ir = incandescenceR
    incandescenceG = incandescence.incandescenceG
    ig = incandescenceG
    incandescenceB = incandescence.incandescenceB
    ib = incandescenceB

    translucence = FloatField(default_value=0.30000001192092896, soft_min_value=0.0, soft_max_value=1.0)
    tc = translucence

    translucenceFocus = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    tcf = translucenceFocus

    translucenceDepth = FloatField(default_value=10.0, soft_min_value=0.0, soft_max_value=20.0)
    trsd = translucenceDepth

    opacityDepth = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=5.0)
    opad = opacityDepth

    glowIntensity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    gi = glowIntensity

    specularGlow = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    spg = specularGlow

    shadowAttenuation = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    fakc = shadowAttenuation

    eccentricity = FloatField(default_value=0.029999999329447746, soft_min_value=0.0, soft_max_value=1.0)
    ec = eccentricity

    specularity = FloatField(default_value=0.699999988079071, soft_min_value=0.0, soft_max_value=1.0)
    spl = specularity

    reflectionLimit = ShortField(default_value=1, min_value=0, soft_max_value=10)
    fll = reflectionLimit

    specularColor = SpecularColorField(default_value=(1.0, 1.0, 1.0))
    sc = specularColor
    specularColorR = specularColor.specularColorR
    sr = specularColorR
    specularColorG = specularColor.specularColorG
    sg = specularColorG
    specularColorB = specularColor.specularColorB
    sb = specularColorB

    reflectivity = FloatField(default_value=0.699999988079071, min_value=0.0, soft_max_value=1.0)
    rfl = reflectivity

    environment = EnvironmentField(multi=True)
    env = environment

    environment_ColorR = FloatField()
    envcr = environment_ColorR

    environment_ColorG = FloatField()
    envcg = environment_ColorG

    environment_ColorB = FloatField()
    envcb = environment_ColorB

    reflectedColor = ReflectedColorField(default_value=(0.0, 0.0, 0.0))
    rc = reflectedColor
    reflectedColorR = reflectedColor.reflectedColorR
    rr = reflectedColorR
    reflectedColorG = reflectedColor.reflectedColorG
    rg = reflectedColorG
    reflectedColorB = reflectedColor.reflectedColorB
    rb = reflectedColorB

    triangleNormalCamera = TriangleNormalCameraField(default_value=(0.0, 1.0, 0.0))
    tnc = triangleNormalCamera
    triangleNormalCameraX = triangleNormalCamera.triangleNormalCameraX
    tnx = triangleNormalCameraX
    triangleNormalCameraY = triangleNormalCamera.triangleNormalCameraY
    tny = triangleNormalCameraY
    triangleNormalCameraZ = triangleNormalCamera.triangleNormalCameraZ
    tnz = triangleNormalCameraZ

    reflectionSpecularity = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    rsp = reflectionSpecularity

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

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    pointCamera = PointCameraField(default_value=(1.0, 1.0, 1.0))
    pc = pointCamera
    pointCameraX = pointCamera.pointCameraX
    px = pointCameraX
    pointCameraY = pointCamera.pointCameraY
    py = pointCameraY
    pointCameraZ = pointCamera.pointCameraZ
    pz = pointCameraZ

    normalCamera = NormalCameraField(default_value=(1.0, 1.0, 1.0))
    n = normalCamera
    normalCameraX = normalCamera.normalCameraX
    nx = normalCameraX
    normalCameraY = normalCamera.normalCameraY
    ny = normalCameraY
    normalCameraZ = normalCamera.normalCameraZ
    nz = normalCameraZ

    filterSize = FilterSizeField(default_value=(0.0, 0.0, 0.0))
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

    time = TimeField(default_value=0.0)
    ti = time

    scale = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.01, soft_max_value=10.0)
    scl = scale

    windUV = WindUVField(default_value=(1.0, 0.0), min_value=(-1.0, -1.0), max_value=(1.0, 1.0))
    wi = windUV
    windU = windUV.windU
    wiu = windU
    windV = windUV.windV
    wiv = windV

    observerSpeed = FloatField(default_value=0.0, min_value=0.0, soft_max_value=2.0)
    os = observerSpeed

    waveDirSpread = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=1.0)
    wd = waveDirSpread

    numFrequencies = FloatField(default_value=3.0, min_value=0.0, soft_max_value=10.0)
    nf = numFrequencies

    waveLengthMin = FloatField(default_value=0.30000001192092896, min_value=0.0, soft_min_value=0.001, soft_max_value=10.0)
    wlm = waveLengthMin

    waveLengthMax = FloatField(default_value=4.0, min_value=0.0, soft_min_value=0.001, soft_max_value=10.0)
    wlx = waveLengthMax

    waveHeight = WaveHeightField(multi=True, default_value=(0.0, 0.0, 0.0))
    wh = waveHeight

    waveTurbulence = WaveTurbulenceField(multi=True, default_value=(0.0, 0.0, 0.0))
    wtb = waveTurbulence

    wavePeaking = WavePeakingField(multi=True, default_value=(0.0, 0.0, 0.0))
    wp = wavePeaking

    waveHeightOffset = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    who = waveHeightOffset

    troughShadowing = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)
    tsh = troughShadowing

    foamColor = FoamColorField(default_value=(1.0, 1.0, 1.0))
    fc = foamColor
    foamColorR = foamColor.foamColorR
    fcr = foamColorR
    foamColorG = foamColor.foamColorG
    fcg = foamColorG
    foamColorB = foamColor.foamColorB
    fcb = foamColorB

    foamEmission = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fme = foamEmission

    foamThreshold = FloatField(default_value=0.5099999904632568, soft_min_value=0.0, soft_max_value=1.0)
    fmt = foamThreshold

    foamOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fmo = foamOffset

    outFoam = FloatField(default_value=0.0, writable=False)
    ofm = outFoam

    displacement = FloatField(default_value=0.0)
    d = displacement

    bumpBlur = FloatField(default_value=0.10000000149011612, min_value=1e-05, soft_max_value=1.0)
    bbl = bumpBlur

    horizonFilter = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    hft = horizonFilter

    waveSpeed = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    wvs = waveSpeed

    refPointCamera = RefPointCameraField(default_value=(0.0, 0.0, 0.0))
    rpc = refPointCamera
    refPointCameraX = refPointCamera.refPointCameraX
    rcx = refPointCameraX
    refPointCameraY = refPointCamera.refPointCameraY
    rcy = refPointCameraY
    refPointCameraZ = refPointCamera.refPointCameraZ
    rcz = refPointCameraZ
