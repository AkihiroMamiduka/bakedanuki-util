# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.custom_rig_default_mapping_node import OffsetField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    T = 0
    R = 1


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    T = 0
    R = 1

    NAME_MAP = {
        T: "T",
        R: "R",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class CustomRigDefaultMappingNode(DG):
    __slots__ = ()

    NODE_TYPE = "CustomRigDefaultMappingNode"

    type = TypeEnumField()
    t = type

    offset = OffsetField()
    o = offset
    offsetX = offset.offsetX
    ox = offsetX
    offsetY = offset.offsetY
    oy = offsetY
    offsetZ = offset.offsetZ
    oz = offsetZ

    matrixSource = MatrixField()
    ms = matrixSource

    destinationRig = MessageField()
    dr = destinationRig

    destinationSkeleton = MessageField()
    ds = destinationSkeleton

    identifier = LongField()
    id = identifier

    bodyPart = DataStringField()
    bp = bodyPart
