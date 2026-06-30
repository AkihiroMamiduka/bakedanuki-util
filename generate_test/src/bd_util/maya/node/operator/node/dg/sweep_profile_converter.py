# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sweep_profile_converter import (
    CachedLocalZCompoundArrayField,
    InObjectArrayField,
)
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class SweepProfileConverter(DG):
    __slots__ = ()

    NODE_TYPE = "sweepProfileConverter"

    sweepProfileData = TypedField()

    inObjectArray = InObjectArrayField(multi=True)

    outDebugMesh = DataMeshField()

    cachedLocalZCompoundArray = CachedLocalZCompoundArrayField(multi=True)

    # TODO: cachedLocalZCompoundArray.cachedLocalZVector0 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: cachedLocalZCompoundArray.cachedLocalZVector1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: cachedLocalZCompoundArray.cachedLocalZVector2 (attributeType=None, dataType=None) は未対応のため手動で追加してください
