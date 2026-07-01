# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.revolve import (
    AxisField,
    CompAnchorField,
    CompAxisField,
    CompPivotField,
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


class Revolve(DG):
    __slots__ = ()

    NODE_TYPE = "revolve"

    inputCurve = DataNurbsCurveField()
    ic = inputCurve

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

    tolerance = DoubleLinearField()
    tol = tolerance

    axis = AxisField()
    ax = axis
    axisX = axis.axisX
    axx = axisX
    axisY = axis.axisY
    axy = axisY
    axisZ = axis.axisZ
    axz = axisZ

    pivot = PivotField()
    p = pivot
    pivotX = pivot.pivotX
    px = pivotX
    pivotY = pivot.pivotY
    py = pivotY
    pivotZ = pivot.pivotZ
    pz = pivotZ

    autoCorrectNormal = BoolField()
    acn = autoCorrectNormal

    computePivotAndAxis = ComputePivotAndAxisEnumField()
    cpa = computePivotAndAxis

    radius = DoubleLinearField()
    r = radius

    radiusAnchor = DoubleField()
    ra = radiusAnchor

    axisChoice = AxisChoiceEnumField()
    aco = axisChoice

    bridge = BoolField()
    br = bridge

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface

    bridgeCurve = DataNurbsCurveField()
    bc = bridgeCurve

    compAxis = CompAxisField()
    ca = compAxis
    compAxisX = compAxis.compAxisX
    cax = compAxisX
    compAxisY = compAxis.compAxisY
    cay = compAxisY
    compAxisZ = compAxis.compAxisZ
    caz = compAxisZ

    compPivot = CompPivotField()
    cp = compPivot
    compPivotX = compPivot.compPivotX
    cpx = compPivotX
    compPivotY = compPivot.compPivotY
    cpy = compPivotY
    compPivotZ = compPivot.compPivotZ
    cpz = compPivotZ

    compAxisChoice = CompAxisChoiceEnumField()
    cac = compAxisChoice

    compAnchor = CompAnchorField()
    cn = compAnchor
    compAnchorX = compAnchor.compAnchorX
    cnx = compAnchorX
    compAnchorY = compAnchor.compAnchorY
    cny = compAnchorY
    compAnchorZ = compAnchor.compAnchorZ
    cnz = compAnchorZ
