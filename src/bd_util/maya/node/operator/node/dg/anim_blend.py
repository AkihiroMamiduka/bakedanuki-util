# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField


class AnimBlend(DG):
    __slots__ = ()

    NODE_TYPE = "animBlend"

    blend = TypedField()
    b = blend

    weight = DoubleField()
    w = weight
