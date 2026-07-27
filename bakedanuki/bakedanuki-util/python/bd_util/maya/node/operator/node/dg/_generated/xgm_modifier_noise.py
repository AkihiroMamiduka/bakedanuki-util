# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.xgm_modifier_noise import MagnitudeScaleField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField


class GeneratedXgmModifierNoise(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierNoise"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    frequency = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    fy = frequency

    magnitude = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True, default_value=(0.0, 0.0, 1.0))
    ms = magnitudeScale

    correlation = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    cl = correlation

    preserveLength = FloatField(default_value=0.0, min_value=0.0, max_value=100.0)
    pl = preserveLength

    tweak = TypedField()
    t = tweak

    live = BoolField(default_value=True)
    lv = live
