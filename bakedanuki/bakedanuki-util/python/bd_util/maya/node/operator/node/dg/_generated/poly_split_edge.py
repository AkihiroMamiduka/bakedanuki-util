# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


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


class GeneratedPolySplitEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polySplitEdge"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    operation = OperationEnumField(default_value=1)
    op = operation

    cutUVs = BoolField(default_value=True)
    xuv = cutUVs

    maya2024 = BoolField(default_value=True)
    m24 = maya2024
