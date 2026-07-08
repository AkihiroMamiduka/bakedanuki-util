# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound._base import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputRotateX", "irx"),
        ("inputRotateY", "iry"),
        ("inputRotateZ", "irz"),
    )

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputRotatePlugOperator]
):
    __slots__ = ()

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class InputRotateField(
    DoubleAngle3CompoundBaseField[InputRotateAttrOperator, InputRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputRotateAttrOperator
    PLUG_CLS = InputRotatePlugOperator

    inputRotateX = DoubleAngleField(default_value=0.0)
    irx = inputRotateX

    inputRotateY = DoubleAngleField(default_value=0.0)
    iry = inputRotateY

    inputRotateZ = DoubleAngleField(default_value=0.0)
    irz = inputRotateZ


class OutputQuatPlugOperator(
    QuatCompoundBasePlugOperator["OutputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputQuatX", "oqx"),
        ("outputQuatY", "oqy"),
        ("outputQuatZ", "oqz"),
        ("outputQuatW", "oqw"),
    )

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[OutputQuatPlugOperator]
):
    __slots__ = ()

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW


class OutputQuatField(
    QuatCompoundBaseField[OutputQuatAttrOperator, OutputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputQuatAttrOperator
    PLUG_CLS = OutputQuatPlugOperator

    outputQuatX = DoubleField(default_value=0.0, writable=False)
    oqx = outputQuatX

    outputQuatY = DoubleField(default_value=0.0, writable=False)
    oqy = outputQuatY

    outputQuatZ = DoubleField(default_value=0.0, writable=False)
    oqz = outputQuatZ

    outputQuatW = DoubleField(default_value=0.0, writable=False)
    oqw = outputQuatW
