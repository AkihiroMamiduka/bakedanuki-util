# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class NormalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "nrx"),
        ("normalY", "nry"),
        ("normalZ", "nrz"),
    )

    normalX = DoubleLinearField(default_value=0.0)
    nrx = normalX

    normalY = DoubleLinearField(default_value=1.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0)
    nrz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField(default_value=0.0)
    nrx = normalX

    normalY = DoubleLinearField(default_value=1.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0)
    nrz = normalZ


class NormalField(
    DoubleLinear3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = DoubleLinearField(default_value=0.0)
    nrx = normalX

    normalY = DoubleLinearField(default_value=1.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0)
    nrz = normalZ
