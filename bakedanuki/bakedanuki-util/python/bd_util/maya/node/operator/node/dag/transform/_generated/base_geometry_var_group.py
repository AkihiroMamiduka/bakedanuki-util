# coding: utf-8
from .._core import Transform
from .....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedBaseGeometryVarGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "baseGeometryVarGroup"

    maxCreated = LongField(default_value=-1)
    mc = maxCreated
