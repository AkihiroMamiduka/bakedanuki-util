# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.revolve import (
    AxisField,
    CompAnchorField,
    CompAxisField,
    CompPivotField,
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


class ComputePivotAndAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SUPPLIED = 0
    PIVOT = 1
    BOTH = 2


class ComputePivotAndAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SUPPLIED = 0
    PIVOT = 1
    BOTH = 2

    NAME_MAP = {
        SUPPLIED: "Supplied",
        PIVOT: "Pivot",
        BOTH: "Both",
    }


class ComputePivotAndAxisEnumField(
    EnumField[ComputePivotAndAxisEnumAttrOperator, ComputePivotAndAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ComputePivotAndAxisEnumAttrOperator
    PLUG_CLS = ComputePivotAndAxisEnumPlugOperator


class AxisChoiceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LONGER = 0
    FIRST = 1
    SECOND = 2


class AxisChoiceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LONGER = 0
    FIRST = 1
    SECOND = 2

    NAME_MAP = {
        LONGER: "Longer",
        FIRST: "First",
        SECOND: "Second",
    }


class AxisChoiceEnumField(
    EnumField[AxisChoiceEnumAttrOperator, AxisChoiceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AxisChoiceEnumAttrOperator
    PLUG_CLS = AxisChoiceEnumPlugOperator


class CompAxisChoiceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LONGER = 0
    FIRST = 1
    SECOND = 2


class CompAxisChoiceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LONGER = 0
    FIRST = 1
    SECOND = 2

    NAME_MAP = {
        LONGER: "Longer",
        FIRST: "First",
        SECOND: "Second",
    }


class CompAxisChoiceEnumField(
    EnumField[CompAxisChoiceEnumAttrOperator, CompAxisChoiceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompAxisChoiceEnumAttrOperator
    PLUG_CLS = CompAxisChoiceEnumPlugOperator


class _GeneratedRevolve(DG):
    __slots__ = ()

    NODE_TYPE = "revolve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

    startSweep = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)
    ssw = startSweep

    endSweep = DoubleAngleField(default_value=360.0, soft_min_value=0.0, soft_max_value=360.0)
    esw = endSweep

    useTolerance = BoolField(default_value=False)
    ut = useTolerance

    degree = DegreeEnumField(default_value=3)
    d = degree

    sections = LongField(default_value=8, min_value=1, soft_max_value=100)
    s = sections

    tolerance = DoubleLinearField(default_value=0.01, min_value=1e-05, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    axis = AxisField(default_value=(1.0, 0.0, 0.0))
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    pivot = PivotField(default_value=(0.0, 0.0, 0.0))
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    autoCorrectNormal = BoolField(default_value=False)
    acn = autoCorrectNormal

    computePivotAndAxis = ComputePivotAndAxisEnumField(default_value=0)
    cpa = computePivotAndAxis

    radius = DoubleLinearField(default_value=1.0)
    r = radius

    radiusAnchor = DoubleField(default_value=-1.0)
    ra = radiusAnchor

    axisChoice = AxisChoiceEnumField(default_value=1)
    aco = axisChoice

    bridge = BoolField(default_value=False)
    br = bridge

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface

    bridgeCurve = DataNurbsCurveField(writable=False)
    bc = bridgeCurve

    compAxis = CompAxisField(default_value=(0.0, 0.0, 0.0), writable=False)
    ca = compAxis
    compAxisX = compAxis.compAxisX
    cax = compAxisX
    compAxisY = compAxis.compAxisY
    cay = compAxisY
    compAxisZ = compAxis.compAxisZ
    caz = compAxisZ

    compPivot = CompPivotField(default_value=(0.0, 0.0, 0.0), writable=False)
    cp = compPivot
    compPivotX = compPivot.compPivotX
    cpx = compPivotX
    compPivotY = compPivot.compPivotY
    cpy = compPivotY
    compPivotZ = compPivot.compPivotZ
    cpz = compPivotZ

    compAxisChoice = CompAxisChoiceEnumField(default_value=0, writable=False)
    cac = compAxisChoice

    compAnchor = CompAnchorField(default_value=(0.0, 0.0, 0.0), writable=False)
    cn = compAnchor
    compAnchorX = compAnchor.compAnchorX
    cnx = compAnchorX
    compAnchorY = compAnchor.compAnchorY
    cny = compAnchorY
    compAnchorZ = compAnchor.compAnchorZ
    cnz = compAnchorZ
