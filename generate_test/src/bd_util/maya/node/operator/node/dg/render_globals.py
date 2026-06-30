# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


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


class RenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "renderGlobals"

    macCodec = LongField()
    macc = macCodec

    macDepth = LongField()
    macd = macDepth

    macQual = LongField()
    macq = macQual

    comFrrt = LongField()
    mcfr = comFrrt

    renderAll = BoolField()
    ra = renderAll

    ignoreFilmGate = BoolField()
    ifg = ignoreFilmGate

    quality = MessageField()
    qual = quality

    resolution = MessageField()
    res = resolution

    clipFinalShadedColor = BoolField()
    clip = clipFinalShadedColor

    enableDepthMaps = BoolField()
    edm = enableDepthMaps

    enableDefaultLight = BoolField()
    edl = enableDefaultLight

    currentRenderer = DataStringField()
    ren = currentRenderer

    enableStrokeRender = BoolField()
    esr = enableStrokeRender

    onlyRenderStrokes = BoolField()
    ors = onlyRenderStrokes

    strokesDepthFile = DataStringField()
    sdf = strokesDepthFile

    imageFormat = ImageFormatEnumField()
    outf = imageFormat

    imfPluginKey = DataStringField()
    imfkey = imfPluginKey

    gammaCorrection = FloatField()
    gama = gammaCorrection

    bitDepth = BitDepthEnumField()
    bitd = bitDepth

    tiffCompression = TiffCompressionEnumField()
    tiffc = tiffCompression

    exrCompression = ExrCompressionEnumField()
    exrc = exrCompression

    exrPixelType = ExrPixelTypeEnumField()
    expt = exrPixelType

    topRegion = LongField()
    top = topRegion

    leftRegion = LongField()
    left = leftRegion

    bottomRegion = LongField()
    bot = bottomRegion

    rightRegion = LongField()
    rght = rightRegion

    useRenderRegion = BoolField()
    urr = useRenderRegion

    animation = BoolField()
    an = animation

    animationRange = AnimationRangeEnumField()
    ar = animationRange

    startFrame = TimeField()
    fs = startFrame

    endFrame = TimeField()
    ef = endFrame

    byFrame = TimeField()
    bf = byFrame

    byFrameStep = FloatField()
    bfs = byFrameStep

    skipExistingFrames = BoolField()
    sef = skipExistingFrames

    modifyExtension = BoolField()
    me = modifyExtension

    startExtension = FloatField()
    se = startExtension

    byExtension = FloatField()
    be = byExtension

    extensionPadding = LongField()
    ep = extensionPadding

    fieldExtControl = FieldExtControlEnumField()
    fec = fieldExtControl

    outFormatControl = OutFormatControlEnumField()
    ofc = outFormatControl

    oddFieldExt = DataStringField()
    ofe = oddFieldExt

    evenFieldExt = DataStringField()
    efe = evenFieldExt

    outFormatExt = DataStringField()
    oft = outFormatExt

    useMayaFileName = BoolField()
    umfn = useMayaFileName

    useFrameExt = BoolField()
    ufe = useFrameExt

    putFrameBeforeExt = BoolField()
    pff = putFrameBeforeExt

    periodInExt = PeriodInExtEnumField()
    peie = periodInExt

    imageFilePrefix = DataStringField()
    ifp = imageFilePrefix

    renderVersion = DataStringField()
    rv = renderVersion

    bufferName = DataStringField()
    bn = bufferName

    multiCamNamingMode = MultiCamNamingModeEnumField()
    mcnm = multiCamNamingMode

    composite = BoolField()
    comp = composite

    compositeThreshold = FloatField()
    cth = compositeThreshold

    shadowsObeyLightLinking = BoolField()
    soll = shadowsObeyLightLinking

    shadowsObeyShadowLinking = BoolField()
    sosl = shadowsObeyShadowLinking

    recursionDepth = LongField()
    rd = recursionDepth

    leafPrimitives = LongField()
    lp = leafPrimitives

    subdivisionPower = FloatField()
    sp = subdivisionPower

    subdivisionHashSize = LongField()
    shs = subdivisionHashSize

    logRenderPerformance = BoolField()
    lpr = logRenderPerformance

    geometryVector = LongField()
    gv = geometryVector

    shadingVector = LongField()
    sv = shadingVector

    maximumMemory = LongField()
    mm = maximumMemory

    numCpusToUse = LongField()
    npu = numCpusToUse

    interruptFrequency = LongField()
    itf = interruptFrequency

    shadowPass = BoolField()
    shp = shadowPass

    iprShadowPass = BoolField()
    isp = iprShadowPass

    useFileCache = BoolField()
    uf = useFileCache

    optimizeInstances = BoolField()
    oi = optimizeInstances

    reuseTessellations = BoolField()
    rut = reuseTessellations

    matteOpacityUsesTransparency = BoolField()
    mot = matteOpacityUsesTransparency

    motionBlur = BoolField()
    mb = motionBlur

    motionBlurByFrame = FloatField()
    mbf = motionBlurByFrame

    motionBlurUseShutter = BoolField()
    mbus = motionBlurUseShutter

    motionBlurShutterOpen = FloatField()
    mbso = motionBlurShutterOpen

    motionBlurShutterClose = FloatField()
    mbsc = motionBlurShutterClose

    fogGeometry = MessageField()
    fg = fogGeometry

    applyFogInPost = BoolField()
    afp = applyFogInPost

    postFogBlur = LongField()
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

    createIprFile = BoolField()
    cif = createIprFile

    blurLength = FloatField()
    bll = blurLength

    blurSharpness = FloatField()
    bls = blurSharpness

    smoothValue = LongField()
    smv = smoothValue

    useBlur2DMemoryCap = BoolField()
    ubc = useBlur2DMemoryCap

    blur2DMemoryCap = FloatField()
    mbc = blur2DMemoryCap

    motionBlurType = MotionBlurTypeEnumField()
    mbt = motionBlurType

    useDisplacementBoundingBox = BoolField()
    udbx = useDisplacementBoundingBox

    smoothColor = BoolField()
    smc = smoothColor

    keepMotionVector = BoolField()
    kmv = keepMotionVector

    iprRenderShading = BoolField()
    isl = iprRenderShading

    iprRenderShadowMaps = BoolField()
    ism = iprRenderShadowMaps

    iprRenderMotionBlur = BoolField()
    imb = iprRenderMotionBlur

    rendercallback = MessageField()
    rcb = rendercallback

    renderLayerEnable = BoolField()
    rlen = renderLayerEnable

    forceTileSize = BoolField()
    frts = forceTileSize

    tileWidth = ShortField()
    tlwd = tileWidth

    tileHeight = ShortField()
    tlht = tileHeight

    jitterFinalColor = BoolField()
    jfc = jitterFinalColor

    raysSeeBackground = BoolField()
    rsb = raysSeeBackground

    oversamplePaintEffects = BoolField()
    ope = oversamplePaintEffects

    oversamplePfxPostFilter = BoolField()
    oppf = oversamplePfxPostFilter

    colorProfileEnabled = BoolField()
    cpe = colorProfileEnabled

    renderingColorProfile = LongField()
    rcp = renderingColorProfile

    inputColorProfile = LongField()
    icp = inputColorProfile

    outputColorProfile = LongField()
    ocp = outputColorProfile

    hyperShadeBinList = DataStringField()
    hbl = hyperShadeBinList

    swatchCamera = MessageField()
    sc = swatchCamera

    renderedOutput = RenderedOutputEnumField()
    ro = renderedOutput

    defaultTraversalSet = DataStringField()
    dts = defaultTraversalSet
