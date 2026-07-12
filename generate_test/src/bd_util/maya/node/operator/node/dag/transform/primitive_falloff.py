# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.primitive_falloff import (
    NegativeSizeField,
    PositiveSizeField,
    RampField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.typed import TypedField


class VertexSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OBJECT_SPACE = 0
    WORLD_SPACE = 1


class VertexSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OBJECT_SPACE = 0
    WORLD_SPACE = 1

    NAME_MAP = {
        OBJECT_SPACE: "Object Space",
        WORLD_SPACE: "World Space",
    }


class VertexSpaceEnumField(
    EnumField[VertexSpaceEnumAttrOperator, VertexSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VertexSpaceEnumAttrOperator
    PLUG_CLS = VertexSpaceEnumPlugOperator


class PrimitiveEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SPHERE = 0
    PLANE = 1


class PrimitiveEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    SPHERE = 0
    PLANE = 1

    NAME_MAP = {
        SPHERE: "Sphere",
        PLANE: "Plane",
    }


class PrimitiveEnumField(
    EnumField[PrimitiveEnumAttrOperator, PrimitiveEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrimitiveEnumAttrOperator
    PLUG_CLS = PrimitiveEnumPlugOperator


class PrimitiveFalloff(Transform):
    __slots__ = ()

    NODE_TYPE = "primitiveFalloff"

    start = DoubleField(default_value=0.0)
    st = start

    end = DoubleField(default_value=1.0)
    ed = end

    useOriginalGeometry = BoolField(default_value=True)
    uo = useOriginalGeometry

    vertexSpace = VertexSpaceEnumField(default_value=0)
    vspc = vertexSpace

    primitive = PrimitiveEnumField(default_value=0)
    pmtv = primitive

    positiveSize = PositiveSizeField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0))
    ps = positiveSize
    positiveSizeX = positiveSize.positiveSizeX
    psx = positiveSizeX
    positiveSizeY = positiveSize.positiveSizeY
    psy = positiveSizeY
    positiveSizeZ = positiveSize.positiveSizeZ
    psz = positiveSizeZ

    negativeSize = NegativeSizeField(default_value=(1.0, 1.0, 1.0), min_value=(0.0, 0.0, 0.0))
    ns = negativeSize
    negativeSizeX = negativeSize.negativeSizeX
    nsx = negativeSizeX
    negativeSizeY = negativeSize.negativeSizeY
    nsy = negativeSizeY
    negativeSizeZ = negativeSize.negativeSizeZ
    nsz = negativeSizeZ

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction

    ramp = RampField(multi=True, default_value=(0.0, 0.0, 0.0))
    rmp = ramp
