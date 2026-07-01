# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.generic import GenericField
from ..std.dt.string import DataStringField


class ConnectionListPlugOperator(
    CompoundPlugOperator["ConnectionListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("connectionAttr", "ca"),
        ("connection", "c"),
    )

    connectionAttr = DataStringField()
    ca = connectionAttr

    connection = GenericField()
    c = connection


class ConnectionListAttrOperator(
    CompoundAttrOperator[ConnectionListPlugOperator]
):
    __slots__ = ()

    connectionAttr = DataStringField()
    ca = connectionAttr

    connection = GenericField()
    c = connection


class ConnectionListField(
    CompoundField[ConnectionListAttrOperator, ConnectionListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConnectionListAttrOperator
    PLUG_CLS = ConnectionListPlugOperator


class MultiParentListPlugOperator(
    CompoundPlugOperator["MultiParentListAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiParent", "mp"),
    )

    multiParent = GenericField()
    mp = multiParent


class MultiParentListAttrOperator(
    CompoundAttrOperator[MultiParentListPlugOperator]
):
    __slots__ = ()

    multiParent = GenericField()
    mp = multiParent


class MultiParentListField(
    CompoundField[MultiParentListAttrOperator, MultiParentListPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiParentListAttrOperator
    PLUG_CLS = MultiParentListPlugOperator
