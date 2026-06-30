# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class FrameBufferFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RGBA = 0
    _8_MINUS_BITS_FIXED_PER_CHANNEL = 1
    RGBA = 2
    _16_MINUS_BIT_FLOAT_PER_CHANNEL = 3


class FrameBufferFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RGBA = 0
    _8_MINUS_BITS_FIXED_PER_CHANNEL = 1
    RGBA = 2
    _16_MINUS_BIT_FLOAT_PER_CHANNEL = 3

    NAME_MAP = {
        RGBA: "RGBA",
        _8_MINUS_BITS_FIXED_PER_CHANNEL: "8-bits fixed per channel",
        RGBA: "RGBA",
        _16_MINUS_BIT_FLOAT_PER_CHANNEL: "16-bit float per channel",
    }


class FrameBufferFormatEnumField(
    EnumField[FrameBufferFormatEnumAttrOperator, FrameBufferFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrameBufferFormatEnumAttrOperator
    PLUG_CLS = FrameBufferFormatEnumPlugOperator


class NumberOfSamplesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _1_SAMPLE = 1
    _3_SAMPLES = 3
    _4_SAMPLES = 4
    _5_SAMPLES = 5
    _7_SAMPLES = 7
    _9_SAMPLES = 9
    _16_SAMPLES = 16
    _25_SAMPLES = 25
    _36_SAMPLES = 36


class NumberOfSamplesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _1_SAMPLE = 1
    _3_SAMPLES = 3
    _4_SAMPLES = 4
    _5_SAMPLES = 5
    _7_SAMPLES = 7
    _9_SAMPLES = 9
    _16_SAMPLES = 16
    _25_SAMPLES = 25
    _36_SAMPLES = 36

    NAME_MAP = {
        _1_SAMPLE: "1 Sample",
        _3_SAMPLES: "3 Samples",
        _4_SAMPLES: "4 Samples",
        _5_SAMPLES: "5 Samples",
        _7_SAMPLES: "7 Samples",
        _9_SAMPLES: "9 Samples",
        _16_SAMPLES: "16 Samples",
        _25_SAMPLES: "25 Samples",
        _36_SAMPLES: "36 Samples",
    }


class NumberOfSamplesEnumField(
    EnumField[NumberOfSamplesEnumAttrOperator, NumberOfSamplesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NumberOfSamplesEnumAttrOperator
    PLUG_CLS = NumberOfSamplesEnumPlugOperator


class TransparencySortingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_OBJECT = 0
    PER_POLYGON = 1


class TransparencySortingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_OBJECT = 0
    PER_POLYGON = 1

    NAME_MAP = {
        PER_OBJECT: "Per Object",
        PER_POLYGON: "Per Polygon",
    }


class TransparencySortingEnumField(
    EnumField[TransparencySortingEnumAttrOperator, TransparencySortingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransparencySortingEnumAttrOperator
    PLUG_CLS = TransparencySortingEnumPlugOperator


class CullingEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PER_OBJECT = 0
    ALL_DOUBLE_SIDED = 1
    ALL_SINGLE_SIDED = 2


class CullingEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PER_OBJECT = 0
    ALL_DOUBLE_SIDED = 1
    ALL_SINGLE_SIDED = 2

    NAME_MAP = {
        PER_OBJECT: "Per Object",
        ALL_DOUBLE_SIDED: "All Double Sided",
        ALL_SINGLE_SIDED: "All Single Sided",
    }


class CullingEnumField(
    EnumField[CullingEnumAttrOperator, CullingEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CullingEnumAttrOperator
    PLUG_CLS = CullingEnumPlugOperator


class TextureCompressionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DISABLED = 0
    ENABLED = 1


class TextureCompressionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DISABLED = 0
    ENABLED = 1

    NAME_MAP = {
        DISABLED: "Disabled",
        ENABLED: "Enabled",
    }


class TextureCompressionEnumField(
    EnumField[TextureCompressionEnumAttrOperator, TextureCompressionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureCompressionEnumAttrOperator
    PLUG_CLS = TextureCompressionEnumPlugOperator


class ShadingModelEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MAYA_SOFTWARE_RENDER_EMULATION = 0
    MAYA_INTERACTIVE_SHADER = 1


class ShadingModelEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MAYA_SOFTWARE_RENDER_EMULATION = 0
    MAYA_INTERACTIVE_SHADER = 1

    NAME_MAP = {
        MAYA_SOFTWARE_RENDER_EMULATION: "Maya software render emulation",
        MAYA_INTERACTIVE_SHADER: "Maya interactive shader",
    }


class ShadingModelEnumField(
    EnumField[ShadingModelEnumAttrOperator, ShadingModelEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadingModelEnumAttrOperator
    PLUG_CLS = ShadingModelEnumPlugOperator


class HardwareRenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "hardwareRenderGlobals"

    colorTextureResolution = LongField()
    ctrs = colorTextureResolution

    bumpTextureResolution = LongField()
    btrs = bumpTextureResolution

    frameBufferFormat = FrameBufferFormatEnumField()
    fbfm = frameBufferFormat

    enableHighQualityLighting = BoolField()
    ehql = enableHighQualityLighting

    enableAcceleratedMultiSampling = BoolField()
    eams = enableAcceleratedMultiSampling

    enableEdgeAntiAliasing = BoolField()
    eeaa = enableEdgeAntiAliasing

    enableGeometryMask = BoolField()
    engm = enableGeometryMask

    numberOfSamples = NumberOfSamplesEnumField()
    mes = numberOfSamples

    enableMotionBlur = BoolField()
    emb = enableMotionBlur

    motionBlurByFrame = FloatField()
    mbbf = motionBlurByFrame

    numberOfExposures = LongField()
    mbs = numberOfExposures

    transparencySorting = TransparencySortingEnumField()
    trm = transparencySorting

    transparentShadowCasting = BoolField()
    tshc = transparentShadowCasting

    enableNonPowerOfTwoTexture = BoolField()
    enpt = enableNonPowerOfTwoTexture

    culling = CullingEnumField()
    clmt = culling

    textureCompression = TextureCompressionEnumField()
    tcov = textureCompression

    lightIntensityThreshold = FloatField()
    lith = lightIntensityThreshold

    smallObjectCulling = BoolField()
    sobc = smallObjectCulling

    cullingThreshold = FloatField()
    cuth = cullingThreshold

    graphicsHardwareGeometryCachingData = BoolField()
    hgcd = graphicsHardwareGeometryCachingData

    graphicsHardwareGeometryCachingIndexing = BoolField()
    hgci = graphicsHardwareGeometryCachingIndexing

    maximumGeometryCacheSize = LongField()
    mgcs = maximumGeometryCacheSize

    writeAlphaAsColor = BoolField()
    twa = writeAlphaAsColor

    writeZDepthAsColor = BoolField()
    twz = writeZDepthAsColor

    hardwareCodec = LongField()
    hwcc = hardwareCodec

    hardwareDepth = LongField()
    hwdp = hardwareDepth

    hardwareQual = LongField()
    hwql = hardwareQual

    hardwareFrameRate = LongField()
    hwfr = hardwareFrameRate

    shadowsObeyLightLinking = BoolField()
    soll = shadowsObeyLightLinking

    shadowsObeyShadowLinking = BoolField()
    sosl = shadowsObeyShadowLinking

    blendSpecularWithAlpha = BoolField()
    bswa = blendSpecularWithAlpha

    shadingModel = ShadingModelEnumField()
    shml = shadingModel

    hardwareEnvironmentLookup = BoolField()
    hwel = hardwareEnvironmentLookup
