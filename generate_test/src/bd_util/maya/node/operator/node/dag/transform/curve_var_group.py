# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class CurveVarGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "curveVarGroup"

    maxCreated = LongField(default_value=-1)
    mc = maxCreated

    create_ = DataNurbsCurveField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = DataNurbsCurveField(multi=True, writable=False)
    l = local

    displaySmoothness = LongField(default_value=-1)
    ds = displaySmoothness
