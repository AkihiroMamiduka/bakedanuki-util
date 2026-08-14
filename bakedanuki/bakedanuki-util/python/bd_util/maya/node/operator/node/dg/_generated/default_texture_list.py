# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedDefaultTextureList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultTextureList"

    textures = MessageField(multi=True, readable=False)
    tx = textures
