# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.angle_dimension import (
    EndPointField,
    MiddlePointField,
    StartPointField,
)
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)


class GeneratedAngleDimension(Shape):
    __slots__ = ()

    NODE_TYPE = "angleDimension"

    startPoint = StartPointField(default_value=(0.0, 0.0, 0.0), readable=False)
    sp = startPoint
    startPointX = startPoint.startPointX
    spx = startPointX
    startPointY = startPoint.startPointY
    spy = startPointY
    startPointZ = startPoint.startPointZ
    spz = startPointZ

    middlePoint = MiddlePointField(
        default_value=(0.0, 0.0, 0.0), readable=False
    )
    mp = middlePoint
    middlePointX = middlePoint.middlePointX
    mpx = middlePointX
    middlePointY = middlePoint.middlePointY
    mpy = middlePointY
    middlePointZ = middlePoint.middlePointZ
    mpz = middlePointZ

    endPoint = EndPointField(default_value=(0.0, 0.0, 0.0), readable=False)
    ep = endPoint
    endPointX = endPoint.endPointX
    epx = endPointX
    endPointY = endPoint.endPointY
    epy = endPointY
    endPointZ = endPoint.endPointZ
    epz = endPointZ

    angle = DoubleAngleField(default_value=0.0, writable=False)
    angl = angle
