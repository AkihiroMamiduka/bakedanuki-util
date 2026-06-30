# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.hardware_rendering_globals import (
    BatchRenderControlsField,
    CustomUVBorderColorField,
    HwFogColorField,
    MotionBlurAtlasSizeField,
    MotionBlurFadeTintField,
    MotionBlurMultiframeChartSizeField,
    QuadDrawOverrideColorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class HoldOutDetailModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_OBJECT_HOLD_MINUS_OUT = 1
    ALL_OBJECT_HOLD_MINUS_OUT = 2


class HoldOutDetailModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_OBJECT_HOLD_MINUS_OUT = 1
    ALL_OBJECT_HOLD_MINUS_OUT = 2

    NAME_MAP = {
        PER_OBJECT_HOLD_MINUS_OUT: "Per Object Hold-Out",
        ALL_OBJECT_HOLD_MINUS_OUT: "All Object Hold-Out",
    }


class HoldOutDetailModeEnumField(
    EnumField[HoldOutDetailModeEnumAttrOperator, HoldOutDetailModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HoldOutDetailModeEnumAttrOperator
    PLUG_CLS = HoldOutDetailModeEnumPlugOperator


class VertexAnimationCacheEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLE = 0
    SYSTEM = 1
    HARDWARE = 2


class VertexAnimationCacheEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLE = 0
    SYSTEM = 1
    HARDWARE = 2

    NAME_MAP = {
        DISABLE: "Disable",
        SYSTEM: "System",
        HARDWARE: "Hardware",
    }


class VertexAnimationCacheEnumField(
    EnumField[VertexAnimationCacheEnumAttrOperator, VertexAnimationCacheEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexAnimationCacheEnumAttrOperator
    PLUG_CLS = VertexAnimationCacheEnumPlugOperator


class TransparencyAlgorithmEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SIMPLE = 0
    OBJECT_SORTING = 1
    WEIGHTED_AVERAGE = 2
    DEPTH_PEELING = 3
    ALPHA_CUT = 5


class TransparencyAlgorithmEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SIMPLE = 0
    OBJECT_SORTING = 1
    WEIGHTED_AVERAGE = 2
    DEPTH_PEELING = 3
    ALPHA_CUT = 5

    NAME_MAP = {
        SIMPLE: "Simple",
        OBJECT_SORTING: "Object Sorting",
        WEIGHTED_AVERAGE: "Weighted Average",
        DEPTH_PEELING: "Depth Peeling",
        ALPHA_CUT: "Alpha Cut",
    }


class TransparencyAlgorithmEnumField(
    EnumField[TransparencyAlgorithmEnumAttrOperator, TransparencyAlgorithmEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencyAlgorithmEnumAttrOperator
    PLUG_CLS = TransparencyAlgorithmEnumPlugOperator


class TextureMaxResModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1


class TextureMaxResModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        CUSTOM: "Custom",
    }


class TextureMaxResModeEnumField(
    EnumField[TextureMaxResModeEnumAttrOperator, TextureMaxResModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureMaxResModeEnumAttrOperator
    PLUG_CLS = TextureMaxResModeEnumPlugOperator


class SsaoSamplesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _8 = 8
    _16 = 16
    _32 = 32


class SsaoSamplesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _8 = 8
    _16 = 16
    _32 = 32

    NAME_MAP = {
        _8: "8",
        _16: "16",
        _32: "32",
    }


class SsaoSamplesEnumField(
    EnumField[SsaoSamplesEnumAttrOperator, SsaoSamplesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SsaoSamplesEnumAttrOperator
    PLUG_CLS = SsaoSamplesEnumPlugOperator


class HwFogFalloffEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    EXPONENTIAL = 1
    EXPONENTIAL_SQUARED = 2


class HwFogFalloffEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    EXPONENTIAL = 1
    EXPONENTIAL_SQUARED = 2

    NAME_MAP = {
        LINEAR: "Linear",
        EXPONENTIAL: "Exponential",
        EXPONENTIAL_SQUARED: "Exponential squared",
    }


class HwFogFalloffEnumField(
    EnumField[HwFogFalloffEnumAttrOperator, HwFogFalloffEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HwFogFalloffEnumAttrOperator
    PLUG_CLS = HwFogFalloffEnumPlugOperator


class MotionBlurTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRANSFORM = 0


class MotionBlurTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRANSFORM = 0

    NAME_MAP = {
        TRANSFORM: "Transform",
    }


class MotionBlurTypeEnumField(
    EnumField[MotionBlurTypeEnumAttrOperator, MotionBlurTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurTypeEnumAttrOperator
    PLUG_CLS = MotionBlurTypeEnumPlugOperator


class MotionBlurSampleCountEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _4 = 4
    _8 = 8
    _16 = 16
    _32 = 32


class MotionBlurSampleCountEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _4 = 4
    _8 = 8
    _16 = 16
    _32 = 32

    NAME_MAP = {
        _4: "4",
        _8: "8",
        _16: "16",
        _32: "32",
    }


class MotionBlurSampleCountEnumField(
    EnumField[MotionBlurSampleCountEnumAttrOperator, MotionBlurSampleCountEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MotionBlurSampleCountEnumAttrOperator
    PLUG_CLS = MotionBlurSampleCountEnumPlugOperator


class MultiSampleCountEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _1 = 1
    _2 = 2
    _4 = 4
    _8 = 8
    _16 = 16


class MultiSampleCountEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _1 = 1
    _2 = 2
    _4 = 4
    _8 = 8
    _16 = 16

    NAME_MAP = {
        _1: "1",
        _2: "2",
        _4: "4",
        _8: "8",
        _16: "16",
    }


class MultiSampleCountEnumField(
    EnumField[MultiSampleCountEnumAttrOperator, MultiSampleCountEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiSampleCountEnumAttrOperator
    PLUG_CLS = MultiSampleCountEnumPlugOperator


class MultiSampleQualityEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _0 = 0


class MultiSampleQualityEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _0 = 0

    NAME_MAP = {
        _0: "0",
    }


class MultiSampleQualityEnumField(
    EnumField[MultiSampleQualityEnumAttrOperator, MultiSampleQualityEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiSampleQualityEnumAttrOperator
    PLUG_CLS = MultiSampleQualityEnumPlugOperator


class FloatingPointRTFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    R32G32B32A32_FLOAT = 1
    R32G32B32_FLOAT = 2
    R16G16B16A16_FLOAT = 3


class FloatingPointRTFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    R32G32B32A32_FLOAT = 1
    R32G32B32_FLOAT = 2
    R16G16B16A16_FLOAT = 3

    NAME_MAP = {
        R32G32B32A32_FLOAT: "R32G32B32A32_FLOAT",
        R32G32B32_FLOAT: "R32G32B32_FLOAT",
        R16G16B16A16_FLOAT: "R16G16B16A16_FLOAT",
    }


class FloatingPointRTFormatEnumField(
    EnumField[FloatingPointRTFormatEnumAttrOperator, FloatingPointRTFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FloatingPointRTFormatEnumAttrOperator
    PLUG_CLS = FloatingPointRTFormatEnumPlugOperator


class HardwareRenderingGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "hardwareRenderingGlobals"

    batchRenderControls = BatchRenderControlsField()
    brc = batchRenderControls
    renderMode = batchRenderControls.renderMode
    rm = renderMode
    lightingMode = batchRenderControls.lightingMode
    lm = lightingMode
    objectTypeFilterNameArray = batchRenderControls.objectTypeFilterNameArray
    otfna = objectTypeFilterNameArray
    objectTypeFilterValueArray = batchRenderControls.objectTypeFilterValueArray
    otfva = objectTypeFilterValueArray
    pluginObjectTypeFilterNameArray = batchRenderControls.pluginObjectTypeFilterNameArray
    potfna = pluginObjectTypeFilterNameArray
    pluginObjectTypeFilterValueArray = batchRenderControls.pluginObjectTypeFilterValueArray
    potfva = pluginObjectTypeFilterValueArray

    renderOverrideName = DataStringField()
    on = renderOverrideName

    currentRendererName = DataStringField()
    cur = currentRendererName

    holdOutMode = BoolField()
    hom = holdOutMode

    holdOutDetailMode = HoldOutDetailModeEnumField()
    hodm = holdOutDetailMode

    xrayMode = BoolField()
    xry = xrayMode

    xrayJointDisplay = BoolField()
    jxr = xrayJointDisplay

    singleSidedLighting = BoolField()
    sslt = singleSidedLighting

    colorBakeResolution = LongField()
    cbr = colorBakeResolution

    bumpBakeResolution = LongField()
    bbr = bumpBakeResolution

    maxHardwareLights = LongField()
    mhl = maxHardwareLights

    useMaximumHardwareLights = BoolField()
    uml = useMaximumHardwareLights

    consolidateWorld = BoolField()
    cons = consolidateWorld

    vertexAnimationCache = VertexAnimationCacheEnumField()
    vac = vertexAnimationCache

    hwInstancing = BoolField()
    hwi = hwInstancing

    compressSharedVertexData = BoolField()
    csvd = compressSharedVertexData

    transparencyAlgorithm = TransparencyAlgorithmEnumField()
    ta = transparencyAlgorithm

    transparencyQuality = FloatField()
    tq = transparencyQuality

    transparentShadow = BoolField()
    ts = transparentShadow

    alphaCutPrepass = BoolField()
    acpp = alphaCutPrepass

    enableTextureMaxRes = BoolField()
    etmr = enableTextureMaxRes

    textureMaxResMode = TextureMaxResModeEnumField()
    tmrm = textureMaxResMode

    textureMaxResolution = LongField()
    tmr = textureMaxResolution

    textureAutoMaxResolution = LongField()
    tamr = textureAutoMaxResolution

    ssaoEnable = BoolField()
    aoon = ssaoEnable

    ssaoAmount = FloatField()
    aoam = ssaoAmount

    ssaoRadius = LongField()
    aora = ssaoRadius

    ssaoFilter = DataStringField()
    aoft = ssaoFilter

    ssaoFilterRadius = LongField()
    aofr = ssaoFilterRadius

    ssaoSamples = SsaoSamplesEnumField()
    aosm = ssaoSamples

    renderDepthOfField = BoolField()
    adof = renderDepthOfField

    hwFogEnable = BoolField()
    hfon = hwFogEnable

    hwFogFalloff = HwFogFalloffEnumField()
    hff = hwFogFalloff

    hwFogDensity = FloatField()
    hfd = hwFogDensity

    hwFogStart = FloatField()
    hfs = hwFogStart

    hwFogEnd = FloatField()
    hfe = hwFogEnd

    hwFogColor = HwFogColorField()
    hfc = hwFogColor
    hwFogColorR = hwFogColor.hwFogColorR
    hfcr = hwFogColorR
    hwFogColorG = hwFogColor.hwFogColorG
    hfcg = hwFogColorG
    hwFogColorB = hwFogColor.hwFogColorB
    hfcb = hwFogColorB

    hwFogAlpha = FloatField()
    hfa = hwFogAlpha

    motionBlurEnable = BoolField()
    mbe = motionBlurEnable

    motionBlurType = MotionBlurTypeEnumField()
    mbt = motionBlurType

    motionBlurShutterOpenFraction = FloatField()
    mbsof = motionBlurShutterOpenFraction

    motionBlurSampleCount = MotionBlurSampleCountEnumField()
    mbsc = motionBlurSampleCount

    motionBlurCurved = BoolField()
    mbc = motionBlurCurved

    motionBlurFadeFilter = DataStringField()
    mbff = motionBlurFadeFilter

    motionBlurFadeAmount = FloatField()
    mbfa = motionBlurFadeAmount

    motionBlurFadeTint = MotionBlurFadeTintField()
    mbft = motionBlurFadeTint
    motionBlurFadeTintR = motionBlurFadeTint.motionBlurFadeTintR
    mbftr = motionBlurFadeTintR
    motionBlurFadeTintG = motionBlurFadeTint.motionBlurFadeTintG
    mbftg = motionBlurFadeTintG
    motionBlurFadeTintB = motionBlurFadeTint.motionBlurFadeTintB
    mbftb = motionBlurFadeTintB

    motionBlurFadeTintA = FloatField()
    mbfta = motionBlurFadeTintA

    motionBlurFadeEmphasis = FloatField()
    mbfe = motionBlurFadeEmphasis

    motionBlurMultiframeEnable = BoolField()
    mbme = motionBlurMultiframeEnable

    motionBlurMultiframeChartSize = MotionBlurMultiframeChartSizeField()
    mbcs = motionBlurMultiframeChartSize
    motionBlurMultiframeChartSizeX = motionBlurMultiframeChartSize.motionBlurMultiframeChartSizeX
    mbcsx = motionBlurMultiframeChartSizeX
    motionBlurMultiframeChartSizeY = motionBlurMultiframeChartSize.motionBlurMultiframeChartSizeY
    mbcsy = motionBlurMultiframeChartSizeY

    motionBlurAtlasSize = MotionBlurAtlasSizeField()
    mbas = motionBlurAtlasSize
    motionBlurAtlasSizeX = motionBlurAtlasSize.motionBlurAtlasSizeX
    mbasx = motionBlurAtlasSizeX
    motionBlurAtlasSizeY = motionBlurAtlasSize.motionBlurAtlasSizeY
    mbasy = motionBlurAtlasSizeY

    bloomEnable = BoolField()
    blen = bloomEnable

    bloomThreshold = FloatField()
    blth = bloomThreshold

    bloomFilter = DataStringField()
    blfl = bloomFilter

    bloomFilterRadius = FloatField()
    blfr = bloomFilterRadius

    bloomFilterAux = FloatField()
    blfa = bloomFilterAux

    bloomAmount = FloatField()
    blat = bloomAmount

    multiSampleEnable = BoolField()
    msaa = multiSampleEnable

    multiSampleCount = MultiSampleCountEnumField()
    aasc = multiSampleCount

    multiSampleQuality = MultiSampleQualityEnumField()
    aasq = multiSampleQuality

    lineAAEnable = BoolField()
    laa = lineAAEnable

    defaultLightIntensity = FloatField()
    dli = defaultLightIntensity

    gammaCorrectionEnable = BoolField()
    gamm = gammaCorrectionEnable

    gammaValue = FloatField()
    gmmv = gammaValue

    floatingPointRTEnable = BoolField()
    fprt = floatingPointRTEnable

    floatingPointRTFormat = FloatingPointRTFormatEnumField()
    rtfm = floatingPointRTFormat

    quadDrawAlwaysOnTop = BoolField()
    qdaot = quadDrawAlwaysOnTop

    quadDrawOverrideColor = QuadDrawOverrideColorField()
    qdoc = quadDrawOverrideColor
    quadDrawOverrideColorR = quadDrawOverrideColor.quadDrawOverrideColorR
    qdocr = quadDrawOverrideColorR
    quadDrawOverrideColorG = quadDrawOverrideColor.quadDrawOverrideColorG
    qdocg = quadDrawOverrideColorG
    quadDrawOverrideColorB = quadDrawOverrideColor.quadDrawOverrideColorB
    qdocb = quadDrawOverrideColorB

    quadDrawOverrideTransparency = FloatField()
    qdot = quadDrawOverrideTransparency

    isCustomUVBorderColor = BoolField()
    isuvbc = isCustomUVBorderColor

    customUVBorderColor = CustomUVBorderColorField()
    uvbc = customUVBorderColor
    customUVBorderColorR = customUVBorderColor.customUVBorderColorR
    uvbcr = customUVBorderColorR
    customUVBorderColorG = customUVBorderColor.customUVBorderColorG
    uvbcg = customUVBorderColorG
    customUVBorderColorB = customUVBorderColor.customUVBorderColorB
    uvbcb = customUVBorderColorB
