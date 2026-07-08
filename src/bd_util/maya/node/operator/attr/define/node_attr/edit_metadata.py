# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.dt.string import DataStringField


class EditsPlugOperator(
    CompoundPlugOperator["EditsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("channelName", "cn"),
        ("channelEdits", "ce"),
    )

    channelName = DataStringField()
    cn = channelName

    channelEdits = CompoundField(multi=True)
    ce = channelEdits


class EditsAttrOperator(
    CompoundAttrOperator[EditsPlugOperator]
):
    __slots__ = ()

    channelName = DataStringField()
    cn = channelName

    channelEdits = CompoundField(multi=True)
    ce = channelEdits


class EditsField(
    CompoundField[EditsAttrOperator, EditsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EditsAttrOperator
    PLUG_CLS = EditsPlugOperator
