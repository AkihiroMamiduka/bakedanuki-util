# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_aov import OutputsField
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class TypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    INT = 1
    UINT = 2
    BOOL = 3
    FLOAT = 4
    RGB = 5
    RGBA = 6
    VECTOR = 7
    VECTOR2 = 9
    POINTER = 11


class TypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    INT = 1
    UINT = 2
    BOOL = 3
    FLOAT = 4
    RGB = 5
    RGBA = 6
    VECTOR = 7
    VECTOR2 = 9
    POINTER = 11

    NAME_MAP = {
        INT: "int",
        UINT: "uint",
        BOOL: "bool",
        FLOAT: "float",
        RGB: "rgb",
        RGBA: "rgba",
        VECTOR: "vector",
        VECTOR2: "vector2",
        POINTER: "pointer",
    }


class TypeEnumField(
    EnumField[TypeEnumAttrOperator, TypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TypeEnumAttrOperator
    PLUG_CLS = TypeEnumPlugOperator


class _GeneratedAiAOV(DG):
    __slots__ = ()

    NODE_TYPE = "aiAOV"

    enabled = BoolField(default_value=True)
    aoven = enabled

    name_ = DataStringField(long_name="name", short_name="aovn")
    aovn = name_

    type = TypeEnumField(default_value=6)
    aovt = type

    defaultValue = MessageField()
    dftv = defaultValue

    prefix = DataStringField()
    aovpre = prefix

    imageFormat = DataStringField()
    img = imageFormat

    filterType = DataStringField()
    fltr = filterType

    outputs = OutputsField(multi=True)
    out = outputs

    lightPathExpression = DataStringField()
    lpe = lightPathExpression

    lightGroups = BoolField(default_value=False)
    lg = lightGroups

    globalAov = BoolField(default_value=True)
    ga = globalAov

    lightGroupsList = DataStringField()
    lgl = lightGroupsList

    camera = DataStringField()
    cam = camera

    denoise = BoolField(default_value=False)
    den = denoise
