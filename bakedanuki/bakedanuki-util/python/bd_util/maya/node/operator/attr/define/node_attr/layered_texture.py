# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class BlendModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    OVER = 1
    IN = 2
    OUT = 3
    ADD = 4
    SUBTRACT = 5
    MULTIPLY = 6
    DIFFERENCE = 7
    LIGHTEN = 8
    DARKEN = 9
    SATURATE = 10
    DESATURATE = 11
    ILLUMINATE = 12
    CPV_MODULATE = 13


class BlendModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    OVER = 1
    IN = 2
    OUT = 3
    ADD = 4
    SUBTRACT = 5
    MULTIPLY = 6
    DIFFERENCE = 7
    LIGHTEN = 8
    DARKEN = 9
    SATURATE = 10
    DESATURATE = 11
    ILLUMINATE = 12
    CPV_MODULATE = 13

    NAME_MAP = {
        NONE: "None",
        OVER: "Over",
        IN: "In",
        OUT: "Out",
        ADD: "Add",
        SUBTRACT: "Subtract",
        MULTIPLY: "Multiply",
        DIFFERENCE: "Difference",
        LIGHTEN: "Lighten",
        DARKEN: "Darken",
        SATURATE: "Saturate",
        DESATURATE: "Desaturate",
        ILLUMINATE: "Illuminate",
        CPV_MODULATE: "CPV Modulate",
    }


class BlendModeEnumField(
    EnumField[BlendModeEnumAttrOperator, BlendModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BlendModeEnumAttrOperator
    PLUG_CLS = BlendModeEnumPlugOperator


class InputsPlugOperator(
    CompoundPlugOperator["InputsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color", "c"),
        ("alpha", "a"),
        ("blendMode", "bm"),
        ("isVisible", "iv"),
    )

    color = Float3Field(default_value=(0.0, 0.0, 0.0))
    c = color

    alpha = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    a = alpha

    blendMode = BlendModeEnumField(default_value=1)
    bm = blendMode

    isVisible = BoolField(default_value=True)
    iv = isVisible


class InputsAttrOperator(
    CompoundAttrOperator[InputsPlugOperator]
):
    __slots__ = ()

    color = Float3Field(default_value=(0.0, 0.0, 0.0))
    c = color

    alpha = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    a = alpha

    blendMode = BlendModeEnumField(default_value=1)
    bm = blendMode

    isVisible = BoolField(default_value=True)
    iv = isVisible


class InputsField(
    CompoundField[InputsAttrOperator, InputsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputsAttrOperator
    PLUG_CLS = InputsPlugOperator


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class HardwareColorPlugOperator(
    Float3CompoundBasePlugOperator["HardwareColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hardwareColorR", "hcr"),
        ("hardwareColorG", "hcg"),
        ("hardwareColorB", "hcb"),
    )

    hardwareColorR = FloatField(default_value=0.5)
    hcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hcb = hardwareColorB


class HardwareColorAttrOperator(
    Float3CompoundBaseAttrOperator[HardwareColorPlugOperator]
):
    __slots__ = ()

    hardwareColorR = FloatField(default_value=0.5)
    hcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hcb = hardwareColorB


class HardwareColorField(
    Float3CompoundBaseField[HardwareColorAttrOperator, HardwareColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HardwareColorAttrOperator
    PLUG_CLS = HardwareColorPlugOperator

    hardwareColorR = FloatField(default_value=0.5)
    hcr = hardwareColorR

    hardwareColorG = FloatField(default_value=0.5)
    hcg = hardwareColorG

    hardwareColorB = FloatField(default_value=0.5)
    hcb = hardwareColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB
