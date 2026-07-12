# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField


class GeometryVarGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "geometryVarGroup"

    maxCreated = LongField(default_value=-1)
    mc = maxCreated

    create_ = TypedField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = TypedField(multi=True, writable=False)
    l = local
