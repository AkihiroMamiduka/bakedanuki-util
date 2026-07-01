# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AboutToSetValueTestNode(DG):
    __slots__ = ()

    NODE_TYPE = "aboutToSetValueTestNode"

    attribA = FloatField()
    a = attribA

    attribB = FloatField()
    b = attribB
