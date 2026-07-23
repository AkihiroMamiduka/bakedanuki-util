# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.string import DataStringField


class ImageFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GIF = 0
    SOFTIMAGE = 1
    RLA = 2
    TIFF = 3
    TIFF16 = 4
    SGI = 5
    ALIAS_PIX = 6
    MAYA_IFF = 7
    JPEG = 8
    EPS = 9
    MAYA16_IFF = 10
    QUANTEL = 12
    SGI16 = 13
    TARGA = 19
    WINDOWS_BITMAP = 20
    SGI_MOVIE = 21
    QUICKTIME = 22
    AVI = 23
    MACPAINT = 30
    PSD = 31
    PNG = 32
    QUICKDRAW = 33
    QUICKTIME_IMAGE = 34
    DDS = 35
    PSD_LAYERED = 36
    EXR_EXR = 40
    IMF_PLUGIN = 50
    CUSTOM_IMAGE_FORMAT = 51
    MACROMEDIA_SWF_SWF = 60
    ADOBE_ILLUSTRATOR_AI = 61
    SVG_SVG = 62
    SWIFT3DIMPORTER_SWFT = 63


class ImageFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    GIF = 0
    SOFTIMAGE = 1
    RLA = 2
    TIFF = 3
    TIFF16 = 4
    SGI = 5
    ALIAS_PIX = 6
    MAYA_IFF = 7
    JPEG = 8
    EPS = 9
    MAYA16_IFF = 10
    QUANTEL = 12
    SGI16 = 13
    TARGA = 19
    WINDOWS_BITMAP = 20
    SGI_MOVIE = 21
    QUICKTIME = 22
    AVI = 23
    MACPAINT = 30
    PSD = 31
    PNG = 32
    QUICKDRAW = 33
    QUICKTIME_IMAGE = 34
    DDS = 35
    PSD_LAYERED = 36
    EXR_EXR = 40
    IMF_PLUGIN = 50
    CUSTOM_IMAGE_FORMAT = 51
    MACROMEDIA_SWF_SWF = 60
    ADOBE_ILLUSTRATOR_AI = 61
    SVG_SVG = 62
    SWIFT3DIMPORTER_SWFT = 63

    NAME_MAP = {
        GIF: "GIF",
        SOFTIMAGE: "SoftImage",
        RLA: "RLA",
        TIFF: "Tiff",
        TIFF16: "Tiff16",
        SGI: "SGI",
        ALIAS_PIX: "Alias PIX",
        MAYA_IFF: "Maya IFF",
        JPEG: "JPEG",
        EPS: "EPS",
        MAYA16_IFF: "Maya16 IFF",
        QUANTEL: "Quantel",
        SGI16: "SGI16",
        TARGA: "Targa",
        WINDOWS_BITMAP: "Windows Bitmap",
        SGI_MOVIE: "SGI Movie",
        QUICKTIME: "Quicktime",
        AVI: "AVI",
        MACPAINT: "MacPaint",
        PSD: "PSD",
        PNG: "PNG",
        QUICKDRAW: "QuickDraw",
        QUICKTIME_IMAGE: "QuickTime Image",
        DDS: "DDS",
        PSD_LAYERED: "PSD Layered",
        EXR_EXR: "EXR(exr)",
        IMF_PLUGIN: "IMF plugin",
        CUSTOM_IMAGE_FORMAT: "Custom Image Format",
        MACROMEDIA_SWF_SWF: "Macromedia SWF (swf)",
        ADOBE_ILLUSTRATOR_AI: "Adobe Illustrator (ai)",
        SVG_SVG: "SVG (svg)",
        SWIFT3DIMPORTER_SWFT: "Swift3DImporter (swft)",
    }


class ImageFormatEnumField(
    EnumField[ImageFormatEnumAttrOperator, ImageFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageFormatEnumAttrOperator
    PLUG_CLS = ImageFormatEnumPlugOperator


class BitDepthEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    UINT_MINUS_8 = 1
    UINT_MINUS_16 = 2
    FLOAT_MINUS_16 = 3
    FLOAT_MINUS_32 = 4


class BitDepthEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    UINT_MINUS_8 = 1
    UINT_MINUS_16 = 2
    FLOAT_MINUS_16 = 3
    FLOAT_MINUS_32 = 4

    NAME_MAP = {
        DEFAULT: "Default",
        UINT_MINUS_8: "uint-8",
        UINT_MINUS_16: "uint-16",
        FLOAT_MINUS_16: "float-16",
        FLOAT_MINUS_32: "float-32",
    }


class BitDepthEnumField(
    EnumField[BitDepthEnumAttrOperator, BitDepthEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BitDepthEnumAttrOperator
    PLUG_CLS = BitDepthEnumPlugOperator


class TiffCompressionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LZW = 1


class TiffCompressionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LZW = 1

    NAME_MAP = {
        NONE: "None",
        LZW: "LZW",
    }


class TiffCompressionEnumField(
    EnumField[TiffCompressionEnumAttrOperator, TiffCompressionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TiffCompressionEnumAttrOperator
    PLUG_CLS = TiffCompressionEnumPlugOperator


class ExrCompressionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    RLE = 1
    ZIPS = 2
    ZIP = 3
    PIZ = 4
    PXR24 = 5
    B44 = 6


class ExrCompressionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    RLE = 1
    ZIPS = 2
    ZIP = 3
    PIZ = 4
    PXR24 = 5
    B44 = 6

    NAME_MAP = {
        NONE: "None",
        RLE: "RLE",
        ZIPS: "ZIPS",
        ZIP: "ZIP",
        PIZ: "PIZ",
        PXR24: "PXR24",
        B44: "B44",
    }


class ExrCompressionEnumField(
    EnumField[ExrCompressionEnumAttrOperator, ExrCompressionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExrCompressionEnumAttrOperator
    PLUG_CLS = ExrCompressionEnumPlugOperator


class ExrPixelTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _32BIT_FLOAT = 0
    _16BIT_HALF = 1


class ExrPixelTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _32BIT_FLOAT = 0
    _16BIT_HALF = 1

    NAME_MAP = {
        _32BIT_FLOAT: "32bit Float",
        _16BIT_HALF: "16bit Half",
    }


class ExrPixelTypeEnumField(
    EnumField[ExrPixelTypeEnumAttrOperator, ExrPixelTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExrPixelTypeEnumAttrOperator
    PLUG_CLS = ExrPixelTypeEnumPlugOperator


class AnimationRangeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RENDER_SETTINGS = 0
    START_SLASH_END = 1


class AnimationRangeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RENDER_SETTINGS = 0
    START_SLASH_END = 1

    NAME_MAP = {
        RENDER_SETTINGS: "Render Settings",
        START_SLASH_END: "Start/End",
    }


class AnimationRangeEnumField(
    EnumField[AnimationRangeEnumAttrOperator, AnimationRangeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AnimationRangeEnumAttrOperator
    PLUG_CLS = AnimationRangeEnumPlugOperator


class FieldExtControlEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    O_AND_E = 0
    NONE = 1
    USER_INPUT = 2


class FieldExtControlEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    O_AND_E = 0
    NONE = 1
    USER_INPUT = 2

    NAME_MAP = {
        O_AND_E: ".o and .e",
        NONE: "None",
        USER_INPUT: "User Input",
    }


class FieldExtControlEnumField(
    EnumField[FieldExtControlEnumAttrOperator, FieldExtControlEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldExtControlEnumAttrOperator
    PLUG_CLS = FieldExtControlEnumPlugOperator


class OutFormatControlEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AS_OUTPUT_FORMAT = 0
    NONE = 1
    USER_INPUT = 2


class OutFormatControlEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AS_OUTPUT_FORMAT = 0
    NONE = 1
    USER_INPUT = 2

    NAME_MAP = {
        AS_OUTPUT_FORMAT: "As Output Format",
        NONE: "None",
        USER_INPUT: "User Input",
    }


class OutFormatControlEnumField(
    EnumField[OutFormatControlEnumAttrOperator, OutFormatControlEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutFormatControlEnumAttrOperator
    PLUG_CLS = OutFormatControlEnumPlugOperator


class PeriodInExtEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_PERIOD_OR_UNDERSCORE_IN_EXTENSION = 0
    PERIOD_IN_EXTENSION = 1
    UNDERSCORE_IN_EXTENSION = 2


class PeriodInExtEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_PERIOD_OR_UNDERSCORE_IN_EXTENSION = 0
    PERIOD_IN_EXTENSION = 1
    UNDERSCORE_IN_EXTENSION = 2

    NAME_MAP = {
        NO_PERIOD_OR_UNDERSCORE_IN_EXTENSION: "No Period or Underscore in Extension",
        PERIOD_IN_EXTENSION: "Period in Extension",
        UNDERSCORE_IN_EXTENSION: "Underscore in Extension",
    }


class PeriodInExtEnumField(
    EnumField[PeriodInExtEnumAttrOperator, PeriodInExtEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PeriodInExtEnumAttrOperator
    PLUG_CLS = PeriodInExtEnumPlugOperator


class MultiCamNamingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1


class MultiCamNamingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        CUSTOM: "Custom",
    }


class MultiCamNamingModeEnumField(
    EnumField[MultiCamNamingModeEnumAttrOperator, MultiCamNamingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiCamNamingModeEnumAttrOperator
    PLUG_CLS = MultiCamNamingModeEnumPlugOperator


class MotionBlurTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MOTION_BLUR_2D = 0
    MOTION_BLUR_3D = 1


class MotionBlurTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MOTION_BLUR_2D = 0
    MOTION_BLUR_3D = 1

    NAME_MAP = {
        MOTION_BLUR_2D: "Motion Blur 2D",
        MOTION_BLUR_3D: "Motion Blur 3D",
    }


class MotionBlurTypeEnumField(
    EnumField[MotionBlurTypeEnumAttrOperator, MotionBlurTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurTypeEnumAttrOperator
    PLUG_CLS = MotionBlurTypeEnumPlugOperator


class RenderedOutputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL_RENDERABLE = 0
    RENDER_TARGETS_ONLY = 1
    OMIT_RENDER_TARGETS = 2


class RenderedOutputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL_RENDERABLE = 0
    RENDER_TARGETS_ONLY = 1
    OMIT_RENDER_TARGETS = 2

    NAME_MAP = {
        ALL_RENDERABLE: "All Renderable",
        RENDER_TARGETS_ONLY: "Render Targets Only",
        OMIT_RENDER_TARGETS: "Omit Render Targets",
    }


class RenderedOutputEnumField(
    EnumField[RenderedOutputEnumAttrOperator, RenderedOutputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderedOutputEnumAttrOperator
    PLUG_CLS = RenderedOutputEnumPlugOperator


class _GeneratedRenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "renderGlobals"

    macCodec = LongField(default_value=1919706400)
    macc = macCodec

    macDepth = LongField(default_value=32)
    macd = macDepth

    macQual = LongField(default_value=1024)
    macq = macQual

    comFrrt = LongField(default_value=24)
    mcfr = comFrrt

    renderAll = BoolField(default_value=True)
    ra = renderAll

    ignoreFilmGate = BoolField(default_value=True)
    ifg = ignoreFilmGate

    quality = MessageField()
    qual = quality

    resolution = MessageField()
    res = resolution

    clipFinalShadedColor = BoolField(default_value=True)
    clip = clipFinalShadedColor

    enableDepthMaps = BoolField(default_value=True)
    edm = enableDepthMaps

    enableDefaultLight = BoolField(default_value=True)
    edl = enableDefaultLight

    currentRenderer = DataStringField()
    ren = currentRenderer

    enableStrokeRender = BoolField(default_value=True)
    esr = enableStrokeRender

    onlyRenderStrokes = BoolField(default_value=False)
    ors = onlyRenderStrokes

    strokesDepthFile = DataStringField()
    sdf = strokesDepthFile

    imageFormat = ImageFormatEnumField(default_value=32)
    outf = imageFormat

    imfPluginKey = DataStringField()
    imfkey = imfPluginKey

    gammaCorrection = FloatField(default_value=1.0)
    gama = gammaCorrection

    bitDepth = BitDepthEnumField(default_value=0)
    bitd = bitDepth

    tiffCompression = TiffCompressionEnumField(default_value=0)
    tiffc = tiffCompression

    exrCompression = ExrCompressionEnumField(default_value=0)
    exrc = exrCompression

    exrPixelType = ExrPixelTypeEnumField(default_value=0)
    expt = exrPixelType

    topRegion = LongField(default_value=256)
    top = topRegion

    leftRegion = LongField(default_value=0)
    left = leftRegion

    bottomRegion = LongField(default_value=0)
    bot = bottomRegion

    rightRegion = LongField(default_value=256)
    rght = rightRegion

    useRenderRegion = BoolField(default_value=False)
    urr = useRenderRegion

    animation = BoolField(default_value=False)
    an = animation

    animationRange = AnimationRangeEnumField(default_value=1)
    ar = animationRange

    startFrame = TimeField(default_value=2.5)
    fs = startFrame

    endFrame = TimeField(default_value=25.0)
    ef = endFrame

    byFrame = TimeField(default_value=2.5)
    bf = byFrame

    byFrameStep = FloatField(default_value=1.0)
    bfs = byFrameStep

    skipExistingFrames = BoolField(default_value=False)
    sef = skipExistingFrames

    modifyExtension = BoolField(default_value=False)
    me = modifyExtension

    startExtension = FloatField(default_value=1.0)
    se = startExtension

    byExtension = FloatField(default_value=1.0)
    be = byExtension

    extensionPadding = LongField(default_value=4, min_value=0, max_value=10)
    ep = extensionPadding

    fieldExtControl = FieldExtControlEnumField(default_value=0)
    fec = fieldExtControl

    outFormatControl = OutFormatControlEnumField(default_value=0)
    ofc = outFormatControl

    oddFieldExt = DataStringField()
    ofe = oddFieldExt

    evenFieldExt = DataStringField()
    efe = evenFieldExt

    outFormatExt = DataStringField()
    oft = outFormatExt

    useMayaFileName = BoolField(default_value=True)
    umfn = useMayaFileName

    useFrameExt = BoolField(default_value=False)
    ufe = useFrameExt

    putFrameBeforeExt = BoolField(default_value=False)
    pff = putFrameBeforeExt

    periodInExt = PeriodInExtEnumField(default_value=1)
    peie = periodInExt

    imageFilePrefix = DataStringField()
    ifp = imageFilePrefix

    renderVersion = DataStringField()
    rv = renderVersion

    bufferName = DataStringField()
    bn = bufferName

    multiCamNamingMode = MultiCamNamingModeEnumField(default_value=0)
    mcnm = multiCamNamingMode

    composite = BoolField(default_value=False)
    comp = composite

    compositeThreshold = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    cth = compositeThreshold

    shadowsObeyLightLinking = BoolField(default_value=True)
    soll = shadowsObeyLightLinking

    shadowsObeyShadowLinking = BoolField(default_value=False)
    sosl = shadowsObeyShadowLinking

    recursionDepth = LongField(default_value=2, min_value=0, max_value=10, soft_min_value=1, soft_max_value=3)
    rd = recursionDepth

    leafPrimitives = LongField(default_value=200, min_value=50, max_value=5000)
    lp = leafPrimitives

    subdivisionPower = FloatField(default_value=0.25, min_value=0.01, max_value=1.0)
    sp = subdivisionPower

    subdivisionHashSize = LongField(default_value=5, min_value=1, max_value=100)
    shs = subdivisionHashSize

    logRenderPerformance = BoolField(default_value=False)
    lpr = logRenderPerformance

    geometryVector = LongField(default_value=20, min_value=1, max_value=500, soft_min_value=10, soft_max_value=100)
    gv = geometryVector

    shadingVector = LongField(default_value=60, min_value=1, max_value=500, soft_min_value=10, soft_max_value=100)
    sv = shadingVector

    maximumMemory = LongField(default_value=48, min_value=1, max_value=2048)
    mm = maximumMemory

    numCpusToUse = LongField(default_value=0, min_value=0, soft_min_value=1, soft_max_value=8)
    npu = numCpusToUse

    interruptFrequency = LongField(default_value=1, min_value=-1)
    itf = interruptFrequency

    shadowPass = BoolField(default_value=False)
    shp = shadowPass

    iprShadowPass = BoolField(default_value=False)
    isp = iprShadowPass

    useFileCache = BoolField(default_value=True)
    uf = useFileCache

    optimizeInstances = BoolField(default_value=True)
    oi = optimizeInstances

    reuseTessellations = BoolField(default_value=True)
    rut = reuseTessellations

    matteOpacityUsesTransparency = BoolField(default_value=True)
    mot = matteOpacityUsesTransparency

    motionBlur = BoolField(default_value=False)
    mb = motionBlur

    motionBlurByFrame = FloatField(default_value=1.0)
    mbf = motionBlurByFrame

    motionBlurUseShutter = BoolField(default_value=False)
    mbus = motionBlurUseShutter

    motionBlurShutterOpen = FloatField(default_value=-0.5)
    mbso = motionBlurShutterOpen

    motionBlurShutterClose = FloatField(default_value=0.5)
    mbsc = motionBlurShutterClose

    fogGeometry = MessageField()
    fg = fogGeometry

    applyFogInPost = BoolField(default_value=False)
    afp = applyFogInPost

    postFogBlur = LongField(default_value=1, min_value=0, max_value=1000, soft_min_value=0, soft_max_value=10)
    pfb = postFogBlur

    preMel = DataStringField()
    pram = preMel

    postMel = DataStringField()
    poam = postMel

    preRenderLayerMel = DataStringField()
    prlm = preRenderLayerMel

    postRenderLayerMel = DataStringField()
    polm = postRenderLayerMel

    preRenderMel = DataStringField()
    prm = preRenderMel

    postRenderMel = DataStringField()
    pom = postRenderMel

    preFurRenderMel = DataStringField()
    pfrm = preFurRenderMel

    postFurRenderMel = DataStringField()
    pfom = postFurRenderMel

    createIprFile = BoolField(default_value=False)
    cif = createIprFile

    blurLength = FloatField(default_value=1.0, min_value=0.0, max_value=100.0, soft_min_value=0.0, soft_max_value=30.0)
    bll = blurLength

    blurSharpness = FloatField(default_value=1.0, min_value=0.0, max_value=100.0, soft_min_value=0.0, soft_max_value=15.0)
    bls = blurSharpness

    smoothValue = LongField(default_value=2, min_value=0)
    smv = smoothValue

    useBlur2DMemoryCap = BoolField(default_value=True)
    ubc = useBlur2DMemoryCap

    blur2DMemoryCap = FloatField(default_value=200.0, min_value=1.0)
    mbc = blur2DMemoryCap

    motionBlurType = MotionBlurTypeEnumField(default_value=1)
    mbt = motionBlurType

    useDisplacementBoundingBox = BoolField(default_value=True)
    udbx = useDisplacementBoundingBox

    smoothColor = BoolField(default_value=False)
    smc = smoothColor

    keepMotionVector = BoolField(default_value=False)
    kmv = keepMotionVector

    iprRenderShading = BoolField(default_value=True)
    isl = iprRenderShading

    iprRenderShadowMaps = BoolField(default_value=True)
    ism = iprRenderShadowMaps

    iprRenderMotionBlur = BoolField(default_value=True)
    imb = iprRenderMotionBlur

    rendercallback = MessageField()
    rcb = rendercallback

    renderLayerEnable = BoolField(default_value=False)
    rlen = renderLayerEnable

    forceTileSize = BoolField(default_value=False)
    frts = forceTileSize

    tileWidth = ShortField(default_value=64)
    tlwd = tileWidth

    tileHeight = ShortField(default_value=64)
    tlht = tileHeight

    jitterFinalColor = BoolField(default_value=True)
    jfc = jitterFinalColor

    raysSeeBackground = BoolField(default_value=True)
    rsb = raysSeeBackground

    oversamplePaintEffects = BoolField(default_value=False)
    ope = oversamplePaintEffects

    oversamplePfxPostFilter = BoolField(default_value=False)
    oppf = oversamplePfxPostFilter

    colorProfileEnabled = BoolField(default_value=False)
    cpe = colorProfileEnabled

    renderingColorProfile = LongField(default_value=2)
    rcp = renderingColorProfile

    inputColorProfile = LongField(default_value=3)
    icp = inputColorProfile

    outputColorProfile = LongField(default_value=2)
    ocp = outputColorProfile

    hyperShadeBinList = DataStringField()
    hbl = hyperShadeBinList

    swatchCamera = MessageField()
    sc = swatchCamera

    renderedOutput = RenderedOutputEnumField(default_value=0)
    ro = renderedOutput

    defaultTraversalSet = DataStringField()
    dts = defaultTraversalSet
