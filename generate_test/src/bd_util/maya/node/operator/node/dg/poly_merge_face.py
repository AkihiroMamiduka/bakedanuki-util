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


class MergeModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIRST = 0
    MIDDLE = 1
    LAST = 2
    PROJFIRST = 3
    PROJMIDDLE = 4
    PROJLAST = 5
    NONE = 6


class MergeModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIRST = 0
    MIDDLE = 1
    LAST = 2
    PROJFIRST = 3
    PROJMIDDLE = 4
    PROJLAST = 5
    NONE = 6

    NAME_MAP = {
        FIRST: "first",
        MIDDLE: "middle",
        LAST: "last",
        PROJFIRST: "projFirst",
        PROJMIDDLE: "projMiddle",
        PROJLAST: "projLast",
        NONE: "none",
    }


class MergeModeEnumField(
    EnumField[MergeModeEnumAttrOperator, MergeModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeModeEnumAttrOperator
    PLUG_CLS = MergeModeEnumPlugOperator


class PolyMergeFace(DG):
    __slots__ = ()

    NODE_TYPE = "polyMergeFace"

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

    mergeMode = MergeModeEnumField()
    mm = mergeMode

    useAreaTolerance = BoolField()
    uat = useAreaTolerance

    firstFacet = LongField()
    ff = firstFacet

    secondFacet = LongField()
    sf = secondFacet
