# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.distance_between import (
    Point1Field,
    Point2Field,
)
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField


class DistanceBetween(DG):
    __slots__ = ()

    NODE_TYPE = "distanceBetween"

    point1 = Point1Field()
    p1 = point1
    point1X = point1.point1X
    p1x = point1X
    point1Y = point1.point1Y
    p1y = point1Y
    point1Z = point1.point1Z
    p1z = point1Z

    inMatrix1 = DataMatrixField()
    im1 = inMatrix1

    point2 = Point2Field()
    p2 = point2
    point2X = point2.point2X
    p2x = point2X
    point2Y = point2.point2Y
    p2y = point2Y
    point2Z = point2.point2Z
    p2z = point2Z

    inMatrix2 = DataMatrixField()
    im2 = inMatrix2

    distance = DoubleLinearField()
    d = distance
