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


class ModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1


class ModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    QUADS = 0
    TRIANGLES = 1

    NAME_MAP = {
        QUADS: "quads",
        TRIANGLES: "triangles",
    }


class ModeEnumField(
    EnumField[ModeEnumAttrOperator, ModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModeEnumAttrOperator
    PLUG_CLS = ModeEnumPlugOperator


class SubdMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EXPONENTIAL = 0
    LINEAR = 1


class SubdMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EXPONENTIAL = 0
    LINEAR = 1

    NAME_MAP = {
        EXPONENTIAL: "Exponential",
        LINEAR: "Linear",
    }


class SubdMethodEnumField(
    EnumField[SubdMethodEnumAttrOperator, SubdMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SubdMethodEnumAttrOperator
    PLUG_CLS = SubdMethodEnumPlugOperator


class PolySubdFace(DG):
    __slots__ = ()

    NODE_TYPE = "polySubdFace"

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

    divisions = LongField()
    dv = divisions

    divisionsU = LongField()
    duv = divisionsU

    divisionsV = LongField()
    dvv = divisionsV

    mode = ModeEnumField()
    m = mode

    subdMethod = SubdMethodEnumField()
    sbm = subdMethod
