# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class FirstPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["FirstAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("firstPointX", "fpx"),
        ("firstPointY", "fpy"),
        ("firstPointZ", "fpz"),
    )

    firstPointX = DoubleLinearField(default_value=1.0)
    fpx = firstPointX

    firstPointY = DoubleLinearField(default_value=0.0)
    fpy = firstPointY

    firstPointZ = DoubleLinearField(default_value=0.0)
    fpz = firstPointZ


class FirstAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[FirstPlugOperator]
):
    __slots__ = ()

    firstPointX = DoubleLinearField(default_value=1.0)
    fpx = firstPointX

    firstPointY = DoubleLinearField(default_value=0.0)
    fpy = firstPointY

    firstPointZ = DoubleLinearField(default_value=0.0)
    fpz = firstPointZ


class FirstField(
    DoubleLinear3CompoundBaseField[FirstAttrOperator, FirstPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FirstAttrOperator
    PLUG_CLS = FirstPlugOperator

    firstPointX = DoubleLinearField(default_value=1.0)
    fpx = firstPointX

    firstPointY = DoubleLinearField(default_value=0.0)
    fpy = firstPointY

    firstPointZ = DoubleLinearField(default_value=0.0)
    fpz = firstPointZ


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

    normalY = DoubleLinearField(default_value=0.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=1.0)
    nrz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField(default_value=0.0)
    nrx = normalX

    normalY = DoubleLinearField(default_value=0.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=1.0)
    nrz = normalZ


class NormalField(
    DoubleLinear3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = DoubleLinearField(default_value=0.0)
    nrx = normalX

    normalY = DoubleLinearField(default_value=0.0)
    nry = normalY

    normalZ = DoubleLinearField(default_value=1.0)
    nrz = normalZ


class CenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerX", "cx"),
        ("centerY", "cy"),
        ("centerZ", "cz"),
    )

    centerX = DoubleLinearField(default_value=0.0)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0)
    cz = centerZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerX = DoubleLinearField(default_value=0.0)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0)
    cz = centerZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    centerX = DoubleLinearField(default_value=0.0)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0)
    cz = centerZ
