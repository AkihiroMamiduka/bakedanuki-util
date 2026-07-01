# coding: utf-8
from ._core import DG


class ChildNode(DG):
    __slots__ = ()

    NODE_TYPE = "childNode"
