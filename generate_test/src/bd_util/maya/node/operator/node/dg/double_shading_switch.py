# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.double_shading_switch import (
    DefaultField,
    InputField,
    OutputField,
)
from ...attr.define.std.at.addr import AddrField


class DoubleShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "doubleShadingSwitch"

    objectId = AddrField()
    id = objectId

    input = InputField(multi=True)
    i = input

    # TODO: input.inComp1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: input.inComp2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    default = DefaultField()
    def_ = default
    defComp1 = default.defComp1
    dc1 = defComp1
    defComp2 = default.defComp2
    dc2 = defComp2

    output = OutputField()
    out = output
    outComp1 = output.outComp1
    oc1 = outComp1
    outComp2 = output.outComp2
    oc2 = outComp2
