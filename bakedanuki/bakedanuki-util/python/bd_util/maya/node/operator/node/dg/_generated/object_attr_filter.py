# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
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


class AttrTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ALL = 0
    WRITABLE = 1
    READABLE = 2
    KEYABLE = 3
    SCALE_ROTATE_TRANSLATE = 4
    WITH_EXPRESSIONS = 5
    WITH_ANIMATION_CURVES = 6
    DYNAMIC = 7
    HIDDEN = 8
    PUBLISHED = 9
    WITH_DRIVEN_KEYS = 10


class AttrTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ALL = 0
    WRITABLE = 1
    READABLE = 2
    KEYABLE = 3
    SCALE_ROTATE_TRANSLATE = 4
    WITH_EXPRESSIONS = 5
    WITH_ANIMATION_CURVES = 6
    DYNAMIC = 7
    HIDDEN = 8
    PUBLISHED = 9
    WITH_DRIVEN_KEYS = 10

    NAME_MAP = {
        ALL: "All",
        WRITABLE: "Writable",
        READABLE: "Readable",
        KEYABLE: "Keyable",
        SCALE_ROTATE_TRANSLATE: "Scale Rotate Translate",
        WITH_EXPRESSIONS: "With Expressions",
        WITH_ANIMATION_CURVES: "With Animation Curves",
        DYNAMIC: "Dynamic",
        HIDDEN: "Hidden",
        PUBLISHED: "Published",
        WITH_DRIVEN_KEYS: "With Driven Keys",
    }


class AttrTypeEnumField(
    EnumField[AttrTypeEnumAttrOperator, AttrTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AttrTypeEnumAttrOperator
    PLUG_CLS = AttrTypeEnumPlugOperator


class GeneratedObjectAttrFilter(DG):
    __slots__ = ()

    NODE_TYPE = "objectAttrFilter"

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

    attrType = AttrTypeEnumField(default_value=1)
    atyp = attrType
