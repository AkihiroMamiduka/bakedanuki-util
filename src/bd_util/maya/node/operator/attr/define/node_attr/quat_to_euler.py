# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double4_compound._base import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class InputQuatPlugOperator(
    Double4CompoundBasePlugOperator["InputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqx"),
        ("inputQuatY", "iqy"),
        ("inputQuatZ", "iqz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class InputQuatAttrOperator(
    Double4CompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class InputQuatField(
    Double4CompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField()
    iqx = inputQuatX

    inputQuatY = DoubleField()
    iqy = inputQuatY

    inputQuatZ = DoubleField()
    iqz = inputQuatZ

    inputQuatW = DoubleField()
    iqw = inputQuatW


class OutputRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputRotateX", "orx"),
        ("outputRotateY", "ory"),
        ("outputRotateZ", "orz"),
    )

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[OutputRotateAttrOperator, OutputRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField()
    orx = outputRotateX

    outputRotateY = DoubleAngleField()
    ory = outputRotateY

    outputRotateZ = DoubleAngleField()
    orz = outputRotateZ
