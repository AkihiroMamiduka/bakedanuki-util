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

    uvSetName = DataStringField()
    uvs = uvSetName

    flipType = FlipTypeEnumField(default_value=0)
    ft = flipType

    local = BoolField(default_value=True)
    l = local

    cutUV = BoolField(default_value=True)
    cut = cutUV

    usePivot = BoolField(default_value=False)
    up = usePivot

    pivotU = DoubleField(default_value=0.0)
    pu = pivotU

    pivotV = DoubleField(default_value=0.0)
    pv = pivotV
