# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearField,
)


class GeneratedBdDblLValue(DG):
    __slots__ = ()

    NODE_TYPE = "bdDblL_Value"

    value = DoubleLinearField(default_value=0.0)
    v = value
