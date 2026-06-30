# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.proximity_falloff import RampField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


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


class VolumeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    INSIDE = 1
    OUTSIDE = 2


class VolumeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    INSIDE = 1
    OUTSIDE = 2

    NAME_MAP = {
        NONE: "None",
        INSIDE: "Inside",
        OUTSIDE: "Outside",
    }


class VolumeEnumField(
    EnumField[VolumeEnumAttrOperator, VolumeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeEnumAttrOperator
    PLUG_CLS = VolumeEnumPlugOperator


class ProximityFalloff(DG):
    __slots__ = ()

    NODE_TYPE = "proximityFalloff"

    proximityGeometry = TypedField()
    pgm = proximityGeometry

    useBindTags = BoolField()
    ubt = useBindTags

    bindTagsFilter = DataStringField()
    btf = bindTagsFilter

    proximitySubset = DataStringField()
    pss = proximitySubset

    start = DoubleField()
    st = start

    end = DoubleField()
    ed = end

    ramp = RampField(multi=True)
    rmp = ramp

    useOriginalGeometry = BoolField()
    uo = useOriginalGeometry

    vertexSpace = VertexSpaceEnumField()
    vspc = vertexSpace

    volume = VolumeEnumField()
    vol = volume

    outputWeightFunction = TypedField()
    wft = outputWeightFunction
