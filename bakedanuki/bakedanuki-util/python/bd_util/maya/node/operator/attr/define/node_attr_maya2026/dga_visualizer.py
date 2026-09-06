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
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.dt.string import DataStringField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ColorRamp_colorRamp_InterpEnumPlugOperator(
    EnumPlugOperator["ColorRamp_colorRamp_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ColorRamp_colorRamp_InterpEnumAttrOperator(
    EnumAttrOperator[ColorRamp_colorRamp_InterpEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class ColorRamp_colorRamp_InterpEnumField(
    EnumField[
        ColorRamp_colorRamp_InterpEnumAttrOperator,
        ColorRamp_colorRamp_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorRamp_colorRamp_InterpEnumAttrOperator
    PLUG_CLS = ColorRamp_colorRamp_InterpEnumPlugOperator


class ColorRamp_colorRamp_ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorRamp_colorRamp_ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRamp_ColorR", "crcvr"),
        ("colorRamp_ColorG", "crcvg"),
        ("colorRamp_ColorB", "crcvb"),
    )

    colorRamp_ColorR = FloatField()
    crcvr = colorRamp_ColorR

    colorRamp_ColorG = FloatField()
    crcvg = colorRamp_ColorG

    colorRamp_ColorB = FloatField()
    crcvb = colorRamp_ColorB


class ColorRamp_colorRamp_ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorRamp_colorRamp_ColorPlugOperator]
):
    __slots__ = ()

    colorRamp_ColorR = FloatField()
    crcvr = colorRamp_ColorR

    colorRamp_ColorG = FloatField()
    crcvg = colorRamp_ColorG

    colorRamp_ColorB = FloatField()
    crcvb = colorRamp_ColorB


class ColorRamp_colorRamp_ColorField(
    Float3CompoundBaseField[
        ColorRamp_colorRamp_ColorAttrOperator,
        ColorRamp_colorRamp_ColorPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ColorRamp_colorRamp_ColorAttrOperator
    PLUG_CLS = ColorRamp_colorRamp_ColorPlugOperator

    colorRamp_ColorR = FloatField()
    crcvr = colorRamp_ColorR

    colorRamp_ColorG = FloatField()
    crcvg = colorRamp_ColorG

    colorRamp_ColorB = FloatField()
    crcvb = colorRamp_ColorB


class ColorRampPlugOperator(CompoundPlugOperator["ColorRampAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorRamp_Position", "crp"),
        ("colorRamp_Color", "crcv"),
        ("colorRamp_Interp", "cri"),
    )

    colorRamp_Position = FloatField(default_value=0.0)
    crp = colorRamp_Position

    colorRamp_Color = ColorRamp_colorRamp_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    crcv = colorRamp_Color

    colorRamp_Interp = ColorRamp_colorRamp_InterpEnumField(default_value=1)
    cri = colorRamp_Interp


class ColorRampAttrOperator(CompoundAttrOperator[ColorRampPlugOperator]):
    __slots__ = ()

    colorRamp_Position = FloatField(default_value=0.0)
    crp = colorRamp_Position

    colorRamp_Color = ColorRamp_colorRamp_ColorField(
        default_value=(0.0, 0.0, 0.0)
    )
    crcv = colorRamp_Color

    colorRamp_Interp = ColorRamp_colorRamp_InterpEnumField(default_value=1)
    cri = colorRamp_Interp


class ColorRampField(
    CompoundField[ColorRampAttrOperator, ColorRampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorRampAttrOperator
    PLUG_CLS = ColorRampPlugOperator


class InputAttributesPlugOperator(
    CompoundPlugOperator["InputAttributesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputName", "iname"),
        ("inputValues", "ival"),
    )

    inputName = DataStringField()
    iname = inputName

    inputValues = DoubleField(multi=True, default_value=0.0)
    ival = inputValues


class InputAttributesAttrOperator(
    CompoundAttrOperator[InputAttributesPlugOperator]
):
    __slots__ = ()

    inputName = DataStringField()
    iname = inputName

    inputValues = DoubleField(multi=True, default_value=0.0)
    ival = inputValues


class InputAttributesField(
    CompoundField[InputAttributesAttrOperator, InputAttributesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttributesAttrOperator
    PLUG_CLS = InputAttributesPlugOperator
