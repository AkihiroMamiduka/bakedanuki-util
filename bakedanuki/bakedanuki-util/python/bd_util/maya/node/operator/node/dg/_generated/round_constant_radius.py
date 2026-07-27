# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.round_constant_radius import EdgeField
from ....attr.define.std.at.scalar.numeric.range.short import ShortField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedRoundConstantRadius(DG):
    __slots__ = ()

    NODE_TYPE = "roundConstantRadius"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    radius = DoubleLinearField(multi=True, default_value=1.0)
    r = radius

    edge = EdgeField(multi=True)
    e = edge

    tolerance = DoubleLinearField(default_value=0.01, soft_min_value=0.001, soft_max_value=1.0)
    tol = tolerance

    filletStatus = ShortField(multi=True, default_value=0, writable=False)
    fis = filletStatus

    originalSurface = DataNurbsSurfaceField(multi=True, writable=False)
    os = originalSurface

    filletSurface = DataNurbsSurfaceField(multi=True, writable=False)
    fs = filletSurface

    cornerSurface = DataNurbsSurfaceField(multi=True, writable=False)
    cs = cornerSurface
