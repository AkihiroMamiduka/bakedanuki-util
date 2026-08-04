# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_condition_multi import CaseField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblConditionMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_ConditionMulti"

    input = DoubleField(default_value=0.0)
    i = input

    case = CaseField(multi=True, default_value=(0.0, 0.0, 0.0))
    cs = case

    elseValue = DoubleField(default_value=0.0)
    ev = elseValue

    output = DoubleField(default_value=0.0, writable=False)
    o = output
