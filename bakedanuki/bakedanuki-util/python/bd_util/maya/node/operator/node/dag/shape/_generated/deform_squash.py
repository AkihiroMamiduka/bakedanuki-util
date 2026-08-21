# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformSquash(Shape):
    __slots__ = ()

    NODE_TYPE = "deformSquash"

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

    startSmoothness = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    ss = startSmoothness

    endSmoothness = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    es = endSmoothness

    maxExpandPos = DoubleField(
        default_value=0.5, min_value=0.01, max_value=0.99
    )
    mp = maxExpandPos

    expand = DoubleField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    exp = expand

    factor = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    fac = factor
