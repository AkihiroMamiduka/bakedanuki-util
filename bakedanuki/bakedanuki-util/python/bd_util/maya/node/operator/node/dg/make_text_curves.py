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

    deprecatedFontName = BoolField(default_value=False)

    outputCurve = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurve

    position = PositionField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    count = LongField(multi=True, default_value=0, writable=False)
    c = count
