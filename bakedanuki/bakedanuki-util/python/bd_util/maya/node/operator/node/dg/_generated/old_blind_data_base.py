# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedOldBlindDataBase(DG):
    __slots__ = ()

    NODE_TYPE = "oldBlindDataBase"

    typeId = LongField(default_value=0)
    tid = typeId
