# coding: utf-8
from ..base_geometry_var_group import BaseGeometryVarGroup
from .....attr.define.std.dt.mesh import DataMeshField


class GeneratedMeshVarGroup(BaseGeometryVarGroup):
    __slots__ = ()

    NODE_TYPE = "meshVarGroup"

    create_ = DataMeshField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = DataMeshField(multi=True, writable=False)
    l = local
