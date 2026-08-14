# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
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


class AxisQuatPlugOperator(
    QuatCompoundBasePlugOperator["AxisQuatAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("axisQuatX", "aqx"),
        ("axisQuatY", "aqy"),
        ("axisQuatZ", "aqz"),
        ("axisQuatW", "aqw"),
    )

    axisQuatX = DoubleField(default_value=0.0)
    aqx = axisQuatX

    axisQuatY = DoubleField(default_value=0.0)
    aqy = axisQuatY

    axisQuatZ = DoubleField(default_value=0.0)
    aqz = axisQuatZ

    axisQuatW = DoubleField(default_value=1.0)
    aqw = axisQuatW


class AxisQuatAttrOperator(QuatCompoundBaseAttrOperator[AxisQuatPlugOperator]):
    __slots__ = ()

    axisQuatX = DoubleField(default_value=0.0)
    aqx = axisQuatX

    axisQuatY = DoubleField(default_value=0.0)
    aqy = axisQuatY

    axisQuatZ = DoubleField(default_value=0.0)
    aqz = axisQuatZ

    axisQuatW = DoubleField(default_value=1.0)
    aqw = axisQuatW


class AxisQuatField(
    QuatCompoundBaseField[AxisQuatAttrOperator, AxisQuatPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisQuatAttrOperator
    PLUG_CLS = AxisQuatPlugOperator

    axisQuatX = DoubleField(default_value=0.0)
    aqx = axisQuatX

    axisQuatY = DoubleField(default_value=0.0)
    aqy = axisQuatY

    axisQuatZ = DoubleField(default_value=0.0)
    aqz = axisQuatZ

    axisQuatW = DoubleField(default_value=1.0)
    aqw = axisQuatW
