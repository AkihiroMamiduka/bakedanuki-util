# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AiCollection(DG):
    __slots__ = ()

    NODE_TYPE = "aiCollection"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    inputs = MessageField(multi=True)

    selection = DataStringField()

    collection = DataStringField()
