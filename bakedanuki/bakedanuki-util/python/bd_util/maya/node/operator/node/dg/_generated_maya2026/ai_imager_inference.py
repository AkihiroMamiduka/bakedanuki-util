# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class InferenceDeviceEnumPlugOperator(
    EnumPlugOperator["InferenceDeviceEnumAttrOperator"]
):
    __slots__ = ()

    CPU = 0
    GPU = 1


class InferenceDeviceEnumAttrOperator(
    EnumAttrOperator[InferenceDeviceEnumPlugOperator]
):
    __slots__ = ()

    CPU = 0
    GPU = 1

    NAME_MAP = {
        CPU: "CPU",
        GPU: "GPU",
    }


class InferenceDeviceEnumField(
    EnumField[InferenceDeviceEnumAttrOperator, InferenceDeviceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InferenceDeviceEnumAttrOperator
    PLUG_CLS = InferenceDeviceEnumPlugOperator


class TransformPresetEnumPlugOperator(
    EnumPlugOperator["TransformPresetEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    SRGB_255 = 1


class TransformPresetEnumAttrOperator(
    EnumAttrOperator[TransformPresetEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    SRGB_255 = 1

    NAME_MAP = {
        NONE: "none",
        SRGB_255: "sRGB_255",
    }


class TransformPresetEnumField(
    EnumField[TransformPresetEnumAttrOperator, TransformPresetEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformPresetEnumAttrOperator
    PLUG_CLS = TransformPresetEnumPlugOperator


class BlendModeEnumPlugOperator(EnumPlugOperator["BlendModeEnumAttrOperator"]):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39


class BlendModeEnumAttrOperator(EnumAttrOperator[BlendModeEnumPlugOperator]):
    __slots__ = ()

    OVERWRITE = 0
    ATOP = 1
    AVERAGE = 2
    COJOINT_OVER = 3
    COLOR_BURN = 4
    COLOR_DODGE = 5
    DIFFERENCE = 6
    DISJOINT_OVER = 7
    DIVIDE = 8
    EXCLUSION = 9
    FROM = 10
    GEOMETRIC = 11
    GLOW = 12
    HARD_LIGHT = 13
    HARD_MIX = 14
    HYPOT_DIAGONAL = 15
    IN = 16
    LINEAR_LIGHT = 17
    MASK = 18
    MATTE = 19
    MAX = 20
    MIN = 21
    MINUS = 22
    MULTIPLY = 23
    NEGATION = 24
    OUT = 25
    OVER = 26
    OVERLAY = 27
    PHOENIX = 28
    PIN_LIGHT = 29
    PLUS = 30
    REFLECT = 31
    SCREEN = 32
    SOFT_LIGHT = 33
    STENCIL = 34
    SUBTRACT = 35
    UNDER = 36
    VIVID_LIGHT = 37
    XOR = 38
    NORMAL_MAP = 39

    NAME_MAP = {
        OVERWRITE: "overwrite",
        ATOP: "atop",
        AVERAGE: "average",
        COJOINT_OVER: "cojoint_over",
        COLOR_BURN: "color_burn",
        COLOR_DODGE: "color_dodge",
        DIFFERENCE: "difference",
        DISJOINT_OVER: "disjoint_over",
        DIVIDE: "divide",
        EXCLUSION: "exclusion",
        FROM: "from",
        GEOMETRIC: "geometric",
        GLOW: "glow",
        HARD_LIGHT: "hard_light",
        HARD_MIX: "hard_mix",
        HYPOT_DIAGONAL: "hypot_diagonal",
        IN: "in",
        LINEAR_LIGHT: "linear_light",
        MASK: "mask",
        MATTE: "matte",
        MAX: "max",
        MIN: "min",
        MINUS: "minus",
        MULTIPLY: "multiply",
        NEGATION: "negation",
        OUT: "out",
        OVER: "over",
        OVERLAY: "overlay",
        PHOENIX: "phoenix",
        PIN_LIGHT: "pin_light",
        PLUS: "plus",
        REFLECT: "reflect",
        SCREEN: "screen",
        SOFT_LIGHT: "soft_light",
        STENCIL: "stencil",
        SUBTRACT: "subtract",
        UNDER: "under",
        VIVID_LIGHT: "vivid_light",
        XOR: "xor",
        NORMAL_MAP: "normal_map",
    }


class BlendModeEnumField(
    EnumField[BlendModeEnumAttrOperator, BlendModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendModeEnumAttrOperator
    PLUG_CLS = BlendModeEnumPlugOperator


class GeneratedAiImagerInference(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerInference"

    out = MessageField(writable=False)

    input = MessageField()

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    inferenceDevice = InferenceDeviceEnumField(default_value=0)
    inference_device = inferenceDevice

    modelPath = DataStringField()
    model_path = modelPath

    transformPreset = TransformPresetEnumField(default_value=1)
    transform_preset = transformPreset

    colorSpace = DataStringField()
    color_space = colorSpace

    inputMultiply = FloatField(
        default_value=1.0,
        min_value=9.999999747378752e-05,
        soft_max_value=255.0,
    )
    input_multiply = inputMultiply

    outputDivide = FloatField(
        default_value=1.0,
        min_value=9.999999747378752e-05,
        soft_max_value=255.0,
    )
    output_divide = outputDivide

    blend = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    blendMode = BlendModeEnumField(default_value=0)
    blend_mode = blendMode
