# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class _GeneratedProxyManager(DG):
    __slots__ = ()

    NODE_TYPE = "proxyManager"

    proxyList = MessageField(multi=True)
    plst = proxyList

    activeProxy = MessageField()
    aprx = activeProxy

    sharedEditsOwner = MessageField()
    psed = sharedEditsOwner
