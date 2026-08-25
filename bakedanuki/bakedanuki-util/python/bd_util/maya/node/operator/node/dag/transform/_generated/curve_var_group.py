# coding: utf-8
from ..base_geometry_var_group import BaseGeometryVarGroup
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class GeneratedCurveVarGroup(BaseGeometryVarGroup):
    __slots__ = ()

    NODE_TYPE = "curveVarGroup"

    create_ = DataNurbsCurveField(
        multi=True, long_name="create", short_name="cr"
    )
    cr = create_

    local = DataNurbsCurveField(multi=True, writable=False)
    l = local

    displaySmoothness = LongField(default_value=-1)
    ds = displaySmoothness
