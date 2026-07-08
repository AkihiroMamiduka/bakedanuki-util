# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class TransferFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "transferFalloff"

    weightedGeometry = TypedField()
    wgm = weightedGeometry

    weightFunction = TypedField(multi=True)
    iwf = weightFunction

    useBindTags = BoolField(default_value=False)
    ubt = useBindTags

    bindTagsFilter = DataStringField()
    btf = bindTagsFilter

    outputWeightFunction = TypedField(multi=True, writable=False)
    wft = outputWeightFunction
