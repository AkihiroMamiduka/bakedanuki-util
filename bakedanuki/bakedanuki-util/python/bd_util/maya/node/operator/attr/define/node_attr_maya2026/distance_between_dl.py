# coding: utf-8

from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Point1PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Point1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("point1X", "p1x"),
        ("point1Y", "p1y"),
        ("point1Z", "p1z"),
    )

    point1X = DoubleLinearField(default_value=0.0, readable=False)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=0.0, readable=False)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0, readable=False)
    p1z = point1Z


class Point1AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Point1PlugOperator]
):
    __slots__ = ()

    point1X = DoubleLinearField(default_value=0.0, readable=False)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=0.0, readable=False)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0, readable=False)
    p1z = point1Z


class Point1Field(
    DoubleLinear3CompoundBaseField[Point1AttrOperator, Point1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Point1AttrOperator
    PLUG_CLS = Point1PlugOperator

    point1X = DoubleLinearField(default_value=0.0, readable=False)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=0.0, readable=False)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0, readable=False)
    p1z = point1Z


class Point2PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Point2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("point2X", "p2x"),
        ("point2Y", "p2y"),
        ("point2Z", "p2z"),
    )

    point2X = DoubleLinearField(default_value=0.0, readable=False)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.0, readable=False)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0, readable=False)
    p2z = point2Z


class Point2AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Point2PlugOperator]
):
    __slots__ = ()

    point2X = DoubleLinearField(default_value=0.0, readable=False)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.0, readable=False)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0, readable=False)
    p2z = point2Z


class Point2Field(
    DoubleLinear3CompoundBaseField[Point2AttrOperator, Point2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Point2AttrOperator
    PLUG_CLS = Point2PlugOperator

    point2X = DoubleLinearField(default_value=0.0, readable=False)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.0, readable=False)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0, readable=False)
    p2z = point2Z
