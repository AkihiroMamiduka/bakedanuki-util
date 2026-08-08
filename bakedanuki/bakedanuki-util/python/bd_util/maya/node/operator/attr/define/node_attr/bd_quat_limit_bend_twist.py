# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..custom import (
    QuatCompoundBaseAttrOperator,
    QuatCompoundBasePlugOperator,
    QuatCompoundBaseField,
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


class MinPlugOperator(DoubleAngle3CompoundBasePlugOperator["MinAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minTwist", "mntw"),
        ("minBendH", "mnbh"),
        ("minBendV", "mnbv"),
    )

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MinAttrOperator(DoubleAngle3CompoundBaseAttrOperator[MinPlugOperator]):
    __slots__ = ()

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MinField(
    DoubleAngle3CompoundBaseField[MinAttrOperator, MinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minTwist = DoubleAngleField(default_value=-180.0)
    mntw = minTwist

    minBendH = DoubleAngleField(default_value=-180.0)
    mnbh = minBendH

    minBendV = DoubleAngleField(default_value=-180.0)
    mnbv = minBendV


class MaxPlugOperator(DoubleAngle3CompoundBasePlugOperator["MaxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxTwist", "mxtw"),
        ("maxBendH", "mxbh"),
        ("maxBendV", "mxbv"),
    )

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


class MaxAttrOperator(DoubleAngle3CompoundBaseAttrOperator[MaxPlugOperator]):
    __slots__ = ()

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


class MaxField(
    DoubleAngle3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxTwist = DoubleAngleField(default_value=180.0)
    mxtw = maxTwist

    maxBendH = DoubleAngleField(default_value=180.0)
    mxbh = maxBendH

    maxBendV = DoubleAngleField(default_value=180.0)
    mxbv = maxBendV


class OutputPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputTwist", "otw"),
        ("outputBendH", "obh"),
        ("outputBendV", "obv"),
    )

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV


class OutputAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV


class OutputField(
    DoubleAngle3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputTwist = DoubleAngleField(default_value=0.0, writable=False)
    otw = outputTwist

    outputBendH = DoubleAngleField(default_value=0.0, writable=False)
    obh = outputBendH

    outputBendV = DoubleAngleField(default_value=0.0, writable=False)
    obv = outputBendV


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
