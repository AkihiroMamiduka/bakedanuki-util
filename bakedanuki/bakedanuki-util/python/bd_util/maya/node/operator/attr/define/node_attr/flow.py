# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class AllCoordsPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["AllCoordsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("xCoord", "xc"),
        ("yCoord", "yc"),
        ("zCoord", "zc"),
    )

    xCoord = DoubleLinearField(default_value=0.0, readable=False)
    xc = xCoord

    yCoord = DoubleLinearField(default_value=0.0, readable=False)
    yc = yCoord

    zCoord = DoubleLinearField(default_value=0.0, readable=False)
    zc = zCoord


class AllCoordsAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[AllCoordsPlugOperator]
):
    __slots__ = ()

    xCoord = DoubleLinearField(default_value=0.0, readable=False)
    xc = xCoord

    yCoord = DoubleLinearField(default_value=0.0, readable=False)
    yc = yCoord

    zCoord = DoubleLinearField(default_value=0.0, readable=False)
    zc = zCoord


class AllCoordsField(
    DoubleLinear3CompoundBaseField[
        AllCoordsAttrOperator, AllCoordsPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AllCoordsAttrOperator
    PLUG_CLS = AllCoordsPlugOperator

    xCoord = DoubleLinearField(default_value=0.0, readable=False)
    xc = xCoord

    yCoord = DoubleLinearField(default_value=0.0, readable=False)
    yc = yCoord

    zCoord = DoubleLinearField(default_value=0.0, readable=False)
    zc = zCoord


class CenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerX", "ctx"),
        ("centerY", "cty"),
        ("centerZ", "ctz"),
    )

    centerX = DoubleLinearField(default_value=0.0, readable=False)
    ctx = centerX

    centerY = DoubleLinearField(default_value=0.0, readable=False)
    cty = centerY

    centerZ = DoubleLinearField(default_value=0.0, readable=False)
    ctz = centerZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerX = DoubleLinearField(default_value=0.0, readable=False)
    ctx = centerX

    centerY = DoubleLinearField(default_value=0.0, readable=False)
    cty = centerY

    centerZ = DoubleLinearField(default_value=0.0, readable=False)
    ctz = centerZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator
