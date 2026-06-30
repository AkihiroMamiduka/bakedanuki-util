# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.make_illustrator_curves import PositionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ...attr.define.std.dt.string import DataStringField


class MakeIllustratorCurves(DG):
    __slots__ = ()

    NODE_TYPE = "makeIllustratorCurves"

    illustratorFilename = DataStringField()
    ifn = illustratorFilename

    scaleFactor = FloatField()
    sf = scaleFactor

    reload = BoolField()
    rl = reload

    outputCurves = DataNurbsCurveField(multi=True)
    oc = outputCurves

    count = LongField(multi=True)
    c = count

    position = PositionField(multi=True)
    p = position

    tolerance = FloatField()
    tl = tolerance
