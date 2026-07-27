# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_nurb_cube import (
    AxisField,
    PivotField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


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


class GeneratedMakeNurbCube(DG):
    __slots__ = ()

    NODE_TYPE = "makeNurbCube"

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

    width = DoubleLinearField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    w = width

    lengthRatio = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    lr = lengthRatio

    heightRatio = DoubleField(default_value=1.0, soft_min_value=0.0, soft_max_value=10.0)
    hr = heightRatio

    patchesU = LongField(default_value=1, min_value=1, max_value=1000, soft_max_value=100)
    u = patchesU

    patchesV = LongField(default_value=1, min_value=1, max_value=1000, soft_max_value=100)
    v = patchesV

    degree = DegreeEnumField(default_value=3)
    d = degree

    outputSurface1 = DataNurbsSurfaceField(writable=False)
    os1 = outputSurface1

    outputSurface2 = DataNurbsSurfaceField(writable=False)
    os2 = outputSurface2

    outputSurface3 = DataNurbsSurfaceField(writable=False)
    os3 = outputSurface3

    outputSurface4 = DataNurbsSurfaceField(writable=False)
    os4 = outputSurface4

    outputSurface5 = DataNurbsSurfaceField(writable=False)
    os5 = outputSurface5
