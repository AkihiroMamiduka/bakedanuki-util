# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.soft_mod_handle import (
    OriginField,
    SoftModTransformsField,
)
from .....attr.define.std.at.message import MessageField


class GeneratedSoftModHandle(Shape):
    __slots__ = ()

    NODE_TYPE = "softModHandle"

    softModTransforms = SoftModTransformsField(multi=True, writable=False)
    x = softModTransforms

    origin = OriginField(default_value=(0.0, 0.0, 0.0))
    or_ = origin
    originX = origin.originX
    ox = originX
    originY = origin.originY
    oy = originY
    originZ = origin.originZ
    oz = originZ

    weightedNode = MessageField(readable=False)
    wn = weightedNode
