# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDeformFlare(Shape):
    __slots__ = ()

    NODE_TYPE = "deformFlare"

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

    startFlareX = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    sfx = startFlareX

    startFlareZ = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    sfz = startFlareZ

    endFlareX = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    efx = endFlareX

    endFlareZ = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=10.0
    )
    efz = endFlareZ

    curve = DoubleField(
        default_value=0.0, soft_min_value=-3.0, soft_max_value=3.0
    )
    crv = curve
