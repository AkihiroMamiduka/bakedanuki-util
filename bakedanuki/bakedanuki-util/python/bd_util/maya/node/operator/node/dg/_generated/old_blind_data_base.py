# coding: utf-8
from .._core import DG
from ....attr.define.std.at.numeric_scalar_range.long import LongField


class _GeneratedOldBlindDataBase(DG):
    __slots__ = ()

    NODE_TYPE = "oldBlindDataBase"

    typeId = LongField(default_value=0)
    tid = typeId
