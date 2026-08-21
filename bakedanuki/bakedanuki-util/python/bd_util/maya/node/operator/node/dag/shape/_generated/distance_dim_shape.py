# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.distance_dim_shape import (
    EndPointField,
    StartPointField,
)
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedDistanceDimShape(Shape):
    __slots__ = ()

    NODE_TYPE = "distanceDimShape"

    startPoint = StartPointField(default_value=(0.0, 0.0, 0.0))
    sp = startPoint
    startPointX = startPoint.startPointX
    spx = startPointX
    startPointY = startPoint.startPointY
    spy = startPointY
    startPointZ = startPoint.startPointZ
    spz = startPointZ

    endPoint = EndPointField(default_value=(0.0, 0.0, 0.0))
    ep = endPoint
    endPointX = endPoint.endPointX
    epx = endPointX
    endPointY = endPoint.endPointY
    epy = endPointY
    endPointZ = endPoint.endPointZ
    epz = endPointZ

    precision = LongField(default_value=6)
    prec = precision

    distance = DoubleField(default_value=0.0, writable=False)
    dist = distance
