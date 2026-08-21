# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformSine(Shape):
    __slots__ = ()

    NODE_TYPE = "deformSine"

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

    amplitude = DoubleField(
        default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0
    )
    amp = amplitude

    wavelength = DoubleField(
        default_value=2.0,
        min_value=0.001,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    wav = wavelength

    dropoff = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    dr = dropoff

    offset = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    off = offset
