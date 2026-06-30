# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveFromSubdivEdge(DG):
    __slots__ = ()

    NODE_TYPE = "curveFromSubdivEdge"

    inputSubdiv = TypedField()
    is_ = inputSubdiv

    minValue = DoubleField()
    min = minValue

    maxValue = DoubleField()
    max = maxValue

    relative = BoolField()
    r = relative

    outputCurve = DataNurbsCurveField()
    oc = outputCurve

    edgeIndexL = LongField(multi=True)
    eil = edgeIndexL

    edgeIndexR = LongField(multi=True)
    eir = edgeIndexR
