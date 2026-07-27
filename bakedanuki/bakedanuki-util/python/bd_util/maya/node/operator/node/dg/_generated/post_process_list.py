# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedPostProcessList(DG):
    __slots__ = ()

    NODE_TYPE = "postProcessList"

    postProcesses = MessageField(multi=True, readable=False)
    p = postProcesses
