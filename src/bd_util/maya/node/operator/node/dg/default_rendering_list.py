# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField


class DefaultRenderingList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultRenderingList"

    rendering = MessageField(multi=True)
    r = rendering
