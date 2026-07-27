# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedAiSwitchOperator(DG):
    __slots__ = ()

    NODE_TYPE = "aiSwitchOperator"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    index = LongField(default_value=0)
