# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_text_curves import PositionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.string import DataStringField


class MakeTextCurves(DG):
    __slots__ = ()

    NODE_TYPE = "makeTextCurves"

    text = DataStringField()
    t = text

    font = DataStringField()
    f = font

    deprecatedFontName = BoolField()

    outputCurve = DataNurbsCurveField(multi=True)
    oc = outputCurve

    position = PositionField(multi=True)
    p = position

    count = LongField(multi=True)
    c = count
