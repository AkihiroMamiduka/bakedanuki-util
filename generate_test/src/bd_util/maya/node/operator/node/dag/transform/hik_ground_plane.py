# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField


class HikGroundPlane(Transform):
    __slots__ = ()

    NODE_TYPE = "hikGroundPlane"

    length = DoubleField(default_value=1.0)
    leng = length
