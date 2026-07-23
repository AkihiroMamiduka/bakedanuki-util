# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedArnoldAOVChildSelector(DG):
    __slots__ = ()

    NODE_TYPE = "arnoldAOVChildSelector"

    input = LongField(default_value=0)
    in_ = input

    output = LongField(default_value=0)
    out = output

    collection = MessageField(writable=False)
    c = collection

    arnoldAOVNodeName = DataStringField()
    ann = arnoldAOVNodeName
