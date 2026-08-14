# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class InputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputX", "ix"),
        ("inputY", "iy"),
        ("inputZ", "iz"),
    )

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class InputField(
    DoubleLinear3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputX = DoubleLinearField(default_value=0.0)
    ix = inputX

    inputY = DoubleLinearField(default_value=0.0)
    iy = inputY

    inputZ = DoubleLinearField(default_value=0.0)
    iz = inputZ


class FactorPlugOperator(
    Double3CompoundBasePlugOperator["FactorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("factorX", "fx"),
        ("factorY", "fy"),
        ("factorZ", "fz"),
    )

    factorX = DoubleField(default_value=1.0)
    fx = factorX

    factorY = DoubleField(default_value=1.0)
    fy = factorY

    factorZ = DoubleField(default_value=1.0)
    fz = factorZ


class FactorAttrOperator(Double3CompoundBaseAttrOperator[FactorPlugOperator]):
    __slots__ = ()

    factorX = DoubleField(default_value=1.0)
    fx = factorX

    factorY = DoubleField(default_value=1.0)
    fy = factorY

    factorZ = DoubleField(default_value=1.0)
    fz = factorZ


class FactorField(
    Double3CompoundBaseField[FactorAttrOperator, FactorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FactorAttrOperator
    PLUG_CLS = FactorPlugOperator

    factorX = DoubleField(default_value=1.0)
    fx = factorX

    factorY = DoubleField(default_value=1.0)
    fy = factorY

    factorZ = DoubleField(default_value=1.0)
    fz = factorZ


class OutputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField(default_value=0.0, writable=False)
    ox = outputX

    outputY = DoubleLinearField(default_value=0.0, writable=False)
    oy = outputY

    outputZ = DoubleLinearField(default_value=0.0, writable=False)
    oz = outputZ
