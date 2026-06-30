# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AiIncludeGraph(DG):
    __slots__ = ()

    NODE_TYPE = "aiIncludeGraph"

    out = MessageField()

    enable = BoolField()

    inputs = MessageField(multi=True)

    filename = DataStringField()

    target = DataStringField()
