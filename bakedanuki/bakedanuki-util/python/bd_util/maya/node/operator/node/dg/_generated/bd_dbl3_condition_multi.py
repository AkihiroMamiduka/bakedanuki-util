# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_condition_multi import (
    CaseField,
    ElseValueField,
    OutputField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDbl3ConditionMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_ConditionMulti"

    input = DoubleField(default_value=0.0)
    i = input

    case = CaseField(multi=True)
    cs = case

    elseValue = ElseValueField(default_value=(0.0, 0.0, 0.0))
    ev = elseValue
    elseValueX = elseValue.elseValueX
    evx = elseValueX
    elseValueY = elseValue.elseValueY
    evy = elseValueY
    elseValueZ = elseValue.elseValueZ
    evz = elseValueZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
