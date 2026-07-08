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


class NormalModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    REVERSE = 0
    PROPAGATE = 1
    CONFORM = 2
    REVANDEXTRACT = 3
    REVANDPROPAGATE = 4


class NormalModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    REVERSE = 0
    PROPAGATE = 1
    CONFORM = 2
    REVANDEXTRACT = 3
    REVANDPROPAGATE = 4

    NAME_MAP = {
        REVERSE: "reverse",
        PROPAGATE: "propagate",
        CONFORM: "conform",
        REVANDEXTRACT: "revAndExtract",
        REVANDPROPAGATE: "revAndPropagate",
    }


class NormalModeEnumField(
    EnumField[NormalModeEnumAttrOperator, NormalModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NormalModeEnumAttrOperator
    PLUG_CLS = NormalModeEnumPlugOperator


class PolyNormal(DG):
    __slots__ = ()

    NODE_TYPE = "polyNormal"

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

    normalMode = NormalModeEnumField(default_value=0)
    nm = normalMode

    userNormalMode = BoolField(default_value=True)
    unm = userNormalMode
