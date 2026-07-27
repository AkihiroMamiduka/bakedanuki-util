# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.triple_shading_switch import (
    DefaultField,
    InputField,
    OutputField,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedTripleShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "tripleShadingSwitch"

    objectId = AddrField(default_value=0.0)
    id = objectId

    input = InputField(multi=True)
    i = input

    inComp1 = FloatField()
    ic1 = inComp1

    inComp2 = FloatField()
    ic2 = inComp2

    inComp3 = FloatField()
    ic3 = inComp3

    default = DefaultField(default_value=(0.800000011920929, 0.800000011920929, 0.800000011920929))
    def_ = default
    defComp1 = default.defComp1
    dc1 = defComp1
    defComp2 = default.defComp2
    dc2 = defComp2
    defComp3 = default.defComp3
    dc3 = defComp3

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = output
    outComp1 = output.outComp1
    oc1 = outComp1
    outComp2 = output.outComp2
    oc2 = outComp2
    outComp3 = output.outComp3
    oc3 = outComp3
