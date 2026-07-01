# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_to_subdiv import CachedUVsField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


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


class PolyToSubdiv(DG):
    __slots__ = ()

    NODE_TYPE = "polyToSubdiv"

    inMesh = DataMeshField()
    i = inMesh

    outSubdiv = TypedField()
    o = outSubdiv

    maxPolyCount = LongField()
    mpc = maxPolyCount

    maxEdgesPerVert = LongField()
    me = maxEdgesPerVert

    applyMatrixToResult = BoolField()
    amr = applyMatrixToResult

    absolutePosition = BoolField()
    ap = absolutePosition

    uvTreatment = UvTreatmentEnumField()
    uvt = uvTreatment

    cachedUVs = CachedUVsField(multi=True)
    cuv = cachedUVs

    preserveVertexOrdering = BoolField()
    pvo = preserveVertexOrdering

    quickConvert = BoolField()
    qc = quickConvert
