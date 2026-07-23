# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class _GeneratedDefaultShaderList(DG):
    __slots__ = ()

    NODE_TYPE = "defaultShaderList"

    shaders = MessageField(multi=True, readable=False)
    s = shaders
