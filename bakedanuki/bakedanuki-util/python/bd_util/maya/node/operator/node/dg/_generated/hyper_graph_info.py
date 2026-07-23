# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class _GeneratedHyperGraphInfo(DG):
    __slots__ = ()

    NODE_TYPE = "hyperGraphInfo"

    bookmarks = MessageField(multi=True)
    b = bookmarks
