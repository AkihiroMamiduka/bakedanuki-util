# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField


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


class _GeneratedObjectNameFilter(DG):
    __slots__ = ()

    NODE_TYPE = "objectNameFilter"

    child = BoolField(default_value=False)
    ch = child

    invert = BoolField(default_value=False)
    inv = invert

    inputList = TypedField()
    in_ = inputList

    outputList = TypedField()
    out = outputList

    annotation = DataStringField()
    an = annotation

    category = DataStringArrayField()
    cat = category

    disable = BoolField(default_value=False)
    dis = disable

    filterClass = FilterClassEnumField(default_value=2)
    fcls = filterClass

    regExp = DataStringField()
    rex = regExp

    nameStrings = DataStringArrayField()
    nstr = nameStrings

    attrName = BoolField(default_value=False)
    attr = attrName
