# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField


class XgmModifierScale(DG):
    __slots__ = ()

    NODE_TYPE = "xgmModifierScale"

    inSplineData = TypedField()
    isd = inSplineData

    outSplineData = TypedField()
    osd = outSplineData

    mute = BoolField()
    m = mute

    mask = FloatField()
    mk = mask

    scale = FloatField()
    s = scale
