# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField


class HipsScalePlugOperator(
    CompoundPlugOperator["HipsScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("hipsScaleX", "hipsScaleX"),
        ("hipsScaleY", "hipsScaleY"),
        ("hipsScaleZ", "hipsScaleZ"),
    )

    hipsScaleX = DoubleField()

    hipsScaleY = DoubleField()

    hipsScaleZ = DoubleField()


class HipsScaleAttrOperator(
    CompoundAttrOperator[HipsScalePlugOperator]
):
    __slots__ = ()

    hipsScaleX = DoubleField()

    hipsScaleY = DoubleField()

    hipsScaleZ = DoubleField()


class HipsScaleField(
    CompoundField[HipsScaleAttrOperator, HipsScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HipsScaleAttrOperator
    PLUG_CLS = HipsScalePlugOperator

    hipsScaleX = DoubleField()

    hipsScaleY = DoubleField()

    hipsScaleZ = DoubleField()
