# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class InPointPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["InPointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inPointX", "ipx"),
        ("inPointY", "ipy"),
        ("inPointZ", "ipz"),
    )

    inPointX = DoubleLinearField()
    ipx = inPointX

    inPointY = DoubleLinearField()
    ipy = inPointY

    inPointZ = DoubleLinearField()
    ipz = inPointZ


class InPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InPointPlugOperator]
):
    __slots__ = ()

    inPointX = DoubleLinearField()
    ipx = inPointX

    inPointY = DoubleLinearField()
    ipy = inPointY

    inPointZ = DoubleLinearField()
    ipz = inPointZ


class InPointField(
    DoubleLinear3CompoundBaseField[InPointAttrOperator, InPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InPointAttrOperator
    PLUG_CLS = InPointPlugOperator

    inPointX = DoubleLinearField()
    ipx = inPointX

    inPointY = DoubleLinearField()
    ipy = inPointY

    inPointZ = DoubleLinearField()
    ipz = inPointZ


class OutputPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["OutputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outputX", "ox"),
        ("outputY", "oy"),
        ("outputZ", "oz"),
    )

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[OutputPlugOperator]
):
    __slots__ = ()

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ


class OutputField(
    DoubleLinear3CompoundBaseField[OutputAttrOperator, OutputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutputAttrOperator
    PLUG_CLS = OutputPlugOperator

    outputX = DoubleLinearField()
    ox = outputX

    outputY = DoubleLinearField()
    oy = outputY

    outputZ = DoubleLinearField()
    oz = outputZ
