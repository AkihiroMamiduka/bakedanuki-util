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
from ....attr.define.std.dt.string import DataStringField


class OptimizeAxisEnumPlugOperator(EnumPlugOperator["OptimizeAxisEnumAttrOperator"]):
    __slots__ = ()

    FREE = 0
    VERTICAL = 1
    HORIZONTAL = 2


class OptimizeAxisEnumAttrOperator(EnumAttrOperator[OptimizeAxisEnumPlugOperator]):
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


class GeneratedPolyOptUvs(DG):
    __slots__ = ()

    NODE_TYPE = "polyOptUvs"

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

    iterations = LongField(default_value=100, min_value=0, soft_max_value=1000)
    i = iterations

    stoppingThreshold = FloatField(default_value=0.0010000000474974513, min_value=0.0, max_value=10.0, soft_max_value=1.0)
    ss = stoppingThreshold

    areaWeight = FloatField(default_value=1.0, min_value=0.0, max_value=10.0, soft_max_value=1.0)
    aw = areaWeight

    useScale = BoolField(default_value=False)
    us = useScale

    scale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    s = scale

    pinUvBorder = BoolField(default_value=False)
    pub = pinUvBorder

    pinSelected = BoolField(default_value=False)
    ps = pinSelected

    applyToShell = BoolField(default_value=False)
    as_ = applyToShell

    optimizeAxis = OptimizeAxisEnumField(default_value=0)
    oa = optimizeAxis

    globalBlend = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    gb = globalBlend

    globalMethodBlend = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    gmb = globalMethodBlend
