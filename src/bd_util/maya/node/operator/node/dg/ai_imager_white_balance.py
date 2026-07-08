# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_imager_white_balance import CustomField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ILLUMINANT = 0
    TEMPERATURE = 1
    CUSTOM = 2


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ILLUMINANT = 0
    TEMPERATURE = 1
    CUSTOM = 2

    NAME_MAP = {
        ILLUMINANT: "illuminant",
        TEMPERATURE: "temperature",
        CUSTOM: "custom",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class IlluminantEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DAYLIGHT = 0
    SUN = 1
    SHADE = 2
    OVERCAST = 3
    INCANDESCENT = 4
    FLUORESCENT = 5
    CIE_A = 6
    CIE_50 = 7
    CIE_55 = 8
    CIE_65 = 9
    CIE_75 = 10
    CIE_F1 = 11
    CIE_F2 = 12
    CIE_F3 = 13
    CIE_F4 = 14
    CIE_F5 = 15
    CIE_F6 = 16
    CIE_F7 = 17
    CIE_F8 = 18
    CIE_F9 = 19
    CIE_F10 = 20
    CIE_F11 = 21
    CIE_F12 = 22
    HALOGEN_WARM = 23
    HALOGEN_BASIC = 24
    HALOGEN_COOL = 25
    CERAMIC_HALIDE_WARM = 26
    CERAMIC_HALIDE_COOL = 27
    QUARTZ_HALIDE_WARM = 28
    QUARTZ_HALIDE = 29
    QUARTZ_HALIDE_COOL = 30
    MERCURY = 31
    PHOSPHOR_MERCURY = 32
    XENON = 33
    HIGH_PRESS_SODIUM = 34
    LOW_PRESS_SODIUM = 35


class IlluminantEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DAYLIGHT = 0
    SUN = 1
    SHADE = 2
    OVERCAST = 3
    INCANDESCENT = 4
    FLUORESCENT = 5
    CIE_A = 6
    CIE_50 = 7
    CIE_55 = 8
    CIE_65 = 9
    CIE_75 = 10
    CIE_F1 = 11
    CIE_F2 = 12
    CIE_F3 = 13
    CIE_F4 = 14
    CIE_F5 = 15
    CIE_F6 = 16
    CIE_F7 = 17
    CIE_F8 = 18
    CIE_F9 = 19
    CIE_F10 = 20
    CIE_F11 = 21
    CIE_F12 = 22
    HALOGEN_WARM = 23
    HALOGEN_BASIC = 24
    HALOGEN_COOL = 25
    CERAMIC_HALIDE_WARM = 26
    CERAMIC_HALIDE_COOL = 27
    QUARTZ_HALIDE_WARM = 28
    QUARTZ_HALIDE = 29
    QUARTZ_HALIDE_COOL = 30
    MERCURY = 31
    PHOSPHOR_MERCURY = 32
    XENON = 33
    HIGH_PRESS_SODIUM = 34
    LOW_PRESS_SODIUM = 35

    NAME_MAP = {
        DAYLIGHT: "daylight",
        SUN: "sun",
        SHADE: "shade",
        OVERCAST: "overcast",
        INCANDESCENT: "incandescent",
        FLUORESCENT: "fluorescent",
        CIE_A: "cie_a",
        CIE_50: "cie_50",
        CIE_55: "cie_55",
        CIE_65: "cie_65",
        CIE_75: "cie_75",
        CIE_F1: "cie_f1",
        CIE_F2: "cie_f2",
        CIE_F3: "cie_f3",
        CIE_F4: "cie_f4",
        CIE_F5: "cie_f5",
        CIE_F6: "cie_f6",
        CIE_F7: "cie_f7",
        CIE_F8: "cie_f8",
        CIE_F9: "cie_f9",
        CIE_F10: "cie_f10",
        CIE_F11: "cie_f11",
        CIE_F12: "cie_f12",
        HALOGEN_WARM: "halogen_warm",
        HALOGEN_BASIC: "halogen_basic",
        HALOGEN_COOL: "halogen_cool",
        CERAMIC_HALIDE_WARM: "ceramic_halide_warm",
        CERAMIC_HALIDE_COOL: "ceramic_halide_cool",
        QUARTZ_HALIDE_WARM: "quartz_halide_warm",
        QUARTZ_HALIDE: "quartz_halide",
        QUARTZ_HALIDE_COOL: "quartz_halide_cool",
        MERCURY: "mercury",
        PHOSPHOR_MERCURY: "phosphor_mercury",
        XENON: "xenon",
        HIGH_PRESS_SODIUM: "high_press_sodium",
        LOW_PRESS_SODIUM: "low_press_sodium",
    }


class IlluminantEnumField(
    EnumField[IlluminantEnumAttrOperator, IlluminantEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IlluminantEnumAttrOperator
    PLUG_CLS = IlluminantEnumPlugOperator


class AiImagerWhiteBalance(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerWhiteBalance"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    mode = ModeEnumField(default_value=0)

    temperature = FloatField(default_value=6500.0, min_value=0.0, soft_max_value=15000.0)

    illuminant = IlluminantEnumField(default_value=0)

    custom = CustomField(default_value=(1.0, 1.0, 1.0))
    customR = custom.customR
    customr = customR
    customG = custom.customG
    customg = customG
    customB = custom.customB
    customb = customB
