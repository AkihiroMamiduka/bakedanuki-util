# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_any_condition_dbl_a_multi import CaseField
from ....attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAngleField,
)
from ....attr.define.std.at.typed import TypedField


class GeneratedBdAnyConditionDblAMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdAny_ConditionDblAMulti"

    input = DoubleAngleField(default_value=0.0)
    i = input

    case = CaseField(multi=True)
    cs = case

    elseValue = TypedField()
    ev = elseValue

    output = TypedField(writable=False)
    o = output
