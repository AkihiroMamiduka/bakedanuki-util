# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField


class GeneratedModulo(DG):
    __slots__ = ()

    NODE_TYPE = "modulo"

    input = DoubleLinearField(default_value=0.0)
    i = input

    modulus = DoubleLinearField(default_value=1.0)
    m = modulus

    output = DoubleLinearField(default_value=0.0, writable=False)
    o = output
