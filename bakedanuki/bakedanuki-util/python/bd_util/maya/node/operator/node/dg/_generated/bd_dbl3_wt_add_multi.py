# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.bd_dbl3_wt_add_multi import (
    InputField,
    OutputField,
)
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedBdDbl3WtAddMulti(DG):
    __slots__ = ()

    NODE_TYPE = "bdDbl3_WtAddMulti"

    input = InputField(multi=True)
    i = input

    valueX = DoubleField()
    vx = valueX

    valueY = DoubleField()
    vy = valueY

    valueZ = DoubleField()
    vz = valueZ

    output = OutputField(default_value=(0.0, 0.0, 0.0), writable=False)
    o = output
    outputX = output.outputX
    ox = outputX
    outputY = output.outputY
    oy = outputY
    outputZ = output.outputZ
    oz = outputZ
