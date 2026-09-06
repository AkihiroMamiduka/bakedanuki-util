# coding: utf-8

from ......value import Double4
from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double4CompoundBaseAttrOperator,
    Double4CompoundBasePlugOperator,
    Double4CompoundBaseField,
)


class OutputPlugOperator(
    Double4CompoundBasePlugOperator["OutputAttrOperator", Double4]
):
    __slots__ = ()

    VALUE_TYPE = Double4
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
        ("outputW", "ow"),
    )

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ

    outputW = DoubleField(default_value=0.0, writable=False)
    ow = outputW


class OutputAttrOperator(Double4CompoundBaseAttrOperator[OutputPlugOperator]):
    __slots__ = ()

    outputX = DoubleField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleField(default_value=0.0, writable=False)
    oz = outputZ

    outputW = DoubleField(default_value=0.0, writable=False)
    ow = outputW


class OutputField(
    Double4CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
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

    outputW = DoubleField(default_value=0.0, writable=False)
    ow = outputW
