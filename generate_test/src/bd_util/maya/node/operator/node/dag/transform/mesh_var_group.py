# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.dt.mesh import DataMeshField


class MeshVarGroup(Transform):
    __slots__ = ()

    NODE_TYPE = "meshVarGroup"

    maxCreated = LongField(default_value=-1)
    mc = maxCreated

    create_ = DataMeshField(multi=True, long_name="create", short_name="cr")
    cr = create_

    local = DataMeshField(multi=True, writable=False)
    l = local
