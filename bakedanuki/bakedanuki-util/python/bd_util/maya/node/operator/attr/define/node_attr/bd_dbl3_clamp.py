# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class InputPlugOperator(Double3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(Double3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class InputField(
    Double3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleField(default_value=0.0)
    ix = inputX

    inputY = DoubleField(default_value=0.0)
    iy = inputY

    inputZ = DoubleField(default_value=0.0)
    iz = inputZ


class MinPlugOperator(Double3CompoundBasePlugOperator["MinAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minX", "mnx"),
        ("minY", "mny"),
        ("minZ", "mnz"),
    )

    minX = DoubleField(default_value=0.0)
    mnx = minX

    minY = DoubleField(default_value=0.0)
    mny = minY

    minZ = DoubleField(default_value=0.0)
    mnz = minZ


class MinAttrOperator(Double3CompoundBaseAttrOperator[MinPlugOperator]):
    __slots__ = ()

    minX = DoubleField(default_value=0.0)
    mnx = minX

    minY = DoubleField(default_value=0.0)
    mny = minY

    minZ = DoubleField(default_value=0.0)
    mnz = minZ


class MinField(Double3CompoundBaseField[MinAttrOperator, MinPlugOperator]):
    __slots__ = ()

    ATTR_CLS = MinAttrOperator
    PLUG_CLS = MinPlugOperator

    minX = DoubleField(default_value=0.0)
    mnx = minX

    minY = DoubleField(default_value=0.0)
    mny = minY

    minZ = DoubleField(default_value=0.0)
    mnz = minZ


class MaxPlugOperator(Double3CompoundBasePlugOperator["MaxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxX", "mxx"),
        ("maxY", "mxy"),
        ("maxZ", "mxz"),
    )

    maxX = DoubleField(default_value=1.0)
    mxx = maxX

    maxY = DoubleField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleField(default_value=1.0)
    mxz = maxZ


class MaxAttrOperator(Double3CompoundBaseAttrOperator[MaxPlugOperator]):
    __slots__ = ()

    maxX = DoubleField(default_value=1.0)
    mxx = maxX

    maxY = DoubleField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleField(default_value=1.0)
    mxz = maxZ


class MaxField(Double3CompoundBaseField[MaxAttrOperator, MaxPlugOperator]):
    __slots__ = ()

    ATTR_CLS = MaxAttrOperator
    PLUG_CLS = MaxPlugOperator

    maxX = DoubleField(default_value=1.0)
    mxx = maxX

    maxY = DoubleField(default_value=1.0)
    mxy = maxY

    maxZ = DoubleField(default_value=1.0)
    mxz = maxZ


class OutputPlugOperator(
    Double3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(Double3CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    Double3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ
