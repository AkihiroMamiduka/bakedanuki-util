# coding: utf-8
from .._core import DG
from ....attr.define.node_attr_maya2026.length import InputField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedLength(DG):
    __slots__ = ()

    NODE_TYPE = "length"

    input = InputField(default_value=(0.0, 0.0, 0.0))
    i = input
    inputX = input.inputX
    ix = inputX
    inputY = input.inputY
    iy = inputY
    inputZ = input.inputZ
    iz = inputZ

    output = DoubleField(default_value=0.0, writable=False)
    o = output
