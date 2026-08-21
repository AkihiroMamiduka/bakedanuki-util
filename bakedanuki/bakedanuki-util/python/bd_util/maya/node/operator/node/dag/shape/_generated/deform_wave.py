# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformWave(Shape):
    __slots__ = ()

    NODE_TYPE = "deformWave"

    deformerData = DataDoubleArrayField()
    dd = deformerData

    handleWidth = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=50.0
    )
    hw = handleWidth

    maxRadius = DoubleField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    mxr = maxRadius

    minRadius = DoubleField(
        default_value=0.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    mnr = minRadius

    amplitude = DoubleField(
        default_value=0.0, soft_min_value=-5.0, soft_max_value=5.0
    )
    amp = amplitude

    wavelength = DoubleField(
        default_value=1.0,
        min_value=0.1,
        soft_min_value=0.1,
        soft_max_value=10.0,
    )
    wav = wavelength

    dropoff = DoubleField(default_value=0.0, min_value=-1.0, max_value=1.0)
    dr = dropoff

    dropoffPosition = DoubleField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    dp = dropoffPosition

    offset = DoubleField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    off = offset
