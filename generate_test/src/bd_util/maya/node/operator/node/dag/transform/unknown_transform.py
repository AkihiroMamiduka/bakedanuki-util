# coding: utf-8
from ._core import Transform


class UnknownTransform(Transform):
    __slots__ = ()

    NODE_TYPE = "unknownTransform"
