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


class ModeEnumPlugOperator(EnumPlugOperator["ModeEnumAttrOperator"]):
    __slots__ = ()

    FILMIC = 0
    REINHARD = 1
    LUT = 2


class ModeEnumAttrOperator(EnumAttrOperator[ModeEnumPlugOperator]):
    __slots__ = ()

    FILMIC = 0
    REINHARD = 1
    LUT = 2

    NAME_MAP = {
        FILMIC: "filmic",
        REINHARD: "reinhard",
        LUT: "lut",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class GeneratedAiImagerTonemap(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerTonemap"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    mode = ModeEnumField(default_value=0)

    filmicToeStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    filmic_toe_strength = filmicToeStrength

    filmicToeLength = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    filmic_toe_length = filmicToeLength

    filmicShoulderStrength = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    filmic_shoulder_strength = filmicShoulderStrength

    filmicShoulderLength = FloatField(default_value=0.5, min_value=0.0, soft_max_value=3.0)
    filmic_shoulder_length = filmicShoulderLength

    filmicShoulderAngle = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    filmic_shoulder_angle = filmicShoulderAngle

    reinhardHighlights = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    reinhard_highlights = reinhardHighlights

    reinhardShadows = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    reinhard_shadows = reinhardShadows

    lutFilename = DataStringField()
    lut_filename = lutFilename

    lutWorkingColorSpace = DataStringField()
    lut_working_color_space = lutWorkingColorSpace

    preserveSaturation = BoolField(default_value=False)
    preserve_saturation = preserveSaturation

    gamma = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)

    mix = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
