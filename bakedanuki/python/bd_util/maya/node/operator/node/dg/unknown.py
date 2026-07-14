# coding: utf-8
from ._core import DG


class Unknown(DG):
    __slots__ = ()

    NODE_TYPE = "unknown"
