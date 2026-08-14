# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedStitchAsNurbsShell(DG):
    __slots__ = ()

    NODE_TYPE = "stitchAsNurbsShell"

    inputSurface = DataNurbsSurfaceField(multi=True)
    is_ = inputSurface

    tolerance = DoubleLinearField(
        default_value=0.1, soft_min_value=0.001, soft_max_value=1.0
    )
    tol = tolerance

    outputShell = TypedField(writable=False)
    osh = outputShell
