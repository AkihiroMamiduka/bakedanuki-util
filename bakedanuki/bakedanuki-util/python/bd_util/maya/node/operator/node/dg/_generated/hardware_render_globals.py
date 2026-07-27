# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class FrameBufferFormatEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    RGBA = 0
    _8_MINUS_BITS_FIXED_PER_CHANNEL = 1
    RGBA_2 = 2
    _16_MINUS_BIT_FLOAT_PER_CHANNEL = 3


class FrameBufferFormatEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    RGBA = 0
    _8_MINUS_BITS_FIXED_PER_CHANNEL = 1
    RGBA_2 = 2
    _16_MINUS_BIT_FLOAT_PER_CHANNEL = 3

    NAME_MAP = {
        RGBA: "RGBA",
        _8_MINUS_BITS_FIXED_PER_CHANNEL: "8-bits fixed per channel",
        RGBA_2: "RGBA",
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


class GeneratedHardwareRenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "hardwareRenderGlobals"

    colorTextureResolution = LongField(default_value=128, min_value=2, max_value=2048)
    ctrs = colorTextureResolution

    bumpTextureResolution = LongField(default_value=256, min_value=2, max_value=2048)
    btrs = bumpTextureResolution

    frameBufferFormat = FrameBufferFormatEnumField(default_value=0)
    fbfm = frameBufferFormat

    enableHighQualityLighting = BoolField(default_value=True)
    ehql = enableHighQualityLighting

    enableAcceleratedMultiSampling = BoolField(default_value=True)
    eams = enableAcceleratedMultiSampling

    enableEdgeAntiAliasing = BoolField(default_value=False)
    eeaa = enableEdgeAntiAliasing

    enableGeometryMask = BoolField(default_value=False)
    engm = enableGeometryMask

    numberOfSamples = NumberOfSamplesEnumField(default_value=1)
    mes = numberOfSamples

    enableMotionBlur = BoolField(default_value=False)
    emb = enableMotionBlur

    motionBlurByFrame = FloatField(default_value=1.0)
    mbbf = motionBlurByFrame

    numberOfExposures = LongField(default_value=3)
    mbs = numberOfExposures

    transparencySorting = TransparencySortingEnumField(default_value=0)
    trm = transparencySorting

    transparentShadowCasting = BoolField(default_value=True)
    tshc = transparentShadowCasting

    enableNonPowerOfTwoTexture = BoolField(default_value=True)
    enpt = enableNonPowerOfTwoTexture

    culling = CullingEnumField(default_value=0)
    clmt = culling

    textureCompression = TextureCompressionEnumField(default_value=0)
    tcov = textureCompression

    lightIntensityThreshold = FloatField(default_value=0.0010000000474974513, min_value=0.0001, max_value=1.0)
    lith = lightIntensityThreshold

    smallObjectCulling = BoolField(default_value=True)
    sobc = smallObjectCulling

    cullingThreshold = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    cuth = cullingThreshold

    graphicsHardwareGeometryCachingData = BoolField(default_value=True)
    hgcd = graphicsHardwareGeometryCachingData

    graphicsHardwareGeometryCachingIndexing = BoolField(default_value=True)
    hgci = graphicsHardwareGeometryCachingIndexing

    maximumGeometryCacheSize = LongField(default_value=64, min_value=1, max_value=512)
    mgcs = maximumGeometryCacheSize

    writeAlphaAsColor = BoolField(default_value=False)
    twa = writeAlphaAsColor

    writeZDepthAsColor = BoolField(default_value=False)
    twz = writeZDepthAsColor

    hardwareCodec = LongField(default_value=1919706400)
    hwcc = hardwareCodec

    hardwareDepth = LongField(default_value=32)
    hwdp = hardwareDepth

    hardwareQual = LongField(default_value=1024)
    hwql = hardwareQual

    hardwareFrameRate = LongField(default_value=24)
    hwfr = hardwareFrameRate

    shadowsObeyLightLinking = BoolField(default_value=True)
    soll = shadowsObeyLightLinking

    shadowsObeyShadowLinking = BoolField(default_value=False)
    sosl = shadowsObeyShadowLinking

    blendSpecularWithAlpha = BoolField(default_value=False)
    bswa = blendSpecularWithAlpha

    shadingModel = ShadingModelEnumField(default_value=0)
    shml = shadingModel

    hardwareEnvironmentLookup = BoolField(default_value=False)
    hwel = hardwareEnvironmentLookup
