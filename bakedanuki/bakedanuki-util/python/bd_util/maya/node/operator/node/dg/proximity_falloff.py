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

    useBindTags = BoolField(default_value=False)
    ubt = useBindTags

    bindTagsFilter = DataStringField()
    btf = bindTagsFilter

    proximitySubset = DataStringField()
    pss = proximitySubset

    start = DoubleField(default_value=0.0)
    st = start

    end = DoubleField(default_value=1.0)
    ed = end

    ramp = RampField(multi=True, default_value=(0.0, 0.0, 0.0))
    rmp = ramp

    useOriginalGeometry = BoolField(default_value=True)
    uo = useOriginalGeometry

    vertexSpace = VertexSpaceEnumField(default_value=0)
    vspc = vertexSpace

    volume = VolumeEnumField(default_value=1)
    vol = volume

    outputWeightFunction = TypedField(writable=False)
    wft = outputWeightFunction
