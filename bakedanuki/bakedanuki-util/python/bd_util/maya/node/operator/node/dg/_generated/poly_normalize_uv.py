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
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class NormalizeTypeEnumPlugOperator(
    EnumPlugOperator["NormalizeTypeEnumAttrOperator"]
):
    __slots__ = ()

    SEPARATE = 0
    COLLECTIVE = 1


class NormalizeTypeEnumAttrOperator(
    EnumAttrOperator[NormalizeTypeEnumPlugOperator]
):
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


class NormalizeDirectionEnumPlugOperator(
    EnumPlugOperator["NormalizeDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 0
    U = 1
    V = 2


class NormalizeDirectionEnumAttrOperator(
    EnumAttrOperator[NormalizeDirectionEnumPlugOperator]
):
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
    EnumField[
        NormalizeDirectionEnumAttrOperator, NormalizeDirectionEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = NormalizeDirectionEnumAttrOperator
    PLUG_CLS = NormalizeDirectionEnumPlugOperator


class GeneratedPolyNormalizeUV(DG):
    __slots__ = ()

    NODE_TYPE = "polyNormalizeUV"

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

    normalizeType = NormalizeTypeEnumField(default_value=1)
    nt = normalizeType

    preserveAspectRatio = BoolField(default_value=True)
    pa = preserveAspectRatio

    centerOnTile = BoolField(default_value=False)
    cot = centerOnTile

    normalizeDirection = NormalizeDirectionEnumField(default_value=0)
    nd = normalizeDirection
