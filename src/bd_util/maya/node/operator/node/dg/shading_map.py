# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.shading_map import (
    ColorField,
    GlowColorField,
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
    ShadingMapColorField,
    TransparencyField,
    UvCoordField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class MapFunctionUEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HUE = 0
    SATURATION = 1
    VALUE = 2
    RED = 3
    GREEN = 4
    BLUE = 5
    RGB_AVERAGE = 6


class MapFunctionUEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HUE = 0
    SATURATION = 1
    VALUE = 2
    RED = 3
    GREEN = 4
    BLUE = 5
    RGB_AVERAGE = 6

    NAME_MAP = {
        HUE: "Hue",
        SATURATION: "Saturation",
        VALUE: "Value",
        RED: "Red",
        GREEN: "Green",
        BLUE: "Blue",
        RGB_AVERAGE: "RGB Average",
    }


class MapFunctionUEnumField(
    EnumField[MapFunctionUEnumAttrOperator, MapFunctionUEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapFunctionUEnumAttrOperator
    PLUG_CLS = MapFunctionUEnumPlugOperator


class MapFunctionVEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HUE = 0
    SATURATION = 1
    VALUE = 2
    RED = 3
    GREEN = 4
    BLUE = 5
    RGB_AVERAGE = 6


class MapFunctionVEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HUE = 0
    SATURATION = 1
    VALUE = 2
    RED = 3
    GREEN = 4
    BLUE = 5
    RGB_AVERAGE = 6

    NAME_MAP = {
        HUE: "Hue",
        SATURATION: "Saturation",
        VALUE: "Value",
        RED: "Red",
        GREEN: "Green",
        BLUE: "Blue",
        RGB_AVERAGE: "RGB Average",
    }


class MapFunctionVEnumField(
    EnumField[MapFunctionVEnumAttrOperator, MapFunctionVEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapFunctionVEnumAttrOperator
    PLUG_CLS = MapFunctionVEnumPlugOperator


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


class RenderPassModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    APPLY_TO_RENDER_PASSES = 1
    NO_CONTRIBUTION = 2
    WRITE_SHADER_RESULT_TO_BEAUTY_PASSES = 3


class RenderPassModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PASS_THROUGH = 0
    APPLY_TO_RENDER_PASSES = 1
    NO_CONTRIBUTION = 2
    WRITE_SHADER_RESULT_TO_BEAUTY_PASSES = 3

    NAME_MAP = {
        PASS_THROUGH: "Pass through",
        APPLY_TO_RENDER_PASSES: "Apply to Render Passes",
        NO_CONTRIBUTION: "No Contribution",
        WRITE_SHADER_RESULT_TO_BEAUTY_PASSES: "Write Shader Result to Beauty Passes",
    }


class RenderPassModeEnumField(
    EnumField[RenderPassModeEnumAttrOperator, RenderPassModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RenderPassModeEnumAttrOperator
    PLUG_CLS = RenderPassModeEnumPlugOperator


class ShadingMap(DG):
    __slots__ = ()

    NODE_TYPE = "shadingMap"

    uvCoord = UvCoordField()
    uv = uvCoord
    uCoord = uvCoord.uCoord
    uu = uCoord
    vCoord = uvCoord.vCoord
    vv = vCoord

    mapFunctionU = MapFunctionUEnumField()
    mfu = mapFunctionU

    mapFunctionV = MapFunctionVEnumField()
    mfv = mapFunctionV

    color = ColorField()
    c = color
    colorR = color.colorR
    cr = colorR
    colorG = color.colorG
    cg = colorG
    colorB = color.colorB
    cb = colorB

    shadingMapColor = ShadingMapColorField()
    sc = shadingMapColor
    shadingMapColorR = shadingMapColor.shadingMapColorR
    scr = shadingMapColorR
    shadingMapColorG = shadingMapColor.shadingMapColorG
    scg = shadingMapColorG
    shadingMapColorB = shadingMapColor.shadingMapColorB
    scb = shadingMapColorB

    glowColor = GlowColorField()
    g = glowColor
    glowColorR = glowColor.glowColorR
    gr = glowColorR
    glowColorG = glowColor.glowColorG
    gg = glowColorG
    glowColorB = glowColor.glowColorB
    gb = glowColorB

    transparency = TransparencyField()
    it = transparency
    transparencyR = transparency.transparencyR
    itr = transparencyR
    transparencyG = transparency.transparencyG
    itg = transparencyG
    transparencyB = transparency.transparencyB
    itb = transparencyB

    outColor = OutColorField()
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outGlowColor = OutGlowColorField()
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    matteOpacityMode = MatteOpacityModeEnumField()
    mom = matteOpacityMode

    matteOpacity = FloatField()
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField()
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB

    renderPassMode = RenderPassModeEnumField()
    arp = renderPassMode
