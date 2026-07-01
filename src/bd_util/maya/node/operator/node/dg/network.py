# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField


class Network(DG):
    __slots__ = ()

    NODE_TYPE = "network"

    affects = MessageField(multi=True)
    a = affects

    affectedBy = MessageField(multi=True)
    ab = affectedBy
