# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_append import VerticesField
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class TextureEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    NORMALIZED = 1
    UNITIZED = 2


class TextureEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    NORMALIZED = 1
    UNITIZED = 2

    NAME_MAP = {
        NONE: "none",
        NORMALIZED: "normalized",
        UNITIZED: "unitized",
    }


class TextureEnumField(
    EnumField[TextureEnumAttrOperator, TextureEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TextureEnumAttrOperator
    PLUG_CLS = TextureEnumPlugOperator


class _GeneratedPolyAppend(DG):
    __slots__ = ()

    NODE_TYPE = "polyAppend"

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

    vertices = VerticesField(multi=True, default_value=(0.0, 0.0, 0.0))
    v = vertices

    desc = LongField(multi=True, default_value=0)
    d = desc

    subdivision = LongField(default_value=1, min_value=1, max_value=100, soft_max_value=10)
    s = subdivision

    texture = TextureEnumField(default_value=0)
    tx = texture

    test2EdgeLoops = BoolField(default_value=True)
    tel = test2EdgeLoops
