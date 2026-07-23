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

    inPointX = DoubleLinearField(default_value=0.0, readable=False)
    ipx = inPointX

    inPointY = DoubleLinearField(default_value=0.0, readable=False)
    ipy = inPointY

    inPointZ = DoubleLinearField(default_value=0.0, readable=False)
    ipz = inPointZ


class InPointAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[InPointPlugOperator]
):
    __slots__ = ()

    inPointX = DoubleLinearField(default_value=0.0, readable=False)
    ipx = inPointX

    inPointY = DoubleLinearField(default_value=0.0, readable=False)
    ipy = inPointY

    inPointZ = DoubleLinearField(default_value=0.0, readable=False)
    ipz = inPointZ


class InPointField(
    DoubleLinear3CompoundBaseField[InPointAttrOperator, InPointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InPointAttrOperator
    PLUG_CLS = InPointPlugOperator

    inPointX = DoubleLinearField(default_value=0.0, readable=False)
    ipx = inPointX

    inPointY = DoubleLinearField(default_value=0.0, readable=False)
    ipy = inPointY

    inPointZ = DoubleLinearField(default_value=0.0, readable=False)
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
