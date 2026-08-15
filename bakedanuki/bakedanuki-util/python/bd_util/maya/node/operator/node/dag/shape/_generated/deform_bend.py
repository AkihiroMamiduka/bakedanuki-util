# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformBend(Shape):
    __slots__ = ()

    NODE_TYPE = "deformBend"

    deformerData = DataDoubleArrayField()
    dd = deformerData

    handleWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=50.0
    )
    hw = handleWidth

    lowBound = DoubleField(
        default_value=-1.0,
        max_value=0.0,
        soft_min_value=-10.0,
        soft_max_value=0.0,
    )
    lb = lowBound

    highBound = DoubleField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    hb = highBound

    curvature = DoubleAngleField(
        default_value=0.0,
        soft_min_value=-179.9998479605043,
        soft_max_value=179.9998479605043,
    )
    cur = curvature
