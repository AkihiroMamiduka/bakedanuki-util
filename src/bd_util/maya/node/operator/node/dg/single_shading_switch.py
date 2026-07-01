# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.single_shading_switch import InputField
from ...attr.define.std.at.addr import AddrField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class SingleShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "singleShadingSwitch"

    objectId = AddrField()
    id = objectId

    input = InputField(multi=True)
    i = input

    default = FloatField()
    def_ = default

    output = FloatField()
    out = output
