# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class _GeneratedTrimWithBoundaries(DG):
    __slots__ = ()

    NODE_TYPE = "trimWithBoundaries"

    inputBoundaries = DataNurbsCurveField(multi=True)
    ib = inputBoundaries

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    flipNormal = BoolField(default_value=False)
    fn = flipNormal

    tolerancePE = DoubleLinearField(default_value=1e-05, soft_min_value=5e-06, soft_max_value=0.001)
    tpe = tolerancePE

    toleranceE = DoubleLinearField(default_value=0.001, soft_min_value=0.0001, soft_max_value=0.1)
    te = toleranceE

    createNewFace = BoolField(default_value=False)
    cnf = createNewFace

    outputSurface = DataNurbsSurfaceField(writable=False)
    os = outputSurface
