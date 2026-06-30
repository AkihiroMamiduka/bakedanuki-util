# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class Choice(DG):
    __slots__ = ()

    NODE_TYPE = "choice"

    selector = LongField()
    s = selector

    input = TypedField(multi=True)
    i = input

    output = TypedField()
    o = output
