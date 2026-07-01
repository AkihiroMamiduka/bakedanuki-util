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
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class NormalizeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SEPARATE = 0
    COLLECTIVE = 1


class NormalizeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SEPARATE = 0
    COLLECTIVE = 1

    NAME_MAP = {
        SEPARATE: "Separate",
        COLLECTIVE: "Collective",
    }


class NormalizeTypeEnumField(
    EnumField[NormalizeTypeEnumAttrOperator, NormalizeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalizeTypeEnumAttrOperator
    PLUG_CLS = NormalizeTypeEnumPlugOperator


class NormalizeDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 0
    U = 1
    V = 2


class NormalizeDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 0
    U = 1
    V = 2

    NAME_MAP = {
        UV: "UV",
        U: "U",
        V: "V",
    }


class NormalizeDirectionEnumField(
    EnumField[NormalizeDirectionEnumAttrOperator, NormalizeDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalizeDirectionEnumAttrOperator
    PLUG_CLS = NormalizeDirectionEnumPlugOperator


class PolyNormalizeUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyNormalizeUV"

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

    normalizeType = NormalizeTypeEnumField()
    nt = normalizeType

    preserveAspectRatio = BoolField()
    pa = preserveAspectRatio

    centerOnTile = BoolField()
    cot = centerOnTile

    normalizeDirection = NormalizeDirectionEnumField()
    nd = normalizeDirection
