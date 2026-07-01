# coding: utf-8
from ._core import DG
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class Modulo(DG):
    __slots__ = ()

    NODE_TYPE = "modulo"

    input = DoubleLinearField()
    i = input

    modulus = DoubleLinearField()
    m = modulus

    output = DoubleLinearField()
    o = output
