# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformTwist(Shape):
    __slots__ = ()

    NODE_TYPE = "deformTwist"

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

    startAngle = DoubleAngleField(
        default_value=0.0,
        soft_min_value=-859.4366926962348,
        soft_max_value=859.4366926962348,
    )
    sa = startAngle

    endAngle = DoubleAngleField(
        default_value=0.0,
        soft_min_value=-859.4366926962348,
        soft_max_value=859.4366926962348,
    )
    ea = endAngle
