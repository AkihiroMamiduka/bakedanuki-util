# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.point_array import DataPointArrayField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class _GeneratedXgmMakeGuide(DG):
    __slots__ = ()

    NODE_TYPE = "xgmMakeGuide"

    cGeom = DataPointArrayField()
    cgm = cGeom

    minCount = LongField(default_value=0, min_value=1)
    mct = minCount

    frame = DataVectorArrayField()
    frm = frame

    override = DataNurbsCurveField()
    ovr = override

    outputMesh = TypedField(writable=False)
    os = outputMesh

    geomHitIn = BoolField(default_value=False)
    gi = geomHitIn

    toGuide = MessageField()
    tg = toGuide
