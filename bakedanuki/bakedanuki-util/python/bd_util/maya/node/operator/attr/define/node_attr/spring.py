# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.typed import TypedField


class IdMappingPlugOperator(CompoundPlugOperator["IdMappingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("sortedId", "sid"),
        ("idIndex", "idix"),
    )

    sortedId = TypedField()
    sid = sortedId

    idIndex = TypedField()
    idix = idIndex


class IdMappingAttrOperator(CompoundAttrOperator[IdMappingPlugOperator]):
    __slots__ = ()

    sortedId = TypedField()
    sid = sortedId

    idIndex = TypedField()
    idix = idIndex


class IdMappingField(
    CompoundField[IdMappingAttrOperator, IdMappingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMappingAttrOperator
    PLUG_CLS = IdMappingPlugOperator
