# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_nurb_circle import (
    CenterField,
    FirstField,
    NormalField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    CUBIC = 3


class DegreeEnumAttrOperator(EnumAttrOperator):
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


class MakeNurbCircle(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbCircle"

    first = FirstField()
    fp = first
    firstPointX = first.firstPointX
    fpx = firstPointX
    firstPointY = first.firstPointY
    fpy = firstPointY
    firstPointZ = first.firstPointZ
    fpz = firstPointZ

    normal = NormalField()
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    center = CenterField()
    c = center
    centerX = center.centerX
    cx = centerX
    centerY = center.centerY
    cy = centerY
    centerZ = center.centerZ
    cz = centerZ

    radius = DoubleLinearField()
    r = radius

    sweep = DoubleAngleField()
    sw = sweep

    useTolerance = BoolField()
    ut = useTolerance

    degree = DegreeEnumField()
    d = degree

    sections = LongField()
    s = sections

    tolerance = DoubleLinearField()
    tol = tolerance

    fixCenter = BoolField()
    fc = fixCenter

    outputCurve = DataNurbsCurveField()
    oc = outputCurve
