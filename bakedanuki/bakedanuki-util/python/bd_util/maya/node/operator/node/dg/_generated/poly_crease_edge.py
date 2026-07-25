# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CREASE = 0
    REMOVE = 1
    REMOVE_ALL = 2


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CREASE = 0
    REMOVE = 1
    REMOVE_ALL = 2

    NAME_MAP = {
        CREASE: "Crease",
        REMOVE: "Remove",
        REMOVE_ALL: "Remove All",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class _GeneratedPolyCreaseEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polyCreaseEdge"

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

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    crease = FloatField(multi=True, default_value=-1.0, min_value=0.0, soft_max_value=10.0)
    cr = crease

    inputVertexComponents = TypedField()
    ivc = inputVertexComponents

    creaseVertex = FloatField(multi=True, default_value=-1.0, min_value=0.0, soft_max_value=10.0)
    crv = creaseVertex

    operation = OperationEnumField(default_value=0)
    op = operation
