# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.xgm_modifier_noise import MagnitudeScaleField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class XgmModifierNoise(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierNoise"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    mask = FloatField()
    mk = mask

    frequency = FloatField()
    fy = frequency

    magnitude = FloatField()
    mg = magnitude

    magnitudeScale = MagnitudeScaleField(multi=True)
    ms = magnitudeScale

    correlation = FloatField()
    cl = correlation

    preserveLength = FloatField()
    pl = preserveLength

    tweak = TypedField()
    t = tweak

    live = BoolField()
    lv = live
