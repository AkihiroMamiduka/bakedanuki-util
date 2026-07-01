# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class PointConstraintPlugOperator(
    CompoundPlugOperator["PointConstraintAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pointPositionXYZ", "xyz"),
        ("pointConstraintUVW", "puv"),
        ("pointWeight", "pw"),
    )

    pointPositionXYZ = Double3Field()
    xyz = pointPositionXYZ

    pointConstraintUVW = Double3Field()
    puv = pointConstraintUVW

    pointWeight = DoubleField()
    pw = pointWeight


class PointConstraintAttrOperator(
    CompoundAttrOperator[PointConstraintPlugOperator]
):
    __slots__ = ()

    pointPositionXYZ = Double3Field()
    xyz = pointPositionXYZ

    pointConstraintUVW = Double3Field()
    puv = pointConstraintUVW

    pointWeight = DoubleField()
    pw = pointWeight


class PointConstraintField(
    CompoundField[PointConstraintAttrOperator, PointConstraintPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointConstraintAttrOperator
    PLUG_CLS = PointConstraintPlugOperator
