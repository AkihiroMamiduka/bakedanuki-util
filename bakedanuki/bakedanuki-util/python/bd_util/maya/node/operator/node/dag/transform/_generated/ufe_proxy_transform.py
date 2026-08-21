# coding: utf-8
from .._core import Transform
from .....attr.define.std.dt.string import DataStringField


class GeneratedUfeProxyTransform(Transform):
    __slots__ = ()

    NODE_TYPE = "ufeProxyTransform"

    ufePath = DataStringField()
    ufep = ufePath
