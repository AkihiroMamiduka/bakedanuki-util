# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.make_illustrator_curves import PositionField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedMakeIllustratorCurves(DG):
    __slots__ = ()

    NODE_TYPE = "makeIllustratorCurves"

    illustratorFilename = DataStringField()
    ifn = illustratorFilename

    scaleFactor = FloatField(default_value=1.0, min_value=0.0010000000474974513)
    sf = scaleFactor

    reload = BoolField(default_value=False)
    rl = reload

    outputCurves = DataNurbsCurveField(multi=True, writable=False)
    oc = outputCurves

    count = LongField(multi=True, default_value=0, writable=False)
    c = count

    position = PositionField(multi=True, default_value=(0.0, 0.0, 0.0), writable=False)
    p = position

    tolerance = FloatField(default_value=0.0010000000474974513, min_value=0.0, soft_min_value=0.0, soft_max_value=0.10000000149011612)
    tl = tolerance
