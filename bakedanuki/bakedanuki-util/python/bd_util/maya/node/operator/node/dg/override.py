# coding: utf-8
from ._core import DG


class Override(DG):
    __slots__ = ()

    NODE_TYPE = "override"
