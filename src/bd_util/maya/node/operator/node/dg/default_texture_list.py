# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField


class DefaultTextureList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultTextureList"

    textures = MessageField(multi=True)
    tx = textures
