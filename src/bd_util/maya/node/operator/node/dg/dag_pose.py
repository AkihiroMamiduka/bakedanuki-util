# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.matrix import DataMatrixField


class DagPose(DG):
    __slots__ = ()

    NODE_TYPE = "dagPose"

    worldMatrix = DataMatrixField(multi=True)
    wm = worldMatrix

    xformMatrix = DataMatrixField(multi=True)
    xm = xformMatrix

    members = MessageField(multi=True)
    m = members

    parents = MessageField(multi=True)
    p = parents

    global_ = BoolField(multi=True, long_name="global", short_name="g")
    g = global_

    world = MessageField()
    w = world

    bindPose = BoolField()
    bp = bindPose
