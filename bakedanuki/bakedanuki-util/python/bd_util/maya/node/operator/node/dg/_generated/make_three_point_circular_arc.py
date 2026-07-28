# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_three_point_circular_arc import (
    CenterField,
    NormalField,
    Point1Field,
    Point2Field,
    Point3Field,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DegreeEnumPlugOperator(EnumPlugOperator["DegreeEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3


class DegreeEnumAttrOperator(EnumAttrOperator[DegreeEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3

    NAME_MAP = {
        LINEAR: "Linear",
        CUBIC: "Cubic",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class GeneratedMakeThreePointCircularArc(DG):
    __slots__ = ()

    NODE_TYPE = "makeThreePointCircularArc"

    degree = DegreeEnumField(default_value=3)
    d = degree

    sections = LongField(default_value=8, min_value=4, soft_max_value=100)
    s = sections

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    centerX = center.centerX
    cx = centerX
    centerY = center.centerY
    cy = centerY
    centerZ = center.centerZ
    cz = centerZ

    normal = NormalField(default_value=(0.0, 0.0, 0.0), writable=False)
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    sweep = DoubleAngleField(default_value=0.0, writable=False)
    sw = sweep

    outputCurve = DataNurbsCurveField(writable=False)
    oc = outputCurve

    point1 = Point1Field(default_value=(0.0, 1.0, 0.0))
    pt1 = point1
    point1X = point1.point1X
    p1x = point1X
    point1Y = point1.point1Y
    p1y = point1Y
    point1Z = point1.point1Z
    p1z = point1Z

    point2 = Point2Field(default_value=(0.7071, 0.7071, 0.0))
    pt2 = point2
    point2X = point2.point2X
    p2x = point2X
    point2Y = point2.point2Y
    p2y = point2Y
    point2Z = point2.point2Z
    p2z = point2Z

    point3 = Point3Field(default_value=(1.0, 0.0, 0.0))
    pt3 = point3
    point3X = point3.point3X
    p3x = point3X
    point3Y = point3.point3Y
    p3y = point3Y
    point3Z = point3.point3Z
    p3z = point3Z

    radius = DoubleLinearField(default_value=0.0, writable=False)
    r = radius
