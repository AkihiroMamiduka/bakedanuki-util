# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class ArnoldAOVChildSelector(DG):
    __slots__ = ()

    NODE_TYPE = "arnoldAOVChildSelector"

    input = LongField()
    in_ = input

    output = LongField()
    out = output

    collection = MessageField()
    c = collection

    arnoldAOVNodeName = DataStringField()
    ann = arnoldAOVNodeName
