# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class TrueValuePlugOperator(
    Double3CompoundBasePlugOperator["TrueValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("trueValueX", "tvx"),
        ("trueValueY", "tvy"),
        ("trueValueZ", "tvz"),
    )

    trueValueX = DoubleField(default_value=0.0)
    tvx = trueValueX

    trueValueY = DoubleField(default_value=0.0)
    tvy = trueValueY

    trueValueZ = DoubleField(default_value=0.0)
    tvz = trueValueZ


class TrueValueAttrOperator(
    Double3CompoundBaseAttrOperator[TrueValuePlugOperator]
):
    __slots__ = ()

    trueValueX = DoubleField(default_value=0.0)
    tvx = trueValueX

    trueValueY = DoubleField(default_value=0.0)
    tvy = trueValueY

    trueValueZ = DoubleField(default_value=0.0)
    tvz = trueValueZ


class TrueValueField(
    Double3CompoundBaseField[TrueValueAttrOperator, TrueValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TrueValueAttrOperator
    PLUG_CLS = TrueValuePlugOperator

    trueValueX = DoubleField(default_value=0.0)
    tvx = trueValueX

    trueValueY = DoubleField(default_value=0.0)
    tvy = trueValueY

    trueValueZ = DoubleField(default_value=0.0)
    tvz = trueValueZ


class FalseValuePlugOperator(
    Double3CompoundBasePlugOperator["FalseValueAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("falseValueX", "fvx"),
        ("falseValueY", "fvy"),
        ("falseValueZ", "fvz"),
    )

    falseValueX = DoubleField(default_value=0.0)
    fvx = falseValueX

    falseValueY = DoubleField(default_value=0.0)
    fvy = falseValueY

    falseValueZ = DoubleField(default_value=0.0)
    fvz = falseValueZ


class FalseValueAttrOperator(
    Double3CompoundBaseAttrOperator[FalseValuePlugOperator]
):
    __slots__ = ()

    falseValueX = DoubleField(default_value=0.0)
    fvx = falseValueX

    falseValueY = DoubleField(default_value=0.0)
    fvy = falseValueY

    falseValueZ = DoubleField(default_value=0.0)
    fvz = falseValueZ


class FalseValueField(
    Double3CompoundBaseField[FalseValueAttrOperator, FalseValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FalseValueAttrOperator
    PLUG_CLS = FalseValuePlugOperator

    falseValueX = DoubleField(default_value=0.0)
    fvx = falseValueX

    falseValueY = DoubleField(default_value=0.0)
    fvy = falseValueY

    falseValueZ = DoubleField(default_value=0.0)
    fvz = falseValueZ


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
