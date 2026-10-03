# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedBdDeleteWithOwner(DG):
    __slots__ = ()

    NODE_TYPE = "bdDeleteWithOwner"

    owner = MessageField(readable=False)
    own = owner

    deleteTarget = MessageField(multi=True, readable=False)
    dt = deleteTarget
