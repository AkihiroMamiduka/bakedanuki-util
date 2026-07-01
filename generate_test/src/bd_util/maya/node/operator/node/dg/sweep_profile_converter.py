# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sweep_profile_converter import (
    CachedLocalZCompoundArrayField,
    InObjectArrayField,
)
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class SweepProfileConverter(DG):
    __slots__ = ()

    NODE_TYPE = "sweepProfileConverter"

    sweepProfileData = TypedField()

    inObjectArray = InObjectArrayField(multi=True)

    outDebugMesh = DataMeshField()

    cachedLocalZCompoundArray = CachedLocalZCompoundArrayField(multi=True)

    cachedLocalZVector0 = DoubleField()

    cachedLocalZVector1 = DoubleField()

    cachedLocalZVector2 = DoubleField()
