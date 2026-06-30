# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.mesh import DataMeshField


class PolyGear(DG):
    __slots__ = ()

    NODE_TYPE = "polyGear"

    output = DataMeshField()

    sides = LongField()

    radius = DoubleLinearField()

    internalRadius = DoubleLinearField()

    height = DoubleLinearField()

    heightDivisions = LongField()

    heightBaseline = FloatField()

    gearSpacing = FloatField()

    gearOffset = DoubleLinearField()

    gearTip = FloatField()

    gearMiddle = FloatField()

    twist = DoubleAngleField()

    taper = FloatField()
