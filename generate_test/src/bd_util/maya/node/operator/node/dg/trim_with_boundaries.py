# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class TrimWithBoundaries(DG):
    __slots__ = ()

    NODE_TYPE = "trimWithBoundaries"

    inputBoundaries = DataNurbsCurveField(multi=True)
    ib = inputBoundaries

    inputSurface = DataNurbsSurfaceField()
    is_ = inputSurface

    flipNormal = BoolField()
    fn = flipNormal

    tolerancePE = DoubleLinearField()
    tpe = tolerancePE

    toleranceE = DoubleLinearField()
    te = toleranceE

    createNewFace = BoolField()
    cnf = createNewFace

    outputSurface = DataNurbsSurfaceField()
    os = outputSurface
