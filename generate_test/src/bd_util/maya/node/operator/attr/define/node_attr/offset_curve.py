# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
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

    normalX = DoubleLinearField()
    nrx = normalX

    normalY = DoubleLinearField()
    nry = normalY

    normalZ = DoubleLinearField()
    nrz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField()
    nrx = normalX

    normalY = DoubleLinearField()
    nry = normalY

    normalZ = DoubleLinearField()
    nrz = normalZ


class NormalField(
    DoubleLinear3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = DoubleLinearField()
    nrx = normalX

    normalY = DoubleLinearField()
    nry = normalY

    normalZ = DoubleLinearField()
    nrz = normalZ
