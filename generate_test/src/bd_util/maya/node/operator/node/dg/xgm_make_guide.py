# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.point_array import DataPointArrayField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


class XgmMakeGuide(DG):
    __slots__ = ()

    NODE_TYPE = "xgmMakeGuide"

    cGeom = DataPointArrayField()
    cgm = cGeom

    minCount = LongField()
    mct = minCount

    frame = DataVectorArrayField()
    frm = frame

    override = DataNurbsCurveField()
    ovr = override

    outputMesh = TypedField()
    os = outputMesh

    geomHitIn = BoolField()
    gi = geomHitIn

    toGuide = MessageField()
    tg = toGuide
