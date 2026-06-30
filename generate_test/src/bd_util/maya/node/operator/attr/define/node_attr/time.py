# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.typed import TypedField


class TimewarpInPlugOperator(
    CompoundPlugOperator["TimewarpInAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("timewarpIn_Hidden", "twih"),
        ("timewarpIn_Raw", "twir"),
        ("timewarpIn_Inmap", "twii"),
        ("timewarpIn_Outmap", "twio"),
    )

    timewarpIn_Hidden = TypedField()
    twih = timewarpIn_Hidden

    timewarpIn_Raw = TypedField()
    twir = timewarpIn_Raw

    timewarpIn_Inmap = CompoundField()
    twii = timewarpIn_Inmap

    timewarpIn_Outmap = CompoundField()
    twio = timewarpIn_Outmap


class TimewarpInAttrOperator(
    CompoundAttrOperator[TimewarpInPlugOperator]
):
    __slots__ = ()

    timewarpIn_Hidden = TypedField()
    twih = timewarpIn_Hidden

    timewarpIn_Raw = TypedField()
    twir = timewarpIn_Raw

    timewarpIn_Inmap = CompoundField()
    twii = timewarpIn_Inmap

    timewarpIn_Outmap = CompoundField()
    twio = timewarpIn_Outmap


class TimewarpInField(
    CompoundField[TimewarpInAttrOperator, TimewarpInPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TimewarpInAttrOperator
    PLUG_CLS = TimewarpInPlugOperator

    timewarpIn_Hidden = TypedField()
    twih = timewarpIn_Hidden

    timewarpIn_Raw = TypedField()
    twir = timewarpIn_Raw

    timewarpIn_Inmap = CompoundField()
    twii = timewarpIn_Inmap

    timewarpIn_Outmap = CompoundField()
    twio = timewarpIn_Outmap
