# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


class GeneratedSubdivCollapse(DG):
    __slots__ = ()

    NODE_TYPE = "subdivCollapse"

    inSubdiv = TypedField()
    is_ = inSubdiv

    outSubdiv = TypedField()
    os = outSubdiv

    level = LongField(default_value=0, min_value=0, max_value=12, soft_min_value=0, soft_max_value=2)
    l = level
