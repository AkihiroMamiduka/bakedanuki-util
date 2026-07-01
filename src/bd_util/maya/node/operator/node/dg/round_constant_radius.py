# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.round_constant_radius import EdgeField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class RoundConstantRadius(DG):
    __slots__ = ()

    NODE_TYPE = "roundConstantRadius"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    radius = DoubleLinearField(multi=True)
    r = radius

    edge = EdgeField(multi=True)
    e = edge

    tolerance = DoubleLinearField()
    tol = tolerance

    filletStatus = ShortField(multi=True)
    fis = filletStatus

    originalSurface = DataNurbsSurfaceField(multi=True)
    os = originalSurface

    filletSurface = DataNurbsSurfaceField(multi=True)
    fs = filletSurface

    cornerSurface = DataNurbsSurfaceField(multi=True)
    cs = cornerSurface
