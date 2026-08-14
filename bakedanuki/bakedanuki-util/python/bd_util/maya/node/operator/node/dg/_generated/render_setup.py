# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedRenderSetup(DG):
    __slots__ = ()

    NODE_TYPE = "renderSetup"

    listItems = MessageField(writable=False)
    lit = listItems

    firstRenderLayer = MessageField()
    frl = firstRenderLayer

    lastRenderLayer = MessageField()
    lrl = lastRenderLayer
