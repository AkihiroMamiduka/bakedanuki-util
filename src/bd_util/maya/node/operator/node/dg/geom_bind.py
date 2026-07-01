# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class GeomBind(DG):
    __slots__ = ()

    NODE_TYPE = "geomBind"

    skinClusters = MessageField()
    scs = skinClusters

    bindPose = MessageField()
    bp = bindPose

    falloff = DoubleField()
    fo = falloff

    maxInfluences = LongField()
    mi = maxInfluences

    gvResolution = LongField()
    gvr = gvResolution

    gvPostVoxelCheck = BoolField()
    gvpv = gvPostVoxelCheck
