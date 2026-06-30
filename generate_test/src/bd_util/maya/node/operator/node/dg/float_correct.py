# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class FloatCorrect(DG):
    __slots__ = ()

    NODE_TYPE = "floatCorrect"

    inFloat = FloatField()
    _f = inFloat

    gain = FloatField()
    _g = gain

    offset = FloatField()
    _o = offset

    gammaScale = FloatField()
    _gg = gammaScale

    clampOutput = BoolField()
    _cmp = clampOutput

    clampMin = FloatField()
    _cmn = clampMin

    clampMax = FloatField()
    _cmx = clampMax

    outFloat = FloatField()
    of = outFloat
