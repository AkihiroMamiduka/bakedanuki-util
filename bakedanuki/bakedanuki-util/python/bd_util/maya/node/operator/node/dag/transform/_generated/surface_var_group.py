# coding: utf-8
from ..base_geometry_var_group import BaseGeometryVarGroup
from .....attr.define.std.dt.nurbs_surface import DataNurbsSurfaceField


class GeneratedSurfaceVarGroup(BaseGeometryVarGroup):
    __slots__ = ()

    NODE_TYPE = "surfaceVarGroup"

    create_ = DataNurbsSurfaceField(
        multi=True, long_name="create", short_name="cr"
    )
    cr = create_

    local = DataNurbsSurfaceField(multi=True, writable=False)
    l = local
