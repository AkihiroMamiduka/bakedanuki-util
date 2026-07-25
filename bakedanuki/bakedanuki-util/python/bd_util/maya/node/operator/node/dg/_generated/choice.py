# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


class _GeneratedChoice(DG):
    __slots__ = ()

    NODE_TYPE = "choice"

    selector = LongField(default_value=0, min_value=0)
    s = selector

    input = TypedField(multi=True)
    i = input

    output = TypedField(writable=False)
    o = output
