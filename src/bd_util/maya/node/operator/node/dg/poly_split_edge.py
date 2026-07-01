# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NON_MINUS_MANIFOLD = 0
    MANIFOLD = 1


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NON_MINUS_MANIFOLD = 0
    MANIFOLD = 1

    NAME_MAP = {
        NON_MINUS_MANIFOLD: "Non-manifold",
        MANIFOLD: "Manifold",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class PolySplitEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polySplitEdge"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    operation = OperationEnumField()
    op = operation

    cutUVs = BoolField()
    xuv = cutUVs

    maya2024 = BoolField()
    m24 = maya2024
