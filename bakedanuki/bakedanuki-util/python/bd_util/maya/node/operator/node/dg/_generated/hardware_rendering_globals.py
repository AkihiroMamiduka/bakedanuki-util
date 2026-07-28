# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hardware_rendering_globals import (
    BatchRenderControlsField,
    CustomUVBorderColorField,
    HwFogColorField,
    MotionBlurAtlasSizeField,
    MotionBlurFadeTintField,
    MotionBlurMultiframeChartSizeField,
    QuadDrawOverrideColorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class HoldOutDetailModeEnumPlugOperator(EnumPlugOperator["HoldOutDetailModeEnumAttrOperator"]):
    __slots__ = ()

    PER_OBJECT_HOLD_MINUS_OUT = 1
    ALL_OBJECT_HOLD_MINUS_OUT = 2


class HoldOutDetailModeEnumAttrOperator(EnumAttrOperator[HoldOutDetailModeEnumPlugOperator]):
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


class VertexAnimationCacheEnumPlugOperator(EnumPlugOperator["VertexAnimationCacheEnumAttrOperator"]):
    __slots__ = ()

    DISABLE = 0
    SYSTEM = 1
    HARDWARE = 2


class VertexAnimationCacheEnumAttrOperator(EnumAttrOperator[VertexAnimationCacheEnumPlugOperator]):
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


class TransparencyAlgorithmEnumPlugOperator(EnumPlugOperator["TransparencyAlgorithmEnumAttrOperator"]):
    __slots__ = ()

    SIMPLE = 0
    OBJECT_SORTING = 1
    WEIGHTED_AVERAGE = 2
    DEPTH_PEELING = 3
    ALPHA_CUT = 5


class TransparencyAlgorithmEnumAttrOperator(EnumAttrOperator[TransparencyAlgorithmEnumPlugOperator]):
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


class TextureMaxResModeEnumPlugOperator(EnumPlugOperator["TextureMaxResModeEnumAttrOperator"]):
    __slots__ = ()

    AUTOMATIC = 0
    CUSTOM = 1


class TextureMaxResModeEnumAttrOperator(EnumAttrOperator[TextureMaxResModeEnumPlugOperator]):
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


class SsaoSamplesEnumPlugOperator(EnumPlugOperator["SsaoSamplesEnumAttrOperator"]):
    __slots__ = ()

    _8 = 8
    _16 = 16
    _32 = 32


class SsaoSamplesEnumAttrOperator(EnumAttrOperator[SsaoSamplesEnumPlugOperator]):
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


class HwFogFalloffEnumPlugOperator(EnumPlugOperator["HwFogFalloffEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 0
    EXPONENTIAL = 1
    EXPONENTIAL_SQUARED = 2


class HwFogFalloffEnumAttrOperator(EnumAttrOperator[HwFogFalloffEnumPlugOperator]):
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


class MotionBlurTypeEnumPlugOperator(EnumPlugOperator["MotionBlurTypeEnumAttrOperator"]):
    __slots__ = ()

    TRANSFORM = 0


class MotionBlurTypeEnumAttrOperator(EnumAttrOperator[MotionBlurTypeEnumPlugOperator]):
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


class MotionBlurSampleCountEnumPlugOperator(EnumPlugOperator["MotionBlurSampleCountEnumAttrOperator"]):
    __slots__ = ()

    _4 = 4
    _8 = 8
    _16 = 16
    _32 = 32


class MotionBlurSampleCountEnumAttrOperator(EnumAttrOperator[MotionBlurSampleCountEnumPlugOperator]):
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


class MultiSampleCountEnumPlugOperator(EnumPlugOperator["MultiSampleCountEnumAttrOperator"]):
    __slots__ = ()

    _1 = 1
    _2 = 2
    _4 = 4
    _8 = 8
    _16 = 16


class MultiSampleCountEnumAttrOperator(EnumAttrOperator[MultiSampleCountEnumPlugOperator]):
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


class MultiSampleQualityEnumPlugOperator(EnumPlugOperator["MultiSampleQualityEnumAttrOperator"]):
    __slots__ = ()

    _0 = 0


class MultiSampleQualityEnumAttrOperator(EnumAttrOperator[MultiSampleQualityEnumPlugOperator]):
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


class FloatingPointRTFormatEnumPlugOperator(EnumPlugOperator["FloatingPointRTFormatEnumAttrOperator"]):
    __slots__ = ()

    R32G32B32A32_FLOAT = 1
    R32G32B32_FLOAT = 2
    R16G16B16A16_FLOAT = 3


class FloatingPointRTFormatEnumAttrOperator(EnumAttrOperator[FloatingPointRTFormatEnumPlugOperator]):
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


class GeneratedHardwareRenderingGlobals(DG):
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

    holdOutMode = BoolField(default_value=True)
    hom = holdOutMode

    holdOutDetailMode = HoldOutDetailModeEnumField(default_value=1)
    hodm = holdOutDetailMode

    xrayMode = BoolField(default_value=False)
    xry = xrayMode

    xrayJointDisplay = BoolField(default_value=False)
    jxr = xrayJointDisplay

    singleSidedLighting = BoolField(default_value=False)
    sslt = singleSidedLighting

    colorBakeResolution = LongField(default_value=64, min_value=4, max_value=8192, soft_max_value=2048)
    cbr = colorBakeResolution

    bumpBakeResolution = LongField(default_value=64, min_value=4, max_value=8192, soft_max_value=2048)
    bbr = bumpBakeResolution

    maxHardwareLights = LongField(default_value=8, min_value=1, soft_max_value=16)
    mhl = maxHardwareLights

    useMaximumHardwareLights = BoolField(default_value=True)
    uml = useMaximumHardwareLights

    consolidateWorld = BoolField(default_value=True)
    cons = consolidateWorld

    vertexAnimationCache = VertexAnimationCacheEnumField(default_value=0)
    vac = vertexAnimationCache

    hwInstancing = BoolField(default_value=False)
    hwi = hwInstancing

    compressSharedVertexData = BoolField(default_value=True)
    csvd = compressSharedVertexData

    transparencyAlgorithm = TransparencyAlgorithmEnumField(default_value=1)
    ta = transparencyAlgorithm

    transparencyQuality = FloatField(default_value=0.33000001311302185, min_value=0.0, max_value=1.0)
    tq = transparencyQuality

    transparentShadow = BoolField(default_value=False)
    ts = transparentShadow

    alphaCutPrepass = BoolField(default_value=False)
    acpp = alphaCutPrepass

    enableTextureMaxRes = BoolField(default_value=True)
    etmr = enableTextureMaxRes

    textureMaxResMode = TextureMaxResModeEnumField(default_value=0)
    tmrm = textureMaxResMode

    textureMaxResolution = LongField(default_value=2048, min_value=32, max_value=16384, soft_max_value=8192)
    tmr = textureMaxResolution

    textureAutoMaxResolution = LongField(default_value=2048, min_value=32, max_value=16384, soft_max_value=8192)
    tamr = textureAutoMaxResolution

    ssaoEnable = BoolField(default_value=False)
    aoon = ssaoEnable

    ssaoAmount = FloatField(default_value=1.0, min_value=0.0, max_value=3.0)
    aoam = ssaoAmount

    ssaoRadius = LongField(default_value=16, min_value=1, max_value=64)
    aora = ssaoRadius

    ssaoFilter = DataStringField()
    aoft = ssaoFilter

    ssaoFilterRadius = LongField(default_value=16, min_value=1, max_value=32)
    aofr = ssaoFilterRadius

    ssaoSamples = SsaoSamplesEnumField(default_value=16)
    aosm = ssaoSamples

    renderDepthOfField = BoolField(default_value=True)
    adof = renderDepthOfField

    hwFogEnable = BoolField(default_value=False)
    hfon = hwFogEnable

    hwFogFalloff = HwFogFalloffEnumField(default_value=0)
    hff = hwFogFalloff

    hwFogDensity = FloatField(default_value=0.10000000149011612, min_value=0.0, max_value=1.0)
    hfd = hwFogDensity

    hwFogStart = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1000.0)
    hfs = hwFogStart

    hwFogEnd = FloatField(default_value=100.0, soft_min_value=0.0, soft_max_value=1000.0)
    hfe = hwFogEnd

    hwFogColor = HwFogColorField(default_value=(0.5, 0.5, 0.5))
    hfc = hwFogColor
    hwFogColorR = hwFogColor.hwFogColorR
    hfcr = hwFogColorR
    hwFogColorG = hwFogColor.hwFogColorG
    hfcg = hwFogColorG
    hwFogColorB = hwFogColor.hwFogColorB
    hfcb = hwFogColorB

    hwFogAlpha = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    hfa = hwFogAlpha

    motionBlurEnable = BoolField(default_value=False)
    mbe = motionBlurEnable

    motionBlurType = MotionBlurTypeEnumField(default_value=0)
    mbt = motionBlurType

    motionBlurShutterOpenFraction = FloatField(default_value=0.20000000298023224, min_value=0.009999999776482582, max_value=2.0)
    mbsof = motionBlurShutterOpenFraction

    motionBlurSampleCount = MotionBlurSampleCountEnumField(default_value=8)
    mbsc = motionBlurSampleCount

    motionBlurCurved = BoolField(default_value=False)
    mbc = motionBlurCurved

    motionBlurFadeFilter = DataStringField()
    mbff = motionBlurFadeFilter

    motionBlurFadeAmount = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    mbfa = motionBlurFadeAmount

    motionBlurFadeTint = MotionBlurFadeTintField(default_value=(0.0, 0.0, 0.0))
    mbft = motionBlurFadeTint
    motionBlurFadeTintR = motionBlurFadeTint.motionBlurFadeTintR
    mbftr = motionBlurFadeTintR
    motionBlurFadeTintG = motionBlurFadeTint.motionBlurFadeTintG
    mbftg = motionBlurFadeTintG
    motionBlurFadeTintB = motionBlurFadeTint.motionBlurFadeTintB
    mbftb = motionBlurFadeTintB

    motionBlurFadeTintA = FloatField(default_value=1.0)
    mbfta = motionBlurFadeTintA

    motionBlurFadeEmphasis = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    mbfe = motionBlurFadeEmphasis

    motionBlurMultiframeEnable = BoolField(default_value=False)
    mbme = motionBlurMultiframeEnable

    motionBlurMultiframeChartSize = MotionBlurMultiframeChartSizeField(default_value=(256, 256), min_value=(1, 1), max_value=(4096, 4096))
    mbcs = motionBlurMultiframeChartSize
    motionBlurMultiframeChartSizeX = motionBlurMultiframeChartSize.motionBlurMultiframeChartSizeX
    mbcsx = motionBlurMultiframeChartSizeX
    motionBlurMultiframeChartSizeY = motionBlurMultiframeChartSize.motionBlurMultiframeChartSizeY
    mbcsy = motionBlurMultiframeChartSizeY

    motionBlurAtlasSize = MotionBlurAtlasSizeField(default_value=(8, 4), min_value=(1, 1), max_value=(32, 32))
    mbas = motionBlurAtlasSize
    motionBlurAtlasSizeX = motionBlurAtlasSize.motionBlurAtlasSizeX
    mbasx = motionBlurAtlasSizeX
    motionBlurAtlasSizeY = motionBlurAtlasSize.motionBlurAtlasSizeY
    mbasy = motionBlurAtlasSizeY

    bloomEnable = BoolField(default_value=False)
    blen = bloomEnable

    bloomThreshold = FloatField(default_value=0.0, min_value=0.0)
    blth = bloomThreshold

    bloomFilter = DataStringField()
    blfl = bloomFilter

    bloomFilterRadius = FloatField(default_value=0.0, min_value=0.0)
    blfr = bloomFilterRadius

    bloomFilterAux = FloatField(default_value=0.0, min_value=0.0)
    blfa = bloomFilterAux

    bloomAmount = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=3.0)
    blat = bloomAmount

    multiSampleEnable = BoolField(default_value=False)
    msaa = multiSampleEnable

    multiSampleCount = MultiSampleCountEnumField(default_value=8)
    aasc = multiSampleCount

    multiSampleQuality = MultiSampleQualityEnumField(default_value=0)
    aasq = multiSampleQuality

    lineAAEnable = BoolField(default_value=False)
    laa = lineAAEnable

    defaultLightIntensity = FloatField(default_value=3.140000104904175, soft_min_value=0.0, soft_max_value=20.0)
    dli = defaultLightIntensity

    gammaCorrectionEnable = BoolField(default_value=False)
    gamm = gammaCorrectionEnable

    gammaValue = FloatField(default_value=2.200000047683716, soft_min_value=1.0, soft_max_value=2.200000047683716)
    gmmv = gammaValue

    floatingPointRTEnable = BoolField(default_value=False)
    fprt = floatingPointRTEnable

    floatingPointRTFormat = FloatingPointRTFormatEnumField(default_value=1)
    rtfm = floatingPointRTFormat

    quadDrawAlwaysOnTop = BoolField(default_value=False)
    qdaot = quadDrawAlwaysOnTop

    quadDrawOverrideColor = QuadDrawOverrideColorField(default_value=(-1.0, -1.0, -1.0))
    qdoc = quadDrawOverrideColor
    quadDrawOverrideColorR = quadDrawOverrideColor.quadDrawOverrideColorR
    qdocr = quadDrawOverrideColorR
    quadDrawOverrideColorG = quadDrawOverrideColor.quadDrawOverrideColorG
    qdocg = quadDrawOverrideColorG
    quadDrawOverrideColorB = quadDrawOverrideColor.quadDrawOverrideColorB
    qdocb = quadDrawOverrideColorB

    quadDrawOverrideTransparency = FloatField(default_value=-1.0)
    qdot = quadDrawOverrideTransparency

    isCustomUVBorderColor = BoolField(default_value=False)
    isuvbc = isCustomUVBorderColor

    customUVBorderColor = CustomUVBorderColorField(default_value=(-1.0, -1.0, -1.0))
    uvbc = customUVBorderColor
    customUVBorderColorR = customUVBorderColor.customUVBorderColorR
    uvbcr = customUVBorderColorR
    customUVBorderColorG = customUVBorderColor.customUVBorderColorG
    uvbcg = customUVBorderColorG
    customUVBorderColorB = customUVBorderColor.customUVBorderColorB
    uvbcb = customUVBorderColorB
