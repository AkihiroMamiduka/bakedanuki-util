# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedLog(DG):
    __slots__ = ()

    NODE_TYPE = "log"

    input = DoubleField(default_value=0.0, min_value=0.0)
    i = input

    base = DoubleField(default_value=2.0, min_value=0.0)
    e = base

    output = DoubleField(default_value=0.0, writable=False)
    o = output
