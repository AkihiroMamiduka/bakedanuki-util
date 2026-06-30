# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.angle_between import (
    AxisAngleField,
    EulerField,
    Vector1Field,
    Vector2Field,
)


class AngleBetween(DG):
    __slots__ = ()

    NODE_TYPE = "angleBetween"

    vector1 = Vector1Field()
    v1 = vector1
    vector1X = vector1.vector1X
    v1x = vector1X
    vector1Y = vector1.vector1Y
    v1y = vector1Y
    vector1Z = vector1.vector1Z
    v1z = vector1Z

    vector2 = Vector2Field()
    v2 = vector2
    vector2X = vector2.vector2X
    v2x = vector2X
    vector2Y = vector2.vector2Y
    v2y = vector2Y
    vector2Z = vector2.vector2Z
    v2z = vector2Z

    euler = EulerField()
    eu = euler
    eulerX = euler.eulerX
    eux = eulerX
    eulerY = euler.eulerY
    euy = eulerY
    eulerZ = euler.eulerZ
    euz = eulerZ

    axisAngle = AxisAngleField()
    axa = axisAngle
    axis = axisAngle.axis
    ax = axis
    angle = axisAngle.angle
    a = angle
