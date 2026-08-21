# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.cluster_handle import (
    ClusterTransformsField,
    OriginField,
)
from .....attr.define.std.at.message import MessageField


class GeneratedClusterHandle(Shape):
    __slots__ = ()

    NODE_TYPE = "clusterHandle"

    clusterTransforms = ClusterTransformsField(multi=True, writable=False)
    x = clusterTransforms

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
