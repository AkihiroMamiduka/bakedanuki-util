# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_nurbs_square import (
    CenterField,
    NormalField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


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


class _GeneratedMakeNurbsSquare(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbsSquare"

    normal = NormalField(default_value=(0.0, 0.0, 1.0))
    nr = normal
    normalX = normal.normalX
    nrx = normalX
    normalY = normal.normalY
    nry = normalY
    normalZ = normal.normalZ
    nrz = normalZ

    center = CenterField(default_value=(0.0, 0.0, 0.0))
    c = center
    centerX = center.centerX
    cx = centerX
    centerY = center.centerY
    cy = centerY
    centerZ = center.centerZ
    cz = centerZ

    sideLength1 = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    sl1 = sideLength1

    sideLength2 = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    sl2 = sideLength2

    degree = DegreeEnumField(default_value=3)
    d = degree

    spansPerSide = LongField(default_value=1, min_value=1, max_value=1024, soft_max_value=4)
    sps = spansPerSide

    outputCurve1 = DataNurbsCurveField(writable=False)
    oc1 = outputCurve1

    outputCurve2 = DataNurbsCurveField(writable=False)
    oc2 = outputCurve2

    outputCurve3 = DataNurbsCurveField(writable=False)
    oc3 = outputCurve3

    outputCurve4 = DataNurbsCurveField(writable=False)
    oc4 = outputCurve4
