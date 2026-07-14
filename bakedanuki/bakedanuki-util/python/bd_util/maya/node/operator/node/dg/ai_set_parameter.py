# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AiSetParameter(DG):
    __slots__ = ()

    NODE_TYPE = "aiSetParameter"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    assignment = DataStringField(multi=True)

    enableAssignment = BoolField(multi=True, default_value=True)
    enable_assignment = enableAssignment
