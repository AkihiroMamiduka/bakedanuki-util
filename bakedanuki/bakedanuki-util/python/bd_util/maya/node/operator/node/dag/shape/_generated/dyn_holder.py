# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.message import MessageField


class GeneratedDynHolder(Shape):
    __slots__ = ()

    NODE_TYPE = "dynHolder"

    connectionsToMe = MessageField(multi=True)
    ct = connectionsToMe

    auxiliariesOwned = MessageField()
    ao = auxiliariesOwned
