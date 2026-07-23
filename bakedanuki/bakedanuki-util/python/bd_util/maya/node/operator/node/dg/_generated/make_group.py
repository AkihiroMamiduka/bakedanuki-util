# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class GroupTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    EDGE = 2
    FACET = 3
    UVMAP = 4


class GroupTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    VERTEX = 1
    EDGE = 2
    FACET = 3
    UVMAP = 4

    NAME_MAP = {
        NONE: "none",
        VERTEX: "vertex",
        EDGE: "edge",
        FACET: "facet",
        UVMAP: "uvMap",
    }


class GroupTypeEnumField(
    EnumField[GroupTypeEnumAttrOperator, GroupTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GroupTypeEnumAttrOperator
    PLUG_CLS = GroupTypeEnumPlugOperator


class _GeneratedMakeGroup(DG):
    __slots__ = ()

    NODE_TYPE = "makeGroup"

    inputGeometry = DataMeshField()
    ig = inputGeometry

    outputGeometry = DataMeshField(writable=False)
    og = outputGeometry

    groupType = GroupTypeEnumField(default_value=0)
    gt = groupType

    groupName = LongField(default_value=-1)
    gn = groupName

    elemList = TypedField()
    el = elemList

    inputComponents = TypedField()
    ic = inputComponents
