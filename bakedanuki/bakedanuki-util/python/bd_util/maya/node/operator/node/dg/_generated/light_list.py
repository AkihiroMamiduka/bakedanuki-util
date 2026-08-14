# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField


class GeneratedLightList(DG):
    __slots__ = ()

    NODE_TYPE = "lightList"

    lights = MessageField(multi=True, readable=False)
    l = lights
