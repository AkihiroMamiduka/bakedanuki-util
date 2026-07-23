# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.single_shading_switch import InputField
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField


class _GeneratedSingleShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "singleShadingSwitch"

    objectId = AddrField(default_value=0.0)
    id = objectId

    input = InputField(multi=True)
    i = input

    default = FloatField(default_value=0.0)
    def_ = default

    output = FloatField(default_value=0.0, writable=False)
    out = output
