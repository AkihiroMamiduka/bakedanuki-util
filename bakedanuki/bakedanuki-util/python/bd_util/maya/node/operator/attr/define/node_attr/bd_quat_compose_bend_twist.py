# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
)


class InputPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputTwist", "itw"),
        ("inputBendH", "ibh"),
        ("inputBendV", "ibv"),
    )

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


class InputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


class InputField(
    DoubleAngle3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputTwist = DoubleAngleField(default_value=0.0)
    itw = inputTwist

    inputBendH = DoubleAngleField(default_value=0.0)
    ibh = inputBendH

    inputBendV = DoubleAngleField(default_value=0.0)
    ibv = inputBendV


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

    outputQuatW = DoubleField(default_value=1.0, writable=False)
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

    outputQuatW = DoubleField(default_value=1.0, writable=False)
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

    outputQuatW = DoubleField(default_value=1.0, writable=False)
    oqw = outputQuatW
