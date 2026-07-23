# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.hw_render_globals import BackgroundColorField
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class RenderPassesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _3 = 3
    _4 = 4
    _5 = 5
    _7 = 7
    _9 = 9
    _16 = 16
    _25 = 25
    _36 = 36


class RenderPassesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _3 = 3
    _4 = 4
    _5 = 5
    _7 = 7
    _9 = 9
    _16 = 16
    _25 = 25
    _36 = 36

    NAME_MAP = {
        _3: "3",
        _4: "4",
        _5: "5",
        _7: "7",
        _9: "9",
        _16: "16",
        _25: "25",
        _36: "36",
    }


class RenderPassesEnumField(
    EnumField[RenderPassesEnumAttrOperator, RenderPassesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassesEnumAttrOperator
    PLUG_CLS = RenderPassesEnumPlugOperator


class ExtensionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NAME_1 = 0
    NAME_1_EXT = 1
    NAME_EXT_1 = 2
    NAME_0001 = 3
    NAME_0001_EXT = 4
    NAME_EXT_0001 = 5


class ExtensionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NAME_1 = 0
    NAME_1_EXT = 1
    NAME_EXT_1 = 2
    NAME_0001 = 3
    NAME_0001_EXT = 4
    NAME_EXT_0001 = 5

    NAME_MAP = {
        NAME_1: "name.1",
        NAME_1_EXT: "name.1.ext",
        NAME_EXT_1: "name.ext.1",
        NAME_0001: "name.0001",
        NAME_0001_EXT: "name.0001.ext",
        NAME_EXT_0001: "name.ext.0001",
    }


class ExtensionEnumField(
    EnumField[ExtensionEnumAttrOperator, ExtensionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ExtensionEnumAttrOperator
    PLUG_CLS = ExtensionEnumPlugOperator


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
    TARGA = 19
    WINDOWS_BITMAP = 20
    IMF_PLUGIN = 50


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
    TARGA = 19
    WINDOWS_BITMAP = 20
    IMF_PLUGIN = 50

    NAME_MAP = {
        GIF: "GIF",
        SOFTIMAGE: "SoftImage",
        RLA: "RLA",
        TIFF: "Tiff",
        TIFF16: "Tiff16",
        SGI: "SGI",
        ALIAS_PIX: "Alias Pix",
        MAYA_IFF: "Maya IFF",
        JPEG: "JPEG",
        EPS: "EPS",
        MAYA16_IFF: "Maya16 IFF",
        QUANTEL: "Quantel",
        TARGA: "Targa",
        WINDOWS_BITMAP: "Windows Bitmap",
        IMF_PLUGIN: "IMF plugin",
    }


class ImageFormatEnumField(
    EnumField[ImageFormatEnumAttrOperator, ImageFormatEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImageFormatEnumAttrOperator
    PLUG_CLS = ImageFormatEnumPlugOperator


class AlphaSourceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    HARDWARE_ALPHA = 1
    LUMINANCE = 2
    RED_CHANNEL = 3
    GREEN_CHANNEL = 4
    BLUE_CHANNEL = 5
    CLAMP = 6
    INVERSE_CLAMP = 7


class AlphaSourceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    HARDWARE_ALPHA = 1
    LUMINANCE = 2
    RED_CHANNEL = 3
    GREEN_CHANNEL = 4
    BLUE_CHANNEL = 5
    CLAMP = 6
    INVERSE_CLAMP = 7

    NAME_MAP = {
        OFF: "Off",
        HARDWARE_ALPHA: "Hardware Alpha",
        LUMINANCE: "Luminance",
        RED_CHANNEL: "Red Channel",
        GREEN_CHANNEL: "Green Channel",
        BLUE_CHANNEL: "Blue Channel",
        CLAMP: "Clamp",
        INVERSE_CLAMP: "Inverse Clamp",
    }


class AlphaSourceEnumField(
    EnumField[AlphaSourceEnumAttrOperator, AlphaSourceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AlphaSourceEnumAttrOperator
    PLUG_CLS = AlphaSourceEnumPlugOperator


class DrawStyleEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINTS = 0
    WIREFRAME = 1
    FLAT_SHADED = 2
    SMOOTH_SHADED = 3


class DrawStyleEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POINTS = 0
    WIREFRAME = 1
    FLAT_SHADED = 2
    SMOOTH_SHADED = 3

    NAME_MAP = {
        POINTS: "Points",
        WIREFRAME: "Wireframe",
        FLAT_SHADED: "Flat Shaded",
        SMOOTH_SHADED: "Smooth Shaded",
    }


class DrawStyleEnumField(
    EnumField[DrawStyleEnumAttrOperator, DrawStyleEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DrawStyleEnumAttrOperator
    PLUG_CLS = DrawStyleEnumPlugOperator


class LightingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT_LIGHT = 0
    ALL_LIGHTS = 1
    SELECTED_LIGHTS = 2


class LightingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT_LIGHT = 0
    ALL_LIGHTS = 1
    SELECTED_LIGHTS = 2

    NAME_MAP = {
        DEFAULT_LIGHT: "Default Light",
        ALL_LIGHTS: "All Lights",
        SELECTED_LIGHTS: "Selected Lights",
    }


class LightingModeEnumField(
    EnumField[LightingModeEnumAttrOperator, LightingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LightingModeEnumAttrOperator
    PLUG_CLS = LightingModeEnumPlugOperator


class _GeneratedHwRenderGlobals(DG):
    __slots__ = ()

    NODE_TYPE = "hwRenderGlobals"

    renderPasses = RenderPassesEnumField(default_value=3)
    rp = renderPasses

    cameraIcons = BoolField(default_value=False)
    cai = cameraIcons

    collisionIcons = BoolField(default_value=False)
    coi = collisionIcons

    backgroundColor = BackgroundColorField(default_value=(0.0, 0.0, 0.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    bc = backgroundColor
    backgroundColorR = backgroundColor.backgroundColorR
    bcr = backgroundColorR
    backgroundColorG = backgroundColor.backgroundColorG
    bcg = backgroundColorG
    backgroundColorB = backgroundColor.backgroundColorB
    bcb = backgroundColorB

    emitterIcons = BoolField(default_value=False)
    ei = emitterIcons

    extension = ExtensionEnumField(default_value=3)
    ex = extension

    edgeSmoothing = FloatField(default_value=1.0)
    es = edgeSmoothing

    endFrame = LongField(default_value=10)
    ef = endFrame

    byFrame = LongField(default_value=1)
    bf = byFrame

    fieldIcons = BoolField(default_value=False)
    fii = fieldIcons

    startFrame = LongField(default_value=1)
    sf = startFrame

    grid = BoolField(default_value=False)
    gr = grid

    lightIcons = BoolField(default_value=False)
    li = lightIcons

    lineSmoothing = BoolField(default_value=False)
    ls = lineSmoothing

    motionBlur = FloatField(default_value=0.0)
    mb = motionBlur

    transformIcons = BoolField(default_value=False)
    ti = transformIcons

    texturing = BoolField(default_value=True)
    txt = texturing

    multiPassRendering = BoolField(default_value=False)
    mpr = multiPassRendering

    writeZDepth = BoolField(default_value=False)
    wzd = writeZDepth

    filename = DataStringField()
    fn = filename

    imageFormat = ImageFormatEnumField(default_value=7)
    if_ = imageFormat

    imfPluginKey = DataStringField()
    imfkey = imfPluginKey

    imfPluginKeyExt = DataStringField()
    imfext = imfPluginKeyExt

    resolution = DataStringField()
    res = resolution

    alphaSource = AlphaSourceEnumField(default_value=0)
    as_ = alphaSource

    drawStyle = DrawStyleEnumField(default_value=3)
    ds = drawStyle

    lightingMode = LightingModeEnumField(default_value=0)
    lm = lightingMode

    fullImageResolution = BoolField(default_value=False)
    fir = fullImageResolution

    antiAliasPolygons = BoolField(default_value=False)
    aap = antiAliasPolygons

    geometryMask = BoolField(default_value=False)
    gh = geometryMask

    displayShadows = BoolField(default_value=False)
    sd = displayShadows
