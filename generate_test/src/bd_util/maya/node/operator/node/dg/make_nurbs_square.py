# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_nurbs_square import (
    CenterField,
    NormalField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class DegreeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7


class DegreeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 1
    QUADRATIC = 2
    CUBIC = 3
    QUINTIC = 5
    HEPTIC = 7

    NAME_MAP = {
        LINEAR: "Linear",
        QUADRATIC: "Quadratic",
        CUBIC: "Cubic",
        QUINTIC: "Quintic",
        HEPTIC: "Heptic",
    }


class DegreeEnumField(
    EnumField[DegreeEnumAttrOperator, DegreeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DegreeEnumAttrOperator
    PLUG_CLS = DegreeEnumPlugOperator


class MakeNurbsSquare(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbsSquare"

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

    sideLength1 = DoubleLinearField()
    sl1 = sideLength1

    sideLength2 = DoubleLinearField()
    sl2 = sideLength2

    degree = DegreeEnumField()
    d = degree

    spansPerSide = LongField()
    sps = spansPerSide

    outputCurve1 = DataNurbsCurveField()
    oc1 = outputCurve1

    outputCurve2 = DataNurbsCurveField()
    oc2 = outputCurve2

    outputCurve3 = DataNurbsCurveField()
    oc3 = outputCurve3

    outputCurve4 = DataNurbsCurveField()
    oc4 = outputCurve4
