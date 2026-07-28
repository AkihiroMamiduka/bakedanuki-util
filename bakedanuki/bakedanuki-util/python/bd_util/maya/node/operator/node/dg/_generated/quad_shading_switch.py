# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.quad_shading_switch import (
    DefaultField,
    InputField,
    OutputField,
)
from ....attr.define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)
from ....attr.define.std.at.addr import AddrField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedQuadShadingSwitch(DG):
    __slots__ = ()

    NODE_TYPE = "quadShadingSwitch"

    objectId = AddrField(default_value=0.0)
    id = objectId

    input = InputField(multi=True)
    i = input

    inTriple = Float3Field()
    itr = inTriple

    inComp1 = FloatField()
    ic1 = inComp1

    inComp2 = FloatField()
    ic2 = inComp2

    inComp3 = FloatField()
    ic3 = inComp3

    inSingle = FloatField()
    isi = inSingle

    default = DefaultField()
    def_ = default
    defTriple = default.defTriple
    dtr = defTriple
    defSingle = default.defSingle
    dsi = defSingle

    output = OutputField(writable=False)
    out = output
    outTriple = output.outTriple
    otr = outTriple
    outSingle = output.outSingle
    osi = outSingle
