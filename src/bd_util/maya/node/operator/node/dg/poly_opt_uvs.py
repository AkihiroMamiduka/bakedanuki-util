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


class OptimizeAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FREE = 0
    VERTICAL = 1
    HORIZONTAL = 2


class OptimizeAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FREE = 0
    VERTICAL = 1
    HORIZONTAL = 2

    NAME_MAP = {
        FREE: "Free",
        VERTICAL: "Vertical",
        HORIZONTAL: "Horizontal",
    }


class OptimizeAxisEnumField(
    EnumField[OptimizeAxisEnumAttrOperator, OptimizeAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OptimizeAxisEnumAttrOperator
    PLUG_CLS = OptimizeAxisEnumPlugOperator


class PolyOptUvs(DG):
    __slots__ = ()

    NODE_TYPE = "polyOptUvs"

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

    iterations = LongField()
    i = iterations

    stoppingThreshold = FloatField()
    ss = stoppingThreshold

    areaWeight = FloatField()
    aw = areaWeight

    useScale = BoolField()
    us = useScale

    scale = FloatField()
    s = scale

    pinUvBorder = BoolField()
    pub = pinUvBorder

    pinSelected = BoolField()
    ps = pinSelected

    applyToShell = BoolField()
    as_ = applyToShell

    optimizeAxis = OptimizeAxisEnumField()
    oa = optimizeAxis

    globalBlend = FloatField()
    gb = globalBlend

    globalMethodBlend = FloatField()
    gmb = globalMethodBlend
