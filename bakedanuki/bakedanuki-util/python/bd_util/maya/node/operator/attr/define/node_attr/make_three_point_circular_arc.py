# coding: utf-8

from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class CenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("centerX", "cx"),
        ("centerY", "cy"),
        ("centerZ", "cz"),
    )

    centerX = DoubleLinearField(default_value=0.0, writable=False)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0, writable=False)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0, writable=False)
    cz = centerZ


class CenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CenterPlugOperator]
):
    __slots__ = ()

    centerX = DoubleLinearField(default_value=0.0, writable=False)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0, writable=False)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0, writable=False)
    cz = centerZ


class CenterField(
    DoubleLinear3CompoundBaseField[CenterAttrOperator, CenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CenterAttrOperator
    PLUG_CLS = CenterPlugOperator

    centerX = DoubleLinearField(default_value=0.0, writable=False)
    cx = centerX

    centerY = DoubleLinearField(default_value=0.0, writable=False)
    cy = centerY

    centerZ = DoubleLinearField(default_value=0.0, writable=False)
    cz = centerZ


class NormalPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["NormalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("normalX", "nrx"),
        ("normalY", "nry"),
        ("normalZ", "nrz"),
    )

    normalX = DoubleLinearField(default_value=0.0, writable=False)
    nrx = normalX

    normalY = DoubleLinearField(default_value=0.0, writable=False)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0, writable=False)
    nrz = normalZ


class NormalAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NormalPlugOperator]
):
    __slots__ = ()

    normalX = DoubleLinearField(default_value=0.0, writable=False)
    nrx = normalX

    normalY = DoubleLinearField(default_value=0.0, writable=False)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0, writable=False)
    nrz = normalZ


class NormalField(
    DoubleLinear3CompoundBaseField[NormalAttrOperator, NormalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalAttrOperator
    PLUG_CLS = NormalPlugOperator

    normalX = DoubleLinearField(default_value=0.0, writable=False)
    nrx = normalX

    normalY = DoubleLinearField(default_value=0.0, writable=False)
    nry = normalY

    normalZ = DoubleLinearField(default_value=0.0, writable=False)
    nrz = normalZ


class Point1PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Point1AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("point1X", "p1x"),
        ("point1Y", "p1y"),
        ("point1Z", "p1z"),
    )

    point1X = DoubleLinearField(default_value=0.0)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=1.0)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0)
    p1z = point1Z


class Point1AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Point1PlugOperator]
):
    __slots__ = ()

    point1X = DoubleLinearField(default_value=0.0)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=1.0)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0)
    p1z = point1Z


class Point1Field(
    DoubleLinear3CompoundBaseField[Point1AttrOperator, Point1PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Point1AttrOperator
    PLUG_CLS = Point1PlugOperator

    point1X = DoubleLinearField(default_value=0.0)
    p1x = point1X

    point1Y = DoubleLinearField(default_value=1.0)
    p1y = point1Y

    point1Z = DoubleLinearField(default_value=0.0)
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

    point2X = DoubleLinearField(default_value=0.7071)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.7071)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0)
    p2z = point2Z


class Point2AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Point2PlugOperator]
):
    __slots__ = ()

    point2X = DoubleLinearField(default_value=0.7071)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.7071)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0)
    p2z = point2Z


class Point2Field(
    DoubleLinear3CompoundBaseField[Point2AttrOperator, Point2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Point2AttrOperator
    PLUG_CLS = Point2PlugOperator

    point2X = DoubleLinearField(default_value=0.7071)
    p2x = point2X

    point2Y = DoubleLinearField(default_value=0.7071)
    p2y = point2Y

    point2Z = DoubleLinearField(default_value=0.0)
    p2z = point2Z


class Point3PlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Point3AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("point3X", "p3x"),
        ("point3Y", "p3y"),
        ("point3Z", "p3z"),
    )

    point3X = DoubleLinearField(default_value=1.0)
    p3x = point3X

    point3Y = DoubleLinearField(default_value=0.0)
    p3y = point3Y

    point3Z = DoubleLinearField(default_value=0.0)
    p3z = point3Z


class Point3AttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Point3PlugOperator]
):
    __slots__ = ()

    point3X = DoubleLinearField(default_value=1.0)
    p3x = point3X

    point3Y = DoubleLinearField(default_value=0.0)
    p3y = point3Y

    point3Z = DoubleLinearField(default_value=0.0)
    p3z = point3Z


class Point3Field(
    DoubleLinear3CompoundBaseField[Point3AttrOperator, Point3PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Point3AttrOperator
    PLUG_CLS = Point3PlugOperator

    point3X = DoubleLinearField(default_value=1.0)
    p3x = point3X

    point3Y = DoubleLinearField(default_value=0.0)
    p3y = point3Y

    point3Z = DoubleLinearField(default_value=0.0)
    p3z = point3Z
