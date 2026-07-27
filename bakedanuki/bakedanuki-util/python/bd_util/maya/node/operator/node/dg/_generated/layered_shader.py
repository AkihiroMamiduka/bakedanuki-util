# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.layered_shader import (
    HardwareColorField,
    HardwareShaderField,
    InputsField,
    OutColorField,
    OutGlowColorField,
    OutMatteOpacityField,
    OutTransparencyField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class CompositingFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LAYER_SHADERS = 0
    LAYER_TEXTURE = 1


class CompositingFlagEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LAYER_SHADERS = 0
    LAYER_TEXTURE = 1

    NAME_MAP = {
        LAYER_SHADERS: "Layer Shaders",
        LAYER_TEXTURE: "Layer Texture",
    }


class CompositingFlagEnumField(
    EnumField[CompositingFlagEnumAttrOperator, CompositingFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompositingFlagEnumAttrOperator
    PLUG_CLS = CompositingFlagEnumPlugOperator


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


class GeneratedLayeredShader(DG):
    __slots__ = ()

    NODE_TYPE = "layeredShader"

    compositingFlag = CompositingFlagEnumField(default_value=0)
    cf = compositingFlag

    inputs = InputsField(multi=True)
    cs = inputs

    colorR = FloatField()
    cr = colorR

    colorG = FloatField()
    cg = colorG

    colorB = FloatField()
    cb = colorB

    transparencyR = FloatField()
    tr = transparencyR

    transparencyG = FloatField()
    tg = transparencyG

    transparencyB = FloatField()
    tb = transparencyB

    glowColorR = FloatField()
    gr = glowColorR

    glowColorG = FloatField()
    gg = glowColorG

    glowColorB = FloatField()
    gb = glowColorB

    renderPassMode = RenderPassModeEnumField(default_value=1)
    rpm = renderPassMode

    hardwareColor = HardwareColorField(default_value=(0.5, 0.5, 0.5))
    hc = hardwareColor
    hardwareColorR = hardwareColor.hardwareColorR
    hcr = hardwareColorR
    hardwareColorG = hardwareColor.hardwareColorG
    hcg = hardwareColorG
    hardwareColorB = hardwareColor.hardwareColorB
    hcb = hardwareColorB

    hardwareShader = HardwareShaderField(default_value=(0.0, 0.0, 0.0))
    hws = hardwareShader
    hardwareShaderR = hardwareShader.hardwareShaderR
    hwr = hardwareShaderR
    hardwareShaderG = hardwareShader.hardwareShaderG
    hwg = hardwareShaderG
    hardwareShaderB = hardwareShader.hardwareShaderB
    hwb = hardwareShaderB

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor
    outColorR = outColor.outColorR
    ocr = outColorR
    outColorG = outColor.outColorG
    ocg = outColorG
    outColorB = outColor.outColorB
    ocb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    outGlowColor = OutGlowColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    ogc = outGlowColor
    outGlowColorR = outGlowColor.outGlowColorR
    ogr = outGlowColorR
    outGlowColorG = outGlowColor.outGlowColorG
    ogg = outGlowColorG
    outGlowColorB = outGlowColor.outGlowColorB
    ogb = outGlowColorB

    matteOpacityMode = MatteOpacityModeEnumField(default_value=2)
    mom = matteOpacityMode

    matteOpacity = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    mog = matteOpacity

    outMatteOpacity = OutMatteOpacityField(default_value=(0.0, 0.0, 0.0), writable=False)
    omo = outMatteOpacity
    outMatteOpacityR = outMatteOpacity.outMatteOpacityR
    omor = outMatteOpacityR
    outMatteOpacityG = outMatteOpacity.outMatteOpacityG
    omog = outMatteOpacityG
    outMatteOpacityB = outMatteOpacity.outMatteOpacityB
    omob = outMatteOpacityB
