# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl_wt_add_multi import InputField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDblWtAddMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl_WtAddMulti"

    input = InputField(multi=True, default_value=(0.0, 0.0))
    i = input

    output = DoubleField(default_value=0.0, writable=False)
    o = output
