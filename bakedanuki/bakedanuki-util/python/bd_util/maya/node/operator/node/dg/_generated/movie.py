# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.movie import (
    BaseExplicitUvTilePositionField,
    ColorGainField,
    ColorOffsetField,
    CoverageField,
    DefaultColorField,
    ExplicitUvTilesField,
    NoiseUVField,
    OffsetField,
    OutColorField,
    OutSizeField,
    OutTransparencyField,
    PixelCenterField,
    RepeatUVField,
    TranslateFrameField,
    UvCoordField,
    UvFilterSizeField,
    VertexCameraOneField,
    VertexCameraThreeField,
    VertexCameraTwoField,
    VertexUvOneField,
    VertexUvThreeField,
    VertexUvTwoField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.char import CharField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.dt.string import DataStringField


class FilterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    MIPMAP = 1
    BOX = 2
    QUADRATIC = 3
    QUARTIC = 4
    GAUSSIAN = 5


class FilterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    MIPMAP = 1
    BOX = 2
    QUADRATIC = 3
    QUARTIC = 4
    GAUSSIAN = 5

    NAME_MAP = {
        OFF: "Off",
        MIPMAP: "Mipmap",
        BOX: "Box",
        QUADRATIC: "Quadratic",
        QUARTIC: "Quartic",
        GAUSSIAN: "Gaussian",
    }


class FilterTypeEnumField(
    EnumField[FilterTypeEnumAttrOperator, FilterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterTypeEnumAttrOperator
    PLUG_CLS = FilterTypeEnumPlugOperator


class UvTilingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    _0_MINUS_BASED_ZBRUSH = 1
    _1_MINUS_BASED_MUDBOX = 2
    UDIM_MARI = 3
    EXPLICIT_TILES = 4


class UvTilingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    _0_MINUS_BASED_ZBRUSH = 1
    _1_MINUS_BASED_MUDBOX = 2
    UDIM_MARI = 3
    EXPLICIT_TILES = 4

    NAME_MAP = {
        OFF: "Off",
        _0_MINUS_BASED_ZBRUSH: "0-based (ZBrush)",
        _1_MINUS_BASED_MUDBOX: "1-based (Mudbox)",
        UDIM_MARI: "UDIM (Mari)",
        EXPLICIT_TILES: "Explicit Tiles",
    }


class UvTilingModeEnumField(
    EnumField[UvTilingModeEnumAttrOperator, UvTilingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvTilingModeEnumAttrOperator
    PLUG_CLS = UvTilingModeEnumPlugOperator


class UvTileProxyQualityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLE_PREVIEW = 0
    LOW_QUALITY_1K = 1
    MEDIUM_QUALITY_2K = 2
    HIGH_QUALITY_4K = 3
    ULTRA_HIGH_QUALITY_8K = 4
    EXTREME_HIGH_QUALITY_16K = 5


class UvTileProxyQualityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLE_PREVIEW = 0
    LOW_QUALITY_1K = 1
    MEDIUM_QUALITY_2K = 2
    HIGH_QUALITY_4K = 3
    ULTRA_HIGH_QUALITY_8K = 4
    EXTREME_HIGH_QUALITY_16K = 5

    NAME_MAP = {
        DISABLE_PREVIEW: "Disable Preview",
        LOW_QUALITY_1K: "Low Quality 1k",
        MEDIUM_QUALITY_2K: "Medium Quality 2k",
        HIGH_QUALITY_4K: "High Quality 4k",
        ULTRA_HIGH_QUALITY_8K: "Ultra High Quality 8k",
        EXTREME_HIGH_QUALITY_16K: "Extreme High Quality 16k",
    }


class UvTileProxyQualityEnumField(
    EnumField[UvTileProxyQualityEnumAttrOperator, UvTileProxyQualityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvTileProxyQualityEnumAttrOperator
    PLUG_CLS = UvTileProxyQualityEnumPlugOperator


class HdrMappingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLAMP = 0
    LINEAR = 1
    EXPONENTIAL = 2


class HdrMappingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLAMP = 0
    LINEAR = 1
    EXPONENTIAL = 2

    NAME_MAP = {
        CLAMP: "Clamp",
        LINEAR: "Linear",
        EXPONENTIAL: "Exponential",
    }


class HdrMappingEnumField(
    EnumField[HdrMappingEnumAttrOperator, HdrMappingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HdrMappingEnumAttrOperator
    PLUG_CLS = HdrMappingEnumPlugOperator


class PtexFilterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINT = 0
    BILINEAR = 1
    BOX = 2
    GAUSSIAN = 3
    BICUBIC = 4
    B_MINUS_SPLINE = 5
    CATMULL_MINUS_ROM = 6
    MITCHELL = 7


class PtexFilterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POINT = 0
    BILINEAR = 1
    BOX = 2
    GAUSSIAN = 3
    BICUBIC = 4
    B_MINUS_SPLINE = 5
    CATMULL_MINUS_ROM = 6
    MITCHELL = 7

    NAME_MAP = {
        POINT: "Point",
        BILINEAR: "Bilinear",
        BOX: "Box",
        GAUSSIAN: "Gaussian",
        BICUBIC: "Bicubic",
        B_MINUS_SPLINE: "B-spline",
        CATMULL_MINUS_ROM: "Catmull-Rom",
        MITCHELL: "Mitchell",
    }


class PtexFilterTypeEnumField(
    EnumField[PtexFilterTypeEnumAttrOperator, PtexFilterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PtexFilterTypeEnumAttrOperator
    PLUG_CLS = PtexFilterTypeEnumPlugOperator


class AiFilterEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    BILINEAR = 1
    BICUBIC = 2
    SMART_BICUBIC = 3


class AiFilterEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    BILINEAR = 1
    BICUBIC = 2
    SMART_BICUBIC = 3

    NAME_MAP = {
        CLOSEST: "closest",
        BILINEAR: "bilinear",
        BICUBIC: "bicubic",
        SMART_BICUBIC: "smart_bicubic",
    }


class AiFilterEnumField(
    EnumField[AiFilterEnumAttrOperator, AiFilterEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiFilterEnumAttrOperator
    PLUG_CLS = AiFilterEnumPlugOperator


class _GeneratedMovie(DG):
    __slots__ = ()

    NODE_TYPE = "movie"

    uvCoord = UvCoordField(default_value=(0.0, 0.0))
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField(default_value=(0.0, 0.0))
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    f = filter

    filterOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    fo = filterOffset

    invert = BoolField(default_value=False)
    i = invert

    alphaIsLuminance = BoolField(default_value=False)
    ail = alphaIsLuminance

    colorGain = ColorGainField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(2.0, 2.0, 2.0))
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    ag = alphaGain

    alphaOffset = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    ao = alphaOffset

    defaultColor = DefaultColorField(default_value=(0.5, 0.5, 0.5), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

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

    fileTextureName = DataStringField()
    ftn = fileTextureName

    fileTextureNamePattern = DataStringField()
    ftnp = fileTextureNamePattern

    computedFileTextureNamePattern = DataStringField()
    cfnp = computedFileTextureNamePattern

    disableFileLoad = BoolField(default_value=False)
    dfl = disableFileLoad

    useFrameExtension = BoolField(default_value=False)
    ufe = useFrameExtension

    frameExtension = LongField(default_value=1)
    fe = frameExtension

    frameOffset = LongField(default_value=0)
    io = frameOffset

    useHardwareTextureCycling = BoolField(default_value=False)
    uhc = useHardwareTextureCycling

    startCycleExtension = LongField(default_value=1)
    sce = startCycleExtension

    endCycleExtension = LongField(default_value=1)
    ece = endCycleExtension

    byCycleIncrement = LongField(default_value=1, min_value=1)
    bci = byCycleIncrement

    forceSwatchGen = BoolField(default_value=False)
    fsg = forceSwatchGen

    filterType = FilterTypeEnumField(default_value=3)
    ft = filterType

    filterWidth = FloatField(default_value=0.7070000171661377, min_value=0.35, max_value=1.05)
    fw = filterWidth

    preFilter = BoolField(default_value=False)
    pf = preFilter

    preFilterRadius = FloatField(default_value=2.0, min_value=1.0, max_value=10.0)
    pfr = preFilterRadius

    useCache = BoolField(default_value=False)
    uca = useCache

    useMaximumRes = BoolField(default_value=False)
    umr = useMaximumRes

    uvTilingMode = UvTilingModeEnumField(default_value=0)
    uvt = uvTilingMode

    explicitUvTiles = ExplicitUvTilesField(multi=True)
    euvt = explicitUvTiles

    explicitUvTilePositionU = FloatField()
    eupu = explicitUvTilePositionU

    explicitUvTilePositionV = FloatField()
    eupv = explicitUvTilePositionV

    baseExplicitUvTilePosition = BaseExplicitUvTilePositionField(default_value=(0.0, 0.0))
    butp = baseExplicitUvTilePosition
    baseExplicitUvTilePositionU = baseExplicitUvTilePosition.baseExplicitUvTilePositionU
    bupu = baseExplicitUvTilePositionU
    baseExplicitUvTilePositionV = baseExplicitUvTilePosition.baseExplicitUvTilePositionV
    bupv = baseExplicitUvTilePositionV

    uvTileProxyDirty = BoolField(default_value=True)
    utpd = uvTileProxyDirty

    uvTileProxyGenerate = BoolField(default_value=False)
    utpg = uvTileProxyGenerate

    uvTileProxyQuality = UvTileProxyQualityEnumField(default_value=3)
    utpq = uvTileProxyQuality

    coverage = CoverageField(default_value=(1.0, 1.0), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    c = coverage
    coverageU = coverage.coverageU
    cu = coverageU
    coverageV = coverage.coverageV
    cv = coverageV

    translateFrame = TranslateFrameField(default_value=(0.0, 0.0), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    tf = translateFrame
    translateFrameU = translateFrame.translateFrameU
    tfu = translateFrameU
    translateFrameV = translateFrame.translateFrameV
    tfv = translateFrameV

    rotateFrame = DoubleAngleField(default_value=0.0)
    rf = rotateFrame

    doTransform = BoolField(default_value=True)
    dtf = doTransform

    mirrorU = BoolField(default_value=False)
    mu = mirrorU

    mirrorV = BoolField(default_value=False)
    mv = mirrorV

    stagger = BoolField(default_value=False)
    s = stagger

    wrapU = BoolField(default_value=True)
    wu = wrapU

    wrapV = BoolField(default_value=True)
    wv = wrapV

    repeatUV = RepeatUVField(default_value=(1.0, 1.0), min_value=(0.0, 0.0))
    re = repeatUV
    repeatU = repeatUV.repeatU
    reu = repeatU
    repeatV = repeatUV.repeatV
    rev = repeatV

    offset = OffsetField(default_value=(0.0, 0.0), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    of = offset
    offsetU = offset.offsetU
    ofu = offsetU
    offsetV = offset.offsetV
    ofv = offsetV

    rotateUV = DoubleAngleField(default_value=0.0)
    ro = rotateUV

    noiseUV = NoiseUVField(default_value=(0.0, 0.0), min_value=(0.0, 0.0))
    n = noiseUV
    noiseU = noiseUV.noiseU
    nu = noiseU
    noiseV = noiseUV.noiseV
    nv = noiseV

    blurPixelation = BoolField(default_value=True)
    blp = blurPixelation

    vertexCameraOne = VertexCameraOneField(default_value=(0.0, 0.0, 0.0))
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField(default_value=(0.0, 0.0, 0.0))
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    vertexCameraThree = VertexCameraThreeField(default_value=(0.0, 0.0, 0.0))
    vc3 = vertexCameraThree
    vertexCameraThreeX = vertexCameraThree.vertexCameraThreeX
    c3x = vertexCameraThreeX
    vertexCameraThreeY = vertexCameraThree.vertexCameraThreeY
    c3y = vertexCameraThreeY
    vertexCameraThreeZ = vertexCameraThree.vertexCameraThreeZ
    c3z = vertexCameraThreeZ

    vertexUvOne = VertexUvOneField(default_value=(0.0, 0.0))
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField(default_value=(0.0, 0.0))
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexUvThree = VertexUvThreeField(default_value=(0.0, 0.0))
    vt3 = vertexUvThree
    vertexUvThreeU = vertexUvThree.vertexUvThreeU
    t3u = vertexUvThreeU
    vertexUvThreeV = vertexUvThree.vertexUvThreeV
    t3v = vertexUvThreeV

    objectType = CharField(default_value=0, min_value=0, max_value=255)
    otp = objectType

    rayDepth = LongField(default_value=0)
    rdp = rayDepth

    primitiveId = LongField(default_value=0, readable=False)
    pi = primitiveId

    pixelCenter = PixelCenterField(default_value=(0.0, 0.0))
    pct = pixelCenter
    pixelCenterX = pixelCenter.pixelCenterX
    pcx = pixelCenterX
    pixelCenterY = pixelCenter.pixelCenterY
    pcy = pixelCenterY

    exposure = FloatField(default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0)
    exp = exposure

    hdrMapping = HdrMappingEnumField(default_value=0)
    hm = hdrMapping

    hdrExposure = FloatField(default_value=0.0, min_value=-10.0, max_value=10.0)
    he = hdrExposure

    dirtyPixelRegion = BoolField(default_value=False)
    dp = dirtyPixelRegion

    ptexFilterType = PtexFilterTypeEnumField(default_value=3)
    pft = ptexFilterType

    ptexFilterWidth = FloatField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    pfw = ptexFilterWidth

    ptexFilterBlur = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    pfb = ptexFilterBlur

    ptexFilterSharpness = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    pfs = ptexFilterSharpness

    ptexFilterInterpolateLevels = BoolField(default_value=False)
    pfil = ptexFilterInterpolateLevels

    colorProfile = LongField(default_value=0)
    cp = colorProfile

    colorSpace = DataStringField()
    cs = colorSpace

    ignoreColorSpaceFileRules = BoolField(default_value=False)
    ifr = ignoreColorSpaceFileRules

    viewNameUsed = BoolField(default_value=False)
    vinu = viewNameUsed

    viewNameStr = DataStringField()
    vin = viewNameStr

    workingSpace = DataStringField()
    ws = workingSpace

    colorManagementEnabled = BoolField(default_value=False)
    cme = colorManagementEnabled

    colorManagementConfigFileEnabled = BoolField(default_value=False)
    cmcf = colorManagementConfigFileEnabled

    colorManagementConfigFilePath = DataStringField()
    cmcp = colorManagementConfigFilePath

    outSize = OutSizeField(default_value=(0.0, 0.0), writable=False)
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField(default_value=False, writable=False)
    fha = fileHasAlpha

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    infoBits = LongField(default_value=0)
    ib = infoBits

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiFilter = AiFilterEnumField(default_value=3, category="arnold")
    ai_filter = aiFilter

    aiAutoTx = BoolField(default_value=True, category="arnold")
    autotx = aiAutoTx

    aiMipBias = LongField(default_value=0, category="arnold")
    ai_mipmap_bias = aiMipBias

    aiUseDefaultColor = BoolField(default_value=True, category="arnold")
    ai_ignore_missing_textures = aiUseDefaultColor
