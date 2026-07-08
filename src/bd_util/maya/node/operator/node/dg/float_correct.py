# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "floatCorrect"

    inFloat = FloatField(default_value=1.0)
    f = inFloat

    gain = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    g = gain

    offset = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    o = offset

    gammaScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=5.0)
    gg = gammaScale

    clampOutput = BoolField(default_value=False)
    cmp = clampOutput

    clampMin = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    cmn = clampMin

    clampMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)
    cmx = clampMax

    outFloat = FloatField(default_value=0.0, writable=False)
    of = outFloat
