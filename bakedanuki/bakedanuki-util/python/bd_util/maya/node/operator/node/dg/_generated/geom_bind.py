# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedGeomBind(DG):
    __slots__ = ()

    NODE_TYPE = "geomBind"

    skinClusters = MessageField()
    scs = skinClusters

    bindPose = MessageField()
    bp = bindPose

    falloff = DoubleField(default_value=0.2, min_value=0.0, max_value=1.0)
    fo = falloff

    maxInfluences = LongField(default_value=-1)
    mi = maxInfluences

    gvResolution = LongField(default_value=256, min_value=1)
    gvr = gvResolution

    gvPostVoxelCheck = BoolField(default_value=True)
    gvpv = gvPostVoxelCheck
