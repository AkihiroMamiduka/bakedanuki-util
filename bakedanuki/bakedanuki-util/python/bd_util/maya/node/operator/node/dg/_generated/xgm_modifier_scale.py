# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.typed import TypedField


class GeneratedXgmModifierScale(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierScale"

    inSplineData = TypedField(readable=False)
    isd = inSplineData

    outSplineData = TypedField(writable=False)
    osd = outSplineData

    mute = BoolField(default_value=False)
    m = mute

    mask = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    mk = mask

    scale = FloatField(default_value=1.0, soft_min_value=0.10000000149011612, soft_max_value=10.0)
    s = scale
