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

    sweepProfileData = TypedField(writable=False)

    inObjectArray = InObjectArrayField(multi=True, readable=False)

    outDebugMesh = DataMeshField(writable=False)

    cachedLocalZCompoundArray = CachedLocalZCompoundArrayField(multi=True)

    cachedLocalZVector0 = DoubleField()

    cachedLocalZVector1 = DoubleField()

    cachedLocalZVector2 = DoubleField()
