# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "floatCorrect"

    inFloat = FloatField()
    f = inFloat

    gain = FloatField()
    g = gain

    offset = FloatField()
    o = offset

    gammaScale = FloatField()
    gg = gammaScale

    clampOutput = BoolField()
    cmp = clampOutput

    clampMin = FloatField()
    cmn = clampMin

    clampMax = FloatField()
    cmx = clampMax

    outFloat = FloatField()
    of = outFloat
