# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..custom import Double3Field


class PointConstraintPlugOperator(
    CompoundPlugOperator["PointConstraintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointPositionXYZ", "xyz"),
        ("pointConstraintUVW", "puv"),
        ("pointWeight", "pw"),
    )

    pointPositionXYZ = Double3Field(
        default_value=(-100000.0, -100000.0, -100000.0)
    )
    xyz = pointPositionXYZ

    pointConstraintUVW = Double3Field(
        default_value=(-100000.0, -100000.0, -100000.0)
    )
    puv = pointConstraintUVW

    pointWeight = DoubleField(default_value=1.0)
    pw = pointWeight


class PointConstraintAttrOperator(
    CompoundAttrOperator[PointConstraintPlugOperator]
):
    __slots__ = ()

    pointPositionXYZ = Double3Field(
        default_value=(-100000.0, -100000.0, -100000.0)
    )
    xyz = pointPositionXYZ

    pointConstraintUVW = Double3Field(
        default_value=(-100000.0, -100000.0, -100000.0)
    )
    puv = pointConstraintUVW

    pointWeight = DoubleField(default_value=1.0)
    pw = pointWeight


class PointConstraintField(
    CompoundField[PointConstraintAttrOperator, PointConstraintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointConstraintAttrOperator
    PLUG_CLS = PointConstraintPlugOperator
