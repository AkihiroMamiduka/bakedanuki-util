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
from ....attr.define.std.dt.mesh import DataMeshField


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


class _GeneratedPolySubdFace(DG):
    __slots__ = ()

    NODE_TYPE = "polySubdFace"

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

    divisions = LongField(default_value=1, min_value=0, max_value=8, soft_max_value=4)
    dv = divisions

    divisionsU = LongField(default_value=1, min_value=1, max_value=250, soft_max_value=8)
    duv = divisionsU

    divisionsV = LongField(default_value=1, min_value=1, max_value=250, soft_max_value=8)
    dvv = divisionsV

    mode = ModeEnumField(default_value=0)
    m = mode

    subdMethod = SubdMethodEnumField(default_value=0)
    sbm = subdMethod
