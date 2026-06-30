# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField


class AiMerge(DG):
    __slots__ = ()

    NODE_TYPE = "aiMerge"

    out = MessageField()

    enable = BoolField()

    inputs = MessageField(multi=True)
