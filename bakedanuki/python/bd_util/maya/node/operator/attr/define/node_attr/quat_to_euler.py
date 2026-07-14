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


class InputQuatPlugOperator(
    QuatCompoundBasePlugOperator["InputQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputQuatX", "iqx"),
        ("inputQuatY", "iqy"),
        ("inputQuatZ", "iqz"),
        ("inputQuatW", "iqw"),
    )

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatAttrOperator(
    QuatCompoundBaseAttrOperator[InputQuatPlugOperator]
):
    __slots__ = ()

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
    iqw = inputQuatW


class InputQuatField(
    QuatCompoundBaseField[InputQuatAttrOperator, InputQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputQuatAttrOperator
    PLUG_CLS = InputQuatPlugOperator

    inputQuatX = DoubleField(default_value=0.0)
    iqx = inputQuatX

    inputQuatY = DoubleField(default_value=0.0)
    iqy = inputQuatY

    inputQuatZ = DoubleField(default_value=0.0)
    iqz = inputQuatZ

    inputQuatW = DoubleField(default_value=1.0)
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

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputRotatePlugOperator]
):
    __slots__ = ()

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ


class OutputRotateField(
    DoubleAngle3CompoundBaseField[OutputRotateAttrOperator, OutputRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputRotateAttrOperator
    PLUG_CLS = OutputRotatePlugOperator

    outputRotateX = DoubleAngleField(default_value=0.0, writable=False)
    orx = outputRotateX

    outputRotateY = DoubleAngleField(default_value=0.0, writable=False)
    ory = outputRotateY

    outputRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    orz = outputRotateZ
