# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_nurb_cube import (
    AxisField,
    PivotField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class MakeNurbCube(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbCube"

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

    width = DoubleLinearField()
    w = width

    lengthRatio = DoubleField()
    lr = lengthRatio

    heightRatio = DoubleField()
    hr = heightRatio

    patchesU = LongField()
    u = patchesU

    patchesV = LongField()
    v = patchesV

    degree = DegreeEnumField()
    d = degree

    outputSurface1 = DataNurbsSurfaceField()
    os1 = outputSurface1

    outputSurface2 = DataNurbsSurfaceField()
    os2 = outputSurface2

    outputSurface3 = DataNurbsSurfaceField()
    os3 = outputSurface3

    outputSurface4 = DataNurbsSurfaceField()
    os4 = outputSurface4

    outputSurface5 = DataNurbsSurfaceField()
    os5 = outputSurface5
