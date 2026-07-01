# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class FlipTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    HORIZONTAL = 0
    VERTICAL = 1


class FlipTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    HORIZONTAL = 0
    VERTICAL = 1

    NAME_MAP = {
        HORIZONTAL: "Horizontal",
        VERTICAL: "Vertical",
    }


class FlipTypeEnumField(
    EnumField[FlipTypeEnumAttrOperator, FlipTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlipTypeEnumAttrOperator
    PLUG_CLS = FlipTypeEnumPlugOperator


class PolyFlipUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyFlipUV"

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

    flipType = FlipTypeEnumField()
    ft = flipType

    local = BoolField()
    l = local

    cutUV = BoolField()
    cut = cutUV

    usePivot = BoolField()
    up = usePivot

    pivotU = DoubleField()
    pu = pivotU

    pivotV = DoubleField()
    pv = pivotV
