# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Input1PlugOperator(Float3CompoundBasePlugOperator["Input1AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input1X", "i1x"),
        ("input1Y", "i1y"),
        ("input1Z", "i1z"),
    )

    input1X = FloatField(default_value=0.0)
    i1x = input1X

    input1Y = FloatField(default_value=0.0)
    i1y = input1Y

    input1Z = FloatField(default_value=0.0)
    i1z = input1Z


class Input1AttrOperator(Float3CompoundBaseAttrOperator[Input1PlugOperator]):
    __slots__ = ()

    input1X = FloatField(default_value=0.0)
    i1x = input1X

    input1Y = FloatField(default_value=0.0)
    i1y = input1Y

    input1Z = FloatField(default_value=0.0)
    i1z = input1Z


class Input1Field(
    Float3CompoundBaseField[Input1AttrOperator, Input1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input1AttrOperator
    PLUG_CLS = Input1PlugOperator

    input1X = FloatField(default_value=0.0)
    i1x = input1X

    input1Y = FloatField(default_value=0.0)
    i1y = input1Y

    input1Z = FloatField(default_value=0.0)
    i1z = input1Z


class Input2PlugOperator(Float3CompoundBasePlugOperator["Input2AttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2X", "i2x"),
        ("input2Y", "i2y"),
        ("input2Z", "i2z"),
    )

    input2X = FloatField(default_value=1.0)
    i2x = input2X

    input2Y = FloatField(default_value=1.0)
    i2y = input2Y

    input2Z = FloatField(default_value=1.0)
    i2z = input2Z


class Input2AttrOperator(Float3CompoundBaseAttrOperator[Input2PlugOperator]):
    __slots__ = ()

    input2X = FloatField(default_value=1.0)
    i2x = input2X

    input2Y = FloatField(default_value=1.0)
    i2y = input2Y

    input2Z = FloatField(default_value=1.0)
    i2z = input2Z


class Input2Field(
    Float3CompoundBaseField[Input2AttrOperator, Input2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2AttrOperator
    PLUG_CLS = Input2PlugOperator

    input2X = FloatField(default_value=1.0)
    i2x = input2X

    input2Y = FloatField(default_value=1.0)
    i2y = input2Y

    input2Z = FloatField(default_value=1.0)
    i2z = input2Z


class OutputPlugOperator(Float3CompoundBasePlugOperator["OutputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Float3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Float3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = FloatField(default_value=0.0, writable=False)
    ox = outputX

    outputY = FloatField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = FloatField(default_value=0.0, writable=False)
    oz = outputZ
