# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_nurb_sphere import (
    AxisField,
    PivotField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class _GeneratedMakeNurbSphere(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbSphere"

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    axis = AxisField(default_value=(1.0, 0.0, 0.0))
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    radius = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    r = radius

    startSweep = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ssw = startSweep

    endSweep = DoubleAngleField(default_value=360.0, soft_min_value=0.0, soft_max_value=360.0)
    esw = endSweep

    useTolerance = BoolField(default_value=False)
    ut = useTolerance

    degree = DegreeEnumField(default_value=3)
    d = degree

    sections = LongField(default_value=8, min_value=1, max_value=1000, soft_max_value=100)
    s = sections

    spans = LongField(default_value=1, min_value=1, max_value=1000, soft_max_value=100)
    nsp = spans

    tolerance = DoubleLinearField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    heightRatio = DoubleField(default_value=2.0, soft_min_value=0.1, soft_max_value=10.0)
    hr = heightRatio

    topCapCurve = DataNurbsCurveField(writable=False)
    tcc = topCapCurve

    bottomCapCurve = DataNurbsCurveField(writable=False)
    bcc = bottomCapCurve

    absoluteSweepDifference = DoubleAngleField(default_value=0.0, writable=False)
    asd = absoluteSweepDifference
