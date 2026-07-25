# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Color1PlugOperator(
    Float3CompoundBasePlugOperator["Color1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color1R", "c1r"),
        ("color1G", "c1g"),
        ("color1B", "c1b"),
    )

    color1R = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1b = color1B


class Color1AttrOperator(
    Float3CompoundBaseAttrOperator[Color1PlugOperator]
):
    __slots__ = ()

    color1R = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1b = color1B


class Color1Field(
    Float3CompoundBaseField[Color1AttrOperator, Color1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color1AttrOperator
    PLUG_CLS = Color1PlugOperator

    color1R = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c1r = color1R

    color1G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1g = color1G

    color1B = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c1b = color1B


class Color2PlugOperator(
    Float3CompoundBasePlugOperator["Color2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("color2R", "c2r"),
        ("color2G", "c2g"),
        ("color2B", "c2b"),
    )

    color2R = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c2b = color2B


class Color2AttrOperator(
    Float3CompoundBaseAttrOperator[Color2PlugOperator]
):
    __slots__ = ()

    color2R = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c2b = color2B


class Color2Field(
    Float3CompoundBaseField[Color2AttrOperator, Color2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Color2AttrOperator
    PLUG_CLS = Color2PlugOperator

    color2R = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2r = color2R

    color2G = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    c2g = color2G

    color2B = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    c2b = color2B


class OutputPlugOperator(
    Float3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputR", "opr"),
        ("outputG", "opg"),
        ("outputB", "opb"),
    )

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB


class OutputAttrOperator(
    Float3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputR = FloatField(default_value=0.0, writable=False)
    opr = outputR

    outputG = FloatField(default_value=0.0, writable=False)
    opg = outputG

    outputB = FloatField(default_value=0.0, writable=False)
    opb = outputB
