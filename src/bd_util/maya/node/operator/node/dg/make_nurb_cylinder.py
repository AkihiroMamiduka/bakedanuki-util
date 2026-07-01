# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_nurb_cylinder import (
    AxisField,
    PivotField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class MakeNurbCylinder(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbCylinder"

    pivot = PivotField()
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    axis = AxisField()
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    radius = DoubleLinearField()
    r = radius

    startSweep = DoubleAngleField()
    ssw = startSweep

    endSweep = DoubleAngleField()
    esw = endSweep

    useTolerance = BoolField()
    ut = useTolerance

    degree = DegreeEnumField()
    d = degree

    sections = LongField()
    s = sections

    spans = LongField()
    nsp = spans

    tolerance = DoubleLinearField()
    tol = tolerance

    heightRatio = DoubleField()
    hr = heightRatio

    topCapCurve = DataNurbsCurveField()
    tcc = topCapCurve

    bottomCapCurve = DataNurbsCurveField()
    bcc = bottomCapCurve

    absoluteSweepDifference = DoubleAngleField()
    asd = absoluteSweepDifference
