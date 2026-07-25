# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.typed import TypedField


class _GeneratedAnimBlend(DG):
    __slots__ = ()

    NODE_TYPE = "animBlend"

    blend = TypedField(writable=False)
    b = blend

    weight = DoubleField(default_value=0.0)
    w = weight
