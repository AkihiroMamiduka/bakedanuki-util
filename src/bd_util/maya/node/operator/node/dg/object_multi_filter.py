# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.string_array import DataStringArrayField


class FilterClassEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2


class FilterClassEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OTHER = 0
    BUILTIN = 1
    USER = 2

    NAME_MAP = {
        OTHER: "other",
        BUILTIN: "builtIn",
        USER: "user",
    }


class FilterClassEnumField(
    EnumField[FilterClassEnumAttrOperator, FilterClassEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterClassEnumAttrOperator
    PLUG_CLS = FilterClassEnumPlugOperator


class FilterTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ITEMFILTER = 0
    ITEMFILTERATTR = 1


class FilterTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ITEMFILTER = 0
    ITEMFILTERATTR = 1

    NAME_MAP = {
        ITEMFILTER: "itemFilter",
        ITEMFILTERATTR: "itemFilterAttr",
    }


class FilterTypeEnumField(
    EnumField[FilterTypeEnumAttrOperator, FilterTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterTypeEnumAttrOperator
    PLUG_CLS = FilterTypeEnumPlugOperator


class ObjectMultiFilter(DG):
    __slots__ = ()

    NODE_TYPE = "objectMultiFilter"

    child = BoolField()
    ch = child

    invert = BoolField()
    inv = invert

    inputList = TypedField()
    in_ = inputList

    outputList = TypedField()
    out = outputList

    annotation = DataStringField()
    an = annotation

    category = DataStringArrayField()
    cat = category

    disable = BoolField()
    dis = disable

    filterClass = FilterClassEnumField()
    fcls = filterClass

    resultList = TypedField()
    res = resultList

    filterType = FilterTypeEnumField()
    ftyp = filterType
