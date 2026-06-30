# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.psd_file_tex import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.char import CharField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField


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


class PsdFileTex(DG):
    __slots__ = ()

    NODE_TYPE = "psdFileTex"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    u = uCoord
    vCoord = uvCoord.vCoord
    v = vCoord

    uvFilterSize = UvFilterSizeField()
    fs = uvFilterSize
    uvFilterSizeX = uvFilterSize.uvFilterSizeX
    fsx = uvFilterSizeX
    uvFilterSizeY = uvFilterSize.uvFilterSizeY
    fsy = uvFilterSizeY

    filter = FloatField()
    f = filter

    filterOffset = FloatField()
    fo = filterOffset

    invert = BoolField()
    i = invert

    alphaIsLuminance = BoolField()
    ail = alphaIsLuminance

    colorGain = ColorGainField()
    cg = colorGain
    colorGainR = colorGain.colorGainR
    cgr = colorGainR
    colorGainG = colorGain.colorGainG
    cgg = colorGainG
    colorGainB = colorGain.colorGainB
    cgb = colorGainB

    colorOffset = ColorOffsetField()
    co = colorOffset
    colorOffsetR = colorOffset.colorOffsetR
    cor = colorOffsetR
    colorOffsetG = colorOffset.colorOffsetG
    cog = colorOffsetG
    colorOffsetB = colorOffset.colorOffsetB
    cob = colorOffsetB

    alphaGain = FloatField()
    ag = alphaGain

    alphaOffset = FloatField()
    ao = alphaOffset

    defaultColor = DefaultColorField()
    dc = defaultColor
    defaultColorR = defaultColor.defaultColorR
    dcr = defaultColorR
    defaultColorG = defaultColor.defaultColorG
    dcg = defaultColorG
    defaultColorB = defaultColor.defaultColorB
    dcb = defaultColorB

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

    fileTextureName = DataStringField()
    ftn = fileTextureName

    fileTextureNamePattern = DataStringField()
    ftnp = fileTextureNamePattern

    computedFileTextureNamePattern = DataStringField()
    cfnp = computedFileTextureNamePattern

    disableFileLoad = BoolField()
    dfl = disableFileLoad

    useFrameExtension = BoolField()
    ufe = useFrameExtension

    frameExtension = LongField()
    fe = frameExtension

    frameOffset = LongField()
    io = frameOffset

    useHardwareTextureCycling = BoolField()
    uhc = useHardwareTextureCycling

    startCycleExtension = LongField()
    sce = startCycleExtension

    endCycleExtension = LongField()
    ece = endCycleExtension

    byCycleIncrement = LongField()
    bci = byCycleIncrement

    forceSwatchGen = BoolField()
    fsg = forceSwatchGen

    filterType = FilterTypeEnumField()
    ft = filterType

    filterWidth = FloatField()
    fw = filterWidth

    preFilter = BoolField()
    pf = preFilter

    preFilterRadius = FloatField()
    pfr = preFilterRadius

    useCache = BoolField()
    uca = useCache

    useMaximumRes = BoolField()
    umr = useMaximumRes

    uvTilingMode = UvTilingModeEnumField()
    uvt = uvTilingMode

    explicitUvTiles = ExplicitUvTilesField(multi=True)
    euvt = explicitUvTiles

    # TODO: explicitUvTiles.explicitUvTilePositionU (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: explicitUvTiles.explicitUvTilePositionV (attributeType=None, dataType=None) は未対応のため手動で追加してください

    baseExplicitUvTilePosition = BaseExplicitUvTilePositionField()
    butp = baseExplicitUvTilePosition
    baseExplicitUvTilePositionU = baseExplicitUvTilePosition.baseExplicitUvTilePositionU
    bupu = baseExplicitUvTilePositionU
    baseExplicitUvTilePositionV = baseExplicitUvTilePosition.baseExplicitUvTilePositionV
    bupv = baseExplicitUvTilePositionV

    uvTileProxyDirty = BoolField()
    utpd = uvTileProxyDirty

    uvTileProxyGenerate = BoolField()
    utpg = uvTileProxyGenerate

    uvTileProxyQuality = UvTileProxyQualityEnumField()
    utpq = uvTileProxyQuality

    coverage = CoverageField()
    c = coverage
    coverageU = coverage.coverageU
    cu = coverageU
    coverageV = coverage.coverageV
    cv = coverageV

    translateFrame = TranslateFrameField()
    tf = translateFrame
    translateFrameU = translateFrame.translateFrameU
    tfu = translateFrameU
    translateFrameV = translateFrame.translateFrameV
    tfv = translateFrameV

    rotateFrame = DoubleAngleField()
    rf = rotateFrame

    doTransform = BoolField()
    dtf = doTransform

    mirrorU = BoolField()
    mu = mirrorU

    mirrorV = BoolField()
    mv = mirrorV

    stagger = BoolField()
    s = stagger

    wrapU = BoolField()
    wu = wrapU

    wrapV = BoolField()
    wv = wrapV

    repeatUV = RepeatUVField()
    re = repeatUV
    repeatU = repeatUV.repeatU
    reu = repeatU
    repeatV = repeatUV.repeatV
    rev = repeatV

    offset = OffsetField()
    of = offset
    offsetU = offset.offsetU
    ofu = offsetU
    offsetV = offset.offsetV
    ofv = offsetV

    rotateUV = DoubleAngleField()
    ro = rotateUV

    noiseUV = NoiseUVField()
    n = noiseUV
    noiseU = noiseUV.noiseU
    nu = noiseU
    noiseV = noiseUV.noiseV
    nv = noiseV

    blurPixelation = BoolField()
    blp = blurPixelation

    vertexCameraOne = VertexCameraOneField()
    vc1 = vertexCameraOne
    vertexCameraOneX = vertexCameraOne.vertexCameraOneX
    c1x = vertexCameraOneX
    vertexCameraOneY = vertexCameraOne.vertexCameraOneY
    c1y = vertexCameraOneY
    vertexCameraOneZ = vertexCameraOne.vertexCameraOneZ
    c1z = vertexCameraOneZ

    vertexCameraTwo = VertexCameraTwoField()
    vc2 = vertexCameraTwo
    vertexCameraTwoX = vertexCameraTwo.vertexCameraTwoX
    c2x = vertexCameraTwoX
    vertexCameraTwoY = vertexCameraTwo.vertexCameraTwoY
    c2y = vertexCameraTwoY
    vertexCameraTwoZ = vertexCameraTwo.vertexCameraTwoZ
    c2z = vertexCameraTwoZ

    vertexCameraThree = VertexCameraThreeField()
    vc3 = vertexCameraThree
    vertexCameraThreeX = vertexCameraThree.vertexCameraThreeX
    c3x = vertexCameraThreeX
    vertexCameraThreeY = vertexCameraThree.vertexCameraThreeY
    c3y = vertexCameraThreeY
    vertexCameraThreeZ = vertexCameraThree.vertexCameraThreeZ
    c3z = vertexCameraThreeZ

    vertexUvOne = VertexUvOneField()
    vt1 = vertexUvOne
    vertexUvOneU = vertexUvOne.vertexUvOneU
    t1u = vertexUvOneU
    vertexUvOneV = vertexUvOne.vertexUvOneV
    t1v = vertexUvOneV

    vertexUvTwo = VertexUvTwoField()
    vt2 = vertexUvTwo
    vertexUvTwoU = vertexUvTwo.vertexUvTwoU
    t2u = vertexUvTwoU
    vertexUvTwoV = vertexUvTwo.vertexUvTwoV
    t2v = vertexUvTwoV

    vertexUvThree = VertexUvThreeField()
    vt3 = vertexUvThree
    vertexUvThreeU = vertexUvThree.vertexUvThreeU
    t3u = vertexUvThreeU
    vertexUvThreeV = vertexUvThree.vertexUvThreeV
    t3v = vertexUvThreeV

    objectType = CharField()
    otp = objectType

    rayDepth = LongField()
    rdp = rayDepth

    primitiveId = LongField()
    pi = primitiveId

    pixelCenter = PixelCenterField()
    pct = pixelCenter
    pixelCenterX = pixelCenter.pixelCenterX
    pcx = pixelCenterX
    pixelCenterY = pixelCenter.pixelCenterY
    pcy = pixelCenterY

    exposure = FloatField()
    exp = exposure

    hdrMapping = HdrMappingEnumField()
    hm = hdrMapping

    hdrExposure = FloatField()
    he = hdrExposure

    dirtyPixelRegion = BoolField()
    dp = dirtyPixelRegion

    ptexFilterType = PtexFilterTypeEnumField()
    pft = ptexFilterType

    ptexFilterWidth = FloatField()
    pfw = ptexFilterWidth

    ptexFilterBlur = FloatField()
    pfb = ptexFilterBlur

    ptexFilterSharpness = FloatField()
    pfs = ptexFilterSharpness

    ptexFilterInterpolateLevels = BoolField()
    pfil = ptexFilterInterpolateLevels

    colorProfile = LongField()
    cp = colorProfile

    colorSpace = DataStringField()
    cs = colorSpace

    ignoreColorSpaceFileRules = BoolField()
    ifr = ignoreColorSpaceFileRules

    viewNameUsed = BoolField()
    vinu = viewNameUsed

    viewNameStr = DataStringField()
    vin = viewNameStr

    workingSpace = DataStringField()
    ws = workingSpace

    colorManagementEnabled = BoolField()
    cme = colorManagementEnabled

    colorManagementConfigFileEnabled = BoolField()
    cmcf = colorManagementConfigFileEnabled

    colorManagementConfigFilePath = DataStringField()
    cmcp = colorManagementConfigFilePath

    outSize = OutSizeField()
    os = outSize
    outSizeX = outSize.outSizeX
    osx = outSizeX
    outSizeY = outSize.outSizeY
    osy = outSizeY

    fileHasAlpha = BoolField()
    fha = fileHasAlpha

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    infoBits = LongField()
    ib = infoBits

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    aiFilter = AiFilterEnumField()
    ai_filter = aiFilter

    aiAutoTx = BoolField()
    autotx = aiAutoTx

    aiMipBias = LongField()
    ai_mipmap_bias = aiMipBias

    aiUseDefaultColor = BoolField()
    ai_ignore_missing_textures = aiUseDefaultColor

    layerSetName = DataStringField()
    lsn = layerSetName

    layerSets = DataStringArrayField()
    lys = layerSets

    layerDepths = TypedField()
    lyd = layerDepths

    alpha = DataStringField()
    alp = alpha

    alphaList = DataStringArrayField()
    als = alphaList

    layerIds = TypedField()
    lid = layerIds
