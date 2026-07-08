# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_create_face import VerticesField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


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


class PolyCreateFace(DG):
    __slots__ = ()

    NODE_TYPE = "polyCreateFace"

    output = DataMeshField(writable=False)
    out = output

    vertices = VerticesField(multi=True, default_value=(0.0, 0.0, 0.0))
    v = vertices

    loop = LongField(multi=True, default_value=0)
    l = loop

    subdivision = LongField(default_value=1, min_value=1, max_value=100, soft_max_value=10)
    s = subdivision

    texture = TextureEnumField(default_value=0)
    tx = texture

    uvSetName = DataStringField()
    uvs = uvSetName
