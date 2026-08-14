# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)
from ....attr.define.std.dt.mesh import DataMeshField


class GeneratedPolyGear(DG):
    __slots__ = ()

    NODE_TYPE = "polyGear"

    output = DataMeshField(writable=False)

    sides = LongField(default_value=16, min_value=3, soft_max_value=20)

    radius = DoubleLinearField(
        default_value=1.0, min_value=0.001, soft_max_value=100.0
    )

    internalRadius = DoubleLinearField(
        default_value=0.3, min_value=0.0, soft_max_value=50.0
    )

    height = DoubleLinearField(
        default_value=1.0, min_value=0.001, soft_max_value=100.0
    )

    heightDivisions = LongField(
        default_value=10, min_value=1, soft_max_value=40
    )

    heightBaseline = FloatField(
        default_value=0.0, min_value=-1.0, max_value=1.0
    )

    gearSpacing = FloatField(
        default_value=0.6000000238418579, min_value=0.0, soft_max_value=1.0
    )

    gearOffset = DoubleLinearField(
        default_value=0.2, min_value=0.0, soft_max_value=20.0
    )

    gearTip = FloatField(default_value=0.5, min_value=0.0, soft_max_value=1.0)

    gearMiddle = FloatField(
        default_value=1.2000000476837158, min_value=0.0, soft_max_value=1.0
    )

    twist = DoubleAngleField(
        default_value=0.0,
        soft_min_value=-59.99999999999999,
        soft_max_value=59.99999999999999,
    )

    taper = FloatField(default_value=1.0, min_value=0.001, soft_max_value=10.0)
