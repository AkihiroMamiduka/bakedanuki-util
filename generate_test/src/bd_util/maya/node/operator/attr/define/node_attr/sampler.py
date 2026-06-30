# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.typed import TypedField


class FunctionPlugOperator(
    CompoundPlugOperator["FunctionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("function_Hidden", "fh"),
        ("function_Raw", "fr"),
        ("function_Inmap", "fi"),
        ("function_Outmap", "fo"),
        ("function_Default", "fd"),
    )

    function_Hidden = TypedField()
    fh = function_Hidden

    function_Raw = TypedField()
    fr = function_Raw

    function_Inmap = CompoundField()
    fi = function_Inmap

    function_Outmap = CompoundField()
    fo = function_Outmap

    function_Default = DoubleField()
    fd = function_Default


class FunctionAttrOperator(
    CompoundAttrOperator[FunctionPlugOperator]
):
    __slots__ = ()

    function_Hidden = TypedField()
    fh = function_Hidden

    function_Raw = TypedField()
    fr = function_Raw

    function_Inmap = CompoundField()
    fi = function_Inmap

    function_Outmap = CompoundField()
    fo = function_Outmap

    function_Default = DoubleField()
    fd = function_Default


class FunctionField(
    CompoundField[FunctionAttrOperator, FunctionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FunctionAttrOperator
    PLUG_CLS = FunctionPlugOperator

    function_Hidden = TypedField()
    fh = function_Hidden

    function_Raw = TypedField()
    fr = function_Raw

    function_Inmap = CompoundField()
    fi = function_Inmap

    function_Outmap = CompoundField()
    fo = function_Outmap

    function_Default = DoubleField()
    fd = function_Default
