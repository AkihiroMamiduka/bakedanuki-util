# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class StitchAsNurbsShell(DG):
    __slots__ = ()

    NODE_TYPE = "stitchAsNurbsShell"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    tolerance = DoubleLinearField()
    tol = tolerance

    outputShell = TypedField()
    osh = outputShell
