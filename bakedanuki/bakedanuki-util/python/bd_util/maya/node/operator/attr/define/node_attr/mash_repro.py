# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)


class DisplayTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    MESH = 0
    PROXY = 1
    LOD = 2


class DisplayTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    MESH = 0
    PROXY = 1
    LOD = 2

    NAME_MAP = {
        MESH: "Mesh",
        PROXY: "Proxy",
        LOD: "Lod",
    }


class DisplayTypeEnumField(
    EnumField[DisplayTypeEnumAttrOperator, DisplayTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DisplayTypeEnumAttrOperator
    PLUG_CLS = DisplayTypeEnumPlugOperator


class InstancedGroupPlugOperator(
    CompoundPlugOperator["InstancedGroupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("instancedMesh", "inMesh"),
        ("proxyGroup", "proxyGroup"),
        ("displayType", "displayType"),
        ("groupMessage", "gmsg"),
        ("groupMatrix", "gmtx"),
    )

    instancedMesh = CompoundField(multi=True)
    inMesh = instancedMesh

    proxyGroup = CompoundField(multi=True)

    displayType = DisplayTypeEnumField(default_value=0)

    groupMessage = MessageField()
    gmsg = groupMessage

    groupMatrix = MatrixField()
    gmtx = groupMatrix


class InstancedGroupAttrOperator(
    CompoundAttrOperator[InstancedGroupPlugOperator]
):
    __slots__ = ()

    instancedMesh = CompoundField(multi=True)
    inMesh = instancedMesh

    proxyGroup = CompoundField(multi=True)

    displayType = DisplayTypeEnumField(default_value=0)

    groupMessage = MessageField()
    gmsg = groupMessage

    groupMatrix = MatrixField()
    gmtx = groupMatrix


class InstancedGroupField(
    CompoundField[InstancedGroupAttrOperator, InstancedGroupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InstancedGroupAttrOperator
    PLUG_CLS = InstancedGroupPlugOperator
