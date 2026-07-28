# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class Input2DPlugOperator(
    Float2CompoundBasePlugOperator["Input2DAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input2Dx", "i2x"),
        ("input2Dy", "i2y"),
    )

    input2Dx = FloatField(default_value=0.0, readable=False)
    i2x = input2Dx

    input2Dy = FloatField(default_value=0.0, readable=False)
    i2y = input2Dy


class Input2DAttrOperator(Float2CompoundBaseAttrOperator[Input2DPlugOperator]):
    __slots__ = ()

    input2Dx = FloatField(default_value=0.0, readable=False)
    i2x = input2Dx

    input2Dy = FloatField(default_value=0.0, readable=False)
    i2y = input2Dy


class Input2DField(
    Float2CompoundBaseField[Input2DAttrOperator, Input2DPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input2DAttrOperator
    PLUG_CLS = Input2DPlugOperator


class Input3DPlugOperator(
    Float3CompoundBasePlugOperator["Input3DAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("input3Dx", "i3x"),
        ("input3Dy", "i3y"),
        ("input3Dz", "i3z"),
    )

    input3Dx = FloatField(default_value=0.0, readable=False)
    i3x = input3Dx

    input3Dy = FloatField(default_value=0.0, readable=False)
    i3y = input3Dy

    input3Dz = FloatField(default_value=0.0, readable=False)
    i3z = input3Dz


class Input3DAttrOperator(Float3CompoundBaseAttrOperator[Input3DPlugOperator]):
    __slots__ = ()

    input3Dx = FloatField(default_value=0.0, readable=False)
    i3x = input3Dx

    input3Dy = FloatField(default_value=0.0, readable=False)
    i3y = input3Dy

    input3Dz = FloatField(default_value=0.0, readable=False)
    i3z = input3Dz


class Input3DField(
    Float3CompoundBaseField[Input3DAttrOperator, Input3DPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Input3DAttrOperator
    PLUG_CLS = Input3DPlugOperator


class Output2DPlugOperator(
    Float2CompoundBasePlugOperator["Output2DAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("output2Dx", "o2x"),
        ("output2Dy", "o2y"),
    )

    output2Dx = FloatField(default_value=0.0, writable=False)
    o2x = output2Dx

    output2Dy = FloatField(default_value=0.0, writable=False)
    o2y = output2Dy


class Output2DAttrOperator(
    Float2CompoundBaseAttrOperator[Output2DPlugOperator]
):
    __slots__ = ()

    output2Dx = FloatField(default_value=0.0, writable=False)
    o2x = output2Dx

    output2Dy = FloatField(default_value=0.0, writable=False)
    o2y = output2Dy


class Output2DField(
    Float2CompoundBaseField[Output2DAttrOperator, Output2DPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Output2DAttrOperator
    PLUG_CLS = Output2DPlugOperator

    output2Dx = FloatField(default_value=0.0, writable=False)
    o2x = output2Dx

    output2Dy = FloatField(default_value=0.0, writable=False)
    o2y = output2Dy


class Output3DPlugOperator(
    Float3CompoundBasePlugOperator["Output3DAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("output3Dx", "o3x"),
        ("output3Dy", "o3y"),
        ("output3Dz", "o3z"),
    )

    output3Dx = FloatField(default_value=0.0, writable=False)
    o3x = output3Dx

    output3Dy = FloatField(default_value=0.0, writable=False)
    o3y = output3Dy

    output3Dz = FloatField(default_value=0.0, writable=False)
    o3z = output3Dz


class Output3DAttrOperator(
    Float3CompoundBaseAttrOperator[Output3DPlugOperator]
):
    __slots__ = ()

    output3Dx = FloatField(default_value=0.0, writable=False)
    o3x = output3Dx

    output3Dy = FloatField(default_value=0.0, writable=False)
    o3y = output3Dy

    output3Dz = FloatField(default_value=0.0, writable=False)
    o3z = output3Dz


class Output3DField(
    Float3CompoundBaseField[Output3DAttrOperator, Output3DPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Output3DAttrOperator
    PLUG_CLS = Output3DPlugOperator

    output3Dx = FloatField(default_value=0.0, writable=False)
    o3x = output3Dx

    output3Dy = FloatField(default_value=0.0, writable=False)
    o3y = output3Dy

    output3Dz = FloatField(default_value=0.0, writable=False)
    o3z = output3Dz
