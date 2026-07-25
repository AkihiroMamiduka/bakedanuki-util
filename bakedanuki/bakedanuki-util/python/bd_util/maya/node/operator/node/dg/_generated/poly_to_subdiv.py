# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_to_subdiv import CachedUVsField
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class UvTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    KEEP_SUBD_UVS = 0
    INHERIT_UVS_FROM_POLY = 1
    NO_UVS_ON_SUBD = 2


class UvTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    KEEP_SUBD_UVS = 0
    INHERIT_UVS_FROM_POLY = 1
    NO_UVS_ON_SUBD = 2

    NAME_MAP = {
        KEEP_SUBD_UVS: "Keep Subd UVs",
        INHERIT_UVS_FROM_POLY: "Inherit UVs From Poly",
        NO_UVS_ON_SUBD: "No UVs On Subd",
    }


class UvTreatmentEnumField(
    EnumField[UvTreatmentEnumAttrOperator, UvTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvTreatmentEnumAttrOperator
    PLUG_CLS = UvTreatmentEnumPlugOperator


class _GeneratedPolyToSubdiv(DG):
    __slots__ = ()

    NODE_TYPE = "polyToSubdiv"

    inMesh = DataMeshField(readable=False)
    i = inMesh

    outSubdiv = TypedField(writable=False)
    o = outSubdiv

    maxPolyCount = LongField(default_value=1000, min_value=1, max_value=100000)
    mpc = maxPolyCount

    maxEdgesPerVert = LongField(default_value=32, min_value=2, max_value=255)
    me = maxEdgesPerVert

    applyMatrixToResult = BoolField(default_value=True)
    amr = applyMatrixToResult

    absolutePosition = BoolField(default_value=False)
    ap = absolutePosition

    uvTreatment = UvTreatmentEnumField(default_value=0)
    uvt = uvTreatment

    cachedUVs = CachedUVsField(multi=True)
    cuv = cachedUVs

    preserveVertexOrdering = BoolField(default_value=True)
    pvo = preserveVertexOrdering

    quickConvert = BoolField(default_value=True)
    qc = quickConvert
