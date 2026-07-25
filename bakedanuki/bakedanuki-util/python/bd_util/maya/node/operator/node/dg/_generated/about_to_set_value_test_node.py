# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class _GeneratedAboutToSetValueTestNode(DG):
    __slots__ = ()

    NODE_TYPE = "aboutToSetValueTestNode"

    attribA = FloatField(default_value=2.0)
    a = attribA

    attribB = FloatField(default_value=2.0)
    b = attribB
