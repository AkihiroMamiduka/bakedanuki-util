# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class AiSwitchOperator(DG):
    __slots__ = ()

    NODE_TYPE = "aiSwitchOperator"

    out = MessageField()

    enable = BoolField()

    inputs = MessageField(multi=True)

    index = LongField()
