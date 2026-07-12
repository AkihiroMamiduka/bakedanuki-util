# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class SurfaceVarGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "surfaceVarGroup"

    maxCreated = LongField(default_value=-1)
    mc = maxCreated

    create_ = DataNurbsSurfaceField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = DataNurbsSurfaceField(multi=True, writable=False)
    l = local
