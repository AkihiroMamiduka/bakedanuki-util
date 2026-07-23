# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.length import InputField
from ....attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class _GeneratedLength(DG):
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

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
