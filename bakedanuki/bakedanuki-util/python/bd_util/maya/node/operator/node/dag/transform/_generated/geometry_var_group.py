# coding: utf-8
from ..base_geometry_var_group import BaseGeometryVarGroup
from .....attr.define.std.at.typed import TypedField


class GeneratedGeometryVarGroup(BaseGeometryVarGroup):
    __slots__ = ()

    NODE_TYPE = "geometryVarGroup"

    create_ = TypedField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = TypedField(multi=True, writable=False)
    l = local
