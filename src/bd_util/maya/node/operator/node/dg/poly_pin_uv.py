# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PIN = 0
    REMOVE = 1
    REMOVE_ALL = 2


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PIN = 0
    REMOVE = 1
    REMOVE_ALL = 2

    NAME_MAP = {
        PIN: "Pin",
        REMOVE: "Remove",
        REMOVE_ALL: "Remove All",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class PolyPinUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyPinUV"

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

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    uvSetName = DataStringField()
    uvs = uvSetName

    pin = FloatField(multi=True)
    pn = pin

    operation = OperationEnumField()
    op = operation
