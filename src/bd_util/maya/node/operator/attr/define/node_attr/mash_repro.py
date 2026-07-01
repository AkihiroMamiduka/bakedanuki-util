# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.matrix import MatrixField
from ..std.at.message import MessageField


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

    instancedMesh = CompoundField()
    inMesh = instancedMesh

    proxyGroup = CompoundField()

    displayType = EnumField()

    groupMessage = MessageField()
    gmsg = groupMessage

    groupMatrix = MatrixField()
    gmtx = groupMatrix


class InstancedGroupAttrOperator(
    CompoundAttrOperator[InstancedGroupPlugOperator]
):
    __slots__ = ()

    instancedMesh = CompoundField()
    inMesh = instancedMesh

    proxyGroup = CompoundField()

    displayType = EnumField()

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
