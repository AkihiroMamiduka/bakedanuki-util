# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.matrix import DataMatrixField


class _GeneratedDagPose(DG):
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

    global_ = BoolField(multi=True, default_value=False, long_name="global", short_name="g")
    g = global_

    world = MessageField(writable=False)
    w = world

    bindPose = BoolField(default_value=False)
    bp = bindPose
